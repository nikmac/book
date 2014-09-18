from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def profile(request):
    return render(request, 'profile.html')

def article(request):
    return render(request, 'article.html')

def register(request):
    # return render(request, 'register.html')
    pass


