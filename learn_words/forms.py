from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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


# class EditProfile(forms.ModelForm):
    # username = None
    # password1 = None
    # password2 = None

    # class Meta:
    #     model = User
    #     fields = (
    #         'username'
    #         'email',
    #         'first_name',
    #         'last_name',
    #     )