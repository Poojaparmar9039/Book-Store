from django.shortcuts import render
from django.http import JsonResponse
from .models import Book
from .GoogleAiCode import AskAi

def Books(request):
    bookdata=Book.objects.all()
    return render(request,'Books.html',{'bookdata':bookdata})


CartList=[]
def AddToCart(request,id):
    book= Book.objects.get(id=id)
    CartList.append(book)
    return render(request,'AddToCart.html',{'CartList':CartList})


def DeleteFromCart(request,id):
    book = Book.objects.get(id=id)
    CartList.remove(book)
    return render(request, 'AddToCart.html', {'CartList': CartList})

BookData=""
def BookDetails(request,id):
    global BookData
    book = Book.objects.get(id=id)
    BookData = book
    return render(request,'BookDetails.html',{'book':book})


book=""
def ReadBook(request,id):
    global book
    book=Book.objects.get(id=id)
    return render(request,'ReadBook.html',{'book':book})

def SendToAi(request):
    Msg = request.GET.get("search_query")
    result =AskAi(f"I am Reading the book {BookData.bookname} and i am stuck in this kine ({Msg}, Explain this thing to a lany man with key points and a short story )")
    return render(request,'ReadBook.html',{'book':book,'result':result})