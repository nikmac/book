from django.contrib import admin
from learn_words.models import Word
# Register your models here.


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    pass