from django.contrib import admin
from houseofapps.hackathon.models import Hackathon, Navigation, Sponsors, Prize, Program, Committee, Sss

class HackathonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'email', 'phone', 'active')
    list_filter = ('active','form_active')


class NavigationAdmin(admin.ModelAdmin):
    list_display = ('name','order', 'hackathon')


class SponsorsAdmin(admin.ModelAdmin):
    list_display = ('name', 'hackathon')


class PrizeAdmin(admin.ModelAdmin):
    list_display = ('name', 'order','hackathon')


class ProgramAdmin(admin.ModelAdmin):
    list_display = ('title', 'day', 'time_interval', 'hackathon')


class CommitteeAdmin(admin.ModelAdmin):
    list_display = ('name', 'title','business', 'jury', 'mentor', 'hackathon')
    list_filter = ('jury', 'mentor',)


class SssAdmin(admin.ModelAdmin):
    list_display = ('question','order','hackathon' )


admin.site.register(Hackathon, HackathonAdmin)
admin.site.register(Navigation, NavigationAdmin)
admin.site.register(Sponsors, SponsorsAdmin)
admin.site.register(Prize, PrizeAdmin)
admin.site.register(Program, ProgramAdmin)
admin.site.register(Committee, CommitteeAdmin)
admin.site.register(Sss, SssAdmin)
