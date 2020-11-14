from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .models import Student, RequestInformation, SentRequestInformation, DormInformation,  User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import DormInformationForm


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def home(request):
    return render(request, 'home.html')


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "index.html")


def login(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "login.html", {
                "message": "กรุณากรอกรหัสผ่านที่ถูกต้อง"
            })
    return render(request, "login.html")


def logout(request):

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))
    else:

        # logout(request)
        return render(request, "login.html")


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            name = form.cleaned_data.get('name')
            password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            year = form.cleaned_data.get('year')
            User = authenticate(request, username=username, name=name,
                                password=password, email=email, phone=phone, year=year)
            login(User)
            return HttpResponseRedirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def profileInfo(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))
    else:
        profile = User.object.all().get(username=request.user.username)
        return render(request, "profile.html", {
            "Profile": profile
        })


def createDorm(request):
    return render(request, 'post.html')


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

    messages.success(request, "Post Added Successfully")
    return redirect('/homepage')


def viewPostDorm(request):
    print("viewPostDorm")
    return render(request, 'homepage.html', {
        "dorms": DormInformation.objects.all()
    })


def post(request):
    return render(request, 'post.html')


def profile(request, studentlink):
    student = Student.objects.get(username=studentlink)
    return render(request, 'profile.html', {
        "name": student.name,
        "email": student.email,
        "phone": student.phone,
        "year": student.year,
    }
    )


def deleteDorm(request, pk):
    d = DormInformation.objects.get(id=pk)
    d.delete()
    messages.success(request, "Post Deleted Successfully")
    return redirect('/home')

# def viewPostDorm(request):
#     if not request.user.is_authenticated:
#         return HttpResponseRedirect(reverse("homepage"))
#     else:
#         dorms = DormInformation.objects.all().get(username=request.user.username)
#         return render(request, 'homepage.html', {
#             "dorms": dorms,
#         })