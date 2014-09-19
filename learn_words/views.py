from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from book import settings
from learn_words.forms import EmailUserCreationForm, NewWord
from learn_words.models import Word, Article


def home(request):
    return render(request, 'home.html')



def profile(request):
    current_user = request.user
    current_words = current_user.words.filter(learned=False)
    finished_words = current_user.words.filter(learned=True)
    data = {'current': current_words, 'finished': finished_words}
    return render(request, 'profile.html', data)


def article(request, word_id):
    word = Word.objects.get(id=word_id)
    data = Article.objects.filter(words=word_id)
    return render(request, 'article.html', {"articles": data, "word": word})


def register(request):
    if request.method == "POST":
        form = EmailUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # text_content = 'Welcome to Learn Words! {}.'.format(user.username)
            # html_content = '<h2>Thanks {} for signing up!</h2> <div>We hope you learn some amazing words!</div>'.format(user.username)
            # msg = EmailMultiAlternatives("Welcome!", text_content, settings.DEFAULT_FROM_EMAIL, [user.email])
            # msg.attach_alternative(html_content, "text/html")
            # msg.send()
            return redirect("login")
    else:
        form = EmailUserCreationForm()
    return render(request, "registration/register.html", {'form': form})

def newword(request):
    if request.method =="POST":
        form = NewWord(request.POST)
        if form.is_valid():
            current_word = Word.objects.create(word_name=form.cleaned_data['word'])
            current_word.users.add(request.user)
            current_word.articles = Article.objects.filter(text__icontains=current_word)
            # if current_word.articles.count == 0:
            #     error_message = "blah"
            #     return render(request, "newword.html", error_message)
            return redirect('profile')
    else:
        form = NewWord()
    return render(request, "newword.html", {'form': form})


def learned(request, word_id):
    word = Word.objects.get(id=word_id)
    word.learned = True
    word.save()
    return redirect('profile')