from django.contrib import admin
from .models import Banner


# Register your models here.

# Blog模型的管理器
class BannerAdmin(admin.ModelAdmin):
    list_display=["title","orders","is_show"]

# 在admin中注册绑定
admin.site.register(Banner, BannerAdmin)


from .models import Nav
class NavModelAdmin(admin.ModelAdmin):
    list_display=["title","link","is_show","is_site","position"]
admin.site.register(Nav, NavModelAdmin)
