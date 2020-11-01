from django.shortcuts import render

def login(request):
    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')

def register(request):
    return render(request, 'register.html')
    
def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def profile(request):
    return render(request, 'profile.html')

def blog(request):
    return render(request, 'blog.html')





# def aboutMe(request):
#     return render(request, 'aboutme.html')
