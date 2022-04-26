from django.contrib import admin

from motherearth.web.models import Plants, Product, Places, Post, Type, Kind, Event, Craft, Thanks


@admin.register(Plants)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner')


@admin.register(Product)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Places)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Event)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user')


@admin.register(Type)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Kind)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Craft)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Thanks)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')