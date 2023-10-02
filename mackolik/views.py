from django.shortcuts import render, get_object_or_404, redirect
from .models import Leagues, Coach, Club, Matches, Player,News,Author, Transfers

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



def staff(request,club_slug):
    kulup = get_object_or_404(Club, slug=club_slug)
    oyuncular = Player.objects.filter(club=kulup)
    return render(request, 'pages/staff.html',{
        'kulup': kulup,
        'oyuncular': oyuncular,
    })



def news(request):
    haberler = News.objects.all()
    return render(request, 'news/news.html', {
        'haberler': haberler,
    })



def news_detail(request, news_slug):
    haber = get_object_or_404(News,slug=news_slug)
    return render(request, 'news/news_detail.html', {
        'haber': haber,
    })

def transfer(request, player_id):
    oyuncu = Player.objects.get(pk=player_id)

    if request.method == 'POST':
        ok = oyuncu.club
        tok_id = request.POST.get('transfer_oldugu_kulup')
        tok = Club.objects.get(pk=tok_id)

        transfer = Transfers(player=oyuncu, ok=ok, tok=tok)
        transfer.save()

        oyuncu.club = tok
        oyuncu.save()

        return redirect('club_details', player_id=player_id)

    kulupler = Club.objects.all()
    return render(request, '', {
        'oyuncu': oyuncu,
        'kulupler': kulupler
    })