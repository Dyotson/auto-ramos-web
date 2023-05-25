from django.shortcuts import render, redirect
from .forms import ScheduleTaskForm, ReLogin
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .backend import verificar_sesion
from django.contrib.auth.decorators import login_required
from .models import Planner, Cookies
import logging
from .tasks import reservar
from datetime import datetime, timedelta
import json
***REMOVED***

def require_state(required_state: bool, redirect_view_name: str = 'index', required_states: set = {***REMOVED***:
    ***REMOVED***Decorador para proteger views por estado de toma***REMOVED***

    def decorator(view_func***REMOVED***:
        def wrapper(request, *args, **kwargs***REMOVED***:
            user = request.user
            try:
                planner = Planner.objects.get(user=user***REMOVED***
            except Exception:
                planner = None
            if required_state:
                if planner is None:
                    return redirect(reverse(redirect_view_name***REMOVED***
                
                if planner.estado_toma not in required_states:
                    return redirect(reverse(redirect_view_name***REMOVED***
                ***REMOVED***
                    return view_func(request, *args, **kwargs***REMOVED***
            ***REMOVED***
                if planner is not None:
                    return redirect(reverse(redirect_view_name***REMOVED***
                ***REMOVED***
                    return view_func(request, *args, **kwargs***REMOVED***
        
        return wrapper
    return decorator


logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname***REMOVED***s***REMOVED*** (%(threadName***REMOVED***-9s***REMOVED*** %(message***REMOVED***s',***REMOVED***


def index(request***REMOVED***:
    return render(request, 'autoramos/home.html'***REMOVED***

# If not logged in redirect to path specified in
# LOGIN_URL in autoramosweb/settings.py
@login_required(***REMOVED***
@require_state(False, redirect_view_name="class_log"***REMOVED***
def reserva_ramos(response***REMOVED***:
    if response.method == 'POST':
        form = ScheduleTaskForm(response.POST***REMOVED***
        if form.is_valid(***REMOVED***:
            user = response.user
            
            try:
                planner = Planner.objects.get(user=user***REMOVED***
                planner.nrc1=form.cleaned_data['nrc1'***REMOVED***
                planner.nrc2=form.cleaned_data['nrc2'***REMOVED***
                planner.nrc3=form.cleaned_data['nrc3'***REMOVED***
                planner.nrc4=form.cleaned_data['nrc4'***REMOVED***
                planner.nrc5=form.cleaned_data['nrc5'***REMOVED***
                planner.nrc6=form.cleaned_data['nrc6'***REMOVED***
                planner.estado_toma=1
                
                
            except:
                hora_agendada = datetime.combine(form.cleaned_data['date'***REMOVED***, form.cleaned_data['time'***REMOVED***
                planner = Planner.objects.create(user=user, nrc1=form.cleaned_data['nrc1'***REMOVED***, nrc2=form.cleaned_data['nrc2'***REMOVED***, nrc3=form.cleaned_data['nrc3'***REMOVED***, 
                                                 nrc4=form.cleaned_data['nrc4'***REMOVED***, nrc5=form.cleaned_data['nrc5'***REMOVED***, nrc6=form.cleaned_data['nrc6'***REMOVED***,
                                                 estado_toma=1, hora_agendada=hora_agendada***REMOVED***
                
            planner.save(***REMOVED***

            complete_datetime = datetime.combine(form.cleaned_data['date'***REMOVED***, form.cleaned_data['time'***REMOVED***
            gmt_adjusted = complete_datetime + timedelta(hours=4***REMOVED*** # Max culiao genio
            reservar.apply_async(
                args=[response.user.username***REMOVED***,
                eta = gmt_adjusted
            ***REMOVED***

            #Usar info usuario
            return redirect(reverse('class_log'***REMOVED***

    ***REMOVED***
        form = ScheduleTaskForm(***REMOVED***
    return render(response, 'autoramos/reserva.html', {'form': form***REMOVED***

@login_required(***REMOVED***
@require_state(True, redirect_view_name="reserva_ramos", required_states={1,4***REMOVED***
def editar_planner(response***REMOVED***:
    Planner.objects.get(user=response.user***REMOVED***.delete(***REMOVED***
    return redirect(reverse('reserva_ramos'***REMOVED***


def equipo(response***REMOVED***:
    f = open(os.path.join("static", "assets", "data", "team.json"***REMOVED***, 'r', encoding="utf8"***REMOVED***
    data = json.load(f***REMOVED***
    f.close(***REMOVED***

    return render(response, 'autoramos/equipo.html', {
        "equipo": data
***REMOVED***

def faq(response***REMOVED***:
    f = open(os.path.join("static", "assets", "data", "faq.json"***REMOVED***, 'r', encoding="utf8"***REMOVED***
    data = json.load(f***REMOVED***
    f.close(***REMOVED***

    return render(response, 'autoramos/faq.html', {
        'faq': data
***REMOVED***

def about(response***REMOVED***:
    return render(response, 'autoramos/about.html'***REMOVED***

@login_required
@require_state(True, redirect_view_name="reserva_ramos", required_states={1, 2, 3, 4***REMOVED***
def class_log(response***REMOVED***:
    if response.method=='POST':
        usuario = response.user
        data = Planner.objects.filter(user=usuario***REMOVED***.values('estado_toma', 'nrc1', 'nrc2','nrc3', 'nrc4', 'nrc5', 'nrc6','hora_agendada'***REMOVED***.first(***REMOVED***
        data['hora_agendada'***REMOVED*** = (data['hora_agendada'***REMOVED*** - timedelta(hours=4***REMOVED***.strftime("%d/%m/%Y a las %H:%M hrs"***REMOVED***
        data = {"data": data***REMOVED***
        
        return JsonResponse(data***REMOVED***
    ***REMOVED***
        # Data: Sea igual al enum que le mandemos (1 al 4***REMOVED***
        # 1: Reservados | 2: Tomando | 3: Listo | 4: Error
        return render(response, 'autoramos/log.html'***REMOVED*** 

@login_required
def relogin(response***REMOVED***:
    if response.method == 'POST':
        form = ReLogin(response.POST***REMOVED***
        if form.is_valid(***REMOVED***:
            test = verificar_sesion(response.user.username, form.cleaned_data['password'***REMOVED***
            if test:
                cookie = Cookies.objects.get(user=response.user.username***REMOVED***
                cookie.estado = True
                cookie.save(***REMOVED***
                return HttpResponseRedirect(reverse('reserva_ramos'***REMOVED***
            ***REMOVED***
                form = ReLogin(***REMOVED***
                return render(response, 'autoramos/relogin.html', {'form': form***REMOVED***
    ***REMOVED***
        form = ReLogin(***REMOVED***
    return render(response, 'autoramos/relogin.html', {'form': form***REMOVED***

