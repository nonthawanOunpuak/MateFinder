from django.test import Client, TestCase
from .models import Student, RequestInformation, SentRequestInformation, DormInformation
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout

class UserTestCase(TestCase):

    def setUp(self):

        self.s1 = Student.objects.create(username="nonthawan1", name="nonthawan1",password="123456789", email= "2563@mail.com", phone="0123456789",year = 1)
        self.s2 = Student.objects.create(username="nonthawan2", name="nonthawan2",password="123456789", email= "2563@mail.com", phone="0123456789",year = 1)
        self.r1 = RequestInformation.objects.create(username="nonthawan1", name_req="12345", status = "waiting", count = 0 , date = "2020-11-21 17:04:48.680158+00:00")
        self.r2 = RequestInformation.objects.create(username="gift", name_req="gift", status = "waiting", count = 0 , date = "2020-11-21 17:04:48.680158+00:00")
        self.sr1 = SentRequestInformation.objects.create(username="nonthawan1", name_sent="nonthawan2", status = "waiting", count = 0 , date = "2020-11-21 17:04:48.680158+00:00")
        self.sr2 = SentRequestInformation.objects.create(username="mai", name_sent="mai", status = "waiting", count = 0 , date = "2020-11-21 17:04:48.680158+00:00")
        self.d1 = DormInformation.objects.create(username="nonthawan1", name_dorm="1234", details_dorm="123",type_dorm="1123",price=4000,light=True,timetosleep="1 a.m",pet=True)
        self.d2 = DormInformation.objects.create(username="nonthawan2", name_dorm="1234", details_dorm="123",type_dorm="1123",price=4000,light=True,timetosleep="1 a.m",pet=True)

        # Create User
        self.user1 = User.objects.create_user(username="nonthawan1",password="123456789",email="2563@mail.com")
        self.user2 = User.objects.create_user(username="nonthawan2",password="123456789",email="2563@mail.com")

        self.about = reverse("about")
        self.signup = reverse("signup")
        self.logout = reverse("logout")
        self.login = reverse("login")
        self.post = reverse("post")
        self.store = reverse("store")
        self.homepage = reverse("homepage")
        self.profile_edit = reverse("profile_edit")
        self.edited = reverse("edited")
        self.request = reverse("request")

    # Django Testing

    def test_DormInformation(self):
        author = DormInformation.objects.get(username="nonthawan1")
        self.assertEqual(DormInformation.objects.filter(username="nonthawan1").count(), 1)
        expected_object_username = f'{author.id}, {author.username}, {author.name_dorm}, {author.details_dorm}, {author.type_dorm}, {author.price},{author.light}, {author.timetosleep},{author.pet}'
        self.assertEqual(expected_object_username, str(author))

    def test_Student(self):
        author = Student.objects.get(username="nonthawan1")
        self.assertEqual(DormInformation.objects.filter(username="nonthawan1").count(), 1)
        expected_object_username = f'{author.id}, {author.username}, {author.name},{author.password}, {author.email}, {author.phone}, {author.year}'
        self.assertEqual(expected_object_username, str(author))

    def test_RequestInformation(self):
        author = RequestInformation.objects.get(username="nonthawan1")
        self.assertEqual(DormInformation.objects.filter(username="nonthawan1").count(), 1)
        expected_object_username = f'{author.id}, {author.username}, {author.name_req}, {author.status}, {author.count}, {author.date}'
        self.assertEqual(expected_object_username, str(author))

    def test_SentRequestInformation(self):
        author = SentRequestInformation.objects.get(username="nonthawan1")
        self.assertEqual(DormInformation.objects.filter(username="nonthawan1").count(), 1)
        expected_object_username = f'{author.id}, {author.username}, {author.name_sent}, {author.status}, {author.count}, {author.date}'
        self.assertEqual(expected_object_username, str(author))

    def test_user_sent_and_user_post(self):
        user = SentRequestInformation.objects.get(username="nonthawan1")
        userPost = (str)(user.username)
        userSent = (str)(user.name_sent)
        self.assertTrue(userPost != userSent)

    def test_user_sent_and_user_post_not_valid(self):
        user = SentRequestInformation.objects.get(username="mai")
        userPost = (str)(user.username)
        userSent = (str)(user.name_sent)
        self.assertFalse(userPost != userSent)

    def test_user_request_and_user_post(self):
        user = RequestInformation.objects.get(username="nonthawan1")
        userPost = (str)(user.username)
        userRequest = (str)(user.name_req)
        self.assertTrue(userPost != userRequest)

    def test_user_request_and_user_post_not_valid(self):
        user = RequestInformation.objects.get(username="gift")
        userPost = (str)(user.username)
        userRequest = (str)(user.name_req)
        self.assertFalse(userPost != userRequest)

    # กรณีที่เราลบ post post นั้นจะหายไปจากหน้า homegage และ post นั้นจะถูกลบออกจาก database
    def test_delete_post(self):
        c = Client()
        response = c.get('/homepage')
        self.assertEqual(response.status_code, 200)
        userPost = DormInformation.objects.get(username="nonthawan1")
        self.assertEqual(DormInformation.objects.filter(username="nonthawan1").count(), 1)
        userPost.delete()
        self.assertEqual(DormInformation.objects.filter(username="nonthawan1").count(), 0)
        self.assertTemplateUsed(response , 'homepage.html')

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
            '/signup',{
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

    # def test_profileInfo(self):


    def  test_createDorm(self):
        c = Client()
        c.force_login(self.user1)
        response = c.get(self.post)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response , 'post.html')

    def test_storeDorm(self):
        c = Client()
        c.force_login(self.user1)
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
    def test_post(self):
        c = Client()
        c.force_login(self.user1)
        response = c.post(self.homepage)
        self.assertEqual(response.status_code, 200)
        response = c.post(self.post)
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
        author = DormInformation.objects.get(username='gift')
        self.assertEqual(DormInformation.objects.filter(username='gift').count(), 1)
        expected_object_username = f'{author.id}, {author.username}, {author.name_dorm}, {author.details_dorm}, {author.type_dorm}, {author.price},{author.light}, {author.timetosleep},{author.pet}'
        self.assertEqual(expected_object_username, str(author))

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
        response = c.post(self.profile_edit)
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
        author = Student.objects.get(username="nonthawan1")
        self.assertEqual(DormInformation.objects.filter(username="nonthawan1").count(), 1)
        expected_object_username = f'{author.id}, {author.username}, {author.name},{author.password}, {author.email}, {author.phone}, {author.year}'
        self.assertEqual(expected_object_username, str(author))

    #เมื่อ login เข้ามาได้แล้วเราสามารถแก้ไข post ของเราได้
    def test_editPost(self):
        c = Client()
        c.force_login(self.user1)
        response = c.post(self.homepage)
        self.assertEqual(response.status_code, 200)
        response = c.post('/updatePost/'+ self.user1.username,{
            'name_dorm':'TU-dome',
            'details_dorm':'12345',
            'type_dorm':'man',
            'price':7500,
            'light':True,
            'timetosleep':'4 a.m',
            'pet':True
        }, follow=True)
        response = c.post(self.homepage)
        self.assertEqual(response.status_code, 200)
        author = DormInformation.objects.get(username=self.user1.username)
        self.assertEqual(DormInformation.objects.filter(username=self.user1.username).count(), 1)
        expected_object_username = f'{author.id}, {author.username}, {author.name_dorm}, {author.details_dorm}, {author.type_dorm}, {author.price},{author.light}, {author.timetosleep},{author.pet}'
        self.assertEqual(expected_object_username, str(author))

    def test_request_page(self):
        c = Client()
        c.force_login(self.user1)
        response = c.post(self.homepage)
        self.assertEqual(response.status_code, 200)
        response = c.post(self.request)
        self.assertEqual(response.status_code, 200)

    def test_request(self):
        c = Client()
        c.force_login(self.user1)
        response = c.post(self.homepage)
        self.assertEqual(response.status_code, 200)
        response = c.post('/sentReq/'+ self.user2.username)
        self.assertEqual(RequestInformation.objects.filter(username=self.user1.username).count(), 1)
        self.assertEqual(SentRequestInformation.objects.filter(username=self.user1.username).count(), 1)

    def test_acceptReq(self):
        c = Client()
        c.force_login(self.user1)
        response = c.post(self.homepage)
        self.assertEqual(response.status_code, 200)
        response = c.post('/accept/'+ self.user2.username)
        response = c.post(self.request)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response , 'request.html')
        # userAccept = RequestInformation.objects.get(username=self.user1.username)
        # userAccept.status = "confirm"
        # userAccept.save()
        # status = (str)(userAccept.status)
        # self.assertTrue(status == "confirm")

    def test_storeAccout(self) :
        c = Client()
        response = c.post(reverse('storeAccount'),{'username':'test1','name':'name1','password':'1234','email':'test@matfinder.com','phone':'0818111111','year':'2'})
        student = Student.objects.get(username='test1')
        self.assertEqual(response.status_code,302)

    def redirect(self , res):
        return dict(res.items())['Location']

    def test_post_1(self):
        """ check test_post_1 """
        c = Client()
        c.force_login(self.user1)
        response = c.post(reverse('post'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'post.html')

    def test_post_2(self):
        """ check test_post_2 """
        c = Client()
        # c.force_login(self.user1)
        response = c.post(reverse('post'))
        self.assertEqual(response.status_code,200)
        # self.assertTemplateUsed(response,'post.html')

    def test_deleteDorm(self):
        c = Client()
        c.force_login(self.user1)
        response = c.post('/delete/'+ self.user1.username)
        self.assertEqual(DormInformation.objects.filter(username="nonthawan1").count(), 1)
