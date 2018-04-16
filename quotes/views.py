from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Author,Quote
from .forms import QuoteForm, AuthorForm, SearchForm
import string

# Create your views here.

def index(request):
    authors = [a.author_name for a in Author.objects.all()]
    author_form = AuthorForm()
    quote_form = QuoteForm()
    search_quote_form = SearchForm()
    return render(request, 'quotes/index.html', {'authors': authors, 'author_form': author_form, 'quote_form': quote_form, 'search_quote_form': search_quote_form})


def quotes(request, author_id):
    author = Author.objects.get(id=author_id)
    quotes = author.quote_set.all()
    return render(request, 'quotes/quotes.html', {'author': author, 'quotes': quotes})

def post_author(request):
    form = AuthorForm(request.POST)
    if form.is_valid():
        form.save(commit = True)
    return HttpResponseRedirect('/quotes')

def post_quote(request):
    form = QuoteForm(request.POST)
    if form.is_valid():
        form.save(commit = True)
    return HttpResponseRedirect('/quotes')

def search_quote(request):
    form = SearchForm(request.POST)
    if form.is_valid():
        queryset = Quote.objects.all()
        text = form.cleaned_data['text']
        quotes = queryset.filter(quote_text__icontains = text)
    return render(request, 'quotes/search.html', {'quotes': quotes})

    