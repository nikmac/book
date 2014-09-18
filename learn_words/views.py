from django.contrib.auth.decorators import login_required
from django.shortcuts import render


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
    # return render(request, 'register.html')
    pass


