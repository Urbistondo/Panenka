from django.db import models


class Contest(models.Model):
    id_contest = models.CharField(unique=True, blank=False, max_length=45)
    title = models.CharField(blank=False, max_length=255, default='Contest')
    password = models.CharField(blank=True, max_length=255, default='')
    created_by_admin = models.BooleanField(blank=False, default=True)
    created_date = models.DateTimeField(blank=False, auto_created=True,
                                        auto_now_add=True)
    open_date = models.DateTimeField(blank=False, auto_created=False,
                                     auto_now_add=False)
    close_date = models.DateTimeField(blank=False, auto_created=False,
                                      auto_now_add=False)
    start_date = models.DateTimeField(blank=False, auto_created=False,
                                      auto_now_add=False)
    end_date = models.DateTimeField(blank=False, auto_created=False,
                                    auto_now_add=False)
    minimum_participants = models.IntegerField(blank=False, default=3)
    maximum_participants = models.IntegerField(blank=False, default=100)

    # objects = ContestManager()

    def get_full_name(self):
        # The user is identified by their email address
        return self.title

    def get_short_name(self):
        # The user is identified by their email address
        return self.title

    def __str__(self):  # __unicode__ on Python 2
        return self.title