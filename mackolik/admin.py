from django.contrib import admin
from .models import Leagues, Club, Coach, Player, Matches, Referee, Author, News, Cup, Transfers, Nationality, Standings,PlayerClubHistory,Contrat
from django.forms import widgets

class LeaguesAdmin(admin.ModelAdmin):
    search_fields = ['name']
    autocomplete_fields = ['nationality',]
    list_display = ('name', 'nationality', )

admin.site.register(Leagues,LeaguesAdmin)


class ClubAdmin(admin.ModelAdmin):
    search_fields = ['name']
    autocomplete_fields = ['nationality', 'coach', 'league', 'cup']
    list_display = ('name', 'nationality', 'league', 'stadium')

admin.site.register(Club,ClubAdmin)



class CoachAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    autocomplete_fields = ['nationality',]
    list_display = ('name', 'nationality',)

admin.site.register(Coach,CoachAdmin)



class PlayerAdmin(admin.ModelAdmin):
    search_fields = ['name']
    autocomplete_fields = ['nationality', 'club', ]
    list_display = ('name','club', 'age','pozition', 'nationality',)

admin.site.register(Player, PlayerAdmin)



class MatchAdmin(admin.ModelAdmin):
    list_display = ('club1', 'club2', 'league', 'referee')
    search_fields = ('club1', 'club2', 'league', 'referee')
    autocomplete_fields = ['club1', 'club2', 'league', 'referee']
    filter_horizontal = ('club1_team_line_up', 'club2_team_line_up', 'club1_team_reserves', 'club2_team_reserves', 'club1_team_goals', 'club2_team_goals', 'man_of_the_match')

admin.site.register(Matches, MatchAdmin)



class RefereeAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    autocomplete_fields = ['nationality']
    list_display = ('name', 'age', 'nationality',)

admin.site.register(Referee, RefereeAdmin)




class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name',)

admin.site.register(Author,AuthorAdmin)




class NewsAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    autocomplete_fields = ['author']
    list_display = ('title', 'author',)

admin.site.register(News,NewsAdmin)



class CupAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'league',)

admin.site.register(Cup,CupAdmin)



class TransferAdmin(admin.ModelAdmin):
    search_fields = ('player',)
    autocomplete_fields = ['player', 'tok', 'ok']
    list_display = ('player', 'tok', 'ok')
admin.site.register(Transfers,TransferAdmin)




class NationalityAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'image',)

admin.site.register(Nationality,NationalityAdmin)


class StandingsAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    autocomplete_fields = ['club']

admin.site.register(Standings,StandingsAdmin)



class PlayerClubHistoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    autocomplete_fields = ['player', 'club']

admin.site.register(PlayerClubHistory,PlayerClubHistoryAdmin)

class ContractAdmin(admin.ModelAdmin):
    pass

admin.site.register(Contrat,ContractAdmin)
