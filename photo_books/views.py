from django.shortcuts import render


def photo_books(request):
    return render(request, 'photo_books/photo_books.html')
