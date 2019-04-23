from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    # TODO: default for dev
    chinese_name = models.CharField(max_length=100, null=False, default='mouren')
    english_name = models.CharField(max_length=100, blank=True, default='Unknown')
    created_time = models.DateTimeField(auto_now_add=True)
    # TODO: check doc for auto_now
    last_seen = models.DateTimeField(auto_now=True)
    company_id = models.IntegerField()
    position = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    phone = models.PositiveIntegerField(blank=True)
    department = models.CharField(max_length=100, blank=True, default='ISV')
    organization = models.ForeignKey('Organization', on_delete=models.SET_NULL, related_name='user_profile', null=True)
    # TODO 用户密码字段
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')

    class Meta:
        verbose_name = 'User Profile'
        db_table = 'user_profile'
        ordering = ('created_time',)


class Organization(models.Model):
    name = models.CharField(max_length=100, default='beijing')

    class Meta:
        verbose_name = 'Organization'
        verbose_name_plural = 'Organization'
        db_table = 'organizations'
