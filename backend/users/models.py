from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class UserProfileManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        """
        Creates and saves a user with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('User must have an email address')
        user = self.model(
            email=self.normalize_email(email), #BaseUserManager defined method
            name=name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email,
            password=password,
            name=name
        )

        user.is_admin = True
        user.save(using=self._db)
        return user

class UserProfile(AbstractUser):
    # TODO: default for dev
    chinese_name = models.CharField(verbose_name=u'中文名', max_length=30, null=False)
    english_name = models.CharField(verbose_name=u'英文名', max_length=30, blank=True, null=True)
    created_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)
    # TODO: check doc for auto_now
    last_seen = models.DateTimeField(verbose_name=u'更新时间', auto_now=True)
    # TODO: 去掉unique=True
    company_id = models.IntegerField(verbose_name=u'员工号', unique=True)
    position = models.CharField(verbose_name=u'职位', max_length=20, blank=True)
    gender = models.CharField(verbose_name=u'性别', max_length=6, choices=(('male', '男'), ('female', '女')), default='male', help_text='性别')
    email = models.EmailField(verbose_name=u'电子邮件地址', max_length=255, unique=True)
    phone = models.CharField(verbose_name=u'手机号码', max_length=20, help_text='手机号码')
    department = models.CharField(verbose_name=u'部门', max_length=20, blank=True, default='ISV')
    organization = models.ForeignKey('Organization', verbose_name=u'组织名称', on_delete=models.SET_NULL,
                                     related_name='user_profile', null=True)
    
    # objects = UserProfileManager()
    REQUIRED_FIELDS = ['email', 'company_id']
    class Meta:
        verbose_name_plural = verbose_name = u'用户'
        db_table = 'user_profile'
        ordering = ('-created_time',)

    def __str__(self):
        return '<UserProfile> ID:{0} Name:{1}'.format(self.id, self.chinese_name)

    def __repr__(self):
        return self.__str__()


class Organization(models.Model):
    name = models.CharField(verbose_name=u'组织名称', max_length=100, unique=True)

    class Meta:
        verbose_name = u'组织'
        verbose_name_plural = u'组织'
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
        verbose_name_plural = verbose_name = u'验证码'

    def __str__(self):
        return '<Phone_VerifyCode> code:{0} mobile:{1}'.format(self.code, self.mobile)
    
    def __repr__(self):
        return self.__str__()