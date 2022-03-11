from django.contrib import admin
from .models import Profile, Country, House, Patronus

# Register your models here.

class CountryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Country, CountryAdmin)

class HouseAdmin(admin.ModelAdmin):
    pass

admin.site.register(House, HouseAdmin)

class PatronusAdmin(admin.ModelAdmin):
    pass

admin.site.register(Patronus, PatronusAdmin)

class ProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile, ProfileAdmin)