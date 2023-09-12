from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('mac/<slug:mac_slug>/', views.match_details, name='match_details')
]

