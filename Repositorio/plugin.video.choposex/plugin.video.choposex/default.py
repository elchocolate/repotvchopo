# -*- coding: utf-8 -*-
#------------------------------------------------------------
# chopodplay - XBMC Add-on by Torete
# Version 0.2.5 (15.05.2014)
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Gracias a la librerÔö£┬ía plugintools de JesÔö£Ôòæs (www.mimediacenter.info)
import os
import sys
 
try:
    import urllib.request, urllib.parse, urllib.error
    import urllib.request, urllib.error, urllib.parse
    from urllib.parse import urlparse, urlencode
    from urllib.request import urlopen, Request
    from urllib.error import HTTPError
except ImportError:
    import urllib2
    from urlparse import urlparse
    from urllib import urlencode
    from urllib2 import urlopen, Request, HTTPError
import re
import xbmc
import xbmcvfs
import xbmcgui
import xbmcaddon
import xbmcplugin
import plugintools
import unicodedata
import base64
import requests
import shutil
import base64
import time
import random
import six
import resolveurl
try:
    from resolveurl.plugins.lib import jsunpack
except:
    from resolveurl.lib import jsunpack
if six.PY3:
    unicode = str
addon = xbmcaddon.Addon()
addonname = '[B][LOWERCASE][CAPITALIZE][COLOR white]choposex[/CAPITALIZE][/LOWERCASE][/B][/COLOR]'
icon = addon.getAddonInfo('icon')
myaddon = xbmcaddon.Addon("plugin.video.choposex")
Set_Color = myaddon.getSetting('SetColor')
Set_View = myaddon.getSetting('SetView')
def run():

    plugintools.log("---> chopodplay.run <---")
    plugintools.set_view(plugintools.LIST)

    # Get params
    params = plugintools.get_params()

    if params.get("action") is None:
        main_list(params)
    else:
       action = params.get("action")
       url = params.get("url")
       exec(action+"(params)")
    plugintools.close_item_list()

#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------
#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------
#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------



def cookie():
    import re,base64
    import requests
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8","Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3","Content-Type": "application/x-www-form-urlencoded", "Upgrade-Insecure-Requests": "1","Pragma": "no-cache","Cache-Control": "no-cache"}
 
    url = "https://www.croxyproxy.rocks/requests?fso="
 
    payload = {'url':'https://www.gnula2.co/estrenos/','proxyServerId':'94','demo':'0','frontOrigin':'https://www.croxyproxy.rocks'}
    x = requests.post(url,data=payload)
    return(x.headers['set-cookie'])
try:
    cookies=cookie()
except:
    cookies=''


def borrar(params):
    plugintools.log("choposex.borrar ")
    plugintools.set_view(plugintools.LIST)
    try:
        my_kodi = xbmc.translatePath('special://home/addons/plugin.video.choposex/')
    except:
        my_kodi = xbmcvfs.translatePath('special://home/addons/plugin.video.choposex/')
    mikodi= my_kodi+'subtitulos.txt'
    f = open(mikodi,'w+')
    f.write('noclave')
    f.close()
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]clave borrada[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://i.imgur.com/yL7keZ1.jpg", fanart = "https://www.multichannel.com/.image/t_share/MTU0MDYzODE1OTc5MDUwNzQ3/bigstock-xxx-adult-rubber-stamp-44482702jpg.jpg",  folder = False )

def main_list(params):
    plugintools.log("choposex.main_list ")
    plugintools.set_view(plugintools.LIST)
    plugintools.add_item(action="", title="[COLOR lime]addon valido para cualquier version kodi[/COLOR]",thumbnail="https://tecnolocura.es/wp-content/uploads/2019/11/Kodi-19-Matrix-ya-est%C3%A1-disponible-para-descargar.-%C2%A1Cuidado-tecnolocura-1.jpg", fanart="https://imagekit.androidphoria.com/wp-content/uploads/kodi-19.jpg",  url= "",folder= False )
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]----------------- [COLOR fuchsia] choposex [COLOR yellow]-----------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://thumbs.dreamstime.com/b/el-grunge-texturiz%C3%B3-sello-adulto-del-xxx-122142866.jpg", fanart = "https://img3.stockfresh.com/files/c/chrisdorney/m/71/3928287_stock-photo-xxx-adult-rubber-stamp.jpg",  folder = False )
    try:
        my_kodi = xbmc.translatePath('special://home/addons/plugin.video.choposex/')
    except:
        my_kodi = xbmcvfs.translatePath('special://home/addons/plugin.video.choposex/')
    mikodi= my_kodi+'subtitulos.txt'
    f = open(mikodi,'r')
    mensaje = f.read()
    if 'x69' in mensaje:
        plugintools.add_item(action = "menu_principal" , title = "[COLOR lime] clave guardada...[/COLOR]"+"[B][LOWERCASE][CAPITALIZE][COLOR %s]entrar al addon[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color, thumbnail ="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9PrWdcYR2t0pJjXg_Wi02ZyiP6E1PJ0mmilizp745_fazgzxu&s", fanart = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9PrWdcYR2t0pJjXg_Wi02ZyiP6E1PJ0mmilizp745_fazgzxu&s",  folder = True )





        plugintools.add_item(action = "borrar" , title = "[B][LOWERCASE][CAPITALIZE][COLOR red]borrar la clave[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://thumbs.dreamstime.com/b/el-grunge-texturiz%C3%B3-sello-adulto-del-xxx-122142866.jpg", fanart = "https://img3.stockfresh.com/files/c/chrisdorney/m/71/3928287_stock-photo-xxx-adult-rubber-stamp.jpg",  folder = True )
        plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]----------------- [COLOR fuchsia] choposex [COLOR yellow]-----------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://thumbs.dreamstime.com/b/el-grunge-texturiz%C3%B3-sello-adulto-del-xxx-122142866.jpg", fanart = "https://img3.stockfresh.com/files/c/chrisdorney/m/71/3928287_stock-photo-xxx-adult-rubber-stamp.jpg",  folder = False )
    else:


        plugintools.add_item(action = "acceso" , title = "[B][LOWERCASE][CAPITALIZE][COLOR orange]introduce la clave aqui[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://i.imgur.com/yL7keZ1.jpg", fanart = "https://www.multichannel.com/.image/t_share/MTU0MDYzODE1OTc5MDUwNzQ3/bigstock-xxx-adult-rubber-stamp-44482702jpg.jpg",  folder = True )
        plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]---------------------------------------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://thumbs.dreamstime.com/b/el-grunge-texturiz%C3%B3-sello-adulto-del-xxx-122142866.jpg", fanart = "https://img3.stockfresh.com/files/c/chrisdorney/m/71/3928287_stock-photo-xxx-adult-rubber-stamp.jpg",  folder = False )

        plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR white] para acceder al addon debes tener una clave[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://thumbs.dreamstime.com/b/el-grunge-texturiz%C3%B3-sello-adulto-del-xxx-122142866.jpg", fanart = "https://img3.stockfresh.com/files/c/chrisdorney/m/71/3928287_stock-photo-xxx-adult-rubber-stamp.jpg",  folder = False )



        plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR white] pasate por  nuestro grupo de telegram[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://thumbs.dreamstime.com/b/el-grunge-texturiz%C3%B3-sello-adulto-del-xxx-122142866.jpg", fanart = "https://img3.stockfresh.com/files/c/chrisdorney/m/71/3928287_stock-photo-xxx-adult-rubber-stamp.jpg",  folder = False )



        plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR gold]@tvchopo  [COLOR white]  y te la daremos  [/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://thumbs.dreamstime.com/b/el-grunge-texturiz%C3%B3-sello-adulto-del-xxx-122142866.jpg", fanart = "https://img3.stockfresh.com/files/c/chrisdorney/m/71/3928287_stock-photo-xxx-adult-rubber-stamp.jpg",  folder = False )

        plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]----------------- [COLOR fuchsia] choposex [COLOR yellow]-----------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://thumbs.dreamstime.com/b/el-grunge-texturiz%C3%B3-sello-adulto-del-xxx-122142866.jpg", fanart = "https://img3.stockfresh.com/files/c/chrisdorney/m/71/3928287_stock-photo-xxx-adult-rubber-stamp.jpg",  folder = False )

def acceso(params):
    plugintools.log("choposex.clasicos_del_cine")
    dialog = xbmcgui.Dialog()
    d = dialog.input('[B][LOWERCASE][CAPITALIZE][COLOR white]introduce la [COLOR yellow]clave[/COLOR][/CAPITALIZE][/LOWERCASE][/B]', type=xbmcgui.INPUT_ALPHANUM).replace(" ", "%20")
    try:
        my_kodi = xbmc.translatePath('special://home/addons/plugin.video.choposex/')
    except:
        my_kodi = xbmcvfs.translatePath('special://home/addons/plugin.video.choposex/')
    mikodi= my_kodi+'subtitulos.txt'
    f = open(mikodi,'w+')
    f.write(d)
    f.close()
    foto1 = "https://pastebin.com/raw/ZJw0rpBF"
    foto1=foto1.replace('pastebin.com','178.63.43.119')+'?__cpo=aHR0cHM6Ly9wYXN0ZWJpbi5jb20'
    headers= {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0","Cookie":cookies}
    url = requests.get(foto1,headers=headers,verify=False,timeout=5)
 
    if six.PY3:
        foto1 = url.text
    else:
        foto1 = url.content
    if d == foto1:
        escribir=d
        try:
            my_kodi = xbmc.translatePath('special://home/addons/plugin.video.choposex/')
        except:
            my_kodi = xbmcvfs.translatePath('special://home/addons/plugin.video.choposex/')
        mikodi= my_kodi+'subtitulos.txt'
        f = open(mikodi,'w+')
        f.write(escribir)
        f.close()
        plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]----------------- [COLOR fuchsia] choposex [COLOR yellow]-----------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://thumbs.dreamstime.com/b/el-grunge-texturiz%C3%B3-sello-adulto-del-xxx-122142866.jpg", fanart = "https://img3.stockfresh.com/files/c/chrisdorney/m/71/3928287_stock-photo-xxx-adult-rubber-stamp.jpg",  folder = False )





        plugintools.add_item(action = "menu_principal" , title = "[COLOR lime] clave correcta...[/COLOR]"+"[B][LOWERCASE][CAPITALIZE][COLOR %s]entrar al addon[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color, thumbnail ="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9PrWdcYR2t0pJjXg_Wi02ZyiP6E1PJ0mmilizp745_fazgzxu&s", fanart = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9PrWdcYR2t0pJjXg_Wi02ZyiP6E1PJ0mmilizp745_fazgzxu&s",  folder = True )




    else:



        plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]----------------- [COLOR fuchsia] choposex [COLOR yellow]-----------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://thumbs.dreamstime.com/b/el-grunge-texturiz%C3%B3-sello-adulto-del-xxx-122142866.jpg", fanart = "https://img3.stockfresh.com/files/c/chrisdorney/m/71/3928287_stock-photo-xxx-adult-rubber-stamp.jpg",  folder = False )
        dialog = xbmcgui.Dialog().ok('[B][COLOR lime]DEBES introducir la clave.........[COLOR red][/COLOR][/B]', '[B][LOWERCASE][CAPITALIZE][COLOR aqua]asegurate esta poniendo la clave correctamente[/COLOR][/CAPITALIZE][/LOWERCASE][/B]')
        plugintools.add_item(action = "acceso" , title = dialog, thumbnail ="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9PrWdcYR2t0pJjXg_Wi02ZyiP6E1PJ0mmilizp745_fazgzxu&s", fanart = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9PrWdcYR2t0pJjXg_Wi02ZyiP6E1PJ0mmilizp745_fazgzxu&s",  folder = True )



        plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]----------------- [COLOR fuchsia] choposex [COLOR yellow]-----------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://thumbs.dreamstime.com/b/el-grunge-texturiz%C3%B3-sello-adulto-del-xxx-122142866.jpg", fanart = "https://img3.stockfresh.com/files/c/chrisdorney/m/71/3928287_stock-photo-xxx-adult-rubber-stamp.jpg",  folder = False )

def menu_principal(params):
    plugintools.add_item(action="", title="[COLOR lime]addon adaptado y totalmente valido para kodi 18 y 19[/COLOR]",thumbnail="https://tecnolocura.es/wp-content/uploads/2019/11/Kodi-19-Matrix-ya-est%C3%A1-disponible-para-descargar.-%C2%A1Cuidado-tecnolocura-1.jpg", fanart="https://imagekit.androidphoria.com/wp-content/uploads/kodi-19.jpg",  url= "",folder= False )
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]----------------- [COLOR fuchsia] choposex [COLOR yellow]-----------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://thumbs.dreamstime.com/b/el-grunge-texturiz%C3%B3-sello-adulto-del-xxx-122142866.jpg", fanart = "https://img3.stockfresh.com/files/c/chrisdorney/m/71/3928287_stock-photo-xxx-adult-rubber-stamp.jpg",  folder = False )



    plugintools.add_item(action = "xvideos_menu" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]xvideos [/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color, thumbnail ="https://lh3.googleusercontent.com/proxy/WTC055bkLO-JyYQFHUo23fmxj0bBt8PgWCTHrgYJRWnQAh6PSIKOZHCmiloMAlSm7rF_DkD1mYoEozp1SiaVOYLTveIeKUJWMq_DwR6t4yuVfyDWwHo9FfxeWzkbocms2-shKIJ9btYsvw", fanart = "https://1000logos.net/wp-content/uploads/2018/12/Symbol-XVideos.jpg", url="",  folder = True )






    plugintools.add_item(action = "menuplayvid" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]playvids [/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color, thumbnail ="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9PrWdcYR2t0pJjXg_Wi02ZyiP6E1PJ0mmilizp745_fazgzxu&s", fanart = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9PrWdcYR2t0pJjXg_Wi02ZyiP6E1PJ0mmilizp745_fazgzxu&s",  folder = True )

    plugintools.add_item(action = "pelis_completas" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]peliculas completas[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color, thumbnail ="https://live.staticflickr.com/1615/25665286642_0152c8a890_b.jpg", fanart = "https://thumbs.dreamstime.com/b/contenido-del-adulto-xxx-36739011.jpg",url="https://www.xnxx.com/search/20min+/Peliculas+porno+xxx+cine+pelicula+completa/",  folder = True )


    plugintools.add_item(action = "pelis_secciones" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]mega-secciones[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color, thumbnail ="https://thumbs.dreamstime.com/b/contenido-del-adulto-xxx-36739011.jpg", fanart = "https://previews.123rf.com/images/gorkemdemir/gorkemdemir1409/gorkemdemir140900475/31478949-xxx-adult-rubber-stamp-over-a-white-background-.jpg",url="https://www.xnxx.com/tags",  folder = True )



    plugintools.add_item(action = "pelis_anios" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]lo mejor de ..[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color, thumbnail ="https://live.staticflickr.com/1615/25665286642_0152c8a890_b.jpg", fanart = "https://thumbs.dreamstime.com/b/contenido-del-adulto-xxx-36739011.jpg",url="https://www.xnxx.com/best/2020-03",  folder = True )

    plugintools.add_item(action = "pelis_visto" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]lo mas visto..[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color, thumbnail ="https://live.staticflickr.com/1615/25665286642_0152c8a890_b.jpg", fanart = "https://thumbs.dreamstime.com/b/contenido-del-adulto-xxx-36739011.jpg",url="https://www.xnxx.com/hits",  folder = True )





    plugintools.add_item(action = "canales_xxx" , title = "[B][LOWERCASE][CAPITALIZE][COLOR white]canales xxx [/COLOR][/B][/CAPITALIZE][/LOWERCASE]", thumbnail ="https://whatdir.com/assets/whatsapp-groups/adults18.png", fanart = "https://i.imgur.com/m9vkwev.jpg",  folder = True )


    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]----------------- [COLOR fuchsia] choposex [COLOR yellow]-----------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://thumbs.dreamstime.com/b/el-grunge-texturiz%C3%B3-sello-adulto-del-xxx-122142866.jpg", fanart = "https://img3.stockfresh.com/files/c/chrisdorney/m/71/3928287_stock-photo-xxx-adult-rubber-stamp.jpg",  folder = False )



def xvideos_menu(params):
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]---------------------[COLOR fuchsia]xvideos[COLOR yellow]---------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://lh3.googleusercontent.com/proxy/WTC055bkLO-JyYQFHUo23fmxj0bBt8PgWCTHrgYJRWnQAh6PSIKOZHCmiloMAlSm7rF_DkD1mYoEozp1SiaVOYLTveIeKUJWMq_DwR6t4yuVfyDWwHo9FfxeWzkbocms2-shKIJ9btYsvw", fanart = "https://1000logos.net/wp-content/uploads/2018/12/Symbol-XVideos.jpg",  folder = False )
    plugintools.add_item(action = "xvideos_idioma" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]xvideos idioma[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color, thumbnail ="https://lh3.googleusercontent.com/proxy/WTC055bkLO-JyYQFHUo23fmxj0bBt8PgWCTHrgYJRWnQAh6PSIKOZHCmiloMAlSm7rF_DkD1mYoEozp1SiaVOYLTveIeKUJWMq_DwR6t4yuVfyDWwHo9FfxeWzkbocms2-shKIJ9btYsvw", fanart = "https://1000logos.net/wp-content/uploads/2018/12/Symbol-XVideos.jpg", url="page=1",  folder = True )

    plugintools.add_item(action = "xvideos_tag" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]xvideos tag[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color, thumbnail ="https://lh3.googleusercontent.com/proxy/WTC055bkLO-JyYQFHUo23fmxj0bBt8PgWCTHrgYJRWnQAh6PSIKOZHCmiloMAlSm7rF_DkD1mYoEozp1SiaVOYLTveIeKUJWMq_DwR6t4yuVfyDWwHo9FfxeWzkbocms2-shKIJ9btYsvw", fanart = "https://1000logos.net/wp-content/uploads/2018/12/Symbol-XVideos.jpg",   folder = True )
    plugintools.add_item(action = "xvideos_buscador" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]xvideos buscador[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color, thumbnail ="https://lh3.googleusercontent.com/proxy/WTC055bkLO-JyYQFHUo23fmxj0bBt8PgWCTHrgYJRWnQAh6PSIKOZHCmiloMAlSm7rF_DkD1mYoEozp1SiaVOYLTveIeKUJWMq_DwR6t4yuVfyDWwHo9FfxeWzkbocms2-shKIJ9btYsvw", fanart = "https://1000logos.net/wp-content/uploads/2018/12/Symbol-XVideos.jpg", url="page=1",  folder = True )
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]---------------------[COLOR fuchsia]xvideos[COLOR yellow]---------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://lh3.googleusercontent.com/proxy/WTC055bkLO-JyYQFHUo23fmxj0bBt8PgWCTHrgYJRWnQAh6PSIKOZHCmiloMAlSm7rF_DkD1mYoEozp1SiaVOYLTveIeKUJWMq_DwR6t4yuVfyDWwHo9FfxeWzkbocms2-shKIJ9btYsvw", fanart = "https://1000logos.net/wp-content/uploads/2018/12/Symbol-XVideos.jpg",   folder = False )
def xvideos_buscador(params):
    plugintools.log("choposex.clasicos_del_cine")

    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]---------------------[COLOR fuchsia]xvideos[COLOR yellow]---------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://lh3.googleusercontent.com/proxy/WTC055bkLO-JyYQFHUo23fmxj0bBt8PgWCTHrgYJRWnQAh6PSIKOZHCmiloMAlSm7rF_DkD1mYoEozp1SiaVOYLTveIeKUJWMq_DwR6t4yuVfyDWwHo9FfxeWzkbocms2-shKIJ9btYsvw", fanart = "https://1000logos.net/wp-content/uploads/2018/12/Symbol-XVideos.jpg",  folder = False )
    plugintools.set_view(plugintools.MOVIES,502)
    dialog = xbmcgui.Dialog()
    d = dialog.input('[B][LOWERCASE][CAPITALIZE][COLOR orange]buscar videos por ejemplo: [COLOR white]anal[/COLOR][/CAPITALIZE][/LOWERCASE][/B]', type=xbmcgui.INPUT_ALPHANUM).replace(" ", "+")
    numero = params.get("url")
    url1='https://www.xvideos.com/?k='+d
    if six.PY3==True:
        data = plugintools.read(url1).decode('utf-8')
    else:
        data = plugintools.read(url1)     
    siguiente = plugintools.find_single_match(data,'class="last-page">.*?</a></li><li><a href="(.*?)" class="no-page next-page">')

    matches = plugintools.find_multiple_matches(data,'<div id="video_.*?href=".*?".*?data-src=".*?".*?mark">.*?<.*?title=".*?".*?class="duration">.*?<')
    for generos in matches:

        url = 'https://www.xvideos.com'+plugintools.find_single_match(generos,'<div id="video_.*?href="(.*?)".*?')

        foto = plugintools.find_single_match(generos,'data-src="(.*?)".*?')

        titulo = plugintools.find_single_match(generos,'title="(.*?)".*?').replace("&aacute;", "a").replace("&ntilde;", "Ôö£├ÂÔö£├éÔö¼├║Ôö£├ÂÔö£ÔòùÔö£├Ñ").replace("&eacute;", "e")

        calidad = plugintools.find_single_match(generos,'mark">(.*?)<.*?')

        plugintools.add_item(action = "xvideos_links" , title ="[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]  [COLOR fuchsia]"+calidad+'[/COLOR]' ,url =url , thumbnail =foto, fanart = foto,  folder=True)
    plugintools.add_item( action="xvideos_idioma_videos" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]   [COLOR lime]ir a la pagina siguiente [/B][/COLOR][/CAPITALIZE][/LOWERCASE]", url= url1+siguiente, thumbnail = "https://www.periodicoelpunto.com/wp-content/uploads/2019/03/flecha-siguiente.png",fanart = "https://www.periodicoelpunto.com/wp-content/uploads/2019/03/flecha-siguiente.png", folder=True )

    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]---------------------[COLOR fuchsia]xvideos[COLOR yellow]---------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://lh3.googleusercontent.com/proxy/WTC055bkLO-JyYQFHUo23fmxj0bBt8PgWCTHrgYJRWnQAh6PSIKOZHCmiloMAlSm7rF_DkD1mYoEozp1SiaVOYLTveIeKUJWMq_DwR6t4yuVfyDWwHo9FfxeWzkbocms2-shKIJ9btYsvw", fanart = "https://1000logos.net/wp-content/uploads/2018/12/Symbol-XVideos.jpg",  folder = False )

def xvideos_tag(params):
    plugintools.log("choposex.xvideos "+repr(params))
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]------------------------------[COLOR yellow] choposex[COLOR aqua]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://lh3.googleusercontent.com/proxy/WTC055bkLO-JyYQFHUo23fmxj0bBt8PgWCTHrgYJRWnQAh6PSIKOZHCmiloMAlSm7rF_DkD1mYoEozp1SiaVOYLTveIeKUJWMq_DwR6t4yuVfyDWwHo9FfxeWzkbocms2-shKIJ9btYsvw", fanart = "https://1000logos.net/wp-content/uploads/2018/12/Symbol-XVideos.jpg",   folder = False )
    thumbnail = params.get("thumbnail")
    url = "https://www.xvideos.com/tags"
    if six.PY3==True:
        data = plugintools.read(url).decode('utf-8')
    else:
        data = plugintools.read(url)
    matches = plugintools.find_multiple_matches(data,'topcat topcat-.*?"><a href=".*?".*?btn btn-default">.*?<')
    for generos in matches:
        titulo = plugintools.find_single_match(generos,'btn btn-default">(.*?)<')
        url = 'https://www.xvideos.com'+plugintools.find_single_match(generos,'a href="(.*?)"')
        plugintools.add_item(action = "xvideos_idioma_videos" , title ="[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" ,url =url , thumbnail =thumbnail, fanart = thumbnail,  folder= True)
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]------------------------------[COLOR yellow] choposex[COLOR aqua]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://lh3.googleusercontent.com/proxy/WTC055bkLO-JyYQFHUo23fmxj0bBt8PgWCTHrgYJRWnQAh6PSIKOZHCmiloMAlSm7rF_DkD1mYoEozp1SiaVOYLTveIeKUJWMq_DwR6t4yuVfyDWwHo9FfxeWzkbocms2-shKIJ9btYsvw", fanart = "https://1000logos.net/wp-content/uploads/2018/12/Symbol-XVideos.jpg",   folder = False )

def xvideos_idioma(params):
    plugintools.log("choposex.xvideos "+repr(params))
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]------------------------------[COLOR yellow] choposex[COLOR aqua]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://lh3.googleusercontent.com/proxy/WTC055bkLO-JyYQFHUo23fmxj0bBt8PgWCTHrgYJRWnQAh6PSIKOZHCmiloMAlSm7rF_DkD1mYoEozp1SiaVOYLTveIeKUJWMq_DwR6t4yuVfyDWwHo9FfxeWzkbocms2-shKIJ9btYsvw", fanart = "https://1000logos.net/wp-content/uploads/2018/12/Symbol-XVideos.jpg",   folder = False )
    thumbnail = params.get("thumbnail")
    url = "https://www.xvideos.com/tags"
    if six.PY3==True:
        data = plugintools.read(url).decode('utf-8')
    else:
        data = plugintools.read(url)

    matches = plugintools.find_multiple_matches(data,'<li><a href="/lang/.*?" title=".*?"')
    for generos in matches:
        titulo = plugintools.find_single_match(generos,' title="(.*?)"')
        url = 'https://www.xvideos.com'+plugintools.find_single_match(generos,'<li><a href="(/lang/.*?)"')



        plugintools.add_item(action = "xvideos_idioma_videos" , title ="[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" ,url =url , thumbnail ='', fanart = '',  folder= True)
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]------------------------------[COLOR yellow] choposex[COLOR aqua]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://lh3.googleusercontent.com/proxy/WTC055bkLO-JyYQFHUo23fmxj0bBt8PgWCTHrgYJRWnQAh6PSIKOZHCmiloMAlSm7rF_DkD1mYoEozp1SiaVOYLTveIeKUJWMq_DwR6t4yuVfyDWwHo9FfxeWzkbocms2-shKIJ9btYsvw", fanart = "https://1000logos.net/wp-content/uploads/2018/12/Symbol-XVideos.jpg",   folder = False )
def xvideos_idioma_videos(params):
    plugintools.log("choposex.xvideos "+repr(params))
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]------------------------------[COLOR yellow] choposex[COLOR aqua]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://lh3.googleusercontent.com/proxy/WTC055bkLO-JyYQFHUo23fmxj0bBt8PgWCTHrgYJRWnQAh6PSIKOZHCmiloMAlSm7rF_DkD1mYoEozp1SiaVOYLTveIeKUJWMq_DwR6t4yuVfyDWwHo9FfxeWzkbocms2-shKIJ9btYsvw", fanart = "https://1000logos.net/wp-content/uploads/2018/12/Symbol-XVideos.jpg",   folder = False )
    thumbnail = params.get("thumbnail")
    url = params.get("url")
    if six.PY3==True:
        data = plugintools.read(url).decode('utf-8')
    else:
        data = plugintools.read(url)
    siguiente = plugintools.find_single_match(data,'class="last-page">.*?</a></li><li><a href="(.*?)" class="no-page next-page">')

    matches = plugintools.find_multiple_matches(data,'<div id="video_.*?href=".*?".*?data-src=".*?".*?mark">.*?<.*?title=".*?".*?class="duration">.*?<')
    for generos in matches:

        url = 'https://www.xvideos.com'+plugintools.find_single_match(generos,'<div id="video_.*?href="(.*?)".*?')

        foto = plugintools.find_single_match(generos,'data-src="(.*?)".*?')

        titulo = plugintools.find_single_match(generos,'title="(.*?)".*?').replace("&aacute;", "a").replace("&ntilde;", "Ôö£├ÂÔö£├éÔö¼├║Ôö£├ÂÔö£ÔòùÔö£├Ñ").replace("&eacute;", "e")

        calidad = plugintools.find_single_match(generos,'mark">(.*?)<.*?')
        duracion = plugintools.find_single_match(generos,'lass="duration">(.*?)<')

        plugintools.add_item(action = "xvideos_links" , title ="[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo+" [COLOR gold] "+calidad+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]  [COLOR fuchsia]"+duracion+'[/COLOR]' ,url =url , thumbnail =foto, fanart = foto,  folder=True)
    plugintools.add_item( action="xvideos_idioma_videos" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]   [COLOR lime]ir a la pagina siguiente [/B][/COLOR][/CAPITALIZE][/LOWERCASE]", url= 'https://www.xvideos.com'+siguiente, thumbnail = "https://www.periodicoelpunto.com/wp-content/uploads/2019/03/flecha-siguiente.png",fanart = "https://www.periodicoelpunto.com/wp-content/uploads/2019/03/flecha-siguiente.png", folder=True )
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]------------------------------[COLOR yellow] choposex[COLOR aqua]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://lh3.googleusercontent.com/proxy/WTC055bkLO-JyYQFHUo23fmxj0bBt8PgWCTHrgYJRWnQAh6PSIKOZHCmiloMAlSm7rF_DkD1mYoEozp1SiaVOYLTveIeKUJWMq_DwR6t4yuVfyDWwHo9FfxeWzkbocms2-shKIJ9btYsvw", fanart = "https://1000logos.net/wp-content/uploads/2018/12/Symbol-XVideos.jpg",   folder = False )
def xvideos_links(params):
    plugintools.log("choposex.xvideos "+repr(params))
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]------------------------------[COLOR yellow] choposex[COLOR aqua]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://lh3.googleusercontent.com/proxy/WTC055bkLO-JyYQFHUo23fmxj0bBt8PgWCTHrgYJRWnQAh6PSIKOZHCmiloMAlSm7rF_DkD1mYoEozp1SiaVOYLTveIeKUJWMq_DwR6t4yuVfyDWwHo9FfxeWzkbocms2-shKIJ9btYsvw", fanart = "https://1000logos.net/wp-content/uploads/2018/12/Symbol-XVideos.jpg",   folder = False )
    thumbnail = params.get("thumbnail")
    url = params.get("url")
    if six.PY3==True:
        data = plugintools.read(url).decode('utf-8')
    else:
        data = plugintools.read(url)
    matches = plugintools.find_multiple_matches(data,"html5player.setVideo.*?.'https.*?'.")
    for generos in matches:

        url = plugintools.find_single_match(generos,"(https.*?)'")
        calidad = plugintools.find_single_match(generos,'html5player.setVideo(Url.*?|HLS.*?)\(').replace("Url", "")

        plugintools.add_item(action = "play_links" , title ="[B][LOWERCASE][CAPITALIZE][COLOR white]CALIDAD "+calidad+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",url =url , thumbnail =thumbnail, fanart = thumbnail,  folder=False,  isPlayable = True)

    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]------------------------------[COLOR yellow] choposex[COLOR aqua]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://lh3.googleusercontent.com/proxy/WTC055bkLO-JyYQFHUo23fmxj0bBt8PgWCTHrgYJRWnQAh6PSIKOZHCmiloMAlSm7rF_DkD1mYoEozp1SiaVOYLTveIeKUJWMq_DwR6t4yuVfyDWwHo9FfxeWzkbocms2-shKIJ9btYsvw", fanart = "https://1000logos.net/wp-content/uploads/2018/12/Symbol-XVideos.jpg",   folder = False )
        #-----------------------------------------------------------------------------------------

def canales_xxx(params):
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]----------------- [COLOR fuchsia] canales xxx [COLOR yellow]-----------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://thumbs.dreamstime.com/b/el-grunge-texturiz%C3%B3-sello-adulto-del-xxx-122142866.jpg", fanart = "https://img3.stockfresh.com/files/c/chrisdorney/m/71/3928287_stock-photo-xxx-adult-rubber-stamp.jpg",  folder = False )



    try:
        url = "http://adultiptv.net/lists/all.m3u"
        if six.PY3==True:
            data = plugintools.read(url).decode('utf-8')
        else:
            data = plugintools.read(url)

        matches = plugintools.find_multiple_matches(data,'#EXTINF:-1.*?m3u8')
        for generos in matches:
            titulo = plugintools.find_single_match(generos,'title="XXX",(.*?)\shttp')
            url = plugintools.find_single_match(generos,'title="XXX",.*?\s(http.*?m3u8)')
            foto1 = plugintools.find_single_match(generos,'tvg-logo="(.*?)"')


            plugintools.add_item(action = "play_links" , title ="[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" ,url =url , thumbnail =foto1, fanart = foto1,  folder=False,  isPlayable = True)
    except:
        pass





    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]----------------- [COLOR fuchsia] canales xxx [COLOR yellow]-----------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://thumbs.dreamstime.com/b/el-grunge-texturiz%C3%B3-sello-adulto-del-xxx-122142866.jpg", fanart = "https://img3.stockfresh.com/files/c/chrisdorney/m/71/3928287_stock-photo-xxx-adult-rubber-stamp.jpg",  folder = False )






def pelis_secciones(params):
    plugintools.log("choposex.clasicos_del_cine")
    plugintools.set_view(plugintools.MOVIES,502)
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]----------------- [COLOR fuchsia] chopoxxx mega-secciones[COLOR yellow]-----------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://live.staticflickr.com/1615/25665286642_0152c8a890_b.jpg", fanart = "https://thumbs.dreamstime.com/b/contenido-del-adulto-xxx-36739011.jpg",  folder = False )

    url = params.get("url")
    thumbnail = params.get("thumbnail")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers( url, headers=request_headers)
    if six.PY3==True:
        url = body.strip().decode('utf-8')
    else:
        url = body.strip()       
    matches = plugintools.find_multiple_matches(url,'<li><a href="/search/.*?">.*?</a><strong>.*?</strong></li>')
    for generos in matches:
        url = 'https://www.xnxx.com'+plugintools.find_single_match(generos,'href="(/search/.*?)">')
        titulo = plugintools.find_single_match(generos,'<li><a href="/search/.*?">(.*?)</a>')
        titulo2 = plugintools.find_single_match(generos,'</a><strong>(.*?)</strong>')
        plugintools.add_item(action = "pelis_completas" , title ="[B][LOWERCASE][CAPITALIZE][COLOR gold]"+titulo+" [COLOR white] " +titulo2+" videos[/B][/COLOR][/CAPITALIZE][/LOWERCASE]", thumbnail =thumbnail, fanart =thumbnail, url =url, folder=True )

    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]----------------- [COLOR fuchsia] chopoxxx mega-secciones[COLOR yellow]-----------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://live.staticflickr.com/1615/25665286642_0152c8a890_b.jpg", fanart = "https://thumbs.dreamstime.com/b/contenido-del-adulto-xxx-36739011.jpg",  folder = False )


def pelis_visto(params):
    plugintools.log("choposex.clasicos_del_cine")
    plugintools.set_view(plugintools.MOVIES,502)
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]----------------- [COLOR fuchsia] chopoxxx [COLOR yellow]-----------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://live.staticflickr.com/1615/25665286642_0152c8a890_b.jpg", fanart = "https://thumbs.dreamstime.com/b/contenido-del-adulto-xxx-36739011.jpg",  folder = False )

    url = params.get("url")
    thumbnail = params.get("thumbnail")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers( url, headers=request_headers)
    if six.PY3==True:
        url = body.strip().decode('utf-8')
    else:
        url = body.strip() 
    matches = plugintools.find_multiple_matches(url,'<li><a href="/hits/.*?</a></li>')
    for generos in matches:
        url = 'https://www.xnxx.com'+plugintools.find_single_match(generos,'href="(.*?)">')
        titulo = plugintools.find_single_match(generos,' href="/hits/.*?">(.*?)<')

        plugintools.add_item(action = "pelis_completas" , title ="[B][LOWERCASE][CAPITALIZE][COLOR gold]lo mas visto "+titulo+"[/B][/COLOR][/CAPITALIZE][/LOWERCASE]", thumbnail =thumbnail, fanart =thumbnail, url =url, folder=True )




def pelis_anios(params):
    plugintools.log("choposex.clasicos_del_cine")
    plugintools.set_view(plugintools.MOVIES,502)
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]----------------- [COLOR fuchsia] chopoxxx [COLOR yellow]-----------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://live.staticflickr.com/1615/25665286642_0152c8a890_b.jpg", fanart = "https://thumbs.dreamstime.com/b/contenido-del-adulto-xxx-36739011.jpg",  folder = False )

    url = params.get("url")
    thumbnail = params.get("thumbnail")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers( url, headers=request_headers)
    if six.PY3==True:
        url = body.strip().decode('utf-8')
    else:
        url = body.strip() 
    matches = plugintools.find_multiple_matches(url,'class="icon-f icf-angle-left"></span>.*?<li class="year-month"><a class="month-label" href=".*?">')
    for generos in matches:
        url = 'https://www.xnxx.com'+plugintools.find_single_match(generos,'class="month-label" href="(.*?)">')
        titulo = plugintools.find_single_match(generos,'ngle-left"></span>(.*?)<')

        plugintools.add_item(action = "pelis_completas" , title ="[B][LOWERCASE][CAPITALIZE][COLOR gold]lo mejor del "+titulo+"[/B][/COLOR][/CAPITALIZE][/LOWERCASE]", thumbnail =thumbnail, fanart =thumbnail, url =url, folder=True )




def pelis_completas(params):
    plugintools.log("choposex.clasicos_del_cine")
    plugintools.set_view(plugintools.MOVIES,502)
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]----------------- [COLOR fuchsia] chopoxxx [COLOR yellow]-----------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://live.staticflickr.com/1615/25665286642_0152c8a890_b.jpg", fanart = "https://thumbs.dreamstime.com/b/contenido-del-adulto-xxx-36739011.jpg",  folder = False )

    url = params.get("url")
    thumbnail = params.get("thumbnail")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers( url, headers=request_headers)
    if six.PY3==True:
        url = body.strip().decode('utf-8')
    else:
        url = body.strip() 
    siguiente= 'https://www.xnxx.com'+plugintools.find_single_match(url,'<li><a class="active" href="">.*?</a></li><li>.*?href="(.*?)">.*?</a>')
    matches = plugintools.find_multiple_matches(url,'<span class="video.*?</span></span>')
    for generos in matches:
        url = 'https://www.xnxx.com'+plugintools.find_single_match(generos,'a href="(.*?)"')
        titulo = plugintools.find_single_match(generos,' title="(.*?)"')
        foto = plugintools.find_single_match(generos,'data-src="(.*?)"')

        plugintools.add_item(action = "pelis_reproducir" , title ="[B][LOWERCASE][CAPITALIZE][COLOR gold]"+titulo+"[/B][/COLOR][/CAPITALIZE][/LOWERCASE]", thumbnail =foto, fanart =foto, url =url, folder=True )

    if '/' in siguiente:
        plugintools.add_item( action="pelis_completas" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]   [COLOR lime]ir a la pagina siguiente[/B][/COLOR][/CAPITALIZE][/LOWERCASE]", url= siguiente, thumbnail = "https://www.periodicoelpunto.com/wp-content/uploads/2019/03/flecha-siguiente.png",fanart = "https://www.periodicoelpunto.com/wp-content/uploads/2019/03/flecha-siguiente.png", folder=True )

    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]----------------- [COLOR fuchsia] chopoxxx [COLOR yellow]-----------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://live.staticflickr.com/1615/25665286642_0152c8a890_b.jpg", fanart = "https://thumbs.dreamstime.com/b/contenido-del-adulto-xxx-36739011.jpg",  folder = False )


def pelis_reproducir(params):
    plugintools.log("choposex.clasicos_del_cine")

    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]----------------- [COLOR fuchsia] chopoxxx [COLOR yellow]-----------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://live.staticflickr.com/1615/25665286642_0152c8a890_b.jpg", fanart = "https://thumbs.dreamstime.com/b/contenido-del-adulto-xxx-36739011.jpg",  folder = False )
    plugintools.set_view(plugintools.MOVIES,502)
    url = params.get("url")
    thumbnail = params.get("thumbnail")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers( url, headers=request_headers)
    if six.PY3==True:
        url = body.strip().decode('utf-8')
    else:
        url = body.strip() 
    url = plugintools.find_single_match(url,"setVideoUrlHigh.'(.*?)'")
    plugintools.add_item(action = "play_links" , title ="[B][LOWERCASE][CAPITALIZE][COLOR gold]reproducir aqui[/B][/COLOR][/CAPITALIZE][/LOWERCASE]", thumbnail =thumbnail, fanart =thumbnail, url =url, folder=False,  isPlayable = True )     

    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]----------------- [COLOR fuchsia] chopoxxx [COLOR yellow]-----------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://live.staticflickr.com/1615/25665286642_0152c8a890_b.jpg", fanart = "https://thumbs.dreamstime.com/b/contenido-del-adulto-xxx-36739011.jpg",  folder = False )
#--------------playvids-----------------------playvids----------------------playvids-----------------------------playvids--------------------playvids#--------------playvids-----------------------playvids----------------------playvids-----------------------------playvids--------------------playvids #--------------playvids-----------------------playvids----------------------playvids-----------------------------playvids--------------------playvids #--------------playvids-----------------------playvids----------------------playvids-----------------------------playvids--------------------playvids #--------------playvids-----------------------playvids----------------------playvids-----------------------------playvids--------------------playvids #--------------playvids-----------------------playvids----------------------playvids-----------------------------playvids--------------------playvids #--------------playvids-----------------------playvids----------------------playvids-----------------------------playvids--------------------playvids #--------------playvids-----------------------playvids----------------------playvids-----------------------------playvids--------------------playvids #--------------playvids-----------------------playvids----------------------playvids-----------------------------playvids--------------------playvids
def menuplayvid(params):
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]----------------- [COLOR fuchsia] menu playvids [COLOR yellow]-----------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9PrWdcYR2t0pJjXg_Wi02ZyiP6E1PJ0mmilizp745_fazgzxu&s", fanart = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9PrWdcYR2t0pJjXg_Wi02ZyiP6E1PJ0mmilizp745_fazgzxu&s",  folder = False )


    plugintools.add_item(action = "playvids_brazzers" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]playvids brazzers[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color, thumbnail ="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9PrWdcYR2t0pJjXg_Wi02ZyiP6E1PJ0mmilizp745_fazgzxu&s", fanart = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9PrWdcYR2t0pJjXg_Wi02ZyiP6E1PJ0mmilizp745_fazgzxu&s",url="https://www.playvids.com/es/Brazzers",  folder = True )

    plugintools.add_item(action = "playvids_buscador" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]playvids buscador[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color, thumbnail ="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9PrWdcYR2t0pJjXg_Wi02ZyiP6E1PJ0mmilizp745_fazgzxu&s", fanart = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9PrWdcYR2t0pJjXg_Wi02ZyiP6E1PJ0mmilizp745_fazgzxu&s",url="page=1",  folder = True )


    plugintools.add_item(action = "playvids_Trending" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]playvids Trending Porn[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color, thumbnail ="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9PrWdcYR2t0pJjXg_Wi02ZyiP6E1PJ0mmilizp745_fazgzxu&s", fanart = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9PrWdcYR2t0pJjXg_Wi02ZyiP6E1PJ0mmilizp745_fazgzxu&s",url="https://www.playvids.com/es/Trending-Porn",  folder = True )


    plugintools.add_item(action = "playvids_categorias" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]playvids categorias[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color, thumbnail ="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9PrWdcYR2t0pJjXg_Wi02ZyiP6E1PJ0mmilizp745_fazgzxu&s", fanart = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9PrWdcYR2t0pJjXg_Wi02ZyiP6E1PJ0mmilizp745_fazgzxu&s",url="https://www.playvids.com/es/categories",  folder = True )      


    plugintools.add_item(action = "playvids_subcategorias" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]playvids subcategorias[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color, thumbnail ="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9PrWdcYR2t0pJjXg_Wi02ZyiP6E1PJ0mmilizp745_fazgzxu&s", fanart = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9PrWdcYR2t0pJjXg_Wi02ZyiP6E1PJ0mmilizp745_fazgzxu&s",url="https://www.playvids.com/es/categories",  folder = True )


    plugintools.add_item(action = "playvids_Pornstars" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]playvids Pornstars[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color, thumbnail ="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9PrWdcYR2t0pJjXg_Wi02ZyiP6E1PJ0mmilizp745_fazgzxu&s", fanart = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9PrWdcYR2t0pJjXg_Wi02ZyiP6E1PJ0mmilizp745_fazgzxu&s",url="https://www.playvids.com/es/pornstars",  folder = True )



    plugintools.add_item(action = "playvids_masPornstars" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]playvids mas Pornstars[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color, thumbnail ="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9PrWdcYR2t0pJjXg_Wi02ZyiP6E1PJ0mmilizp745_fazgzxu&s", fanart = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9PrWdcYR2t0pJjXg_Wi02ZyiP6E1PJ0mmilizp745_fazgzxu&s",url="https://www.playvids.com/es/pornstars",  folder = True )  


    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]----------------- [COLOR fuchsia] menu playvids [COLOR yellow]-----------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9PrWdcYR2t0pJjXg_Wi02ZyiP6E1PJ0mmilizp745_fazgzxu&s", fanart = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9PrWdcYR2t0pJjXg_Wi02ZyiP6E1PJ0mmilizp745_fazgzxu&s",  folder = False )





def playvids_buscador(params):
    plugintools.log("choposex.clasicos_del_cine")

    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]---------------------[COLOR fuchsia]playvids[COLOR yellow]---------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9PrWdcYR2t0pJjXg_Wi02ZyiP6E1PJ0mmilizp745_fazgzxu&s", fanart = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9PrWdcYR2t0pJjXg_Wi02ZyiP6E1PJ0mmilizp745_fazgzxu&s",  folder = False )
    plugintools.set_view(plugintools.MOVIES,502)
    dialog = xbmcgui.Dialog()
    d = dialog.input('[B][LOWERCASE][CAPITALIZE][COLOR orange]buscar videos por ejemplo: [COLOR white]anal[/COLOR][/CAPITALIZE][/LOWERCASE][/B]', type=xbmcgui.INPUT_ALPHANUM).replace(" ", "+")
    numero = params.get("url")
    page='https://www.playvids.com/es/sq?q='+d+'&'+numero
    thumbnail = params.get("thumbnail")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers( page, headers=request_headers)
    if six.PY3==True:
        url = body.strip().decode('utf-8')
    else:
        url = body.strip() 
    siguiente= plugintools.find_single_match(url,'class="next" href=".*?q=.*?&(page=.*?)">Siguiente')
    matches = plugintools.find_multiple_matches(url,'<div class="card-img">.*?</div>')
    for generos in matches:
        url = 'https://www.playvids.com'+plugintools.find_single_match(generos,'href="(.*?)"')
        foto = plugintools.find_single_match(generos,'src="(.*?)"')
        titulo = plugintools.find_single_match(generos,'alt="(.*?)"')
        duracion = plugintools.find_single_match(generos,'duration">(.*?)<.*?')
        plugintools.add_item(action = "server" , title ="[B][LOWERCASE][CAPITALIZE][COLOR gold]"+titulo+" [COLOR white]"+duracion+"[/B][/COLOR][/CAPITALIZE][/LOWERCASE]", thumbnail =foto, fanart =foto, url =url, folder=True )





def playvids_masPornstars(params):
    plugintools.log("choposex.clasicos_del_cine")

    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]---------------------[COLOR fuchsia]playvids[COLOR yellow]---------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9PrWdcYR2t0pJjXg_Wi02ZyiP6E1PJ0mmilizp745_fazgzxu&s", fanart = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9PrWdcYR2t0pJjXg_Wi02ZyiP6E1PJ0mmilizp745_fazgzxu&s",  folder = False )
    plugintools.set_view(plugintools.MOVIES,502)
    url8 = params.get("url")
    thumbnail = params.get("thumbnail")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers( url8, headers=request_headers)
    if six.PY3==True:
        url = body.strip().decode('utf-8')
    else:
        url = body.strip() 
    siguiente = plugintools.find_single_match(url,'<li><a class="next" href="(.*?)">Siguiente</a></li>')
    matches = plugintools.find_multiple_matches(url,'li class="overflow-visible">.*?</a>')
    for generos in matches:
        titulo = plugintools.find_single_match(generos,'<a href=".*?" >\s*(.*?)\n')
        url1 = plugintools.find_single_match(generos,'a href="(.*?)"')
        url = 'https://www.playvids.com'+url1
        foto = plugintools.find_single_match(generos,'src="(.*?)"')
        plugintools.add_item(action = "playvids_Trending" , title ="[B][LOWERCASE][CAPITALIZE][COLOR gold]"+titulo+"[/B][/COLOR][/CAPITALIZE][/LOWERCASE]", thumbnail =thumbnail, fanart =thumbnail, url =url, folder=True )

    if 'page' in siguiente:
        plugintools.add_item( action="playvids_masPornstars" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]ir a la pagina siguiente[/B][/COLOR][/CAPITALIZE][/LOWERCASE]", url= "https://www.playvids.com"+siguiente, thumbnail = "https://www.periodicoelpunto.com/wp-content/uploads/2019/03/flecha-siguiente.png",fanart = "https://www.periodicoelpunto.com/wp-content/uploads/2019/03/flecha-siguiente.png", folder=True )

    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]---------------------[COLOR fuchsia]playvids[COLOR yellow]---------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9PrWdcYR2t0pJjXg_Wi02ZyiP6E1PJ0mmilizp745_fazgzxu&s", fanart = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9PrWdcYR2t0pJjXg_Wi02ZyiP6E1PJ0mmilizp745_fazgzxu&s",  folder = False )


def playvids_Pornstars(params):
    plugintools.log("choposex.clasicos_del_cine")

    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]---------------------[COLOR fuchsia]playvids[COLOR yellow]---------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9PrWdcYR2t0pJjXg_Wi02ZyiP6E1PJ0mmilizp745_fazgzxu&s", fanart = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9PrWdcYR2t0pJjXg_Wi02ZyiP6E1PJ0mmilizp745_fazgzxu&s",  folder = False )
    plugintools.set_view(plugintools.MOVIES,502)
    url = params.get("url")
    thumbnail = params.get("thumbnail")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers( url, headers=request_headers)
    if six.PY3==True:
        url = body.strip().decode('utf-8')
    else:
        url = body.strip() 

    matches = plugintools.find_multiple_matches(url,'<div class="card-img">.*?</div>')
    for generos in matches:
        titulo = plugintools.find_single_match(generos,' alt="(.*?)"')
        url1 = plugintools.find_single_match(generos,'a  href="(.*?)"')
        url = 'https://www.playvids.com'+url1
        foto = plugintools.find_single_match(generos,'src="(.*?)"')
        plugintools.add_item(action = "playvids_Trending" , title ="[B][LOWERCASE][CAPITALIZE][COLOR gold]"+titulo+"[/B][/COLOR][/CAPITALIZE][/LOWERCASE]", thumbnail =foto, fanart =foto, url =url, folder=True )
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]---------------------[COLOR fuchsia]playvids[COLOR yellow]---------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9PrWdcYR2t0pJjXg_Wi02ZyiP6E1PJ0mmilizp745_fazgzxu&s", fanart = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9PrWdcYR2t0pJjXg_Wi02ZyiP6E1PJ0mmilizp745_fazgzxu&s",  folder = False )

def playvids_subcategorias(params):
    plugintools.log("choposex.clasicos_del_cine")

    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]---------------------[COLOR fuchsia]playvids[COLOR yellow]---------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9PrWdcYR2t0pJjXg_Wi02ZyiP6E1PJ0mmilizp745_fazgzxu&s", fanart = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9PrWdcYR2t0pJjXg_Wi02ZyiP6E1PJ0mmilizp745_fazgzxu&s",  folder = False )
    plugintools.set_view(plugintools.MOVIES,502)
    url = params.get("url")
    thumbnail = params.get("thumbnail")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers( url, headers=request_headers)
    if six.PY3==True:
        url = body.strip().decode('utf-8')
    else:
        url = body.strip() 

    matches = plugintools.find_multiple_matches(url,'<li>.*?<a href=".*?">.*?</a>')
    for generos in matches:
        url1 = plugintools.find_single_match(generos,'<a href="(.*?)"')
        url = 'https://www.playvids.com'+url1
        titulo = plugintools.find_single_match(generos,'<a href=".*?">.*?\s*(.*?\n)')
        plugintools.add_item(action = "playvids_Trending" , title ="[B][LOWERCASE][CAPITALIZE][COLOR gold]"+titulo+"[/B][/COLOR][/CAPITALIZE][/LOWERCASE]", thumbnail =thumbnail, fanart =thumbnail, url =url, folder=True )

    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]---------------------[COLOR fuchsia]playvids[COLOR yellow]---------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9PrWdcYR2t0pJjXg_Wi02ZyiP6E1PJ0mmilizp745_fazgzxu&s", fanart = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9PrWdcYR2t0pJjXg_Wi02ZyiP6E1PJ0mmilizp745_fazgzxu&s",  folder = False )


def playvids_categorias(params):
    plugintools.log("choposex.clasicos_del_cine")

    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]---------------------[COLOR fuchsia]playvids[COLOR yellow]---------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9PrWdcYR2t0pJjXg_Wi02ZyiP6E1PJ0mmilizp745_fazgzxu&s", fanart = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9PrWdcYR2t0pJjXg_Wi02ZyiP6E1PJ0mmilizp745_fazgzxu&s",  folder = False )
    plugintools.set_view(plugintools.MOVIES,502)
    url = params.get("url")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers( url, headers=request_headers)
    if six.PY3==True:
        url = body.strip().decode('utf-8')
    else:
        url = body.strip() 

    matches = plugintools.find_multiple_matches(url,'<div class="card-img">.*?</div>')
    for generos in matches:
        url1 = plugintools.find_single_match(generos,'<a href="(.*?)"')
        url = 'https://www.playvids.com'+url1
        foto = plugintools.find_single_match(generos,'src="(.*?)"')
        titulo = plugintools.find_single_match(generos,'alt="(.*?)"')
        plugintools.add_item(action = "playvids_Trending" , title ="[B][LOWERCASE][CAPITALIZE][COLOR gold]"+titulo+"[/B][/COLOR][/CAPITALIZE][/LOWERCASE]", thumbnail =foto, fanart =foto, url =url, folder=True )
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]---------------------[COLOR fuchsia]playvids[COLOR yellow]---------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9PrWdcYR2t0pJjXg_Wi02ZyiP6E1PJ0mmilizp745_fazgzxu&s", fanart = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9PrWdcYR2t0pJjXg_Wi02ZyiP6E1PJ0mmilizp745_fazgzxu&s",  folder = False )

def playvids_Trending(params):
    plugintools.log("choposex.clasicos_del_cine")

    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]---------------------[COLOR fuchsia]playvids[COLOR yellow]---------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9PrWdcYR2t0pJjXg_Wi02ZyiP6E1PJ0mmilizp745_fazgzxu&s", fanart = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9PrWdcYR2t0pJjXg_Wi02ZyiP6E1PJ0mmilizp745_fazgzxu&s",  folder = False )
    plugintools.set_view(plugintools.MOVIES,502)
    url = params.get("url")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers( url, headers=request_headers)
    if six.PY3==True:
        url = body.strip().decode('utf-8')
    else:
        url = body.strip() 
    siguiente = plugintools.find_single_match(url,'rel="next" href="(.*?)"')
    matches = plugintools.find_multiple_matches(url,'class="card thumbs_rotate itemVideo.*?</div>')
    for generos in matches:
        url1 = plugintools.find_single_match(generos,'<a href="(.*?)"')
        url = 'https://www.playvids.com'+url1
        foto = plugintools.find_single_match(generos,'src="(.*?)"')
        titulo = plugintools.find_single_match(generos,'alt="(.*?)"')
        plugintools.add_item(action = "server" , title ="[B][LOWERCASE][CAPITALIZE][COLOR gold]"+titulo+"[/B][/COLOR][/CAPITALIZE][/LOWERCASE]", thumbnail =foto, fanart =foto, url =url, folder=True )
    if 'http' in siguiente:
        plugintools.add_item( action="playvids_Trending" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]ir a la pagina siguiente[/B][/COLOR][/CAPITALIZE][/LOWERCASE]", url= siguiente, thumbnail = "https://www.periodicoelpunto.com/wp-content/uploads/2019/03/flecha-siguiente.png",fanart = "https://www.periodicoelpunto.com/wp-content/uploads/2019/03/flecha-siguiente.png", folder=True )
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]---------------------[COLOR fuchsia]playvids[COLOR yellow]---------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9PrWdcYR2t0pJjXg_Wi02ZyiP6E1PJ0mmilizp745_fazgzxu&s", fanart = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9PrWdcYR2t0pJjXg_Wi02ZyiP6E1PJ0mmilizp745_fazgzxu&s",  folder = False )





def playvids_brazzers(params):
    plugintools.log("choposex.clasicos_del_cine")

    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]---------------------[COLOR fuchsia]playvids[COLOR yellow]---------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9PrWdcYR2t0pJjXg_Wi02ZyiP6E1PJ0mmilizp745_fazgzxu&s", fanart = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9PrWdcYR2t0pJjXg_Wi02ZyiP6E1PJ0mmilizp745_fazgzxu&s", folder = False )
    plugintools.set_view(plugintools.MOVIES,502)
    url = params.get("url")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers( url, headers=request_headers)
    if six.PY3==True:
        url = body.strip().decode('utf-8')
    else:
        url = body.strip() 
    siguiente = plugintools.find_single_match(url,'rel="next" href="(.*?)"')
    matches = plugintools.find_multiple_matches(url,'<div id="row_item_.*?</div>')
    for generos in matches:
        url1 = plugintools.find_single_match(generos,'<a href="(.*?)"')
        url = 'https://www.playvids.com'+url1
        foto = plugintools.find_single_match(generos,'src="(.*?)"')
        titulo = plugintools.find_single_match(generos,'alt="(.*?)"')
        plugintools.add_item(action = "server" , title ="[B][LOWERCASE][CAPITALIZE][COLOR gold]"+titulo+"[/B][/COLOR][/CAPITALIZE][/LOWERCASE]", thumbnail =foto, fanart =foto, url =url, folder=True )
    if 'http' in siguiente:
        plugintools.add_item( action="playvids_brazzers" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]ir a la pagina siguiente[/B][/COLOR][/CAPITALIZE][/LOWERCASE]", url= siguiente, thumbnail = "https://www.periodicoelpunto.com/wp-content/uploads/2019/03/flecha-siguiente.png",fanart = "https://www.periodicoelpunto.com/wp-content/uploads/2019/03/flecha-siguiente.png", folder=True )
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]---------------------[COLOR fuchsia]playvids[COLOR yellow]---------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9PrWdcYR2t0pJjXg_Wi02ZyiP6E1PJ0mmilizp745_fazgzxu&s", fanart = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9PrWdcYR2t0pJjXg_Wi02ZyiP6E1PJ0mmilizp745_fazgzxu&s",  folder = False )

def server(params):
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]---------------------[COLOR fuchsia]elige la calidad[COLOR yellow]---------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9PrWdcYR2t0pJjXg_Wi02ZyiP6E1PJ0mmilizp745_fazgzxu&s", fanart = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9PrWdcYR2t0pJjXg_Wi02ZyiP6E1PJ0mmilizp745_fazgzxu&s",  folder = False )
    url = params.get("url")
    thumbnail = params.get("thumbnail")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers( url, headers=request_headers)
    if six.PY3==True:
        url = body.strip().decode('utf-8')
    else:
        url = body.strip() 
    matches = plugintools.find_multiple_matches(url,' data-hls-src.*?=".*?" ')
    for generos in matches:
        calidad = plugintools.find_single_match(generos,'data-hls-src(.*?)="')
        url = plugintools.find_single_match(generos,'data-hls-src.*?="(.*?)"').replace("amp;", "")
        plugintools.add_item(action = "play_links" , title =calidad, thumbnail =thumbnail, fanart =thumbnail, url =url, folder=False,  isPlayable = True )
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]---------------------[COLOR fuchsia]elige la calidad[COLOR yellow]---------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9PrWdcYR2t0pJjXg_Wi02ZyiP6E1PJ0mmilizp745_fazgzxu&s", fanart = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9PrWdcYR2t0pJjXg_Wi02ZyiP6E1PJ0mmilizp745_fazgzxu&s",  folder = False )



#--------------playvids-----------------------playvids----------------------playvids-----------------------------playvids--------------------playvids#--------------playvids-----------------------playvids----------------------playvids-----------------------------playvids--------------------playvids #--------------playvids-----------------------playvids----------------------playvids-----------------------------playvids--------------------playvids #--------------playvids-----------------------playvids----------------------playvids-----------------------------playvids--------------------playvids #--------------playvids-----------------------playvids----------------------playvids-----------------------------playvids--------------------playvids #--------------playvids-----------------------playvids----------------------playvids-----------------------------playvids--------------------playvids #--------------playvids-----------------------playvids----------------------playvids-----------------------------playvids--------------------playvids #--------------playvids-----------------------playvids----------------------playvids-----------------------------playvids--------------------playvids #--------------playvids-----------------------playvids----------------------playvids-----------------------------playvids--------------------playvids




#---------------------------------------------------------reproducir--RESOLVERURL-------------------------------------------------------------------#---------------------------------------------------------reproducir--RESOLVERURL-------------------------------------------------------------------
#---------------------------------------------------------reproducir--RESOLVERURL-------------------------------------------------------------------#---------------------------------------------------------reproducir--RESOLVERURL-------------------------------------------------------------------#---------------------------------------------------------reproducir--RESOLVERURL-------------------------------------------------------------------#---------------------------------------------------------reproducir--RESOLVERURL-------------------------------------------------------------------#---------------------------------------------------------reproducir--RESOLVERURL-------------------------------------------------------------------#---------------------------------------------------------reproducir--RESOLVERURL-------------------------------------------------------------------#---------------------------------------------------------reproducir--RESOLVERURL-------------------------------------------------------------------#---------------------------------------------------------reproducir--RESOLVERURL-------------------------------------------------------------------#---------------------------------------------------------reproducir--RESOLVERURL-------------------------------------------------------------------#---------------------------------------------------------reproducir--RESOLVERURL-------------------------------------------------------------------

def play_links(params):
    try:
        plugintools.play_resolved_url( params.get("url") )

    except:
        u= xbmc.executebuiltin('XBMC.Notification([B][LOWERCASE][CAPITALIZE][COLOR white]enlace  [COLOR red]borrado [/CAPITALIZE][/LOWERCASE][/B][/COLOR],[B][LOWERCASE][CAPITALIZE][COLOR white]elige otro [/CAPITALIZE][/LOWERCASE][/B][/COLOR], 4000)')
        plugintools.add_item(action = "servidores" , title = u,  folder = True )
def play_resolver(params):
    import resolveurl
    try:
        video = resolveurl.resolve( params.get("url") )
        plugintools.play_resolved_url( video )
    except:
        u= xbmc.executebuiltin('XBMC.Notification([B][LOWERCASE][CAPITALIZE][COLOR white]enlace  [COLOR red]borrado [/CAPITALIZE][/LOWERCASE][/B][/COLOR],[B][LOWERCASE][CAPITALIZE][COLOR white]elige otro [/CAPITALIZE][/LOWERCASE][/B][/COLOR], 4000)')
        plugintools.add_item(action = "servidores" , title = u,  folder = True )



#---------------------------------------------------------reproducir--RESOLVERURL-------------------------------------------------------------------#---------------------------------------------------------reproducir--RESOLVERURL-------------------------------------------------------------------
#---------------------------------------------------------reproducir--RESOLVERURL-------------------------------------------------------------------#---------------------------------------------------------reproducir--RESOLVERURL-------------------------------------------------------------------#---------------------------------------------------------reproducir--RESOLVERURL-------------------------------------------------------------------#---------------------------------------------------------reproducir--RESOLVERURL-------------------------------------------------------------------#---------------------------------------------------------reproducir--RESOLVERURL-------------------------------------------------------------------#---------------------------------------------------------reproducir--RESOLVERURL-------------------------------------------------------------------#---------------------------------------------------------reproducir--RESOLVERURL-------------------------------------------------------------------#---------------------------------------------------------reproducir--RESOLVERURL-------------------------------------------------------------------#---------------------------------------------------------reproducir--RESOLVERURL-------------------------------------------------------------------#---------------------------------------------------------reproducir--RESOLVERURL-------------------------------------------------------------------


run()