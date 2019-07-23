from django.contrib import admin
from django.apps import apps
# Register your models here.
""" 
admin.site.register(UserProfile)
admin.site.register(Organization)
admin.site.register(VerifyCode)
 """
# register all
all_models = apps.get_app_config('users').get_models()
for model in all_models:
    try:
        admin.site.register(model)
    except:
        pass