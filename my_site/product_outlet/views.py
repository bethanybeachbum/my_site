from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Book
from django.db.models import Avg

# Create your views here.

def index(request):
    books = Book.objects.all().order_by("title")
    num_books = books.count()
    avr_rating = books.aggregate(Avg("rating"))
    
    return render(request, "product_outlet/index.html", {
                  "books" : books,
                  "total_number_of_books": num_books,
                  "average_rating": avr_rating
                  })
    
def book_detail(request, slug):
    # try:
    #     book = Book.objects.get(pk=id)
    # except:
    #     raise Http404()
    book = get_object_or_404(Book, slug=slug) # right side is the name of parameter, left side is the atribute name in the model (line 14)
    
    return render(request, "product_outlet/book_detail.html",{
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestseller": book.is_bestselling

    })