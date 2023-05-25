from django.db import models
from django.conf import settings

# Guarda los NRC's y los asocia a un usuario
class Planner(models.Model***REMOVED***:
    ***REMOVED***Modelo que guarda los NRC con un foreign key al usuario***REMOVED***
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE***REMOVED***

    nrc1 = models.CharField(max_length=5***REMOVED***
    nrc2 = models.CharField(max_length=5***REMOVED***
    nrc3 = models.CharField(max_length=5***REMOVED***
    nrc4 = models.CharField(max_length=5***REMOVED***
    nrc5 = models.CharField(max_length=5***REMOVED***
    nrc6 = models.CharField(max_length=5***REMOVED***
    estado_toma = models.IntegerField(null=True***REMOVED***
    hora_agendada = models.DateTimeField(blank=True***REMOVED***
    failed = models.CharField(max_length=3***REMOVED***
    
# Guarda los cookies del usuario
class Cookies(models.Model***REMOVED***:
    user = models.CharField(max_length=255, unique=True***REMOVED***
    cookie_value = models.CharField(max_length=2000, blank=True, null=True***REMOVED***
    estado = models.BooleanField(default=True***REMOVED***
