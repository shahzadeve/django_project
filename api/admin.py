from django.contrib import admin
from .models import *
from django.contrib.auth.models import User

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    def user(self, obj):
        
        return obj.user.username

    list_display = ('user','id', 'rating', 'description', 'watchlist', 'created', 'update', 'active')
    list_display_links = ('user','id', 'rating')
    list_filter = ('rating', 'active', 'created', 'update')

    search_fields = ('description', 'watchlist__title')  
    list_editable = ('active',)

@admin.register(StreamPlatform)
class StreamPlatformAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'about', 'website')
    list_display_links = ('id', 'name')
    
    search_fields = ('name', 'about')
    

@admin.register(Watchlist)
class WatchlistAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'storyline', 'platform', 'active', 'created')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'storyline')
