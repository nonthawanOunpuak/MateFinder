from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, logout, login as dj_login
from .models import Student, RequestInformation, SentRequestInformation, DormInformation,  User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import DormInformationForm
from .forms import StudentForm

# About's page


def about(request):
    return render(request, 'about.html')

# Contact's page


def contact(request):
    return render(request, 'contact.html')

# Home's page


def home(request):
    return render(request, 'home.html')

# Homepage's page


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "homepage.html")

# Login page


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            dj_login(request, user)
            return HttpResponseRedirect(reverse("homepage"))
        else:
            return render(request, "login.html", {
                "message": "Please enter the correct username and password."
            })
    return render(request, "login.html")

# Logout page


def logout(request):
    return render(request, "login.html")

# Signup page


def createAccount(request):
    return render(request, 'signup.html')

# create account when fill out of field in signup page and then click create account
# the server will be call storeAccount method for keep acc.


def storeAccount(request):
    s = Student()
    u = User()
    s.username = request.POST.get('username')
    s.name = request.POST.get('name')
    s.password = request.POST.get('password')
    s.email = request.POST.get('email')
    s.phone = request.POST.get('phone')
    s.year = request.POST.get('year')
    s.save()
    User.objects.create_user(username=s.username, password=s.password)
    return redirect('/login')

# get the Information's Profile


def profileInfo(request):
    profile = User.object.all().get(username=request.user.username)
    return render(request, "profile.html", {
        "Profile": profile
    })

# Post's page


def createDorm(request):
    return render(request, 'post.html')

# Create post method


def storeDorm(request):
    d = DormInformation()
    d.username = request.POST.get('username')
    d.name_dorm = request.POST.get('name_dorm')
    d.details_dorm = request.POST.get('details_dorm')
    d.type_dorm = request.POST.get('type_dorm')
    d.price = request.POST.get('price')
    d.timetosleep = request.POST.get('timetosleep')
    d.pet = request.POST.get('pet')
    d.light = request.POST.get('light')
    d.save()
    return redirect('/homepage')

# Showing all post of dorm in timeline


def viewPostDorm(request):
    return render(request, 'homepage.html', {
        "dorms": DormInformation.objects.all(),
    })


def post(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, 'post.html')

# require fields of profile


def profile_edit(request):
    student = Student.objects.get(username=request.user.username)
    return render(request, 'profile_edit.html', {
        "name": student.name,
        "email": student.email,
        "phone": student.phone,
        "year": student.year,
    })

# editing


def profile_edited(request):
    Student.objects.filter(username=request.user.username).update(
        name=request.POST.get('name'),
        phone=request.POST.get('phone'),
        email=request.POST.get('email'),
        year=request.POST.get('year')
    )
    return redirect('homepage')

# show profile for each student's user


def profile(request, studentlink):
    student = Student.objects.get(username=studentlink)
    return render(request, 'profile.html', {
        "name": student.name,
        "email": student.email,
        "phone": student.phone,
        "year": student.year,
    }
    )

# delete post


def deleteDorm(request, pk):
    d = DormInformation.objects.get(id=pk)
    d.delete()
    return redirect('/homepage')

# edit post


def editPost(request, pk):
    d = DormInformation.objects.get(id=pk)
    return render(request, 'edit.html', {
        "dorm": d
    })

# upate post


def updatePost(request, pk):
    d = DormInformation.objects.get(id=pk)
    d.name_dorm = request.POST.get('name_dorm')
    d.details_dorm = request.POST.get('details_dorm')
    d.type_dorm = request.POST.get('type_dorm')
    d.price = request.POST.get('price')
    d.timetosleep = request.POST.get('timetosleep')
    d.pet = request.POST.get('pet')
    d.light = request.POST.get('light')
    d.save()
    return redirect('/homepage')

# ตอนกดขอ join
# db ถูกสร้างสองฝั่ง คือ sentRequest (username-mine) ของเรา กับ Request ของเขา (เราจะเป็น name_req)

# when you sent request to someone. the server will be call this method


def sentRequestInformation(request, pk):

    d = DormInformation.objects.get(id=pk)
    #dusername = d.username
    # d.username = request.GET.get('username')
    # user ของคนที่เราไปขอ
    newSent = SentRequestInformation()
    newSent.name_sent = d.username
    newSent.username = request.user.username
    newSent.status = "waiting"
    newSent.count = 1
    newSent.save()

    newReq = RequestInformation()
    newReq.username = d.username
    newReq.name_req = request.user.username
    newReq.count = 1
    newReq.status = "waiting"
    newReq.save()

    objReq = RequestInformation.objects.all()
    objSent = SentRequestInformation.objects.all()
    return HttpResponseRedirect(reverse('homepage'))
    # return render(request, 'request.html', {
    #     "req": objReq,
    #     "sent": objSent,
    # })
    # พอกด join แล้วเปลี่ยนเป็น waiting อัตโนมัติเลย แบบไม่ต้องเช็คจาก backend
    # จริงๆอันนี้อยู่หน้า homepage ก็ได้ ใช้ def request ส่งมาเอา
    # return render(request, 'homepage.html', {
    #     "req": objReq,
    #     "sent": objSent,
    # })

# request feature showing

# accept method for request


def acceptReq(request, pk):
    req = RequestInformation.objects.get(id=pk)
    req.status = "joined"
    req.save()
    #s = SentRequestInformation()
    print("accept   : ", request.user.username)
    #sent = SentRequestInformation()
    sent = SentRequestInformation.objects.filter(
        date=req.date, username=request.user.username).update(
        status="confirm"
    )

    objAcc = RequestInformation.objects.all()

    # พอเด้งไปหน้า homepage ปุ่มจะเปลี่ยนเป็น join
    # ให้ get acc.name_req ขึ้นมาแล้วหาว่าโพสไหนชื่อตรง
    # แล้วก็ get acc.status ออกมาเช็คว่า == "joined" มั้ย แล้วเปลี่ยนปุ่ม
    return redirect('/request')
    # return render(request, 'homepage.html',
    #               # {
    #               #     "acc": objAcc,
    #               # }
    #               )

# get request's info


def request(request):
    # จะดึงข้อมูลละก็ข้อคาม status มาเช็ค ถ้า == 'confirm' จะเป็น message บอก
    obj = RequestInformation.objects.all()
    objSentReq = SentRequestInformation.objects.all()
    return render(request, 'request.html', {
        'obj': obj,
        'objSentReq': objSentReq
    })

# decline method for a request


def declineReq(request, pk):
    o = RequestInformation.objects.get(id=pk)
    o.delete()
    return redirect('/request')

# cancel Request when you change minds.


def cancleReq(request, pk):
    o = SentRequestInformation.objects.get(id=pk)
    o.delete()
    return redirect('/request')
