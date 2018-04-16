from django import forms
from .models import Quote, Author

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['author_name']

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['quote_text', 'quote_author']

class SearchForm(forms.Form):
    text = forms.CharField(label='text', max_length=100)
    
