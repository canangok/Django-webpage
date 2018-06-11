from django.contrib import admin
from houseofapps.main.models import App


class AppAdmin(admin.ModelAdmin):
    pass

admin.site.register(App, AppAdmin)
