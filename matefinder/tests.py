from django.test import TestCase
from django.test import Client, TestCase
from .models import Student, RequestInformation, SentRequestInformation, DormInformation
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout

class UserTestCase(TestCase):

    def setUp(self):

        Student.objects.create(username="nonthawan1", name="nonthawan1",password="123456789", email= "2563@mail.com", phone="0123456789",year = 1)
        Student.objects.create(username="nonthawan2", name="nonthawan2",password="123456789", email= "2563@mail.com", phone="0123456789",year = 1)
        RequestInformation.objects.create(username="nonthawan1", name_req="12345")
        SentRequestInformation.objects.create(username="nonthawan1", name_sent="nonthawan1")
        DormInformation.objects.create(username="nonthawan1", name_dorm="1234", details_dorm="123",type_dorm="1123",price=4000,light=True,timetosleep="1 a.m",pet=True)

        # Create User
        self.user1 = User.objects.create_user(username="nonthawan1",password="123456789",email="3591@mail.com")

        self.about = reverse("about")
        self.signup = reverse("signup")
        self.logout = reverse("logout")
        self.login = reverse("login")
        self.post = reverse("post")
        self.store = reverse("store")
        self.homepage = reverse("homepage")
        self.profile_edit = reverse("profile_edit")
        self.edited = reverse("edited")

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

    #กรณีที่เรา login และใส่ username และ passwork ที่ถูกต้องเราจะสามารถ login ได้และเข้าสู่ระบบได้สำเร็จ
    def test_login(self):
        pass
        c = Client()
        response = c.get('/login')
        self.assertEqual(response.status_code, 200)
        response = c.post('/login',{'username':'knanporn','password':'Kanaporn1'}, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_loginFalse(self):
        c = Client()
        #กรณีที่ login ไม่สำเร็จเพราะใส่ password ผิด จะมีข้อความแจ้งเตือนและให้ทำการ login ใหม่
        response = c.post('/login',{'username':'knanporn','password':'Kanaporn1111'}, follow=True)

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response , 'login.html')

        # Check that the response message.
        self.assertEqual(response.context["message"],"Please enter the correct username and password.")

        #กรณีที่ login ไม่สำเร็จเพราะใส่ username ผิด จะมีข้อความแจ้งเตือนและให้ทำการ login ใหม่
        response = c.post('/login',{'username':'knanpornn','password':'Kanaporn1'}, follow=True)
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response , 'login.html')

        # Check that the response message.
        self.assertEqual(response.context["message"],"Please enter the correct username and password.")

    #กรณีที่มีการเข้ามาใช้งานครั้งแรกจะต้องมีการสมัครก่อนใช้งานและกรอกข้อมูลต่าง ๆ
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

    #เมื่อ login สำเร็จจะมีสิทธิเข้าถึงหน้า about
    def test_about(self):
        c = Client()
        c.force_login(self.user1)
        response = c.post(self.about)
        self.assertEqual(response.status_code, 200)

    #เมื่อ login สำเร็จจะมีสิทธิเข้าจึงหน้า homepage
    def test_homepage(self):
        c = Client()
        c.force_login(self.user1)
        response = c.post(self.homepage)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response , 'homepage.html')

    #เมื่อ login เข้ามาได้แล้ว เราสามารถ logout ออกมาได้และจะกลับมาที่หน้า login
    def test_logout(self):
        c = Client()
        c.force_login(self.user1)
        response = c.get(self.logout)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response , 'login.html')

    #เมื่อเรา login เข้ามาได้เราสามารถเข้าถึงหน้า about และสามารถ logout ออกจากหน้า about ได้และจะกลับมาที่หน้า login
    def test_logout_form_about(self):
        c = Client()
        c.force_login(self.user1)
        response = c.get(self.about)
        self.assertEqual(response.status_code, 200)
        response = c.get(self.logout)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response , 'login.html')

    #เมื่อ login เข้ามาได้สำเร็จ เรามีสิทธิที่จะเข้าถึงหน้า homepage และมีสิทธิในการ post ข้อมูลต่าง ๆ
    def test_post_and_show_post(self):
        c = Client()
        c.force_login(self.user1)
        response = c.post(self.homepage)
        self.assertEqual(response.status_code, 200)
        response = c.post('/store',{
            'username':'gift',
            'name_dorm':'citypark',
            'details_dorm':'-',
            'type_dorm':'woman',
            'price':7000,
            'light':True,
            'timetosleep':'3 a.m',
            'pet':True
        }, follow=True)
        self.assertTemplateUsed(response, 'homepage.html')

    #เมื่อ login เข้ามาได้สำเร็จ เราสามารถดูข้อมูลส่วนตัวของเราได้
    def test_profileInfo(self):
        c = Client()
        c.force_login(self.user1)
        response = c.get("/" + self.user1.username)
        self.assertEqual(response.status_code, 200)
        response = c.get("/" + self.user1.username)
        response = c.post(self.profile_edit)
        self.assertEqual(response.status_code, 200)

    #เมื่อ login เข้ามาได้สำเร็จเราสามารถแก้ไขข้อมูลส่วนตัวของเราได้
    def test_edit_profile(self):
        c = Client()
        c.force_login(self.user1)
        response = c.get("/" + self.user1.username)
        self.assertEqual(response.status_code, 200)
        response = c.post('/edited',{
            'name':'mai',
            'phone':'1111111111',
            'email':'124@mail.com',
            'year':3
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response , 'homepage.html')
        response = c.get("/" + self.user1.username)
        self.assertEqual(response.status_code, 200)

