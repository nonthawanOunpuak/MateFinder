from django.shortcuts import render


def helloWorld(request):
    return render(request, 'home.html')


def contact(request):
    return render(request, 'contact.html')

# def aboutMe(request):
#     return render(request, 'aboutme.html')
