from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, FormView

from viewer.forms import MovieForm
from viewer.models import Movie, Actor


def hello(request, mood):
    return HttpResponse(f'Hello, {mood} world!')


def goodbye(request):
    mood = request.GET.get('mood', '')
    return HttpResponse(f'Goodbye, {mood} world!')


def user(request, username, age):
    return HttpResponse(f'My name is {username} and I\'m {age} years old')


def travel(request):
    return render(request, template_name='travel.html', context={
        'cities': ['Praha', 'Ostrava','Bratislava', 'Berlin', 'Budapest'],
        'transport': 'train'
    })


def movies(request):
    movie_list = Movie.objects.all()
    return render(request, template_name='movies.html', context={
        'movies': movie_list
    })


def movies_genre(request, genre):
    movie_list = Movie.objects.filter(genre__name=genre)
    return render(request, template_name='movies.html', context={
        'movies': movie_list
    })


class MoviesView(View):
    def get(self, request):
        movie_list = Movie.objects.all()
        return render(request, template_name='movies.html', context={
            'movies': movie_list
        })


class MoviesTemplateView(TemplateView):
    template_name = 'movies.html'
    extra_context = {'movies': Movie.objects.all()}


class MoviesListView(ListView):
    template_name = 'movies_list.html'
    model = Movie

class MovieCreateView(FormView):
    template_name='form.html'
    form_class = MovieForm
    success_url = reverse_lazy('movie_create')

    def form_valid(self, form):
        result = super().form_valid(form)
        cleaned_data=form.cleaned_data
        Movie.objects.create(
            title=cleaned_data['title'],
            genre=cleaned_data['genre'],
            rating=cleaned_data['rating'],
            released=cleaned_data['released'],
            description=cleaned_data['description'],
        )
        return  result

class ActorsTemplateView(TemplateView):
    template_name = 'actors.html'
    extra_context = {'actors': Actor.objects.all()}

class ActorListView(ListView):
    template_name = 'actors_list.html'
    model = Actor