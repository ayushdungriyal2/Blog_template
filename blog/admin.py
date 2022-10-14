from django.contrib import admin

# Register your models here.

from .models import WebsiteInfo, Category, SinlgeBlogInfo
admin.site.register(WebsiteInfo)
admin.site.register(Category)
admin.site.register(SinlgeBlogInfo)
