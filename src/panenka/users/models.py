from django.db import models
from django.core.urlresolvers import reverse

class User(models.Model):
    username = models.CharField(max_length = 120)
    email = models.CharField(max_length = 120)
    password = models.CharField(max_length = 300)
    first_name = models.CharField(max_length = 120)
    last_name_1 = models.CharField(max_length = 120)
    last_name_2 = models.CharField(max_length = 120, default = '', blank = 'true')
    country = models.CharField(max_length = 120, default = '', blank = 'true')
    created = models.DateTimeField(auto_now = False, auto_now_add = True)
    updated = models.DateTimeField(auto_now = True, auto_now_add = False)
    birth_date = models.DateTimeField(auto_created = False, auto_now_add = False)
    photo = models.CharField(max_length = 300, default = '', blank = 'true')

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:show', kwargs = {'id': self.id})