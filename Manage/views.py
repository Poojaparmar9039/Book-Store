from django.shortcuts import render
from Books.models import Book

def manage(request):
    return render(request,'Manage.html')


def Addbook(request):
    if request.method == 'POST':
        book = Book(
            poster=request.FILES.get('poster'),
            bookname=request.POST.get('bookname'),
            authorname=request.POST.get('authorname'),
            price=request.POST.get('price'),
            desc=request.POST.get('desc'),
            Bookpdf=request.FILES.get('Bookpdf'),
        )
        book.save()
        return render(request, 'Manage.html', {'message': 'Book added successfully'})
    return render(request, 'Manage.html', {'message': 'Book not added!'})


