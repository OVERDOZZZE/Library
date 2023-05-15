from django import forms
from .models import Author, Publisher, Books


class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['title', 'author', 'publisher', 'publication_date', 'cover_photo']
        widgets = {
            'author': forms.Select(attrs={'class': 'form-select'},
                                   choices=[('', 'Not Selected')] + list(Author.objects.values_list('id', 'name'))),
            'publisher': forms.Select(attrs={'class': 'form-select'}, choices=[('', 'Not Selected')] + list(
                Publisher.objects.values_list('id', 'name'))),
            'cover_photo': forms.ClearableFileInput(attrs={'class': 'form-control-file'})
        }
