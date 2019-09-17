from django.contrib import admin
from .models import *

# Register your models here.
class MenuAdminHot(admin.ModelAdmin):
	list_display =('title_hot', 'weight_hot', 'price_hot', 'date_hot_add', 'image_hot')
	prepopulated_fields = {"slug_hot": ("title_hot",)}

admin.site.register(MenuKitchenHot, MenuAdminHot)