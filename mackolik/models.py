from django.db import models
from autoslug import AutoSlugField


class Nationality(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='news_nationality_images/', default='league_image.jpg')
    slug = AutoSlugField(populate_from='name', unique=True, editable=True, blank=True)

    class Meta:
        db_table = 'Nationality'
        verbose_name = 'Ülke'
        verbose_name_plural = 'Ülke'
    def __str__(self):
        return self.name




class Leagues(models.Model):
    name = models.CharField(max_length=120)
    nationality = models.ManyToManyField(Nationality, related_name='league_nationality', blank=True)
    image = models.ImageField(upload_to='news_league_images/', default='league_image.jpg')
    slug = AutoSlugField(populate_from='name', unique=True, editable=True, blank=True)
    history = models.TextField(null=True)

    class Meta:
        db_table = 'Leagues'
        verbose_name = 'Ligler'
        verbose_name_plural = 'Ligler'

    def __str__(self):
        return self.name



class Cup(models.Model):
    name = models.CharField(max_length=120)
    league = models.ForeignKey(Leagues, on_delete=models.CASCADE, related_name='league')

    class Meta:
        db_table = 'Cup'
        verbose_name = 'Kupa'
        verbose_name_plural = 'Kupa'

    def __str__(self):
        return self.name


class Club(models.Model):
    name = models.CharField(max_length=120, unique=True)
    nationality = models.ManyToManyField(Nationality, related_name='club_nationality', blank=True)
    stadium = models.CharField(max_length=120, unique=True)
    coach = models.ForeignKey('Coach', on_delete=models.CASCADE, related_name='kulüp')   #coach modelini referans veriyor önde tanımlanmadıgı için
    league = models.ForeignKey(Leagues, on_delete=models.CASCADE, related_name='Ligler')
    image = models.ImageField(upload_to='news_club_images/', default='club_image.jpg')
    slug = AutoSlugField(populate_from='name', unique=True, editable=True, blank=True)
    cup = models.ForeignKey(Cup, on_delete=models.CASCADE, related_name='kupa', null=True)

    class Meta:
        db_table = 'Club'
        verbose_name = 'Kulüp'
        verbose_name_plural = 'Kulüp'

    def __str__(self):
        return self.name

class Coach(models.Model):
    name = models.CharField(max_length=120)
    age = models.PositiveIntegerField()
    date_of_birth = models.DateField()
    nationality = models.ManyToManyField(Nationality, related_name='coach_nationality', blank=True)
    image = models.ImageField(upload_to='news_coach_images/', default='coach_image.jpg')


    class Meta:
        db_table = 'Coach'
        verbose_name = 'Teknik Direktör'
        verbose_name_plural = 'Teknik Direktör'

    def __str__(self):
        return self.name




class Player(models.Model):
    name = models.CharField(max_length=120)
    age = models.PositiveIntegerField()
    date_of_birth = models.DateField()
    nationality = models.ManyToManyField(Nationality, related_name='player_nationality', blank=True)
    foot = models.CharField(max_length=120)
    size = models.FloatField()
    weight = models.PositiveIntegerField()
    numbers = models.PositiveIntegerField()
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='kulüp')
    image = models.ImageField(upload_to='news_player_images/', default='player_image.jpg')
    pozition = models.CharField(max_length=20, null=True)
    slug = AutoSlugField(populate_from='name', unique=True, editable=True, blank=True)

    class Meta:
        db_table = 'Player'
        verbose_name = 'Oyuncu'
        verbose_name_plural = 'Oyuncu'

    def __str__(self):
        return self.name




class Referee(models.Model):
    name = models.CharField(max_length=120)
    age = models.PositiveIntegerField()
    nationality = models.ManyToManyField(Nationality, related_name='referee_nationality', blank=True)
    image = models.ImageField(upload_to='news_referee_images/', default='referee_image.jpg')


    class Meta:
        db_table = 'Referee'
        verbose_name = 'Hakem'
        verbose_name_plural = 'Hakem'

    def __str__(self):
        return self.name








class Matches(models.Model):
    club1 = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='kulüp1')
    club2 = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='kulüp2')
    time = models.FloatField()
    stadium = models.CharField(max_length=120)
    club1_skor = models.CharField(max_length=120)
    club2_skor = models.CharField(max_length=120, null=True)
    slug = AutoSlugField(populate_from='league', unique=True, editable=True, blank=True)
    league = models.ForeignKey(Leagues, on_delete=models.CASCADE, related_name='lig')
    referee =models.ForeignKey(Referee, on_delete=models.CASCADE, related_name='hakem')
    club1_team_line_up = models.ManyToManyField(Player, related_name='club1_mac_ilk_11', blank=True)
    club1_team_reserves = models.ManyToManyField(Player, related_name='club1_mac_yedekler', blank=True)
    club1_team_goals = models.ManyToManyField(Player, related_name='club1_mac_goller', blank=True)
    club2_team_line_up = models.ManyToManyField(Player, related_name='club2_mac_ilk_11', blank=True)
    club2_team_reserves = models.ManyToManyField(Player, related_name='club2_mac_yedekler', blank=True)
    club2_team_goals = models.ManyToManyField(Player, related_name='club2_mac_goller', blank=True)
    man_of_the_match = models.ManyToManyField(Player, related_name='maçın_adamı', blank=True)

    class Meta:
        db_table = 'Matches'
        verbose_name = 'Maçlar'
        verbose_name_plural = 'Maçlar'

    def __str__(self):
        return self.stadium










class Author(models.Model):
    name = models.CharField(max_length=120)
    about = models.TextField()


    class Meta:
        db_table = 'Author'
        verbose_name = 'Yazar'
        verbose_name_plural = 'Yazar'


    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=120)
    summary = models.TextField(max_length=300)
    contents = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(populate_from='title', unique=True, editable=True, blank=True)
    image = models.ImageField(upload_to='news_images/', default='default_image.jpg')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='yazar')



    class Meta:
        db_table = 'News'
        verbose_name = 'New'
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title





class Transfers(models.Model):
    player = models.ManyToManyField(Player, related_name='oyuncu')
    tok = models.ManyToManyField(Club,  related_name='transfer_oldugu_kulup')
    ok = models.ManyToManyField(Club, related_name='oynadıgı_kulup',)
    time = models.DateField()

    class Meta:
        db_table = 'Transfers'
        verbose_name = 'Transferler'
        verbose_name_plural = 'Transferler'




class Standings(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='kulup')
    om = models.PositiveIntegerField()
    win = models.PositiveIntegerField()
    draw = models.PositiveIntegerField()
    lost = models.PositiveIntegerField()
    goal = models.PositiveIntegerField()
    puan = models.PositiveIntegerField()


    class Meta:
        db_table = 'Standings'
        verbose_name = 'Puan Durumu'
        verbose_name_plural = 'Puan Durumu'

    def __str__(self):
        return self.club.name




