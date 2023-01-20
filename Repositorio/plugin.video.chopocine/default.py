# -*- coding: utf-8 -*-
#------------------------------------------------------------
# chopodplay - XBMC Add-on by Torete
# Version 0.2.5 (15.05.2014)
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Gracias a la librería plugintools de Jesús (www.mimediacenter.info)
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
addonname = '[B][LOWERCASE][CAPITALIZE][COLOR white]choposeries[/CAPITALIZE][/LOWERCASE][/B][/COLOR]'
icon = addon.getAddonInfo('icon')
myaddon = xbmcaddon.Addon("plugin.video.chopocine")
Set_Color = myaddon.getSetting('SetColor')
Set_View = myaddon.getSetting('SetView')
local_remote = '1'
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

 

 
#menu principal----------------------- menu principal----------------------- menu principal----------------------- menu principal----------------------- menu principal----------------------- menu principal----------------------- menu principal----------------------- menu principal----------------------- menu principal----------------------- menu principal----------------------- menu principal----------------------- menu principal----------------------- menu principal----------------------- menu principal----------------------- menu principal----------------------- menu principal----------------------- menu principal----------------------- menu principal----------------------- menu principal----------------------- menu principal----------------------- menu principal----------------------- menu principal----------------------- menu principal----------------------- menu principal----------------------- menu principal----------------------- menu principal----------------------- menu principal----------------------- menu principal----------------------- menu principal----------------------- menu principal----------------------- menu principal----------------------- menu principal----------------------- menu principal----------------------- menu principal----------------------- 
def cookie():
    import re,base64
    import requests
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8","Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3","Content-Type": "application/x-www-form-urlencoded", "Upgrade-Insecure-Requests": "1","Pragma": "no-cache","Cache-Control": "no-cache"}
 
    url = "https://www.croxyproxy.rocks/requests?fso="
 
    payload = {'url':'https://www.gnula2.co/estrenos/','proxyServerId':'94','demo':'0','frontOrigin':'https://www.croxyproxy.rocks'}
    x = requests.post(url,headers=headers,data=payload,verify=False)
    return(x.headers['set-cookie'])
try:
    cookies=cookie()
except:
    cookies=''
def activar_proxy(params):
    s='' 
    if six.PY3==True:
        t = urllib.request.urlopen(urllib.request.Request("https://pastebin.com/raw/nUgxp2gN")).read().decode('utf-8')
    else:
        t=urllib2.urlopen(urllib2.Request("https://pastebin.com/raw/nUgxp2gN")).read()
    favoritos = xbmc.translatePath('special://home/addons/plugin.video.chopocine/t.py')
    f = open(favoritos,'w+')
    f.write(t)
    f.close()
    s=''    
    def proxy(s):
        import xbmc
        import xbmcgui
        import webbrowser
        import t
        return '{0}'.format(t.main())
    proxys=proxy(s)
    if '.' in proxys:
        u='[B][LOWERCASE][CAPITALIZE][COLOR lime]proxy valido encontrado dar aqui para activarlo[/CAPITALIZE][/LOWERCASE][/B][/COLOR]'
        dialog = xbmcgui.Dialog()
        dialog.textviewer('[B][COLOR yellow]INSTRUCCIONES:[/COLOR][/B]', '[B][CAPITALIZE][COLOR aqua] AHORA ACTIVAS EL PROXY ENCONTRADO\nY COMPRUEBA LAS SECCIONES QUE LO NECESITAN\nSI ES LENTO O NO ABRE LA SECCION\nHACEMOS DE NUEVO LA BUSQUEDA DE PROXY\nNO TODOS LOS PROXYS ENCONTRADOS NOS VALDRAN\n[COLOR aqua]DUDAS Y PREGUNTAS  [COLOR yellow]TELEGRAM @TVCHOPO[/COLOR][/CAPITALIZE][/B] ') 
        plugintools.add_item(action = "main_list" ,title=u, extra = proxys,  folder = True )
    else:
        u='[B][LOWERCASE][CAPITALIZE][COLOR red]no encontrado ningun proxy valido.. prueba de nuevo[/CAPITALIZE][/LOWERCASE][/B][/COLOR]'
        plugintools.add_item(action = "activar_proxy" ,title=u,   folder = False )
def main_list(params):
    plugintools.log("chopocine.main_list ")    
    plugintools.set_view(plugintools.LIST)  

#peliswebs----------------#peliswebs----------------#peliswebs----------------#peliswebs----------------#peliswebs----------------#peliswebs----------------#peliswebs----------------#peliswebs----------------#peliswebs----------------#peliswebs----------------#peliswebs----------------#peliswebs----------------#peliswebs----------------#peliswebs----------------#peliswebs----------------
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]ADDON VALIDO PARA KODI 18 Y 19 [/COLOR][/CAPITALIZE][/LOWERCASE][/B]",  thumbnail ="https://enfilme.com/img/content/newhollywoodalgarabia_Enfilme_30h24_675_489.jpg", fanart ="https://www.unir.net/wp-content/uploads/2019/09/foto-hollywood-guion-unir.jpg", url="https://pastebin.com/raw/3YLJFMXK", folder = False ) 
    plugintools.add_item(action="", title="[B][COLOR orange]TELEGRAM [COLOR yellow]@tvchopo[/COLOR][/B]",thumbnail="https://i.imgur.com/oCst1B7.jpg", fanart="https://colegasdelorden.com/wp-content/uploads/2021/05/Telegram-Emblema.png",  url= "",folder= False ) 


 
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]--------[COLOR yellow]addon chopocine[COLOR aqua]--------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://i.imgur.com/9a16ENI.jpg", fanart = "https://i.imgur.com/9a16ENI.jpg",  folder = False )  
 
    plugintools.add_item(action="nuestros_addons", title="[B][COLOR white]accede a nuestros addons desde aqui[/B][/COLOR]",thumbnail="https://i.imgur.com/m4jQxam.jpg", fanart="https://i.imgur.com/m4jQxam.jpg",  url= "https://www.documaniatv.com/newvideos.html",folder= True )
    

 
 
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]----------------- [COLOR aqua] web de pelis [COLOR yellow]-----------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://i.imgur.com/9a16ENI.jpg", fanart = "https://i.imgur.com/9a16ENI.jpg",  folder = False ) 

    plugintools.add_item(action = "mega_busca" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]megabuscador [COLOR lime]¡¡[COLOR gold]en todas las webs a la vez[COLOR lime]!! [COLOR gold][/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color,  thumbnail ="https://i.imgur.com/sLNFVk7.jpg", fanart ="https://i.imgur.com/4s19wsT.jpg", url="https://descargacineclasico.net/", folder = True ) 
    plugintools.add_item(action = "menu_gnula" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]gnula [/COLOR][/CAPITALIZE][/LOWERCASE][/B]"% Set_Color, thumbnail ="https://i.imgur.com/pm9MmeF.jpg", fanart ="https://i.imgur.com/X8DiYut.jpg", url='', folder = True )    

    plugintools.add_item(action = "menu_cuevana3" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]cuevana3[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color, thumbnail ="https://idescargar.com/wp-content/uploads/2019/09/cuevana-3-3.jpg", fanart = "https://www.fondoswiki.com/Uploads/fondoswiki.com/ImagenesGrandes/imagen-avatar.jpg", url='https://www.gnula2.co/', folder = True )     


 
    plugintools.add_item(action = "repelis_menu" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]repelis[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color, thumbnail ="https://s3.amazonaws.com/podcasts-image-uploads/nuevo-online-en-espanol-latino-600x600.png", fanart ="https://img.scoop.it/uipR2D6JTUIKefEqbCGZqzl72eJkfbmt4t8yenImKBVvK0kTmF0xjctABnaLJIm9",extra="https://img.scoop.it/uipR2D6JTUIKefEqbCGZqzl72eJkfbmt4t8yenImKBVvK0kTmF0xjctABnaLJIm9", url='', folder = True )
 
 
 
#peliswebs----------------#peliswebs----------------#peliswebs----------------#peliswebs----------------#peliswebs----------------#peliswebs----------------#peliswebs----------------#peliswebs----------------#peliswebs----------------#peliswebs----------------#peliswebs----------------#peliswebs----------------#peliswebs----------------#peliswebs----------------#peliswebs----------------#peliswebs----------------
 
 
 
 
 #especiales , sagas----------------- #especiales , sagas-----------------  #especiales , sagas-----------------  #especiales , sagas-----------------  #especiales , sagas-----------------  #especiales , sagas-----------------  #especiales , sagas-----------------  #especiales , sagas-----------------  #especiales , sagas-----------------  #especiales , sagas-----------------  #especiales , sagas-----------------  #especiales , sagas-----------------  #especiales , sagas-----------------  #especiales , sagas-----------------  #especiales , sagas-----------------  #especiales , sagas-----------------  #especiales , sagas-----------------  #especiales , sagas-----------------  #especiales , sagas-----------------  #especiales , sagas-----------------  #especiales , sagas-----------------  #especiales , sagas-----------------    
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]----------------- [COLOR aqua]sagas, especiales, y mas.. [COLOR yellow]-----------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",thumbnail ="https://i.imgur.com/9a16ENI.jpg", fanart = "https://i.imgur.com/9a16ENI.jpg",  folder = False ) 
    
    plugintools.add_item(action = "PRODUCTORAS" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s] cine por productoras [/COLOR][/CAPITALIZE][/LOWERCASE][/B]"% Set_Color,  thumbnail ="https://vertele.eldiario.es/2019/10/31/noticias/Amazon-Netflix-Apple-TV-Espana_2172692762_14050592_660x371.jpg", fanart = "https://e00-marca.uecdn.es/assets/multimedia/imagenes/2020/11/20/16058878063470.jpg", page='1', folder = True )  
 
    plugintools.add_item(action = "cien_mejores_sagas" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s] LAS 101 MEJORES SAGAS [/COLOR][/CAPITALIZE][/LOWERCASE][/B]"% Set_Color, thumbnail ="https://www.alvarocuevas.es/wp-content/uploads/2021/01/Las-mejores-sagas-de-peliculas.jpg",fanart = "https://media.vandalsports.com/master/6-2021/2021629471_1.jpg",  folder = True )     
 

 
    plugintools.add_item(action = "oscar_actores" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s] pelis ganadoras del Oscar a la mejor película [/COLOR][/CAPITALIZE][/LOWERCASE][/B]"% Set_Color,  thumbnail="https://i0.wp.com/www.moonmagazine.info/wp-content/uploads/2020/02/rumbo-al-oscar-2020-cual-sera-la-mejor-pelicula-8.png?resize=1140%2C641&ssl=1",fanart="https://drraa3ej68s2c.cloudfront.net/wp-content/uploads/2020/01/07082647/eeaf9e7342a0d077a20f395dfcb8791e3d240e5afc2b69f74870afcac3979626.jpg",url='https://decine21.com/listas-de-cine/lista/todas-las-peliculas-ganadoras-del-oscar-a-la-mejor-pelicula-100163', folder = True ) 

    plugintools.add_item(action = "mejores_peliculas" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s] las mejores peliculas de.. [/COLOR][/CAPITALIZE][/LOWERCASE][/B]"% Set_Color,  thumbnail="https://w7.pngwing.com/pngs/90/19/png-transparent-film-cinema-movies-miscellaneous-text-logo.png",fanart="https://w7.pngwing.com/pngs/768/177/png-transparent-graphic-film-computer-hardware-automotive-lighting-design-photography-film-camera-accessory.png",url='https://decine21.com/listas-de-cine/lista/todas-las-peliculas-ganadoras-del-oscar-a-la-mejor-pelicula-100163', folder = True )

 
    plugintools.add_item(action = "filmografias" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s] filmografias completas[/COLOR][/CAPITALIZE][/LOWERCASE][/B]"% Set_Color,  thumbnail="https://www.nicepng.com/png/detail/341-3412483_te-invita-al-cine-carrete-de-pelicula-png.png",fanart="https://images5.alphacoders.com/351/thumb-1920-351364.jpg",url='https://sobreelmundodelcine.com/biografias-de-actores-y-actrices/', folder = True ) 

    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]----------------- [COLOR aqua]pelis españolas.. [COLOR yellow]-----------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",thumbnail ="https://i.imgur.com/9a16ENI.jpg", fanart = "https://i.imgur.com/9a16ENI.jpg",  folder = False )    
 
    plugintools.add_item(action = "cine_kinki" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s] cine kinki[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color,  thumbnail ="https://i.ytimg.com/vi/gom1cQNshzo/hqdefault.jpg",fanart = "http://3.bp.blogspot.com/-ABfKzNTa8zo/V_uZANGZ-rI/AAAAAAAAKXI/y2WMvfjL3CwV7hyRPz2VlU7pbVEEI49bACK4B/s1600/foto.jpg",url = "https://zoowoman.website/wp/genre/cine-quinqui/",   folder = True )    
 
 
    plugintools.add_item(action = "cine_espanol" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s] cine  [COLOR gold]español[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color,  thumbnail ="https://lapublicidad.net/wp-content/uploads/2022/10/J2KQGULE4ND77FOYZVAJYZCN7E.png", fanart = "https://www.cope.es/blogs/palomitas-de-maiz/wp-content/uploads/sites/6/2020/01/cine-espa%C3%B1ol.jpg",  folder = True )
 
 
   
 
 
 
    plugintools.add_item(action = "pelis_you" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s] Películas españolas clásicas[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color,  thumbnail ="https://i.pinimg.com/474x/d6/5c/42/d65c426b3de0679aecc15868aa067d6e.jpg",fanart = "https://i.pinimg.com/474x/d6/5c/42/d65c426b3de0679aecc15868aa067d6e.jpg",url='https://www.youtube.com/watch?v=OVjZTR0w_n4&list=PLhgZbivoHwSViCGE5ljvi8cYTgouloz_-', folder=True )  
 
 
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]----------------- [COLOR aqua]cine clasico.. [COLOR yellow]-----------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",thumbnail ="https://i.imgur.com/9a16ENI.jpg", fanart = "https://i.imgur.com/9a16ENI.jpg",  folder = False )
    
    plugintools.add_item(action = "clasicos_del_cine" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s] el baul del cine [COLOR gold]todas[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color,  thumbnail ="https://d3b5jqy5xuub7g.cloudfront.net/wp-content/uploads/2018/11/CineClasico-1.jpg", fanart ="https://www.unir.net/wp-content/uploads/2019/09/foto-hollywood-guion-unir.jpg", url="https://95.216.8.160/peliculas/?__cpo=aHR0cHM6Ly9vbmxpbmUudHVjaW5lY2xhc2ljby5lcw", folder = True )  
 

    plugintools.add_item(action = "clasicos_del_cine_generos" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s] el baul del cine [COLOR gold]generos[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color,  thumbnail ="https://d3b5jqy5xuub7g.cloudfront.net/wp-content/uploads/2018/11/CineClasico-1.jpg", fanart ="https://www.unir.net/wp-content/uploads/2019/09/foto-hollywood-guion-unir.jpg", url="https://95.216.8.160/peliculas/?__cpo=aHR0cHM6Ly9vbmxpbmUudHVjaW5lY2xhc2ljby5lcw", folder = True ) 
 
    plugintools.add_item(action = "clasicos_del_cine_busca" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s] el baul del cine [COLOR gold]buscador[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color,  thumbnail ="https://d3b5jqy5xuub7g.cloudfront.net/wp-content/uploads/2018/11/CineClasico-1.jpg", fanart ="https://www.unir.net/wp-content/uploads/2019/09/foto-hollywood-guion-unir.jpg", url="https://descargacineclasico.net/", folder = True )     
 
    plugintools.add_item(action = "pelis_you" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s] Películas de cine clásico[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color,  thumbnail ="https://d3bjfa2fjkx310.cloudfront.net/test/8ee1ba6699378be2a9c45269f7666188.jpeg",fanart = "https://d3bjfa2fjkx310.cloudfront.net/test/8ee1ba6699378be2a9c45269f7666188.jpeg",url='https://www.youtube.com/watch?v=_ppHqkSS_uQ&list=PL5Elc2OLiWk6pkscyMTC6DCbE4GIeqfAe', folder=True ) 

    plugintools.add_item(action = "ciclos_de_cine" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s] ciclos de cine [/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color,  thumbnail ="https://thumbs.dreamstime.com/b/logotipo-de-c%C3%A1mara-v%C3%ADdeo-vintage-para-el-proyecto-cine-o-203577152.jpg", fanart ="https://www.cabdeburgos.com/img/upload/ciclo_cine_1_slider_cab.jpg", url="https://95.216.8.160/category/ciclos-de-cine-clasico/?__cpo=aHR0cHM6Ly90dWNpbmVjbGFzaWNvLmVz", folder = True )  

    plugintools.add_item(action = "pelis_de_los_80_90" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s] pelis de los años 80 y 90[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color,  thumbnail ="https://www.alucine.es/wp-content/uploads/2015/03/341.jpg", fanart = "https://www.lacabecita.com/wp-content/uploads/90s.png",  folder = True ) 

    plugintools.add_item(action = "pelis_you" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s] Películas de bud spencer y Terence Hill[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color,  thumbnail ="https://i.imgur.com/M0tEdLG.jpg",fanart = "https://i.imgur.com/BEAJ9Vr.jpg",url='https://www.youtube.com/watch?v=PuMlIOHBaqg&list=PLy-qmp54bpB2yopTCH_4G5WLnniNQerQf', folder=True ) 
 
    plugintools.add_item(action = "pelis_you" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s] Películas de cantinflas[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color,  thumbnail ="https://i.pinimg.com/736x/7d/0c/14/7d0c147fbe15039a153756b653911e1e.jpg",fanart = "https://www.sectorcine.com/wp-content/uploads/2020/04/cantinflas-peli%CC%81culas.jpg",url='https://www.youtube.com/watch?v=U5neiehwYMk&list=PLEN1o4MXDPxA-o78qTZRqEU-XgRUyh76u', folder=True )
 
    plugintools.add_item(action = "pelis_you" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s] Películas del Oeste[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color,  thumbnail ="https://i.pinimg.com/originals/88/5b/73/885b737ec111ec20cdbf8ea47dab591a.jpg",fanart = "https://www.diariocritico.com/fotos/grupo.jpg",url='https://www.youtube.com/watch?v=1g_SGZn4_-c&list=PLLxxgrF1QnBjEvwkfWLPkr-CLEeEHJuWl', folder=True ) 
 

 
    plugintools.add_item(action = "list_you" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s] CLASICOS TORAYMAR [/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color,  thumbnail ="https://s3.eu-central-1.amazonaws.com/images.jacksonlive.es/upload/spots/high/1397241495.jpg",fanart = "https://es-cdn.kinepolis.com/sites/kinepolis.es/files/styles/general_item_big/public/general_page/image/web1_clasicos_460x250px.jpg?itok=7eb2c0zn",url='https://www.youtube.com/channel/UCqcgpX5JKYDSGAXCLdB6SNg/playlists', folder=True ) 
 

 

 
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]--------[COLOR yellow]addon chopocine[COLOR aqua]--------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://i.imgur.com/9a16ENI.jpg", fanart = "https://i.imgur.com/9a16ENI.jpg",  folder = False ) 
 
def nuestros_addons(params):
    plugintools.log("tvchopo.MEDICITV_menu ")   
    thumbnail = params.get("thumbnail")   
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]--------[COLOR aqua]nuestros addons[COLOR yellow]--------[/COLOR][/CAPITALIZE][/LOWERCASE][/B]", thumbnail ='https://i.imgur.com/FuFnLjS.jpg', fanart ='https://i.imgur.com/FuFnLjS.jpg',  folder = False )

    plugintools.add_item( action="plugin://plugin.video.chopocine", title="[B][LOWERCASE][CAPITALIZE][COLOR white]chopocine [/COLOR][/CAPITALIZE][/LOWERCASE][/B]", thumbnail="https://i.imgur.com/uZGkK64.jpg", fanart="https://i.imgur.com/4s19wsT.jpg",url='plugin://plugin.video.chopocine',folder=True )   
    plugintools.add_item( action="plugin://plugin.video.choposeries", title="[B][LOWERCASE][CAPITALIZE][COLOR white]CHOPOSERIES [/COLOR][/CAPITALIZE][/LOWERCASE][/B]", thumbnail="https://i.imgur.com/CRhUqF1.jpg", fanart="https://i.imgur.com/CRhUqF1.jpg",url='plugin://plugin.video.choposeries',folder=True ) 
 
    plugintools.add_item(action="plugin://plugin.video.mitelechopo", title="[B][LOWERCASE][CAPITALIZE][COLOR white]mitele[COLOR gold] chopo[/COLOR][/CAPITALIZE][/LOWERCASE][/B]",thumbnail="https://i.imgur.com/QBeSVbu.jpg", fanart="https://i.imgur.com/QBeSVbu.jpg",  url= "plugin://plugin.video.mitelechopo",folder= True ) 
 
 
    plugintools.add_item(action="plugin://plugin.video.atresplayerchopo", title="[B][LOWERCASE][CAPITALIZE][COLOR white]atresplayer [COLOR gold]chopo[/COLOR][/CAPITALIZE][/LOWERCASE][/B]",thumbnail="https://i.imgur.com/Xt1xuef.jpg", fanart="https://imagenes.atresplayer.com/atp/clipping/cmsimages01/2018/01/24/3A62BD1C-A059-40B1-8688-8BECED7D41A7/1280x720.jpg",  url= "plugin://plugin.video.atresplayerchopo",folder= True )     
 
    plugintools.add_item( action="plugin://plugin.video.emuchopo", title="[B][LOWERCASE][CAPITALIZE][COLOR white]emu[COLOR aqua]chopo[/COLOR][/CAPITALIZE][/LOWERCASE][/B]", thumbnail = 'https://i.imgur.com/LsV3BxT.jpg', fanart='https://i.imgur.com/tSf8bhl.jpg',url='plugin://plugin.video.emuchopo',folder=True )  
 
    plugintools.add_item( action="plugin://plugin.video.koditv", title="[B][LOWERCASE][CAPITALIZE][COLOR white]kodi[COLOR aqua]tv[/COLOR][/CAPITALIZE][/LOWERCASE][/B]", thumbnail="https://i.imgur.com/F4rPD1M.jpg", fanart="https://i.imgur.com/P7VIG6b.jpg",url='plugin://plugin.video.koditv',folder=True )    
 
    plugintools.add_item( action="plugin://plugin.video.choposex", title="[B][LOWERCASE][CAPITALIZE][COLOR white]chopo[COLOR fuchsia]sex [/COLOR][/CAPITALIZE][/LOWERCASE][/B]", thumbnail="https://i.imgur.com/rzp0C9t.jpg", fanart="https://i.imgur.com/UaAQEbB.jpg",url='plugin://plugin.video.choposex',folder=True )  
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]dudas o problemas..[COLOR aqua]telegram [COLOR yellow]@tvchopo[/COLOR][/CAPITALIZE][/LOWERCASE][/B]", thumbnail ='https://i.imgur.com/FuFnLjS.jpg', fanart ='https://i.imgur.com/FuFnLjS.jpg',  folder = False )             
 
 
 
 
 

 
 
def mejores_peliculas(params):  

    plugintools.log("chopocine.accion_actores")
    plugintools.set_view(plugintools.LIST,50)
    thumbnail = params.get("thumbnail")

  
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]----[COLOR aqua]chopocine[COLOR yellow]----[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail =thumbnail, fanart =thumbnail,  folder = False ) 
    url = 'https://decine21.com/listas-de-cine/listas?limit=290'
    def sucuri(url):
        import re,base64
        import requests
        import xbmc, xbmcaddon
        headers= {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0","Cookie":cookies}

        x = requests.get(url,headers=headers,verify=False)  
        if six.PY3==True :             
            return x.text
        else :             
            return x.content
    url= sucuri(url)

 
    matches = plugintools.find_multiple_matches(url,'(?s)class="listas-list-item col-md.*?a href="/listas-de-cine/lista/las-mejores-peliculas.*?">.*?data-src=".*?".*?title="Las mejores .*?".*?')   
    for generos in matches:
 
 
        patron= plugintools.find_single_match(generos,'(?s)class="listas-list-item col-md.*?a href="(/listas-de-cine/lista/las-mejores-peliculas.*?)">.*?data-src="(.*?)".*?title="Las mejores .*?(.*?)".*?')
        titulo=patron[2]
        foto=patron[1]

        url='https://decine21.com'+patron[0]

        plugintools.add_item(action = "oscar_actores" , title = "[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",  thumbnail =foto, fanart =foto,url =url,  folder=True )
 
  
 
 
 
 
 
 
 
 
 
def oscar_actores(params):  
    plugintools.set_view(plugintools.MOVIES,503)
    plugintools.log("chopocine.accion_actores")
    thumbnail = params.get("thumbnail")

  
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]----[COLOR aqua]chopocine[COLOR yellow]----[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail =thumbnail, fanart =thumbnail,  folder = False ) 
    url = params.get("url")
    def sucuri(url):
        import re,base64
        import requests
        import xbmc, xbmcaddon
        headers= {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0","Cookie":cookies}

        x = requests.get(url,headers=headers,verify=False)  
        if six.PY3==True :             
            return x.text
        else :             
            return x.content
    url= sucuri(url)
    try:
        pagina_siguiente= plugintools.find_single_match(url,'link href="(/listas-de-cine/lista/.*?)" rel="next" />')
    except:
        pass
 
    matches = plugintools.find_multiple_matches(url,'((?s)class="list-film card shadow mb-3">.*?alt=".*?".*?data-src=".*?".*?film-sinopsis">.*?<.*?)')   
    for generos in matches:
 
        import random
        patron= plugintools.find_single_match(generos,'(?s)class="list-film card shadow mb-3">.*?alt="(.*?)".*?data-src="(.*?)".*?film-sinopsis">(.*?)<.*?')
        titulo=patron[0]
        foto=patron[1]
        texto=patron[2]
        if six.PY3==True :
            texto=unicodedata.normalize("NFKD", texto).encode("ascii","ignore").decode("ascii")
        else:
            texto=texto
        url=patron[0].lower().replace("(2002)", "").replace("birdman (o la inesperada virtud de la ignorancia)", "birdman").replace("coda. los sonidos del silencio", "coda").replace(" ", "%20")
                  
        quitar=str(random.randrange(1900, 2022))
        if six.PY3==True :
            url=unicodedata.normalize("NFKD", url).encode("ascii","ignore").decode("ascii").replace("parasitos", "Parasite").lower().replace(".", "").replace(",", "").replace("(", "").replace(")", "").replace(":", "").replace(quitar, "")
        else :
            url=url.replace("parasitos", "Parasite").lower().replace(".", "").replace(",", "").replace("(", "").replace(")", "").replace(":", "").replace(quitar, "")
        plugintools.set_view(plugintools.MOVIES,503) 
        plugintools.add_item(action = "gnula_pelis_proveedoras" , title ="[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", plot = "[B][LOWERCASE][CAPITALIZE][COLOR white]"+texto+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail =foto, fanart =foto,url =url,  folder=True )
 

 
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]----[COLOR aqua]chopocine[COLOR yellow]----[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail =thumbnail, fanart =thumbnail,  folder = False ) 
    
    
    
def buscar_actor(params):  
    plugintools.log("chopocine.repelis_generos")
    thumbnail = params.get("thumbnail")
    fanart = params.get("extra") 
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]---------------------[COLOR aqua]repelis[COLOR yellow]---------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail =thumbnail, fanart =fanart,  folder = False ) 
    plugintools.set_view(plugintools.MOVIES,502)  
    dialog = xbmcgui.Dialog()
    d = dialog.input('[B][LOWERCASE][CAPITALIZE][COLOR orange]nombre y el apellido, ejemplo: [COLOR white]sylvester stallone[/COLOR][/CAPITALIZE][/LOWERCASE][/B]', type=xbmcgui.INPUT_ALPHANUM).replace(" ", "-")    
    plugintools.add_item(action = "filmografias2" , title ="[B][LOWERCASE][CAPITALIZE][COLOR orange]"+d+"[/COLOR][/CAPITALIZE][/LOWERCASE][/B]",  thumbnail =thumbnail, fanart =thumbnail,url =d,  folder=True )
def filmografias(params):  
 
    plugintools.log("chopocine.accion_actores")
    thumbnail = params.get("thumbnail")
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]----[COLOR aqua]chopocine[COLOR yellow]----[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail =thumbnail, fanart =thumbnail,  folder = False ) 
    
    plugintools.add_item(action = "buscar_actor" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]buscar actor o actriz aqui[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",  thumbnail =thumbnail, fanart =thumbnail,url ='',  folder=True )
    plugintools.add_item(action = "buscar_actor" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]------------------------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",  thumbnail =thumbnail, fanart =thumbnail,url ='',  folder=True )
    url = params.get("url")
    def sucuri(url):
        import re,base64
        import requests
        import xbmc, xbmcaddon
        headers= {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0","Cookie":cookies}

        x = requests.get(url,headers=headers,verify=False)  
        if six.PY3==True :             
            return x.text
        else :             
            return x.content
    url= sucuri(url)

    plugintools.add_item(action = "filmografias2" , title = "[B][LOWERCASE][CAPITALIZE][COLOR white] Sylvester Stallone[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",  thumbnail =thumbnail, fanart =thumbnail,url ='sylvester-stallone',  folder=True )
    matches = plugintools.find_multiple_matches(url,'(?s)<li><strong>.*?</strong></li>.*?|<li><a title=".*?".*?ref="https://sobreelmundodel.*?".*?">.*?<')   
    for generos in matches:
        patron = plugintools.find_single_match(generos,'(?s)<li><strong>(.*?)</strong></li>.*?|<li><a title=".*?".*?ref="https://sobreelmundodel.*?".*?">(.*?)<')
        letra=patron[0]
        titulo=patron[1]
        titulo1=titulo.replace(" ", "-")
        
   
        
 
        plugintools.add_item(action = "filmografias2" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]"+letra+"[COLOR white]"+titulo+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",  thumbnail =thumbnail, fanart =thumbnail,url =titulo1,  folder=True )
 
def filmografias2(params):  
 
    plugintools.log("chopocine.accion_actores")
    thumbnail = params.get("thumbnail")
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]----[COLOR aqua]chopocine[COLOR yellow]----[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail =thumbnail, fanart =thumbnail,  folder = False ) 
    

    url = 'https://www.elseptimoarte.net/actores/'+params.get("url")
    def sucuri(url):
        import re,base64
        import requests
        import xbmc, xbmcaddon
        headers= {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0","Cookie":cookies}

        x = requests.get(url,headers=headers,timeout=15,verify=False)  
        if six.PY3==True :             
            return x.text
        else :             
            return x.content
    url= sucuri(url)
    
    matches = plugintools.find_multiple_matches(url,'(?s)data-lazy-image="/carteles/.*?".*?<h3>.*?">.*?</a></h3>.*?<p>.*?</p>') 
    for generos in matches:
       patron = plugintools.find_single_match(generos,'(?s)data-lazy-image="(/carteles/.*?)".*?<h3>.*?">(.*?)</a></h3>.*?<p>(.*?)</p>')
       foto='https://www.elseptimoarte.net'+patron[0]
       anio=patron[2]

       titulo = patron[1].lower()
       # coding: utf-8
       titulo=str(titulo).replace("\xf1", "ñ").replace(',','').replace("\xe1", "a").replace("\xe9", "e").replace("\xed", "i").replace("\xf3", "o").replace("\xfa", "u").replace(".", "").replace("(", "").replace(")", "").replace(":", "").replace("\xc1", "a").replace("\xc9", "e").replace("\xcd", "i").replace("\xd3", "o").replace("\xda", "u")
           
       plugintools.add_item(action = "gnula_pelis_proveedoras" , title = "[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo+"  [COLOR yellow]("+anio+")[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",  thumbnail =foto, fanart =foto,url =titulo,  folder=True )  
     

 
 
 #especiales , sagas----------------- #especiales , sagas-----------------  #especiales , sagas-----------------  #especiales , sagas-----------------  #especiales , sagas-----------------  #especiales , sagas-----------------  #especiales , sagas-----------------  #especiales , sagas-----------------  #especiales , sagas-----------------  #especiales , sagas-----------------  #especiales , sagas-----------------  #especiales , sagas-----------------  #especiales , sagas-----------------  #especiales , sagas-----------------  #especiales , sagas-----------------  #especiales , sagas-----------------  #especiales , sagas-----------------  #especiales , sagas-----------------  #especiales , sagas-----------------  #especiales , sagas-----------------  #especiales , sagas-----------------  #especiales , sagas-----------------    
 
#menu principal----------------------- menu principal----------------------- menu principal----------------------- menu principal----------------------- menu principal----------------------- menu principal----------------------- menu principal----------------------- menu principal----------------------- menu principal----------------------- menu principal----------------------- menu principal----------------------- menu principal----------------------- menu principal----------------------- menu principal----------------------- menu principal----------------------- menu principal----------------------- menu principal----------------------- menu principal----------------------- menu principal----------------------- menu principal----------------------- menu principal----------------------- menu principal----------------------- menu principal----------------------- menu principal----------------------- menu principal----------------------- menu principal----------------------- menu principal----------------------- menu principal----------------------- menu principal----------------------- menu principal----------------------- menu principal----------------------- menu principal----------------------- menu principal----------------------- menu principal----------------------- 
 
 
 

 

 
 


 
 
#cuevana3----------------------------#cuevana3----------------------------#cuevana3----------------------------#cuevana3----------------------------#cuevana3----------------------------#cuevana3----------------------------#cuevana3----------------------------#cuevana3----------------------------#cuevana3----------------------------#cuevana3----------------------------#cuevana3----------------------------#cuevana3----------------------------#cuevana3----------------------------#cuevana3----------------------------#cuevana3----------------------------#cuevana3----------------------------#cuevana3----------------------------#cuevana3----------------------------#cuevana3----------------------------#cuevana3----------------------------#cuevana3----------------------------#cuevana3----------------------------#cuevana3----------------------------
 
 
def menu_cuevana3(params):  
    plugintools.log("chopocine.menu_cuevana3")

    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]----[COLOR aqua]menu cuevana3[COLOR yellow]----[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://idescargar.com/wp-content/uploads/2019/09/cuevana-3-3.jpg", fanart = "https://www.fondoswiki.com/Uploads/fondoswiki.com/ImagenesGrandes/imagen-avatar.jpg",  folder = False )  
 
    plugintools.add_item(action = "cuevana3_buscador" , url='https://95.216.8.160',title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]cuevana3 buscador[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color, thumbnail ="https://idescargar.com/wp-content/uploads/2019/09/cuevana-3-3.jpg", fanart = "https://www.fondoswiki.com/Uploads/fondoswiki.com/ImagenesGrandes/imagen-avatar.jpg",page='',  folder = True )
 
    plugintools.add_item(action = "cuevana3_pelis" , url='https://95.216.8.160/peliculas',title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]cuevana3 todas[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color, thumbnail ="https://idescargar.com/wp-content/uploads/2019/09/cuevana-3-3.jpg", fanart = "https://www.fondoswiki.com/Uploads/fondoswiki.com/ImagenesGrandes/imagen-avatar.jpg",page='peliculas',  folder = True )     
 
    plugintools.add_item(action = "cuevana3_pelis" , url='https://95.216.8.160/estrenos',title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]cuevana3 estrenos[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color, thumbnail ="https://idescargar.com/wp-content/uploads/2019/09/cuevana-3-3.jpg", fanart = "https://www.fondoswiki.com/Uploads/fondoswiki.com/ImagenesGrandes/imagen-avatar.jpg",page='estrenos',  folder = True )  
 
    plugintools.add_item(action = "cuevana3_pelis" , url='https://95.216.8.160/peliculas-mas-valoradas',title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]cuevana3 mas valoradas[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color, thumbnail ="https://idescargar.com/wp-content/uploads/2019/09/cuevana-3-3.jpg", fanart = "https://www.fondoswiki.com/Uploads/fondoswiki.com/ImagenesGrandes/imagen-avatar.jpg",page='peliculas-mas-valoradas',  folder = True )  
 
    plugintools.add_item(action = "cuevana3_pelis" , url='https://95.216.8.160/peliculas-mas-vistas',title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]cuevana3 mas vistas[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color, thumbnail ="https://idescargar.com/wp-content/uploads/2019/09/cuevana-3-3.jpg", fanart = "https://www.fondoswiki.com/Uploads/fondoswiki.com/ImagenesGrandes/imagen-avatar.jpg",page='peliculas-mas-vistas',  folder = True )  
    plugintools.add_item(action = "cuevana3_pelis" , url='https://95.216.8.160/peliculas-espanol',title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]cuevana3 todas con idioma en español[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color, thumbnail ="https://idescargar.com/wp-content/uploads/2019/09/cuevana-3-3.jpg", fanart = "https://www.fondoswiki.com/Uploads/fondoswiki.com/ImagenesGrandes/imagen-avatar.jpg",page='peliculas-mas-vistas',  folder = True ) 
    plugintools.add_item(action = "cuevana3_generos" , url='https://95.216.8.160',title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]cuevana3 generos[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color, thumbnail ="https://idescargar.com/wp-content/uploads/2019/09/cuevana-3-3.jpg", fanart = "https://www.fondoswiki.com/Uploads/fondoswiki.com/ImagenesGrandes/imagen-avatar.jpg",page='',  folder = True )  


    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]----[COLOR aqua]menu cuevana3[COLOR yellow]----[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://idescargar.com/wp-content/uploads/2019/09/cuevana-3-3.jpg", fanart = "https://www.fondoswiki.com/Uploads/fondoswiki.com/ImagenesGrandes/imagen-avatar.jpg",  folder = False ) 
 
 
def cuevana3_buscador(params):  
    plugintools.log("chopocine.cuevana3_pelis")
    
  
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]----[COLOR aqua]buscador cuevana3[COLOR yellow]----[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://idescargar.com/wp-content/uploads/2019/09/cuevana-3-3.jpg", fanart = "https://www.fondoswiki.com/Uploads/fondoswiki.com/ImagenesGrandes/imagen-avatar.jpg",  folder = False ) 
    plugintools.set_view(plugintools.MOVIES,503)
    dialog = xbmcgui.Dialog()
    d = dialog.input('[B][LOWERCASE][CAPITALIZE][COLOR orange]buscar pelicula: ejemplo: [COLOR white]rocky[/COLOR][/CAPITALIZE][/LOWERCASE][/B]', type=xbmcgui.INPUT_ALPHANUM).replace(" ", "%20")
 
    url3= "https://95.216.8.160/search/"+d+'?__cpo=aHR0cHM6Ly93d3cxLmN1ZXZhbmEzLmFp'
    def cuerpo(url3):#torete
        import re , requests ,json        
        url=url3
        torete = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0","cookie":cookies} 
        de = requests.get(url3,  headers=torete,verify=False)
        if six.PY3==True :
            return de.text
        else :
            return de.content
       
    url=cuerpo(url3)
    matches = plugintools.find_multiple_matches(url,'((?s)class="xxx TPostMv">.*?<a href=".*?".*?class="Year">.*?<.*?data-src=".*?".*?class="Title">.*?<.*?<p><p>.*?<.*?)')
    for generos in matches:
 
       
        url= plugintools.find_single_match(generos,'a href="(.*?)"')
        anio=plugintools.find_single_match(generos,'class="Year">(.*?)<')
        foto='https://95.216.8.160'+plugintools.find_single_match(generos,'data-src=".*?cuevana3.ai(.*?)".*?')+'?__cpo=aHR0cHM6Ly93d3cxLmN1ZXZhbmEzLmFp|cookie='+cookies
        titulo=plugintools.find_single_match(generos,'class="Title">(.*?)<')
        texto=plugintools.find_single_match(generos,'<p><p>(.*?)<').replace("[&hellip;]", "")
        plugintools.set_view(plugintools.MOVIES,503) 
 
        plugintools.add_item(action = "cuevana3_servers" , title = "[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo+"[COLOR gold] "+anio+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", plot="[B][LOWERCASE][CAPITALIZE][COLOR white]"+texto+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail =foto, fanart =foto,url =url,  folder=True )
        
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]----[COLOR aqua]buscador cuevana3[COLOR yellow]----[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://idescargar.com/wp-content/uploads/2019/09/cuevana-3-3.jpg", fanart = "https://www.fondoswiki.com/Uploads/fondoswiki.com/ImagenesGrandes/imagen-avatar.jpg",  folder = False ) 
 
 
def cuevana3_generos(params):  
    plugintools.log("chopocine.cuevana3_pelis")
    proxys=params.get("extra")
    viva = {"https": "http://"+proxys+""}   
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]----[COLOR aqua]generos cuevana3[COLOR yellow]----[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://idescargar.com/wp-content/uploads/2019/09/cuevana-3-3.jpg", fanart = "https://www.fondoswiki.com/Uploads/fondoswiki.com/ImagenesGrandes/imagen-avatar.jpg",  folder = False ) 
    thumbnail = params.get("thumbnail")
    url3 = params.get("url").replace("www4.cuevana3.ai", "95.216.8.160")+'?__cpo=aHR0cHM6Ly93d3cxLmN1ZXZhbmEzLmFp'
    def cuerpo(url3):#torete
        import re , requests ,json        
        url=url3
        torete = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8","Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3","Upgrade-Insecure-Requests": "1","cookie":cookies} 
        de = requests.get(url, headers=torete,verify=False)
        if six.PY3==True :
            return de.text
        else :
            return de.content
    url=cuerpo(url3)
 
    matches = plugintools.find_multiple_matches(url,'<li class="menu-item"><a href="/category/.*?">.*?</a></li>')
    for generos in matches:
 
 
        url= 'https://95.216.8.160'+plugintools.find_single_match(generos,' href="(/category/.*?)"')
        titulo=plugintools.find_single_match(generos,'href="/category/(.*?)"')

 
 
        plugintools.add_item(action = "cuevana3_pelis" , title = "[B][LOWERCASE][CAPITALIZE][COLOR white]peliculas del genero[COLOR gold] "+titulo+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail =thumbnail, fanart =thumbnail,url =url,  folder=True )
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]----[COLOR aqua]generos cuevana3[COLOR yellow]----[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://idescargar.com/wp-content/uploads/2019/09/cuevana-3-3.jpg", fanart = "https://www.fondoswiki.com/Uploads/fondoswiki.com/ImagenesGrandes/imagen-avatar.jpg",  folder = False ) 
def cuevana3_pelis(params):  
    plugintools.log("chopocine.cuevana3_pelis")
    plugintools.set_view(plugintools.MOVIES,503)  
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]----[COLOR aqua]pelis cuevana3[COLOR yellow]----[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://idescargar.com/wp-content/uploads/2019/09/cuevana-3-3.jpg", fanart = "https://www.fondoswiki.com/Uploads/fondoswiki.com/ImagenesGrandes/imagen-avatar.jpg",  folder = False ) 
    thumbnail = params.get("thumbnail")
    url3 = params.get("url")+'?__cpo=aHR0cHM6Ly93d3cxLmN1ZXZhbmEzLmFp'
    page = params.get("page")
    def cuerpo(url3):#torete
        import re , requests ,json        
        url=url3
        torete = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8","Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3","Upgrade-Insecure-Requests": "1","cookie":cookies} 
        de = requests.get(url,  headers=torete,verify=False)
        if six.PY3==True :
            return de.text
        else :
            return de.content
       
    url=cuerpo(url3)
    try:
        pagina_siguiente=plugintools.find_single_match(url,'(?s)class="page-link current" class="page-link" href="https://ww2.cuevana3.*?<a href="(https://ww2.cuevana3.*?/page/.*?)" class="next page-numbers">').replace("www4.cuevana3.ai", "95.216.8.160")
        pagina_numero=plugintools.find_single_match(url,'class="page-link current" class="page-link" href="https://ww2.cuevana3.*?">(.*?)</a>')
        pagina_numero_fin=plugintools.find_single_match(url,'(?s)class="extend">...</span>.*?"page-link" .*?href=".*?page/.*?">(.*?)<')
        pagina_numero_elegir=plugintools.find_single_match(url,'<link rel="canonical" href="(https://ww2.cuevana3.*?)" />').replace("www4.cuevana3.ai", "95.216.8.160")
    except:
        pass
    matches = plugintools.find_multiple_matches(url,'((?s)class="xxx TPostMv">.*?<a href=".*?".*?class="Year">.*?<.*?data-src=".*?".*?class="Title">.*?<.*?<p><p>.*?<.*?)')
    for generos in matches:
 
       
        url= plugintools.find_single_match(generos,'a href="(.*?)"')
        anio=plugintools.find_single_match(generos,'class="Year">(.*?)<')
        foto='https://95.216.8.160'+plugintools.find_single_match(generos,'data-src=".*?cuevana3.ai(.*?)".*?')+'?__cpo=aHR0cHM6Ly93d3cxLmN1ZXZhbmEzLmFp|cookie='+cookies
        titulo=plugintools.find_single_match(generos,'class="Title">(.*?)<')
        texto=plugintools.find_single_match(generos,'<p><p>(.*?)<').replace("[&hellip;]", "")
        plugintools.set_view(plugintools.MOVIES,503) 
 
        plugintools.add_item(action = "cuevana3_servers" , title = "[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo+"[COLOR gold] "+anio+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",page=page, plot="[B][LOWERCASE][CAPITALIZE][COLOR white]"+texto+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail =foto, fanart =foto,url =url,  folder=True )
 
    if 'page' in pagina_siguiente:  
 
        plugintools.add_item( action="" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]estamos en la pagina [COLOR yellow]"+pagina_numero+" [COLOR lime]de [COLOR yellow]"+pagina_numero_fin+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", url= '', thumbnail = "https://previews.123rf.com/images/faysalfarhan/faysalfarhan1502/faysalfarhan150200608/36265105-siguiente-bot%C3%B3n-verde-vidrioso.jpg",fanart = "https://logos.flamingtext.com/Word-Logos/siguiente-design-china-name.png", folder=False )
        
        
        plugintools.add_item( action="cuevana3_pelis" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]ir a la pagina siguiente aqui[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", url= pagina_siguiente, thumbnail = "https://previews.123rf.com/images/faysalfarhan/faysalfarhan1502/faysalfarhan150200608/36265105-siguiente-bot%C3%B3n-verde-vidrioso.jpg",fanart = "https://logos.flamingtext.com/Word-Logos/siguiente-design-china-name.png", folder=True )
 
        plugintools.add_item( action="numeroscuevana3" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]elegir el numero de la pagina [COLOR orange]aqui [COLOR yellow] [/B][/COLOR][/CAPITALIZE][/LOWERCASE]", url= pagina_numero_elegir, thumbnail ="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTWSRFzCY9np6OBJOeSteicnEpi01dXfrf9WQ&usqp=CAU", fanart = "https://animarlogo.com/wp-content/uploads/2019/12/Logo-animado-Ave-m%C3%A1gica-AL316.jpg", folder=True ) 
 
 
 
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]----[COLOR aqua]pelis cuevana3[COLOR yellow]----[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://idescargar.com/wp-content/uploads/2019/09/cuevana-3-3.jpg", fanart = "https://www.fondoswiki.com/Uploads/fondoswiki.com/ImagenesGrandes/imagen-avatar.jpg",  folder = False ) 
 
 
def numeroscuevana3(params):  
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]----[COLOR aqua]elegir pagina cuevana3[COLOR yellow]----[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://idescargar.com/wp-content/uploads/2019/09/cuevana-3-3.jpg", fanart = "https://www.fondoswiki.com/Uploads/fondoswiki.com/ImagenesGrandes/imagen-avatar.jpg",  folder = False ) 
    proxys=params.get("extra")
    dialog = xbmcgui.Dialog()
    d = dialog.input('[B][LOWERCASE][CAPITALIZE][COLOR orange]PON EL NUMERO DE LA PAGINA [COLOR white]EJEMPLO 12[/COLOR][/CAPITALIZE][/LOWERCASE][/B]', type=xbmcgui.INPUT_NUMERIC)
    url1=params.get("url")+'/page/'+d
    
 
    plugintools.add_item( action="cuevana3_pelis" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]ir a la pagina "+d+"[/B][/COLOR][/CAPITALIZE][/LOWERCASE]", url= url1, thumbnail = "https://previews.123rf.com/images/faysalfarhan/faysalfarhan1502/faysalfarhan150200608/36265105-siguiente-bot%C3%B3n-verde-vidrioso.jpg",fanart = "https://logos.flamingtext.com/Word-Logos/siguiente-design-china-name.png", folder=True ) 
 
 
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]----[COLOR aqua]elegir pagina cuevana3[COLOR yellow]----[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://idescargar.com/wp-content/uploads/2019/09/cuevana-3-3.jpg", fanart = "https://www.fondoswiki.com/Uploads/fondoswiki.com/ImagenesGrandes/imagen-avatar.jpg",  folder = False ) 
 
def cuevana3_servers(params):  
    plugintools.log("chopocine.cuevana3_pelis")
 
    proxys=params.get("extra")
    viva = {"https": "http://"+proxys+""}  
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]----[COLOR aqua]servidores cuevana3[COLOR yellow]----[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://idescargar.com/wp-content/uploads/2019/09/cuevana-3-3.jpg", fanart = "https://www.fondoswiki.com/Uploads/fondoswiki.com/ImagenesGrandes/imagen-avatar.jpg",  folder = False ) 
    thumbnail = params.get("thumbnail")
    url3 = params.get("url").replace('www4.cuevana3.ai', '95.216.8.160')+'?__cpo=aHR0cHM6Ly93d3cxLmN1ZXZhbmEzLmFp'
    plot = params.get("plot")
    def sucuri(url3):
        import re,base64
        import requests
        import xbmc, xbmcaddon
        url = url3
        headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0","Cookie":cookies}
        if six.PY3==True :
            x = requests.get(url,headers=headers,verify=False).text
        else :
            x = requests.get(url,headers=headers,verify=False).content
        return x 
    url= sucuri(url3)
    trailer= plugintools.find_single_match(url,'"TPlayerTb" id="OptY"><iframe.*?data-src="(.*?)"')    

    matches = plugintools.find_multiple_matches(url,'(?s)data-TPlayerNv=.*? data-server.*?class="cdtr"><span>.*?<')
    for generos in matches:
 
 
        url= plugintools.find_single_match(generos,'data-TPlayerNv="(.*?)"')
        titulo=plugintools.find_single_match(generos,'="cdtr"><span(>.*?)<').replace('>1 - ', '1[COLOR red] no elegir-').replace('Español', '[COLOR lime] Español').replace('>', '')
 
 
        plugintools.add_item(action = "cuevana3_reproducir" , title = "[B][LOWERCASE][CAPITALIZE][COLOR white]opcion "+titulo+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", url=url3, thumbnail =thumbnail, fanart =thumbnail,page =url,  folder=False,  isPlayable = True  )
 
    plugintools.add_item(action = "play_resolver" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]ver el trailer [COLOR red]aqui[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", url=trailer,plot="[COLOR orange]"+plot+"[/COLOR]", thumbnail =thumbnail, fanart =thumbnail,  folder=False,  isPlayable = True ) 

    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]----[COLOR aqua]servidores cuevana3[COLOR yellow]----[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://idescargar.com/wp-content/uploads/2019/09/cuevana-3-3.jpg", fanart = "https://www.fondoswiki.com/Uploads/fondoswiki.com/ImagenesGrandes/imagen-avatar.jpg",  folder = False )         
 
def cuevana3_reproducir(params):  
    plugintools.log("chopocine.cuevana3_pelis")   
    url3 = params.get("page")
    url6=params.get("url")
    
    html='' 
    def sucuri(html):
        import re,base64
        import requests
        import xbmc, xbmcaddon
        headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0","Cookie":cookies}
        if six.PY3==True :
            x = requests.get(url6,headers=headers,verify=False).text
        else :
            x = requests.get(url6,headers=headers,verify=False).content
        return x 
    url= sucuri(html)
    url5= 'https:'+plugintools.find_single_match(url,'(?s)div class="TPlayerTb" id="'+url3+'".*?src="(.*?)"')
    
    if 'fembe' in url5:
        codec= plugintools.find_single_match(url5,'fembed/.h=(.*)')
        html='https://www.cliver.to/' 
        def sucuri(html):
            import re,base64
            import requests
            import xbmc, xbmcaddon
          
            headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0","Cookie":cookies}
            payload = {'h':codec}
            x = requests.post('https://95.216.8.160/fembed/api.php?__cpo=aHR0cHM6Ly9hcGkuY3VldmFuYTMubWU',headers=headers,data=payload,verify=False)
            
            if six.PY3==True :
                return x.text 
            else :
                return x.content 
        url= sucuri(html)
        
        try:
            url1= plugintools.find_single_match(url,'(?s)url":"(.*?)"').replace("\\", "")
        except:
            pass
        if 'https://www.fembed' in url1:
            import resolveurl 
            try:  
                video = resolveurl.resolve(url1)
                plugintools.play_resolved_url(video)
            except: 
                dialog = xbmcgui.Dialog()
                dialog.textviewer('[B][COLOR yellow]INFORMACION:[/COLOR][/B]', '[B][CAPITALIZE][COLOR aqua]parece que el enlace esta borrado\nelige otro server\n[COLOR aqua]DUDAS Y PREGUNTAS  [COLOR yellow]TELEGRAM @TVCHOPO[/COLOR][/CAPITALIZE][/B] ')

      

    if 'player.php' in url5:
        codec= plugintools.find_single_match(url5,'player.php.h=(.*)')
        html='https://www.cliver.to/' 
        def sucuri(html):
            import re,base64
            import requests
            import xbmc, xbmcaddon
          
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0"}
            payload = {'url':codec}
            x = requests.post('https://apialfa.tomatomatela.club/ir/rd.php',headers=headers,data=payload,verify=False)
            return x.request.url 
        url= sucuri(html).replace("telyn610zoanthropy.com", "voe.sx")
        if 'index' in url:
            codec= plugintools.find_single_match(url,'index.php.h=(.*)')
           
            html='https://www.cliver.to/' 
            def sucuri(html):
                import re,base64
                import requests
                import xbmc, xbmcaddon
                headers ={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0","Cookie":cookies}
                payload = {'h':codec}
                x = requests.post('https://95.216.8.160/sc/r.php?__cpo=aHR0cHM6Ly9hcGkuY3VldmFuYTMubWU',headers=headers,data=payload,verify=False)
                url= x.request.url
                x = requests.get(url,headers=headers,verify=False)
                if six.PY3==True : 
                    return x.text
                else : 
                    return x.content                    
                    
            url= sucuri(html)
            url= plugintools.find_single_match(url,'cpGenerated=.*?href="(.*?)"')
            import resolveurl 
            try:  
                video = resolveurl.resolve(url)
                plugintools.play_resolved_url(video)
            except: 
                dialog = xbmcgui.Dialog()
                dialog.textviewer('[B][COLOR yellow]INFORMACION:[/COLOR][/B]', '[B][CAPITALIZE][COLOR aqua]parece que el enlace esta borrado\nelige otro server\n[COLOR aqua]DUDAS Y PREGUNTAS  [COLOR yellow]TELEGRAM @TVCHOPO[/COLOR][/CAPITALIZE][/B] ')

       
        if 'sbembed' in url or 'streamtape' in url or  'telyn' in url or  'vanfem' in url or 'zplayer' in url or 'watch' in url:
            
            import resolveurl 
            try:  
                video = resolveurl.resolve(url)
                plugintools.play_resolved_url(video)
            except: 
                dialog = xbmcgui.Dialog()
                
                dialog.textviewer('[B][COLOR yellow]INFORMACION:[/COLOR][/B]', '[B][CAPITALIZE][COLOR aqua]parece que el enlace esta borrado\nelige otro server\n[COLOR aqua]DUDAS Y PREGUNTAS  [COLOR yellow]TELEGRAM @TVCHOPO[/COLOR][/CAPITALIZE][/B] ')



        else: 
            import resolveurl 
            try:  
                video = resolveurl.resolve(url)
                plugintools.play_resolved_url(video)
            except: 
                dialog = xbmcgui.Dialog()
                
                dialog.textviewer('[B][COLOR yellow]INFORMACION:[/COLOR][/B]', '[B][CAPITALIZE][COLOR aqua]parece que el enlace esta borrado\nelige otro server\n[COLOR aqua]DUDAS Y PREGUNTAS  [COLOR yellow]TELEGRAM @TVCHOPO[/COLOR][/CAPITALIZE][/B] ')        
#cuevana3----------------------------#cuevana3----------------------------#cuevana3----------------------------#cuevana3----------------------------#cuevana3----------------------------#cuevana3----------------------------#cuevana3----------------------------#cuevana3----------------------------#cuevana3----------------------------#cuevana3----------------------------#cuevana3----------------------------#cuevana3----------------------------#cuevana3----------------------------#cuevana3----------------------------#cuevana3----------------------------#cuevana3----------------------------#cuevana3----------------------------#cuevana3----------------------------#cuevana3----------------------------#cuevana3----------------------------#cuevana3----------------------------#cuevana3----------------------------#cuevana3----------------------------
 
 
 
 
 
 
 
#---gnula-------------------------------#gnula-------------------------------#---gnula-------------------------------#gnula-------------------------------#---gnula-------------------------------#gnula-------------------------------#---gnula-------------------------------#gnula-------------------------------#---gnula-------------------------------#gnula-------------------------------#---gnula-------------------------------#gnula-------------------------------#---gnula-------------------------------#gnula-------------------------------#---gnula-------------------------------#gnula-------------------------------#---gnula-------------------------------#gnula-------------------------------#---gnula-------------------------------#gnula-------------------------------#---gnula-------------------------------#gnula-------------------------------#---gnula-------------------------------#gnula-------------------------------

      
def menu_gnula(params):  
    plugintools.log("chopocine.hdfull_menu")
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]----[COLOR aqua]menu gnula[COLOR yellow]----[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://i.imgur.com/pm9MmeF.jpg", fanart = "https://i.imgur.com/X8DiYut.jpg",  folder = False )

    plugintools.add_item(action = "gnula_pelis_buscador" , url='https://www.gnula2.co/estrenos/',title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]gnula buscador[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color, thumbnail ="https://i.imgur.com/pm9MmeF.jpg",fanart = "https://i.imgur.com/X8DiYut.jpg",  folder = True )     
 
    plugintools.add_item(action = "gnula_pelis" , url='https://www.gnula2.co/estrenos/',title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]gnula estrenos[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color, thumbnail ="https://i.imgur.com/pm9MmeF.jpg",fanart = "https://i.imgur.com/X8DiYut.jpg",  folder = True ) 
 
 
    plugintools.add_item(action = "gnula_generos" , url='https://www.gnula2.co/',title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]gnula generos[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color, thumbnail ="https://i.imgur.com/pm9MmeF.jpg", fanart = "https://i.imgur.com/X8DiYut.jpg",  folder = True )    
 
 
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]----[COLOR aqua]menu gnula[COLOR yellow]----[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://i.imgur.com/pm9MmeF.jpg", fanart = "https://i.imgur.com/X8DiYut.jpg",  folder = False )
 
 
 
 
def gnula_pelis_buscador(params):  
    plugintools.log("chopocine.cine_torete_pelis")
    plugintools.set_view(plugintools.MOVIES,503)
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]----[COLOR aqua] gnula[COLOR yellow]----[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://i.imgur.com/pm9MmeF.jpg", fanart = "https://i.imgur.com/X8DiYut.jpg",  folder = False )
    dialog = xbmcgui.Dialog()
    d = dialog.input('[B][LOWERCASE][CAPITALIZE][COLOR orange]buscar pelicula: ejemplo: [COLOR white]rocky[/COLOR][/CAPITALIZE][/LOWERCASE][/B]', type=xbmcgui.INPUT_ALPHANUM).replace(" ", "%20")
 
    url= "https://95.216.8.160/buscar/"+d+"/"+'?__cpo=aHR0cHM6Ly93d3cuZ251bGEyLmNv'
 
    def sucuri(url):
        import re,base64
        import requests
        import xbmc, xbmcaddon
        headers= {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0","Cookie":cookies}

        x = requests.get(url,headers=headers,verify=False)  
        if six.PY3==True :             
            return x.text
        else :             
            return x.content
    url= sucuri(url)
 
    matches = plugintools.find_multiple_matches(url,'(<article class="tolbox".*?</article>)')
    for generos in matches:
 
        titulo=plugintools.find_single_match(generos,'data-title="(.*?)"') 
        texto=plugintools.find_single_match(generos,'data-desc="(.*?)"')
        if six.PY3==True:
            texto=unicodedata.normalize("NFKD", texto).encode("ascii","ignore").decode("ascii")
        else:
            texto=texto
        anio=plugintools.find_single_match(generos,'data-year="(.*?)"')      
        url=plugintools.find_single_match(generos,'a href="(.*?)"')        
        foto=plugintools.find_single_match(generos,'img src="(.*?)"')
 
        lenguaje=plugintools.find_single_match(generos,'class="langs">.*?<div class="(.*?)"')
        lenguaje2=plugintools.find_single_match(generos,'class="langs">.*?<div class=".*?<div class="(.*?)"')
 
        plugintools.set_view(plugintools.MOVIES,503) 
        plugintools.add_item(action = "gnula_servers" ,title = "[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo+" [COLOR gold]"+anio+" [COLOR lime]"+lenguaje+" [COLOR red]"+lenguaje2+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",  plot = "[B][LOWERCASE][CAPITALIZE][COLOR white][COLOR orange]"+texto+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail =foto, fanart =foto,url =url,  folder=True )    
 
def gnula_generos(params):  
    plugintools.log("chopocine.cine_torete_pelis")
 
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]----[COLOR aqua] gnula[COLOR yellow]----[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://i.imgur.com/pm9MmeF.jpg", fanart = "https://i.imgur.com/X8DiYut.jpg",  folder = False )
    thumbnail = params.get("thumbnail")
    url8 = params.get("url").replace("www.gnula2.co", "95.216.8.160")+'?__cpo=aHR0cHM6Ly93d3cuZ251bGEyLmNv'
  
    
    def sucuri(url8):
        import re,base64
        import requests
        import xbmc, xbmcaddon
        headers= {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0","Cookie":cookies}

        x = requests.get(url8,headers=headers,verify=False)        
        if six.PY3==True :             
            return x.text
        else :             
            return x.content
    url= sucuri(url8)
    matches = plugintools.find_multiple_matches(url,'<li>.*?<a href="https://www.gnula2.co/categoria/.*?/">.*?</a>.*?</li>')
    for generos in matches:
 
 
        url=plugintools.find_single_match(generos,'<a href="(https://www.gnula2.co/categoria/.*?)"')
        lenguaje=plugintools.find_single_match(generos,'<li>.*?>(.*?)</a>')
 
        plugintools.add_item(action = "gnula_pelis" , title = "[COLOR white]"+str(lenguaje)+"[/COLOR]",  thumbnail =thumbnail, fanart =thumbnail,url =url,  folder=True )
 
 
 
def gnula_pelis(params):  
    plugintools.log("chopocine.cine_torete_pelis")
    plugintools.set_view(plugintools.MOVIES,503)
    
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]----[COLOR aqua] gnula[COLOR yellow]----[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://i.imgur.com/pm9MmeF.jpg", fanart = "https://i.imgur.com/X8DiYut.jpg",  folder = False )

    
    url8 = params.get("url").replace("www.gnula2.co", "95.216.8.160")+'?__cpo=aHR0cHM6Ly93d3cuZ251bGEyLmNv'
    def sucuri(url8):
        import re,base64
        import requests
        import xbmc, xbmcaddon
        headers= {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0","Cookie":cookies}
        x = requests.get(url8,headers=headers,verify=False)   
        if six.PY3==True:            
            return x.text
        else:
            return x.content
    url= sucuri(url8)
    pagina_siguiente=plugintools.find_single_match(url,'class="counter">.*?<div><a href="(https://www.gnula2.co/.*?/.*?/)">Página siguiente')        
    pagina_numero=plugintools.find_single_match(url,'class="counter">Página (.*?)<')
    numero_elegido=plugintools.find_single_match(url,'<div><a href="(https://www.gnula2.co/.*?pagina)')
    matches = plugintools.find_multiple_matches(url,'(<article class="tolbox".*?</article>)')
    for generos in matches:
 
        titulo=plugintools.find_single_match(generos,'data-title="(.*?)"') 
        texto=plugintools.find_single_match(generos,'data-desc="(.*?)"')
        if six.PY3==True :
            texto=unicodedata.normalize("NFKD", texto).encode("ascii","ignore").decode("ascii")
        else:
            texto=texto
        anio=plugintools.find_single_match(generos,'data-year="(.*?)"')      
        url=plugintools.find_single_match(generos,'a href="(.*?)"')       
        foto=plugintools.find_single_match(generos,'img src="(.*?)"')
 
        lenguaje=plugintools.find_single_match(generos,'class="langs">.*?<div class="(.*?)"')
        lenguaje2=plugintools.find_single_match(generos,'class="langs">.*?<div class=".*?<div class="(.*?)"')
 
        plugintools.set_view(plugintools.MOVIES,503) 
        plugintools.add_item(action = "gnula_servers" , title = "[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo+" [COLOR gold]"+anio+"     [COLOR lime] "+lenguaje+", [COLOR red]"+lenguaje2+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", plot = "[B][LOWERCASE][CAPITALIZE][COLOR white][COLOR orange]"+texto+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail =foto, fanart =foto,url =url,  folder=True )
 
 
 
    if 'pagina' in pagina_siguiente:  
        plugintools.add_item( action="" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]estamos en la pagina "+pagina_numero+"[/B][/COLOR][/CAPITALIZE][/LOWERCASE]", url= pagina_siguiente, thumbnail = "https://previews.123rf.com/images/faysalfarhan/faysalfarhan1502/faysalfarhan150200608/36265105-siguiente-bot%C3%B3n-verde-vidrioso.jpg",fanart = "https://logos.flamingtext.com/Word-Logos/siguiente-design-china-name.png", folder=False ) 
        plugintools.add_item( action="gnula_pelis" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow] ir a la pagina siguiente [/B][/COLOR][/CAPITALIZE][/LOWERCASE]", url= pagina_siguiente, thumbnail = "https://previews.123rf.com/images/faysalfarhan/faysalfarhan1502/faysalfarhan150200608/36265105-siguiente-bot%C3%B3n-verde-vidrioso.jpg",fanart = "https://logos.flamingtext.com/Word-Logos/siguiente-design-china-name.png", folder=True )   
        
        plugintools.add_item( action="numerosgnula" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]elegir numero de la pagina  [COLOR yellow] [/B][/COLOR][/CAPITALIZE][/LOWERCASE]", url= numero_elegido, thumbnail ="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTWSRFzCY9np6OBJOeSteicnEpi01dXfrf9WQ&usqp=CAU", fanart = "https://animarlogo.com/wp-content/uploads/2019/12/Logo-animado-Ave-m%C3%A1gica-AL316.jpg", folder=True )  
 
def numerosgnula(params):  
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]----[COLOR aqua] gnula[COLOR yellow]----[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://i.imgur.com/pm9MmeF.jpg", fanart = "https://i.imgur.com/X8DiYut.jpg",  folder = False )

    dialog = xbmcgui.Dialog()
    d = dialog.input('[B][LOWERCASE][CAPITALIZE][COLOR orange]PON EL NUMERO DE LA PAGINA [COLOR white]EJEMPLO 12[/COLOR][/CAPITALIZE][/LOWERCASE][/B]', type=xbmcgui.INPUT_NUMERIC)
    url1=params.get("url")+d
 
    plugintools.add_item( action="gnula_pelis" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]ir a la pagina "+d+"[/B][/COLOR][/CAPITALIZE][/LOWERCASE]", url= url1, thumbnail = "https://previews.123rf.com/images/faysalfarhan/faysalfarhan1502/faysalfarhan150200608/36265105-siguiente-bot%C3%B3n-verde-vidrioso.jpg",fanart = "https://logos.flamingtext.com/Word-Logos/siguiente-design-china-name.png", folder=True )
 
 
 
def gnula_servers(params):  
    plugintools.log("chopocine.cine_torete_pelis")
 
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]----[COLOR aqua] gnula[COLOR yellow]----[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://i.imgur.com/pm9MmeF.jpg", fanart = "https://i.imgur.com/X8DiYut.jpg",  folder = False )
    thumbnail = params.get("thumbnail")
    url8 = params.get("url").replace("www.gnula2.co", "95.216.8.160")+'?__cpo=aHR0cHM6Ly93d3cuZ251bGEyLmNv'
    def sucuri(url8):
        import re,base64
        import requests
        import xbmc, xbmcaddon
        headers= {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0","Cookie":cookies}

        x = requests.get(url8,headers=headers,verify=False)        
        if six.PY3==True :           
            return x.text
        else:
            return x.content
    url= sucuri(url8)
    matches = plugintools.find_multiple_matches(url,'(class="lang-name">.*?<.*?|data-hash=".*?img src=".*?name">.*?quality">.*?</div>)')
    trailer=plugintools.find_single_match(url,'<iframe class="resp-iframe" src="(https://www.youtube..*?)"')
 
 
    for generos in matches:
 
        url='https://95.216.8.160/player.php?file='+plugintools.find_single_match(generos,'data-hash="(.*?)"')+'&play=1'
        server=plugintools.find_single_match(generos,'s-name">(.*?)<') 
        calidad=plugintools.find_single_match(generos,'s-quality">(.*?)<')   
        lenguaje=plugintools.find_single_match(generos,'class="lang-name">(.*?)<.*?')
        plugintools.add_item(action = "reproducir_gnula" , title ="[COLOR lime]"+lenguaje+" [COLOR white]"+server+" [COLOR gold]"+calidad+"[/COLOR]", thumbnail =thumbnail, fanart =thumbnail,url =url,  folder=False,  isPlayable = True)
        
        
    plugintools.add_item(action = "play_resolver" , title ="[COLOR fuchsia]ver el trailer[/COLOR]", thumbnail =thumbnail, fanart =thumbnail,url =trailer,  folder=False,  isPlayable = True)  
    
def reproducir_gnula(params):
        url = params.get("url")+'&__cpo=aHR0cHM6Ly93d3cuZ251bGEyLmNv'
        def sucuri(url):
            import re,base64
            import requests
            import xbmc, xbmcaddon
            headers= {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0","Cookie":cookies}

            x = requests.get(url,headers=headers,verify=False)      
            if six.PY3==True :           
                return x.text
            else:
                return x.content
        url= sucuri(url)
        url3=plugintools.find_single_match(url,'<iframe src="(.*?)"') 
        if 'ups' in url3:
            try:
                s=url3
                def dec(s):
                    from resolveurl.plugins.lib import jsunpack
                    import re, requests, resolveurl, xbmc
         
                    headers= {"User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8","Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3","Alt-Used": "gamovideo.com:443","Upgrade-Insecure-Requests": "1","Cache-Control": "max-age=0", "cookie": "gam=1"}
                    url=s
                    s=requests.session()
                    source=s.get(url, headers=headers,  verify=False)
                    if six.PY3==True :
                        pack = re.findall('javascript.*?(eval\(function\(p,a,c,k,e,d.*?m3u8.*)', source.text)[0]
                    else :
                        pack = re.findall('javascript.*?(eval\(function\(p,a,c,k,e,d.*?m3u8.*)', source.content)[0]
                    unpack=jsunpack.unpack(pack).replace('\\', '')
                    return re.findall('(?s)sources.*?file:"(https.*?m3u8.*?)"', unpack)[0].replace('hls/,', 'hls/').replace(',.urlset/master.m3u8', '/index-v1-a1.m3u8')+'|user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36&referer=https://upstream.to/'
                url8=dec(s)
                plugintools.play_resolved_url( url8 ) 
 
 
 
            except:
               import resolveurl 
               video = resolveurl.resolve( url3 ) 
               plugintools.play_resolved_url( video )
        else:
            import resolveurl 
            video = resolveurl.resolve( url3 ) 
            plugintools.play_resolved_url( video )          

 
 
 

#hdfull-------------------------------------------------------------------------------------------------------
 
 
 


def list_you(params):
    plugintools.log("chopocine.clivert_generos "+repr(params))    
    url = params.get("url")
    if six.PY3==True :
        data = plugintools.read(url).decode('utf-8')
    else:
        data = plugintools.read(url)
    matches = plugintools.find_multiple_matches(data,'("title":{"runs":.{"text":".*?",".*?"url":"/watch.v=.*?\\.*?list=.*?",".*?","webPageType":"WEB_PAGE_TYPE_WATCH","rootVe":.*?}},"watchEndpoint":{"videoId":".*?",")')
    for generos in matches:
 
 
        title = plugintools.find_single_match(generos,'"text":"(.*?)",".*?')
        url2 = plugintools.find_single_match(generos,'list=(.*?)",".*?')
        url1 = plugintools.find_single_match(generos,'"videoId":"(.*?)"')
 
        plugintools.add_item(action = "pelis_you" , title = "[B][LOWERCASE][CAPITALIZE][COLOR white]"+title+"[/COLOR][/CAPITALIZE][/LOWERCASE][/B]", url = 'https://www.youtube.com/watch?v='+url1+'&list='+url2,thumbnail = 'https://i.ytimg.com/vi/'+url1+'/hqdefault.jpg', fanart = 'https://i.ytimg.com/vi/'+url1+'/hqdefault.jpg', folder=True )
 
def pelis_you(params):
    plugintools.log("chopocine.clivert_generos "+repr(params))    
    url = params.get("url")
    if six.PY3==True :
        data = plugintools.read(url).decode('utf-8')
    else:
        data = plugintools.read(url)
    matches = plugintools.find_multiple_matches(data,'playlistPanelVideoRenderer":{"title":.*?simpleText":".*?".*?"videoId":".*?"')
    for generos in matches:
        url = plugintools.find_single_match(generos,'"videoId":"(.*?)"')
        title = plugintools.find_single_match(generos,'simpleText":"(.*?)".*?')
 
        plugintools.add_item(action = "play_resolver" , title = "[B][LOWERCASE][CAPITALIZE][COLOR white]"+title+"[/COLOR][/CAPITALIZE][/LOWERCASE][/B]", url = 'https://www.youtube.com/watch?v='+url,thumbnail = 'https://i.ytimg.com/vi/'+url+'/hqdefault.jpg', fanart = 'https://i.ytimg.com/vi/'+url+'/hqdefault.jpg', folder=False,  isPlayable = True )
 
 
 
 

 
 
 
 
 
  #------------------------------------------------------------------YAPE-------------------------------------------------------------------YAPE-------------------------------------------------------------------YAPE-------------------------------------------------------------------YAPE--------
def repelis_menu(params):  
    plugintools.log("chopocine.clasicos_del_cine")
    plugintools.set_view(plugintools.MOVIES,502)  
    thumbnail = params.get("thumbnail")
    fanart = params.get("extra")
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]---------------------[COLOR aqua]repelis[COLOR yellow]---------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail =thumbnail, fanart =fanart,  folder = False )   
 
 
 
 
 
    plugintools.add_item(action = "repelis_pelis" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]repelis[COLOR red] ESTRENOS[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color, thumbnail =thumbnail, fanart =fanart, url='https://www.repelis2.co/estrenos/', folder = True )  

    plugintools.add_item(action = "repelis_generos" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]repelis[COLOR red]  GENEROS[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color, thumbnail =thumbnail, fanart =fanart, url='', folder = True )    
 

    plugintools.add_item(action = "repelis_busca" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]repelis[COLOR red]  buscador[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color, thumbnail =thumbnail, fanart =fanart, url='', folder = True )    
 
 
 
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]---------------------[COLOR aqua]repelis[COLOR yellow]---------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail =thumbnail, fanart =fanart,  folder = False )  
 

def repelis_busca(params):  
    plugintools.log("chopocine.repelis_generos")
    thumbnail = params.get("thumbnail")
    fanart = params.get("extra") 
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]---------------------[COLOR aqua]repelis[COLOR yellow]---------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail =thumbnail, fanart =fanart,  folder = False ) 
    plugintools.set_view(plugintools.MOVIES,502)  
    dialog = xbmcgui.Dialog()
    d = dialog.input('[B][LOWERCASE][CAPITALIZE][COLOR orange]buscar una peli: ejemplo: [COLOR white]rocky[/COLOR][/CAPITALIZE][/LOWERCASE][/B]', type=xbmcgui.INPUT_ALPHANUM).replace(" ", "%20")
    url= 'https://www.repelis2.co/buscar/'+d+'/'
    html='' 
    def sucuri(html):
        import re,base64
        import requests
        import xbmc, xbmcaddon
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0"}
        if six.PY3==True :
            x = requests.get(url).text
        else :
            x = requests.get(url).content
        return x 
    url= sucuri(html)
    matches = plugintools.find_multiple_matches(url,'(?s)article class="tolbox" data-title=".*?".*?desc=".*?".*?data-year=".*?".*?href=".*?".*?img src=".*?".*?')
    for generos in matches:

        patron = plugintools.find_single_match(generos,'(?s)article class="tolbox" data-title="(.*?)".*?desc="(.*?)".*?data-year="(.*?)".*?href="(.*?)".*?img src="(.*?)".*?')
        url=patron[3]
        titulo = patron[0]
        foto = patron[4]  
        texto = patron[1]       
        anio = patron[2]
        plugintools.set_view(plugintools.MOVIES,503)
        plugintools.add_item(action = "repelis_servers" , title ="[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo+" [COLOR gold] "+anio+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", page=titulo, plot="[B][LOWERCASE][CAPITALIZE][COLOR gold]"+texto+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",thumbnail=foto, url=url, fanart =foto,   folder = True ) 
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]---------------------[COLOR aqua]repelis[COLOR yellow]---------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail =thumbnail, fanart =fanart,  folder = False ) 
 
 
 
 
 
 
def repelis_generos(params):  
    plugintools.log("chopocine.repelis_servers")
 
    thumbnail = params.get("thumbnail")
    fanart = params.get("extra") 
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]---------------------[COLOR aqua]repelis[COLOR yellow]---------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail =thumbnail, fanart =fanart,  folder = False ) 
    url5='https://www.repelis2.co/principal-b/'
    html='' 
    def sucuri(html):
        import re,base64
        import requests
        import xbmc, xbmcaddon
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0"}
        if six.PY3==True :
            x = requests.get(url5).text
        else :
            x = requests.get(url5).content
        return x 
    url= sucuri(html)
 
    matches = plugintools.find_multiple_matches(url,'(?s)<li>.*?<a href="https://www.repelis2.co/categoria/.*?">.*?</a>')
    for generos in matches:
 
 
        patron = plugintools.find_single_match(generos,'(?s)<li>.*?<a href="(https://www.repelis2.co/categoria/.*?)">(.*?)</a>') 
        url = patron[0]       
        titulo = patron[1]
 
        plugintools.add_item(action = "repelis_pelis" , title ="[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail=thumbnail, url=url, fanart =thumbnail,  folder=True  )     
 
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]---------------------[COLOR aqua]repelis[COLOR yellow]---------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail =thumbnail, fanart =fanart,  folder = False )      
 
  
 
 
 
def repelis_pelis(params):  
    plugintools.log("chopocine.clasicos_del_cine")
    thumbnail = params.get("thumbnail")
    fanart = params.get("extra") 
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]---------------------[COLOR aqua]repelis[COLOR yellow]---------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail =thumbnail, fanart =fanart,  folder = False )    
    plugintools.set_view(plugintools.MOVIES,503)
    url5 = params.get("url")
 
    html='' 
    def sucuri(html):
        import re,base64
        import requests
        import xbmc, xbmcaddon
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0"}
        if six.PY3==True :
            x = requests.get(url5).text
        else :
            x = requests.get(url5).content
        return x 
    url= sucuri(html)
    try:
        patron_pagina = plugintools.find_single_match(url,'(?s)<div class="counter">Página (.*?)<.*?<div><a href="(.*?)"')
        numero=patron_pagina[0]
        pagina_siguiente=patron_pagina[1]
        numero_pagina = plugintools.find_single_match(url,'(?s)<div class="paginator">.*?<div><a href="(https://www.repelis2.co/.*?/)pagina')
    except:
        pagina_siguiente=''
    matches = plugintools.find_multiple_matches(url,'(?s)article class="tolbox" data-title=".*?".*?desc=".*?".*?data-year=".*?".*?href=".*?".*?img src=".*?".*?')
    for generos in matches:

        patron = plugintools.find_single_match(generos,'(?s)article class="tolbox" data-title="(.*?)".*?desc="(.*?)".*?data-year="(.*?)".*?href="(.*?)".*?img src="(.*?)".*?')
        url=patron[3]
        titulo = patron[0]
        foto = patron[4]  
        texto = patron[1]       
        anio = patron[2]
        plugintools.set_view(plugintools.MOVIES,503)
        plugintools.add_item(action = "repelis_servers" , title ="[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo+" [COLOR gold] "+anio+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", page=titulo, plot="[B][LOWERCASE][CAPITALIZE][COLOR gold]"+texto+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",thumbnail=foto, url=url, fanart =foto,   folder = True ) 
 
    if 'http' in pagina_siguiente:
        plugintools.add_item(action = "repelis_pelis" , title ="[B][LOWERCASE][CAPITALIZE][COLOR orange]estamos en la pagina "+numero+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",  thumbnail='', url='', fanart ='',   folder = False )
        
        plugintools.add_item(action = "repelis_pelis" , title ="[B][LOWERCASE][CAPITALIZE][COLOR lime]ir a la pagina siguiente[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",  thumbnail = "https://previews.123rf.com/images/faysalfarhan/faysalfarhan1502/faysalfarhan150200608/36265105-siguiente-bot%C3%B3n-verde-vidrioso.jpg",fanart = "https://logos.flamingtext.com/Word-Logos/siguiente-design-china-name.png", url=pagina_siguiente,   folder = True )
        
        
        plugintools.add_item(action = "repelis_pelis_numeros" , title ="[B][LOWERCASE][CAPITALIZE][COLOR yellow]elige tu el numero de la pagina[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",  thumbnail='', url=numero_pagina, fanart ='',   folder = True )        
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]---------------------[COLOR aqua]repelis[COLOR yellow]---------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail =thumbnail, fanart =fanart,  folder = False )   
 
def repelis_pelis_numeros(params):  
    thumbnail = params.get("thumbnail")
    fanart = params.get("extra") 
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]---------------------[COLOR aqua]repelis[COLOR yellow]---------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail =thumbnail, fanart =fanart,  folder = False ) 
 
    dialog = xbmcgui.Dialog()
    d = dialog.input('[B][LOWERCASE][CAPITALIZE][COLOR orange]PON EL NUMERO DE LA PAGINA [COLOR white]EJEMPLO 12[/COLOR][/CAPITALIZE][/LOWERCASE][/B]', type=xbmcgui.INPUT_NUMERIC)
    url1=params.get("url")+'pagina'+d+'/'
    
 
    plugintools.add_item( action="repelis_pelis" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]ir a la pagina "+d+"[/B][/COLOR][/CAPITALIZE][/LOWERCASE]", url= url1, thumbnail = "https://previews.123rf.com/images/faysalfarhan/faysalfarhan1502/faysalfarhan150200608/36265105-siguiente-bot%C3%B3n-verde-vidrioso.jpg",fanart = "https://logos.flamingtext.com/Word-Logos/siguiente-design-china-name.png", folder=True ) 
 
def repelis_servers(params):  
    plugintools.log("chopocine.repelis_servers") 
    thumbnail = params.get("thumbnail")
    fanart = params.get("extra")
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]---------------------[COLOR aqua]repelis[COLOR yellow]---------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail =thumbnail, fanart =fanart,  folder = False ) 
    url = params.get("url")
    thumbnail = params.get("thumbnail")
    html='' 
    def sucuri(html):
        import re,base64
        import requests
        import xbmc, xbmcaddon
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0"}
        if six.PY3==True :
            x = requests.get(url).text
        else :
            x = requests.get(url).content
        return x 
    url= sucuri(html)
    server = plugintools.find_multiple_matches(url,'(?s)class="lang-name">.*?<.*?|class="server.*?data-hash=".*?".*?s-name">.*?<.*?class="s-quality">.*?<.*?')
    for generos in server:
        patron = plugintools.find_single_match(generos,'(?s)class="lang-name">(.*?)<.*?|class="server.*?data-hash="(.*?)".*?s-name">(.*?)<.*?class="s-quality">(.*?)<.*?')
        idioma = patron[0]
        url = patron[1]  
        server = patron[2]
        
        calidad=patron[3]         
        plugintools.add_item(action = "repelis_reproducir" ,url =str(url),thumbnail =thumbnail ,fanart =thumbnail, title ="[B][LOWERCASE][CAPITALIZE][COLOR white]"+str(idioma)+"[COLOR gold]"+str(server)+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", folder= False,  isPlayable = True )
 
def repelis_reproducir(params):  
    plugintools.log("chopocine.repelis_servers")   
    url = 'https://www.repelis2.co/player.php?file='+params.get("url")+'&play=1'
    html='' 
    def sucuri(html):
        import re,base64
        import requests
        import xbmc, xbmcaddon
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0"}
        if six.PY3==True :
            x = requests.get(url).text
        else :
            x = requests.get(url).content
        return x 
    url= sucuri(html)
    url = plugintools.find_single_match(url,'<iframe src="(.*?)".*?')
    import resolveurl 
    try:  
        video = resolveurl.resolve( url )+'&verifypeer=false' 
        plugintools.play_resolved_url( video )
    except: 
        xbmc.executebuiltin('XBMC.Notification([B][LOWERCASE][CAPITALIZE][COLOR white]enlace  [COLOR red]borrado [/CAPITALIZE][/LOWERCASE][/B][/COLOR],[B][LOWERCASE][CAPITALIZE][COLOR white]elige otro [/CAPITALIZE][/LOWERCASE][/B][/COLOR], 2000)')

    #------------------------------------------------------------------YAPE-------------------------------------------------------------------YAPE-------------------------------------------------------------------YAPE-------------------------------------------------------------------YAPE----
 
 
 
#-------------------------REPELIS----------------REPELIS-----------------------------REPELIS-------------------------------REPELIS----------------REPELIS-----------------------------REPELIS-------------------------------REPELIS----------------REPELIS-----------------------------REPELIS-------------------------------REPELIS----------------REPELIS-----------------------------REPELIS-------------------------------REPELIS----------------REPELIS
 
 
 
def ciclos_de_cine(params):  
    plugintools.log("chopocine.clasicos_del_cine")
    plugintools.set_view(plugintools.MOVIES,503)
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]---------------------[COLOR aqua]clasicos del cine generos[COLOR yellow]---------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://enfilme.com/img/content/newhollywoodalgarabia_Enfilme_30h24_675_489.jpg", fanart ="https://www.unir.net/wp-content/uploads/2019/09/foto-hollywood-guion-unir.jpg",  folder = False )  
     
    url = params.get("url")
 
    def cuerpo(url):
        import re, requests, resolveurl, xbmc
        url =url
        headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
        "Upgrade-Insecure-Requests": "1",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache","cookie":cookies
    }
 
 
        logueo = requests.get(url, headers=headers,verify=False)
        if six.PY3==True :
            r = logueo.text
        else:
            r = logueo.content
        return r
    url=cuerpo(url)
    matches = plugintools.find_multiple_matches(url,'(?s)<div id="post-.*?href=".*?".*?src=".*?".*?entry-title">.*?">.*?</a></h2>.*?"entry-summary">.*?<')
    for generos in matches: 
        patron = plugintools.find_single_match(generos,'(?s)<div id="post-.*?href="(.*?)".*?src="(.*?)".*?entry-title">.*?">(.*?)</a></h2>.*?"entry-summary">(.*?)<')
        url=patron[0].replace("tucineclasico.es", "95.216.8.160")+'?__cpo=aHR0cHM6Ly90dWNpbmVjbGFzaWNvLmVz'
        titulo = patron[2]
        foto = patron[1]
        texto = patron[3]
        plugintools.set_view(plugintools.MOVIES,503)
        plugintools.add_item(action = "ciclo_del_cine2" ,plot ="[B][LOWERCASE][CAPITALIZE][COLOR white][COLOR gold]"+texto+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", title ="[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",  thumbnail =foto, fanart =foto, url=url,    folder = True ) 
        
        
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]---------------------[COLOR aqua]ciclos del cine generos[COLOR yellow]---------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://enfilme.com/img/content/newhollywoodalgarabia_Enfilme_30h24_675_489.jpg", fanart ="https://www.unir.net/wp-content/uploads/2019/09/foto-hollywood-guion-unir.jpg",  folder = False )   
 
def ciclo_del_cine2(params):  
    plugintools.log("chopocine.clasicos_del_cine")
 
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]---------------------[COLOR aqua]ciclos del cine[COLOR yellow]---------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://enfilme.com/img/content/newhollywoodalgarabia_Enfilme_30h24_675_489.jpg", fanart ="https://www.unir.net/wp-content/uploads/2019/09/foto-hollywood-guion-unir.jpg",  folder = False )  
    plugintools.set_view(plugintools.MOVIES,502)  
    url = params.get("url")
    def cuerpo(url):
        import re, requests, resolveurl, xbmc
        url =url
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8","Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3","Upgrade-Insecure-Requests": "1","Pragma": "no-cache","Cache-Control": "no-cache","cookie":cookies}
        logueo = requests.get(url, headers=headers,verify=False)
        if six.PY3==True :
            r = logueo.text
        else:
            r = logueo.content
        return r
    url=cuerpo(url)

    matches = plugintools.find_multiple_matches(url,'figure class=".*?</a></figure>')
    for generos in matches: 
        patron = plugintools.find_single_match(generos,'href="(https://.*?tucineclasico.es/(.*?))".*?src="(.*?)".*?')
        url=patron[0]
        titulo = patron[1].replace("peliculas/", "").replace("-", " ").replace("/", "")
        foto = patron[2]   

        plugintools.add_item(action = "clasicos_del_server" , title ="[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", page=titulo,thumbnail=foto, url=url, fanart =foto,   folder = True ) 
 
 
 
def clasicos_del_cine_busca(params):  
    plugintools.log("chopocine.clasicos_del_cine")
 
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]---------------------[COLOR aqua]clasicos del cine[COLOR yellow]---------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://enfilme.com/img/content/newhollywoodalgarabia_Enfilme_30h24_675_489.jpg", fanart ="https://www.unir.net/wp-content/uploads/2019/09/foto-hollywood-guion-unir.jpg",  folder = False )  
    plugintools.set_view(plugintools.MOVIES,503) 
    dialog = xbmcgui.Dialog()
    d = dialog.input('[B][LOWERCASE][CAPITALIZE][COLOR orange]buscar una peli: ejemplo: [COLOR white]rocky[/COLOR][/CAPITALIZE][/LOWERCASE][/B]', type=xbmcgui.INPUT_ALPHANUM).replace(" ", "+")
    url="https://95.216.8.160/?s="+d+"&__cpo=aHR0cHM6Ly9vbmxpbmUudHVjaW5lY2xhc2ljby5lcw"
    def cuerpo(url):
        import re, requests, resolveurl, xbmc
        url =url
        headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
        "Upgrade-Insecure-Requests": "1",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache","cookie":cookies
    }
 
 
        logueo = requests.get(url, headers=headers,verify=False)
        if six.PY3==True :
            r = logueo.text
        else:
            r = logueo.content
        return r
    url=cuerpo(url)
    matches = plugintools.find_multiple_matches(url,'(?s)class="result-item"><article>.*?href=".*?".*?img src=".*?".*?alt=".*?".*?contenido"><p>.*?<.*?')
    for generos in matches: 
        patron = plugintools.find_single_match(generos,'(?s)class="result-item"><article>.*?href="(.*?)".*?img src="(.*?)".*?alt="(.*?)".*?contenido"><p>(.*?)<.*?')
        url=patron[0].replace("Descargar", "").replace("y ver Online", "")
        titulo = patron[2]
        foto = patron[1]   
        texto = patron[3]
        plugintools.set_view(plugintools.MOVIES,503)
        plugintools.add_item(action = "clasicos_del_server" , title ="[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", plot="[B][LOWERCASE][CAPITALIZE][COLOR white]"+texto+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",thumbnail=foto, url=url, fanart =foto,   folder = True ) 
 
def clasicos_del_cine_generos(params):  
    plugintools.log("chopocine.clasicos_del_cine")
 
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]---------------------[COLOR aqua]clasicos del cine generos[COLOR yellow]---------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://enfilme.com/img/content/newhollywoodalgarabia_Enfilme_30h24_675_489.jpg", fanart ="https://www.unir.net/wp-content/uploads/2019/09/foto-hollywood-guion-unir.jpg",  folder = False )  
    plugintools.set_view(plugintools.MOVIES,502)  
    url = params.get("url")
 
    def cuerpo(url):
        import re, requests, resolveurl, xbmc
        url =url
        headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
        "Upgrade-Insecure-Requests": "1",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache","cookie":cookies
    }
 
 
        logueo = requests.get(url, headers=headers,verify=False)
        if six.PY3==True :
            r = logueo.text
        else:
            r = logueo.content
        return r
    url=cuerpo(url)
    matches = plugintools.find_multiple_matches(url,'<a href="https://online.tucineclasico.es/genero/.*?/">.*?</a>')
    for generos in matches: 
        url = plugintools.find_single_match(generos,'href="(.*?)"').replace("online.tucineclasico.es", "95.216.8.160")+'?__cpo=aHR0cHM6Ly9vbmxpbmUudHVjaW5lY2xhc2ljby5lcw'
        titulo = plugintools.find_single_match(generos,'">(.*?)</a>')
 
        plugintools.add_item(action = "clasicos_del_cine" , title ="[B][LOWERCASE][CAPITALIZE][COLOR white]peliculas clasicas del genero [COLOR gold]"+titulo+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",  thumbnail ="https://enfilme.com/img/content/newhollywoodalgarabia_Enfilme_30h24_675_489.jpg", fanart ="https://www.unir.net/wp-content/uploads/2019/09/foto-hollywood-guion-unir.jpg", url=url,    folder = True ) 
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]---------------------[COLOR aqua]clasicos del cine generos[COLOR yellow]---------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://enfilme.com/img/content/newhollywoodalgarabia_Enfilme_30h24_675_489.jpg", fanart ="https://www.unir.net/wp-content/uploads/2019/09/foto-hollywood-guion-unir.jpg",  folder = False )  
def clasicos_del_cine(params):  
    plugintools.log("chopocine.clasicos_del_cine")
 
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]---------------------[COLOR aqua]clasicos del cine[COLOR yellow]---------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://enfilme.com/img/content/newhollywoodalgarabia_Enfilme_30h24_675_489.jpg", fanart ="https://www.unir.net/wp-content/uploads/2019/09/foto-hollywood-guion-unir.jpg",  folder = False )  
    plugintools.set_view(plugintools.MOVIES,502)  
    url = params.get("url")
    def cuerpo(url):
        import re, requests, resolveurl, xbmc
        url =url
        headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
        "Upgrade-Insecure-Requests": "1",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache","cookie":cookies
    }
 
 
        logueo = requests.get(url, headers=headers,verify=False)
        if six.PY3==True :
            r = logueo.text
        else:
            r = logueo.content
        return r
    url=cuerpo(url)
    try:
        paginas = plugintools.find_single_match(url,'class="pagination"><span>(.*?gina .*? de .*?)</')
        siguiente= plugintools.find_single_match(url,'next" href="(.*?)"')
        pagina= plugintools.find_single_match(url,"class='pages'>(.*?)<")
    except:
        siguiente=''
    matches = plugintools.find_multiple_matches(url,'(?s)<article id="post-.*?img src=".*?".*?alt=".*?".*?href=".*?".*?<span>.*?<.*?')
    for generos in matches: 
        patron = plugintools.find_single_match(generos,'(?s)<article id="post-(.*?)".*?img src="(.*?)".*?alt="(.*?)".*?href="(.*?)".*?<span>(.*?)<.*?')
        url=patron[3]
        titulo = patron[2]
        foto = patron[1]   
        anio = patron[4]
        post = patron[0]
        plugintools.add_item(action = "clasicos_del_server" , title ="[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo+"[COLOR yellow] "+anio+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", page=titulo,thumbnail=foto, url=url, fanart =foto,   folder = True ) 
 
    if 'http' in siguiente: 
        plugintools.add_item( action="clasicos_del_cine" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]"+paginas+"   [/B][/COLOR][/CAPITALIZE][/LOWERCASE]", url= '', thumbnail = "https://www.periodicoelpunto.com/wp-content/uploads/2019/03/flecha-siguiente.png",fanart = "https://www.periodicoelpunto.com/wp-content/uploads/2019/03/flecha-siguiente.png", folder=False )    
        plugintools.add_item( action="clasicos_del_cine" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]ir a la pagina siguiente[/B][/COLOR][/CAPITALIZE][/LOWERCASE]", url= siguiente, thumbnail = "https://previews.123rf.com/images/faysalfarhan/faysalfarhan1502/faysalfarhan150200608/36265105-siguiente-bot%C3%B3n-verde-vidrioso.jpg",fanart = "https://logos.flamingtext.com/Word-Logos/siguiente-design-china-name.png", folder=True )
 
def clasicos_del_server(params):  
    plugintools.log("chopocine.clasicos_del_cine")
    plugintools.set_view(plugintools.MOVIES,503)
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]---------------------[COLOR aqua]clasicos del cine[COLOR yellow]---------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://enfilme.com/img/content/newhollywoodalgarabia_Enfilme_30h24_675_489.jpg", fanart ="https://www.unir.net/wp-content/uploads/2019/09/foto-hollywood-guion-unir.jpg",  folder = False )  
    thumbnail = params.get("thumbnail") 
    url = params.get("url").replace("online.tucineclasico.es", "95.216.8.160")+'?__cpo=aHR0cHM6Ly9vbmxpbmUudHVjaW5lY2xhc2ljby5lcw'
    thumbnail = params.get("thumbnail") 
    def cuerpo(url):
        import re, requests, resolveurl, xbmc
        url =url
        headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
        "Upgrade-Insecure-Requests": "1",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache","cookie":cookies
    }
 
        logueo = requests.get(url,headers=headers,verify=False)
        if six.PY3==True :
            r = logueo.text
        else:
            r = logueo.content
        return r
    url=cuerpo(url)
    try:
        texto = plugintools.find_single_match(url,'property="og:description" content="(.*?)"')
    except:
        texto='no hay sipnosis de esta pelicula'
    matches = plugintools.find_multiple_matches(url,"(?s)ata-type='movie' data-post='.*?data-nume='.*?'.*?title'>.*?<.*?img/flags/.*?.png'>")
 
    for generos in matches: 
        patron = plugintools.find_single_match(generos,"(?s)ata-type='movie' data-post='(.*?)'.*?data-nume='(.*?)'.*?title'>Ver Online (.*?)<.*?img/flags/(.*?).png'>")
        post = patron[0]
        numero = patron[1]
        titulo = patron[2]   
        idioma = patron[3]
        url = 'https://95.216.8.160/wp-json/dooplayer/v2/'+post+'/movie/'+numero+'?__cpo=aHR0cHM6Ly9vbmxpbmUudHVjaW5lY2xhc2ljby5lcw'
        plugintools.set_view(plugintools.MOVIES,503)
        plugintools.add_item(action = "clasicos_del_reproducir" , title ="[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo+"[COLOR gold]  "+idioma+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",plot ="[B][LOWERCASE][CAPITALIZE][COLOR white]"+texto+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",  thumbnail=thumbnail, url=url, fanart =thumbnail,folder=False,  isPlayable = True  ) 
 
 

    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]---------------------[COLOR aqua]clasicos del cine[COLOR yellow]---------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://enfilme.com/img/content/newhollywoodalgarabia_Enfilme_30h24_675_489.jpg", fanart ="https://www.unir.net/wp-content/uploads/2019/09/foto-hollywood-guion-unir.jpg",  folder = False )     
 
def clasicos_del_reproducir(params): 
    plugintools.log("chopocine.pelis_de_los_80_90 ")   
    url = params.get("url")
    def cuerpo(url):
        import re, requests, resolveurl, xbmc
        url =url
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8","Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3","Upgrade-Insecure-Requests": "1","Pragma": "no-cache","Cache-Control": "no-cache","cookie":cookies}
        logueo = requests.get(url,headers=headers,verify=False)
        if six.PY3==True :
            r = logueo.text
        else:
            r = logueo.content
        return r
    url=cuerpo(url)
    url = plugintools.find_single_match(url,'(?s)"embed_url":".*?src=."(http.*?)."').replace("\\", "")       
    import resolveurl 
    try:  
        video = resolveurl.resolve( url )
        try:
            plugintools.play_resolved_url( video )
        except:
            pass
    except: 
        dp = xbmcgui.DialogProgress()
        dp.create('[CAPITALIZE][COLOR yellow]parece que el enlace esta borrado[/COLOR][/CAPITALIZE]')
        xbmc.sleep(2000)
        dp.update(100,'[CAPITALIZE][COLOR lime]ELIGE OTRO SERVER\nESTE ENLACE ESTA BORRADO[/COLOR][/CAPITALIZE]')  
        xbmc.sleep(2000)
        dp.close()
 
 
 
 
 
 
 
 
 
 
 
def cine_espanol(params): 
    plugintools.log("chopocine.pelis_de_los_80_90 ")  
    plugintools.set_view(plugintools.MOVIES,502)
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]--------------[COLOR yellow] las mejores peliculas del cine español[COLOR aqua]-------------- [/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://st-listas.20minutos.es/images/2017-08/423961/list_640px.jpg?1518448609", fanart = "https://img.vavel.com/peliculas-taquilleras-espanolas-9649484213.png",   folder = False )  
    if six.PY3==True :
        data = plugintools.read("https://pastebin.com/raw/QW0A0mzx").decode('utf-8')
    else:
        data = plugintools.read("https://pastebin.com/raw/QW0A0mzx")
    matches = plugintools.find_multiple_matches(data,'(name".*?url".*?".*?".*?)')
    for generos in matches:
        titulo = plugintools.find_single_match(generos,'name".*?"(.*?)".*?') 
        foto = plugintools.find_single_match(generos,'mage".*?"(.*?)".*?')       
        url = plugintools.find_single_match(generos,'url".*?"(.*?)"')         
        plugintools.add_item(action = "play_resolver" , title = "[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail =foto,url=url, fanart = foto,  folder=False,  isPlayable = True )
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]--------------[COLOR yellow] las mejores peliculas del cine español[COLOR aqua]-------------- [/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://st-listas.20minutos.es/images/2017-08/423961/list_640px.jpg?1518448609", fanart = "https://img.vavel.com/peliculas-taquilleras-espanolas-9649484213.png",   folder = False )  
 
 
 
 
 
    #---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------
 

 
 
 
 
 
 
 
##---------------------SAGAS ESPECIALES Y MAS--------------------------------------------------------------SAGAS ESPECIALES Y MAS------------------
##---------------------SAGAS ESPECIALES Y MAS--------------------------------------------------------------SAGAS ESPECIALES Y MAS------------------
 
 
 
def cien_mejores_sagas(params):  
    plugintools.log("chopocine.cien_mejores_sagas") 
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR white]--------------[COLOR yellow] LAS 101 MEJORES SAGAS DE LA HISTORIA[COLOR white]-------------- [/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://www.alvarocuevas.es/wp-content/uploads/2021/01/Las-mejores-sagas-de-peliculas.jpg",fanart = "https://media.vandalsports.com/master/6-2021/2021629471_1.jpg",  folder = False )  
    plugintools.set_view(plugintools.MOVIES,502)  
    proxys=params.get("extra") 
    url = 'https://pastebin.com/raw/gUfB3DrX'
    def sucuri(url):
        import re,base64
        import requests
        import xbmc, xbmcaddon
        headers= {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0","Cookie":cookies}

        x = requests.get(url,headers=headers,verify=False)  
        if six.PY3==True :             
            return x.text
        else :             
            return x.content
    url= sucuri(url)
 
    matches = plugintools.find_multiple_matches(url,'(?s)titulo ".*?".*?foto ".*?".*?anio ".*?".*?')
    for generos in matches: 
        foto = plugintools.find_single_match(generos,'foto "(.*?)".*?')+'|user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36&referer=https://upstream.to/'
        titulo = plugintools.find_single_match(generos,'(?s)titulo "(.*?)".*?foto ".*?".*?anio ".*?".*?')
        titulo2= titulo.replace("James Bond", "007").replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u").replace(",", "").replace(".", "").replace(' ','%20')
        anio = plugintools.find_single_match(generos,'anio "(.*?)".*?')
 
        plugintools.add_item(action = "gnula_pelis_proveedoras" , title ="[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo+" [COLOR gold]"+anio+"[COLOR aqua][/CAPITALIZE][/LOWERCASE][/B][/COLOR]",  thumbnail=foto, url=titulo2, fanart =foto,   folder = True ) 
 
 
 
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR white]--------------[COLOR yellow] LAS 101 MEJORES SAGAS DE LA HISTORIA[COLOR white]-------------- [/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://st-listas.20minutos.es/images/2013-11/372969/list_640px.jpg?1518602731",fanart = "https://media.vandalsports.com/master/6-2021/2021629471_1.jpg",  folder = False )  
 
 
def PRODUCTORAS(params): 
    plugintools.log("chopocine.pelis_de_los_80_90 ")  
    plugintools.set_view(plugintools.MOVIES,502)
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]--------------[COLOR yellow] CINE PRODUCTORAS[COLOR aqua]-------------- [/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://vertele.eldiario.es/2019/10/31/noticias/Amazon-Netflix-Apple-TV-Espana_2172692762_14050592_660x371.jpg", fanart = "https://e00-marca.uecdn.es/assets/multimedia/imagenes/2020/11/20/16058878063470.jpg",  folder = False ) 
        
    numero=params.get("page")
    url = "https://pastebin.com/raw/sr9tjvQc"
    def sucuri(url):
        import re,base64
        import requests
        import xbmc, xbmcaddon
        headers= {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0","Cookie":cookies}

        x = requests.get(url,headers=headers,verify=False)  
        if six.PY3==True :             
            return x.text
        else :             
            return x.content
    data= sucuri(url)
    matches = plugintools.find_multiple_matches(data,'(technical_name":".*?","short_name":".*?","clear_name":".*?".*?icon_url":".*?{profile)')
    for generos in matches:
        patron = plugintools.find_single_match(generos,'technical_name":".*?","short_name":"(.*?)","clear_name":"(.*?)".*?icon_url":"(.*?){profile') 
        proveedeor = patron[1] 
        foto = 'https://images.justwatch.com'+patron[2]+'s100'   
        url = patron[0]
 
        url = 'https://apis.justwatch.com/content/titles/es_ES/popular?body={%22age_certifications%22:[],%22content_types%22:[%22movie%22],%22genres%22:[],%22languages%22:null,%22min_price%22:null,%22matching_offers_only%22:null,%22max_price%22:null,%22monetization_types%22:[],%22presentation_types%22:[],%22providers%22:[%22'+url+'%22],%22release_year_from%22:null,%22release_year_until%22:null,%22scoring_filter_types%22:null,%22timeline_type%22:null,%22sort_by%22:null,%22sort_asc%22:null,%22page%22:'
 
        plugintools.add_item(action = "peliculas_netflix" , title ="[B][LOWERCASE][CAPITALIZE][COLOR white]"+proveedeor+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail =foto,url=url,page=numero, fanart = foto,  folder=True)
        
        
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]--------------[COLOR yellow] CINE PRODUCTORAS[COLOR aqua]-------------- [/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://vertele.eldiario.es/2019/10/31/noticias/Amazon-Netflix-Apple-TV-Espana_2172692762_14050592_660x371.jpg", fanart = "https://e00-marca.uecdn.es/assets/multimedia/imagenes/2020/11/20/16058878063470.jpg",  folder = False ) 
 
 
 
def peliculas_netflix(params):  
    plugintools.log("chopocine.peliculas_netflix") 
    plugintools.set_view(plugintools.LIST) 
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]--------------[COLOR yellow] CINE PRODUCTORAS[COLOR aqua]-------------- [/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://vertele.eldiario.es/2019/10/31/noticias/Amazon-Netflix-Apple-TV-Espana_2172692762_14050592_660x371.jpg", fanart = "https://e00-marca.uecdn.es/assets/multimedia/imagenes/2020/11/20/16058878063470.jpg",  folder = False ) 
    
    url1=params.get("url")
    numero=params.get("page")
    url=url1+numero+',%22page_size%22:30}'
    def sucuri(url):
        import re,base64
        import requests
        import xbmc, xbmcaddon
        headers= {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0","Cookie":cookies}

        x = requests.get(url,headers=headers,verify=False)  
        if six.PY3==True :             
            return x.text
        else :             
            return x.content
    url= sucuri(url)
    matches = plugintools.find_multiple_matches(url,'(?s)(title":".*?)object_type":"movie')
    for generos in matches: 
        titulo = plugintools.find_single_match(generos,'title":"(.*?)"') 
        titulo2 = titulo.replace("Enola Holmes 2", "enola holmes").replace(' ','%20').replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u").replace(",", "").replace(".", "")
        foto = plugintools.find_single_match(generos,'poster":"(.*?).profile..*?')
 
        plugintools.add_item(action = "gnula_pelis_proveedoras" , title ="[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",thumbnail ="https://images.justwatch.com"+foto+"s166",fanart = "https://images.justwatch.com"+foto+"s166", url= titulo2,    folder = True ) 
 
    if '66' > numero : 
        s='sumar'
        def dec(s):
            a = int("1")
            b = int(numero)
            suma = a+b
            return (str(suma))
        esto = dec(s)    
        plugintools.add_item( action="peliculas_netflix" , title = "[B][LOWERCASE][CAPITALIZE][COLOR gold]---------pagina "+numero+"[/B][/COLOR][/CAPITALIZE][/LOWERCASE]", url=url1,page= esto, thumbnail = "https://previews.123rf.com/images/faysalfarhan/faysalfarhan1502/faysalfarhan150200608/36265105-siguiente-bot%C3%B3n-verde-vidrioso.jpg",fanart = "https://logos.flamingtext.com/Word-Logos/siguiente-design-china-name.png", folder=False )
        
        plugintools.add_item( action="peliculas_netflix" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]ir a la pagina siguiente[/B][/COLOR][/CAPITALIZE][/LOWERCASE]", url=url1,page= esto, thumbnail = "https://previews.123rf.com/images/faysalfarhan/faysalfarhan1502/faysalfarhan150200608/36265105-siguiente-bot%C3%B3n-verde-vidrioso.jpg",fanart = "https://logos.flamingtext.com/Word-Logos/siguiente-design-china-name.png", folder=True )
 
 
        plugintools.add_item( action="numerosproductoras" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]o eliges tu  la pagina a la que ir aqui[/B][/COLOR][/CAPITALIZE][/LOWERCASE]", url=url1,page= esto, thumbnail = "https://previews.123rf.com/images/faysalfarhan/faysalfarhan1502/faysalfarhan150200608/36265105-siguiente-bot%C3%B3n-verde-vidrioso.jpg",fanart = "https://logos.flamingtext.com/Word-Logos/siguiente-design-china-name.png", folder=True )
 
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]--------------[COLOR yellow] CINE PRODUCTORAS[COLOR aqua]-------------- [/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://vertele.eldiario.es/2019/10/31/noticias/Amazon-Netflix-Apple-TV-Espana_2172692762_14050592_660x371.jpg", fanart = "https://e00-marca.uecdn.es/assets/multimedia/imagenes/2020/11/20/16058878063470.jpg",  folder = False ) 
 
def numerosproductoras(params):  
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]--------------[COLOR yellow] CINE PRODUCTORAS[COLOR aqua]-------------- [/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://vertele.eldiario.es/2019/10/31/noticias/Amazon-Netflix-Apple-TV-Espana_2172692762_14050592_660x371.jpg", fanart = "https://e00-marca.uecdn.es/assets/multimedia/imagenes/2020/11/20/16058878063470.jpg",  folder = False ) 
    
    dialog = xbmcgui.Dialog()
    d = dialog.input('[B][LOWERCASE][CAPITALIZE][COLOR orange]PON EL NUMERO DE LA PAGINA [COLOR white]EJEMPLO 12[/COLOR][/CAPITALIZE][/LOWERCASE][/B]', type=xbmcgui.INPUT_NUMERIC)
    url1=params.get("url")
    numero=d
    plugintools.add_item( action="peliculas_netflix" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]ir a la pagina "+d+" [/B][/COLOR][/CAPITALIZE][/LOWERCASE]", url=url1,page= d, thumbnail = "https://previews.123rf.com/images/faysalfarhan/faysalfarhan1502/faysalfarhan150200608/36265105-siguiente-bot%C3%B3n-verde-vidrioso.jpg",fanart = "https://logos.flamingtext.com/Word-Logos/siguiente-design-china-name.png", folder=True )
    
    
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]--------------[COLOR yellow] CINE PRODUCTORAS[COLOR aqua]-------------- [/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://vertele.eldiario.es/2019/10/31/noticias/Amazon-Netflix-Apple-TV-Espana_2172692762_14050592_660x371.jpg", fanart = "https://e00-marca.uecdn.es/assets/multimedia/imagenes/2020/11/20/16058878063470.jpg",  folder = False ) 
 
 
def gnula_pelis_proveedoras(params):  
    plugintools.log("chopocine.gnula_pelis_proveedoras")
    plugintools.set_view(plugintools.MOVIES,503)
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]--------------[COLOR yellow] opcion 1[COLOR aqua]-------------- [/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://vertele.eldiario.es/2019/10/31/noticias/Amazon-Netflix-Apple-TV-Espana_2172692762_14050592_660x371.jpg", fanart = "https://e00-marca.uecdn.es/assets/multimedia/imagenes/2020/11/20/16058878063470.jpg",  folder = False ) 
    d=params.get("url").replace(' ','%20')
  
    url= "https://95.216.8.160/buscar/"+d+"/"+'?__cpo=aHR0cHM6Ly93d3cuZ251bGEyLmNv'
    dp = xbmcgui.DialogProgress()
    dp.create('[CAPITALIZE][COLOR yellow]BUSCANDO LA PELICULA [/COLOR][/CAPITALIZE]')
    xbmc.sleep(2000)
    dp.update(100,'[CAPITALIZE][COLOR lime]ESTAMOS BUSCANDO LA PELI\nPACIENCIA POR FAVOR[/COLOR][/CAPITALIZE]')  
    xbmc.sleep(2000)
    dp.close()
    def sucuri(url):
        import re,base64
        import requests
        import xbmc, xbmcaddon
        headers= {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0","Cookie":cookies}

        x = requests.get(url,headers=headers,verify=False)  
        if six.PY3==True :             
            return x.text
        else :             
            return x.content
    url= sucuri(url)
    if 'article class="tolbox' in url:
        matches = plugintools.find_multiple_matches(url,'(<article class="tolbox".*?</article>)')
        for generos in matches:
 
            titulo=plugintools.find_single_match(generos,'data-title="(.*?)"') 
            texto=plugintools.find_single_match(generos,'data-desc="(.*?)"')
            if six.PY3==True :
                texto=unicodedata.normalize("NFKD", texto).encode("ascii","ignore").decode("ascii")
            else:
                texto=texto
            anio=plugintools.find_single_match(generos,'data-year="(.*?)"')      
            url=plugintools.find_single_match(generos,'a href="(.*?)"')        
            foto=plugintools.find_single_match(generos,'img src="(.*?)"')
 
            lenguaje=plugintools.find_single_match(generos,'class="langs">.*?<div class="(.*?)"')
            lenguaje2=plugintools.find_single_match(generos,'class="langs">.*?<div class=".*?<div class="(.*?)"')
 
            plugintools.set_view(plugintools.MOVIES,503)
            plugintools.add_item(action = "gnula_servers" ,title = "[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo+" [COLOR gold]"+anio+" [COLOR lime]"+lenguaje+" [COLOR red]"+lenguaje2+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",  plot = "[B][LOWERCASE][CAPITALIZE][COLOR white][COLOR orange]"+texto+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail =foto, fanart =foto,url =url,  folder=True )   
    else:  
        plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua][COLOR white] no hay resultado de la busqueda en esta web[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://vertele.eldiario.es/2019/10/31/noticias/Amazon-Netflix-Apple-TV-Espana_2172692762_14050592_660x371.jpg", fanart = "https://e00-marca.uecdn.es/assets/multimedia/imagenes/2020/11/20/16058878063470.jpg",  folder = False )  
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]--------------[COLOR yellow] opcion 2[COLOR aqua]-------------- [/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://vertele.eldiario.es/2019/10/31/noticias/Amazon-Netflix-Apple-TV-Espana_2172692762_14050592_660x371.jpg", fanart = "https://e00-marca.uecdn.es/assets/multimedia/imagenes/2020/11/20/16058878063470.jpg",  folder = False )        
    plugintools.set_view(plugintools.MOVIES,503)    
    url3= "https://95.216.8.160/search/"+d+"?__cpo=aHR0cHM6Ly93d3cxLmN1ZXZhbmEzLmFp"
    def cuerpo(url3):#torete
        import re , requests ,json        
        url=url3
        torete = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0","Cookie":cookies} 
        de = requests.get(url3,  headers=torete,verify=False)
        if six.PY3==True :
            return de.text
        else :
            return de.content
       
    url=cuerpo(url3)
    if 'class="xxx TPostMv">' in url:
        matches = plugintools.find_multiple_matches(url,'((?s)class="xxx TPostMv">.*?<a href=".*?".*?class="Year">.*?<.*?data-src=".*?".*?class="Title">.*?<.*?<p><p>.*?<.*?)')
        for generos in matches:
 
       
            url= plugintools.find_single_match(generos,'a href="(.*?)"')
            anio=plugintools.find_single_match(generos,'class="Year">(.*?)<')
            foto='https://95.216.8.160'+plugintools.find_single_match(generos,'data-src=".*?cuevana3.ai(.*?)".*?')+'?__cpo=aHR0cHM6Ly93d3cxLmN1ZXZhbmEzLmFp|cookie='+cookies
            titulo=plugintools.find_single_match(generos,'class="Title">(.*?)<')
            texto=plugintools.find_single_match(generos,'<p><p>(.*?)<').replace("[&hellip;]", "") 
            plugintools.set_view(plugintools.MOVIES,503)
            plugintools.add_item(action = "cuevana3_servers" , title = "[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo+"[COLOR gold] "+anio+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", plot="[B][LOWERCASE][CAPITALIZE][COLOR white]"+texto+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail =foto, fanart =foto,url =url,  folder=True )
            
    else:  
        plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua][COLOR white] no hay resultado de la busqueda en esta web[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://vertele.eldiario.es/2019/10/31/noticias/Amazon-Netflix-Apple-TV-Espana_2172692762_14050592_660x371.jpg", fanart = "https://e00-marca.uecdn.es/assets/multimedia/imagenes/2020/11/20/16058878063470.jpg",  folder = False )            
            
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]--------------[COLOR yellow] opcion 3[COLOR aqua]-------------- [/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://vertele.eldiario.es/2019/10/31/noticias/Amazon-Netflix-Apple-TV-Espana_2172692762_14050592_660x371.jpg", fanart = "https://e00-marca.uecdn.es/assets/multimedia/imagenes/2020/11/20/16058878063470.jpg",  folder = False ) 
    plugintools.set_view(plugintools.MOVIES,503)
    url= 'https://www.repelis2.co/buscar/'+d+'/'
    html='' 
    def sucuri(html):
        import re,base64
        import requests
        import xbmc, xbmcaddon
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0"}
        if six.PY3==True :
            x = requests.get(url).text
        else :
            x = requests.get(url).content
        return x 
    url= sucuri(html)
    if 'article class="tolbox"' in url:
        matches = plugintools.find_multiple_matches(url,'(?s)article class="tolbox" data-title=".*?".*?desc=".*?".*?data-year=".*?".*?href=".*?".*?img src=".*?".*?')
        for generos in matches:

            patron = plugintools.find_single_match(generos,'(?s)article class="tolbox" data-title="(.*?)".*?desc="(.*?)".*?data-year="(.*?)".*?href="(.*?)".*?img src="(.*?)".*?')
            url=patron[3]
            titulo = patron[0]
            foto = patron[4]  
            texto = patron[1]       
            anio = patron[2]
            plugintools.set_view(plugintools.MOVIES,503)
            plugintools.add_item(action = "repelis_servers" , title ="[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo+" [COLOR gold] "+anio+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", page=titulo, plot="[B][LOWERCASE][CAPITALIZE][COLOR gold]"+texto+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",thumbnail=foto, url=url, fanart =foto,   folder = True )  
        
    else:  
        plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua][COLOR white] no hay resultado de la busqueda en esta web[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://vertele.eldiario.es/2019/10/31/noticias/Amazon-Netflix-Apple-TV-Espana_2172692762_14050592_660x371.jpg", fanart = "https://e00-marca.uecdn.es/assets/multimedia/imagenes/2020/11/20/16058878063470.jpg",  folder = False )        
        
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]--------------[COLOR yellow] opcion 4[COLOR aqua]-------------- [/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://vertele.eldiario.es/2019/10/31/noticias/Amazon-Netflix-Apple-TV-Espana_2172692762_14050592_660x371.jpg", fanart = "https://e00-marca.uecdn.es/assets/multimedia/imagenes/2020/11/20/16058878063470.jpg",  folder = False ) 

    d=d.replace("%20", "+")    
    url="https://95.216.8.160/?s="+d+"&__cpo=aHR0cHM6Ly9vbmxpbmUudHVjaW5lY2xhc2ljby5lcw"
    def cuerpo(url):
        import re, requests, resolveurl, xbmc
        url =url
        headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
        "Upgrade-Insecure-Requests": "1",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache","cookie":cookies
    }
 
 
        logueo = requests.get(url, headers=headers,verify=False)
        if six.PY3==True :
            r = logueo.text
        else:
            r = logueo.content
        return r
    url=cuerpo(url)
    if 'class="result-item"><article>' in url:
        matches = plugintools.find_multiple_matches(url,'(?s)class="result-item"><article>.*?href=".*?".*?img src=".*?".*?alt=".*?".*?contenido"><p>.*?<.*?')
        for generos in matches: 
            patron = plugintools.find_single_match(generos,'(?s)class="result-item"><article>.*?href="(.*?)".*?img src="(.*?)".*?alt="(.*?)".*?contenido"><p>(.*?)<.*?')
            url=patron[0].replace("Descargar", "").replace("y ver Online", "")
            titulo = patron[2]
            foto = patron[1]   
            texto = patron[3]
            plugintools.set_view(plugintools.MOVIES,503)
            plugintools.add_item(action = "clasicos_del_server" , title ="[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", plot="[B][LOWERCASE][CAPITALIZE][COLOR white]"+texto+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",thumbnail=foto, url=url, fanart =foto,   folder = True )  
    else:  
        plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua][COLOR white] no hay resultado de la busqueda en esta web[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://vertele.eldiario.es/2019/10/31/noticias/Amazon-Netflix-Apple-TV-Espana_2172692762_14050592_660x371.jpg", fanart = "https://e00-marca.uecdn.es/assets/multimedia/imagenes/2020/11/20/16058878063470.jpg",  folder = False ) 
def pelis_de_los_80_90(params): 
    plugintools.log("chopocine.pelis_de_los_80_90 ")  
    plugintools.set_view(plugintools.MOVIES,503)
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]--------------[COLOR yellow] pelis de los años 80 y 90[COLOR aqua]-------------- [/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://www.alucine.es/wp-content/uploads/2015/03/341.jpg", fanart = "https://www.lacabecita.com/wp-content/uploads/90s.png",  folder = False ) 
    if six.PY3==True :    
        data = plugintools.read("https://pastebin.com/raw/V9mRefns").decode('utf-8')
    else :    
        data = plugintools.read("https://pastebin.com/raw/V9mRefns") 
    url= base64.b64decode(data)
    if six.PY3==True:
        data = url.decode('utf-8')
    else:
        data=url        
    matches = plugintools.find_multiple_matches(data,'(?s)"name": ".*?".*?year": ".*?".*?genre": ".*?".*?synopsis": ".*?".*?url": ".*?".*?')
    for generos in matches:
        titulo = plugintools.find_single_match(generos,'"name": "(.*?)\(') 
        foto = plugintools.find_single_match(generos,'"image": "(.*?)"')       
        url = plugintools.find_single_match(generos,'url": "(.*?)"') 
        year = plugintools.find_single_match(generos,'"year": "(.*?)"')       
        synopsis = plugintools.find_single_match(generos,'synopsis": "(.*?)"') 
        plugintools.set_view(plugintools.MOVIES,503)
        plugintools.add_item(action = "repro_80_90" , page=titulo,title = "[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo+" [COLOR orange]"+year+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail =foto,plot="[B][LOWERCASE][CAPITALIZE][COLOR yellow]"+synopsis+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",url=url, fanart = foto,  folder=False,  isPlayable = True)
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]--------------[COLOR yellow] pelis de los años 80 y 90[COLOR aqua]-------------- [/CAPITALIZE][/LOWERCASE][/B][/COLOR]",  thumbnail ="https://www.alucine.es/wp-content/uploads/2015/03/341.jpg", fanart = "https://www.lacabecita.com/wp-content/uploads/90s.png",  folder = False )  
 
def repro_80_90(params):
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]--------------[COLOR yellow] pelis de los años 80 y 90[COLOR aqua]-------------- [/CAPITALIZE][/LOWERCASE][/B][/COLOR]",  thumbnail ="https://www.alucine.es/wp-content/uploads/2015/03/341.jpg", fanart = "https://www.lacabecita.com/wp-content/uploads/90s.png",  folder = False )
    url = params.get("url")
    if 'gamovideo' in url:
        def dec(url):
            try:
                from resolveurl.plugins.lib import jsunpack
 
            except:
                from resolveurl.lib import jsunpack
            import re, requests, resolveurl, xbmc
            url=url
            s=requests.session()
            headers= {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8","Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3","Alt-Used": "gamovideo.net","cookie":"sugamun=1"}
            rsource=s.get(url, headers=headers,  verify=False)
            source=s.get(url, headers=headers,  verify=False)
            pack = re.findall('javascript.*?(eval\(function\(p,a,c,k,e,d.*)', source.text)[0]
            unpack=jsunpack.unpack(pack).replace('\\', '')
            return re.findall('file:\s*"(http.*?)"', unpack)[0]
 
        url=dec(url)
        plugintools.play_resolved_url( url) 
    else:        
        import resolveurl 
        video = resolveurl.resolve( url )+'&verifypeer=false'
        plugintools.play_resolved_url( video ) 
 

def cine_kinki(params):  
    plugintools.log("chopocine.cine_kinki ")    
    thumbnail = params.get("thumbnail") 

    plugintools.set_view(plugintools.MOVIES,515)   
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]--------------[COLOR yellow] cine quinqui[COLOR aqua]-------------- [/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail =thumbnail,fanart = thumbnail,url = "https://zoowoman.website/wp/genre/cine-quinqui/",  folder = False )  

    url = 'https://cinekinkihd.freesite.host/'
    def sucuri(url):
        import re,base64
        import requests
        import xbmc, xbmcaddon
        headers= {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
        "Upgrade-Insecure-Requests": "1",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache"
    }

        x = requests.get(url,headers=headers,verify=False)  
        if six.PY3==True :             
            return x.text
        else :             
            return x.content
    url= sucuri(url)

    matches = plugintools.find_multiple_matches(url,'(?s)<article id="post-.*?data-src=".*?".*?alt=".*?".*?href=".*?".*?<span>.*?.*?<')
    for generos in matches:
 
        patron = plugintools.find_single_match(generos,'(?s)<article id="post-.*?data-src="(.*?)".*?alt="(.*?)".*?href="(.*?)".*?<span>.*?(.*?)<') 
        foto =  patron[0]
        titulo =  patron[1] 
        url =  patron[2]  
        
        anio =  patron[3]        
        plugintools.set_view(plugintools.MOVIES,55)
        plugintools.add_item(action = "link_kinki" , title ="[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo+"  [COLOR yellow]"+anio+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",thumbnail =foto,url=url, fanart = foto,  folder=True )

    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]--------------[COLOR yellow] cine quinqui[COLOR aqua]-------------- [/CAPITALIZE][/LOWERCASE][/B][/COLOR]",  thumbnail ="https://i.ytimg.com/vi/gom1cQNshzo/hqdefault.jpg",fanart = "http://3.bp.blogspot.com/-ABfKzNTa8zo/V_uZANGZ-rI/AAAAAAAAKXI/y2WMvfjL3CwV7hyRPz2VlU7pbVEEI49bACK4B/s1600/foto.jpg",url = "https://zoowoman.website/wp/genre/cine-quinqui/",  folder = False )  
 

def link_kinki(params):  
    plugintools.log("chopocine.cine_kinki ")    
    url = params.get("url")
    thumbnail = params.get("thumbnail")
    def sucuri(url):
        import re,base64
        import requests
        import xbmc, xbmcaddon
        headers= {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
        "Upgrade-Insecure-Requests": "1",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache"
    }

        x = requests.get(url,headers=headers,verify=False)  
        if six.PY3==True :             
            return x.text
        else :             
            return x.content
    url= sucuri(url)

    url = 'https:'+plugintools.find_single_match(url,'name="advanced_iframe" src="(.*?)"')

    def sucuri(url):
        import re,base64
        import requests
        import xbmc, xbmcaddon
        headers= {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
        "Upgrade-Insecure-Requests": "1",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache"
    }

        x = requests.get(url,headers=headers,verify=False)  
        if six.PY3==True :             
            return x.text
        else :             
            return x.content
    url= sucuri(url)
    matches = plugintools.find_multiple_matches(url,'({.&quot;name.&quot;:.&quot;.*?.&quot.*?url.&quot;:.&quot;https.*?.&quot;)')
 
    for generos in matches:
        url = plugintools.find_single_match(generos,'{.&quot;name.&quot;:.&quot;.*?.&quot.*?url.&quot;:.&quot;(https.*?).&quot;').replace('\\','').replace('u0026','&')
        titulo = plugintools.find_single_match(generos,'{.&quot;name.&quot;:.&quot;(.*?).&quot.*?url.&quot;:.&quot;https.*?.&quot;')
 
        plugintools . add_item ( action = "motogp5" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime] elige en calidad [COLOR white]"+titulo+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", url = url, thumbnail =  thumbnail , fanart=thumbnail, folder=False,  isPlayable = True) 

def motogp5(params): 
    plugintools.log("tvchopo.canales_deportes ")
    url = params.get("url")
    plugintools.play_resolved_url(url) 
 
 
#-------------------------------------------------PELIS24---------------------------------------------------
#-------------------------------------------------PELIS24---------------------------------------------------
 
 
 
def megalink(params): 
    url = params.get("url")
    urlmega = mega.finalurl(url)
    finalurl = mega.main(urlmega)[0]
    plugintools.play_resolved_url(finalurl) 
 
 
#---------------------------------------------------------reproducir--RESOLVERURL-------------------------------------------------------------------#---------------------------------------------------------reproducir--RESOLVERURL-------------------------------------------------------------------
def play_links2(params): 
    try:  
        url =params.get("url")
        plugintools.play_resolved_url( url ) 
 
    except: 
        u= xbmc.executebuiltin('XBMC.Notification([B][LOWERCASE][CAPITALIZE][COLOR white]enlace  [COLOR red]borrado [/CAPITALIZE][/LOWERCASE][/B][/COLOR],[B][LOWERCASE][CAPITALIZE][COLOR white]elige otro [/CAPITALIZE][/LOWERCASE][/B][/COLOR], 2000)')
        plugintools.add_item(action = "" ,title = u, thumbnail ='',url='', fanart = '', folder=False,  isPlayable = True )
 
def play_links(params): 
    try:  
        url =params.get("url")+'&verifypeer=false'
        plugintools.play_resolved_url( url ) 
 
    except: 
        u= xbmc.executebuiltin('XBMC.Notification([B][LOWERCASE][CAPITALIZE][COLOR white]enlace  [COLOR red]borrado [/CAPITALIZE][/LOWERCASE][/B][/COLOR],[B][LOWERCASE][CAPITALIZE][COLOR white]elige otro [/CAPITALIZE][/LOWERCASE][/B][/COLOR], 2000)')
        plugintools.add_item(action = "" ,title = u, thumbnail ='',url='', fanart = '', folder=False,  isPlayable = True )
def play_resolver(params):
    import resolveurl 
    try:  
        video = resolveurl.resolve( params.get("url") )+'&verifypeer=false' 
        plugintools.play_resolved_url( video )
    except: 
        u= xbmc.executebuiltin('XBMC.Notification([B][LOWERCASE][CAPITALIZE][COLOR white]enlace  [COLOR red]borrado [/CAPITALIZE][/LOWERCASE][/B][/COLOR],[B][LOWERCASE][CAPITALIZE][COLOR white]elige otro [/CAPITALIZE][/LOWERCASE][/B][/COLOR], 2000)')
        plugintools.add_item(action = "" ,title = u, thumbnail ='',url='', fanart = '', folder=False,  isPlayable = True )
 
#---------------------------------------------------------reproducir--RESOLVERURL-------------------------------------------------------------------#---------------------------------------------------------reproducir--RESOLVERURL-----------------------------------------------------------------
 
 
 
#megabuscador-------------------------------------------------------------------------------
def mega_busca(params):  
    plugintools.log("chopocine.clasicos_del_cine")
 

    proxys=params.get("extra")
    viva = {"http": "http://"+proxys,"https": "http://"+proxys}
    dialog = xbmcgui.Dialog()
    d = dialog.input('[B][LOWERCASE][CAPITALIZE][COLOR orange]buscar una peli: ejemplo: [COLOR white]rocky[/COLOR][/CAPITALIZE][/LOWERCASE][/B]', type=xbmcgui.INPUT_ALPHANUM).replace(" ", "%20")
    plugintools.log("chopocine.mega_busca"+repr(params)) 
 
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]--------------[COLOR yellow] opcion 1[COLOR aqua]-------------- [/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://vertele.eldiario.es/2019/10/31/noticias/Amazon-Netflix-Apple-TV-Espana_2172692762_14050592_660x371.jpg", fanart = "https://e00-marca.uecdn.es/assets/multimedia/imagenes/2020/11/20/16058878063470.jpg",  folder = False ) 
    url= "https://95.216.8.160/buscar/"+d+"/"+'?__cpo=aHR0cHM6Ly93d3cuZ251bGEyLmNv'
    dp = xbmcgui.DialogProgress()
    dp.create('[CAPITALIZE][COLOR yellow]BUSCANDO LA PELICULA [/COLOR][/CAPITALIZE]')
    xbmc.sleep(2000)
    dp.update(100,'[CAPITALIZE][COLOR lime]ESTAMOS BUSCANDO LA PELI\nPACIENCIA POR FAVOR[/COLOR][/CAPITALIZE]')  
    xbmc.sleep(2000)
    dp.close()
    def sucuri(url):
        import re,base64
        import requests
        import xbmc, xbmcaddon
        headers= {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0","Cookie":cookies}

        x = requests.get(url,headers=headers,verify=False)  
        if six.PY3==True :             
            return x.text
        else :             
            return x.content
    url= sucuri(url)
    if 'article class="tolbox' in url:
        matches = plugintools.find_multiple_matches(url,'(<article class="tolbox".*?</article>)')
        for generos in matches:
 
            titulo=plugintools.find_single_match(generos,'data-title="(.*?)"') 
            texto=plugintools.find_single_match(generos,'data-desc="(.*?)"')
            if six.PY3==True :
                texto=unicodedata.normalize("NFKD", texto).encode("ascii","ignore").decode("ascii")
            else:
                texto=texto
            anio=plugintools.find_single_match(generos,'data-year="(.*?)"')      
            url=plugintools.find_single_match(generos,'a href="(.*?)"')        
            foto=plugintools.find_single_match(generos,'img src="(.*?)"')
 
            lenguaje=plugintools.find_single_match(generos,'class="langs">.*?<div class="(.*?)"')
            lenguaje2=plugintools.find_single_match(generos,'class="langs">.*?<div class=".*?<div class="(.*?)"')
 
            plugintools.set_view(plugintools.MOVIES,503)
            plugintools.add_item(action = "gnula_servers" ,title = "[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo+" [COLOR gold]"+anio+" [COLOR lime]"+lenguaje+" [COLOR red]"+lenguaje2+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",  plot = "[B][LOWERCASE][CAPITALIZE][COLOR white][COLOR orange]"+texto+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail =foto, fanart =foto,url =url,  folder=True )   
    else:  
        plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua][COLOR white] no hay resultado de la busqueda en esta web[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://vertele.eldiario.es/2019/10/31/noticias/Amazon-Netflix-Apple-TV-Espana_2172692762_14050592_660x371.jpg", fanart = "https://e00-marca.uecdn.es/assets/multimedia/imagenes/2020/11/20/16058878063470.jpg",  folder = False )  
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]--------------[COLOR yellow] opcion 2[COLOR aqua]-------------- [/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://vertele.eldiario.es/2019/10/31/noticias/Amazon-Netflix-Apple-TV-Espana_2172692762_14050592_660x371.jpg", fanart = "https://e00-marca.uecdn.es/assets/multimedia/imagenes/2020/11/20/16058878063470.jpg",  folder = False )        
    plugintools.set_view(plugintools.MOVIES,503)    
    url3= "https://95.216.8.160/search/"+d+"?__cpo=aHR0cHM6Ly93d3cxLmN1ZXZhbmEzLmFp"
    def cuerpo(url3):#torete
        import re , requests ,json        
        url=url3
        torete = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0","Cookie":cookies} 
        de = requests.get(url3,  headers=torete,verify=False)
        if six.PY3==True :
            return de.text
        else :
            return de.content
       
    url=cuerpo(url3)
    if 'class="xxx TPostMv">' in url:
        matches = plugintools.find_multiple_matches(url,'((?s)class="xxx TPostMv">.*?<a href=".*?".*?class="Year">.*?<.*?data-src=".*?".*?class="Title">.*?<.*?<p><p>.*?<.*?)')
        for generos in matches:
 
       
            url= plugintools.find_single_match(generos,'a href="(.*?)"')
            anio=plugintools.find_single_match(generos,'class="Year">(.*?)<')
            foto='https://95.216.8.160'+plugintools.find_single_match(generos,'data-src=".*?cuevana3.ai(.*?)".*?')+'?__cpo=aHR0cHM6Ly93d3cxLmN1ZXZhbmEzLmFp|cookie='+cookies
            titulo=plugintools.find_single_match(generos,'class="Title">(.*?)<')
            texto=plugintools.find_single_match(generos,'<p><p>(.*?)<').replace("[&hellip;]", "") 
            plugintools.set_view(plugintools.MOVIES,503)
            plugintools.add_item(action = "cuevana3_servers" , title = "[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo+"[COLOR gold] "+anio+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", plot="[B][LOWERCASE][CAPITALIZE][COLOR white]"+texto+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail =foto, fanart =foto,url =url,  folder=True )
            
    else:  
        plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua][COLOR white] no hay resultado de la busqueda en esta web[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://vertele.eldiario.es/2019/10/31/noticias/Amazon-Netflix-Apple-TV-Espana_2172692762_14050592_660x371.jpg", fanart = "https://e00-marca.uecdn.es/assets/multimedia/imagenes/2020/11/20/16058878063470.jpg",  folder = False )            
            
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]--------------[COLOR yellow] opcion 3[COLOR aqua]-------------- [/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://vertele.eldiario.es/2019/10/31/noticias/Amazon-Netflix-Apple-TV-Espana_2172692762_14050592_660x371.jpg", fanart = "https://e00-marca.uecdn.es/assets/multimedia/imagenes/2020/11/20/16058878063470.jpg",  folder = False ) 
    plugintools.set_view(plugintools.MOVIES,503)
    url= 'https://www.repelis2.co/buscar/'+d+'/'
    html='' 
    def sucuri(html):
        import re,base64
        import requests
        import xbmc, xbmcaddon
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0"}
        if six.PY3==True :
            x = requests.get(url).text
        else :
            x = requests.get(url).content
        return x 
    url= sucuri(html)
    if 'article class="tolbox"' in url:
        matches = plugintools.find_multiple_matches(url,'(?s)article class="tolbox" data-title=".*?".*?desc=".*?".*?data-year=".*?".*?href=".*?".*?img src=".*?".*?')
        for generos in matches:

            patron = plugintools.find_single_match(generos,'(?s)article class="tolbox" data-title="(.*?)".*?desc="(.*?)".*?data-year="(.*?)".*?href="(.*?)".*?img src="(.*?)".*?')
            url=patron[3]
            titulo = patron[0]
            foto = patron[4]  
            texto = patron[1]       
            anio = patron[2]
            plugintools.set_view(plugintools.MOVIES,503)
            plugintools.add_item(action = "repelis_servers" , title ="[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo+" [COLOR gold] "+anio+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", page=titulo, plot="[B][LOWERCASE][CAPITALIZE][COLOR gold]"+texto+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",thumbnail=foto, url=url, fanart =foto,   folder = True )  
        
    else:  
        plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua][COLOR white] no hay resultado de la busqueda en esta web[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://vertele.eldiario.es/2019/10/31/noticias/Amazon-Netflix-Apple-TV-Espana_2172692762_14050592_660x371.jpg", fanart = "https://e00-marca.uecdn.es/assets/multimedia/imagenes/2020/11/20/16058878063470.jpg",  folder = False )        
        
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]--------------[COLOR yellow] opcion 4[COLOR aqua]-------------- [/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://vertele.eldiario.es/2019/10/31/noticias/Amazon-Netflix-Apple-TV-Espana_2172692762_14050592_660x371.jpg", fanart = "https://e00-marca.uecdn.es/assets/multimedia/imagenes/2020/11/20/16058878063470.jpg",  folder = False ) 

    d=d.replace("%20", "+")    
    url="https://95.216.8.160/?s="+d+"&__cpo=aHR0cHM6Ly9vbmxpbmUudHVjaW5lY2xhc2ljby5lcw"
    def cuerpo(url):
        import re, requests, resolveurl, xbmc
        url =url
        headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
        "Upgrade-Insecure-Requests": "1",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache","cookie":cookies
    }
 
 
        logueo = requests.get(url, headers=headers,verify=False)
        if six.PY3==True :
            r = logueo.text
        else:
            r = logueo.content
        return r
    url=cuerpo(url)
    if 'class="result-item"><article>' in url:
        matches = plugintools.find_multiple_matches(url,'(?s)class="result-item"><article>.*?href=".*?".*?img src=".*?".*?alt=".*?".*?contenido"><p>.*?<.*?')
        for generos in matches: 
            patron = plugintools.find_single_match(generos,'(?s)class="result-item"><article>.*?href="(.*?)".*?img src="(.*?)".*?alt="(.*?)".*?contenido"><p>(.*?)<.*?')
            url=patron[0].replace("Descargar", "").replace("y ver Online", "")
            titulo = patron[2]
            foto = patron[1]   
            texto = patron[3]
            plugintools.set_view(plugintools.MOVIES,503)
            plugintools.add_item(action = "clasicos_del_server" , title ="[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", plot="[B][LOWERCASE][CAPITALIZE][COLOR white]"+texto+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",thumbnail=foto, url=url, fanart =foto,   folder = True )  
    else:  
        plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua][COLOR white] no hay resultado de la busqueda en esta web[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://vertele.eldiario.es/2019/10/31/noticias/Amazon-Netflix-Apple-TV-Espana_2172692762_14050592_660x371.jpg", fanart = "https://e00-marca.uecdn.es/assets/multimedia/imagenes/2020/11/20/16058878063470.jpg",  folder = False ) 
run()