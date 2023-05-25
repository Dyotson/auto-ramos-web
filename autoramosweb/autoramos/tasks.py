from celery import shared_task
from datetime import datetime
from .backend import tomar_ramos, revalidar_cookies


@shared_task
def reserva_creada(mes, dia, horas, minutos***REMOVED***:
    datetime_str = f'{dia***REMOVED***/{mes***REMOVED***/2022 {horas***REMOVED***:{minutos***REMOVED***:00'
    date_time_obj = datetime.strptime(datetime_str, '%d/%m/%y %H:%M:%S'***REMOVED***

    return date_time_obj


@shared_task
def reservar(usuario***REMOVED***:
    tomar_ramos(usuario***REMOVED***
    return None


@shared_task(name='revalidar_cookie'***REMOVED***
def celery_revalidar_cookie(***REMOVED***:
    revalidar_cookies(***REMOVED***
    return None
