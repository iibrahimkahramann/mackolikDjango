from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('mac/<slug:match_slug>/', views.match_details, name='match_details'),
    path('league/<slug:league_slug>/', views.league_details, name='league_details'),
]

