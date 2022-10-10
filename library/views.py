from django.shortcuts import render, redirect
from django.db.models import Q
from .forms import *
from .models import *
# Create your views here.

def bookList(request):
    if request.method == 'GET' and 'q' in request.GET:
        books = Book.objects.filter(
        Q(category__title__icontains=request.GET.get('q'))|
        Q(title__icontains=request.GET.get('q'))
    )
    elif request.method == 'GET' and 'a' in request.GET:
        books = Book.objects.filter(Q(author__contains=request.GET.get('a'))) 
    else:
        books = Book.objects.all()
    categories = Category.objects.all()
    context = {
        'books':books,
        'categories':categories
    }
    return render(request, 'library/book_list.html', context)

def bookDetail(request, pk):
    book = Book.objects.get(id=pk)
    categories = Category.objects.all()
    context = {
        'book':book,
        'categories':categories
    }
    return render(request, 'library/book_detail.html', context)

def EngbookList(request):
    books = Book.objects.filter(
        Q(language='en'),
    )
    categories = Category.objects.all()
    context = {
        'books':books,
        'categories':categories
    }
    return render(request, 'library/english_list.html', context)

def bookUpdate(request, pk):
    book = Book.objects.get(id=pk)
    form = BookForm(instance=book)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book-list')
    return render(request, 'library/book_update.html', {'form':form})

def newBooks(request):
    books = Book.objects.order_by('-writed')
    return render(request, 'library/new_books.html', {'books':books})

def feedBack(request):
    form = FeedBackForm()
    if request.method == 'POST':
        form = FeedBackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book-list')
    return render(request, 'library/feedback.html', {'form':form})

def frameworks(request):
    books = Book.objects.filter(
        category__framework=True)
    categories = Category.objects.all()
    print(categories)
    context = {
        'books':books,
        'categories':categories
    }
    return render(request, 'library/frameworks.html', context)

def lastBooks(request):
    books = Book.objects.order_by('-created')
    return render(request, 'library/last_books.html', {'books':books})

def aboutUs(request):
    return render(request, 'library/about_us.html')