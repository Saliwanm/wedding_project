from django.shortcuts import render


def photographers(request):
    return render(request, 'photographers/photographers.html')
