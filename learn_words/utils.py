from learn_words.models import Word, Article
from bs4 import BeautifulSoup
import requests, re

def get_article(website):
    book = requests.get(website)
    data = book.text
    book_text = BeautifulSoup(data)
    for paragraph in book_text.find_all("p"):
        words = paragraph.get_text()
        Article.objects.create(text=words)

   # 'http://www.gutenberg.org/files/98/98-h/98-h.htm'