from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class Player(models.Model):
    # TODO - Custom ID field
    player_shirt = models.CharField(blank=False, max_length=255)
    player_number = models.IntegerField(blank=True, default=0)
    player_birth = models.DateTimeField(blank=True, auto_created=False, auto_now=False, auto_now_add=False)
    player_value = models.FloatField(blank=False, default=100000)
    player_position_category = models.CharField(blank=False, default='position_category3', max_length=18)
    player_link = models.URLField(blank=True, max_length=255)
    id_country = models.CharField(blank=True, max_length=3)
    id_club = models.CharField(blank=True, max_length=45)
    # photo = models.CharField(blank=True, default='', max_length=300)

    # objects = PlayerManager()

    def get_full_name(self):
        # The user is identified by their email address
        return self.player_shirt

    def get_short_name(self):
        # The user is identified by their email address
        return self.player_shirt

    def get_position_category(self):
        return self.player_position_category

    def __str__(self):              # __unicode__ on Python 2
        return self.player_shirt
