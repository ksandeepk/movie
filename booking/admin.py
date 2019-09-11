from django.contrib import admin
from .models import udata,movie,theatre
# Register your models here.
class movieAdmin(admin.ModelAdmin):
    list_display = ('movie_name','cast','director','image','language')

class udataAdmin(admin.ModelAdmin):
    list_display = ('name','email','mobile','password')

class theatreAdmin(admin.ModelAdmin):
    list_display =('theatre_name','address')

admin.site.register(udata,udataAdmin)
admin.site.register(movie,movieAdmin)
admin.site.register(theatre,theatreAdmin)