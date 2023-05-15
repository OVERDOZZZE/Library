from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Books
from .forms import BookForm


def books(request):
    books_list = Books.objects.all()
    paginator = Paginator(books_list, 6)
    page = request.GET.get('page')
    books = paginator.get_page(page)
    context = {'books': books}
    return render(request, 'main/books.html', context=context)


def book_detail(request, id):
    book = Books.objects.get(id=id)
    context = {'book': book}
    return render(request, 'main/book_detail.html', context=context)


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm()
    return render(request, 'main/add_book.html', {'form': form})
