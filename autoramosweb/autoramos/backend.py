# Django
from django.conf import settings
from .models import Cookies, Planner
from django.contrib.auth.models import User
from django.core.mail import send_mail

# Web
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from bs4 import BeautifulSoup
from captcha.solver import solve_captcha
from captcha.assets import path_to_image

# Misc
import json
***REMOVED***
import base64
import logging
from threading import Thread


def init_driver(***REMOVED***:
    options = Options(***REMOVED***
    # Correr Headless
    options.headless = True
    options.add_experimental_option("excludeSwitches", ["enable-automation"***REMOVED***
    options.add_experimental_option('useAutomationExtension', False***REMOVED***
    driver = webdriver.Remote(command_executor=settings.SELENIUM_REMOTE_URL, options=options, desired_capabilities=DesiredCapabilities.CHROME***REMOVED***
    driver.implicitly_wait(5***REMOVED***
    return driver


logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname***REMOVED***s***REMOVED*** (%(threadName***REMOVED***-9s***REMOVED*** %(message***REMOVED***s',***REMOVED***


def tomar_ramos(usuario, segunda_toma=False***REMOVED***:  # Esto debe ser de una corrida ya que usa Sessions
    LOGIN_ENDPOINT = "https://ssb.uc.cl/ERPUC/twbkwbis.P_WWWLogin"
    MENU_ENDPOINT = "https://ssb.uc.cl/ERPUC/twbkwbis.P_GenMenu?name=bmenu.P_MainMnu"
    cookie = Cookies.objects.filter(user=usuario***REMOVED***.values('cookie_value'***REMOVED***[0***REMOVED***['cookie_value'***REMOVED***

    # Planner toma foreign id, entonces debemos obtenerlo
    id_usuario = User.objects.get(username=usuario***REMOVED***.id
    try:
        estado = Planner.objects.get(user=id_usuario***REMOVED***
    except:
        return

    with open('base_cookie.json'***REMOVED*** as f:
        data = json.load(f***REMOVED***

    data[0***REMOVED***["value"***REMOVED*** = cookie

    driver = init_driver(***REMOVED***
    driver.get(LOGIN_ENDPOINT***REMOVED***
    for cookie in data:
        driver.add_cookie(cookie***REMOVED***
    driver.get(MENU_ENDPOINT***REMOVED***

    estado.estado_toma = 2
    estado.save(***REMOVED***
    # Ya logeado, printea que va a tomar ramos y redirige el output
    print('\nChequeando credenciales...'***REMOVED***

    try:
        # ENCONTRAR EL LINK DE AGREGAR O ELIMINAR CLASES
        agregar = driver.find_element(by=By.XPATH, value="/html/body/div[3***REMOVED***/table[1***REMOVED***/tbody/tr[2***REMOVED***/td[2***REMOVED***/a"***REMOVED***
        print('¡Credenciales aceptadas!'***REMOVED***
        agregar.click(***REMOVED***
    except Exception as err:
        print(f"Debug: {err***REMOVED***"***REMOVED***
        print(f'Las credenciales de {usuario***REMOVED*** fueron rechazadas. No se pudieron tomar ramos'***REMOVED***
        mail = User.objects.get(username=usuario***REMOVED***.email
        send_mail(
        'AutoRamosWeb Error',
        'Hola, hemos detectado un fallo en tu toma de ramos: Credenciales UC rechazadas, , porfavor hacer relogin en: autoramos.xyz/relogin/',
        os.environ.get('EMAIL_HOST_USER'***REMOVED***,
        [mail***REMOVED***,
        fail_silently=False,
        ***REMOVED***
        estado.estado_toma = 4
        estado.save(***REMOVED***
        driver.quit(***REMOVED***
        return
    logging.debug('\nTomando ramos...'***REMOVED***


    def solve_period_captcha(captcha_button, text_c, usuario***REMOVED***:
        # SOLUCIONAR CAPTCHA
        html = driver.page_source
        scrapeo_img_base64(html, usuario***REMOVED***
        captcha = path_to_image(f'{usuario***REMOVED***.dib'***REMOVED*** # Aqui se carga el captcha
        solution = solve_captcha(captcha***REMOVED*** # Aqui se resuelve el captcha
        text_c.send_keys(solution***REMOVED***
        # APRETAR SUBMIT
        captcha_button.click(***REMOVED***
    if not segunda_toma:
        try:
            # Ingresa a sector seleccionar periodo
            text_c = driver.find_element(by=By.XPATH, value='//*[@id="captcha_id"***REMOVED***'***REMOVED***
            captcha_button = driver.find_element(by=By.XPATH, value='/html/body/div[3***REMOVED***/form/p/button/div/div/div'***REMOVED***
            solve_period_captcha(captcha_button, text_c, usuario***REMOVED***
        except NoSuchElementException as err:
            print("Captcha no encontrado, asumiendo estudiante PIANE"***REMOVED***
            non_captcha_button = driver.find_element(by=By.XPATH, value='/html/body/div[3***REMOVED***/form/input'***REMOVED***
            non_captcha_button.click(***REMOVED***
        except:
            # Asumiendo error con el resolvedor de captcha
            print(f'Error al seleccionar el semestre de {usuario***REMOVED***'***REMOVED***
            mail = User.objects.get(username=usuario***REMOVED***.email
            send_mail(
            'AutoRamosWeb Error',
            'Hola, hemos detectado un fallo en tu toma de ramos: Error al seleccionar el semestre, porfavor hacer relogin en: autoramos.xyz/relogin/',
            os.environ.get('EMAIL_HOST_USER'***REMOVED***,
            [mail***REMOVED***,
            fail_silently=False,
            ***REMOVED***
            estado.estado_toma = 4
            estado.save(***REMOVED***
            driver.quit(***REMOVED***
            return

    # Seleccionar plan de estudios
    try:
        # Seleccionar primer plan de estudio
        select = Select(driver.find_element(By.XPATH, '//*[@id="st_path_id"***REMOVED***'***REMOVED***
        select.select_by_index(1***REMOVED***
        # Submit
        driver.find_element(By.XPATH, '/html/body/div[3***REMOVED***/form/input[19***REMOVED***'***REMOVED***.click(***REMOVED***
    except:
        print(f'Error al seleccionar el plan de estudio de {usuario***REMOVED***'***REMOVED***
        mail = User.objects.get(username=usuario***REMOVED***.email
        send_mail(
        'AutoRamosWeb Error',
        'Hola, hemos detectado un fallo en tu toma de ramos: Error al seleccionar el plan de estudio | Fuera de horario de toma, porfavor hacer relogin en: autoramos.xyz/relogin/',
        os.environ.get('EMAIL_HOST_USER'***REMOVED***,
        [mail***REMOVED***,
        fail_silently=False,
        ***REMOVED***
        estado.estado_toma = 4
        estado.save(***REMOVED***
        driver.quit(***REMOVED***
        return

    # Tomar ramos
    try:
        planner = estado
        crn_id1 = driver.find_element(by=By.XPATH, value='//*[@id="crn_id1"***REMOVED***'***REMOVED***
        crn_id2 = driver.find_element(by=By.XPATH, value='//*[@id="crn_id2"***REMOVED***'***REMOVED***
        crn_id3 = driver.find_element(by=By.XPATH, value='//*[@id="crn_id3"***REMOVED***'***REMOVED***
        btn_cambios = driver.find_element(by=By.XPATH, value='/html/body/div[3***REMOVED***/form/input[19***REMOVED***'***REMOVED***

        if not segunda_toma:
            crn_id1.send_keys(planner.nrc1***REMOVED***
            crn_id2.send_keys(planner.nrc2***REMOVED***
            crn_id3.send_keys(planner.nrc3***REMOVED***
            btn_cambios.click(***REMOVED***
        ***REMOVED***
            failed_string = planner.failed
            print(f"DEBUG FAILED STRING: {failed_string***REMOVED***"***REMOVED***
            if '1' in failed_string:
                crn_id1.send_keys(planner.nrc4***REMOVED***
            if '2' in failed_string:
                crn_id2.send_keys(planner.nrc5***REMOVED***
            if '3' in failed_string:
                crn_id3.send_keys(planner.nrc6***REMOVED***
            btn_cambios.click(***REMOVED***
        html = driver.page_source
    except:
        print(f'Error al tomar los ramos de {usuario***REMOVED***'***REMOVED***
        mail = User.objects.get(username=usuario***REMOVED***.email
        send_mail(
        'AutoRamosWeb Error',
        'Hola, hemos detectado un fallo en tu toma de ramos: Error al tomar los ramos (NRC***REMOVED***, porfavor hacer relogin en: autoramos.xyz/relogin/',
        os.environ.get('EMAIL_HOST_USER'***REMOVED***,
        [mail***REMOVED***,
        fail_silently=False,
        ***REMOVED***
        estado.estado_toma = 4
        estado.save(***REMOVED***
        driver.quit(***REMOVED***
        return
    print(f'\n¡Ramos tomados para {usuario***REMOVED***!'***REMOVED***

    # Check logged in or not
    cookie = str(driver.get_cookies(***REMOVED***[0***REMOVED***["value"***REMOVED***

    # If cookie exists
    if cookie != 'set':
        if Cookies.objects.filter(user=usuario***REMOVED***.exists(***REMOVED***:
            Cookies.objects.filter(user=usuario***REMOVED***.update(cookie_value=cookie***REMOVED***
        ***REMOVED***
            Cookies.objects.create(user=usuario, cookie_value=cookie***REMOVED***

    failed_nrcs = scrapeo_pagina_final(html***REMOVED***
    if failed_nrcs and not segunda_toma:
        failed_ids = ""
        failed_nrcs_string = [str(x***REMOVED*** for x in failed_nrcs***REMOVED***
        print(f"DEBUG FAILED STRINGS: {failed_nrcs_string***REMOVED***"***REMOVED***
        if planner.nrc1 in failed_nrcs_string:
            failed_ids += "1"
        if planner.nrc2 in failed_nrcs_string:
            failed_ids += "2"
        if planner.nrc3 in failed_nrcs_string:
            failed_ids += "3"
        planner.failed = failed_ids
        planner.save(***REMOVED***
        return tomar_ramos(usuario, True***REMOVED***
    ***REMOVED***
        estado.estado_toma = 3
        estado.save(***REMOVED***
        driver.quit(***REMOVED***

        failed_new = [str(x***REMOVED*** for x in scrapeo_pagina_final(html***REMOVED***
        nrc_tomados = [***REMOVED***
        nrc_fallados = [***REMOVED***

        if '1' in planner.failed:
            nrc_fallados.append(planner.nrc1***REMOVED***
            if planner.nrc4 not in failed_new:
                nrc_tomados.append(planner.nrc4***REMOVED***
            ***REMOVED***
                nrc_fallados.append(planner.nrc4***REMOVED***
        ***REMOVED***
            nrc_tomados.append(planner.nrc1***REMOVED***
        if '2' in planner.failed:
            nrc_fallados.append(planner.nrc2***REMOVED***
            if planner.nrc5 not in failed_new:
                nrc_tomados.append(planner.nrc5***REMOVED***
            ***REMOVED***
                nrc_fallados.append(planner.nrc5***REMOVED***
        ***REMOVED***
            nrc_tomados.append(planner.nrc2***REMOVED***
        if '3' in planner.failed:
            nrc_fallados.append(planner.nrc3***REMOVED***
            if planner.nrc6 not in failed_new:
                nrc_tomados.append(planner.nrc6***REMOVED***
            ***REMOVED***
                nrc_fallados.append(planner.nrc6***REMOVED***
        ***REMOVED***
            nrc_tomados.append(planner.nrc3***REMOVED***

        return finalizar_toma(usuario, nrc_tomados, nrc_fallados***REMOVED***


def finalizar_toma(usuario, nrc_tomados, nrc_fallados***REMOVED***:
    print(f'\nFinalizando toma de ramos para {usuario***REMOVED***'***REMOVED***
    # TODO Mail usuario de exito
    mail = User.objects.get(username=usuario***REMOVED***.email
    send_mail(
    'AutoRamosWeb Exito',
    f"Hola, te informamos que hemos tomado tus ramos exitosamente! Los nrc's que fueron tomados son: {', '.join(nrc_tomados***REMOVED*** y los que fallaron fueron: {', '.join(nrc_fallados***REMOVED***",
    os.environ.get('EMAIL_HOST_USER'***REMOVED***,
    [mail***REMOVED***,
    fail_silently=False,
    ***REMOVED***

    # Eliminar planner
    user_id = User.objects.get(username=usuario***REMOVED***.id
    Planner.objects.get(user=user_id***REMOVED***.delete(***REMOVED***

    # TODO Manejo de cookie
    cookie = Cookies.objects.get(user=usuario***REMOVED***
    # cookie.estado = False
    # cookie.save(***REMOVED***
    # cookie.delete(***REMOVED***
    return


# Login
def verificar_sesion(usuario, password***REMOVED*** -> bool:
    # (True/False***REMOVED***
    LOGIN_ENDPOINT = "https://ssb.uc.cl/ERPUC/twbkwbis.P_WWWLogin"
    out: bool

    driver = init_driver(***REMOVED***
    driver.get(LOGIN_ENDPOINT***REMOVED***
    username_field = driver.find_element(by=By.XPATH, value="//*[@id='UserID'***REMOVED***"***REMOVED***
    username_field.send_keys(usuario***REMOVED***

***REMOVED***word_field = driver.find_element(by=By.XPATH, value="/html/body/div[3***REMOVED***/form/table/tbody/tr[2***REMOVED***/td[2***REMOVED***/input"***REMOVED***
***REMOVED***word_field.send_keys(password***REMOVED***

    access_button = driver.find_element(by=By.XPATH, value="/html/body/div[3***REMOVED***/form/p/input"***REMOVED***
    access_button.click(***REMOVED***

    # Check logged in or not
    cookie = str(driver.get_cookies(***REMOVED***[0***REMOVED***["value"***REMOVED***

    # If cookie exists
    if cookie != 'set':
        if Cookies.objects.filter(user=usuario***REMOVED***.exists(***REMOVED***:
            Cookies.objects.filter(user=usuario***REMOVED***.update(cookie_value=cookie***REMOVED***
        ***REMOVED***
            Cookies.objects.create(user=usuario, cookie_value=cookie***REMOVED***
        out = True
    ***REMOVED***
        out = False

    driver.quit(***REMOVED***
    return out

# TODO: Implementar que revise todas las cookies cada 30 minutos y de ahi saque las que estan expiradas
def revalidar_cookies(***REMOVED***:
    print(f"<><> Debug: revalidar_cookies llamado! <><>"***REMOVED***

    with open('base_cookie.json'***REMOVED*** as f:
            data = json.load(f***REMOVED***

    def validate_cookie(item, data=data***REMOVED***:
        LOGIN_ENDPOINT = "https://ssb.uc.cl/ERPUC/twbkwbis.P_WWWLogin"
        MENU_ENDPOINT = "https://ssb.uc.cl/ERPUC/twbkwbis.P_GenMenu?name=bmenu.P_MainMnu"

        print('Iniciando driver...', flush=True***REMOVED***
        driver = init_driver(***REMOVED***
        print('Driver iniciado!', flush=True***REMOVED***
        # Obtenemos la cookie en base al usuario
        usuario = item.user
        id_usuario = User.objects.get(username=usuario***REMOVED***.id
        planner = None
        try:
            print('Obteniendo planner de ' + usuario, flush=True***REMOVED***
            planner = Planner.objects.get(user=id_usuario***REMOVED***
            if planner.estado_toma in {2, 3, 4***REMOVED*** or not item.estado:
                driver.quit(***REMOVED***
                return (False, 'Planner no disponible o cookie invalida'***REMOVED***
        except:
            print('Chequeando que cookie no esta expirada', flush=True***REMOVED***
            if not item.estado:
                print(item.estado, flush=True***REMOVED***
                print('Cookie expirada', flush=True***REMOVED***
                driver.quit(***REMOVED***
                return (False, 'Cookie invalida'***REMOVED***

        cookie = item.cookie_value
        data[0***REMOVED***["value"***REMOVED*** = cookie

        print('Iniciando sesion...', flush=True***REMOVED***
        driver.get(LOGIN_ENDPOINT***REMOVED***

        print('Cargando cookies...', flush=True***REMOVED***
        for cookie in data:
            driver.add_cookie(cookie***REMOVED***
        try:
            print('Chequeando que cookie no esta expirada', flush=True***REMOVED***
            driver.get(MENU_ENDPOINT***REMOVED***
            driver.find_element(by=By.XPATH, value="/html/body/div[3***REMOVED***/table[1***REMOVED***/tbody/tr[1***REMOVED***/td[2***REMOVED***/a"***REMOVED***
            print(f'¡Credenciales aceptadas de {usuario***REMOVED***!'***REMOVED***
            driver.quit(***REMOVED***
            return (True, 'Cuenta aceptada'***REMOVED***
        except:
            driver.quit(***REMOVED***
            if planner:
                planner.estado_toma = 4
                planner.save(***REMOVED***

            cookie = Cookies.objects.get(user=usuario***REMOVED***
            item.estado = False
            item.save(***REMOVED***
            print(f'Las credenciales fueron rechazadas. El usuario {usuario***REMOVED*** tendrá que hacer login nuevamente', flush=True***REMOVED***
            mail = User.objects.get(username=usuario***REMOVED***.email
            send_mail(
            'AutoRamosWeb Necesita ReLogin',
            'Hola, hemos detectado un fallo en tu cuenta y necesitamos que te hagas relogin en el siguiente link: https://autoramos.xyz/relogin/.',
            os.environ.get('EMAIL_HOST_USER'***REMOVED***,
            [mail***REMOVED***,
            fail_silently=False,
            ***REMOVED***
            return (False, 'Cookie invalida'***REMOVED***

    threads_ammount = 3
    threads = [***REMOVED***
    cookies_master = [***REMOVED***
    cant_cookies = Cookies.objects.count(***REMOVED***

    for i in range(threads_ammount***REMOVED***:
        cookies_master.append(list(***REMOVED***
    for id in range(cant_cookies***REMOVED***:
        cookies_master[id % threads_ammount***REMOVED***.append(Cookies.objects.all(***REMOVED***[id***REMOVED***
    print(f"Debug cookies_master: {cookies_master***REMOVED***"***REMOVED***
    for cookie_list in cookies_master:
        for cookie in cookie_list:
            t = Thread(target=validate_cookie, args=(cookie,***REMOVED***
            threads.append(t***REMOVED***
            t.start(***REMOVED***
    for t in threads:
        t.join(***REMOVED***


def scrapeo_img_base64(html, usuario***REMOVED***:
    soup = BeautifulSoup(html, 'lxml'***REMOVED***
    paso1 = soup.find_all('img'***REMOVED***
    img_sucio = paso1[2***REMOVED***['src'***REMOVED***

    img = img_sucio.split(','***REMOVED***[-1***REMOVED***

    with open(f"{usuario***REMOVED***.dib","wb"***REMOVED*** as f:
        f.write(base64.b64decode(img***REMOVED***


def scrapeo_pagina_final(html***REMOVED***:
    try:
        print('Scrapeando pagina final...'***REMOVED***
        print(f"Debug, html: {html[40***REMOVED***"***REMOVED***
        nrcs = [***REMOVED***
        bs = BeautifulSoup(html, 'lxml'***REMOVED***
        table = bs.find('table', attrs={'summary':'Esta tabla es usada para presentar Errores de Inscripción.'***REMOVED***
        table_body = table.find('tbody'***REMOVED***
        rows = table_body.find_all('tr'***REMOVED***
        for row in rows:
            if row.find('th'***REMOVED***:
                continue
            cols = row.find_all('td'***REMOVED***
            cols = [ele.text.strip(***REMOVED*** for ele in cols***REMOVED***
            nrc = cols[1***REMOVED***
            nrcs.append(nrc***REMOVED***
        print("SCRAPEO RETORNANDO NRCS: ", nrcs***REMOVED***
        return nrcs
    except Exception as err:
        print("SCRAPEO LLEGO A EXCEPT NO RETORNA NIUNA WEA", err***REMOVED***
        return [***REMOVED***
