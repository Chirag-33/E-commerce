from django.contrib import admin
from .models import Vendor,Product,Comment,ItemStatu
# Register your models here.
admin.site.register(Vendor)

admin.site.register(Product)
admin.site.register(ItemStatu)
# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name','price','category')
#     list_filter = ('category',)