from django.contrib import admin
from cms.models import Banners, Faq, HomepageInfo

class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'image')

class FaqAdmin(admin.ModelAdmin):
    list_display = ('question',)

class HomepageInfoAdmin(admin.ModelAdmin):
    list_display = ('phone', 'email')

admin.site.register(Banners, BannerAdmin)
admin.site.register(Faq, FaqAdmin)
admin.site.register(HomepageInfo, HomepageInfoAdmin)
