from django.contrib import admin

from .models import Usuario

# Register your models here.

@admin.register(Usuario)

class AdminUser(admin.ModelAdmin):
	list_display = ('name' , 'email' , 'donador')