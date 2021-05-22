"""hollymovies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path

from viewer.views import hello, goodbye, user, travel, movies, movies_genre, MoviesView, MoviesTemplateView, \
    MoviesListView, MovieCreateView, ActorListView, ActorsTemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/<mood>', hello),
    path('goodbye', goodbye),
    re_path(r'^user/(?P<username>\w+)/(?P<age>\d{2})$', user),

    path('travel', travel, name='travel'),
    path('', movies, name='index'),
    path('movies/genre/<genre>', movies_genre, name='movies_genre'),
    path('movies/class', MoviesView.as_view(), name='movies_class'),
    path('movies/class/template', MoviesTemplateView.as_view(), name='movies_template'),
    path('movies/class/list', MoviesListView.as_view(), name='movies_list'),
    path('movie/create', MovieCreateView.as_view(), name='movie_create'),

    path('actors/class/template', ActorsTemplateView.as_view(), name='actors_template'),
    path('actors/class/list', ActorListView.as_view(), name='actor_list'),
]
