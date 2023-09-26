from django.shortcuts import render, get_object_or_404
from .models import Leagues, Coach, Club, Matches, Player

def homepage(request):
    ligler = Leagues.objects.all()
    td = Coach.objects.all()
    kulupler = Club.objects.all()
    maclar = Matches.objects.all()
    futbolcular = Player.objects.all()
    return render(request, 'pages/homepage.html', {
        'ligler': ligler,
        'td': td,
        'kulup': kulupler,
        'maclar': maclar,
        'futbolcu': futbolcular
    })


def match_details(request, match_slug):
    maclar = get_object_or_404(Matches, slug=match_slug)
    kulupler_maclar = Matches.objects.filter(league=maclar.league).order_by('-time')
    return render(request, 'pages/match_details.html', {
        'maclar': maclar,
        'kulupler_maclar': kulupler_maclar,
    })



def league_details(request, league_slug):
    ligler = get_object_or_404(Leagues, slug=league_slug)
    kulupler_ligler = Club.objects.filter(league=ligler).order_by('-puan')
    return render(request, 'pages/league_details.html', {
        'ligler': ligler,
        'kulupler_ligler': kulupler_ligler

    })




def club_details(request, club_slug):
    kulupler = get_object_or_404(Club, slug=club_slug)
    futbolcular = Player.objects.all()
    return render(request, 'pages/club_details.html', {
        'kulupler': kulupler,
        'futbolcular': futbolcular,
    })



def staff(request, club_slug):
    oyuncular = Player.objects.all()
    return render(request, 'pages/staff.html',{
        'oyuncular': oyuncular,
    })
