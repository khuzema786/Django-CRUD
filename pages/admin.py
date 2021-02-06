from django.contrib import admin
from .models import Form

# Register your models here.
class FormAdmin(admin.ModelAdmin):    
    list_display = ('id', 'first_name', 'last_name', 'designation', 'industry', 'website', 'created_date') # Display these table columns
    list_display_links = ('id', 'first_name', 'last_name') # Make fieldnames clickable
    search_fields = ('first_name', 'last_name', 'designation', 'industry', 'website') # Search by fieldnames
    list_filter = ('first_name', 'last_name', 'designation', 'industry') # Filter as per fieldnames, Note: If just one value in tuple then we add a trailing commma

admin.site.register(Form, FormAdmin)