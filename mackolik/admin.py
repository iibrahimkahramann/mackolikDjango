from django.contrib import admin
from .models import Leagues, Club, Coach, Player, Matches, Referee


admin.site.register(Leagues)
admin.site.register(Club)
admin.site.register(Coach)
admin.site.register(Player)
admin.site.register(Matches)
admin.site.register(Referee)
