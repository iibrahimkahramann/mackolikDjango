from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import AbstractUser


class Nationality(models.Model):
    name = models.CharField(max_length=120, verbose_name = 'İsim')
    image = models.ImageField(upload_to='news_nationality_images/', default='league_image.jpg', verbose_name = 'Bayrak')
    slug = AutoSlugField(populate_from='name', unique=True, editable=True, blank=True)

    class Meta:
        db_table = 'Nationality'
        verbose_name = 'Ülke'
        verbose_name_plural = 'Ülke'
    def __str__(self):
        return self.name




class Leagues(models.Model):
    name = models.CharField(max_length=120, verbose_name = 'İsim')
    nationality = models.ForeignKey(Nationality, on_delete=models.CASCADE, verbose_name = 'Ülke', null=True)
    image = models.ImageField(upload_to='news_league_images/', default='league_image.jpg', verbose_name = 'Logo')
    slug = AutoSlugField(populate_from='name', unique=True, editable=True, blank=True)
    history = models.TextField(null=True ,verbose_name='Tarihçe')

    class Meta:
        db_table = 'Leagues'
        verbose_name = 'Ligler'
        verbose_name_plural = 'Ligler'



    def __str__(self):
        return self.name



class Cup(models.Model):
    name = models.CharField(max_length=120, verbose_name = 'İsim')
    league = models.ForeignKey(Leagues, on_delete=models.CASCADE, related_name='league', verbose_name = 'Lig')

    class Meta:
        db_table = 'Cup'
        verbose_name = 'Kupa'
        verbose_name_plural = 'Kupa'

    def __str__(self):
        return self.name


class Club(models.Model):
    name = models.CharField(max_length=120, unique=True, verbose_name = 'İsim')
    nationality = models.ForeignKey(Nationality, on_delete=models.CASCADE, verbose_name = 'Ülke', null=True)
    stadium = models.CharField(max_length=120, unique=True,verbose_name = 'Staydum')
    coach = models.ForeignKey('Coach', on_delete=models.CASCADE, verbose_name = 'Teknik Direktör')   #coach modelini referans veriyor önde tanımlanmadıgı için
    league = models.ForeignKey(Leagues, on_delete=models.CASCADE, verbose_name = 'Lig')
    image = models.ImageField(upload_to='news_club_images/', default='club_image.jpg', verbose_name = 'Logo')
    slug = AutoSlugField(populate_from='name', unique=True, editable=True, blank=True)
    cup = models.ForeignKey(Cup, on_delete=models.CASCADE, related_name='kupa', null=True,verbose_name = 'Kupa')

    class Meta:
        db_table = 'Club'
        verbose_name = 'Kulüp'
        verbose_name_plural = 'Kulüp'

    def __str__(self):
        return self.name

class Coach(models.Model):
    name = models.CharField(max_length=120,verbose_name = 'İsim')
    age = models.PositiveIntegerField(verbose_name = 'Yaş')
    date_of_birth = models.DateField(verbose_name = 'Doğum Tarihi')
    nationality = models.ForeignKey(Nationality, on_delete=models.CASCADE, verbose_name = 'Ülke', null=True)
    image = models.ImageField(upload_to='news_coach_images/', default='coach_image.jpg',verbose_name = 'Resim')


    class Meta:
        db_table = 'Coach'
        verbose_name = 'Teknik Direktör'
        verbose_name_plural = 'Teknik Direktör'

    def __str__(self):
        return self.name




class Player(models.Model):
    name = models.CharField(max_length=120,verbose_name = 'İsim')
    age = models.PositiveIntegerField(verbose_name = 'Yaş')
    date_of_birth = models.DateField(verbose_name = 'Doğum Tarihi')
    nationality = models.ForeignKey(Nationality, on_delete=models.CASCADE, verbose_name = 'Ülke', null=True)
    foot = models.CharField(max_length=120, verbose_name = 'Ayak')
    size = models.FloatField(verbose_name = 'Boy')
    weight = models.PositiveIntegerField(verbose_name = 'Kilo')
    numbers = models.PositiveIntegerField(verbose_name = 'Numara')
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='kulüp')
    image = models.ImageField(upload_to='news_player_images/', default='player_image.jpg',verbose_name = 'resim')
    pozition = models.CharField(max_length=20, null=True,verbose_name = 'Oynadığı Pozisyon')
    slug = AutoSlugField(populate_from='name', unique=True, editable=True, blank=True)
    history_clubs = models.ManyToManyField(Club, through='PlayerClubHistory',verbose_name = 'Geçmiş külüpleri')   #through ilişkisel modellerde ara modeli kullanmak için kullanılır

    class Meta:
        db_table = 'Player'
        verbose_name = 'Oyuncu'
        verbose_name_plural = 'Oyuncu'

    def __str__(self):
        return self.name




class Referee(models.Model):
    name = models.CharField(max_length=120,verbose_name = 'İsim')
    age = models.PositiveIntegerField(verbose_name = 'Yaş')
    nationality = models.ForeignKey(Nationality, on_delete=models.CASCADE, verbose_name = 'Ülke', null=True)
    image = models.ImageField(upload_to='news_referee_images/', default='referee_image.jpg',verbose_name = 'Resim')


    class Meta:
        db_table = 'Referee'
        verbose_name = 'Hakem'
        verbose_name_plural = 'Hakem'

    def __str__(self):
        return self.name







class Matches(models.Model):
    club1 = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='kulüp1', verbose_name='Kulüp 1')
    club2 = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='kulüp2', verbose_name='Kulüp 2')
    time = models.CharField( max_length=20,verbose_name='Maç Saati')
    stadium = models.CharField(max_length=120, verbose_name='Stadyum')
    club1_skor = models.CharField(max_length=120, verbose_name='Kulüp 1 Skor')
    club2_skor = models.CharField(max_length=120, null=True, verbose_name='Kulüp 2 Skor')
    slug = AutoSlugField(populate_from='league', unique=True, editable=True, blank=True)
    league = models.ForeignKey(Leagues, on_delete=models.CASCADE, related_name='lig', verbose_name='Lig')
    referee = models.ForeignKey(Referee, on_delete=models.CASCADE, verbose_name='Hakem')
    club1_team_line_up = models.ManyToManyField(Player, related_name='club1_line_up', verbose_name='Kulüp 1 İlk 11', blank=True)
    club1_team_reserves = models.ManyToManyField(Player, verbose_name='Kulüp 1 Yedekler', blank=True)
    club1_team_goals = models.ManyToManyField(Player, related_name='club1_mac_goller', verbose_name='Kulüp 1 Goller', blank=True)
    club2_team_line_up = models.ManyToManyField(Player, related_name='club2_mac_ilk_11', verbose_name='Kulüp 2 İlk 11', blank=True)
    club2_team_reserves = models.ManyToManyField(Player, related_name='club2_mac_yedekler', verbose_name='Kulüp 2 Yedekler', blank=True)
    club2_team_goals = models.ManyToManyField(Player, related_name='club2_mac_goller', verbose_name='Kulüp 2 Goller', blank=True)
    man_of_the_match = models.ManyToManyField(Player, related_name='maçın_adamı', verbose_name='Maçın Adamı', blank=True)

    class Meta:
        db_table = 'Matches'
        verbose_name = 'Maçlar'
        verbose_name_plural = 'Maçlar'

    def __str__(self):
        return self.stadium










class Author(models.Model):
    name = models.CharField(max_length=120,verbose_name='İsim')
    about = models.TextField(verbose_name='Hakkında')


    class Meta:
        db_table = 'Author'
        verbose_name = 'Yazar'
        verbose_name_plural = 'Yazar'


    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=120,verbose_name='Başlık')
    summary = models.TextField(max_length=300,verbose_name='Özet')
    contents = models.TextField(verbose_name='Haber')
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(populate_from='title', unique=True, editable=True, blank=True)
    image = models.ImageField(upload_to='news_images/', default='default_image.jpg',verbose_name='Resim')
    author = models.ForeignKey(Author, on_delete=models.CASCADE,verbose_name='Yazar')



    class Meta:
        db_table = 'News'
        verbose_name = 'New'
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title




class Contrat(models.Model):
    contrat = models.CharField(max_length=120, verbose_name='Kontrat', null=True)


    class Meta:
        db_table = 'Contrat'
        verbose_name = 'Kontrat'
        verbose_name_plural = 'Kontratlar'

    def __str__(self):
        return self.contrat




class Transfers(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, verbose_name='Oyuncu', null=True)
    tok = models.ForeignKey(Club, on_delete=models.CASCADE,verbose_name='Transfer Olduğu Kulüp', null=True)
    ok = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='play_club',verbose_name='Oynadığı Kulüp', null=True)
    time = models.DateField(verbose_name='Tarih',)
    contrat = models.ForeignKey(Contrat, on_delete=models.CASCADE,verbose_name='Kontrat', null=True)

    class Meta:
        db_table = 'Transfers'
        verbose_name = 'Transferler'
        verbose_name_plural = 'Transferler'




class Standings(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE, verbose_name='Kulüp',)
    om = models.PositiveIntegerField(verbose_name='Oynanan Maç',)
    win = models.PositiveIntegerField(verbose_name='Kazanılan Maç',)
    draw = models.PositiveIntegerField(verbose_name='Beraberlik',)
    lost = models.PositiveIntegerField(verbose_name='Kaybedilen Maç',)
    goal = models.PositiveIntegerField(verbose_name='Atılan Gol',)
    puan = models.PositiveIntegerField(verbose_name='Puan',)


    class Meta:
        db_table = 'Standings'
        verbose_name = 'Puan Durumu'
        verbose_name_plural = 'Puan Durumu'

    def __str__(self):
        return self.club.name



class PlayerClubHistory(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE,verbose_name='Oyuncu',)
    club = models.ForeignKey(Club, on_delete=models.CASCADE,verbose_name=' Kulüp',)
    start_date = models.DateField(verbose_name='Transfer Olduğu Tarih',)
    end_date = models.DateField(verbose_name='Sözleşme nin Bittiği Tarih' ,)


    class Meta:
        db_table = 'PlayerClubHistory'
        verbose_name = 'Oyuncu Geçmiş Kulüpleri'
        verbose_name_plural = 'Oyuncu Geçmiş Kulüpleri'

    def __str__(self):
        return self.club.name



