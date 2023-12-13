from django.contrib import admin
from django.contrib.contenttypes.admin import InlineModelAdmin
from .models import *


@admin.register(Method)
class MethodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ['name']


@admin.register(WebSite)
class WebSiteAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address',)
    list_display_links = ['name']


class SpiderProductInline(admin.TabularInline):
    model = SpiderProduct
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ['name']
    inlines = [SpiderProductInline, ]


@admin.register(Extract)
class ExtractAdmin(admin.ModelAdmin):
    list_display = ('id', 'spider', 'datetime', 'price_net', 'price_gross', 'variant', 'percent_change', 'status',)
    list_display_links = ['spider']

