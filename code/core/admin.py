from django.contrib import admin
from django.contrib.auth.models import Group, User

from .models import ClienteModel

# Register your models here.

admin.site.site_header = "GreenTrade"

admin.site.unregister(Group)
admin.site.unregister(User)

class ClienteModelAdmin(admin.ModelAdmin):
    list_filter = ('nome',)

admin.site.register(ClienteModel, ClienteModelAdmin)
