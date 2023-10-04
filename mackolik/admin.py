from django.contrib import admin
from .models import Leagues, Club, Coach, Player, Matches, Referee, Author, News, Cup, Transfers, Nationality




admin.site.register(Leagues)
admin.site.register(Club)
admin.site.register(Coach)
admin.site.register(Player)

class MatchAdmin(admin.ModelAdmin):
    filter_horizontal = ('club1_team_line_up', 'club2_team_line_up')


admin.site.register(Matches,MatchAdmin)
admin.site.register(Referee)
admin.site.register(Author)
admin.site.register(News)
admin.site.register(Cup)

class TransferAdmin(admin.ModelAdmin):
    filter_horizontal = ('player','tok', 'ok')


admin.site.register(Transfers,TransferAdmin)
admin.site.register(Nationality)
