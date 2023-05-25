from django.contrib import admin
from .models import Planner, Cookies

class PlannerAdmin(admin.ModelAdmin***REMOVED***:
    list_display = ('user', 'nrc1', 'nrc2', 'nrc3', 'nrc4', 'nrc5', 'nrc6', 'hora_agendada'***REMOVED***
    search_fields = ['user'***REMOVED***

admin.site.register(Planner, PlannerAdmin***REMOVED***

class CookiesAdmin(admin.ModelAdmin***REMOVED***:
    list_display = ('user', 'cookie_value'***REMOVED***

admin.site.register(Cookies, CookiesAdmin***REMOVED***
