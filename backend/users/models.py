from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Users(User):
    # TODO: default for dev
    ChineseName = models.CharField(max_length=100, null=False, default='')
    EnglishName = models.CharField(max_length=100, blank=True, default='Unknown')
    Created_time = models.DateTimeField(auto_now_add=True)
    # TODO: check doc for auto_now
    LastSeen = models.DateTimeField(auto_now=True)
    CompanyID

    class Meta:
        db_table = 'user'
        ordering = ('Created_time',)