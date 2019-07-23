from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    # TODO: default for dev
    chinese_name = models.CharField(verbose_name=u'中文名', max_length=30, null=False)
    english_name = models.CharField(verbose_name=u'英文名', max_length=30, blank=True, null=True)
    created_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)
    # TODO: check doc for auto_now
    last_seen = models.DateTimeField(verbose_name=u'更新时间', auto_now=True)
    company_id = models.IntegerField(verbose_name=u'员工号', unique=True)
    position = models.CharField(verbose_name=u'职位', max_length=100, blank=True)
    gender = models.CharField(verbose_name=u'性别', max_length=6, choices=(('male', '男'), ('female', '女')), default='male', help_text='性别')
    email = models.EmailField(verbose_name=u'电子邮件地址', max_length=100, unique=True)
    phone = models.CharField(verbose_name=u'手机号码', max_length=20, help_text='手机号码')
    department = models.CharField(verbose_name=u'部门', max_length=100, blank=True, default='ISV')
    organization = models.ForeignKey('Organization', verbose_name=u'组织名称', on_delete=models.SET_NULL,
                                     related_name='user_profile', null=True)
    user = models.OneToOneField(User, verbose_name=u'用户', on_delete=models.CASCADE, related_name='user_profile')

    class Meta:
        verbose_name = 'User Profile'
        db_table = 'user_profile'
        ordering = ('-created_time',)

    def __str__(self):
        return '<UserProfile> ID:{0} Name:{1} UserID:{2}'.format(self.id, self.chinese_name, self.user)

    def __repr__(self):
        return self.__str__()


class Organization(models.Model):
    name = models.CharField(verbose_name=u'组织名称', max_length=100, unique=True)

    class Meta:
        verbose_name = 'Organization'
        verbose_name_plural = 'Organization'
        db_table = 'organizations'

    def __str__(self):
        return '<Organization> ID:{0} Name:{1}'.format(self.id, self.name)

    def __repr__(self):
        return self.__str__()


class VerifyCode(models.Model):
    code = models.CharField(verbose_name=u'验证码', max_length=20, help_text='验证码')
    mobile = models.CharField(verbose_name=u'手机号码', max_length=20, help_text='手机号码')
    add_time = models.DateTimeField(verbose_name=u'添加时间', auto_now_add=True)

    class Meta:
        verbose_name_plural = verbose_name = ''

    def __str__(self):
        return '<Phone_VerifyCode> code:{0} mobile:{1}'.format(self.code, self.mobile)
    
    def __repr__(self):
        return self.__str__()