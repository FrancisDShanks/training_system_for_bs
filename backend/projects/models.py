from django.db import models
# from django.contrib.postgres.fields import JSONField
from django_mysql.models import JSONField
from backend.users.models import Organization, UserProfile


# Create your models here.
class Project(models.Model):
    name = models.CharField(verbose_name=u'项目名称', max_length=100, default='test project', unique=True)
    created_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name=u'更新时间', auto_now=True)
    start_time = models.DateTimeField(verbose_name=u'开始时间', )
    end_time = models.DateTimeField(verbose_name=u'结束时间', )
    organization = models.ForeignKey(Organization, verbose_name=u'组织名称', on_delete=models.SET_NULL,
                                     related_name='project', null=True)
    location = models.CharField(verbose_name=u'项目地点', max_length=200, default='some where', blank=True)
    introduction = models.TextField(verbose_name=u'项目简介', blank=True)
    cover = models.ImageField(verbose_name=u'封面', upload_to='cover/', null=True, blank=True)
    cost_budget = models.DecimalField(verbose_name=u'花费预算', max_digits=10, decimal_places=2, null=True, blank=True)
    cost = models.DecimalField(verbose_name=u'实际花费', max_digits=10, decimal_places=2, null=True, blank=True)
    project_manager = models.ForeignKey(UserProfile, verbose_name=u'托管人', on_delete=models.SET_NULL,
                                        related_name='project_manager', null=True, blank=True)
    project_creator = models.ForeignKey(UserProfile, verbose_name=u'创建人', on_delete=models.SET_NULL,
                                        related_name='project_creator', null=True, blank=True)
    price = models.DecimalField(verbose_name=u'定价', max_digits=5, decimal_places=2, null=True, blank=True)

    class Meta:
        verbose_name_plural = verbose_name = u'项目'
        db_table = 'project'
        indexes = [
            models.Index(fields=['name'], ),
            models.Index(fields=['created_time'],),
            models.Index(fields=['start_time']),
            models.Index(fields=['end_time']),
            models.Index(fields=['cost_budget']),
            models.Index(fields=['cost']),
            models.Index(fields=['price']),
            models.Index(fields=['location']),
        ]

    def __str__(self):
        return '<Project> ID: {0} Name:{1}'.format(self.id, self.name)

    def __repr__(self):
        return self.__str__()



class Activity(models.Model):
    # TODO: 暂时只做学习，在线学习，活动
    ACTIVITY_TYPE = (
        ('S', 'study'),
        ('O', 'online_study'),
        ('A', 'activity'),
    )
    name = models.CharField(verbose_name=u'活动名称', max_length=100, default='test activity', unique=True)
    activity_creator = models.ForeignKey(UserProfile, verbose_name=u'创建人', on_delete=models.SET_NULL,
                                         related_name='activity_creator', null=True)
    created_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name=u'更新时间', auto_now=True)
    start_time = models.DateTimeField(verbose_name=u'开始时间', )
    end_time = models.DateTimeField(verbose_name=u'结束时间', )
    activity_type = models.CharField(verbose_name=u'活动类型', max_length=1, choices=ACTIVITY_TYPE)
    cover = models.ImageField(verbose_name=u'封面', upload_to='cover/', null=True, blank=True)
    outline = models.TextField(verbose_name=u'大纲', null=True, blank=True)
    introduction = models.TextField(verbose_name=u'简介', null=True, blank=True)
    details = JSONField(verbose_name=u'活动细节', blank=True)

    project = models.ForeignKey(Project, verbose_name=u'项目', on_delete=models.CASCADE, related_name='activity')

    class Meta:
        verbose_name_plural = verbose_name = u'活动'
        db_table = 'activity'

    def __str__(self):
        return '<Activity> ID: {0} Name:{1}'.format(self.id, self.name)

    def __repr__(self):
        return self.__str__()


class Material(models.Model):
    name = models.CharField(verbose_name=u'材料名称', max_length=100, default='test material', unique=True)
    activity = models.ManyToManyField(Activity, verbose_name=u'活动', related_name='material')
    introduction = models.TextField(verbose_name=u'简介', null=True, blank=True)
    owner = models.ForeignKey(UserProfile, verbose_name=u'创建人', on_delete=models.SET_NULL, null=True, blank=True)
    created_time = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)
    resource = models.FileField(verbose_name=u'资源地址', upload_to='material/', null=True, blank=True)

    class Meta:
        verbose_name_plural = verbose_name = u'资料/材料'
        db_table = 'material'

    def __str__(self):
        m = Material.objects.get(id=self.id)
        return '<Material> ID:{0} Name:{1}'.format(self.id, self.name)

    def __repr__(self):
        return self.__str__()