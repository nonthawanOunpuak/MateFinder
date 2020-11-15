from django.test import TestCase
from django.test import Client, TestCase
from .models import Student, RequestInformation, SentRequestInformation, DormInformation
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
# from selenium import webdriver
# from django.contrib.staticfiles.testing import StaticLiveServerTestCase
# from selenium.webdriver.firefox.webdriver import WebDriver
# from django_selenium_test import selenium, SeleniumTestCase, PageElement
# from selenium.webdriver.common.by import By

class UserTestCase(TestCase):



    def setUp(self):

        # super().setUpClass()
        # self.selenium.implicitly_wait(10)
        # self.selenium = webdriver.Chrome()

        Student.objects.create(username="nonthawan1", name="nonthawan1",password="123456789", email= "2563@mail.com", phone="0123456789",year = 1)
        Student.objects.create(username="nonthawan2", name="nonthawan2",password="123456789", email= "2563@mail.com", phone="0123456789",year = 1)
        RequestInformation.objects.create(username="nonthawan1", name_req="12345")
        SentRequestInformation.objects.create(username="nonthawan1", name_sent="nonthawan1")
        DormInformation.objects.create(username="nonthawan1", name_dorm="1234", details_dorm="123",type_dorm="1123",price=4000,light=True,timetosleep="1 a.m",pet=True)

        # Create User
        self.user1 = User.objects.create_user(username="nonthawan1",password="123456789",email="3591@mail.com")

        self.about = reverse("about")
        self.signup = reverse("signup")
        self.home = reverse("home")
        self.logout = reverse("logout")
        self.login = reverse("login")
        self.post = reverse("post")
        self.store = reverse("store")
        self.homepage = reverse("homepage")
        # self.profile = reverse("profile/nonthawan1")

    # Django Testing
    
    # กรณีที่เราลบ post post นั้นจะหายไปจากหน้า homegage และ post นั้นจะถูกลบออกจาก database
    def test_delete_post(self):
        c = Client()
        response = c.get('/homepage')
        self.assertEqual(response.status_code, 200)
        userPost = DormInformation.objects.get(username="nonthawan1")
        userPost.delete()
        self.assertTemplateUsed(response , 'homepage.html')
        # self.assertEqual(response.context["message"],"Post Deleted Successfully")


    # Client Testing
    
    
    def test_login(self):
        pass
        c = Client()
        response = c.get('/login')
        self.assertEqual(response.status_code, 200)
        response = c.post('/login',{'username':'knanporn','password':'Kanaporn1'}, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_loginFalse(self):
        c = Client()
        response = c.post('/login',{'username':'knanporn','password':'Kanaporn1111'}, follow=True)

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response , 'login.html')

        # Check that the response message.
        self.assertEqual(response.context["message"],"Please enter the correct username and password.")


        response = c.post('/login',{'username':'knanporn','password':'Kanaporn1'}, follow=True)
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response , 'login.html')

        # Check that the response message.
        self.assertEqual(response.context["message"],"Please enter the correct username and password.")


    def test_add_signup(self):
        c = Client()
        response = c.get('/signup')
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

    def test_logout(self):
        c = Client()
        c.force_login(self.user1)
        response = c.get(self.logout)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response , 'login.html')

    def test_logout_form_about(self):
        c = Client()
        c.force_login(self.user1)
        response = c.get(self.about)
        self.assertEqual(response.status_code, 200)
        response = c.get(self.logout)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response , 'login.html')

    def test_post_and_show_post(self):
        c = Client()
        c.force_login(self.user1)
        response = c.post(self.home)
        self.assertEqual(response.status_code, 200)
        response = c.post('/store',{'username':'gift','name_dorm':'citypark','details_dorm':'-','type_dorm':'woman','price':7000,'light':True,'timetosleep':'3 a.m','pet':True}, follow=True)
        self.assertTemplateUsed(response , 'homepage.html')
        userPost = DormInformation.objects.filter(username="gift").get()
        self.assertEqual(userPost.username, 'gift')
        self.assertEqual(userPost.name_dorm, 'citypark')
        self.assertEqual(userPost.details_dorm, '-')
        self.assertEqual(userPost.type_dorm, 'woman')
        self.assertEqual(userPost.price, 7000)
        self.assertEqual(userPost.light, True)
        self.assertEqual(userPost.timetosleep, '3 a.m')
        self.assertEqual(userPost.pet, True)

    def test_profileInfo(self):
        c = Client()
        c.force_login(self.user1)
        response = c.get("/" + self.user1.username)
        self.assertEqual(response.status_code, 200)



