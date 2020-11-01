from django.test import TestCase
from django.test import Client, TestCase
from .models import Student, RequestInformation, SentRequestInformation, DormInformation,CheckLists
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout

class UserTestCase(TestCase):

    def setUp(self):

        Student.objects.create(username="nonthawan1", name="nonthawan1",password="123456789", email= "2563@mail.com", phone="0123456789",year = 1)
        RequestInformation.objects.create(username="nonthawan1", name_req="12345")
        SentRequestInformation.objects.create(username="nonthawan1", name_sent="nonthawan1")
        DormInformation.objects.create(username="nonthawan1", name_dorm="1234", details_dorm="123",type_dorm="1123",price=4000)
        CheckLists.objects.create(username="nonthawan1", light=True,timetosleep="12",pet=True)
        self.logout = reverse("logout")
        self.login = reverse("login")

        # Create User
        self.user1 = User.objects.create_user(username="knanporn",password="Knanporn1",email="knanporn@mail.com")

        self.about = reverse("about")
        self.signup = reverse("signup")
        self.home = reverse("home")

    # Django Testing

    # Client Testing

    def test_login(self):
        pass
        c = Client()
        response = c.get('/login')
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        response = c.post('/login',{'username':'gift','password':'Gift1234'}, follow=True)
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

    def test_loginFalse(self):
        c = Client()
        response = c.post('/login',{'username':'gift','password':'Gift123'}, follow=True)
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        # self.assertTemplateUsed(response , '/login')
        # Check that the response message.
        self.assertEqual(response.context["message"],"กรุณากรอกรหัสผ่านที่ถูกต้อง")

        response = c.post('/login',{'username':'gif','password':'Gift1234'}, follow=True)
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        # self.assertTemplateUsed(response , '/login')
        # Check that the response message.
        self.assertEqual(response.context["message"],"กรุณากรอกรหัสผ่านที่ถูกต้อง")

    def test_add_signup(self):
        c = Client()
        response= c.get('/signup')
        self.assertEqual(response.status_code, 200)
        response = c.post(
            '/signup', data = {
                "username":"nonthawan",
                "name":"nonthawan",
                "password":"123456789",
                "email":"nonthawan@mail.com",
                "phone":"1234567890",
                "year":"First years"
            }
            )
        self.assertEqual(response.status_code, 200)

    def test_about(self):
        c = Client()
        c.force_login(self.user1)
        response = c.post(self.about)
        self.assertEqual(response.status_code, 200)

    def test_home(self):
        c = Client()
        c.force_login(self.user1)
        response = c.post(self.home)
        self.assertEqual(response.status_code, 200)

    # def test_logout(self):
    #     c = Client()
    #     c.force_login(self.user1)
    #     response = c.post(self.logout)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response , '/login')
    #     self.assertEqual(response.context["message"],"Logged out")

