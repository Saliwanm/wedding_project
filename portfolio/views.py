from django.http import Http404
from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm


def portfolio(request):
    return render(request, 'portfolio/portfolio.html')


def movie(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    if movie is not None:
        return render(request, 'portfolio/portfolio.html', {'movie': movie})
    else:
        raise Http404('Movie does not exist')


def upload(request):
    if request.POST:
        form = MovieForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'portfolio/portfolio.html', {'form': MovieForm})