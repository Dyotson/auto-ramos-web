from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'***REMOVED***,
    path('reserva/', views.reserva_ramos, name='reserva_ramos'***REMOVED***,
    path('editar/', views.editar_planner, name='editar_planner'***REMOVED***,
    path('equipo/', views.equipo, name='equipo'***REMOVED***,
    path('faq/', views.faq, name="faq"***REMOVED***,
    path('about/', views.about, name="about"***REMOVED***,
    path('reserva/confirmacion/', views.class_log, name="class_log"***REMOVED***,
    path('relogin/', views.relogin, name="relogin"***REMOVED***,

***REMOVED***
