import datetime
import itertools
from time import strptime
from books.models import Book
from django.shortcuts import render
import json
from django.core.paginator import Paginator
from django.db.models import DateTimeField
from django.db.models.functions import Trunc
from datetime import date


def books_view(request):
    template = 'books/books_list.html'
    db_book = Book.objects.order_by('pub_date')
    context = {'books': db_book}
    
    return render(request, template, context)


def about_book(request, date):
    template = 'books/about_book.html'
    book = Book.objects.get(pub_date=date)
    all_books = Book.objects.all()
    paginator = Paginator(all_books, 1)
    page_number = request.GET.get('date')
    page = paginator.get_page(page_number)
    prev_page = Book.objects.filter(pub_date__lt=date).values_list('pub_date').first()
    next_page = Book.objects.filter(pub_date__lt=date).values_list('pub_date').first()
    context = {'book': book,
                'page': page,
                'prev': prev_page,
                'next': next_page}
    return render(request, template, context=context)
