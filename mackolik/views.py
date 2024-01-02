from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Leagues, Club, Matches, Player,News, Transfers, Standings, Nationality,ClubCups
from django.db.models import Q
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm, CustomAuthenticationForm, UserProfileForm, CustomPasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from allauth.account.views import PasswordChangeView





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
    standings = [(i + 1, standing) for i, standing in enumerate(standings)]
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


def coach_details(request,):
    return render(request, 'pages/coach_details.html',)



def search(request,):
    query = request.GET.get('q')
    clubs = Club.objects.filter(name__icontains=query)
    players = Player.objects.filter(name__icontains=query)
    leagues = Leagues.objects.filter(name__icontains=query)
    nationalitys = Nationality.objects.filter(name__icontains=query)


    return render(request, 'pages/search_table.html',{
        'clubs': clubs,
        'players': players,
        'leagues': leagues,
        'nationalitys': nationalitys

    })



def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('homepage')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'user/login.html', {'form': form})


def user_register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect('homepage')
    else:
        form = CustomUserCreationForm()
    return render(request, 'user/register.html', {'form': form})


@login_required
def user_dashboard(request):
    if request.method == 'POST':
        user_form = UserProfileForm(request.POST, instance=request.user)
        password_form = PasswordChangeForm(request.user, request.POST)

        if user_form.is_valid() and password_form.is_valid():
            user_form.save()

            if password_form.is_valid():
                password_form.save()
                messages.success(request, 'Değişiklikler Kaydedildi')
                return redirect('homepage')
            else:
                messages.error(request, 'Şifre değiştirme işlemi başarısız oldu.')
    else:
        user_form = UserProfileForm(instance=request.user)
        password_form = PasswordChangeForm(request.user)

    return render(request, 'user/dashboard.html', {
        'user_form': user_form,
        'password_form': password_form
    })
def user_logout(request):
    logout(request)
    return redirect('homepage')


