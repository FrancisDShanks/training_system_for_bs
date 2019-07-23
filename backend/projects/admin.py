from django.contrib import admin
from django.apps import apps
# Register your models here.
""" 
admin.site.register(Project)
admin.site.register(Activity)
admin.site.register(Material)
 """

all_models = apps.get_app_config('projects').get_models()
for model in all_models:
    try:
        admin.site.register(model)
    except:
        pass