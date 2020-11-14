from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .models import Student, RequestInformation, SentRequestInformation, DormInformation, CheckLists, User
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


# def dormCreate(request):
#     if request.method == 'POST':
#         form = DormInformationForm(request.POST)
#         if form.is_valid():
#             name_dorm = form.cleaned_data['name_dorm']
#             details_dorm = form.cleaned_data['details_dorm']
#             type_dorm = form.cleaned_data['type_dorm']
#             price = form.cleaned_data['price_dorm']
#             form.save()
#             return HttpResponseRedirect('home')
#     else:
#         form = DormInformationForm()
#     return render(request, 'home.html', {'form': form})


def createDorm(request):
    return render(request, 'post.html')


def storeDorm(request):
    d = DormInformation()
    d.username = request.POST.get('username')
    d.name_dorm = request.POST.get('name_dorm')
    d.details_dorm = request.POST.get('details_dorm')
    d.type_dorm = request.POST.get('type_dorm')
    d.price = request.POST.get('price')
    d.save()
    messages.success(request, "Employee Added Successfully")
    return redirect('/home')

def dormCreate(request):
    if request.method == "POST":
        form = DormInformationForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('home')
            except:
                pass
    else:
        form = DormInformationForm()
    return render(request, 'home.html', {'form': form})


def viewPostDorm(request):
    print("viewPostDorm")
    return render(request, 'home.html', {
        "dorms" : DormInformation.objects.all()
    })


def post(request):
    return render(request, 'post.html')


