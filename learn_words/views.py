from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from book import settings


def home(request):
    return render(request, 'home.html')


# @login_required
def profile(request):
    current_user = request.user
    current_words = current_user.words.filter(learned=False)
    finished_words = current_user.words.filter(learned=True)
    data = {'current': current_words, 'finished': finished_words}
    return render(request, 'profile.html', data)

def article(request):
    return render(request, 'article.html')

def register(request):
    if request.method =="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            text_content = 'Welcome to Learn Words! {}.'.format(user.username)
            html_content = '<h2>Thanks {} for signing up!</h2> <div>We hope you learn some amazing words!</div>'.format(user.username)
            msg = EmailMultiAlternatives("Welcome!", text_content, settings.DEFAULT_FROM_EMAIL, [user.email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {'form':form,})


