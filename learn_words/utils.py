from learn_words.models import Word, Article
from bs4 import BeautifulSoup
import requests, re

def test():
    book = requests.get('http://www.gutenberg.org/files/98/98-h/98-h.htm')
    data = book.text
    book_text = BeautifulSoup(data)
    # paragraphs = book_text.find_all("<p>")
    for paragraph in book_text.find_all("p"):
        print '=========================================================='

        print paragraph.get_text()

    # for word in book_text



    # article = Article.objects.create(paragraph)