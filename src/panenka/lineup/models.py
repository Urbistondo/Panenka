from django.db import models
from src.panenka.players.models import Player


# Create your models here.
class Lineup(models.Model):
    id_lineup = models.CharField(unique=True, blank=False, max_length=45)
    week = models.IntegerField(blank=False)
    budget = models.IntegerField(blank=False, default=500000000)
    id_starter1 = models.IntegerField(unique=True,default=0)
    id_starter2 = models.IntegerField(unique=True,default=0)
    id_starter3 = models.IntegerField(unique=True,default=0)
    id_starter4 = models.IntegerField(unique=True,default=0)
    id_starter5 = models.IntegerField(unique=True,default=0)
    id_starter6 = models.IntegerField(unique=True,default=0)
    id_starter7 = models.IntegerField(unique=True,default=0)
    id_starter8 = models.IntegerField(unique=True,default=0)
    id_starter9 = models.IntegerField(unique=True,default=0)
    id_starter10 = models.IntegerField(unique=True,default=0)
    id_starter11 = models.IntegerField(unique=True,default=0)
    id_bench1 = models.IntegerField(unique=True,default=0)
    id_bench2 = models.IntegerField(unique=True,default=0)
    id_bench3 = models.IntegerField(unique=True,default=0)
    id_contest = models.CharField(unique=True, blank=False, max_length=45)
    id_user = models.IntegerField(unique=True, blank=False)
    captain = models.IntegerField(unique=True,default=0)
    date = models.DateTimeField(blank=False, auto_created=True,
                                        auto_now_add=True)
    # objects = LineupManager()

    def get_user(self):
        # The user is identified by their email address
        return self.id_user

    def get_starterplayers(self):
        i = 1
        players = list()
        while i < 12:
            players.append(Player.objects.get(id=i))
            i += 1
        return players
        # return {
        #     'id_starter1': self.id_starter1,
        #     'id_starter2': self.id_starter2,
        #     'id_starter3': self.id_starter3,
        #     'id_starter4': self.id_starter4,
        #     'id_starter5': self.id_starter5,
        #     'id_starter6': self.id_starter6,
        #     'id_starter7': self.id_starter7,
        #     'id_starter8': self.id_starter8,
        #     'id_starter9': self.id_starter9,
        #     'id_starter10': self.id_starter10,
        #     'id_starter11': self.id_starter11
        # }

    def get_benchplayers(self):
        return {
            'id_bench1': self.id_bench1,
            'id_bench2': self.id_bench2,
            'id_bench3': self.id_bench3,
        }

    def __str__(self):  # __unicode__ on Python 2
        return self.id_lineup