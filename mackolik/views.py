from django.shortcuts import render, get_object_or_404
from .models import Leagues, Coach, Club, Matches, Player

def homepage(request):
    ligler = Leagues.objects.all()
    td = Coach.objects.all()
    kulupler = Club.objects.all()
    maclar = Matches.objects.all()
    futbolcular = Player.objects.all()
    return render(request, 'base.html', {
        'ligler': ligler,
        'td': td,
        'kulup': kulupler,
        'maclar': maclar,
        'futbolcu': futbolcular
    })





def match_details(request, mac_slug):
    maclar = get_object_or_404(Matches,slug=mac_slug)
    kulupler = Matches.objects.all()
    kulupler_maclar = Club.objects.filter(category=category).order_by('-created_on')

    return render(request, 'match_details.html', {
        'maclar': maclar,
        'kulupler': kulupler,

    })




