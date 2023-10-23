from django.contrib import admin
from .models import Leagues, Club, Coach, Player, Matches, Referee, Author, News, Cup, Transfers, Nationality, Standings,PlayerClubHistory

class LeaguesAdmin(admin.ModelAdmin):
    search_fields = ['league_nationality']


admin.site.register(Leagues,LeaguesAdmin)



class ClubAdmin(admin.ModelAdmin):
    pass


admin.site.register(Club,ClubAdmin)

class CoachAdmin(admin.ModelAdmin):
    pass

admin.site.register(Coach,CoachAdmin)


class PlayerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Player, PlayerAdmin)

class MatchAdmin(admin.ModelAdmin):
    filter_horizontal = ('club1_team_line_up', 'club2_team_line_up', 'club1_team_reserves', 'club2_team_reserves', 'club1_team_goals', 'club2_team_goals', 'man_of_the_match')



admin.site.register(Matches,MatchAdmin)

class RefereeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Referee, RefereeAdmin)
admin.site.register(Author)
admin.site.register(News)
admin.site.register(Cup)
class TransferAdmin(admin.ModelAdmin):
    pass
admin.site.register(Transfers,TransferAdmin)
admin.site.register(Nationality)
admin.site.register(Standings)
admin.site.register(PlayerClubHistory)


