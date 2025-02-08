from django.contrib import admin
from .models import Stock,Category

# Register your models here.
class Stockcreateadmin(admin.ModelAdmin):
    list_display = ['category', 'item_name', 'quantity']
    list_filter = ['category']
    search_fields = ['category', 'item_name']



admin.site.register(Stock,Stockcreateadmin)
admin.site.register(Category)


