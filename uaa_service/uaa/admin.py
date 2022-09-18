from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Permission
from django.apps import apps
from .models import User,Role

# Register your models here.
class UserClass(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,
        ('Additional Info',
         {
            "fields": (
                'role',
            ),
        }),
    )

fields = list(UserAdmin.fieldsets)
fields[1] = ('personal Info', {'fields':('first_name','last_name','email','username','email','role')})
UserAdmin.fieldsets = tuple(fields)

app = apps.get_app_config('graphql_auth')
for model_name, model in app.models.items():
    admin.site.register(model)

admin.site.register(User,UserClass)
admin.site.register(Role)
admin.site.register(Permission)
