# Generated by Django 2.2 on 2019-04-29 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='name',
            field=models.CharField(default='test activity', max_length=100, unique=True, verbose_name='活动名称'),
        ),
        migrations.AlterField(
            model_name='material',
            name='name',
            field=models.CharField(default='test material', max_length=100, unique=True, verbose_name='材料名称'),
        ),
        migrations.AlterField(
            model_name='project',
            name='cost',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='实际花费'),
        ),
        migrations.AlterField(
            model_name='project',
            name='cost_budget',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='花费预算'),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(default='test project', max_length=100, unique=True, verbose_name='项目名称'),
        ),
        migrations.AlterField(
            model_name='project',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='定价'),
        ),
    ]