from django.contrib import admin

from motherearth.auth_app.models import MotherearthUser, Profile


@admin.register(MotherearthUser)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

