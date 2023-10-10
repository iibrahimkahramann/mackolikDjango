from django.shortcuts import render, get_object_or_404, redirect
from .models import Leagues, Coach, Club, Matches, Player,News,Author, Transfers, Standings
from django.db.models import Q

def homepage(request):
    league = Leagues.objects.all()
    matches = Matches.objects.all()
    return render(request, 'pages/homepage.html', {
        'league': league,
        'matches': matches,
    })


def match_details(request, match_slug):
    matches = get_object_or_404(Matches, slug=match_slug)
    clubs_matches = Matches.objects.filter(league=matches.league).order_by('-time')
    return render(request, 'pages/match_details.html', {
        'matches': matches,
        'clubs_matches': clubs_matches,
    })



def league_details(request, league_slug):
    leagues = get_object_or_404(Leagues, slug=league_slug)
    match_leagues = Matches.objects.filter(league=leagues).order_by('-time')
    standings = Standings.objects.filter(club__league=leagues).order_by('-puan')
    return render(request, 'pages/league_details.html', {
        'leagues': leagues,
        'match_leagues': match_leagues,
        'standings': standings,

    })




def club_details(request, club_slug):
    clubs = get_object_or_404(Club, slug=club_slug)
    players = Player.objects.filter(club=clubs)
    matches = Matches.objects.filter(Q(club1=clubs) | Q(club2=clubs))
    standings = Standings.objects.filter(club=clubs)
    transfers = Transfers.objects.filter(Q(ok=clubs) | Q(tok=clubs))
    return render(request, 'pages/club_details.html', {
        'clubs': clubs,
        'players': players,
        'matches': matches,
        'standings': standings,
        'transfers': transfers,

    })



def staff(request,club_slug):
    club = get_object_or_404(Club, slug=club_slug)
    players = Player.objects.filter(club=club)
    return render(request, 'pages/staff.html',{
        'club': club,
        'players': players,
    })



def news(request):
    news = News.objects.all()
    return render(request, 'news/news.html', {
        'news': news,
    })



def news_detail(request, news_slug):
    news = get_object_or_404(News,slug=news_slug)
    return render(request, 'news/news_detail.html', {
        'news': news,
    })

def transfers(request, club_slug):
    club = get_object_or_404(Club, slug=club_slug)
    ok = Transfers.objects.filter(ok=club).order_by('-time')
    tok = Transfers.objects.filter(tok=club).order_by('-time')
    return render(request, 'pages/transfer.html', {
        'club': club,
        'ok': ok,
        'tok': tok
    })

def player_details(request, player_slug):
    player = get_object_or_404(Player, slug=player_slug)
    return render(request, 'pages/player_details.html', {
        'player': player,
    })


