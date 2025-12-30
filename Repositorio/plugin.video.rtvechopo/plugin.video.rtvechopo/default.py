# -*- coding: utf-8 -*-
import xbmc
import xbmcgui
import webbrowser
import urllib.request
import six
import os
import sys
import time
import random
import shutil
import platform
import socket
import hashlib
import json
import base64
import re
import unicodedata
import requests
import xbmcaddon
import xbmcplugin
import xbmcvfs
import plugintools
import uuid
import subprocess
 
from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError
 
 
 
# Compatibilidad con Python 2 y 3
try:
    import urllib.request
    import urllib.parse
    import urllib.error
    from urllib.parse import urlparse, urlencode
    from urllib.request import urlopen, Request
    from urllib.error import HTTPError
except ImportError:  # Compatibilidad con Python 2
    import urllib2
    from urlparse import urlparse
    from urllib import urlencode
    from urllib2 import urlopen, Request, HTTPError
 
try:
    import resolveurl
except ImportError:
    resolveurl = None
 
try:
    from resolveurl.plugins.lib import jsunpack
except ImportError:
    try:
        from resolveurl.lib import jsunpack
    except ImportError:
        jsunpack = None
 
 
 
 
if six.PY3:
    unicode = str
addon = xbmcaddon.Addon()
addonname = '[B][LOWERCASE][CAPITALIZE][COLOR white]choposeries[/CAPITALIZE][/LOWERCASE][/B][/COLOR]'
icon = addon.getAddonInfo('icon')
myaddon = xbmcaddon.Addon("plugin.video.rtvechopo")
Set_Color = myaddon.getSetting('SetColor')
Set_View = myaddon.getSetting('SetView')
import xbmc
import xbmcgui
from lib import vistas
skin_name=xbmc.getSkinDir()
ALL_VIEW_CODES='{0}'.format(vistas.vista())
try:
    view_tipe='movies'
    view_codes = re.findall("(?s)"+skin_name+".*?"+view_tipe+"': (.*?),", ALL_VIEW_CODES, flags=re.DOTALL)[0]
except:
    view_codes =50

def run():   
 
    params = plugintools.get_params()   
    if params.get("action") is None:
        main_list(params)
    else:
       action = params.get("action")
       url = params.get("url")
       exec(action+"(params)")
    plugintools.close_item_list()
 
 
 

xbmc.executebuiltin('UpdateAddonRepos')
 
 
try:    
    reporesolver = xbmcaddon.Addon('repository.resolveurl')
    reporesolver=reporesolver.getAddonInfo('version')
 
except:
    reporesolver="[B][LOWERCASE][CAPITALIZE][COLOR orange]no tienes instalado el repositorio de resolveurl  [/COLOR][/CAPITALIZE][/LOWERCASE][/B]"
    dp = xbmcgui.DialogProgress()
    dp.create('[CAPITALIZE][COLOR yellow]ATENCION:[COLOR lime]no tienes el repositorio de resolveurl instalado[/COLOR][/CAPITALIZE]')
    xbmc.sleep(2000)
    dp.update(800,'[CAPITALIZE][COLOR white]dale a [COLOR lime]si [COLOR white]para instalarlo[/COLOR][/CAPITALIZE]')  
    xbmc.sleep(2000)
    dp.close() 
    xbmc.executebuiltin('InstallAddon(repository.resolveurl)')
 
 
try:    
    f4m = xbmcaddon.Addon('script.module.resolveurl')
    f4m=f4m.getAddonInfo('version')
 
except:
    f4m="[B][LOWERCASE][CAPITALIZE][COLOR orange]no tienes instalado resolveurl  [/COLOR][/CAPITALIZE][/LOWERCASE][/B]"
    dp = xbmcgui.DialogProgress()
    dp.create('[CAPITALIZE][COLOR yellow]ATENCION:[COLOR lime]no tienes resolveurl instalado[/COLOR][/CAPITALIZE]')
    xbmc.sleep(2000)
    dp.update(800,'[CAPITALIZE][COLOR white]dale a [COLOR lime]si [COLOR white]para instalarlo[/COLOR][/CAPITALIZE]')  
    xbmc.sleep(2000)
    dp.close() 
 
    xbmc.executebuiltin('InstallAddon(script.module.resolveurl)')        
 
def main_list(params):
    thumbnail = 'https://tmbroadcast.es/wp-content/uploads/2021/07/rtve_a_la_carta_transforacion_rtve_play.jpg'

    
    plugintools.add_item(action="", title="[B][LOWERCASE][CAPITALIZE][COLOR yellow]======[COLOR orange]menu tve_a la carta[COLOR yellow]=======[/COLOR][/CAPITALIZE][/LOWERCASE][/B]",thumbnail=thumbnail, fanart='https://i.imgur.com/gxNuSrI.png',folder=False )  
    
    

    
#----------------------------------------------------------------------------------------------------------------------------      
    plugintools.add_item(action="tve_buscador", title="[B][LOWERCASE][CAPITALIZE][COLOR white]tve buscador[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",thumbnail="https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png", fanart="https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png",  url= "https://www.rtve.es/play/a-z/",folder= True ) 

    plugintools.add_item(action="tve_directos", title="[B][LOWERCASE][CAPITALIZE][COLOR white]tve directos[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",thumbnail="https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png", fanart="https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png",  url= "https://www.rtve.es/play/a-z/",folder= True )
    
    plugintools.add_item(action="tve_todos", title="[B][LOWERCASE][CAPITALIZE][COLOR white]tve completa[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",thumbnail="https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png", fanart="https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png",  url= "https://www.rtve.es/play/a-z/",folder= True )
    
    plugintools.add_item(action="tve_informativos", title="[B][LOWERCASE][CAPITALIZE][COLOR white]tve adios-2022[/COLOR][/CAPITALIZE][/LOWERCASE][/B]",thumbnail="https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png", fanart="https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png",page='0', url= "https://www.rtve.es/play/adios-2022-lo-mas-destacado-del-ano/?locale=ES",folder= True )
    
 
    plugintools.add_item(action="tve_informativos", title="[B][LOWERCASE][CAPITALIZE][/CAPITALIZE][COLOR white]tve informativos[/LOWERCASE][/B][/COLOR]",thumbnail="https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png", fanart="https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png", url= 'https://www.rtve.es/play/informativos/',folder= True )  


    plugintools.add_item(action="tve_informativos",page='1', title="[B][LOWERCASE][CAPITALIZE][COLOR white]tve cine[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",thumbnail="https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png", fanart="https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png", url= 'https://www.rtve.es/play/cine/',folder= True ) 

    plugintools.add_item(action="tve_informativos",page='1', title="[B][LOWERCASE][CAPITALIZE][COLOR white]tve series[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",thumbnail="https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png", fanart="https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png", url= 'https://www.rtve.es/play/series/',folder= True )



    
    plugintools.add_item(action="tve_todos",page='1', title="[B][LOWERCASE][CAPITALIZE][COLOR white]tve crimenes [COLOR lime]!!novedad[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",thumbnail="https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png", fanart="https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png", url= 'https://www.rtve.es/play/colecciones/true-crime/1770/',folder= True ) 

  
    plugintools.add_item(action="",page='1', title="[B][LOWERCASE][CAPITALIZE][COLOR white]tve retro[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",thumbnail="https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png", fanart="https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png", url= 'plugin://plugin.video.choposeries/?action=secciones_tve&extra&page&plot&thumbnail=https%3a%2f%2fimages-na.ssl-images-amazon.com%2fimages%2fI%2f516rC6urOwL.png&title=%5bB%5d%5bLOWERCASE%5d%5bCAPITALIZE%5d%5bCOLOR%20white%5dsuper%20retros%20spain%20%5b%2fCAPITALIZE%5d%5b%2fLOWERCASE%5d%5b%2fB%5d%5b%2fCOLOR%5d&url=https%3a%2f%2fwww.rtve.es%2fplay%2farchivo%2f',folder= True )     


    plugintools.add_item(action="tve_informativos",page='1', title="[B][LOWERCASE][CAPITALIZE][/CAPITALIZE][COLOR white]tve entretenimiento[/LOWERCASE][/B][/COLOR]",thumbnail="https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png", fanart="https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png", url= 'https://www.rtve.es/play/entretenimiento/',folder= True )     
    
    
    plugintools.add_item(action="tve_informativos", title="[B][LOWERCASE][CAPITALIZE][COLOR white]tve eurovision[/COLOR][/CAPITALIZE][/LOWERCASE][/B]",thumbnail="https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png", fanart="https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png",page='0', url= "https://www.rtve.es/play/eurovision/",folder= True )      
    plugintools.add_item(action="tve_informativos", title="[B][LOWERCASE][CAPITALIZE][COLOR white]tve playz[/COLOR][/CAPITALIZE][/LOWERCASE][/B]",thumbnail="https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png", fanart="https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png",page='0', url= "https://www.rtve.es/play/playz/",folder= True )    


    plugintools.add_item( action="reyes", title="[B][LOWERCASE][CAPITALIZE][COLOR white]carta a los reyes magos[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail="https://www.diocesismalaga.es/cms/media/articulos/articulos-235638.jpg", fanart="https://www.losreyesmagos.tv/wp-content/uploads/2018/11/Reyes.jpg",url='',folder=False,  isPlayable = True ) 

    plugintools.add_item( action="el_rincon_de_papanoel", title="[B][LOWERCASE][CAPITALIZE][COLOR white]rincon de_papa noel[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail="https://www.viveusa.mx/sites/default/files/field/image/ciudad_santa_claus.jpg", fanart="https://okdiario.com/img/2019/12/21/papa-noel_-la-verdadera-historia-de-santa-claus.jpg",url='',folder=True )

 

    plugintools.add_item( action="SERIES_ESPECIALES", title="[B][LOWERCASE][CAPITALIZE][B][LOWERCASE][CAPITALIZE][COLOR white]series especiales [COLOR orange]chopo  [/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail='https://i.ytimg.com/vi/ZXtwHMasoBo/hqdefault.jpg', fanart='https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/portada80s-1519981906.jpg',url='',folder=True ) 

    plugintools.add_item( action="seriesclan", title="[B][LOWERCASE][CAPITALIZE][B][LOWERCASE][CAPITALIZE][COLOR white]series clan  [/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail='https://images.produ.com/noticias/1121/big-ClanTV.jpg', fanart='https://img2.rtve.es/i/?i=1661947875887.jpg',url='https://www.rtve.es/drmn/catalog-category/?page=1&colT=4&colM=2&size=18&sizeT=18&sizeM=11&exT=N&exM=N&tipopag=0&tpT=0&tpM=0&progtitle=S&ctx=INF&csel=1&n1=Todos&c1=NN&i1=0&t1=PRO&f1=N&o1=FP&e1&q1=inPubTarget%253DINFANTIL%2526lang%253Des%2526order%253Dprogram_orden%252Casc&de=N&ll=N&stt=S&fakeImg=S&col=4&r=/infantil/series/',folder=True ) 



def seriesclan(params):  
   
    thumbnail = params.get("thumbnail")    
    url=params.get("url")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers( url, headers=request_headers)
    if six.PY3==True :
        url = body.strip().decode('utf-8')
    else :
        url = body.strip()
    try:
        siguiente=plugintools.find_single_match(url,'<a class="verMas" href=".*?page=(.*?)&')
    except:
        pass
    matches = plugintools.find_multiple_matches(url,'(?s)data-rtve-id=".*?".*?a class="linkElemento mainLink" href=".*?".*?ttribute-src=".*?".*?lass="tit M">.*?<.*?apiCall summary"><p>.*?</p>')
    for generos in matches:  
        patron=plugintools.find_single_match(generos,'(?s)data-rtve-id="(.*?)".*?a class="linkElemento mainLink" href=".*?".*?ttribute-src="(.*?)".*?lass="tit M">(.*?)<.*?apiCall summary"><p>(.*?)</p>')    
        url=patron[0]
        foto=patron[1]
        titulo=patron[2]
        texto=patron[3]
        url='https://www.rtve.es/drmn/iso/catalog-category/?&col=5&colT=3&colM=2&size=40&sizeT=9&sizeM=6&exT=N&exM=N&tipopag=0&tpT=0&tpM=0&ctx=INF&n1=Todos&c1=TEM&i1='+url+'&t1=VID&f1=N&o1=FP&e1&q1=type%3D39816&csel=1&de=S&ll=N&stt=S&fakeImg=S&r=/infantil/series/team-nuggets/'
        plugintools.add_item(action="capitulos_clan", url=url,title="[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",plot="[B][LOWERCASE][CAPITALIZE][COLOR yellow]"+texto+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",thumbnail=foto,fanart=foto,folder=True ) 
    if siguiente:
        siguiente='https://www.rtve.es/drmn/catalog-category/?page='+siguiente+'&colT=4&colM=2&size=18&sizeT=18&sizeM=11&exT=N&exM=N&tipopag=0&tpT=0&tpM=0&progtitle=S&ctx=INF&csel=1&n1=Todos&c1=NN&i1=0&t1=PRO&f1=N&o1=FP&e1&q1=inPubTarget%253DINFANTIL%2526lang%253Des%2526order%253Dprogram_orden%252Casc&de=N&ll=N&stt=S&fakeImg=S&col=4&r=/infantil/series/'+siguiente
        plugintools.add_item(action="seriesclan", url=siguiente,title="[B][LOWERCASE][CAPITALIZE][COLOR lime]ir a la pagina siguiente[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",thumbnail=thumbnail,fanart=thumbnail,folder=True ) 
    xbmcplugin.setContent( int(sys.argv[1]) ,""+str(view_tipe)+"" )
    xbmc.executebuiltin("Container.SetViewMode("+str(view_codes)+")")

def capitulos_clan(params):  
   
    thumbnail = params.get("thumbnail")    
    url=params.get("url")
    headers= {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0","Referer": "https://enn.ennovelas-tv.com/"}
    source=requests.get(url, headers=headers, verify=False)
    url = source.text
    
    matches = plugintools.find_multiple_matches(url,'(?s)a class="linkElemento mainLink" href=".*?".*?ttribute-src=".*?".*?lass="tit M">.*?<.*?apiCall summary"><p>.*?</p>')
    for generos in matches:  
        patron=plugintools.find_single_match(generos,'(?s)a class="linkElemento mainLink" href="(.*?)".*?ttribute-src="(.*?)".*?lass="tit M">(.*?)<.*?apiCall summary"><p>(.*?)</p>')    
        url=patron[0]
        foto=patron[1]
        titulo=patron[2]
        texto=patron[3]
        plugintools.add_item(action="javi_descarga", url=url,title="[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",plot="[B][LOWERCASE][CAPITALIZE][COLOR yellow]"+texto+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",thumbnail=foto,fanart=foto,folder=False,  isPlayable = True ) 
    xbmcplugin.setContent( int(sys.argv[1]) ,""+str(view_tipe)+"" )
    xbmc.executebuiltin("Container.SetViewMode("+str(view_codes)+")")
    


def PAPANOEL_WEBCAM(params):
    
    
    thumbnail = params.get("thumbnail")
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR white]--------especial [COLOR red]navidad --------[/COLOR][/CAPITALIZE][/LOWERCASE][/B]", thumbnail =thumbnail, fanart =thumbnail,  folder = False )    
    import xbmc, time, random
    cancion = ['https://s3.amazonaws.com/emailsanta/vid/0024.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0009.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0036.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0023.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0011.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0029.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0043.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0020.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0020.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0003.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0053.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0021.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0050.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0066.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0017.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0060.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0016.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0065.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0003.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0036.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0021.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0018.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0010.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0034.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0030.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0059.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0020.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0052.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0059.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0054.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0002.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0007.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0026.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0053.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0055.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0067.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0013.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0006.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0044.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0064.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0022.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0048.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0005.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0065.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0051.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0025.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0037.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0038.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0035.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0042.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0023.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0013.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0023.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0062.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0012.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0011.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0031.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0036.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0040.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0029.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0061.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0014.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0004.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0051.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0027.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0030.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0057.mp4',
'https://s3.amazonaws.com/emailsanta/vid/0027.mp4']
    sel1 = random.choice(cancion)
    plugintools.play_resolved_url(sel1)



    
def reyes(params):  
 thumbnail=params.get("thumbnail")
 from email.mime.multipart import MIMEMultipart
 from email.mime.text import MIMEText
 import re, requests, xbmcgui, xbmcaddon, random, xbmc, resolveurl, webbrowser, smtplib
 reyes = True
 reyElegido = ""
 chicoChica = True
 generoElegido = ""
 edad = 0
 deberes = True
 haceDeberes = ""
 comportamiento = True
 comoMePorto = ""
 ayudoCasa = True
 tareasCasa = ""
 regalos = ""
 carta = ""
 haySitio = True
 lugar = ""
 hayComida = True
 comida = ""
 receptor = ""
 receptorConfirmacion = ""
 receptorIgual = True 
 server = smtplib.SMTP('smtp.gmail.com:587')
 
#elige reyes
 dialog = xbmcgui.Dialog()
 ret = dialog.select('[B][COLOR yellow]Selecciona tu Rey Mago favorito:[/COLOR][/B]', ['[B][LOWERCASE][CAPITALIZE][COLOR lime]Melchor[/COLOR][/CAPITALIZE][/LOWERCASE][/B]', '[B][LOWERCASE][CAPITALIZE][COLOR red]Gaspar[/COLOR][/CAPITALIZE][/LOWERCASE][/B]', '[B][LOWERCASE][CAPITALIZE][COLOR yellow]Baltasar[/COLOR][/CAPITALIZE][/LOWERCASE][/B]'])
 lists = ['t1', 't2', 't3', '']
 reyElegido = lists[ret]
 opcionMenu = reyElegido
 if opcionMenu == "t1":
     reyElegido ='Melchor'
 if opcionMenu == "t2":
     reyElegido = 'Gaspar'
 if opcionMenu == "t3":
     reyElegido = 'Baltasar'
 if opcionMenu == "":     
     xbmcgui.Dialog().ok('[B][COLOR lime]DEBES ELEGIR UN REY.........[COLOR red][/COLOR][/B]', '[B][LOWERCASE][CAPITALIZE][COLOR aqua]... para enviar, tu carta a los reyes magos[/COLOR][/CAPITALIZE][/LOWERCASE][/B]', '[B][LOWERCASE][CAPITALIZE]  [COLOR aqua] debes contestarnos todas las preguntas... venga empezamos de nuevo [COLOR yellow][/COLOR][/CAPITALIZE][/LOWERCASE][/B]')
 
 
 
#nombre
 dialog = xbmcgui.Dialog()
 nombre = dialog.input('[B][LOWERCASE][CAPITALIZE][COLOR orange]Introduce tu nombre:[/COLOR][/CAPITALIZE][/LOWERCASE][/B]', type=xbmcgui.INPUT_ALPHANUM)
 if nombre == "" or nombre == " ":
     xbmcgui.Dialog().ok('[B][COLOR lime]NO PUEDES METER UN NOMBRE VACIO......[COLOR red][/COLOR][/B]', '[B][LOWERCASE][CAPITALIZE][COLOR aqua]... para enviar, tu carta a los reyes magos[/COLOR][/CAPITALIZE][/LOWERCASE][/B]', '[B][LOWERCASE][CAPITALIZE]  [COLOR aqua] debes contestarnos todas las preguntas... venga empezamos de nuevo [COLOR yellow][/COLOR][/CAPITALIZE][/LOWERCASE][/B]')
 
#sexo
 dialog = xbmcgui.Dialog()
 ret = dialog.select('[B][COLOR yellow]eres un chico o una chica?[/COLOR][/B]', ['[B][LOWERCASE][CAPITALIZE][COLOR lime]chico[/COLOR][/CAPITALIZE][/LOWERCASE][/B]', '[B][LOWERCASE][CAPITALIZE][COLOR red]chica[/COLOR][/CAPITALIZE][/LOWERCASE][/B]'])
 lists = ['t1', 't2', '']
 generoElegido+= lists[ret]
 if generoElegido == "t1":
     generoElegido = "chico"
 if generoElegido == "t2":
     generoElegido = "chica"
 if generoElegido == "" or generoElegido == " ":
     xbmcgui.Dialog().ok('[B][COLOR lime]TIENES QUE DECIRME SI ERES CHICO O CHICA...[COLOR red][/COLOR][/B]', '[B][LOWERCASE][CAPITALIZE][COLOR aqua]... para enviar, tu carta a los reyes magos[/COLOR][/CAPITALIZE][/LOWERCASE][/B]', '[B][LOWERCASE][CAPITALIZE]  [COLOR aqua] debes contestarnos todas las preguntas... venga empezamos de nuevo [COLOR yellow][/COLOR][/CAPITALIZE][/LOWERCASE][/B]') 
 
 
 
#edad
 dialog = xbmcgui.Dialog()
 edad = dialog.input('[B][LOWERCASE][CAPITALIZE][COLOR orange]Introduce tu edad:[/COLOR][/CAPITALIZE][/LOWERCASE][/B]', type=xbmcgui.INPUT_NUMERIC)
 if edad == "" or edad == " ":
     xbmcgui.Dialog().ok('[B][COLOR lime]TIENES QUE DECIRME TU EDAD..[COLOR red][/COLOR][/B]', '[B][LOWERCASE][CAPITALIZE][COLOR aqua]... para enviar, tu carta a los reyes magos[/COLOR][/CAPITALIZE][/LOWERCASE][/B]', '[B][LOWERCASE][CAPITALIZE]  [COLOR aqua] debes contestarnos todas las preguntas... venga empezamos de nuevo [COLOR yellow][/COLOR][/CAPITALIZE][/LOWERCASE][/B]')
 else:
     edad = edad
 
#ciudad
 dialog = xbmcgui.Dialog()
 ciudad = dialog.input('[B][LOWERCASE][CAPITALIZE][COLOR orange]Introduce tu ciudad o pueblo:[/COLOR][/CAPITALIZE][/LOWERCASE][/B]', type=xbmcgui.INPUT_ALPHANUM)
 if ciudad == "" or ciudad == " ":     
     xbmcgui.Dialog().ok('[B][COLOR lime]TIENES QUE DECIRME TU CIUDAD..[COLOR red][/COLOR][/B]', '[B][LOWERCASE][CAPITALIZE][COLOR aqua]... para enviar, tu carta a los reyes magos[/COLOR][/CAPITALIZE][/LOWERCASE][/B]', '[B][LOWERCASE][CAPITALIZE]  [COLOR aqua] debes contestarnos todas las preguntas... venga empezamos de nuevo [COLOR yellow][/COLOR][/CAPITALIZE][/LOWERCASE][/B]')
 else:
     ciudad = ciudad
 
#deveres
 dialog = xbmcgui.Dialog()
 ret = dialog.select('[B][COLOR yellow]como te portas en el cole. ¿Haces siempre tus deberes?[/COLOR][/B]', ['[B][LOWERCASE][CAPITALIZE][COLOR lime]si[/COLOR][/CAPITALIZE][/LOWERCASE][/B]', '[B][LOWERCASE][CAPITALIZE][COLOR red]no[/COLOR][/CAPITALIZE][/LOWERCASE][/B]'])
 lists = ['t1', 't2', '']
 haceDeberes+= lists[ret]
 if haceDeberes == "t1":
     haceDeberes = "Este año he sido muy buen@, he hecho los deberes, "
 if haceDeberes == "t2":
     haceDeberes = "Este año he sido un poco travies@ porque algunas veces no hago los deberes, "
 if haceDeberes == "" or haceDeberes == " ":     
     xbmcgui.Dialog().ok('[B][COLOR lime]TIENES QUE DECIRME SI HICISTES LOS DEVERES O NO...[COLOR red][/COLOR][/B]', '[B][LOWERCASE][CAPITALIZE][COLOR aqua]... para enviar, tu carta a los reyes magos[/COLOR][/CAPITALIZE][/LOWERCASE][/B]', '[B][LOWERCASE][CAPITALIZE]  [COLOR aqua] debes contestarnos todas las preguntas... venga empezamos de nuevo [COLOR yellow][/COLOR][/CAPITALIZE][/LOWERCASE][/B]')
 
 
 
#comportamiento
 dialog = xbmcgui.Dialog()
 ret = dialog.select('[B][COLOR yellow]¿Te peleas con tus compañeros y con tus hermanos?[/COLOR][/B]', ['[B][LOWERCASE][CAPITALIZE][COLOR red]si[/COLOR][/CAPITALIZE][/LOWERCASE][/B]', '[B][LOWERCASE][CAPITALIZE][COLOR lime]Juego con ellos y comparto mis juguetes[/COLOR][/CAPITALIZE][/LOWERCASE][/B]'])
 lists = ['t1', 't2', '']
 comoMePorto = lists[ret]
 if comoMePorto == "t1":
     comoMePorto = "de vez en cuando discuto con mis amigos, "
 if comoMePorto == "t2":
     comoMePorto = " y no me he peleado con mis hermanos ni mis amiguitos, "
 if comoMePorto == "" or comoMePorto == " ":     
     xbmcgui.Dialog().ok('[B][COLOR lime]TIENES QUE DECIRME COMO TE PORTAS...[COLOR red][/COLOR][/B]', '[B][LOWERCASE][CAPITALIZE][COLOR aqua]... para enviar, tu carta a los reyes magos[/COLOR][/CAPITALIZE][/LOWERCASE][/B]', '[B][LOWERCASE][CAPITALIZE]  [COLOR red] debes contestarnos todas las preguntas... venga empezamos de nuevo [COLOR yellow][/COLOR][/CAPITALIZE][/LOWERCASE][/B]')
 
#tareas
 dialog = xbmcgui.Dialog()
 ret = dialog.select('[B][COLOR yellow]¿ haces lo que te mandan tus padres sin rechistar?[/COLOR][/B]', ['[B][LOWERCASE][CAPITALIZE][COLOR lime]Soy obediente.[/COLOR][/CAPITALIZE][/LOWERCASE][/B]', '[B][LOWERCASE][CAPITALIZE][COLOR red]No soy obediente lloro y chillo.[/COLOR][/CAPITALIZE][/LOWERCASE][/B]'])
 lists = ['t1', 't2', '', ' ']
 tareasCasa+= lists[ret]
 if tareasCasa == "t1":
     tareasCasa = " cuando como, dejo el plato vacío. He sido obediente,\n he hecho todo lo que mis papás me han dicho,\n ¡y a la primera y sin rechistar!. Trato muy bien a los animalitos \ny ordeno mis juguetes cuando acabo de jugar."
 if tareasCasa == "t2":
     tareasCasa = "algunas veces protesto cuando me mandan hacer algo,\n pero te prometo que este año me voy a portar mejor."
 if tareasCasa == "" or tareasCasa == " ":
     xbmcgui.Dialog().ok('[B][COLOR lime]TIENES QUE DECIRME SI HACES CASO A LOS PAPAS...[COLOR red][/COLOR][/B]', '[B][LOWERCASE][CAPITALIZE][COLOR aqua]... para enviar, tu carta a los reyes magos[/COLOR][/CAPITALIZE][/LOWERCASE][/B]', '[B][LOWERCASE][CAPITALIZE]  [COLOR aqua] debes contestarnos todas las preguntas... venga empezamos de nuevo [COLOR yellow][/COLOR][/CAPITALIZE][/LOWERCASE][/B]')
 
 
 
#regalos
 dialog = xbmcgui.Dialog()
 dialog.textviewer('[B][COLOR yellow]¡¡¡ ves tu !!!, ya se me había olvidado preguntarte lo principal:[/COLOR][/B]', '[B][LOWERCASE][CAPITALIZE][COLOR aqua] los regalos que quieres para este año,  tengo que leer tranquilamente todo lo que me has contado, y luego ya veremos si te traigo los regalos que quieres, Aquí te dejo a mi pajecillo que va a tomar nota de tus deseos, anda, escribe los regalos que te gustaría recibir este año[/COLOR][/CAPITALIZE][/LOWERCASE][/B] ')
 regalos+= dialog.input('[B][LOWERCASE][CAPITALIZE][COLOR lime]Introduce los regalitos que quieres separados por , :[/COLOR][/CAPITALIZE][/LOWERCASE][/B]', type=xbmcgui.INPUT_ALPHANUM)
 if regalos == "" or regalos== " ":     
     xbmcgui.Dialog().ok('[B][COLOR lime]No puedes dejar tu lista vacia!...[COLOR red][/COLOR][/B]', '[B][LOWERCASE][CAPITALIZE][COLOR aqua]... para enviar, tu carta a los reyes magos[/COLOR][/CAPITALIZE][/LOWERCASE][/B]', '[B][LOWERCASE][CAPITALIZE]  [COLOR aqua] debes contestarnos todas las preguntas... venga empezamos de nuevo [COLOR yellow][/COLOR][/CAPITALIZE][/LOWERCASE][/B]')
 
 
 
#donderegalos
 dialog = xbmcgui.Dialog()
 ret = dialog.select('[B][COLOR yellow]Y otra cosa, ¿dónde quieres que te deje los regalos?:[/COLOR][/B]', ['[B][LOWERCASE][CAPITALIZE][COLOR red]En el árbol de navidad.[/COLOR][/CAPITALIZE][/LOWERCASE][/B]', '[B][LOWERCASE][CAPITALIZE][COLOR lime]En los calcetines de la chimenea.[/COLOR][/CAPITALIZE][/LOWERCASE][/B]', '[B][LOWERCASE][CAPITALIZE][COLOR aqua]En mis zapatos.[/COLOR][/CAPITALIZE][/LOWERCASE][/B]'])
 lists = ['t1', 't2', 't3', '']
 lugar = lists[ret]
 if lugar == "t1":
     lugar ='En el árbol de navidad.'
 if lugar == "t2":
     lugar = 'En los calcetines de la chimenea.'
 if lugar == "t3":
     lugar = 'En mis zapatos.'
 if lugar == "":
     xbmcgui.Dialog().ok('[B][COLOR lime]DEBES ELEGIR UN LUGAR DONDE DEJARTE LOS REGALOS...[COLOR red][/COLOR][/B]', '[B][LOWERCASE][CAPITALIZE][COLOR aqua]... para enviar, tu carta a los reyes magos[/COLOR][/CAPITALIZE][/LOWERCASE][/B]', '[B][LOWERCASE][CAPITALIZE]  [COLOR aqua] debes contestarnos todas las preguntas... venga empezamos de nuevo [COLOR yellow][/COLOR][/CAPITALIZE][/LOWERCASE][/B]')
 
 
 
#algoComida
 dialog = xbmcgui.Dialog()
 dialog.textviewer('[B][COLOR yellow]Pues creo que ya si está todo. Bueno..., no, falta una cosita...[/COLOR][/B]', '[B][LOWERCASE][CAPITALIZE][COLOR aqua]En las noches de invierno hace muuuuuucho frío y mis camellos tienen que trabajar mucho y se les quedan las patitas heladas, así que no estaría mal que les dejaras algo de comer y algo calentito para beber.[/COLOR][/CAPITALIZE][/LOWERCASE][/B] ')
 dialog = xbmcgui.Dialog()
 ret = dialog.select('[B][COLOR yellow]¿que le vas a dejar de comer a los camellos?[/COLOR][/B]', ['[B][LOWERCASE][CAPITALIZE][COLOR red]Vino.[/COLOR][/CAPITALIZE][/LOWERCASE][/B]', '[B][LOWERCASE][CAPITALIZE][COLOR lime]Leche calentita.[/COLOR][/CAPITALIZE][/LOWERCASE][/B]', '[B][LOWERCASE][CAPITALIZE][COLOR aqua]Bombones y mantecados.[/COLOR][/CAPITALIZE][/LOWERCASE][/B]'])
 lists = ['t1', 't2', 't3', '']
 comida = lists[ret]
 
 if comida == "t1":
     comida = "vino "
 if comida == "t2":
     comida = "leche "
 if comida == "t3":
     comida = "bombones "
 if comida == "" or comida == " ":     
     xbmcgui.Dialog().ok('[B][COLOR lime]TIENES QUE DEJARLES ALGO DE COMER A LOS CAMELLOS...[COLOR red][/COLOR][/B]', '[B][LOWERCASE][CAPITALIZE][COLOR aqua]... para enviar, tu carta a los reyes magos[/COLOR][/CAPITALIZE][/LOWERCASE][/B]', '[B][LOWERCASE][CAPITALIZE]  [COLOR aqua] debes contestarnos todas las preguntas... venga empezamos de nuevo [COLOR yellow][/COLOR][/CAPITALIZE][/LOWERCASE][/B]')
 
#cartakodi
 dialog = xbmcgui.Dialog()
 carta = dialog.textviewer ('[B][COLOR yellow]aqui esta la carta[/COLOR][/B]', '[B][COLOR aqua]Querido rey [COLOR red]'+ reyElegido+'\n[COLOR aqua] Me llamo [COLOR red]'+nombre+'[COLOR aqua], tengo [COLOR red]'+str(edad) + '[COLOR aqua] añitos y vivo en [COLOR red]'+ciudad + '\n[COLOR aqua]'+haceDeberes+'\n'+comoMePorto+ '\n'+tareasCasa + '\ny por todo esto, me gustaría que me trajeras los regalos que te pido:\n[COLOR red]'+ regalos + '[COLOR aqua]\nSi puedes me dejas los regalos [COLOR red]'+lugar + ' [COLOR aqua]\nYo os dejaré un poco de [COLOR red]'+comida+ '[COLOR aqua]a ti y a tus \ncamellos para que se os quite el frío y comáis un poquito. \nBueno, nada más. ¡Ah si!, te prometo que \neste año también voy a ser muy bueno.\nMuchas gracias. Un beso muy fuerte, rey ' + reyElegido+'. \nY saluda a los otros Reyes de mi parte, ¡no lo olvides!' + '[/COLOR][/B]')
 
 
 ret = dialog.select('[B][COLOR yellow]¿enviar la carta a los reyes magos?[/COLOR][/B]', ['[B][LOWERCASE][CAPITALIZE][COLOR lime]si.[/COLOR][/CAPITALIZE][/LOWERCASE][/B]', '[B][LOWERCASE][CAPITALIZE][COLOR red]no.[/COLOR][/CAPITALIZE][/LOWERCASE][/B]'])
 lists = ['si', 'no']
 enviar = lists[ret]
 if enviar == "si":
     xbmcgui.Dialog().ok('[B][COLOR lime]LA CARTA HA SIDO ENVIADA. [COLOR red][/COLOR][/B]', '[B][LOWERCASE][CAPITALIZE][COLOR aqua]... que bien, tu carta  ya a llegado a los reyes magos\nya saben como te has portado [COLOR aqua]y los regalitos que quieres.[/COLOR][/CAPITALIZE][/LOWERCASE][/B]') 
     cartaEmail = "\t Querido rey " + reyElegido+":\n \tMe llamo "+nombre+", tengo "+str(edad) + " añitos y vivo en "+ciudad+".\n \t "+haceDeberes+comoMePorto + \
    tareasCasa+"\n\t... y por todo esto, me gustaría que me trajeras los regalos que te pido:\n" + \
        regalos+"\n \tSi puedes me dejas los regalos "+lugar+" Yo os dejaré un poco de "+comida + \
    "a ti y a tus camellos para que se os quite el frío y comáis un poquito.\n \tBueno, nada más. ¡Ah si!, te prometo que este año también voy a ser muy bueno.\n \tMuchas gracias. Un beso muy fuerte, rey Melchor. Y saluda a los otros Reyes de mi parte, ¡no lo olvides!"

     xbmcgui.Dialog().ok('[B][COLOR lime]atencion no te vayas...[COLOR red][/COLOR][/B]', '[B][LOWERCASE][CAPITALIZE][COLOR aqua]... oohh estamos reciviendo una videollamada\n[COLOR aqua]a tvchopo son los reyes quieren hablar contigo[/COLOR][/CAPITALIZE][/LOWERCASE][/B]')
     ret = dialog.select('[B][COLOR yellow]¿quieres hacer la videollamada con los reyes?[/COLOR][/B]', ['[B][LOWERCASE][CAPITALIZE][COLOR lime]si.[/COLOR][/CAPITALIZE][/LOWERCASE][/B]', '[B][LOWERCASE][CAPITALIZE][COLOR red]no.[/COLOR][/CAPITALIZE][/LOWERCASE][/B]'])
     lists = ['video', 'no']
     llamada = lists[ret]
     if 'video' in llamada:
         xbmcgui.Dialog().ok('[B][COLOR lime]de parte del equipo de tvchopo...[COLOR red][/COLOR][/B]', '[B][LOWERCASE][CAPITALIZE][COLOR aqua]os deceamos a todos los niños del mundo\nfeliz navidad, que seais felices pequeños... y que ojala se os cumplan todos vuestros sueños\ny que os traigan todos los regalitos[/COLOR][/CAPITALIZE][/LOWERCASE][/B]')
         url= 'https://github.com/elchocolate/repotvchopo/raw/master/Repositorio/tvchopo-feliz-navidad.mp4'
         plugintools.play_resolved_url(url)
     if 'no' in llamada:         
         xbmcgui.Dialog().ok('[B][COLOR lime]llamada rechazada...[COLOR red][/COLOR][/B]', '[B][LOWERCASE][CAPITALIZE][COLOR aqua]... oohh los reyes querian decirte algo\nsi camias de opinion puedes volver a intentarlo[/COLOR][/CAPITALIZE][/LOWERCASE][/B]')
 
 
 if enviar == "no":
     xbmcgui.Dialog().ok('[B][COLOR lime]tu carta no ha sido enviada...[COLOR red][/COLOR][/B]', '[B][LOWERCASE][CAPITALIZE][COLOR aqua]... no te preocupes\nsi camias de opinion puedes volver a intentarlo[/COLOR][/CAPITALIZE][/LOWERCASE][/B]')
 
 
     xbmcgui.Dialog().ok('[B][COLOR lime]de parte del equipo de tvchopo...[COLOR red][/COLOR][/B]', '[B][LOWERCASE][CAPITALIZE][COLOR aqua]os deceamos a todos los niños del mundo\nfeliz navidad, que seais felices pequeños... y que ojala se os cumplan todos vuestros sueños\ny que os traigan todos los regalitos[/COLOR][/CAPITALIZE][/LOWERCASE][/B]')        
    






def el_rincon_de_papanoel(params):
 
    
    thumbnail = params.get("thumbnail")
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR white]--------el rincon [COLOR red]de santa claus--------[/COLOR][/CAPITALIZE][/LOWERCASE][/B]", thumbnail =thumbnail, fanart =thumbnail,  folder = False )    

    plugintools.add_item( action="", title="[B][LOWERCASE][CAPITALIZE][COLOR pink]Santa,la señora Claus,los duendes y los renos[/COLOR][/CAPITALIZE][/LOWERCASE][/B]", thumbnail=thumbnail, fanart=thumbnail,url='',folder=False) 

    plugintools.add_item( action="", title="[B][LOWERCASE][CAPITALIZE][COLOR pink]se están preparando para la gran noche.[/COLOR][/CAPITALIZE][/LOWERCASE][/B]", thumbnail=thumbnail, fanart=thumbnail,url='',folder=False)    
    
    plugintools.add_item( action="", title="[B][LOWERCASE][CAPITALIZE][COLOR pink]mueve por las secciones para ver algunas[/COLOR][/CAPITALIZE][/LOWERCASE][/B]", thumbnail=thumbnail, fanart=thumbnail,url='',folder=False)   

    plugintools.add_item( action="", title="[B][LOWERCASE][CAPITALIZE][COLOR pink]cosas divertidas que pasan en Navidad[/COLOR][/CAPITALIZE][/LOWERCASE][/B]", thumbnail=thumbnail, fanart=thumbnail,url='',folder=False) 

    plugintools.add_item( action="", title="[B][LOWERCASE][CAPITALIZE][COLOR yellow]----------------------------------------------------------[/COLOR][/CAPITALIZE][/LOWERCASE][/B]", thumbnail=thumbnail, fanart=thumbnail,url='',folder=False)  
    
    plugintools.add_item( action="carta_a_papa", title="[B][LOWERCASE][CAPITALIZE][COLOR lime]¡[COLOR orange]enviar la carta a papa noel[COLOR lime]! [/COLOR][/CAPITALIZE][/LOWERCASE][/B]", thumbnail="https://www.santatelevision.com/wp-content/uploads/santa-claus-personalized-video-message.jpg", fanart="https://st3.depositphotos.com/11124126/33977/v/600/depositphotos_339777760-stock-video-santa-claus-uses-a-smartphone.jpg",url='',folder=False,  isPlayable = True) 
    
    plugintools.add_item( action="PAPANOEL_WEBCAM", title="[B][LOWERCASE][CAPITALIZE][COLOR lime]¡[COLOR orange]Mira a Papá Noel en directo a través de su Webcam del Polo Norte[COLOR lime]! [/COLOR][/CAPITALIZE][/LOWERCASE][/B]", thumbnail="https://www.emailsanta.com/img3/webcam-spanish.webp", fanart="https://i.imgur.com/xMIa9N7.jpg",url='',folder=False,  isPlayable = True ) 
 
    plugintools.add_item( action="el_vuelo_de_santa", title="[B][LOWERCASE][CAPITALIZE][COLOR lime]¡[COLOR orange]Video del gran vuelo de Santa[COLOR lime]! [/COLOR][/CAPITALIZE][/LOWERCASE][/B]", thumbnail="https://www.wallpaperk.com/wallpapers/papa-noel-en-trineo-5820.jpg", fanart="https://cdn.ssl-socket.com/wp-content/uploads/2017/12/TRINEO-SANTA.jpg",url='https://www.youtube.com/watch?v=GJH2tVTCqw4',folder=False,  isPlayable = True ) 


    #plugintools.add_item( action="galletas", title="[B][LOWERCASE][CAPITALIZE][COLOR lime]¡[COLOR orange]La Cámara de galletas navideña[COLOR lime]! [/COLOR][/CAPITALIZE][/LOWERCASE][/B]", thumbnail="https://lh3.googleusercontent.com/proxy/lSkupDawg8Oaaj0OUB_hiuJcGAKo2aNVPyFuwfjEknZcCtQmgViPnfVobFH6S-E4cDCOK00b4rpxP9rbLZRsyHMSmkDGzChOrPoHd4cfSV73wNSgDGMD3llKJSyhXAoEGA", fanart="https://cdn5.upsocl.com/wp-content/uploads/2018/11/cook.jpg",url='',folder=True )



    plugintools.add_item( action="donde_esta", title="[B][LOWERCASE][CAPITALIZE][COLOR lime]¿[COLOR orange]Dónde está Santa en este momento[COLOR lime]? [/COLOR][/CAPITALIZE][/LOWERCASE][/B]", thumbnail="https://www.viveusa.mx/sites/default/files/field/image/ciudad_santa_claus.jpg", fanart="https://okdiario.com/img/2019/12/21/papa-noel_-la-verdadera-historia-de-santa-claus.jpg",url='',folder=True) 


def donde_esta(params):

    thumbnail = params.get("thumbnail")
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR white]--------camara [COLOR red]de galletas --------[/COLOR][/CAPITALIZE][/LOWERCASE][/B]", thumbnail =thumbnail, fanart =thumbnail,  folder = False ) 
    import re, requests, xbmcgui, xbmcaddon, random, xbmc, resolveurl, webbrowser, smtplib    

    url='https://www.emailsanta.com/es/sigueasanta.asp'
    headers= {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1"
    }
    import requests,re
    url=requests.get(url, headers=headers, verify=False).text
    foto=plugintools.find_single_match(url,'(?s)Audio5.playclip..;">En este momento, Santa Claus est..*?color: #790000;">(.*?)<') 
    dialog = xbmcgui.Dialog()
    dialog.textviewer('[B][COLOR lime]¿[COLOR orange]DONDE ESTA SANTA EN ESTE MOMENTO[COLOR lime]?[/COLOR][/B]', '[B][LOWERCASE][CAPITALIZE][COLOR yellow]En este momento, Santa Claus está [COLOR white]'+foto+'\n[COLOR yellow]¡vamos a verlo en vivo en la cámara de Santa!)[/COLOR][/CAPITALIZE][/LOWERCASE][/B] ')
    plugintools.add_item( action="PAPANOEL_WEBCAM", title="[B][LOWERCASE][CAPITALIZE][COLOR orange]ver la camara de santa aqui[/COLOR][/CAPITALIZE][/LOWERCASE][/B]", thumbnail=thumbnail, fanart=thumbnail,url='',folder=False,  isPlayable = True)


   

def el_vuelo_de_santa(params):

    import re, requests, xbmcgui, xbmcaddon, random, xbmc, resolveurl, webbrowser, smtplib    
    dialog = xbmcgui.Dialog()
    dialog.textviewer('[B][COLOR lime]¡[COLOR yellow]DIAS ANTES DE NAVIDAD,[COLOR lime]![/COLOR][/B]', '[B][LOWERCASE][CAPITALIZE][COLOR white]allá en el frío polar\nSanta miraba la lista\nde niños que se portan bien y mal.\nLos duendes vinieron corriendo\nmientras felices reían.\nEn sus manos un regalo: \n¡una cámara traían!\n[COLOR yellow]"Esto es para tu trineo",\n[COLOR white]dijo un duende muy jocundo.\n[COLOR yellow]"Para la víspera de Navidad,\n¡que te vea todo el mundo!\nCon solo entrar a tvchopo,\ny con ganas de reír,\nen esta seccion podrán \na Santa seguir.\n[COLOR yellow]Y, ¿qué aparecerá ante sus ojos asombrados?\n¡Los renos, los regalos \ny Santa en el trineo, acomodados!"\n[COLOR pink]Repartiré juguetes con mucho cariño,\n¡y veré los mensajes\nde niñas y niños!"\nEn tvchopo encontrarán a Santa\n[COLOR yellow]¡Es genial! ¡Lo mejor!\n¡A todos nos encanta![/COLOR][/CAPITALIZE][/LOWERCASE][/B] ')
    url='https://www.youtube.com/watch?v=GJH2tVTCqw4'
    import resolveurl 
    video = resolveurl.resolve( url )
    plugintools.play_resolved_url( video )


    
    
   
def carta_a_papa(params):  
 from email.mime.multipart import MIMEMultipart
 from email.mime.text import MIMEText
 import re, requests, xbmcgui, xbmcaddon, random, xbmc, resolveurl, webbrowser, smtplib
 receptor = ""
 receptorConfirmacion = ""
 receptorIgual = True 
 server = smtplib.SMTP('smtp.gmail.com:587')



#comienza carta
 dialog = xbmcgui.Dialog()
 dialog.textviewer('[B][COLOR orange]¿Quieres escribirle una carta a Papá Noel?,[/COLOR][/B]', '[B][LOWERCASE][CAPITALIZE][COLOR yellow]Así es, niños, es verdad.\nLo único que tienes que hacer es completar esta carta...\n¡Papá Noel te está esperando! Y te enviará su respuesta\ndesde el Polo Norte...más rápido que un rayo.\nEscribe tu carta a Papá Noel cualquier día del año.\nPapá Noel te responderá con una carta mágica inmediatamente,\nsin que tengas que esperar. Simplemente desde tvchopo te respondera.\n[COLOR aqua]Comienza a escribir tu carta[/COLOR][/CAPITALIZE][/LOWERCASE][/B] ')  
 
 
 #nombre
 dialog = xbmcgui.Dialog()
 nombre = dialog.input('[B][LOWERCASE][CAPITALIZE][COLOR lime]Querido Papá Noel: Mi nombre es[/COLOR][/CAPITALIZE][/LOWERCASE][/B]', type=xbmcgui.INPUT_ALPHANUM)
 if nombre == "" or nombre == " ":
     xbmcgui.Dialog().ok('[B][COLOR lime]NO PUEDES METER UN NOMBRE VACIO......[COLOR red][/COLOR][/B]', '[B][LOWERCASE][CAPITALIZE][COLOR aqua]... para enviar, tu carta a papa noel[/COLOR][/CAPITALIZE][/LOWERCASE][/B]', '[B][LOWERCASE][CAPITALIZE]  [COLOR aqua] debes contestarnos todas las preguntas... venga empezamos de nuevo [COLOR yellow][/COLOR][/CAPITALIZE][/LOWERCASE][/B]') 
     plugintools.add_item( action="carta_a_papa", title="[B][LOWERCASE][CAPITALIZE][COLOR lime]¡[COLOR orange]venga empezamos de nuevo[/COLOR][/CAPITALIZE][/LOWERCASE][/B]", thumbnail="https://www.santatelevision.com/wp-content/uploads/santa-claus-personalized-video-message.jpg", fanart="https://st3.depositphotos.com/11124126/33977/v/600/depositphotos_339777760-stock-video-santa-claus-uses-a-smartphone.jpg",url='',folder=False)
 else:
 #elige sexo
   dialog = xbmcgui.Dialog()
   ret = dialog.select('[B][COLOR yellow]eres niño o niña?:[/COLOR][/B]', ['[B][LOWERCASE][CAPITALIZE][COLOR lime]niño...aunque jugar con muñecas también es divertido.[/COLOR][/CAPITALIZE][/LOWERCASE][/B]', '[B][LOWERCASE][CAPITALIZE][COLOR red]niña...para no recibir ropa de niño por error[/COLOR][/CAPITALIZE][/LOWERCASE][/B]'])
   lists = ['uno de nuestros niños favoritos', 'una de nuestras niñas favoritas']
   reyElegido = lists[ret]
   sexo = reyElegido
 #años
 dialog = xbmcgui.Dialog()
 anios = dialog.input('[B][LOWERCASE][CAPITALIZE][COLOR lime]Cuantos Años Tienes[/COLOR][/CAPITALIZE][/LOWERCASE][/B]', type=xbmcgui.INPUT_NUMERIC)
 if anios == "" or anios == " ":
     xbmcgui.Dialog().ok('[B][COLOR lime]debes decirnos tu edad......[COLOR red][/COLOR][/B]', '[B][LOWERCASE][CAPITALIZE][COLOR aqua]... para enviar, tu carta a papa noel[/COLOR][/CAPITALIZE][/LOWERCASE][/B]', '[B][LOWERCASE][CAPITALIZE]  [COLOR aqua] debes contestarnos todas las preguntas... venga empezamos de nuevo [COLOR yellow][/COLOR][/CAPITALIZE][/LOWERCASE][/B]') 
     plugintools.add_item( action="carta_a_papa", title="[B][LOWERCASE][CAPITALIZE][COLOR lime]¡[COLOR orange]venga empezamos de nuevo[/COLOR][/CAPITALIZE][/LOWERCASE][/B]", thumbnail="https://www.santatelevision.com/wp-content/uploads/santa-claus-personalized-video-message.jpg", fanart="https://st3.depositphotos.com/11124126/33977/v/600/depositphotos_339777760-stock-video-santa-claus-uses-a-smartphone.jpg",url='',folder=False)
 else:
     xbmcgui.Dialog().ok('[B][COLOR lime]debes decirnos donde vives......[COLOR red][/COLOR][/B]', '[B][LOWERCASE][CAPITALIZE][COLOR aqua]Escribe el nombre ciudad [/COLOR][/CAPITALIZE][/LOWERCASE][/B]')  
     dialog = xbmcgui.Dialog()

     ciudad = dialog.input('[B][LOWERCASE][CAPITALIZE][COLOR lime]Vivo en la ciudad de: [/COLOR][/CAPITALIZE][/LOWERCASE][/B]', type=xbmcgui.INPUT_ALPHANUM)    
 if ciudad == "" or ciudad == " ":
     xbmcgui.Dialog().ok('[B][COLOR lime]debes decirnos donde vives......[COLOR red][/COLOR][/B]', '[B][LOWERCASE][CAPITALIZE][COLOR aqua]... para que papa noel te lleve los regalos[/COLOR][/CAPITALIZE][/LOWERCASE][/B]', '[B][LOWERCASE][CAPITALIZE]  [COLOR aqua] debes contestarnos todas las preguntas... venga empezamos de nuevo [COLOR yellow][/COLOR][/CAPITALIZE][/LOWERCASE][/B]') 
     plugintools.add_item( action="carta_a_papa", title="[B][LOWERCASE][CAPITALIZE][COLOR lime]¡[COLOR orange]venga empezamos de nuevo[/COLOR][/CAPITALIZE][/LOWERCASE][/B]", thumbnail="https://www.santatelevision.com/wp-content/uploads/santa-claus-personalized-video-message.jpg", fanart="https://st3.depositphotos.com/11124126/33977/v/600/depositphotos_339777760-stock-video-santa-claus-uses-a-smartphone.jpg",url='',folder=False)
 else:  
  #comportamiento
   dialog = xbmcgui.Dialog()
   dialog.textviewer('[B][COLOR orange]¡Cuéntale a Papá Noel,[/COLOR][/B]', '[B][LOWERCASE][CAPITALIZE][COLOR yellow]si te has portado bien o mal! \n(¡Mira que está haciendo una lista y revisándola varias veces!)[/COLOR][/CAPITALIZE][/LOWERCASE][/B] ') 
   dialog = xbmcgui.Dialog()
   ret = dialog.select('[B][COLOR yellow]Este año me he portado tan bien que?:[/COLOR][/B]', ['[B][LOWERCASE][CAPITALIZE][COLOR lime]¡Tendría que ir yo en la punta del árbol en lugar del angelito!.[/COLOR][/CAPITALIZE][/LOWERCASE][/B]', '[B][LOWERCASE][CAPITALIZE][COLOR orange]Bueno, digamos que mi aureola está un poquito torcida[/COLOR][/CAPITALIZE][/LOWERCASE][/B]', '[B][LOWERCASE][CAPITALIZE][COLOR lime]No hay dudas de que debería estar en la lista de los que se portaron bien[/COLOR][/CAPITALIZE][/LOWERCASE][/B]', '[B][LOWERCASE][CAPITALIZE][COLOR red]He tenido que mandar a reparar mi aureola un par de veces[/COLOR][/CAPITALIZE][/LOWERCASE][/B]'])
   lists = ['muy bien', 'mal', 'bien', 'muy mal']
   reyElegido = lists[ret]
   comportamiento = reyElegido
   
   #regalos
   dialog = xbmcgui.Dialog()
   dialog.textviewer('[B][COLOR orange]QUERIDO PAPA NOEL,[/COLOR][/B]', '[B][LOWERCASE][CAPITALIZE][COLOR yellow]¡Papá Noel hará todo lo posible\n pero ya sabes que no puede prometerte que te regalará todo lo que pides!\nQUERIDO PAPA NOEL,\n algunas cosas que me gustaría recibir para Navidad este año son....[/COLOR][/CAPITALIZE][/LOWERCASE][/B] ')     
   regalo1 = dialog.input('[B][LOWERCASE][CAPITALIZE][COLOR lime]escribe tu primer regalo: [/COLOR][/CAPITALIZE][/LOWERCASE][/B]', type=xbmcgui.INPUT_ALPHANUM) 
   if regalo1 == "" or regalo1 == " ":
    xbmcgui.Dialog().ok('[B][COLOR lime]debes decirnos que regalos quieres......[COLOR red][/COLOR][/B]', '[B][LOWERCASE][CAPITALIZE][COLOR aqua]... para que papa noel te lleve los regalos[/COLOR][/CAPITALIZE][/LOWERCASE][/B]', '[B][LOWERCASE][CAPITALIZE]  [COLOR aqua] debes contestarnos todas las preguntas... venga empezamos de nuevo [COLOR yellow][/COLOR][/CAPITALIZE][/LOWERCASE][/B]') 
    plugintools.add_item( action="carta_a_papa", title="[B][LOWERCASE][CAPITALIZE][COLOR lime]¡[COLOR orange]venga empezamos de nuevo[/COLOR][/CAPITALIZE][/LOWERCASE][/B]", thumbnail="https://www.santatelevision.com/wp-content/uploads/santa-claus-personalized-video-message.jpg", fanart="https://st3.depositphotos.com/11124126/33977/v/600/depositphotos_339777760-stock-video-santa-claus-uses-a-smartphone.jpg",url='',folder=False)
   else:
    xbmcgui.Dialog().ok('[B][COLOR lime]ayudanos[/COLOR][/B]', '[B][LOWERCASE][CAPITALIZE][COLOR aqua]... "Cuantas más ideas les des a los duendes, mejor[/COLOR][/CAPITALIZE][/LOWERCASE][/B]') 
    regalo2 = dialog.input('[B][LOWERCASE][CAPITALIZE][COLOR lime]escribe tu segundo regalo: [/COLOR][/CAPITALIZE][/LOWERCASE][/B]', type=xbmcgui.INPUT_ALPHANUM)
    if regalo2 == "" or regalo2 == " ":
     xbmcgui.Dialog().ok('[B][COLOR lime]debes decirnos que regalos quieres......[COLOR red][/COLOR][/B]', '[B][LOWERCASE][CAPITALIZE][COLOR aqua]... para que papa noel te lleve los regalos\ndebes contestarnos todas las preguntas... venga empezamos de nuevo[/COLOR][/CAPITALIZE][/LOWERCASE][/B]') 
     plugintools.add_item( action="carta_a_papa", title="[B][LOWERCASE][CAPITALIZE][COLOR lime]¡[COLOR orange]venga empezamos de nuevo[/COLOR][/CAPITALIZE][/LOWERCASE][/B]", thumbnail="https://www.santatelevision.com/wp-content/uploads/santa-claus-personalized-video-message.jpg", fanart="https://st3.depositphotos.com/11124126/33977/v/600/depositphotos_339777760-stock-video-santa-claus-uses-a-smartphone.jpg",url='',folder=False)
    else:
     regalo3 = dialog.input('[B][LOWERCASE][CAPITALIZE][COLOR lime]¡Pon tu tercer deseo aquí!: [/COLOR][/CAPITALIZE][/LOWERCASE][/B]', type=xbmcgui.INPUT_ALPHANUM)
     if regalo3 == "" or regalo3 == " ":
      xbmcgui.Dialog().ok('[B][COLOR lime]debes decirnos que regalos quieres......[COLOR red][/COLOR][/B]', '[B][LOWERCASE][CAPITALIZE][COLOR aqua]... para que papa noel te lleve los regalos[/COLOR][/CAPITALIZE][/LOWERCASE][/B]', '[B][LOWERCASE][CAPITALIZE]  [COLOR aqua] debes contestarnos todas las preguntas... venga empezamos de nuevo [COLOR yellow][/COLOR][/CAPITALIZE][/LOWERCASE][/B]') 
      plugintools.add_item( action="carta_a_papa", title="[B][LOWERCASE][CAPITALIZE][COLOR lime]¡[COLOR orange]venga empezamos de nuevo[/COLOR][/CAPITALIZE][/LOWERCASE][/B]", thumbnail="https://www.santatelevision.com/wp-content/uploads/santa-claus-personalized-video-message.jpg", fanart="https://st3.depositphotos.com/11124126/33977/v/600/depositphotos_339777760-stock-video-santa-claus-uses-a-smartphone.jpg",url='',folder=False)
     else:
      anios2=(str(int(anios)-1)) 
      dialog = xbmcgui.Dialog()
      dialog.textviewer('[B][COLOR orange]¡Hola '+nombre+'![/COLOR][/B]', '[B][LOWERCASE][CAPITALIZE][COLOR lime]¡[COLOR white]Los duendes y yo estamos felices de que haya llegado tu carta.[COLOR lime]¡\n[COLOR white]Después de todo, eres '+sexo+'\nen [COLOR gold]'+ciudad+'!\n[COLOR white]Cuando llegó tu carta,algunos de los duendes\nsalieron corriendo hasta la pantalla\ngigante de la computadora\ny empezaron a saltar y bailar.\nMe encanta la Internet porque ya nunca me\nsiento solo, solito aquí en el Polo Norte.\n¡Recibir un e-mail tuyo, [COLOR gold]'+nombre+',\n[COLOR white]me hace feliz por el resto del día!\n¡Uy, mira lo que encontré en mi casilla de correos!\n¡Con campanas hay que festejar, [COLOR gold]'+nombre+'!\n[COLOR white]¡Estás creciendo tan rápido!  ¡Ya tienes [COLOR gold]'+anios+' [COLOR white]años!\nMe parece que era el año pasado cuando tenías [COLOR gold]'+anios2+' [COLOR white]años.\n¡Quisiera saber cuántos años vas a\ntener el próximo año!\n¿A que no adivinas en qué otra cosa estoy pensando?\n¡EN LA NAVIDAD! ¿Tú también estás ansioso\npor que llegue la Navidad?\n¿O estás súper feliz, como Rodolfo?\nTambién he oído que te has portado realmente bien.\n(Claro que igual tengo que comprobarlo en los\ninformes de los duendes, ¿no te parece?)\nVeamos qué deseos de Navidad has puesto en tu carta:\n1. [COLOR gold]'+regalo1+'\n[COLOR white]2. [COLOR gold]'+regalo2+'\n[COLOR white]3. [COLOR gold]'+regalo3+'.\n[COLOR white]¡Que todos tus deseos de Navidad se hagan realidad [COLOR gold]'+nombre+'\n[COLOR white]!¡Mamá Noel estará encantada cuando se entere\nde que tu lista incluye [COLOR gold]'+regalo2+'!\n[COLOR white]Le encanta.\n[COLOR white]¡HO!! ¡Ho!! ¡ho!! ¡Tengo que salir corriendo!\nLos duendes están corriendo\ncomo locos y agitando las manos en el aire.\nEstán pensando cómo pueden meter un rascacielos\nen la bolsa de juguetes.Mejor les digo\nque lo que el niño quería\nera una guitarra color cielo y no un "rascacielos".\nCuídate [COLOR gold]'+nombre+' [COLOR white]y no te olvides de volver a visitarme\n aquí en tvchopò cuando llegue la Navidad.\n¡Y recuerda...  queda muy poquito hasta Navidad!\n¡Sé bueno, diviértete, y convierte cada día en algo extraordinario!\nPapá Noel\nP.D.   te vamos a mostrar tu carta [/COLOR][/CAPITALIZE][/LOWERCASE][/B] ')  
      
      dialog.textviewer('[B][COLOR orange]Querido Papá Noel,[/COLOR][/B]', '[B][LOWERCASE][CAPITALIZE][COLOR lime]¡[COLOR white]Me llamo [COLOR gold]'+nombre+'.\n[COLOR white]¡Ya tengo [COLOR gold]'+anios+' [COLOR white]años de edad!\nVivo en la hermosa ciudad que se llama [COLOR gold]'+ciudad+'\n[COLOR white]¡pero seguro que ya lo sabías!\nEste año me he portado tan bien que ¡Tengo el halo un poco torcido!\nPapá Noel, estas son las cosas que me gustaría recibir para Navidad:\n[COLOR gold]-'+regalo1+'\n[COLOR gold]-'+regalo2+'\n[COLOR gold]-'+regalo3+'\n[COLOR white]Papá Noel, casi me olvido de decirte... que te quiero mucho\nTodo mi cariño, [COLOR gold]'+nombre+'[/COLOR][/CAPITALIZE][/LOWERCASE][/B] ') 
      
      cartaEmail = "\t Querido Papá Noel, :\n \tMe llamo "+nombre+", ¡Ya tengo "+str(anios) + " Vivo en la hermosa ciudad que se llama  "+ciudad+".\n \t ¡pero seguro que ya lo sabías!"+ \
    "\n\t... Este año me he portado tan bien que ¡Tengo el halo un poco torcido!\n" + \
        "\n \t papá Noel, estas son las cosas que me gustaría recibir para Navidad: "+regalo1+" ,"+regalo2+", "+regalo3+".\n \tPapá Noel, casi me olvido de decirte... que te quiero mucho " \
    "a ti a tus renos y tus duendecillos os dejare unas galletitas para que comáis un poquito.\n \tBueno, nada más. ¡Ah si!, te prometo que este año también voy a ser muy bueno.\n \tMuchas gracias. Un beso muy fuerte, papa noel. Y saluda a los renos y los duendecillos de mi parte, ¡no lo olvides! Todo mi cariño,\n"+nombre
      dp = xbmcgui.DialogProgress()
      dp.create('[CAPITALIZE][COLOR white]ENVIANDO LA CARTA A PAPA NOEL >>>[/COLOR][/CAPITALIZE]')
      dp.update(50,'[CAPITALIZE][COLOR yellow]ATENCION:[COLOR lime] LA CARTA HA SIDO ENVIADA CON EXITO[/COLOR][/CAPITALIZE]')
      xbmc.sleep(2000)
      dp.update(75,'[CAPITALIZE][COLOR yellow]PORTATE MUY BIEN PARA QUE TE TRAIGAN TODO[/COLOR][/CAPITALIZE]')  
      xbmc.sleep(2000)
      dp.update(100,'[CAPITALIZE][COLOR yellow]TE DECEAMOS FELIZ NAVIDAD[/COLOR][/CAPITALIZE]')  
      xbmc.sleep(2000)
      dp.close()       
      xbmcgui.Dialog().ok('[B][COLOR lime]atencion no te vayas...[COLOR red][/COLOR][/B]', '[B][LOWERCASE][CAPITALIZE][COLOR aqua]... oohh estamos reciviendo una videollamada\na tvchopo es papa noel quiere hablar contigo[/COLOR][/CAPITALIZE][/LOWERCASE][/B]')
      ret = dialog.select('[B][COLOR yellow]¿quieres hacer la videollamada con papa noel?[/COLOR][/B]', ['[B][LOWERCASE][CAPITALIZE][COLOR lime]si.[/COLOR][/CAPITALIZE][/LOWERCASE][/B]', '[B][LOWERCASE][CAPITALIZE][COLOR red]no.[/COLOR][/CAPITALIZE][/LOWERCASE][/B]'])
      lists = ['video', 'no']
      llamada = lists[ret]
      if 'video' in llamada:
         xbmcgui.Dialog().ok('[B][COLOR lime]de parte del equipo de tvchopo...[COLOR red][/COLOR][/B]', '[B][LOWERCASE][CAPITALIZE][COLOR aqua]os deceamos a todos los niños del mundo\nfeliz navidad, que seais felices pequeños... y que ojala se os cumplan todos vuestros sueños\ny que os traigan todos los regalitos[/COLOR][/CAPITALIZE][/LOWERCASE][/B]')
         url= 'https://www.youtube.com/watch?v=24h5FHwZzAw'
         import resolveurl 
         video = resolveurl.resolve( url )
         plugintools.play_resolved_url( video )    
      if 'no' in llamada:         
         xbmcgui.Dialog().ok('[B][COLOR lime]llamada rechazada...[COLOR red][/COLOR][/B]', '[B][LOWERCASE][CAPITALIZE][COLOR aqua]... oohh papanoel queria decirte algo\nsi camias de opinion puedes volver a intentarlo[/COLOR][/CAPITALIZE][/LOWERCASE][/B]')            
def videos_de_santa(params):

    thumbnail = params.get("thumbnail")
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR white]--------los videos  [COLOR red]de santa--------[/COLOR][/CAPITALIZE][/LOWERCASE][/B]", thumbnail =thumbnail, fanart =thumbnail,  folder = False ) 
    url = 'https://www.emailsanta.com/es/sigueasanta.asp'
    headers= {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1"
    }
    import requests,re
    source=requests.get(url, headers=headers, verify=False).text
    matches = plugintools.find_multiple_matches(source,"(?s)class='vLink a6'><a href='.*?'.*?Sigue a Santa.*?<")
    for generos in matches:  
        url='https://www.youtube.com/watch?v='+plugintools.find_single_match(generos,"href='https://www.youtube.com/embed/(.*?)'") 
        titulo=plugintools.find_single_match(generos,'(Sigue a Santa.*?) #') 
  

        plugintools.add_item( action="play_resolver", title="[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo+"[/COLOR][/CAPITALIZE][/LOWERCASE][/B]",url=url,folder=False,  isPlayable = True)   
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR white]--------los videos  [COLOR red]de santa--------[/COLOR][/CAPITALIZE][/LOWERCASE][/B]", thumbnail =thumbnail, fanart =thumbnail,  folder = False )  





def DOCUSDELA2(params):

    plugintools.add_item(action = "" , title ="[B][LOWERCASE][CAPITALIZE][COLOR yellow]------------[COLOR white] tve[COLOR yellow]------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png", fanart = "https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png",  folder = False )    
    thumbnail = params.get("thumbnail") 
    fanart = params.get("thumbnail")
    url = params.get("url")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers(url, headers=request_headers)
    if six.PY3==True:
        data = body.strip().decode('utf-8')
    else:
        data = body.strip()
    matches = plugintools.find_multiple_matches(data,'(?s)container  fila tobeload".*?href=".*?".*? >\s*.*?\s*</a>')
    for generos in matches:
        url = plugintools.find_single_match(generos,'href="(.*?)"').replace("&amp;", "&")
        titulo = plugintools.find_single_match(generos,'(?s)container  fila tobeload".*?href=".*?".*? >\s*(.*?)\s*</a>')
 
 
        plugintools.add_item(action = "series_tve_series" , title ="[B][LOWERCASE][CAPITALIZE][COLOR yellow][COLOR aqua]"+titulo+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" ,url =url , thumbnail ="https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png", fanart = "https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png", folder = True )

    plugintools.add_item(action="", title="[B][LOWERCASE][CAPITALIZE][COLOR yellow]======[COLOR orange]documentales de la 2[COLOR yellow]=======[/COLOR][/CAPITALIZE][/LOWERCASE][/B]",thumbnail=thumbnail, fanart=thumbnail,folder=False )


def tve_directos(params):  
  
    thumbnail = params.get("thumbnail")    
    plugintools.add_item(action="", title="[B][LOWERCASE][CAPITALIZE][COLOR yellow]======[COLOR orange]tve_a la carta[COLOR yellow]=======[/COLOR][/CAPITALIZE][/LOWERCASE][/B]",thumbnail=thumbnail, fanart=thumbnail,folder=False )
    url='https://www.rtve.es/play/videos/directo/'
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers( url, headers=request_headers)
    if six.PY3==True :
        url = body.strip().decode('utf-8')
    else :
        url = body.strip()
    matches = plugintools.find_multiple_matches(url,'(?s)data-setup="{&quot;id&quot;:&quot;.*?&quot;,&quot;idAsset&quot;:&quot;.*?&quot.*?<div class="mod video_mod live.*?-.*? dir_brocast.*?class="content" aria-label="Emisi.n en directo.*?aintitle">.*?<.*?class="maintitle">.*?<.*?rtve-icons">.*?<.*?.*?src=".*?.jpg".*?href=".*?"')
    for generos in matches:  
        patron=plugintools.find_single_match(generos,'(?s)data-setup="{&quot;id&quot;:&quot;.*?&quot;,&quot;idAsset&quot;:&quot;(.*?)&quot.*?<div class="mod video_mod live.*?-(.*?) dir_brocast.*?class="content" aria-label="Emisi.n en directo.*?aintitle">(.*?)<.*?class="maintitle">.*?<.*?rtve-icons">(.*?)<.*?.*?src="(.*?).jpg".*?href=".*?"')    
        region=patron[1]
        emision=patron[2]    
        canal=patron[3]
        if 'can' in str(region):
            canal=canal+' canarias'
        if 'cat' in str(region):
            canal=canal+' cataluña'            
        foto=patron[4]+'.jpg'
        url='https://ztnr.rtve.es/ztnr/'+patron[0].replace("H_", "")+'.m3u8|user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0'
        plugintools.add_item(action="play_links", url=url,title="[B][LOWERCASE][CAPITALIZE][COLOR white]"+canal+" [COLOR yellow]"+emision+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",thumbnail=foto,fanart=foto,folder=False,  isPlayable = True)





def tve_deportes(params):  
  
    thumbnail = params.get("thumbnail")    
    plugintools.add_item(action="", title="[B][LOWERCASE][CAPITALIZE][COLOR yellow]======[COLOR orange]tve_a la carta[COLOR yellow]=======[/COLOR][/CAPITALIZE][/LOWERCASE][/B]",thumbnail=thumbnail, fanart=thumbnail,folder=False )
    url='https://www.rtve.es/play/deportes/'
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers( url, headers=request_headers)
    if six.PY3==True :
        url = body.strip().decode('utf-8')
    else :
        url = body.strip()
    matches = plugintools.find_multiple_matches(url,'(?s)completo ">.*?<a href="https://www.rtve.es/play/videos/.*?".*?pretitle">.*?<.*?class="i_prvw".*?i_post poster" src=".*?".*?')
    for generos in matches:  
        patron=plugintools.find_single_match(generos,'(?s)completo ">.*?<a href="(https://www.rtve.es/play/videos/.*?)".*?pretitle">(.*?)<.*?class="i_prvw".*?i_post poster" src="(.*?)".*?')    
        url2=patron[0]
        titulo1=patron[1].replace("#8211;", "")
        foto=patron[2]
        plugintools.add_item(action="series_tve_temporada", url=url2,title="[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo1+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",thumbnail=foto,fanart=foto,folder=True )
    matches = plugintools.find_multiple_matches(url,'(?s)completo ">.*?<a href="https://www.rtve.es/play/videos/.*?".*?pretitle">.*?<.*?class="i_prvw".*?i_post poster" src=".*?".*?')
    for generos in matches:  
        patron=plugintools.find_single_match(generos,'(?s)completo ">.*?<a href="(https://www.rtve.es/play/videos/.*?)".*?pretitle">(.*?)<.*?class="i_prvw".*?i_post poster" src="(.*?)".*?')    
        url2=patron[0]
        titulo1=patron[1].replace("#8211;", "")
        foto=patron[2]
        plugintools.add_item(action="series_tve_temporada", url=url2,title="[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo1+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",thumbnail=foto,fanart=foto,folder=True )  
def tve_buscador(params):  
 
    thumbnail = params.get("thumbnail") 
    plugintools.set_view(plugintools.MOVIES,503)    
    plugintools.add_item(action="", title="[B][LOWERCASE][CAPITALIZE][COLOR yellow]======[COLOR orange]tve_a la carta[COLOR yellow]=======[/COLOR][/CAPITALIZE][/LOWERCASE][/B]",thumbnail=thumbnail, fanart=thumbnail,folder=False )
    dialog = xbmcgui.Dialog()
    d = dialog.input('[B][LOWERCASE][CAPITALIZE][COLOR orange]buscar en tve: ejemplo: [COLOR white]aguila roja[/COLOR][/CAPITALIZE][/LOWERCASE][/B]', type=xbmcgui.INPUT_ALPHANUM).replace(" ", "%2520")
 
    url= 'https://api.rtve.es/api/search/programs?search='+d+'&page=1&size=6&context=tve&isExpanded=true&isChild=true&useOntology=true'
    headers= {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
        "Upgrade-Insecure-Requests": "1",
        
    }
    marcador = requests.get(url, headers=headers)
    if six.PY3==True :
        url = marcador.text
    else :
        url = marcador.content
    matches = plugintools.find_multiple_matches(url,'"htmlShortUrl":"https://www.rtve.es/pr/.*?"htmlUrl":".*?".*?"imageSEO":".*?".*?longDescription":"<p>.*?<.*?"name":".*?".*?')
    for generos in matches:  
        patron=plugintools.find_single_match(generos,'"htmlShortUrl":"https://www.rtve.es/pr/.*?"htmlUrl":"(.*?)".*?"imageSEO":"(.*?)".*?"imgPortada":"(.*?)".*?longDescription":"<p>(.*?)<.*?"name":"(.*?)".*?')    
        url=patron[0]

        titulo1=patron[4].replace("#8211;", "")
        texto=patron[3]
        foto=patron[1]
        foto2=patron[2]
        plugintools.set_view(plugintools.MOVIES,503)
        plugintools.add_item(action="series_tve_temporada", plot=texto,url=url,title="[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo1+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",thumbnail=foto,fanart=foto2,folder=True )
    xbmcplugin.setContent( int(sys.argv[1]) ,""+str(view_tipe)+"" )
    xbmc.executebuiltin("Container.SetViewMode("+str(view_codes)+")")
def tve_informativos(params):  
   
    thumbnail = params.get("thumbnail")    
    plugintools.add_item(action="", title="[B][LOWERCASE][CAPITALIZE][COLOR yellow]======[COLOR orange]tve_a la carta[COLOR yellow]=======[/COLOR][/CAPITALIZE][/LOWERCASE][/B]",thumbnail=thumbnail, fanart=thumbnail,folder=False )
    url=params.get("url")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers( url, headers=request_headers)
    if six.PY3==True :
        url = body.strip().decode('utf-8')
    else :
        url = body.strip()
    matches = plugintools.find_multiple_matches(url,'<div class="secBox">\n.*?<strong>\n.*?<a href="https://www.rtve.es/play/colecciones.*?".*?\n.*?\s*.*?\s*</a>')
    for generos in matches:  
        patron=plugintools.find_single_match(generos,'<div class="secBox">\n.*?<strong>\n.*?<a href="(https://www.rtve.es/play/colecciones.*?)".*?\n.*?\s*(.*?)\s*</a>')    
        ide=patron[0]

        titulo=patron[1]
        plugintools.add_item(action="series_tve_series",page='1', url=ide,title="[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",thumbnail=thumbnail,fanart=thumbnail,folder=True ) 

 




    
def tve_todos(params):  

    
    thumbnail = params.get("thumbnail")    
    plugintools.add_item(action="", title="[B][LOWERCASE][CAPITALIZE][COLOR yellow]======[COLOR orange]tve_a la carta[COLOR yellow]=======[/COLOR][/CAPITALIZE][/LOWERCASE][/B]",thumbnail=thumbnail, fanart=thumbnail,folder=False )
    url= params.get("url")+'?criteria=ASC&order=1&pageSize=40'
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers( url, headers=request_headers)
    if six.PY3==True :
        url = body.strip().decode('utf-8')
    else :
        url = body.strip()
    matches = plugintools.find_multiple_matches(url,'(?s)<li class="elem_nV.*?.*?<a href=".*?".*?class="maintitle">.*?<.*?<p>.*?<.*?src=".*?".*?alt=".*?".*?src="https://img2.rtve.es/p/.*?".*?')
    for generos in matches:  
        patron=plugintools.find_single_match(generos,'(?s)<li class="elem_nV.*?.*?<a href="(.*?)".*?class="maintitle">(.*?)<.*?<p>(.*?)<.*?src=".*?".*?alt=".*?".*?src="(https://img2.rtve.es/p/.*?)".*?')    
        url=patron[0]
        texto=patron[2]
        foto=patron[3].replace('amp;','')
        titulo1=patron[1]
        plugintools.set_view(plugintools.MOVIES,503)
        plugintools.add_item(action="series_tve_temporada", url=url,plot=texto,title="[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo1+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",thumbnail=foto,fanart=foto,folder=True ) 
    xbmcplugin.setContent( int(sys.argv[1]) ,""+str(view_tipe)+"" )
    xbmc.executebuiltin("Container.SetViewMode("+str(view_codes)+")")        
        
        
   

    plugintools.add_item(action="", title="[B][LOWERCASE][CAPITALIZE][COLOR yellow]======[COLOR orange]tve_a la carta[COLOR yellow]=======[/COLOR][/CAPITALIZE][/LOWERCASE][/B]",thumbnail=thumbnail, fanart=thumbnail,folder=False )       
      
 
def secciones_tve(params):
  
    plugintools.add_item(action = "" , title ="[B][LOWERCASE][CAPITALIZE][COLOR yellow]------------[COLOR white] tve[COLOR yellow]------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png", fanart = "https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png",  folder = False )    
    thumbnail = params.get("thumbnail") 
    fanart = params.get("thumbnail")
    url = params.get("url")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers(url, headers=request_headers)
    if six.PY3==True:
        data = body.strip().decode('utf-8')
    else:
        data = body.strip()
    matches = plugintools.find_multiple_matches(data,'<a href="https://www.rtve.es/play/colecciones/.*?".*? >\s*.*?\s*<')
    for generos in matches:
        url = plugintools.find_single_match(generos,'<a href="(https://www.rtve.es/play/colecciones/.*?)".*? >\s*.*?\s*<').replace("&amp;", "&")
        titulo = plugintools.find_single_match(generos,'<a href="https://www.rtve.es/play/colecciones/.*?".*? >\s*(.*?)\s*<')
 
 
        plugintools.add_item(action = "series_tve_series" , title ="[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" ,url =url , thumbnail ="https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png", fanart = "https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png", folder = True )

def series_tve_series(params):

    plugintools.add_item(action = "" , title ="[B][LOWERCASE][CAPITALIZE][COLOR yellow]------------[COLOR white] tve[COLOR yellow]------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png", fanart = "https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png",  folder = False )    
    thumbnail = params.get("thumbnail") 
    url = params.get("url")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers(url, headers=request_headers)
    if six.PY3==True:
        url = body.strip().decode('utf-8')
    else:
        url = body.strip()
 
    matches = plugintools.find_multiple_matches(url,'(?s)class="mod serie_mod tve">.*?<a href=".*?".*?class="maintitle">.*?<.*?src=".*?".*?src=".*?".*?alt=".*?".*?')
    for generos in matches:
        patron = plugintools.find_single_match(generos,'(?s)class="mod serie_mod tve">.*?<a href="(.*?)".*?class="maintitle">.*?<.*?src="(.*?)".*?src="(.*?)".*?alt="(.*?)".*?')
        url5=patron[0]
        titulo = patron[3]
        foto = patron[1]
        foto2 = patron[2]
 
        plugintools.add_item(action = "series_tve_temporada" , title ="[B][LOWERCASE][CAPITALIZE][COLOR yellow][COLOR aqua]"+titulo+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" ,url =url5, thumbnail =foto2,fanart = foto,folder = True )
 
 
 
 
 
    plugintools.add_item(action = "" , title ="[B][LOWERCASE][CAPITALIZE][COLOR yellow]------------[COLOR white] tve[COLOR yellow]------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png", fanart = "https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png",  folder = False )   
 
 
 
 
def series_tve_temporada(params):

    plugintools.add_item(action = "" , title ="[B][LOWERCASE][CAPITALIZE][COLOR yellow]------------[COLOR white] tve[COLOR yellow]------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png", fanart = "https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png",  folder = False )    
    thumbnail = params.get("thumbnail") 
    url5 = params.get("url")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"])
    body,response_headers = plugintools.read_body_and_headers(url5, headers=request_headers)
    if six.PY3==True:
        url = body.strip().decode('utf-8')
    else:
        url = body.strip() 
 
    page = plugintools.find_single_match(url,'data-tab="capters"   >.*?data-module="(/play/videos/modulos.*?)"')
    url ='https://www.rtve.es'+page
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers(url, headers=request_headers)
    if six.PY3==True:
        url3 = body.strip().decode('utf-8')
    else:
        url3 = body.strip()
    if 'Seleccionar temporada' in url3:  
        matches = plugintools.find_multiple_matches(url3,'(?s)data-season=".*?" data-order=".*?<a href=".*?"><span>.*?</span>')
        for generos in matches:
            url = plugintools.find_single_match(generos,'(?s)data-season=".*?" data-order=".*?<a href="(.*?)"><span>.*?</span>')   
            titulo = plugintools.find_single_match(generos,'(?s)data-season=".*?" data-order=".*?<a href=".*?"><span>(.*?)</span>')   
 
            plugintools.add_item(action = "series_tve_capitulos" ,url=url, title ="[B][LOWERCASE][CAPITALIZE][COLOR yellow]"+titulo+ " [COLOR lime] [/CAPITALIZE][/LOWERCASE][/B][/COLOR]",plot='' , thumbnail =thumbnail,fanart =thumbnail,folder = True )
    else:  
        matches = plugintools.find_multiple_matches(url3,'(?s)li class="elem_nH getoff.*?"imagen": ".*?".*?class="maintitle">.*?<.*?<.*?href="https://www.rtve.es/play/videos/.*?"')
        for generos in matches:
            patron = plugintools.find_single_match(generos,'(?s)li class="elem_nH getoff.*?"imagen": "(.*?)".*?class="maintitle">(.*?)<.*?href="(https://www.rtve.es/play/videos/.*?)"')   
            
            titulo = patron[1].replace("\&quot;", '"')
            try:
                texto= plugintools.find_single_match(generos,'(?s)description .*?<p>(.*?)<.*?')
                capitulo = plugintools.find_single_match(generos,'(?s)class="capter">(.*?)<.*?')     
            except:
                texto= ''
                capitulo = ''                          
            foto = patron[0]
            url = patron[2]
            plugintools.set_view(plugintools.MOVIES,503)
            plugintools.add_item(action = "javi_descarga" ,url=url, title ="[B][LOWERCASE][CAPITALIZE][COLOR white]capitulo "+capitulo+" [COLOR yellow]"+titulo+ " [COLOR lime] [/CAPITALIZE][/LOWERCASE][/B][/COLOR]",plot="[B][LOWERCASE][CAPITALIZE][COLOR orange]"+texto+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" , thumbnail =foto,fanart =thumbnail,folder=False,  isPlayable = True )   
    xbmcplugin.setContent( int(sys.argv[1]) ,""+str(view_tipe)+"" )
    xbmc.executebuiltin("Container.SetViewMode("+str(view_codes)+")") 
def series_tve_capitulos(params):

    plugintools.add_item(action = "" , title ="[B][LOWERCASE][CAPITALIZE][COLOR yellow]------------[COLOR white] tve[COLOR yellow]------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png", fanart = "https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png",  folder = False )    
    thumbnail = params.get("thumbnail") 
    url = 'https://www.rtve.es'+params.get("url")
 
    count=8
    pn=1
    data=[]
    while pn <= int(count):
        page=url+'/?page='+str(pn)
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"}
        if six.PY3==True:
            source=requests.get(page, headers=headers).text
        else:
            source=requests.get(page, headers=headers).content
        data += plugintools.find_multiple_matches(source,'(?s)li class="elem_nH getoff.*?"imagen": ".*?".*?class="maintitle">.*?<.*?<.*?.*?<.*?href="https://www.rtve.es/play/videos/.*?"')
        pn +=1
 
    matches=data
    for generos in matches:
        foto = plugintools.find_single_match(generos,'"imagen": "(.*?)"')   
        titulo = plugintools.find_single_match(generos,'class="maintitle">(.*?)<')
        try:
            capitulo = plugintools.find_single_match(generos,' <span class="capter">(.*?)</span>')   
            texto = plugintools.find_single_match(generos,'description .*?<p>(.*?)<.*?')
        except:
            capitulo = ''
            texto=''            
        url = plugintools.find_single_match(generos,'href="(https://www.rtve.es/play/videos/.*?)"') 
        plugintools.set_view(plugintools.MOVIES,503)
        plugintools.add_item(action = "javi_descarga" ,url=url, title ="[B][LOWERCASE][CAPITALIZE][COLOR white] "+capitulo+"  [COLOR yellow]"+titulo+ " [COLOR lime] [/CAPITALIZE][/LOWERCASE][/B][/COLOR]",plot="[B][LOWERCASE][CAPITALIZE][COLOR yellow]"+texto+ " [COLOR lime] [/CAPITALIZE][/LOWERCASE][/B][/COLOR]" , thumbnail =foto,fanart =thumbnail, folder=False,  isPlayable = True )
    xbmcplugin.setContent( int(sys.argv[1]) ,""+str(view_tipe)+"" )
    xbmc.executebuiltin("Container.SetViewMode("+str(view_codes)+")") 

def javi_descarga(params): 
  
    url = params.get("url") 
    s = "regex"
    def dec(s):
        import re, requests
        url2 = 'https://www.descargavideos.tv/'
        headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
        "Content-Type": "application/x-www-form-urlencoded",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1"
    }
        params ={"web":url}
        s = requests.Session()
        if six.PY3==True:
            logueo = requests.post(url2, headers=headers, data=params)
            r = logueo.text
        else:
            logueo = requests.post(url2, headers=headers, data=params)
            r = logueo.content
        return(r)
 
    esto = dec(s)
    url = plugintools.find_single_match(esto,'link" rel="noreferrer" href="(.*?)".*?Opci')+'|user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:145.0) Gecko/20100101 Firefox/145.0' 
    
    plugintools.play_resolved_url(url)    

 
 
 

def SERIES_ESPECIALES(params):
    
    plugintools.set_view(plugintools.LIST) 
    thumbnail = params.get("thumbnail")    
    plugintools.add_item( action="DEPORTUBE4", title="[B][LOWERCASE][CAPITALIZE][COLOR aqua]--------------------[/COLOR][COLOR yellow]especial SERIES tvchopo[COLOR aqua]---------------------[/COLOR][/CAPITALIZE][/LOWERCASE][/B]", thumbnail='https://st-listas.20minutos.es/images/2011-09/301470/list_640px.jpg?1315184785', fanart='https://static3.lavozdigital.es/media/ocio/tv/2016/03/01/v/canciones-serie-infantiles3--620x349.jpg',url='',folder=False )  
 
    plugintools.add_item( action="DEPORTUBE4", title="[B][LOWERCASE][CAPITALIZE][COLOR lime][COLOR white]rui el pequeño cid[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail='http://www.museodelnaipe.com/naipecoleccion/image/cache/data/Ruyelpeque%C3%B1ocid1-500x500.jpg', fanart='https://images.justwatch.com/backdrop/52225648/s640/ruy-el-pequeno-cid',url='https://www.youtube.com/watch?v=4KY-WmxftUM&list=PL1812714DE488ECFC',folder=True ) 
 
 
 

 
    plugintools.add_item( action="DEPORTUBE4", title="[B][LOWERCASE][CAPITALIZE][COLOR white]Las aventuras de Teddy Ruxpin[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail='https://i.imgur.com/jY0tOqZ.jpg', fanart='https://i.imgur.com/jY0tOqZ.jpg',url='https://www.youtube.com/watch?v=fZPv0cdLSd0&list=PLvVLlsVj1Vgj1tBps9gIoDoT81RPVQU5A',folder=True ) 
 
 
    plugintools.add_item( action="DEPORTUBE4", title="[B][LOWERCASE][CAPITALIZE][COLOR lime][COLOR white]POPEYE   [/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail='https://parecidas.com/img_es/movie/thumb/4a/35513.jpg', fanart='https://parecidas.com/img_es/movie/thumb/4a/35513.jpg',url='https://www.youtube.com/watch?v=DgQCJ8HPJCA&list=PLV0ww1Vq7oOxQs1VyZqMOzQuaclGbLRmD',folder=True ) 
 
    plugintools.add_item( action="DEPORTUBE4", title="[B][LOWERCASE][CAPITALIZE][COLOR lime][COLOR white]ALVIN Y LAS ARDILLAS  [/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail='https://es.web.img3.acsta.net/pictures/15/11/12/13/40/265670.jpg', fanart='https://es.web.img3.acsta.net/pictures/15/11/12/13/40/265670.jpg',url='https://www.youtube.com/watch?v=V6iOmr47ePc&list=PLu3eYgTaETWqwmipmgL6PI8EfoBylXJbg',folder=True ) 
 

 
    plugintools.add_item( action="DEPORTUBE4", title="[B][LOWERCASE][CAPITALIZE][COLOR lime][COLOR white]los cazafantasmas  [/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail='https://i.imgur.com/biqj7Mh.jpg', fanart='https://i.imgur.com/biqj7Mh.jpg',url='https://www.youtube.com/watch?v=bRDJRNXsThM&list=PLhcFeyCsqAAXXK2XS03ZnNZyE2YET8yl-',folder=True ) 
 
    plugintools.add_item( action="DEPORTUBE4", title="[B][LOWERCASE][CAPITALIZE][COLOR lime][COLOR white]Mofli, el último koala  [/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail='https://i1.wp.com/www.rebecasanchez.es/wp-content/uploads/2009/04/mofli41.jpg?w=635', fanart='https://i1.wp.com/www.rebecasanchez.es/wp-content/uploads/2009/04/mofli41.jpg?w=635',url='https://www.youtube.com/watch?v=OudbZHQgL04&list=PLKKK82DrF4db5Cq-rOUirBOtoRjJvhvsC',folder=True ) 
 
 
 
 
    plugintools.add_item( action="DEPORTUBE4", title="[B][LOWERCASE][CAPITALIZE][COLOR lime][COLOR white]Inspector Gadget  [/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail='https://1.bp.blogspot.com/-rkJLJmB15B8/XVC9ENnKqgI/AAAAAAABADY/hj0vy26JzCs0mjQksnyb-dkLMSprab3HACLcBGAs/s1600/inspector%2Bgadget.jpg', fanart='https://1.bp.blogspot.com/-rkJLJmB15B8/XVC9ENnKqgI/AAAAAAABADY/hj0vy26JzCs0mjQksnyb-dkLMSprab3HACLcBGAs/s1600/inspector%2Bgadget.jpg',url='https://www.youtube.com/watch?v=gTjd0VbDqNQ&list=PLQrG71R4T-nJ3aeMzWhP0U0Luy3USWdXN',folder=True ) 
 
 
    plugintools.add_item( action="DEPORTUBE4", title="[B][LOWERCASE][CAPITALIZE][COLOR lime][COLOR white]He-Man y los Masters del Universo  [/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail='https://i.imgur.com/cLxufNn.jpg', fanart='https://i.imgur.com/cLxufNn.jpg',url='https://www.youtube.com/watch?v=Stwkaqqtous&list=PLHVth4IGGf8uJ8WoenAucdukgFmzgWvmv',folder=True ) 
 
    plugintools.add_item( action="DEPORTUBE4", title="[B][LOWERCASE][CAPITALIZE][COLOR lime][COLOR white]LUCKY LUKE  [/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail='https://assets.thalia.media/img/artikel/848a368d3bf49ac0e75996df4a436cccf7317e74-00-00.jpeg', fanart='https://assets.thalia.media/img/artikel/848a368d3bf49ac0e75996df4a436cccf7317e74-00-00.jpeg',url='https://www.youtube.com/watch?v=oJk3rxJ3l10&list=PLmdLOXt-r6Y94QmmyoJ-cm3dhFdGsgOKg',folder=True ) 
 
 
 
    plugintools.add_item( action="DEPORTUBE4", title="[B][LOWERCASE][CAPITALIZE][COLOR lime][COLOR white]los fruitis  [/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail='https://i.pinimg.com/originals/2a/31/1c/2a311c9a6dc7b828b4db6326484dd3e0.jpg', fanart='https://i.pinimg.com/originals/2a/31/1c/2a311c9a6dc7b828b4db6326484dd3e0.jpg',url='https://www.youtube.com/watch?v=cCrJDEZArew&list=PLKyxl_P11uR1st3aqWqrJtYKsunbfIGIg',folder=True ) 
 
    plugintools.add_item( action="DEPORTUBE4", title="[B][LOWERCASE][CAPITALIZE][COLOR lime][COLOR white]daniel el travieso  [/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail='https://pictures.abebooks.com/HIPERCOMIC/md/md30132610623.jpg', fanart='https://pictures.abebooks.com/HIPERCOMIC/md/md30132610623.jpg',url='https://www.youtube.com/watch?v=uL_E5wum6hI&list=PLrzXhAF3O2FOaRwEQblgHh0zyMZ6EcNPZ',folder=True ) 
 
 
    plugintools.add_item( action="DEPORTUBE4", title="[B][LOWERCASE][CAPITALIZE][COLOR lime][COLOR white]los osos amorosos  [/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail='https://cloud10.todocoleccion.online/album-incompleto/tc/2013/09/29/39249373.jpg', fanart='https://cloud10.todocoleccion.online/album-incompleto/tc/2013/09/29/39249373.jpg',url='https://www.youtube.com/watch?v=vE7gDUUmGG0&list=PLyq8RHRc3jNh2wu2N4eVT5z1RyRWrEkdn',folder=True ) 
 

 
    plugintools.add_item( action="DEPORTUBE4", title="[B][LOWERCASE][CAPITALIZE][COLOR lime][COLOR white]el gato isidoro   [/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail='https://images-na.ssl-images-amazon.com/images/I/7165TkzoZWL._SL1370_.jpg', fanart='https://images-na.ssl-images-amazon.com/images/I/7165TkzoZWL._SL1370_.jpg',url='https://www.youtube.com/watch?v=2xUmmgPyrbg&list=PLyq8RHRc3jNjinn6pHFmIY6C3aRNunCOw',folder=True ) 
 
 
    plugintools.add_item( action="DEPORTUBE4", title="[B][LOWERCASE][CAPITALIZE][COLOR lime][COLOR white]la abeja maya  [/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail='https://2.bp.blogspot.com/-ZzetehVCHTo/XAJH7U0y2nI/AAAAAAAACCg/MZGaGkdsftcNgispdSp9b5GlXuJaIM_NQCLcBGAs/s1600/maya.jpg', fanart='https://2.bp.blogspot.com/-ZzetehVCHTo/XAJH7U0y2nI/AAAAAAAACCg/MZGaGkdsftcNgispdSp9b5GlXuJaIM_NQCLcBGAs/s1600/maya.jpg',url='https://www.youtube.com/watch?v=E-pKGTkcUkQ&list=PLYpTR-80tSP2dA3FsuEklQm_u4mtLoQdA',folder=True ) 
 
 
    plugintools.add_item( action="DEPORTUBE4", title="[B][LOWERCASE][CAPITALIZE][COLOR lime][COLOR white]Marco    [/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail='https://cloud10.todocoleccion.online/tebeos-marco/tc/2016/10/20/20/63261812.jpg', fanart='https://cloud10.todocoleccion.online/tebeos-marco/tc/2016/10/20/20/63261812.jpg',url='https://www.youtube.com/watch?v=hBZyqA8pjXQ&list=PLutxf9xWvQKa0-ZMI5fyFSeABblPOF3Kk',folder=True )     
 
 
    plugintools.add_item( action="DEPORTUBE4", title="[B][LOWERCASE][CAPITALIZE][COLOR lime][COLOR white]Heidi      [/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail='https://edicola.shop/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/i/m/image_340_1_24335.jpg', fanart='https://edicola.shop/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/i/m/image_340_1_24335.jpg',url='https://www.youtube.com/watch?v=n5qQMnje_kU&list=PLUuRJYptYFXBmaLE1oNJYPxyl-3mSLKL3',folder=True )
 
    plugintools.add_item( action="DEPORTUBE4", title="[B][LOWERCASE][CAPITALIZE][COLOR lime][COLOR white]los pitufos   [/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail='https://2.bp.blogspot.com/-qn-4wBcU8gE/WU_6maJ2dXI/AAAAAAAACcc/JdMLvN_p0kcFbL62MYP2oi6PPiu84q7NACLcBGAs/s1600/los%2Bpitufos.jpg', fanart='https://2.bp.blogspot.com/-qn-4wBcU8gE/WU_6maJ2dXI/AAAAAAAACcc/JdMLvN_p0kcFbL62MYP2oi6PPiu84q7NACLcBGAs/s1600/los%2Bpitufos.jpg',url='https://www.youtube.com/watch?v=PNKQQ_N6L8g&list=PLynb7MteT3bv-JXyQJFD0dgMX1p-kbTyw',folder=True )
 
    plugintools.add_item( action="DEPORTUBE4", title="[B][LOWERCASE][CAPITALIZE][COLOR lime][COLOR white]los trotamusicos   [/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail='https://images-na.ssl-images-amazon.com/images/I/51nADpEtELL._SY445_.jpg', fanart='https://images-na.ssl-images-amazon.com/images/I/51nADpEtELL._SY445_.jpg',url='https://www.youtube.com/watch?v=CLvxg1YH3zg&list=PLjGG4eB-AY7lLRIEZTftqW63JTe6jCg1W',folder=True )    
 
    plugintools.add_item( action="DEPORTUBE4", title="[B][LOWERCASE][CAPITALIZE][COLOR lime][COLOR white]D'Artacán y los tres mosqueperros [/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail='https://brb.es/wp-content/uploads/2018/06/DARTAC%C3%81N.jpg', fanart='https://brb.es/wp-content/uploads/2018/06/DARTAC%C3%81N.jpg',url='https://www.youtube.com/watch?v=J9jaLvw6QiM&list=PLQ1EusvOGEavUOGO6nTfwDGj8NvrbaDgg',folder=True )
 
    plugintools.add_item( action="DEPORTUBE4", title="[B][LOWERCASE][CAPITALIZE][COLOR lime][COLOR white]Sherlock Holmes series  [/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail='https://images-na.ssl-images-amazon.com/images/I/51gUhLKDJ2L._SY445_.jpg', fanart='https://images-na.ssl-images-amazon.com/images/I/51gUhLKDJ2L._SY445_.jpg',url='https://www.youtube.com/watch?v=2HDDvei0RSA&list=PL04gTKRCAl-Pc6AEz99h-lhC49Q6O2Pas',folder=True )
 
    plugintools.add_item( action="DEPORTUBE4", title="[B][LOWERCASE][CAPITALIZE][COLOR lime][COLOR white]los fraguels rocks  [/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail='https://www.medusacomics.es/media/medusa_comics/images/cover-95405.jpg', fanart='https://www.medusacomics.es/media/medusa_comics/images/cover-95405.jpg',url='https://www.youtube.com/watch?v=9mQ_Im0MBlg&list=PLyq8RHRc3jNgMVBPL8UMnczVVLD1d00Tl',folder=True )
 
    plugintools.add_item( action="DEPORTUBE4", title="[B][LOWERCASE][CAPITALIZE][COLOR lime][COLOR white]Campeones. Oliver y Benji  [/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail='https://images-na.ssl-images-amazon.com/images/I/91aqJ%2BBCFbL._SL1500_.jpg', fanart='https://images-na.ssl-images-amazon.com/images/I/91aqJ%2BBCFbL._SL1500_.jpg',url='https://www.youtube.com/watch?v=Rd0jtrc3Ml8&list=PL6jR_8PLNNy8SIa4R2xyjGZlMLgLLp7E-',folder=True )    
 
    plugintools.add_item( action="DEPORTUBE4", title="[B][LOWERCASE][CAPITALIZE][COLOR lime][COLOR white]dragones y mazmorras serie  [/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail='https://i.pinimg.com/originals/9f/c6/1b/9fc61b0da761affd3c15d23f0f974afc.jpg', fanart='https://i.pinimg.com/originals/9f/c6/1b/9fc61b0da761affd3c15d23f0f974afc.jpg',url='https://www.youtube.com/watch?v=VuaYo4KVRhY&list=PLsHZRFRhMph1o1qcw0MO71pPtnJrupuvy',folder=True )
 
    plugintools.add_item( action="DEPORTUBE4", title="[B][LOWERCASE][CAPITALIZE][COLOR lime][COLOR white]las aventuras de tom sawyer  [/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail='https://images-na.ssl-images-amazon.com/images/I/91iDH7Kw75L._SY445_.jpg', fanart='https://images-na.ssl-images-amazon.com/images/I/91iDH7Kw75L._SY445_.jpg',url='https://www.youtube.com/watch?v=cjTFxJSupYo&list=PLFx214hsEASeKomaRgURlVHA_obnZkho2',folder=True )    
 
 
    plugintools.add_item( action="DEPORTUBE4", title="[B][LOWERCASE][CAPITALIZE][COLOR lime][COLOR white]Ulises 31  [/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail='https://3.bp.blogspot.com/-OYxPadKL3nI/UXWO8OizD0I/AAAAAAAAAuY/RwG1hNeAjng/s1600/ulises31-imagen.jpg', fanart='https://3.bp.blogspot.com/-OYxPadKL3nI/UXWO8OizD0I/AAAAAAAAAuY/RwG1hNeAjng/s1600/ulises31-imagen.jpg',url='https://www.youtube.com/watch?v=fns5R61QhhI&list=PL99kuo33pyKXVljP_1-9eSUrES6915Uk9',folder=True )
 
    plugintools.add_item( action="DEPORTUBE4", title="[B][LOWERCASE][CAPITALIZE][COLOR lime][COLOR white]LOS DIMINUTOS  [/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail='https://i.imgur.com/dj7UekS.jpg', fanart='https://i0.wp.com/www.misstechin.com/wp-content/uploads/2019/01/los-diminutos-2.jpg?fit=1440%2C750&ssl=1',url='https://www.youtube.com/watch?v=lPHVQGZX54w&list=PLx5yOvA8qMRWVlvCjkWrJkAuzb9J-OVts',folder=True )
 
    plugintools.add_item( action="DEPORTUBE4", title="[B][LOWERCASE][CAPITALIZE][COLOR lime][COLOR white]David, el Gnomo  [/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail='https://images-na.ssl-images-amazon.com/images/I/81QfqudCRyL._SY445_.jpg', fanart='https://images-na.ssl-images-amazon.com/images/I/81QfqudCRyL._SY445_.jpg',url='https://www.youtube.com/watch?v=2dCUmOQfQ4E&list=PL6jgvKHZMaUX_JfZPZ_GCsHx1aSNmnIjo',folder=True )
 
    plugintools.add_item( action="DEPORTUBE4", title="[B][LOWERCASE][CAPITALIZE][COLOR lime][COLOR white]la vuelta al mundo en 80 dias de willy fog  [/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail='https://brb.es/wp-content/uploads/2018/06/VUELTA-WILLY-FOG.jpg', fanart='https://brb.es/wp-content/uploads/2018/06/VUELTA-WILLY-FOG.jpg',url='https://www.youtube.com/watch?v=GJUnJcKjeyA&list=PL82F9AECFA0523F53',folder=True )
 
    plugintools.add_item( action="DEPORTUBE4", title="[B][LOWERCASE][CAPITALIZE][COLOR lime][COLOR white]Érase una vez el cuerpo humano  [/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail='https://pictures.abebooks.com/LIBRERIADAVINCI/22637626161.jpg', fanart='https://pictures.abebooks.com/LIBRERIADAVINCI/22637626161.jpg',url='https://www.youtube.com/watch?v=CtCQI8gP1HM&list=PL3trIOgZnbH1Xk_qpl2srL5wYlgd8Bu9f',folder=True )    
 
    plugintools.add_item( action="DEPORTUBE4", title="[B][LOWERCASE][CAPITALIZE][COLOR aqua]--------------------[/COLOR][COLOR yellow]especial SERIES tvchopo[COLOR aqua]---------------------[/COLOR][/CAPITALIZE][/LOWERCASE][/B]", thumbnail='https://st-listas.20minutos.es/images/2011-09/301470/list_640px.jpg?1315184785', fanart='https://static3.lavozdigital.es/media/ocio/tv/2016/03/01/v/canciones-serie-infantiles3--620x349.jpg',url='',folder=False )  
 

 
 
def DEPORTUBE4(params): 

    thumbnail = params.get("thumbnail")    
    plugintools.add_item(action="", title="[B][LOWERCASE][CAPITALIZE][COLOR fuchsia]YOUTUBE [COLOR lime][/CAPITALIZE][/LOWERCASE][/B][/COLOR]",thumbnail=thumbnail,fanart=thumbnail,folder=False ) 
 
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
 
    url = params.get("url")
    if six.PY3==True:
        data=requests.get(url, headers=headers, verify=False).text
    else:
        data=requests.get(url, headers=headers, verify=False).content
 
    matches = plugintools.find_multiple_matches(data,'playlistPanelVideoRenderer":{"title":.*?simpleText":".*?".*?"videoId":".*?"')
    for generos in matches:
        url = plugintools.find_single_match(generos,'"videoId":"(.*?)"')
        title = plugintools.find_single_match(generos,'simpleText":"(.*?)".*?')
 
        plugintools.add_item(action = "DEPORTUBE5" , title = "[B][LOWERCASE][CAPITALIZE][COLOR white]"+title+"[/COLOR][/CAPITALIZE][/LOWERCASE][/B]", url = 'https://www.youtube.com/watch?v='+url,thumbnail = 'https://i.ytimg.com/vi/'+url+'/hqdefault.jpg', fanart = 'https://i.ytimg.com/vi/'+url+'/hqdefault.jpg', folder=False,  isPlayable = True ) 
 
def DEPORTUBE5(params): 

    thumbnail = params.get("thumbnail")    
    plugintools.add_item(action="", title="[B][LOWERCASE][CAPITALIZE][COLOR fuchsia]YOUTUBE [COLOR lime][/CAPITALIZE][/LOWERCASE][/B][/COLOR]",thumbnail=thumbnail,fanart=thumbnail,folder=False ) 
    url = params.get("url")
    import resolveurl 
    video = resolveurl.resolve( url )
    plugintools.play_resolved_url(video) 


def repelishd_buscador(params):
    import xbmc, time
    thumbnail = params.get("thumbnail") 
    cookies, url2base = obtener_proxy()
    dialog = xbmcgui.Dialog()
    d = dialog.input('[B][LOWERCASE][CAPITALIZE][COLOR orange]buscar una peli: ejemplo: [COLOR white]rocky[/COLOR][/CAPITALIZE][/LOWERCASE][/B]', type=xbmcgui.INPUT_ALPHANUM).replace(" ", "+")
    intentos = 0
    source1 = None
    while intentos < 20:
        intentos += 1 
         
        url=url2base+'catalog/a?story='+d+'&do=search&subaction=search&__cpo=aHR0cHM6Ly9yZXBlbGlzaGQuY2Ft'
        headers= {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0","cookie":cookies}    
        source=requests.get(url, headers=headers, verify=False)
        status_code =source.status_code
        if status_code == 200:
            source1=source.content  # Esto ya es el contenido decodificado
            break    
    if source1:    
        token = source1.decode('utf-8') 
        pattern = r'(?s)<article class="item movies">.*?<img src="([^"]+)" alt="([^"]+)">.*?<span class="quality">([^<]+)</span>.*?<a href="https://repelishd.city/([^"]+)">.*?<div class="audio">.*?<div class="[^"]+"></div>.*?</div>.*?<h3><a href="[^"]+">[^<]+</a></h3>\s*<span>(\d{4})</span>'
   
# Buscar coincidencias
        matches = re.findall(pattern, token, re.DOTALL)
# Mostrar resultados
        for foto, titulo, calidad, url,  year in matches:
            foto=url2base+foto+'?__cpo=aHR0cHM6Ly9yZXBlbGlzaGQuY2Ft|cookie='+cookies
            url=url2base+url
            plugintools.add_item(action="repelishd_servers",extra=titulo, url=url,title="[B][COLOR white]"+titulo+" [COLOR yellow]"+calidad+"  [COLOR red]"+year+"[/COLOR][/B]",thumbnail=foto,fanart=foto,page=params.get("page", "{}"),folder=True) 



def repelishd_alfabetico(params):
    import xbmc, time
    thumbnail = params.get("thumbnail")    
    generos = '''    <ul class=glossary>
      <li><a href="/catalog/09">#</a></li>
      <li><a href="/catalog/a">A</a></li>
      <li><a href="/catalog/b">B</a></li>
      <li><a href="/catalog/c">C</a></li>
      <li><a href="/catalog/d">D</a></li>
      <li><a href="/catalog/e">E</a></li>
      <li><a href="/catalog/f">F</a></li>
      <li><a href="/catalog/g">G</a></li>
      <li><a href="/catalog/h">H</a></li>
      <li><a href="/catalog/i">I</a></li>
      <li><a href="/catalog/j">J</a></li>
      <li><a href="/catalog/k">K</a></li>
      <li><a href="/catalog/l">L</a></li>
      <li><a href="/catalog/m">M</a></li>
      <li><a href="/catalog/n">N</a></li>
      <li><a href="/catalog/o">O</a></li>
      <li><a href="/catalog/p">P</a></li>
      <li><a href="/catalog/q">Q</a></li>
      <li><a href="/catalog/r">R</a></li>
      <li><a href="/catalog/s">S</a></li>
      <li><a href="/catalog/t">T</a></li>
      <li><a href="/catalog/u">U</a></li>
      <li><a href="/catalog/v">V</a></li>
      <li><a href="/catalog/w">W</a></li>
      <li><a href="/catalog/x">X</a></li>
      <li><a href="/catalog/y">Y</a></li>
      <li><a href="/catalog/z">Z</a></li>
    </ul>'''  

    gamo=plugintools.find_multiple_matches(generos,'<li><a href="/(catalog)/(.*?)">.*?</a></li>') 
    for tema,titulo in gamo:
        tema=tema+'/'+titulo
        pagina='1'

        plugintools.add_item(action = "repelishd_pelis" , title ="[B][LOWERCASE][CAPITALIZE][COLOR white]pelis que empiezan por: [COLOR red] "+titulo+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail =thumbnail, fanart ='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTlQn_-m8utZCiPrhQe2P3pROEJITO1PDI2Hw&s', url= tema,extra=pagina, folder = True )




def repelishd_idiomas(params):
    import xbmc, time
    thumbnail = params.get("thumbnail")   
    generos = '''<div class="latino"></div>
                 <div class="castellano"></div>
			     <div class="sub"></div>'''  

    gamo=plugintools.find_multiple_matches(generos,'<div class="(.*?)">') 
    for idioma in gamo:
        
        pagina='1'
        url=url2base+'pelicula/page/'+pagina+'/?language='+idioma+'&__cpo=aHR0cHM6Ly9yZXBlbGlzaGQuY2Ft'
        plugintools.add_item(action = "repelishd_pelis_paises" , title ="[B][LOWERCASE][CAPITALIZE][COLOR white]pelis con idioma en: [COLOR red] "+idioma+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail =thumbnail, fanart ='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTlQn_-m8utZCiPrhQe2P3pROEJITO1PDI2Hw&s', url= url,extra=pagina, folder = True )

def repelishd_pelis_paises(params):
    import xbmc, time
    thumbnail = params.get("thumbnail")
    url=params.get("url")
    cookies, url2base = obtener_proxy() 
    pagina=params.get("extra")
    intentos = 0
    source1 = None
    while intentos < 20:
        intentos += 1 
           
        headers= {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0","cookie":cookies}
        source=requests.get(url, headers=headers, verify=False)
        status_code =source.status_code
        if status_code == 200:
            source1=source.content  # Esto ya es el contenido decodificado
            break    
    if source1:
        token = source1.decode('utf-8')   
        pattern = r'<article class="item movies">.*?<img src="([^"]+)" alt="([^"]+)">.*?<span class="quality">([^<]+)</span>.*?<a href="([^"]+)">.*?<div class="audio">.*?<div class="[^"]+"></div>.*?</div>.*?<h3><a href="[^"]+">[^<]+</a></h3>\s*<span>(\d{4})</span>'
        paginas = r'<a href="https://repelishd.cam/(pelicula/page/.*?\d+.*?)">(\d+)(?!"><)'
# Buscar coincidencias
        matches = re.findall(pattern, token, re.DOTALL)
# Mostrar resultados
        for foto, titulo, calidad, url,  year in matches:
            foto=url2base+foto+'?__cpo=aHR0cHM6Ly9yZXBlbGlzaGQuY2Ft|cookie='+cookies
            plugintools.add_item(action="repelishd_servers",extra=titulo, url=url,title="[B][COLOR white]"+titulo+" [COLOR yellow]"+calidad+"  [COLOR red]"+year+"[/COLOR][/B]",thumbnail=foto,fanart=foto,folder=True) 
        urls = re.findall(paginas, token)
        for url,paginas in urls:
            url=url2base+url+'&__cpo=aHR0cHM6Ly9yZXBlbGlzaGQuY2Ft'
            plugintools.add_item(action="repelishd_pelis_paises",extra=paginas, url=url,title="[B][COLOR lime]ir a la pagina "+paginas+"[/COLOR][/B]",thumbnail='',fanart='',folder=True)

def repelishd_paises(params):
    import xbmc, time
    thumbnail = params.get("thumbnail") 
    generos = '''          
                                                                    <div class="value-wrapper">
                                <input type="radio" name="country" id="countryEspaña" value="España" >
                                <label for="countryEspaña">España</label>
                            </div>
                                                        <div class="value-wrapper">
                                <input type="radio" name="country" id="countryMéxico" value="México" checked="checked">
                                <label for="countryMéxico">México</label>
                            </div>
                                                        <div class="value-wrapper">
                                <input type="radio" name="country" id="countryBrasil" value="Brasil" >
                                <label for="countryBrasil">Brasil</label>
                            </div>
                                                        <div class="value-wrapper">
                                <input type="radio" name="country" id="countryAlemania" value="Alemania" >
                                <label for="countryAlemania">Alemania</label>
                            </div>
                                                        <div class="value-wrapper">
                                <input type="radio" name="country" id="countryEstados Unidos" value="Estados Unidos" >
                                <label for="countryEstados Unidos">Estados Unidos</label>
                            </div>
                                                        <div class="value-wrapper">
                                <input type="radio" name="country" id="countryReino Unido" value="Reino Unido" >
                                <label for="countryReino Unido">Reino Unido</label>
                            </div>
                                                        <div class="value-wrapper">
                                <input type="radio" name="country" id="countryItalia" value="Italia" >
                                <label for="countryItalia">Italia</label>
                            </div>
                                                        <div class="value-wrapper">
                                <input type="radio" name="country" id="countryFrancia" value="Francia" >
                                <label for="countryFrancia">Francia</label>
                            </div>
                                                        <div class="value-wrapper">
                                <input type="radio" name="country" id="countryCanadá" value="Canadá" >
                                <label for="countryCanadá">Canadá</label>
                            </div>
                                                        <div class="value-wrapper">
                                <input type="radio" name="country" id="countryJapón" value="Japón" >
                                <label for="countryJapón">Japón</label>
                            </div>
                                                        <div class="value-wrapper">
                                <input type="radio" name="country" id="countryIndia" value="India" >
                                <label for="countryIndia">India</label>
                            </div>
                                                        <div class="value-wrapper">
                                <input type="radio" name="country" id="countryAustralia" value="Australia" >
                                <label for="countryAustralia">Australia</label>
                            </div>
                                                        <div class="value-wrapper">
                                <input type="radio" name="country" id="countryRusia" value="Rusia" >
                                <label for="countryRusia">Rusia</label>
                            </div>
                                                        <div class="value-wrapper">
                                <input type="radio" name="country" id="countryBélgica" value="Bélgica" >
                                <label for="countryBélgica">Bélgica</label>
                            </div>
                                                        <div class="value-wrapper">
                                <input type="radio" name="country" id="countryPolonia" value="Polonia" >
                                <label for="countryPolonia">Polonia</label>
                            </div>
                                                        <div class="value-wrapper">
                                <input type="radio" name="country" id="countryNoruega" value="Noruega" >
                                <label for="countryNoruega">Noruega</label>
'''  

    gamo=plugintools.find_multiple_matches(generos,'<input type="radio" name="country" id=".*?" value="(.*?)"') 
    for pais in gamo:
        tema='?country='+pais
        pagina='1'
        url=url2base+'pelicula/page/'+pagina+'/'+tema+'&__cpo=aHR0cHM6Ly9yZXBlbGlzaGQuY2Ft'
        plugintools.add_item(action = "repelishd_pelis_paises" , title = "  [B][LOWERCASE][CAPITALIZE][COLOR white]pelis de [COLOR red] "+pais+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail =thumbnail, fanart ='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTlQn_-m8utZCiPrhQe2P3pROEJITO1PDI2Hw&s', url= url,extra=pagina, folder = True )




def repelishd_anios(params):
    import xbmc, time
    thumbnail = params.get("thumbnail")    
    generos = '''          <li><a style="color: #fff;" href="/xfsearch/year/2025">2025</a></li>
<li><a style="color: #fff;" href="/xfsearch/year/2024">2024</a></li>
<li><a style="color: #fff;" href="/xfsearch/year/2023">2023</a></li>
<li><a style="color: #fff;" href="/xfsearch/year/2022">2022</a></li>
<li><a style="color: #fff;" href="/xfsearch/year/2021">2021</a></li>
<li><a style="color: #fff;" href="/xfsearch/year/2020">2020</a></li>
<li><a style="color: #fff;" href="/xfsearch/year/2019">2019</a></li>
<li><a style="color: #fff;" href="/xfsearch/year/2018">2018</a></li>
<li><a style="color: #fff;" href="/xfsearch/year/2017">2017</a></li>
<li><a style="color: #fff;" href="/xfsearch/year/2016">2016</a></li>
<li><a style="color: #fff;" href="/xfsearch/year/2015">2015</a></li>
<li><a style="color: #fff;" href="/xfsearch/year/2014">2014</a></li>
<li><a style="color: #fff;" href="/xfsearch/year/2013">2013</a></li>
<li><a style="color: #fff;" href="/xfsearch/year/2012">2012</a></li>
<li><a style="color: #fff;" href="/xfsearch/year/2011">2011</a></li>
<li><a style="color: #fff;" href="/xfsearch/year/2010">2010</a></li>
<li><a style="color: #fff;" href="/xfsearch/year/2009">2009</a></li>
<li><a style="color: #fff;" href="/xfsearch/year/2008">2008</a></li>
<li><a style="color: #fff;" href="/xfsearch/year/2007">2007</a></li>
<li><a style="color: #fff;" href="/xfsearch/year/2006">2006</a></li>
<li><a style="color: #fff;" href="/xfsearch/year/2005">2005</a></li>
<li><a style="color: #fff;" href="/xfsearch/year/2004">2004</a></li>
<li><a style="color: #fff;" href="/xfsearch/year/2003">2003</a></li>
<li><a style="color: #fff;" href="/xfsearch/year/2002">2002</a></li>
<li><a style="color: #fff;" href="/xfsearch/year/2001">2001</a></li>
<li><a style="color: #fff;" href="/xfsearch/year/2000">2000</a></li>
'''  

    gamo=plugintools.find_multiple_matches(generos,'href="/(xfsearch/year/)(.*?)"') 
    for tema,year in gamo:
        tema=tema+year
        plugintools.add_item(action = "repelishd_pelis" , title = "[B][LOWERCASE][CAPITALIZE][COLOR white]repelishd [COLOR red] "+year+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail =thumbnail, fanart ='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTlQn_-m8utZCiPrhQe2P3pROEJITO1PDI2Hw&s', url= tema,extra='1',page=params.get("page", "{}"), folder = True )


    
def repelishd_generos(params):
    import xbmc, time
    thumbnail = params.get("thumbnail") 
    generos = '''									<li><a href="https://repelishd.cam/cine/">cine</a></li><li><a href="https://repelishd.cam/proximas-peliculas/">Próximas</a></li><li><a href="https://repelishd.cam/belica/">Bélica</a></li><li><a href="https://repelishd.cam/accion/">Acción</a></li><li><a href="https://repelishd.cam/suspenso/">Suspenso</a></li><li><a href="https://repelishd.cam/animacion/">Animación</a></li><li><a href="https://repelishd.cam/aventuras/">Aventuras</a></li><li><a href="https://repelishd.cam/biografia/">Biografia</a></li><li><a href="https://repelishd.cam/ciencia-ficcion/">ciencia ficcion</a></li><li><a href="https://repelishd.cam/comedia/">Comedia</a></li><li><a href="https://repelishd.cam/crimen/">Crimen</a></li><li><a href="https://repelishd.cam/documental/">Documental</a></li><li><a href="https://repelishd.cam/drama/">Drama</a></li><li><a href="https://repelishd.cam/familia/">Familia</a></li><li><a href="https://repelishd.cam/fantasia/">Fantasía</a></li><li><a href="https://repelishd.cam/guerra/">Guerra</a></li><li><a href="https://repelishd.cam/historicas/">Históricas</a></li><li><a href="https://repelishd.cam/intriga/">Intriga</a></li><li><a href="https://repelishd.cam/misterio/">Misterio</a></li><li><a href="https://repelishd.cam/musical/">Musical</a></li><li><a href="https://repelishd.cam/terror/">Terror</a></li><li><a href="https://repelishd.cam/thriller/">Thriller</a></li><li><a href="https://repelishd.cam/romance/">Romance</a></li><li><a href="https://repelishd.cam/reality/">Reality</a></li><li><a href="https://repelishd.cam/western/">Western</a></li><li><a href="https://repelishd.cam/series/">Series</a></li>'''  
    gamo=plugintools.find_multiple_matches(generos,'href="https://repelishd.cam/(.*?)/">(.*?)</a>') 
    for tema,titulo in gamo:
        plugintools.add_item(action = "repelishd_pelis" , title = "[B][LOWERCASE][CAPITALIZE][COLOR white]repelishd [COLOR red] "+titulo+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail =thumbnail, fanart ='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTlQn_-m8utZCiPrhQe2P3pROEJITO1PDI2Hw&s', url= tema,extra='1', folder = True )      

def repelishd_pelis(params):
    import xbmc, xbmcgui, requests, re, plugintools

    thumbnail = params.get("thumbnail") 
    tema = params.get("url")
    pagina = params.get("extra")

    try:
        # Obtener proxy y base URL
        cookies, url2base = obtener_proxy()
        if not cookies or not url2base:
            raise ValueError("No se pudo conectar con la base de la web,intentalo mas tarde")
            return
        
        # Construir URL
        url = f"{url2base}{tema}/page/{pagina}/?__cpo=aHR0cHM6Ly9yZXBlbGlzaGQuY2l0eQ"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
            "cookie": cookies
        }

        # Hacer request con timeout y manejo de errores
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        source1 = response.content
        if not source1:
            raise ValueError("No se obtuvo contenido de la web")

        # Decodificar contenido
        token = source1.decode('utf-8')

        # Patrón para películas y páginas
        pattern = r'<article class="item movies">.*?<img src=".([^"]+)" alt="([^"]+)">.*?<span class="quality">([^<]+)</span>.*?<a href="https://repelishd.city/([^"]+)">.*?<div class="audio">.*?<div class="[^"]+"></div>.*?</div>.*?<h3><a href="[^"]+">[^<]+</a></h3>\s*<span>(\d{4})</span>'
        paginas_pattern = r'(?s)<a href="https://repelishd.*?/page/(\d+)/(?!"><)'

        # Buscar coincidencias
        matches = re.findall(pattern, token, re.DOTALL)
        if not matches:
            xbmcgui.Dialog().ok("Aviso", "No se encontraron películas en esta página")
            return

        for foto, titulo, calidad, url_item, year in matches:
            foto_full = f"{url2base}{foto}?__cpo=aHR0cHM6Ly9yZXBlbGlzaGQuY2l0eQ|cookie={cookies}"
            url_full = f"{url2base}{url_item}"
            plugintools.add_item(
                action="repelishd_servers",
                extra=titulo,
                url=url_full,
                title=f"[B][COLOR white]{titulo} [COLOR yellow]{calidad}  [COLOR red]{year}[/COLOR][/B]",
                thumbnail=foto_full,
                fanart=foto_full,
                page=params.get("page", "{}"),
                folder=True
            )

        # Páginas
        urls = re.findall(paginas_pattern, token)
        for pag in urls:
            plugintools.add_item(
                action="repelishd_pelis",
                extra=pag,
                url=tema,
                title=f"[B][COLOR lime]ir a la pagina {pag}[/COLOR][/B]",
                thumbnail='',
                fanart='',
                folder=True
            )

    except Exception as e:
        xbmcgui.Dialog().ok("Error", f"{e}")
        return

def repelishd_servers(params):
    import xbmc, time
    trailer = params.get("extra")
    thumbnail = params.get("thumbnail")
    cookies, url2base = obtener_proxy()
    plugintools.add_item(action="trailer", url=trailer,title="[B][LOWERCASE][CAPITALIZE][COLOR orange]ver el trailer[/CAPITALIZE][/LOWERCASE][/COLOR][/B]",thumbnail=thumbnail,fanart=thumbnail,folder=True)
    url=params.get("url")+'?__cpo=aHR0cHM6Ly9yZXBlbGlzaGQuY2l0eQ'
    headers= {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36","cookie":cookies
}
    source=requests.get(url, headers=headers)
    status_code =source.status_code
    source1=source.content  # Esto ya es el contenido decodificado
            
    if source1:
        token = source1.decode('utf-8') 
        url=plugintools.find_single_match(token,'<iframe src="(.*?)"') 
        descripcion=plugintools.find_single_match(token,'</strong></div><p>(.*?)</p>')

        try:        
            source=requests.get(url, headers=headers, verify=False).content

            token = source.decode('utf-8')
            pattern = r'<ul class="_player-mirrors (\w+).*?">(.*?)</ul>'
            server_pattern = r'<li.*?data-link="([^"]+)".*?>\s*([^<\s]+)\s*</li>'
            matches = re.findall(pattern, token, re.DOTALL)
# Iterar por cada idioma y buscar servidores en su lista
            for idioma, content in matches:
                plugintools.add_item(action="", url='',title='[B][LOWERCASE][CAPITALIZE][COLOR yellow]Idioma: [COLOR red]'+idioma+'[/CAPITALIZE][/LOWERCASE][/COLOR][/B]',thumbnail=thumbnail,fanart=thumbnail,folder=False)
                servers = re.findall(server_pattern, content)
                for link, server in servers:
                    if 'http' in link:
                        pass
                    else:
                        link='https:'+link
  
                    plugintools.add_item(action="play_resolver", url=link,title='     [B][LOWERCASE][CAPITALIZE][COLOR aqua]Servidor: [COLOR lime]'+server+'[/CAPITALIZE][/LOWERCASE][/COLOR][/B]',plot='     [B][LOWERCASE][CAPITALIZE][COLOR orange]descripcion: [COLOR white]'+descripcion+'[/CAPITALIZE][/LOWERCASE][/COLOR][/B]',thumbnail=thumbnail,fanart=thumbnail,folder=False,  isPlayable = True)
        except:  
            plugintools.add_item(action="", url='',title='[B][LOWERCASE][CAPITALIZE][COLOR red]no disponible, buscala en otras secciones del addon[/CAPITALIZE][/LOWERCASE][/COLOR][/B]',thumbnail=thumbnail,fanart=thumbnail,folder=False)            
    else:
        xbmcgui.Dialog().ok("Error", "el proxy fallo intentalo de nuevo")
    xbmcplugin.setContent( int(sys.argv[1]) ,""+str(view_tipe)+"" )
    xbmc.executebuiltin("Container.SetViewMode("+str(view_codes)+")")
 









'''   
def generos(params):
    thumbnail = params.get("thumbnail")
    servidor = params.get("url")
    token = params.get("extra")
    #cambiar aqui ParentId=5 el id  de la seccion de cine 
    url=f'{servidor}emby/Genres?IncludeItemTypes=Movie&Fields=BasicSyncInfo%2CCanDelete%2CCanDownload%2CPrimaryImageAspectRatio&StartIndex=0&SortBy=SortName&SortOrder=Ascending&ParentId=5&EnableImageTypes=Primary%2CBackdrop%2CThumb&ImageTypeLimit=1&Recursive=true&Limit=50&userId=d8b34c7aaf3b49318a975e469d20fe86&X-Emby-Client=Emby+Web&X-Emby-Device-Name=Chrome+Windows&X-Emby-Device-Id=962cf0b0-0000-4594-8148-2d431985a3fc&X-Emby-Client-Version=4.9.1.90&X-Emby-Token={token}&X-Emby-Language=es'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0"}
    response = requests.get(url, headers=headers, verify=False)
    items = response.json().get('Items', [])
    for item in items:
        name = item.get('Name', '')
        item_id = item.get('Id', '')
                     
        primary_image_tag = item.get('ImageTags', {}).get('Primary', '')
        primary_image_url = f"{servidor}emby/Items/{item_id}/Images/Primary?maxHeight=563&maxWidth=375&tag={primary_image_tag}&keepAnimation=true&quality=90"
        
   
        url = f"{servidor}emby/Users/d8b34c7aaf3b49318a975e469d20fe86/Items?IncludeItemTypes=Movie%2CSeries%2CVideo%2CGame%2CMusicAlbum&Fields=BasicSyncInfo%2CCanDelete%2CCanDownload%2CPrimaryImageAspectRatio%2CProductionYear%2CStatus%2CEndDate&StartIndex=0&SortBy=ProductionYear%2CSortName&SortOrder=Descending&ParentId=5&EnableImageTypes=Primary%2CBackdrop%2CThumb&ImageTypeLimit=1&GenreIds={item_id}&Recursive=true&Limit=50&X-Emby-Client=Emby+Web&X-Emby-Device-Name=Chrome+Windows&X-Emby-Device-Id=962cf0b0-0000-4594-8148-2d431985a3fc&X-Emby-Client-Version=4.9.1.90&X-Emby-Token={token}&X-Emby-Language=es"
        
        plugintools.add_item(action="emby2",thumbnail=primary_image_url,fanart=primary_image_url,extra='Movie',url=',title=f"[B][LOWERCASE][CAPITALIZE][COLOR white]{name}[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",page=servidor,plot=token,folder=True)
       
'''   
    
def nuevomenu(params):
    servidor = params.get("url")
    token = params.get("extra")
    url = construct_url(servidor, token)
    headers = get_headers()
    items = fetch_emby_items(url, headers)
    process_items_nuevo(items, servidor, token)


def nuevomenu2(params):
    servidor="http://alpu.dnsfor.me:8092/"
    token = '54347348ddb9408a95be1a16e114955f' 
    url = construct_url(servidor, token)
    headers = get_headers()
    items = fetch_emby_items(url, headers)
    process_items_nuevo(items, servidor, token)
 
def nuevomenu3(params):
    servidor="http://151.80.18.63:8096/"
    token = '410c58b35d6e43e9bbff9727f4a5ed69' 
    url = construct_url(servidor, token)
    headers = get_headers()
    items = fetch_emby_items(url, headers)
    process_items_nuevo(items, servidor, token)   
 
def process_items_nuevo(items, servidor, token):
    """
    Procesa los ítems obtenidos de la API y los agrega al plugin.
    """
  
    for item in items:
        name = item.get('Name')
        collection_type = str(item.get('CollectionType')).replace('movies', 'Movie').replace('tvshows', 'series')
        id = item.get('Id')
        primary_image = item.get('ImageTags')
        primary_image_url = f"{servidor}emby/Items/{id}/Images/Primary?maxHeight=563&maxWidth=375&tag={primary_image.get('Primary')}&keepAnimation=true&quality=90"

        url = f"{servidor}emby/Users/157469d30e4e4af49963b6183a384813/Items?IncludeItemTypes={collection_type}&Fields=BasicSyncInfo%2CCanDelete%2CPrimaryImageAspectRatio%2CProductionYear%2CStatus%2CEndDate&StartIndex=0&SortBy=DateCreated%2CSortName&SortOrder=Descending&ParentId={id}&EnableImageTypes=Primary%2CBackdrop%2CThumb&ImageTypeLimit=1&Recursive=true&Limit=20000&X-Emby-Client=Emby+Web&X-Emby-Device-Name=Google+Chrome+Windows&X-Emby-Device-Id=53415749-fefb-4915-91a3-c664efc8277b&X-Emby-Client-Version=4.8.10.2&X-Emby-Token={token}&X-Emby-Language=es"

        if 'Lista de' not in name and 'Colecciones' not in name and 'Audiolibros' not in name:
            if 'TV' == name:
                name = 'programas de la tele'
            xbmc.executebuiltin("Container.SetViewMode(50)")

            url_lo_nuevo = f"{servidor}emby/Users/157469d30e4e4af49963b6183a384813/Items/Latest?ParentId={id}&Fields=BasicSyncInfo%2CCanDelete%2CCanDownload%2CPrimaryImageAspectRatio%2CProgramPrimaryImageAspectRatio%2CProductionYear&ImageTypeLimit=1&EnableImageTypes=Primary%2CBackdrop%2CThumb&Limit=12&X-Emby-Client=Emby+Web&X-Emby-Device-Name=Chrome+Windows&X-Emby-Device-Id=53415749-fefb-4915-91a3-c664efc8277b&X-Emby-Client-Version=4.9.1.90&X-Emby-Token={token}&X-Emby-Language=es"

   
            plugintools.add_item(
                action="",
                thumbnail=primary_image_url,
                fanart=primary_image_url,
                title=f" [B][LOWERCASE][CAPITALIZE][COLOR orange]******* [COLOR yellow]lo nuevo en {name} [COLOR orange]*******[/CAPITALIZE][/LOWERCASE][/B][/COLOR]\n",
                folder=False
            )

            response = requests.get(url_lo_nuevo, headers=headers, verify=False)
            lonuevo = response.json()

        
            for item in lonuevo:
                name1 = item.get('Name', '')
                id = item.get('Id', '')
                Type = item.get('Type', '')
                CollectionType = Type.replace('movies', 'Movie').replace('tvshows', 'serie').replace('Series', 'serie')
                primary_image = item.get('ImageTags')
                primary_image_url = f"{servidor}emby/Items/{id}/Images/Primary?maxHeight=563&maxWidth=375&tag={primary_image.get('Primary')}&keepAnimation=true&quality=90"
                if 'serie' in CollectionType:
                    plugintools.add_item(action="emby_series",thumbnail=primary_image_url,fanart=primary_image_url,extra=token,page=servidor,url=id,title=f"[B][LOWERCASE][CAPITALIZE][COLOR white]       {name1} [/CAPITALIZE][/LOWERCASE][/B][/COLOR]",folder=True)
        
                else:
                    plugintools.add_item(action="emby3",thumbnail=primary_image_url,fanart=primary_image_url,extra=name,url=id,plot=token,page=servidor,title=f"[B][LOWERCASE][CAPITALIZE][COLOR white]       {name1} [/CAPITALIZE][/LOWERCASE][/B][/COLOR]",folder=True)



def construct_url(servidor, token):
    """
    Construye la URL para la API de Emby usando el servidor y el token.
    """
    return f"{servidor}emby/Users/b2395e931d1d4266b6fb0e5944bf05b4/Views?X-Emby-Client=Emby+Web&X-Emby-Device-Name=Chrome+Windows&X-Emby-Device-Id=1dbf3ed8-c2b4-4c2a-936d-0592eefa52c6&X-Emby-Client-Version=4.9.0.34&X-Emby-Token={token}&X-Emby-Language=es"

def get_headers():
    """
    Retorna los encabezados necesarios para la solicitud HTTP.
    """
    return {
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "accept": "application/json",
        "Content-Type": "text/plain",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "es-ES,es;q=0.9"
    }

def fetch_emby_items(url, headers):
    """
    Realiza la solicitud a Emby y obtiene los ítems.
    """
    response = requests.get(url, headers=headers, verify=False)
    return response.json().get('Items', [])

def process_items(items, servidor, token):
    """
    Procesa los ítems obtenidos de la API y los agrega al plugin.
    """
    for item in items:
        name = item.get('Name')
        collection_type = str(item.get('CollectionType')).replace('movies', 'Movie').replace('tvshows', 'series')
        id = item.get('Id')
        primary_image = item.get('ImageTags')
        primary_image_url = f"{servidor}emby/Items/{id}/Images/Primary?maxHeight=563&maxWidth=375&tag={primary_image.get('Primary')}&keepAnimation=true&quality=90"

        url = f"{servidor}emby/Users/157469d30e4e4af49963b6183a384813/Items?IncludeItemTypes={collection_type}&Fields=BasicSyncInfo%2CCanDelete%2CPrimaryImageAspectRatio%2CProductionYear%2CStatus%2CEndDate&StartIndex=0&SortBy=DateCreated%2CSortName&SortOrder=Descending&ParentId={id}&EnableImageTypes=Primary%2CBackdrop%2CThumb&ImageTypeLimit=1&Recursive=true&Limit=20000&X-Emby-Client=Emby+Web&X-Emby-Device-Name=Google+Chrome+Windows&X-Emby-Device-Id=53415749-fefb-4915-91a3-c664efc8277b&X-Emby-Client-Version=4.8.10.2&X-Emby-Token={token}&X-Emby-Language=es"
        if 'Lista de' not in name and 'Colecciones' not in name and 'PELIS 3D' not in name and 'Audiolibros' not in name:
            if 'TV' == name:
                name= 'programas de la tele'
            plugintools.add_item(action="emby2",thumbnail=primary_image_url,fanart=primary_image_url,extra=collection_type,url=url,title=f"[B][LOWERCASE][CAPITALIZE][COLOR white]{name}[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",page=servidor,plot=token,folder=True)


    
import xbmc
import time
import requests
import re

def emby2(params):

    thumbnail = params.get("thumbnail")
    url = params.get("url")
    servidor = params.get("page")
    token = params.get("plot")
    CollectionType = params.get("extra")
 
    

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0"
    }
    

    response = requests.get(url, headers=headers, verify=False)
    items = response.json().get('Items', [])

    for item in items:
        name = item.get('Name', '')
        item_id = item.get('Id', '')
        production_year = item.get('ProductionYear', '')
        
   
        production_year = '' if 'None' in str(production_year) else production_year
        
  
        primary_image_tag = item.get('ImageTags', {}).get('Primary', '')
        primary_image_url = f"{servidor}emby/Items/{item_id}/Images/Primary?maxHeight=563&maxWidth=375&tag={primary_image_tag}&keepAnimation=true&quality=90"
        

        if 'serie' in CollectionType:
            plugintools.add_item(
                action="emby_series",
                thumbnail=primary_image_url,
                fanart=primary_image_url,
                extra=token,
                page=servidor,
                url=item_id,
                title=f"[B][LOWERCASE][CAPITALIZE][COLOR white]{name} [COLOR gold]{production_year}[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",
                folder=True
            )
       
        else:
            plugintools.add_item(
                action="emby3",
                thumbnail=primary_image_url,
                fanart=primary_image_url,
                extra=name,
                url=item_id,
                plot=token,
                page=servidor,
                title=f"[B][LOWERCASE][CAPITALIZE][COLOR white]{name} [COLOR gold]{production_year}[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",
                folder=True
            )
    


def emby_series(params):
    import xbmc, time
    thumbnail = params.get("thumbnail") 
    Shows = params.get("url")
    token = params.get("extra") 
    servidor = params.get("page")
    url=servidor+'emby/Shows/'+Shows+'/Seasons?UserId=157469d30e4e4af49963b6183a384813&Fields=BasicSyncInfo%2CCanDelete%2CPrimaryImageAspectRatio%2COverview&EnableUserData=false&EnableTotalRecordCount=false&EnableImages=false&X-Emby-Client=Emby+Web&X-Emby-Device-Name=Google+Chrome+Windows&X-Emby-Device-Id=52205847-fefb-4985-99a3-c664efc80277b&X-Emby-Client-Version=4.8.10.2&X-Emby-Token='+token+'&X-Emby-Language=es' 
    headers= {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0"}
    import requests,re
    x=requests.get(url, headers=headers, verify=False).json()
    Items = x.get('Items')
    for item in Items:
        Name=item.get('Name')
        Id=item.get('Id')

        plugintools.add_item(action="emby_series2",thumbnail =thumbnail, fanart = thumbnail,extra=Shows,plot=token,page=servidor, url=Id,title="[B][LOWERCASE][CAPITALIZE][COLOR white]"+Name+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",folder=True)

def emby_series2(params):
    import xbmc, time
    thumbnail = params.get("thumbnail") 
    Id = params.get("url")
    Shows = params.get("extra")
    token = params.get("plot") 
    servidor = params.get("page")
    url=servidor+'emby/Shows/'+Shows+'/Episodes?SeasonId='+Id+'&ImageTypeLimit=1&UserId=157469d30e4e4af49963b6183a384813&Fields=Overview%2CPrimaryImageAspectRatio%2CPremiereDate%2CProductionYear%2CSyncStatus&Limit=2000&X-Emby-Client=Emby+Web&X-Emby-Device-Name=Google+Chrome+Windows&X-Emby-Device-Id=541176309-fefb-4915-91a3-c664efc8277b&X-Emby-Client-Version=4.8.10.2&X-Emby-Token='+token+'&X-Emby-Language=es' 
    headers= {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0"}
    import requests,re
    x=requests.get(url, headers=headers, verify=False).json()
    Items = x.get('Items')
    for item in Items:
        Name=item.get('Name')
        Id=item.get('Id')
        try:
            Overview=item.get('Overview')
        except:
            Overview=''
        IndexNumber=item.get('IndexNumber')
        plugintools.add_item(action="embyseriesfin",thumbnail =thumbnail, fanart = thumbnail,extra=str(token), url=str(Id),title="[B][LOWERCASE][CAPITALIZE][COLOR gold]"+str(IndexNumber)+" [COLOR white]"+str(Name)+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",plot="[B][LOWERCASE][CAPITALIZE][COLOR orange]"+str(Overview)+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",page=servidor,folder=False,  isPlayable= True)
    xbmcplugin.setContent( int(sys.argv[1]) ,""+str(view_tipe)+"" )
    xbmc.executebuiltin("Container.SetViewMode("+str(view_codes)+")")
def embyseriesfin(params):
    import xbmc, time
    thumbnail = params.get("thumbnail") 
    Id = params.get("url")
    token = params.get("extra") 
    servidor = params.get("page")
    
    url=servidor+'emby/Items/'+Id+'/PlaybackInfo?UserId=157469d30e4e4af49963b6183a384813&StartTimeTicks=0&IsPlayback=false&AutoOpenLiveStream=false&MaxStreamingBitrate=60000000&X-Emby-Client=Emby+Web&X-Emby-Device-Name=Google+Chrome+Windows&X-Emby-Device-Id=54105845-fefb-4798-12a3-c663efc8277b&X-Emby-Client-Version=4.8.10.2&X-Emby-Token='+token+'&X-Emby-Language=es&reqformat=json' 
    headers= {"Connection":"keep-alive","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36","accept":"application/json","Content-Type":"text/plain","Accept-Encoding":"gzip, deflate","Accept-Language":"es-ES,es;q=0.9"}
    import requests,re
    true='true'
    false='false'
    payload="{\"DeviceProfile\":{\"MaxStaticBitrate\":140000000,\"MaxStreamingBitrate\":140000000,\"MusicStreamingTranscodingBitrate\":192000,\"DirectPlayProfiles\":[{\"Container\":\"mp4,m4v\",\"Type\":\"Video\",\"VideoCodec\":\"h264,h265,hevc,av1,vp8,vp9\",\"AudioCodec\":\"mp3,aac,opus,flac,vorbis\"},{\"Container\":\"mkv\",\"Type\":\"Video\",\"VideoCodec\":\"h264,h265,hevc,av1,vp8,vp9\",\"AudioCodec\":\"mp3,aac,opus,flac,vorbis\"},{\"Container\":\"flv\",\"Type\":\"Video\",\"VideoCodec\":\"h264\",\"AudioCodec\":\"aac,mp3\"},{\"Container\":\"3gp\",\"Type\":\"Video\",\"VideoCodec\":\"\",\"AudioCodec\":\"mp3,aac,opus,flac,vorbis\"},{\"Container\":\"mov\",\"Type\":\"Video\",\"VideoCodec\":\"h264\",\"AudioCodec\":\"mp3,aac,opus,flac,vorbis\"},{\"Container\":\"opus\",\"Type\":\"Audio\"},{\"Container\":\"mp3\",\"Type\":\"Audio\",\"AudioCodec\":\"mp3\"},{\"Container\":\"mp2,mp3\",\"Type\":\"Audio\",\"AudioCodec\":\"mp2\"},{\"Container\":\"aac\",\"Type\":\"Audio\",\"AudioCodec\":\"aac\"},{\"Container\":\"m4a\",\"AudioCodec\":\"aac\",\"Type\":\"Audio\"},{\"Container\":\"mp4\",\"AudioCodec\":\"aac\",\"Type\":\"Audio\"},{\"Container\":\"flac\",\"Type\":\"Audio\"},{\"Container\":\"webma,webm\",\"Type\":\"Audio\"},{\"Container\":\"wav\",\"Type\":\"Audio\",\"AudioCodec\":\"PCM_S16LE,PCM_S24LE\"},{\"Container\":\"ogg\",\"Type\":\"Audio\"},{\"Container\":\"webm\",\"Type\":\"Video\",\"AudioCodec\":\"vorbis,opus\",\"VideoCodec\":\"av1,VP8,VP9\"}],\"TranscodingProfiles\":[{\"Container\":\"aac\",\"Type\":\"Audio\",\"AudioCodec\":\"aac\",\"Context\":\"Streaming\",\"Protocol\":\"hls\",\"MaxAudioChannels\":\"2\",\"MinSegments\":\"1\",\"BreakOnNonKeyFrames\":true},{\"Container\":\"aac\",\"Type\":\"Audio\",\"AudioCodec\":\"aac\",\"Context\":\"Streaming\",\"Protocol\":\"http\",\"MaxAudioChannels\":\"2\"},{\"Container\":\"mp3\",\"Type\":\"Audio\",\"AudioCodec\":\"mp3\",\"Context\":\"Streaming\",\"Protocol\":\"http\",\"MaxAudioChannels\":\"2\"},{\"Container\":\"opus\",\"Type\":\"Audio\",\"AudioCodec\":\"opus\",\"Context\":\"Streaming\",\"Protocol\":\"http\",\"MaxAudioChannels\":\"2\"},{\"Container\":\"wav\",\"Type\":\"Audio\",\"AudioCodec\":\"wav\",\"Context\":\"Streaming\",\"Protocol\":\"http\",\"MaxAudioChannels\":\"2\"},{\"Container\":\"opus\",\"Type\":\"Audio\",\"AudioCodec\":\"opus\",\"Context\":\"Static\",\"Protocol\":\"http\",\"MaxAudioChannels\":\"2\"},{\"Container\":\"mp3\",\"Type\":\"Audio\",\"AudioCodec\":\"mp3\",\"Context\":\"Static\",\"Protocol\":\"http\",\"MaxAudioChannels\":\"2\"},{\"Container\":\"aac\",\"Type\":\"Audio\",\"AudioCodec\":\"aac\",\"Context\":\"Static\",\"Protocol\":\"http\",\"MaxAudioChannels\":\"2\"},{\"Container\":\"wav\",\"Type\":\"Audio\",\"AudioCodec\":\"wav\",\"Context\":\"Static\",\"Protocol\":\"http\",\"MaxAudioChannels\":\"2\"},{\"Container\":\"mkv\",\"Type\":\"Video\",\"AudioCodec\":\"mp3,aac,opus,flac,vorbis\",\"VideoCodec\":\"h264,h265,hevc,av1,vp8,vp9\",\"Context\":\"Static\",\"MaxAudioChannels\":\"2\",\"CopyTimestamps\":true},{\"Container\":\"ts\",\"Type\":\"Video\",\"AudioCodec\":\"mp3,aac\",\"VideoCodec\":\"h264,h265,hevc,av1\",\"Context\":\"Streaming\",\"Protocol\":\"hls\",\"MaxAudioChannels\":\"2\",\"MinSegments\":\"1\",\"BreakOnNonKeyFrames\":true,\"ManifestSubtitles\":\"vtt\"},{\"Container\":\"webm\",\"Type\":\"Video\",\"AudioCodec\":\"vorbis\",\"VideoCodec\":\"vpx\",\"Context\":\"Streaming\",\"Protocol\":\"http\",\"MaxAudioChannels\":\"2\"},{\"Container\":\"mp4\",\"Type\":\"Video\",\"AudioCodec\":\"mp3,aac,opus,flac,vorbis\",\"VideoCodec\":\"h264\",\"Context\":\"Static\",\"Protocol\":\"http\"}],\"ContainerProfiles\":[],\"CodecProfiles\":[{\"Type\":\"VideoAudio\",\"Codec\":\"aac\",\"Conditions\":[{\"Condition\":\"Equals\",\"Property\":\"IsSecondaryAudio\",\"Value\":\"false\",\"IsRequired\":\"false\"}]},{\"Type\":\"VideoAudio\",\"Conditions\":[{\"Condition\":\"Equals\",\"Property\":\"IsSecondaryAudio\",\"Value\":\"false\",\"IsRequired\":\"false\"}]},{\"Type\":\"Video\",\"Codec\":\"h264\",\"Conditions\":[{\"Condition\":\"EqualsAny\",\"Property\":\"VideoProfile\",\"Value\":\"high|main|baseline|constrained baseline|high 10\",\"IsRequired\":false},{\"Condition\":\"LessThanEqual\",\"Property\":\"VideoLevel\",\"Value\":\"62\",\"IsRequired\":false},{\"Condition\":\"LessThanEqual\",\"Property\":\"Width\",\"Value\":\"1920\",\"IsRequired\":false}]},{\"Type\":\"Video\",\"Codec\":\"hevc\",\"Conditions\":[{\"Condition\":\"EqualsAny\",\"Property\":\"VideoCodecTag\",\"Value\":\"hvc1|hev1|hevc|hdmv\",\"IsRequired\":false},{\"Condition\":\"LessThanEqual\",\"Property\":\"Width\",\"Value\":\"1920\",\"IsRequired\":false}]},{\"Type\":\"Video\",\"Conditions\":[{\"Condition\":\"LessThanEqual\",\"Property\":\"Width\",\"Value\":\"1920\",\"IsRequired\":false}]}],\"SubtitleProfiles\":[{\"Format\":\"vtt\",\"Method\":\"Hls\"},{\"Format\":\"eia_608\",\"Method\":\"VideoSideData\",\"Protocol\":\"hls\"},{\"Format\":\"eia_708\",\"Method\":\"VideoSideData\",\"Protocol\":\"hls\"},{\"Format\":\"vtt\",\"Method\":\"External\"},{\"Format\":\"ass\",\"Method\":\"External\"},{\"Format\":\"ssa\",\"Method\":\"External\"}],\"ResponseProfiles\":[{\"Type\":\"Video\",\"Container\":\"m4v\",\"MimeType\":\"video/mp4\"}]}}"
    x=requests.post(url, headers=headers,data=payload).text
    patron = plugintools.find_single_match(x,'DirectStreamUrl":"(.*?)".*?')
    url=patron.replace('stream?','master.m3u8?')
    url = servidor+'emby'+url
    plugintools.play_resolved_url( url )     
def emby3(params):
    import xbmc, time,requests
    thumbnail = params.get("thumbnail") 
    Id = params.get("url")
    token = params.get("plot") 
    servidor = params.get("page")
    trailer = params.get("extra")
    plugintools.add_item(action="trailer", url=trailer,title="[B][LOWERCASE][CAPITALIZE][COLOR orange]ver el trailer[/CAPITALIZE][/LOWERCASE][/COLOR][/B]",thumbnail=thumbnail,fanart=thumbnail,folder=True)
    url=servidor+'emby/Items/'+Id+'/PlaybackInfo?UserId=b2395e931d1d4266b6fb0e5944bf05b4&StartTimeTicks=0&IsPlayback=false&AutoOpenLiveStream=false&MaxStreamingBitrate=7000000&X-Emby-Client=Emby+Web&X-Emby-Device-Name=Chrome+Windows&X-Emby-Device-Id=1dbf2ed7-c2b2-4c7a-926d-0192eefa52c6&X-Emby-Client-Version=4.9.0.34&X-Emby-Token='+token+'&X-Emby-Language=es&reqformat=json'
    headers= {"Connection":"keep-alive","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36","accept":"application/json","Content-Type":"text/plain","Accept-Encoding":"gzip, deflate","Accept-Language":"es-ES,es;q=0.9"}
    url_info=servidor+'emby/Users/157469d30e4e4af49963b6183a384813/Items/'+Id+'?fields=ShareLevel&ExcludeFields=VideoChapters%2CVideoMediaSources%2CMediaStreams&X-Emby-Client=Emby+Web&X-Emby-Device-Name=Google+Chrome+Windows&X-Emby-Device-Id=53145546-fefb-4915-91a3-c664efc8277b&X-Emby-Client-Version=4.8.10.2&X-Emby-Token='+token+'&X-Emby-Language=es'
    x=requests.get(url_info, headers=headers, verify=False).text
    texto = plugintools.find_single_match(x,'Overview":"(.*?)".*?')
    payload="{\"DeviceProfile\":{\"MaxStaticBitrate\":140000000,\"MaxStreamingBitrate\":140000000,\"MusicStreamingTranscodingBitrate\":192000,\"DirectPlayProfiles\":[{\"Container\":\"mp4,m4v\",\"Type\":\"Video\",\"VideoCodec\":\"h264,h265,hevc,av1,vp8,vp9\",\"AudioCodec\":\"mp3,aac,opus,flac,vorbis\"},{\"Container\":\"mkv\",\"Type\":\"Video\",\"VideoCodec\":\"h264,h265,hevc,av1,vp8,vp9\",\"AudioCodec\":\"mp3,aac,opus,flac,vorbis\"},{\"Container\":\"flv\",\"Type\":\"Video\",\"VideoCodec\":\"h264\",\"AudioCodec\":\"aac,mp3\"},{\"Container\":\"3gp\",\"Type\":\"Video\",\"VideoCodec\":\"\",\"AudioCodec\":\"mp3,aac,opus,flac,vorbis\"},{\"Container\":\"mov\",\"Type\":\"Video\",\"VideoCodec\":\"h264\",\"AudioCodec\":\"mp3,aac,opus,flac,vorbis\"},{\"Container\":\"opus\",\"Type\":\"Audio\"},{\"Container\":\"mp3\",\"Type\":\"Audio\",\"AudioCodec\":\"mp3\"},{\"Container\":\"mp2,mp3\",\"Type\":\"Audio\",\"AudioCodec\":\"mp2\"},{\"Container\":\"aac\",\"Type\":\"Audio\",\"AudioCodec\":\"aac\"},{\"Container\":\"m4a\",\"AudioCodec\":\"aac\",\"Type\":\"Audio\"},{\"Container\":\"mp4\",\"AudioCodec\":\"aac\",\"Type\":\"Audio\"},{\"Container\":\"flac\",\"Type\":\"Audio\"},{\"Container\":\"webma,webm\",\"Type\":\"Audio\"},{\"Container\":\"wav\",\"Type\":\"Audio\",\"AudioCodec\":\"PCM_S16LE,PCM_S24LE\"},{\"Container\":\"ogg\",\"Type\":\"Audio\"},{\"Container\":\"webm\",\"Type\":\"Video\",\"AudioCodec\":\"vorbis,opus\",\"VideoCodec\":\"av1,VP8,VP9\"}],\"TranscodingProfiles\":[{\"Container\":\"aac\",\"Type\":\"Audio\",\"AudioCodec\":\"aac\",\"Context\":\"Streaming\",\"Protocol\":\"hls\",\"MaxAudioChannels\":\"2\",\"MinSegments\":\"1\",\"BreakOnNonKeyFrames\":true},{\"Container\":\"aac\",\"Type\":\"Audio\",\"AudioCodec\":\"aac\",\"Context\":\"Streaming\",\"Protocol\":\"http\",\"MaxAudioChannels\":\"2\"},{\"Container\":\"mp3\",\"Type\":\"Audio\",\"AudioCodec\":\"mp3\",\"Context\":\"Streaming\",\"Protocol\":\"http\",\"MaxAudioChannels\":\"2\"},{\"Container\":\"opus\",\"Type\":\"Audio\",\"AudioCodec\":\"opus\",\"Context\":\"Streaming\",\"Protocol\":\"http\",\"MaxAudioChannels\":\"2\"},{\"Container\":\"wav\",\"Type\":\"Audio\",\"AudioCodec\":\"wav\",\"Context\":\"Streaming\",\"Protocol\":\"http\",\"MaxAudioChannels\":\"2\"},{\"Container\":\"opus\",\"Type\":\"Audio\",\"AudioCodec\":\"opus\",\"Context\":\"Static\",\"Protocol\":\"http\",\"MaxAudioChannels\":\"2\"},{\"Container\":\"mp3\",\"Type\":\"Audio\",\"AudioCodec\":\"mp3\",\"Context\":\"Static\",\"Protocol\":\"http\",\"MaxAudioChannels\":\"2\"},{\"Container\":\"aac\",\"Type\":\"Audio\",\"AudioCodec\":\"aac\",\"Context\":\"Static\",\"Protocol\":\"http\",\"MaxAudioChannels\":\"2\"},{\"Container\":\"wav\",\"Type\":\"Audio\",\"AudioCodec\":\"wav\",\"Context\":\"Static\",\"Protocol\":\"http\",\"MaxAudioChannels\":\"2\"},{\"Container\":\"mkv\",\"Type\":\"Video\",\"AudioCodec\":\"mp3,aac,opus,flac,vorbis\",\"VideoCodec\":\"h264,h265,hevc,av1,vp8,vp9\",\"Context\":\"Static\",\"MaxAudioChannels\":\"2\",\"CopyTimestamps\":true},{\"Container\":\"ts\",\"Type\":\"Video\",\"AudioCodec\":\"mp3,aac\",\"VideoCodec\":\"h264,h265,hevc,av1\",\"Context\":\"Streaming\",\"Protocol\":\"hls\",\"MaxAudioChannels\":\"2\",\"MinSegments\":\"1\",\"BreakOnNonKeyFrames\":true,\"ManifestSubtitles\":\"vtt\"},{\"Container\":\"webm\",\"Type\":\"Video\",\"AudioCodec\":\"vorbis\",\"VideoCodec\":\"vpx\",\"Context\":\"Streaming\",\"Protocol\":\"http\",\"MaxAudioChannels\":\"2\"},{\"Container\":\"mp4\",\"Type\":\"Video\",\"AudioCodec\":\"mp3,aac,opus,flac,vorbis\",\"VideoCodec\":\"h264\",\"Context\":\"Static\",\"Protocol\":\"http\"}],\"ContainerProfiles\":[],\"CodecProfiles\":[{\"Type\":\"VideoAudio\",\"Codec\":\"aac\",\"Conditions\":[{\"Condition\":\"Equals\",\"Property\":\"IsSecondaryAudio\",\"Value\":\"false\",\"IsRequired\":\"false\"}]},{\"Type\":\"VideoAudio\",\"Conditions\":[{\"Condition\":\"Equals\",\"Property\":\"IsSecondaryAudio\",\"Value\":\"false\",\"IsRequired\":\"false\"}]},{\"Type\":\"Video\",\"Codec\":\"h264\",\"Conditions\":[{\"Condition\":\"EqualsAny\",\"Property\":\"VideoProfile\",\"Value\":\"high|main|baseline|constrained baseline|high 10\",\"IsRequired\":false},{\"Condition\":\"LessThanEqual\",\"Property\":\"VideoLevel\",\"Value\":\"62\",\"IsRequired\":false},{\"Condition\":\"LessThanEqual\",\"Property\":\"Width\",\"Value\":\"1920\",\"IsRequired\":false}]},{\"Type\":\"Video\",\"Codec\":\"hevc\",\"Conditions\":[{\"Condition\":\"EqualsAny\",\"Property\":\"VideoCodecTag\",\"Value\":\"hvc1|hev1|hevc|hdmv\",\"IsRequired\":false},{\"Condition\":\"LessThanEqual\",\"Property\":\"Width\",\"Value\":\"1920\",\"IsRequired\":false}]},{\"Type\":\"Video\",\"Conditions\":[{\"Condition\":\"LessThanEqual\",\"Property\":\"Width\",\"Value\":\"1920\",\"IsRequired\":false}]}],\"SubtitleProfiles\":[{\"Format\":\"vtt\",\"Method\":\"Hls\"},{\"Format\":\"eia_608\",\"Method\":\"VideoSideData\",\"Protocol\":\"hls\"},{\"Format\":\"eia_708\",\"Method\":\"VideoSideData\",\"Protocol\":\"hls\"},{\"Format\":\"vtt\",\"Method\":\"External\"},{\"Format\":\"ass\",\"Method\":\"External\"},{\"Format\":\"ssa\",\"Method\":\"External\"}],\"ResponseProfiles\":[{\"Type\":\"Video\",\"Container\":\"m4v\",\"MimeType\":\"video/mp4\"}]}}"
    x=requests.post(url, headers=headers,data=payload).text
    patron = plugintools.find_single_match(x,'DirectStreamUrl":"(.*?)".*?')
    url=patron.replace('stream?','master.m3u8?')
    url = servidor+'emby'+url
    plugintools.add_item(action="play_links",url=url,title ="[B][LOWERCASE][CAPITALIZE][COLOR gold]REPRODUCIR [/CAPITALIZE][/LOWERCASE][/B][/COLOR]",plot = "[B][LOWERCASE][CAPITALIZE][COLOR orange]"+texto+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",thumbnail=thumbnail,fanart=thumbnail,folder=False,  isPlayable= True) 
    xbmcplugin.setContent( int(sys.argv[1]) ,""+str(view_tipe)+"" )
    xbmc.executebuiltin("Container.SetViewMode("+str(view_codes)+")")


        




import difflib



def trailer(params):  

    
    thumbnail = params.get("thumbnail")
    trailer = params.get("url").replace(" ", "+").replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u").replace("¡", "").replace("!", "").replace("¿", "").replace("?", "").replace("ñ", "%C3%B1o")
    
    url = 'https://www.youtube.com/results?search_query='+trailer+'+trailer+español' 
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:144.0) Gecko/20100101 Firefox/144.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1"
    }

    source = requests.get(url, headers=headers, verify=False).text

    gamo=plugintools.find_multiple_matches(source,'videoRenderer":{"videoId":".*?".*?{"url":".*?".*?"text":".*?"')    
    for generos in gamo:
        patron=plugintools.find_single_match(generos,'videoRenderer":{"videoId":"(.*?)".*?{"url":"(.*?)".*?"text":"(.*?)"')  
        movies=patron[0]
        titulo=patron[2]
        foto= patron[1]
        url='plugin://plugin.video.youtube/play/?video_id='+movies
        plugintools.add_item(action="play_links", url=url,title="[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo+"[/CAPITALIZE][/LOWERCASE][/COLOR][/B]",thumbnail=foto,fanart=thumbnail,folder=False,  isPlayable = True)              






    
 
def play_links(params): 
    try:  
        url =params.get("url")+'&verifypeer=false'
        plugintools.play_resolved_url( url ) 
 
    except: 
        u= xbmc.executebuiltin('XBMC.Notification([B][LOWERCASE][CAPITALIZE][COLOR white]enlace  [COLOR red]borrado [/CAPITALIZE][/LOWERCASE][/B][/COLOR],[B][LOWERCASE][CAPITALIZE][COLOR white]elige otro [/CAPITALIZE][/LOWERCASE][/B][/COLOR], 2000)')
        plugintools.add_item(action = "" ,title = u, thumbnail ='',url='', fanart = '', folder=False,  isPlayable = True )

def play_resolver(params):
    import resolveurl 
    url=params.get("url")
    try:
        video = resolveurl.resolve(url) 
        plugintools.play_resolved_url( video )

    except:
        import xbmcgui,xbmc
        dp = xbmcgui.DialogProgress()
        dp.create('[CAPITALIZE][COLOR yellow]parece que el enlace esta borrado[/COLOR][/CAPITALIZE]')
        xbmc.sleep(2000)
        dp.update(100,'[CAPITALIZE][COLOR lime]ELIGE OTRO SERVER\nESTE ENLACE ESTA BORRADO[/COLOR][/CAPITALIZE]') 
        xbmc.sleep(2000)
        dp.close() 




run()

