from django.contrib import admin

from phones import models


@admin.register(models.Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'image', 'release_date', 'lte_exists', 'slug']
    list_filter = ['name', 'price', 'lte_exists']


try:
    admin.site.register(models.Phone, PhoneAdmin)
except:
    reg_result = 'The model Phone is already registered'
