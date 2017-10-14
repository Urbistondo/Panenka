from django.db import models
from src.panenka.users.models import User


class Profile(models.Model):
    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=120)
    last_name_1 = models.CharField(max_length=120)
    last_name_2 = models.CharField(max_length=120)
    country = models.CharField(max_length=120)
    birth_date = models.DateTimeField(blank=False, auto_created=False, auto_now_add=False)
    photo = models.CharField(blank=True, default='', max_length=300)
    balance = models.FloatField(blank=False, default=0)

    # objects = ProfileManager()

    def get_full_name(self):
        # The user is identified by their email address
        return '%s %s' % (self.first_name, self.last_name_1)

    def get_short_name(self):
        # The user is identified by their email address
        return self.first_name

    def __str__(self):  # __unicode__ on Python 2
        return '%s %s' % (self.first_name, self.last_name_1)

    def get_balance(self):
        return self.balance

