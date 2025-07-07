from django.shortcuts import render
from Books. models import Book

def Home(request):
    bookdata=Book.objects.all()
    print(bookdata)
    return render(request,'Home.html',{'bookdata':bookdata})
