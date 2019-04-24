from django.db import models
from django.contrib.postgres.fields import JSONField
from backend.users.models import Organization, UserProfile


# Create your models here.
class Project(models.Model):
    name = models.CharField(verbose_name='', max_length=100, default='test project')
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, related_name='project', null=True)
    location = models.CharField(max_length=200, default='some where', blank=True)
    introduction = models.TextField(blank=True)
    cover = models.ImageField(upload_to='cover/', null=True, blank=True)
    cost_budget = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    project_manager = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, related_name='project_manager', null=True, blank=True)
    project_creator = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, related_name='project_creator', null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True)

    class Meta:
        verbose_name = 'Project'
        db_table = 'project'

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
    name = models.CharField(max_length=100, default='test activity')
    activity_creator = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, related_name='activity_creator', null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    activity_type = models.CharField(max_length=1, choices=ACTIVITY_TYPE)
    cover = models.ImageField(upload_to='cover/', null=True, blank=True)
    outline = models.TextField(null=True, blank=True)
    introduction = models.TextField(null=True, blank=True)
    # material = models.FileField(upload_to='material/', null=True, blank=True)
    details = JSONField()

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='activity')

    class Meta:
        verbose_name = 'activity'
        db_table = 'activity'

    def __str__(self):
        return '<Activity> ID: {0} Name:{1}'.format(self.id, self.name)

    def __repr__(self):
        return self.__str__()


class Material(models.Model):
    name = models.CharField(max_length=100, default='test material')
    activity = models.ManyToManyField(Activity, related_name='material')
    introduction = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    resource = models.FileField(upload_to='material/', null=True, blank=True)

    class Meta:
        verbose_name = 'material'
        db_table = 'material'

    def __str__(self):
        m = Material.objects.get(id=self.id)
        return '<Material> ID:{0} Name:{1}'.format(self.id, self.name)

    def __repr__(self):
        return self.__str__()