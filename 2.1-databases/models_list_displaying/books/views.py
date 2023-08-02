import datetime
import itertools
from time import strptime
from books.models import Book
from django.shortcuts import render
import json
from django.core.paginator import Paginator
from django.db.models import DateTimeField
from django.db.models.functions import Trunc
from books.converters import DateConverter


def books_view(request):
    template = 'books/books_list.html'
    db_book = Book.objects.order_by('pub_date')
    context = {'books': db_book}
    
    return render(request, template, context)


def about_book(request, date):
    template = 'books/about_book.html'
    book = Book.objects.get(pub_date=date)
    previous_page = Book.objects.filter(pub_date__lt=date).order_by('-pub_date').first()
    next_page = Book.objects.filter(pub_date__gt=date).order_by('pub_date').first()
    context = {
        'book': book,
        'previous_page': previous_page,
        'next_page': next_page,
    }
    return render(request, template, context=context)
