from django.contrib import admin

from motherearth.web.models import Plants, Product, Place, Event, Post


@admin.register(Plants)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Place)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Event)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class ProfileAdmin(admin.ModelAdmin):
    pass

