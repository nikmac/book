from django.contrib import admin
from learn_words.models import Word, Article
# Register your models here.


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    pass

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass




