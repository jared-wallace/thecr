from django.contrib import admin
from about.models import Pastor, Beliefs, WorshipTeam
from about.models import Video, Music, SermonSeries

class PastorAdmin(admin.ModelAdmin):
    list_display = ('name', 'photo', 'bio')

class BeliefsAdmin(admin.ModelAdmin):
    list_display = ('text',)

class SermonSeriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'body')

class WorshipTeamAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')

class MusicAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

admin.site.register(Pastor, PastorAdmin)
admin.site.register(Beliefs, BeliefsAdmin)
admin.site.register(WorshipTeam, WorshipTeamAdmin)
admin.site.register(Music, MusicAdmin)
admin.site.register(Video, VideoAdmin)
