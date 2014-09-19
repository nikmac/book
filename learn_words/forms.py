from django import forms
from django.contrib.auth.forms import UserCreationForm
from learn_words.models import Word


class EmailUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=False)


class NewWord(forms.ModelForm):
    word = forms.CharField(required=True, max_length=40)


    class Meta:
        model = Word
        fields = ('word',)

