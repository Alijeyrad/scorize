from django.contrib import admin
from .models import University, City, Country

# Register your models here.

@admin.register(University)
class UserAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_established'
    empty_value_display = '-empty-'
    list_display = ('name', 'uni_type', 'city', 'total_students',)
    search_fields = ['name', 'city', 'overview',]
    list_filter = ('city', 'uni_type',)


admin.site.register(Country)

admin.site.register(City)