from django.db import models


class Game(models.Model):
    title = models.CharField(max_length=32, blank=False, null=False, default='Untitled Title :O')
    developer = models.CharField(max_length=32, default='Bad Games Company Inc.')

    def __str__(self):
        return f'{self.title} - {self.developer}'


class Player(models.Model):
    first_name = models.CharField(max_length=32, null=True, blank=True)
    internet_name = models.CharField(max_length=32, null=False, blank=False, default='PoopSteve420')
    last_name = models.CharField(max_length=32, null=True, blank=True)
    twitter = models.CharField(max_length=64, null=True, blank=True)
    youtube = models.CharField(max_length=64, null=True, blank=True)
    twitch = models.CharField(max_length=64, null=True, blank=True)
    discord = models.CharField(max_length=64, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} \"{self.internet_name}\" {self.last_name}"


class Team(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    players = models.ManyToManyField(Player)
    sign_date = models.DateTimeField(auto_now_add=True)
    release_date = models.DateTimeField(null=True, blank=True)
    active = models.BooleanField(default=True)
    coach = models.ForeignKey(Player, related_name='team_coach', on_delete=models.CASCADE)
    manager = models.ForeignKey(Player, related_name='team_manager', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.game.title}'


