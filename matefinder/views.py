from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .models import Student, RequestInformation, SentRequestInformation, DormInformation, CheckLists
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "index.html")


def login(request):
    # if not request.user.is_authenticated:
    #     return HttpResponseRedirect(reverse("index"))
    # else:
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
        logout(request)
        return render(request, "login.html", {
            "message": "Logged out"
        })


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
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
