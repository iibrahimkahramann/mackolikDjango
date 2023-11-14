from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('match/<slug:match_slug>/', views.match_details, name='match_details'),
    path('league/<slug:league_slug>/', views.league_details, name='league_details'),
    path('club/<slug:club_slug>/', views.club_details, name='club_details'),
    path('club/<slug:club_slug>/staff/', views.staff, name='staff'),
    path('club/<slug:club_slug>/transfer/', views.transfers, name='transfers'),
    path('news/', views.news, name='news'),
    path('news-detail/<slug:news_slug>/', views.news_detail, name='news_detail'),
    path('player/<slug:player_slug>/', views.player_details, name='player_details'),
    path('coach/', views.coach_details, name='coach_details'),
    path('search/', views.search, name='search'),
    path('login/', views.user_login, name='user_login'),
    path('register/', views.user_register, name='user_register'),
    path('dashboard/', views.user_dashboard, name='user_dashboard')

]


