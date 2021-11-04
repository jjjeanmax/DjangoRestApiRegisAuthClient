from django.contrib import admin
from .models import Client


class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'adress', 'photo_tag')
    readonly_fields = ['photo_tag']
    fields = ('first_name', 'last_name', 'adress', 'email', 'username', 'photo')


admin.site.register(Client, ClientAdmin)
