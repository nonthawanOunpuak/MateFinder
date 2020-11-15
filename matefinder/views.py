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


def about(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, 'about.html')


def contact(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, 'contact.html')


def home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, 'home.html')


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "index.html")


def login(request):
    print("login methodd")
    if request.method == "POST":
        username = request.POST["username"]
        print('uuuuuu    :', username)
        password = request.POST["password"]
        print('pwwww  :', password)
        user = authenticate(request, username=username, password=password)

        if user is not None:
            dj_login(request, user)
            return HttpResponseRedirect(reverse("homepage"))
        else:
            return render(request, "login.html", {
                "message": "Please enter the correct username and password."
            })
    return render(request, "login.html")


def logout(request):

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    else:
        return render(request, "login.html")


def createAccount(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, 'signup.html')


def storeAccount(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))
    else:
        s = Student()
        u = User()
        s.username = request.POST.get('username')
        s.name = request.POST.get('name')
        s.password = request.POST.get('password')
        s.email = request.POST.get('email')
        s.phone = request.POST.get('phone')
        s.year = request.POST.get('year')
        # u.username = s.username
        # u.email = s.email
        # u.password = s.password
        s.save()

        #user = Student.objects.filter(username=s.username)

        User.objects.create_user(username=s.username, password=s.password)

        messages.success(request, "Created Account Successfully")
        return redirect('/login')


def profileInfo(request):

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))
    else:
        profile = User.object.all().get(username=request.user.username)
        return render(request, "profile.html", {
            "Profile": profile
        })


def createDorm(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, 'post.html')


def storeDorm(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))
    else:
        d = DormInformation()
        d.username = request.POST.get('username')
        #d.name_owner = request.POST.get('name_owner')
        d.name_dorm = request.POST.get('name_dorm')
        d.details_dorm = request.POST.get('details_dorm')
        d.type_dorm = request.POST.get('type_dorm')
        d.price = request.POST.get('price')
        d.timetosleep = request.POST.get('timetosleep')
        d.pet = request.POST.get('pet')
        d.light = request.POST.get('light')
        d.save()

        messages.success(request, "Post Added Successfully")
        return redirect('/homepage')


# def viewPostDorm(request):
#     if not request.user.is_authenticated:
#         return HttpResponseRedirect(reverse("index"))
#     else:
#         return redirect('/homepage')


def viewPostDorm(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))
    else:
        print("viewPostDorm")
        return render(request, 'homepage.html', {
            "dorms": DormInformation.objects.all()
        })


def post(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    else:
        return render(request, 'post.html')


def profile_edit(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, 'profile_edit.html')


def profile_edited(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))
    else:
        s = Student(request.user.username)
        s.name = request.POST.get('name')
        s.phone = request.POST.get('phone')
        s.email = request.POST.get('email')
        s.year = request.POST.get('year')
        s.password = request.POST.get('password')
        s.save()

        messages.success(request, "Profile edited Successfully")
        return redirect('/home')


def profile(request, studentlink):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))
    else:
        student = Student.objects.get(username=studentlink)
        return render(request, 'profile.html', {
            "name": student.name,
            "email": student.email,
            "phone": student.phone,
            "year": student.year,
        }
        )


def deleteDorm(request, pk):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))
    else:
        d = DormInformation.objects.get(id=pk)
        d.delete()
        messages.success(request, "Post Deleted Successfully")
        return redirect('/home')
        return redirect('/homepage')


def editPost(request, pk):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))
    else:
        d = DormInformation.objects.get(id=pk)
        # return redirect('/post', {
        #     "d": d
        # })
        return render(request, 'edit.html', {
            "dorm": d
        })


def updatePost(request, pk):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))
    else:

        d = DormInformation.objects.get(id=pk)

        d.username = request.user.is_authenticated
        d.name_dorm = request.POST.get('name_dorm')
        d.details_dorm = request.POST.get('details_dorm')
        d.type_dorm = request.POST.get('type_dorm')
        d.price = request.POST.get('price')
        d.timetosleep = request.POST.get('timetosleep')
        d.pet = request.POST.get('pet')
        d.light = request.POST.get('light')
        d.save()

        messages.success(request, "Edited Successfully")
        return redirect('/homepage')
