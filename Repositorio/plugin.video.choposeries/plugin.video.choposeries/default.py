# -*- coding: utf-8 -*-
#------------------------------------------------------------
# chopocine - XBMC Add-on by Juarrox (juarrox@gmail.com)
# Version 0.2.5 (15.05.2014)
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Gracias a la librería plugintools de Jesús (www.mimediacenter.info)


import os
import sys
import urllib
import urllib2
import re
import xbmc
import xbmcgui
import xbmcaddon
import xbmcplugin
import plugintools



addon = xbmcaddon.Addon()
addonname = '[B][LOWERCASE][CAPITALIZE][COLOR white]chopo[COLOR gold]cine[/CAPITALIZE][/LOWERCASE][/B][/COLOR]'
icon = addon.getAddonInfo('icon')
myaddon = xbmcaddon.Addon("plugin.video.chopocine")
Set_Color = myaddon.getSetting('SetColor')
Set_View = myaddon.getSetting('SetView')



# Entry point
def run():
    
    plugintools.log("---> chopocine.run <---")
    plugintools.set_view(plugintools.LIST)
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
       action = params.get("action")
       url = params.get("url")
       exec action+"(params)"

    plugintools.close_item_list()

#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------
#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------
#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------


   
def main_list(params):
    plugintools.log("chopocine.main_list ")    
    plugintools.set_view(plugintools.LIST)  


    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE]   [COLOR blue]------------[COLOR yellow] series webs    [COLOR blue]-----------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://i.imgur.com/9a16ENI.jpg", fanart = "https://i.imgur.com/9a16ENI.jpg",  folder = False ) 
    
    plugintools.add_item(action = "mega_buscador" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]megabuscador [/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color,  thumbnail ="http://i.imgur.com/P1D92cf.png", fanart ="http://i.imgur.com/P1D92cf.png", folder = True )     




    
    plugintools.add_item(action = "menu_seriespapaya" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]series papaya [/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color,  thumbnail ="http://i.imgur.com/P1D92cf.png", fanart ="http://i.imgur.com/P1D92cf.png", folder = True ) 
    
    plugintools.add_item(action = "mundo_series_menu" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]mundoseries [/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color,  thumbnail ="https://i.imgur.com/Du21mll.jpg", fanart = "https://i.imgur.com/Du21mll.jpg", folder = True )   
 
    plugintools.add_item(action = "pepeseries_menu" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]pepeseries [/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color,  thumbnail ="https://st-listas.20minutos.es/images/2019-06/440207/5476186_640px.jpg?1567524986",url="https://pepecine.to/secure/titles?type=series&onlyStreamable=true&",plot='page=1', fanart = "https://i.imgur.com/x89QdGV.jpg", folder = True )
    
    
    plugintools.add_item(action = "danko_menu" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]series danko [/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color,  thumbnail ="https://beautifulgishi.com/wp-content/uploads/2018/09/series.jpg", fanart = "https://beautifulgishi.com/wp-content/uploads/2018/09/series.jpg",url="https://pepecine.to/secure/titles?type=series&onlyStreamable=true&",plot='page=1',  folder = True )
    
    plugintools.add_item(action = "series_dilo_menu" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]series dilo [/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color,  thumbnail ="https://i.imgur.com/bEWd9YM.jpg", fanart = "https://i.imgur.com/bEWd9YM.jpg", url="?format%5B%5D=tv", folder = True )  


    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]atresplayer [/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color,  thumbnail ="https://pbs.twimg.com/profile_images/1147997973399388160/-2tfDUQ8_400x400.png",url="plugin://plugin.video.atresplayerchopo", fanart ="https://como-funciona.com/wp-content/uploads/2019/11/1280x720.jpg", folder = True )     
    
    plugintools.add_item(action = "serie_mitele" , title = "[B][LOWERCASE][CAPITALIZE][COLOR white]mitele series[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",  thumbnail ="https://album.mediaset.es//parrillas/2019/10/04/e3ceb5881a0a1fdaad01296d7554868d1570194115.jpg", fanart = "https://album.mediaset.es/eimg/2017/11/03/RDrSzFS5nu4Eyyq5gGEES2.jpg",url="1",  folder = True ) 
    
    plugintools.add_item(action = "miniserie_mitele" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]miniseries mitele[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color,  thumbnail ="https://beautifulgishi.com/wp-content/uploads/2018/09/series.jpg", fanart = "https://beautifulgishi.com/wp-content/uploads/2018/09/series.jpg",url="https://pepecine.to/secure/titles?type=series&onlyStreamable=true&",plot='page=1',  folder = True ) 





    plugintools.add_item(action = "series_tve" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]series tve[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color,  thumbnail ="https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png", fanart = "https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png",  folder = True ) 
    
    
    
    
   
    
    

    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE]   [COLOR blue]------------[COLOR yellow] series retro, especiales y mas...    [COLOR blue]-----------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",  thumbnail ="https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png", fanart = "https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png",  folder = False )     

    plugintools.add_item(action = "series_tve_series_retro" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]super retros spain [/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color,  thumbnail ="https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png", fanart = "https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png",url="https://www.rtve.es/alacarta/programas/tve/archivo/1/?pageSize=15&order=1&criteria=asc&emissionFilter=all",  folder = True ) 
    
    
    plugintools.add_item(action = "miniserie" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]miniseries [/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color,  thumbnail ="https://as2.ftcdn.net/jpg/01/72/36/71/500_F_172367168_EBfTeRi6JI3vDUbwGmR1CKg51AsqZWPe.jpg", fanart = "https://as2.ftcdn.net/jpg/01/72/36/71/500_F_172367168_EBfTeRi6JI3vDUbwGmR1CKg51AsqZWPe.jpg",  folder = True ) 


    plugintools.add_item(action = "retrotv_series" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]retrotv series  todas[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color,  thumbnail ="https://i.imgur.com/hkMvrC4.jpg", fanart = "https://i.imgur.com/oArwph7.jpg", url="https://retroseriestv.com/seriestv/", folder = True ) 

    plugintools.add_item(action = "retrotv_series_generos" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]retrotv series  generos[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color,  thumbnail ="https://i.imgur.com/hkMvrC4.jpg", fanart = "https://i.imgur.com/oArwph7.jpg", url="https://retroseriestv.com/", folder = True ) 


    plugintools.add_item(action = "retrotv_series_anios" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]retrotv series  años[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color,  thumbnail ="https://i.imgur.com/hkMvrC4.jpg", fanart = "https://i.imgur.com/oArwph7.jpg", url="https://retroseriestv.com/", folder = True ) 

    plugintools.add_item(action = "retrotv_series_busca" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]retrotv series  buscador[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color,  thumbnail ="https://i.imgur.com/hkMvrC4.jpg", fanart = "https://i.imgur.com/oArwph7.jpg",  folder = True ) 
    


    plugintools.add_item(action = "series_netflix" , title = "[B][LOWERCASE][CAPITALIZE][COLOR white]series de [COLOR lime]([COLOR aqua]netflix,movistar,hbo,amazon,a3 player[COLOR lime])[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",  thumbnail ="https://cronicaglobal.elespanol.com/uploads/s1/67/38/06/3/series-streaming.jpeg", fanart = "https://cronicaglobal.elespanol.com/uploads/s1/67/38/06/3/series-streaming.jpeg",  folder = True )     
    
 


 
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]    *    *    *    *    *    [/COLOR][COLOR blue]menu[/COLOR] [COLOR lawngreen]series[/COLOR][COLOR red]papaya[COLOR yellow]    *    *    *    *    *    [/COLOR][/CAPITALIZE][/LOWERCASE][/B]", thumbnail ="https://i.imgur.com/9a16ENI.jpg", fanart = "https://i.imgur.com/9a16ENI.jpg",  folder = False ) 


def serie_mitele(params):  
    plugintools.log("chopocine.miniserie_mitele")    
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]------------------------------[COLOR yellow]series mitele[COLOR aqua]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://album.mediaset.es//parrillas/2019/10/04/e3ceb5881a0a1fdaad01296d7554868d1570194115.jpg", fanart = "https://album.mediaset.es/eimg/2017/11/03/RDrSzFS5nu4Eyyq5gGEES2.jpg",  folder = False ) 
    numero= params.get("url")    
    url= "https://mab.mediaset.es/1.0.0/get?oid=bitban&eid=%2FautomaticIndex%2Fmtweb%3Furl%3Dwww%252Emitele%252Ees%252Fseries%252Donline%252F%26page%3D"+numero+"%26id%3Da-z%26size%3D24"
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers(url, headers=request_headers)
    url = body.strip()
    page = plugintools.find_single_match(url,'totalPages":(.*?),"elementsPerPage"')
    matches = plugintools.find_multiple_matches(url,'("id":".*?","title":".*?false,"_elapsedSeconds)')       
    for generos in matches: 
        url = "https://www.mitele.es"+plugintools.find_single_match(generos,'href":"(.*?)"').replace('\\','')
        titulo = plugintools.find_single_match(generos,'title":"(.*?)"').replace('\u00ed','i').replace('\u00eda','e').replace('\u00f1','ñ').replace('\u00fa','u').replace('\u00f3','o').replace('\u00c1','a').replace('\u00e9','e').replace('\u00e1','a')
        foto = plugintools.find_single_match(generos,'src":"(.*?)".*?').replace('\\','')
        plugintools.add_item(action = "serie_mitele_temporadas" , title ="[B][LOWERCASE][CAPITALIZE][COLOR gold][COLOR white] "+titulo+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", url=url, thumbnail =foto,fanart =foto, folder = True )
    if page > numero :
        s='sumar'
        def dec(s):
            a = int("1")
            b = int(numero)
            suma = a+b
            return (str(suma))
        esto = dec(s)   


        plugintools.add_item( action="serie_mitele" ,url=esto, title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]ir a la pagina siguiente[/B][/COLOR][/CAPITALIZE][/LOWERCASE]",  thumbnail = "https://www.periodicoelpunto.com/wp-content/uploads/2019/03/flecha-siguiente.png",fanart = "https://www.periodicoelpunto.com/wp-content/uploads/2019/03/flecha-siguiente.png", folder=True )
        
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]------------------------------[COLOR yellow]series mitele[COLOR aqua]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://album.mediaset.es//parrillas/2019/10/04/e3ceb5881a0a1fdaad01296d7554868d1570194115.jpg", fanart = "https://album.mediaset.es/eimg/2017/11/03/RDrSzFS5nu4Eyyq5gGEES2.jpg",  folder = False )

def serie_mitele_temporadas(params):  
    plugintools.log("chopocine.miniserie_mitele")    
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]------------------------------[COLOR yellow]series mitele[COLOR aqua]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://album.mediaset.es//parrillas/2019/10/04/e3ceb5881a0a1fdaad01296d7554868d1570194115.jpg", fanart = "https://album.mediaset.es/eimg/2017/11/03/RDrSzFS5nu4Eyyq5gGEES2.jpg",  folder = False )
    url= params.get("url") 
    thumbnail= params.get("thumbnail")    
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers(url, headers=request_headers)
    url = body.strip()

    matches = plugintools.find_multiple_matches(url,'(<button class="itemListButton__buttonTitle-26fP"><a class="link__link-1f64" draggable="true" href=".*?" target="_self"><span>Temporada .*?</span></a></button></div)')       
    for generos in matches: 

        url = "https://www.mitele.es"+plugintools.find_single_match(generos,'draggable="true" href="(.*?)"')
        titulo = plugintools.find_single_match(generos,'target="_self"><span>(Temporada .*?)<')
        plugintools.add_item(action = "miniserie_mitele_server" , title ="[B][LOWERCASE][CAPITALIZE][COLOR gold][COLOR white] "+titulo+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", url=url, thumbnail =thumbnail,fanart =thumbnail, folder = True )
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]------------------------------[COLOR yellow]series mitele[COLOR aqua]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://album.mediaset.es//parrillas/2019/10/04/e3ceb5881a0a1fdaad01296d7554868d1570194115.jpg", fanart = "https://album.mediaset.es/eimg/2017/11/03/RDrSzFS5nu4Eyyq5gGEES2.jpg",  folder = False )

#------------------------------------dilo----------------------------dilo------------------------dilo----------------dilo-------------------------#------------------------------------dilo----------------------------dilo------------------------dilo----------------dilo-------------------------
#------------------------------------dilo----------------------------dilo------------------------dilo----------------dilo-------------------------
#------------------------------------dilo----------------------------dilo------------------------dilo----------------dilo-------------------------
#------------------------------------dilo----------------------------dilo------------------------dilo----------------dilo-------------------------
#------------------------------------dilo----------------------------dilo------------------------dilo----------------dilo-------------------------
#------------------------------------dilo----------------------------dilo------------------------dilo----------------dilo-------------------------
#------------------------------------dilo----------------------------dilo------------------------dilo----------------dilo-------------------------
#------------------------------------dilo----------------------------dilo------------------------dilo----------------dilo-------------------------
#------------------------------------dilo----------------------------dilo------------------------dilo----------------dilo-------------------------
#------------------------------------dilo----------------------------dilo------------------------dilo----------------dilo-------------------------
#------------------------------------dilo----------------------------dilo------------------------dilo----------------dilo-------------------------
#------------------------------------dilo----------------------------dilo------------------------dilo----------------dilo-------------------------
#------------------------------------dilo----------------------------dilo------------------------dilo----------------dilo-------------------------
#------------------------------------dilo----------------------------dilo------------------------dilo----------------dilo-------------------------

def series_dilo_menu(params):
    plugintools.log("chopocine.series_netflix_series "+repr(params))
    plugintools.add_item(action = "" , title ="[B][LOWERCASE][CAPITALIZE][COLOR yellow]----------[COLOR white] series [COLOR red]dilo[COLOR yellow]----------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://i.imgur.com/bEWd9YM.jpg", fanart = "https://i.imgur.com/bEWd9YM.jpg",  folder = False ) 

    plugintools.add_item(action = "seriesdilo_busca" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]series dilo buscador[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color,  thumbnail ="https://i.imgur.com/bEWd9YM.jpg", fanart = "https://i.imgur.com/bEWd9YM.jpg", url="?country%5B0%5D=ES", folder = True )

    plugintools.add_item(action = "series_dilo" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]series dilo todas[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color,  thumbnail ="https://i.imgur.com/bEWd9YM.jpg", fanart = "https://i.imgur.com/bEWd9YM.jpg", url="?format%5B%5D=tv", folder = True )




    plugintools.add_item(action = "series_dilo_anios" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]series dilo años[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color,  thumbnail ="https://i.imgur.com/bEWd9YM.jpg", fanart = "https://i.imgur.com/bEWd9YM.jpg",  folder = True )

    plugintools.add_item(action = "series_dilo_generos" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]series dilo generos[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color,  thumbnail ="https://i.imgur.com/bEWd9YM.jpg", fanart = "https://i.imgur.com/bEWd9YM.jpg",  folder = True )
    
    
    plugintools.add_item(action = "series_dilo_paises" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]series dilo paises[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color,  thumbnail ="https://i.imgur.com/bEWd9YM.jpg", fanart = "https://i.imgur.com/bEWd9YM.jpg",  folder = True )
    
    plugintools.add_item(action = "series_dilo" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]series dilo españolas[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color,  thumbnail ="https://i.imgur.com/bEWd9YM.jpg", fanart = "https://i.imgur.com/bEWd9YM.jpg", url="?country%5B0%5D=ES", folder = True )
    
    
    plugintools.add_item(action = "seriesdilo_lonuevo" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]series dilo lo nuevo hoy[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color,  thumbnail ="https://i.imgur.com/bEWd9YM.jpg", fanart = "https://i.imgur.com/bEWd9YM.jpg", url="?country%5B0%5D=ES", folder = True )
    
    
    plugintools.add_item(action = "" , title ="[B][LOWERCASE][CAPITALIZE][COLOR yellow]----------[COLOR white] series [COLOR red]dilo[COLOR yellow]----------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://i.imgur.com/bEWd9YM.jpg", fanart = "https://i.imgur.com/bEWd9YM.jpg",  folder = False ) 
    





def seriesdilo_lonuevo(params):  
    plugintools.log("chopocine.series_netflix_series "+repr(params))
    plugintools.add_item(action = "" , title ="[B][LOWERCASE][CAPITALIZE][COLOR yellow]----------[COLOR white] series dilo[COLOR red] busqueda[COLOR yellow]----------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://i.imgur.com/bEWd9YM.jpg", fanart = "https://i.imgur.com/bEWd9YM.jpg",  folder = False ) 
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers("https://www.dilo.nu/", headers=request_headers)
    url = body.strip()       
    matches = plugintools.find_multiple_matches(url,'(col-sm-12 mb-3">.*?href=".*?" title=".*?".*?src="https://cdn.dilo.nu/resize/backdrop/90x60@.*?".*?)')
    for generos in matches:    
        url = plugintools.find_single_match(generos,'col-sm-12 mb-3">.*?href="https://www.dilo.nu/(.*?)/"')
        foto = plugintools.find_single_match(generos,'src="https://cdn.dilo.nu/resize/backdrop/90x60@(.*?)".*?') 
        titulo = plugintools.find_single_match(generos,'title="(.*?)".*?')
        
        plugintools.add_item(action = "series_dilo_servers" ,url= url, title ="[B][LOWERCASE][CAPITALIZE][COLOR white]  "+titulo+"[COLOR aqua]  [/CAPITALIZE][/LOWERCASE][/B][/COLOR]" ,thumbnail ="https://cdn.dilo.nu/resize/backdrop/2600x2600@"+foto, fanart = "https://cdn.dilo.nu/resize/backdrop/2600x2600@"+foto, folder = True )      
    plugintools.add_item(action = "" , title ="[B][LOWERCASE][CAPITALIZE][COLOR yellow]----------[COLOR white] series dilo[COLOR red] busqueda[COLOR yellow]----------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://i.imgur.com/bEWd9YM.jpg", fanart = "https://i.imgur.com/bEWd9YM.jpg",  folder = False ) 

def seriesdilo_busca(params):  
    plugintools.log("chopocine.series_netflix_series "+repr(params))
    plugintools.add_item(action = "" , title ="[B][LOWERCASE][CAPITALIZE][COLOR yellow]----------[COLOR white] series dilo[COLOR red] busqueda[COLOR yellow]----------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://i.imgur.com/bEWd9YM.jpg", fanart = "https://i.imgur.com/bEWd9YM.jpg",  folder = False ) 
    dialog = xbmcgui.Dialog()
    d = dialog.input('[B][LOWERCASE][CAPITALIZE][COLOR orange]buscar una peli: ejemplo: [COLOR white]la casa de papel[/COLOR][/CAPITALIZE][/LOWERCASE][/B]', type=xbmcgui.INPUT_ALPHANUM).replace(" ", "+")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers("https://www.dilo.nu/search?s="+d, headers=request_headers)
    url = body.strip()       
    matches = plugintools.find_multiple_matches(url,'(<div class="col-lg-2 col-md-3 col-6 mb-3">.*?txt-gray-700">Duración)')
    for generos in matches:    
        url = plugintools.find_single_match(generos,'a href="(.*?)"')
        foto = plugintools.find_single_match(generos,'img src="(.*?)"') 
        titulo = plugintools.find_single_match(generos,'weight-500">(.*?)<')
        anio = plugintools.find_single_match(generos,'txt-size-12">(.*?)<')
        texto = plugintools.find_single_match(generos,'description">(.*?)<')
        
        plugintools.add_item(action = "series_dilo_temporadas" ,url= url, title ="[B][LOWERCASE][CAPITALIZE][COLOR white]  "+titulo+"[COLOR aqua]  "+anio+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" ,thumbnail =foto, fanart = foto, folder = True )      
    plugintools.add_item(action = "" , title ="[B][LOWERCASE][CAPITALIZE][COLOR yellow]----------[COLOR white] series dilo[COLOR red] busqueda[COLOR yellow]----------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://i.imgur.com/bEWd9YM.jpg", fanart = "https://i.imgur.com/bEWd9YM.jpg",  folder = False ) 


    
def series_dilo_paises(params):
    plugintools.log("chopocine.series_netflix_series "+repr(params))
    plugintools.add_item(action = "" , title ="[B][LOWERCASE][CAPITALIZE][COLOR yellow]----------[COLOR white] series [COLOR red]dilo[COLOR yellow]----------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://i.imgur.com/bEWd9YM.jpg", fanart = "https://i.imgur.com/bEWd9YM.jpg",  folder = False ) 
    thumbnail = params.get("thumbnail")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers("https://www.dilo.nu/catalogue", headers=request_headers)
    url = body.strip()       
    matches = plugintools.find_multiple_matches(url,'(name="country.*?for=".*?">.*?</label)')
    for generos in matches:    
        url = plugintools.find_single_match(generos,'name="country.*?for="(.*?)">.*?</label')
        titulo = plugintools.find_single_match(generos,'name="country.*?for=".*?">(.*?)</label')
        plugintools.add_item(action = "series_dilo" ,url= "?country%5B%5D="+url, title ="[B][LOWERCASE][CAPITALIZE][COLOR white]series del pais [COLOR aqua]"+titulo+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" ,thumbnail =thumbnail, fanart = thumbnail, folder = True ) 
    plugintools.add_item(action = "" , title ="[B][LOWERCASE][CAPITALIZE][COLOR yellow]----------[COLOR white] series [COLOR red]dilo[COLOR yellow]----------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://i.imgur.com/bEWd9YM.jpg", fanart = "https://i.imgur.com/bEWd9YM.jpg",  folder = False )     
    
    

def series_dilo_generos(params):
    plugintools.log("chopocine.series_netflix_series "+repr(params))
    plugintools.add_item(action = "" , title ="[B][LOWERCASE][CAPITALIZE][COLOR yellow]----------[COLOR white] series [COLOR red]dilo[COLOR yellow]----------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://i.imgur.com/bEWd9YM.jpg", fanart = "https://i.imgur.com/bEWd9YM.jpg",  folder = False ) 
    thumbnail = params.get("thumbnail")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers("https://www.dilo.nu/catalogue", headers=request_headers)
    url = body.strip()       
    matches = plugintools.find_multiple_matches(url,'(float-left txt-size-12 overflow-hidden">.*?for=".*?">.*?</label>)')
    for generos in matches:    
        url = plugintools.find_single_match(generos,'control-input" id="(.*?)" value="')
        
        plugintools.add_item(action = "series_dilo" ,url= "?genre%5B%5D="+url, title ="[B][LOWERCASE][CAPITALIZE][COLOR white]series del genero  [COLOR aqua]"+url+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" ,thumbnail =thumbnail, fanart = thumbnail, folder = True ) 
    plugintools.add_item(action = "" , title ="[B][LOWERCASE][CAPITALIZE][COLOR yellow]----------[COLOR white] series [COLOR red]dilo[COLOR yellow]----------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://i.imgur.com/bEWd9YM.jpg", fanart = "https://i.imgur.com/bEWd9YM.jpg",  folder = False ) 
def series_dilo_anios(params):
    plugintools.log("chopocine.series_netflix_series "+repr(params))
    plugintools.add_item(action = "" , title ="[B][LOWERCASE][CAPITALIZE][COLOR yellow]----------[COLOR white] series [COLOR red]dilo[COLOR yellow]----------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://i.imgur.com/bEWd9YM.jpg", fanart = "https://i.imgur.com/bEWd9YM.jpg",  folder = False ) 
    thumbnail = params.get("thumbnail")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers("https://www.dilo.nu/catalogue", headers=request_headers)
    url = body.strip()       
    matches = plugintools.find_multiple_matches(url,'(class="custom-control-input" id=".*?" name="year)')
    for generos in matches:    
        url = plugintools.find_single_match(generos,'custom-control-input" id="(\d+\d+\d+\d)" name="year')
        
        plugintools.add_item(action = "series_dilo" ,url= "?year%5B%5D="+url, title ="[B][LOWERCASE][CAPITALIZE][COLOR white]series del año [COLOR aqua] "+url+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" ,thumbnail =thumbnail, fanart = thumbnail, folder = True ) 
    
    plugintools.log("chopocine.series_netflix_series "+repr(params))
    plugintools.add_item(action = "" , title ="[B][LOWERCASE][CAPITALIZE][COLOR yellow]----------[COLOR white] series [COLOR red]dilo[COLOR yellow]----------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://i.imgur.com/bEWd9YM.jpg", fanart = "https://i.imgur.com/bEWd9YM.jpg",  folder = False )     

def series_dilo(params):
    plugintools.log("chopocine.series_netflix_series "+repr(params))
    plugintools.add_item(action = "" , title ="[B][LOWERCASE][CAPITALIZE][COLOR yellow]----------[COLOR white] series [COLOR red]dilo[COLOR yellow]----------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://i.imgur.com/bEWd9YM.jpg", fanart = "https://i.imgur.com/bEWd9YM.jpg",  folder = False ) 


    
    url = params.get("url")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers("https://www.dilo.nu/catalogue"+url, headers=request_headers)
    url = body.strip()       
    siguiente = plugintools.find_single_match(url,'class="active page-item"><span class="page-link.*? class="page-item">.*?tx-gray-500" href="(.*?)"')
    pagesiguiente = plugintools.find_single_match(url,'class="active page-item"><span class="page-link.*? class="page-item">.*?tx-gray-500" href=".*?">(.*?)<')
    matches = plugintools.find_multiple_matches(url,'(<div class="col-lg-2 col-md-3 col-6 mb-3">.*?txt-gray-700">Duración)')
    for generos in matches:    
        url = plugintools.find_single_match(generos,'a href="(.*?)"')
        foto = plugintools.find_single_match(generos,'img src="(.*?)"') 
        titulo = plugintools.find_single_match(generos,'weight-500">(.*?)<')
        anio = plugintools.find_single_match(generos,'txt-size-12">(.*?)<')
        texto = plugintools.find_single_match(generos,'description">(.*?)<')
        
        plugintools.add_item(action = "series_dilo_temporadas" ,url= url, title ="[B][LOWERCASE][CAPITALIZE][COLOR white]  "+titulo+"[COLOR aqua]  "+anio+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" ,thumbnail =foto, fanart = foto, folder = True )  

    if 'page' in siguiente:     
        plugintools.add_item( action="series_dilo" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow][COLOR lime]ir a la pagina siguiente""   [COLOR yellow]"+pagesiguiente+"[/B][/COLOR][/CAPITALIZE][/LOWERCASE]", url= siguiente, thumbnail = "https://www.periodicoelpunto.com/wp-content/uploads/2019/03/flecha-siguiente.png",fanart = "https://www.periodicoelpunto.com/wp-content/uploads/2019/03/flecha-siguiente.png", folder=True ) 

    
    plugintools.add_item(action = "" , title ="[B][LOWERCASE][CAPITALIZE][COLOR yellow]----------[COLOR white] series [COLOR red]dilo[COLOR yellow]----------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://i.imgur.com/bEWd9YM.jpg", fanart = "https://i.imgur.com/bEWd9YM.jpg",  folder = False )  
    
    
    
def series_dilo_temporadas(params):
    plugintools.log("chopocine.series_netflix_series "+repr(params))
    plugintools.add_item(action = "" , title ="[B][LOWERCASE][CAPITALIZE][COLOR yellow]----------[COLOR white] series [COLOR red]dilo temporadas[COLOR yellow]----------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://i.imgur.com/bEWd9YM.jpg", fanart = "https://i.imgur.com/bEWd9YM.jpg",  folder = False ) 
    thumbnail = params.get("thumbnail")   
    url = params.get("url")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers(url, headers=request_headers)
    url = body.strip()       
    ids = plugintools.find_single_match(url,'data-json=.."item_id": "(.*?)"')
    request_headers=[]   
    request_headers.append(['User-Agent','Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0'])
    request_headers.append(["Referer","https://www.dilo.nu/spides/"])           
    custom_post='item_id='+ids
    body,response_headers = plugintools.read_body_and_headers("https://www.dilo.nu/api/web/seasons.php", post=custom_post)
    url = body.strip()    
    matches = plugintools.find_multiple_matches(url,'("number":".*?description")')
    for generos in matches:
        temporada = plugintools.find_single_match(generos,'temporada-(.*?)"')    
        plugintools.add_item(action = "series_dilo_capitulos" ,url =custom_post+'&season_number='+temporada,thumbnail =thumbnail ,fanart =thumbnail, title ="[B][LOWERCASE][CAPITALIZE][COLOR white]  temporada[COLOR gold] "+temporada+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" , folder = True )     
    
    plugintools.add_item(action = "" , title ="[B][LOWERCASE][CAPITALIZE][COLOR yellow]----------[COLOR white] series [COLOR red]dilo temporadas[COLOR yellow]----------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://i.imgur.com/bEWd9YM.jpg", fanart = "https://i.imgur.com/bEWd9YM.jpg",  folder = False )     
    
    
def series_dilo_capitulos(params):
    plugintools.log("chopocine.series_netflix_series "+repr(params))
    plugintools.add_item(action = "" , title ="[B][LOWERCASE][CAPITALIZE][COLOR yellow]----------[COLOR white] series [COLOR red]dilo capitulos[COLOR yellow]----------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://i.imgur.com/bEWd9YM.jpg", fanart = "https://i.imgur.com/bEWd9YM.jpg",  folder = False ) 
    thumbnail = params.get("thumbnail")   
    custom = params.get("url")
    request_headers=[]   
    request_headers.append(['User-Agent','Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0'])
    request_headers.append(["Referer","https://www.dilo.nu/spides/"])           
    custom_post=custom
    body,response_headers = plugintools.read_body_and_headers("https://www.dilo.nu/api/web/episodes.php", post=custom_post)
    url = body.strip()    
    matches = plugintools.find_multiple_matches(url,'(season_number":".*?",".*?","description":".*?","audio":")')
    for generos in matches:
        temporada = plugintools.find_single_match(generos,'season_number":"(.*?)"') 
        titulo = plugintools.find_single_match(generos,'season_number":".*?permalink":"(.*?)"') 
        name = plugintools.find_single_match(generos,'season_number":".*?","number":".*?","name":"(.*?)","') 
        
        plugintools.add_item(action = "series_dilo_servers" ,url =titulo,thumbnail =thumbnail ,fanart =thumbnail, title ="[B][LOWERCASE][CAPITALIZE][COLOR white][COLOR gold] "+titulo+" [COLOR white] "+name+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" , folder = True ) 
    plugintools.add_item(action = "" , title ="[B][LOWERCASE][CAPITALIZE][COLOR yellow]----------[COLOR white] series [COLOR red]dilo capitulos[COLOR yellow]----------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://i.imgur.com/bEWd9YM.jpg", fanart = "https://i.imgur.com/bEWd9YM.jpg",  folder = False ) 
def series_dilo_servers(params):
    plugintools.log("chopocine.series_netflix_series "+repr(params))
    plugintools.add_item(action = "" , title ="[B][LOWERCASE][CAPITALIZE][COLOR yellow]----------[COLOR white] series [COLOR red]dilo servidores[COLOR yellow]----------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://i.imgur.com/bEWd9YM.jpg", fanart = "https://i.imgur.com/bEWd9YM.jpg",  folder = False ) 
    thumbnail = params.get("thumbnail")   
    url = "https://www.dilo.nu/"+params.get("url")+"/"
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers(url, headers=request_headers)
    url = body.strip()    
    matches = plugintools.find_multiple_matches(url,'(items-center py-2 sv_.*?class="ml-auto px-3)')
    for generos in matches:
        temporada = plugintools.find_single_match(generos,'py-2 sv_(.*?)"').replace('powvideo_net','powvideo_net [COLOR red]no elegir').replace('streamplay_to','streamplay_to [COLOR red]no elegir').replace('vidtodo_com','vidtodo_com [COLOR red]no elegir').replace('waaw_tv','waaw_tv [COLOR red]no elegir').replace('flix555_com','flix555_com [COLOR red]no elegir').replace('jetload_net','jetload_net [COLOR red]no elegir')
        link = plugintools.find_single_match(generos,'link="(.*?)"')

        Reproducir = plugintools.find_single_match(generos,'Reproducir en(.*?)<')

        request_headers=[]
        request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
        body,response_headers = plugintools.read_body_and_headers(link, headers=request_headers)
        url = body.strip()           
        clipwachin = plugintools.find_single_match(url,'iframe class="" src="https://clipwatching.com/embed-(.*?)"')
        gamo = plugintools.find_single_match(url,'a href="(htt.*?//gamovideo.*?)"')
        if 'html' in clipwachin:
            request_headers=[]
            request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
            body,response_headers = plugintools.read_body_and_headers("https://clipwatching.com/"+clipwachin, headers=request_headers)
            url = body.strip()          
            source = plugintools.find_single_match(url,'sources: ."(.*?)"')
            plugintools.add_item(action = "play_links" ,  title ="[B][LOWERCASE][CAPITALIZE][COLOR white][COLOR gold] "+temporada+"  [COLOR white]"+Reproducir+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", url = source,thumbnail=thumbnail,fanart = thumbnail,  folder=False,  isPlayable = True )
    
        plugintools.add_item(action = "play_resolver" ,url =gamo+clipwachin,thumbnail =thumbnail ,fanart =thumbnail, title ="[B][LOWERCASE][CAPITALIZE][COLOR white][COLOR gold] "+temporada+" [COLOR white] "+Reproducir+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" , folder=False,  isPlayable = True )    


        
    
    plugintools.add_item(action = "" , title ="[B][LOWERCASE][CAPITALIZE][COLOR yellow]----------[COLOR white] series [COLOR red]dilo servidores[COLOR yellow]----------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://i.imgur.com/bEWd9YM.jpg", fanart = "https://i.imgur.com/bEWd9YM.jpg",  folder = False )     
    
    
    
#especiales-----------------especiales--------------------------------especiales---------------------------------------------especiales----------especiales-----------------especiales--------------------------------especiales---------------------------------------------especiales----------especiales-----------------especiales--------------------------------especiales---------------------------------------------especiales----------especiales-----------------especiales--------------------------------especiales---------------------------------------------especiales----------especiales-----------------especiales--------------------------------especiales---------------------------------------------especiales----------especiales-----------------especiales--------------------------------especiales---------------------------------------------especiales----------especiales-----------------especiales--------------------------------especiales---------------------------------------------especiales----------especiales-----------------especiales--------------------------------especiales---------------------------------------------especiales----------especiales-----------------especiales--------------------------------especiales---------------------------------------------especiales----------especiales-----------------especiales--------------------------------especiales---------------------------------------------especiales----------

def series_netflix(params):
    plugintools.log("chopocine.series_netflix "+repr(params))
    plugintools.add_item(action = "" , title ="[B][LOWERCASE][CAPITALIZE][COLOR yellow]----[COLOR orange] series netflix,movistar,hbo,amazon,a3 player[COLOR yellow]----[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://cronicaglobal.elespanol.com/uploads/s1/67/38/06/3/series-streaming.jpeg", fanart = "https://cronicaglobal.elespanol.com/uploads/s1/67/38/06/3/series-streaming.jpeg",  folder = False )    
    thumbnail = params.get("thumbnail") 
    fanart = params.get("thumbnail")
    data = plugintools.read("https://pastebin.com/raw/LJcc6sCz")

    matches = plugintools.find_multiple_matches(data,'(http.*?proveedor/.*?/.*?,.*?,)')
    for generos in matches:
        titulo = plugintools.find_single_match(generos,'http.*?proveedor/(.*?)/.*?,.*?,')
        url1 = plugintools.find_single_match(generos,'http.*?proveedor/.*?/.*?,(.*?),')
        foto = plugintools.find_single_match(generos,'http.*?proveedor/(.*?)/.*?,.*?,').replace('hbo','https://cr00.epimg.net/radio/imagenes/2019/07/31/entretenimiento/1564585474_035981_1564586869_noticia_normal.jpg').replace('netflix','https://media.metrolatam.com/2018/11/09/image5ba9601010c3f-210e0e1fb7bf5879e0f9c24f23ef50ba-600x400.jpg').replace('movistar-plus','https://i.blogs.es/928bbf/movistar/450_1000.jpg').replace('amazon-prime-video','https://images-na.ssl-images-amazon.com/images/I/411j1k1u9yL.png').replace('atres-player','https://miro.medium.com/max/2625/1*S59PGDhLvGfvCWR_y6gPGg.jpeg') 
        numero="1"
        url2='https://apis.justwatch.com/content/titles/es_ES/popular?body={"age_certifications":[],"content_types":["show"],"genres":[],"languages":null,"min_price":null,"max_price":null,"monetization_types":["ads","buy","flatrate","free","rent"],"presentation_types":[],"providers":["'+url1+'"],"release_year_from":null,"release_year_until":null,"scoring_filter_types":null,"timeline_type":null,"q":null,"person_id":null,"sort_by":"title","sort_asc":true,"query":null,"page":'+numero+',"page_size":150}'    
        request_headers=[]
        request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
        body,response_headers = plugintools.read_body_and_headers(url2, headers=request_headers)
        url = body.strip()     
        titulo2 = plugintools.find_single_match(url,'total_results":(.*?),"')        
        plugintools.add_item(action = "series_netflix_series" , title ="[B][LOWERCASE][CAPITALIZE][COLOR white]series "+titulo+" [COLOR aqua] "+titulo2+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" , url='https://apis.justwatch.com/content/titles/es_ES/popular?body={"age_certifications":[],"content_types":["show"],"genres":[],"languages":null,"min_price":null,"max_price":null,"monetization_types":["ads","buy","flatrate","free","rent"],"presentation_types":[],"providers":["'+url1+'"],"release_year_from":null,"release_year_until":null,"scoring_filter_types":null,"timeline_type":null,"q":null,"person_id":null,"sort_by":"title","sort_asc":true,"query":null,"page":', plot="1" ,thumbnail =foto, fanart = foto, folder = True )


    plugintools.add_item(action = "" , title ="[B][LOWERCASE][CAPITALIZE][COLOR yellow]----[COLOR orange] series netflix,movistar,hbo,amazon,a3 player[COLOR yellow]----[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://cronicaglobal.elespanol.com/uploads/s1/67/38/06/3/series-streaming.jpeg", fanart = "https://cronicaglobal.elespanol.com/uploads/s1/67/38/06/3/series-streaming.jpeg",  folder = False )   


def series_netflix_series(params):
    plugintools.log("chopocine.series_netflix_series "+repr(params))
    plugintools.add_item(action = "" , title ="[B][LOWERCASE][CAPITALIZE][COLOR yellow]----[COLOR orange] series netflix,movistar,hbo,amazon,a3 player[COLOR yellow]----[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://cronicaglobal.elespanol.com/uploads/s1/67/38/06/3/series-streaming.jpeg", fanart = "https://cronicaglobal.elespanol.com/uploads/s1/67/38/06/3/series-streaming.jpeg",  folder = False )    
    thumbnail = params.get("thumbnail") 
    proove = params.get("url")
    numero = params.get("plot")
    url2=proove+numero    
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers(url2+',"page_size":150}', headers=request_headers)
    url = body.strip()       
    pagina = plugintools.find_single_match(url,'"page":(.*?),"page_size')  
    total_pagina = plugintools.find_single_match(url,'"total_pages":(.*?),"total')   
    matches = plugintools.find_multiple_matches(url,'"title":".*?poster":".*?.profile..*?')
    for generos in matches:    
        titulo = plugintools.find_single_match(generos,'"title":"([^":]+).*?').replace(' ','+').replace(':','+').replace('(','').replace(')','').replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u')  
        foto = plugintools.find_single_match(generos,'poster":"(.*?).profile..*?') 
        titulo_fin = plugintools.find_single_match(generos,'"title":"([^":]+).*?')
        
        plugintools.add_item(action = "miniseries_buscador" ,url= titulo, title ="[B][LOWERCASE][CAPITALIZE][COLOR white] [COLOR aqua] "+titulo_fin+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" ,thumbnail ="https://images.justwatch.com"+foto+"s166", fanart = "https://images.justwatch.com"+foto+"s166",plot=numero, folder = True )
        
    if pagina < total_pagina:
        s="hola"         
        def dec(s):
            a = int("1")
            b = int(pagina)
            suma = a+b
            return (str(suma))
        esto = dec(s)


        plugintools.add_item( action="series_netflix_series" ,url=proove, title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]ir a la pagina siguiente [COLOR yellow]"+esto+"[/B][/COLOR][/CAPITALIZE][/LOWERCASE]", plot=esto, thumbnail = "https://www.periodicoelpunto.com/wp-content/uploads/2019/03/flecha-siguiente.png",fanart = "https://www.periodicoelpunto.com/wp-content/uploads/2019/03/flecha-siguiente.png", folder=True )


    plugintools.add_item(action = "" , title ="[B][LOWERCASE][CAPITALIZE][COLOR yellow]----[COLOR orange] series netflix,movistar,hbo,amazon,a3 player[COLOR yellow]----[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://cronicaglobal.elespanol.com/uploads/s1/67/38/06/3/series-streaming.jpeg", fanart = "https://cronicaglobal.elespanol.com/uploads/s1/67/38/06/3/series-streaming.jpeg",  folder = False )  



def retrotv_series_busca(params):  
    plugintools.log("chopocine.miniserie_mitele")    
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]------------------------------[COLOR %s]retrotv series [COLOR aqua]------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color,  thumbnail ="https://i.imgur.com/hkMvrC4.jpg", fanart = "https://i.imgur.com/oArwph7.jpg",  folder = False )   
    dialog = xbmcgui.Dialog()
    d = dialog.input('[B][LOWERCASE][CAPITALIZE][COLOR orange]buscar una peli: ejemplo: [COLOR white]la casa de papel[/COLOR][/CAPITALIZE][/LOWERCASE][/B]', type=xbmcgui.INPUT_ALPHANUM).replace(" ", "+")
    url= "https://retroseriestv.com/?s="+d
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers(url, headers=request_headers)
    url = body.strip()
    matches = plugintools.find_multiple_matches(url,'(class="image">.*?a href=".*?">.*?<p>.*?</p>)')      
    for generos in matches: 
        url = plugintools.find_single_match(generos,'href="(.*?)"')
        titulo = plugintools.find_single_match(generos,'alt="(.*?)"')  
        foto = plugintools.find_single_match(generos,'img src="(.*?)"')
        anio = plugintools.find_single_match(generos,'class="year">(.*?)<.*?')
        texto = plugintools.find_single_match(generos,'class="contenido"><p>(.*?)</p>')        
        plugintools.add_item(action = "retrotv_series_temporadas" , title ="[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo+" [COLOR gold] "+anio+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail =foto, fanart = foto,url=url, plot=texto, folder = True )


def retrotv_series_anios(params):  
    plugintools.log("chopocine.miniserie_mitele")    
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]------------------------------[COLOR %s]retrotv series [COLOR aqua]------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color,  thumbnail ="https://i.imgur.com/hkMvrC4.jpg", fanart = "https://i.imgur.com/oArwph7.jpg",  folder = False )   
    url = params.get("url")
    thumbnail = params.get("thumbnail")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers(url, headers=request_headers)
    url = body.strip()
    matches = plugintools.find_multiple_matches(url,'(href="https://retroseriestv.com/lanzamiento/.*?">.*?<)')       
    for generos in matches: 
        url = plugintools.find_single_match(generos,'href="(https://retroseriestv.com/lanzamiento/.*?)">.*?<')
        titulo = plugintools.find_single_match(generos,'href="https://retroseriestv.com/lanzamiento/.*?">(.*?)<').replace('amp;','')       
        plugintools.add_item(action = "retrotv_series" , title ="[B][LOWERCASE][CAPITALIZE][COLOR white]retroseries del año "+titulo+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail =thumbnail, fanart = thumbnail,url=url,  folder = True )

def retrotv_series_generos(params):  
    plugintools.log("chopocine.miniserie_mitele")    
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]------------------------------[COLOR %s]retrotv series [COLOR aqua]------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color,  thumbnail ="https://i.imgur.com/hkMvrC4.jpg", fanart = "https://i.imgur.com/oArwph7.jpg",  folder = False )   
    url = params.get("url")
    thumbnail = params.get("thumbnail")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers(url, headers=request_headers)
    url = body.strip()
    matches = plugintools.find_multiple_matches(url,'(class="cat-item cat-item-.*?href="https://retroseriestv.com/genero/.*?">.*?<)')       
    for generos in matches: 
        url = plugintools.find_single_match(generos,'href="(https://retroseriestv.com/genero/.*?)"')
        titulo = plugintools.find_single_match(generos,'class="cat-item cat-item-.*?href="https://retroseriestv.com/genero/.*?">(.*?)<').replace('amp;','')       
        plugintools.add_item(action = "retrotv_series" , title ="[B][LOWERCASE][CAPITALIZE][COLOR white]retroseries del genero "+titulo+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail =thumbnail, fanart = thumbnail,url=url,  folder = True )




def retrotv_series(params):  
    plugintools.log("chopocine.miniserie_mitele")    
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]------------------------------[COLOR %s]retrotv series [COLOR aqua]------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color,  thumbnail ="https://i.imgur.com/hkMvrC4.jpg", fanart = "https://i.imgur.com/oArwph7.jpg",  folder = False )   
    url = params.get("url")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers(url, headers=request_headers)
    url = body.strip()
    siguiente = plugintools.find_single_match(url,"class=.current.>.*?</span><a href='(.*?)'")
    matches = plugintools.find_multiple_matches(url,'(<article id="post-\d+" class="item tvshows">.*?</article>)')       
    for generos in matches: 
        foto = plugintools.find_single_match(generos,'class="poster"><img src="(.*?)"')
        titulo = plugintools.find_single_match(generos,'" alt="(.*?)"><div')
        url = plugintools.find_single_match(generos,'</div><a href="(.*?)"')
        fecha = plugintools.find_single_match(generos,'</h3> <span>(.*?)<')
        texto = plugintools.find_single_match(generos,'class="texto">(.*?)<')         
        plugintools.add_item(action = "retrotv_series_temporadas" , title ="[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo+" [COLOR gold]"+fecha+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail =foto, fanart = foto,url=url, plot=texto, folder = True )
    if 'http' in siguiente:     
        plugintools.add_item( action="retrotv_series" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow][COLOR lime]ir a la pagina siguiente[/B][/COLOR][/CAPITALIZE][/LOWERCASE]", url= siguiente, thumbnail = "https://www.periodicoelpunto.com/wp-content/uploads/2019/03/flecha-siguiente.png",fanart = "https://www.periodicoelpunto.com/wp-content/uploads/2019/03/flecha-siguiente.png", folder=True ) 
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]------------------------------[COLOR %s]retrotv series [COLOR aqua]------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color,  thumbnail ="https://i.imgur.com/hkMvrC4.jpg", fanart = "https://i.imgur.com/oArwph7.jpg",  folder = False ) 

def retrotv_series_temporadas(params):  
    plugintools.log("chopocine.miniserie_mitele")    
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]------------------------------[COLOR %s]retrotv series [COLOR aqua]------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color,  thumbnail ="https://i.imgur.com/hkMvrC4.jpg", fanart = "https://i.imgur.com/oArwph7.jpg",  folder = False )   
    url = params.get("url")
    thumbnail = params.get("thumbnail")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers(url, headers=request_headers)
    url = body.strip()
    matches = plugintools.find_multiple_matches(url,"(class='numerando'>.*?<.*?href='.*?'>.*?<.*?date'>.*?<)")       
    for generos in matches: 
        numerando = plugintools.find_single_match(generos,"class='numerando'>(.*?)<")
        titulo = plugintools.find_single_match(generos,"href='.*?'>(.*?)<")
        url = plugintools.find_single_match(generos,"href='(.*?)'")
        fecha = plugintools.find_single_match(generos,"date'>(.*?)<")         
        plugintools.add_item(action = "retrotv_series_server" , title ="[B][LOWERCASE][CAPITALIZE][COLOR white]"+numerando+" "+titulo+" [COLOR gold]"+fecha+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail =thumbnail, fanart = thumbnail,url=url,  folder = True )        
        
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]------------------------------[COLOR %s]retrotv series [COLOR aqua]------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color,  thumbnail ="https://i.imgur.com/hkMvrC4.jpg", fanart = "https://i.imgur.com/oArwph7.jpg",  folder = False ) 
    
    
    
    
def retrotv_series_server(params):  
    plugintools.log("chopocine.miniserie_mitele")    
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]------------------------------[COLOR %s]retrotv series [COLOR aqua]------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color,  thumbnail ="https://i.imgur.com/hkMvrC4.jpg", fanart = "https://i.imgur.com/oArwph7.jpg",  folder = False )  
    url = params.get("url")
    thumbnail = params.get("thumbnail")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers(url, headers=request_headers)
    url = body.strip()
    matches = plugintools.find_multiple_matches(url,"(id='player-option-1.*?</li>)")       
    for generos in matches: 
        numerando = plugintools.find_single_match(generos,"id='player-(option-1).*?data-post='.*?' data-nume='.*?'.*?class='title'>.*?<.*?class='server'>.*?<")
        post = plugintools.find_single_match(generos,"id='player-option-1.*?data-post='(.*?)' data-nume='.*?'.*?class='title'>.*?<.*?class='server'>.*?<")
        nume = plugintools.find_single_match(generos,"id='player-option-1.*?data-post='.*?' data-nume='(.*?)'.*?class='title'>.*?<.*?class='server'>.*?<")
        title = plugintools.find_single_match(generos,"id='player-option-1.*?data-post='.*?' data-nume='.*?'.*?class='title'>(.*?)<.*?class='server'>.*?<") 
        server = plugintools.find_single_match(generos,"id='player-option-1.*?data-post='.*?' data-nume='.*?'.*?class='title'>.*?<.*?class='server'>(.*?)<") 

        ports='action=doo_player_ajax&post='+post+'&nume='+nume+'&type=tv' 
        request_headers=[]   
        request_headers.append(['User-Agent','Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0'])
        request_headers.append(["Referer","https://retroseriestv.com/episodios/expediente-x-1x1/"])           
        custom_post=ports
        body,response_headers = plugintools.read_body_and_headers("https://retroseriestv.com/wp-admin/admin-ajax.php", post=custom_post)
        url = body.strip()
        url = plugintools.find_single_match(url,"rptss' src='(https://www.fembed.com.*?)'")
        
        plugintools.add_item(action = "play_resolver" , title ="[B][LOWERCASE][CAPITALIZE][COLOR lime] gamovideo [COLOR gold]"+title+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail =thumbnail, fanart = thumbnail,url=url,  folder=False,  isPlayable = True )        
        
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]------------------------------[COLOR %s]retrotv series [COLOR aqua]------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color,  thumbnail ="https://i.imgur.com/hkMvrC4.jpg", fanart = "https://i.imgur.com/oArwph7.jpg",  folder = False ) 
def miniserie(params):  
    plugintools.log("chopocine.miniserie_mitele")    
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]miniseries [/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color,  thumbnail ="https://as2.ftcdn.net/jpg/01/72/36/71/500_F_172367168_EBfTeRi6JI3vDUbwGmR1CKg51AsqZWPe.jpg", fanart = "https://as2.ftcdn.net/jpg/01/72/36/71/500_F_172367168_EBfTeRi6JI3vDUbwGmR1CKg51AsqZWPe.jpg",  folder = False )   
    url= "https://www.filmaffinity.com/es/listtopmovies.php?list_id=345"
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers(url, headers=request_headers)
    url = body.strip()
    
    matches = plugintools.find_multiple_matches(url,'(div class="mc-title"><a  href=".*?" title=".*?">.*?</a>.*?<img class="nflag")')       
    for generos in matches: 
        titulo0 = plugintools.find_single_match(generos,'title="([^":\(]+).*?')
        titulo = plugintools.find_single_match(generos,'title="([A-z]+.*?[A-z][^ :]+)').replace(' (','').replace(' ','+').replace('á','a').replace('Á','A').replace('É','E').replace('é','e').replace('í','i').replace('Í','I').replace('Ó','O').replace('ó','o').replace('ú','u').replace('Ú','U').replace(',','').replace('Miniserie','').replace('Serie','').replace(':','')
        anio = plugintools.find_single_match(generos,'.*?</a> (.*?)<')
        
        
        
        plugintools.add_item(action = "miniseries_buscador" , title ="[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo0+" [COLOR gold]"+anio+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://as2.ftcdn.net/jpg/01/72/36/71/500_F_172367168_EBfTeRi6JI3vDUbwGmR1CKg51AsqZWPe.jpg", fanart = "https://as2.ftcdn.net/jpg/01/72/36/71/500_F_172367168_EBfTeRi6JI3vDUbwGmR1CKg51AsqZWPe.jpg",url=titulo,  folder = True )
        
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]miniseries [/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color,  thumbnail ="https://as2.ftcdn.net/jpg/01/72/36/71/500_F_172367168_EBfTeRi6JI3vDUbwGmR1CKg51AsqZWPe.jpg", fanart = "https://as2.ftcdn.net/jpg/01/72/36/71/500_F_172367168_EBfTeRi6JI3vDUbwGmR1CKg51AsqZWPe.jpg",  folder = False )   
def miniseries_buscador(params):
    plugintools.log("chopocine.series_papaya_buscador "+repr(params))
    plugintools.set_view(plugintools.LIST)
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR gold]---[COLOR aqua]series papaya resultado de la busqueda[COLOR gold]---[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="http://i.imgur.com/P1D92cf.png", fanart ="http://i.imgur.com/P1D92cf.png",  folder = False ) 
    url = params.get("url")
    request_headers=[]   
    request_headers.append(['User-Agent','Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0'])
    request_headers.append(["Referer","https://www.seriespapaya.nu/busqueda/"])           
    custom_post="searchquery="+url
    body,response_headers = plugintools.read_body_and_headers("https://www.seriespapaya.nu/busqueda/", post=custom_post)
    url = body.strip()
    matches = plugintools.find_multiple_matches(url,'(class="capitulo-caja.*?style="display: table.*? </div>)')
    for generos in matches: 
        titulo = plugintools.find_single_match(generos,'165px; ">\s*(.*?)\s*<')
        url = "https://www.seriespapaya.nu"+plugintools.find_single_match(generos," onclick=.location.href='(.*?)'")
        foto = "https://www.seriespapaya.nu"+plugintools.find_single_match(generos,"image: url.'(.*?)'")
        
        plugintools.add_item(action = "series_papaya_temporadas" , thumbnail=foto,fanart =foto,title ="[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",url= url,   folder = True )
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR gold]---[COLOR aqua]series papaya resultado de la busqueda[COLOR gold]---[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="http://i.imgur.com/P1D92cf.png", fanart ="http://i.imgur.com/P1D92cf.png",  folder = False )   
#-----------tve------------------------tve------------------------------------tve--------------------------tve-----------------------tve------------#-----------tve------------------------tve------------------------------------tve--------------------------tve-----------------------tve------------  #-----------tve------------------------tve------------------------------------tve--------------------------tve-----------------------tve------------  #-----------tve------------------------tve------------------------------------tve--------------------------tve-----------------------tve------------  #-----------tve------------------------tve------------------------------------tve--------------------------tve-----------------------tve------------  #-----------tve------------------------tve------------------------------------tve--------------------------tve-----------------------tve------------  #-----------tve------------------------tve------------------------------------tve--------------------------tve-----------------------tve------------  #-----------tve------------------------tve------------------------------------tve--------------------------tve-----------------------tve------------  #-----------tve------------------------tve------------------------------------tve--------------------------tve-----------------------tve------------  #-----------tve------------------------tve------------------------------------tve--------------------------tve-----------------------tve------------  #-----------tve------------------------tve------------------------------------tve--------------------------tve-----------------------tve------------     
  
def series_tve_series_retro(params):
    plugintools.log("chopocine.cinetuxanios "+repr(params))
    plugintools.add_item(action = "" , title ="[B][LOWERCASE][CAPITALIZE][COLOR yellow]------------[COLOR white] tve[COLOR yellow]------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png", fanart = "https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png",  folder = False )    
    thumbnail = params.get("thumbnail") 
    url = params.get("url")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers(url, headers=request_headers)
    url = body.strip()
    siguiente = plugintools.find_single_match(url,'class="siguiente">.*?<a name="paginaIR" href="(.*?)"').replace("amp;", "")
    matches = plugintools.find_multiple_matches(url,'col_tit" id=".*?".*?href="https://www.rtve.es/alacarta/videos/.*?".*?title="Ver .*?">.*?<.*? class="col_cat">')
    for generos in matches:

        titulo = plugintools.find_single_match(generos,'title="Ver .*?">(.*?)<')
        foto = plugintools.find_single_match(generos,'img src="(.*?)"')
        pageid = plugintools.find_single_match(generos,'col_tit" id="(.*?)"')
        url='/alacarta/interno/contenttable.shtml?pbq=1&module=OTHER&sectionFilter=-1&orderCriteria=DESC&modl=TOC&locale=es&pageSize=100&ctx='+pageid+'&typeFilter=39816&mode=TEXT'
        plugintools.add_item(action = "series_tve_temporada" , title ="[B][LOWERCASE][CAPITALIZE][COLOR yellow][COLOR aqua]"+titulo+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" ,url =url, thumbnail =foto,fanart = foto,folder = True )   
    if 'alacarta' in siguiente:  
    
    
    
        plugintools.add_item( action="series_tve_series_retro" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow][COLOR lime]ir a la pagina siguiente[/B][/COLOR][/CAPITALIZE][/LOWERCASE]", url= 'https://www.rtve.es'+siguiente, thumbnail = "https://www.periodicoelpunto.com/wp-content/uploads/2019/03/flecha-siguiente.png",fanart = "https://www.periodicoelpunto.com/wp-content/uploads/2019/03/flecha-siguiente.png", folder=True )  

def series_tve(params):
    plugintools.log("chopocine.cinetuxanios "+repr(params))
    plugintools.add_item(action = "" , title ="[B][LOWERCASE][CAPITALIZE][COLOR yellow]------------[COLOR white] tve[COLOR yellow]------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png", fanart = "https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png",  folder = False )    
    thumbnail = params.get("thumbnail") 
    fanart = params.get("thumbnail")
    data = plugintools.read("https://pastebin.com/raw/G5ZPhUN1")

    matches = plugintools.find_multiple_matches(data,'<a href=".*?" title=".*?">')
    for generos in matches:
        url = plugintools.find_single_match(generos,'a href="(.*?)"')
        titulo = plugintools.find_single_match(generos,'title="(.*?)"')
        
        
        plugintools.add_item(action = "series_tve_series" , title ="[B][LOWERCASE][CAPITALIZE][COLOR yellow]series [COLOR aqua]"+titulo+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" ,url ='http://www.rtve.es'+url , thumbnail ="https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png", fanart = "https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png", folder = True )
        
        
    plugintools.add_item(action = "" , title ="[B][LOWERCASE][CAPITALIZE][COLOR yellow]------------[COLOR white] tve[COLOR yellow]------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png", fanart = "https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png",  folder = False )   
    

    
def series_tve_series(params):
    plugintools.log("chopocine.cinetuxanios "+repr(params))
    plugintools.add_item(action = "" , title ="[B][LOWERCASE][CAPITALIZE][COLOR yellow]------------[COLOR white] tve[COLOR yellow]------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png", fanart = "https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png",  folder = False )    
    thumbnail = params.get("thumbnail") 
    url = params.get("url")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers(url, headers=request_headers)
    url = body.strip()
    
    matches = plugintools.find_multiple_matches(url,'<article>.*?</article>')
    for generos in matches:
        url5 = plugintools.find_single_match(generos,'<a href="(.*?)"').replace("http://", "https://")
        titulo = plugintools.find_single_match(generos,'class="maintitle">(.*?)<')
        foto = plugintools.find_single_match(generos,'class="ima">.*?<img src="(.*?)"')
        request_headers=[]
        request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"])
        body,response_headers = plugintools.read_body_and_headers(url5, headers=request_headers)
        url = body.strip()    
        page = plugintools.find_single_match(url,'pageID":"(.*?)","')
        url ='/alacarta/interno/contenttable.shtml?pbq=1&module=OTHER&sectionFilter=-1&orderCriteria=DESC&modl=TOC&locale=es&pageSize=15&ctx='+page+'&typeFilter=39816&mode=TEXT'
        
        plugintools.add_item(action = "series_tve_temporada" , title ="[B][LOWERCASE][CAPITALIZE][COLOR yellow][COLOR aqua]"+titulo+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" ,url =url, thumbnail =foto,fanart = foto,folder = True )
        
        
  
    plugintools.add_item(action = "" , title ="[B][LOWERCASE][CAPITALIZE][COLOR yellow]------------[COLOR white] tve[COLOR yellow]------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",  thumbnail ="https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png", fanart = "https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png",  folder = False )  
    
    
    
    
    
def series_tve_temporada(params):
    plugintools.log("chopocine.cinetuxanios "+repr(params))
    plugintools.add_item(action = "" , title ="[B][LOWERCASE][CAPITALIZE][COLOR yellow]------------[COLOR white] tve[COLOR yellow]------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png", fanart = "https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png",  folder = False )    
    thumbnail = params.get("thumbnail") 
    url='https://www.rtve.es'+params.get("url")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers(url, headers=request_headers)
    url3 = body.strip() 
    siguiente = plugintools.find_single_match(url3,'class="siguiente">.*?<a name="paginaIR" href="(.*?)"').replace("amp;", "")    
    matches = plugintools.find_multiple_matches(url3,'(tooltip"><a href=".*?<span class="miga">)')
    for generos in matches:
        url = plugintools.find_single_match(generos,'a href="(.*?)"')   
        titulo = plugintools.find_single_match(generos,'<a href=".*?" title="Ver.*?">(.*?)</a>')   
        fecha = plugintools.find_single_match(generos,'class="fecha">(.*?)</span>')  
        texto = plugintools.find_single_match(generos,'class="detalle">(.*?)<')        
        plugintools.add_item(action = "javi_descarga" ,url=url, title ="[B][LOWERCASE][CAPITALIZE][COLOR yellow]"+titulo+ " [COLOR lime] "+fecha+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",plot=texto , thumbnail =thumbnail,fanart =thumbnail,folder = True )
    if 'alacarta' in siguiente:  
    
    
    
        plugintools.add_item( action="series_tve_temporada" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow][COLOR lime]ir a la pagina siguiente[/B][/COLOR][/CAPITALIZE][/LOWERCASE]", url= siguiente, thumbnail = "https://www.periodicoelpunto.com/wp-content/uploads/2019/03/flecha-siguiente.png",fanart = "https://www.periodicoelpunto.com/wp-content/uploads/2019/03/flecha-siguiente.png", folder=True )  



        
    plugintools.add_item(action = "" , title ="[B][LOWERCASE][CAPITALIZE][COLOR yellow]------------[COLOR white] tve[COLOR yellow]------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",  thumbnail ="https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png", fanart = "https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png",  folder = False )     


  
#----------------------------javi_descarga-------------------javi_descarga---------------------javi_descarga------------------javi_descarga#----------------------------javi_descarga-------------------javi_descarga---------------------javi_descarga------------------javi_descarga#----------------------------javi_descarga-------------------javi_descarga---------------------javi_descarga------------------javi_descarga#----------------------------javi_descarga-------------------javi_descarga---------------------javi_descarga------------------javi_descarga#----------------------------javi_descarga-------------------javi_descarga---------------------javi_descarga------------------javi_descarga#----------------------------javi_descarga-------------------javi_descarga---------------------javi_descarga------------------javi_descarga#----------------------------javi_descarga-------------------javi_descarga---------------------javi_descarga------------------javi_descarga#----------------------------javi_descarga-------------------javi_descarga---------------------javi_descarga------------------javi_descarga#----------------------------javi_descarga-------------------javi_descarga---------------------javi_descarga------------------javi_descarga#----------------------------javi_descarga-------------------javi_descarga---------------------javi_descarga------------------javi_descarga#----------------------------javi_descarga-------------------javi_descarga---------------------javi_descarga------------------javi_descarga#----------------------------javi_descarga-------------------javi_descarga---------------------javi_descarga------------------javi_descarga#----------------------------javi_descarga-------------------javi_descarga---------------------javi_descarga------------------javi_descarga#----------------------------javi_descarga-------------------javi_descarga---------------------javi_descarga------------------javi_descarga#----------------------------javi_descarga-------------------javi_descarga---------------------javi_descarga------------------javi_descarga#----------------------------javi_descarga-------------------javi_descarga---------------------javi_descarga------------------javi_descarga
        
def javi_descarga(params): 
    plugintools.add_item(action = "" , title ="[B][LOWERCASE][CAPITALIZE][COLOR yellow]------------[COLOR white] tve[COLOR yellow]------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",  thumbnail ="https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png", fanart = "https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png",  folder = False )  
    url = params.get("url")   
    s = "regex"
    def dec(s):
        import re, requests, resolveurl, xbmc
        url2 = 'https://eljaviero.com/descargarvideosdelatele/index.php'
        headers = {'referent':'https://eljaviero.com/descargarvideosdelatele/', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:72.0) Gecko/20100101 Firefox/72.0'}
        payload ={'url_noticia':url,'submit_enviar_url':'ok'}
        s = requests.Session()
        logueo = s.post(url2, headers=headers, data=payload)
        r = logueo
        return r.content
    
    thumbnail = params.get("thumbnail") 
    fanart = params.get("thumbnail")    
    esto = dec(s)

    matches = plugintools.find_multiple_matches(esto,"(role='alert'>.*?<.*?/a>)")
    for generos in matches: 
        url = plugintools.find_single_match(generos,"href='(.*?)'").replace("\\", "")
        titulo = plugintools.find_single_match(generos," href=\'.*?\'.*?>(.*?)<").replace('\u00ed','i').replace('\u00e9','e').replace('\u00f3','o').replace('\u00f1','ñ').replace('\u00e1','a').replace('\u00fa','u').replace('\u00da','u')

        plugintools.add_item(action = "play_links" ,thumbnail =thumbnail, fanart = fanart,title="[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo+"[/B][/COLOR][/CAPITALIZE][/LOWERCASE]", url=url,   folder=False,  isPlayable = True )      
    plugintools.add_item(action = "" , title ="[B][LOWERCASE][CAPITALIZE][COLOR yellow]------------[COLOR white] tve[COLOR yellow]------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",  thumbnail ="https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png", fanart = "https://images-na.ssl-images-amazon.com/images/I/516rC6urOwL.png",  folder = False )           


#------------------MITELE-------------------MITELE--------------------------MITELE-------------------------MITELE--------------------MITELE-----------#------------------MITELE-------------------MITELE--------------------------MITELE-------------------------MITELE--------------------MITELE-----------#------------------MITELE-------------------MITELE--------------------------MITELE-------------------------MITELE--------------------MITELE-----------#------------------MITELE-------------------MITELE--------------------------MITELE-------------------------MITELE--------------------MITELE-----------#------------------MITELE-------------------MITELE--------------------------MITELE-------------------------MITELE--------------------MITELE-----------#------------------MITELE-------------------MITELE--------------------------MITELE-------------------------MITELE--------------------MITELE-----------#------------------MITELE-------------------MITELE--------------------------MITELE-------------------------MITELE--------------------MITELE-----------#------------------MITELE-------------------MITELE--------------------------MITELE-------------------------MITELE--------------------MITELE-----------#------------------MITELE-------------------MITELE--------------------------MITELE-------------------------MITELE--------------------MITELE-----------#------------------MITELE-------------------MITELE--------------------------MITELE-------------------------MITELE--------------------MITELE-----------#------------------MITELE-------------------MITELE--------------------------MITELE-------------------------MITELE--------------------MITELE-----------#------------------MITELE-------------------MITELE--------------------------MITELE-------------------------MITELE--------------------MITELE-----------#------------------MITELE-------------------MITELE--------------------------MITELE-------------------------MITELE--------------------MITELE-----------
def miniserie_mitele(params):  
    plugintools.log("chopocine.miniserie_mitele")    
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]------------------------------[COLOR yellow]miniseries mitele[COLOR aqua]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://album.mediaset.es//parrillas/2019/10/04/e3ceb5881a0a1fdaad01296d7554868d1570194115.jpg", fanart = "https://album.mediaset.es/eimg/2017/11/03/RDrSzFS5nu4Eyyq5gGEES2.jpg",  folder = False )   
    url= "https://mab.mediaset.es/1.0.0/get?oid=bitban&eid=%2FautomaticIndex%2Fmtweb%3Furl%3Dwww%252Emitele%252Ees%252Fminiseries%252F%26page%3D1%26id%3Da-z%26size%3D24"
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers(url, headers=request_headers)
    url = body.strip()
    
    matches = plugintools.find_multiple_matches(url,'("id":".*?","title":".*?false,"_elapsedSeconds)')       
    for generos in matches: 
        url = "https://www.mitele.es"+plugintools.find_single_match(generos,'href":"(.*?)"').replace('\\','')
        titulo = plugintools.find_single_match(generos,'title":"(.*?)"').replace('\u00ed','i').replace('\u00eda','e').replace('\u00f1','ñ').replace('\u00fa','u').replace('\u00f3','o')
        foto = plugintools.find_single_match(generos,'src":"(.*?)".*?').replace('\\','')
        plugintools.add_item(action = "miniserie_mitele_server" , title ="[B][LOWERCASE][CAPITALIZE][COLOR gold][COLOR white] "+titulo+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", url=url, thumbnail =foto,fanart =foto, folder = True )
        
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]------------------------------[COLOR yellow]miniseries mitele[COLOR aqua]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://album.mediaset.es//parrillas/2019/10/04/e3ceb5881a0a1fdaad01296d7554868d1570194115.jpg", fanart = "https://album.mediaset.es/eimg/2017/11/03/RDrSzFS5nu4Eyyq5gGEES2.jpg",  folder = False )





def miniserie_mitele_server(params):  
    plugintools.log("chopocine.miniserie_mitele_server")    
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]------------------------------[COLOR yellow]series mitele[COLOR aqua]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://album.mediaset.es//parrillas/2019/10/04/e3ceb5881a0a1fdaad01296d7554868d1570194115.jpg", fanart = "https://album.mediaset.es/eimg/2017/11/03/RDrSzFS5nu4Eyyq5gGEES2.jpg",  folder = False )     
    url = params.get("url")
    thumbnail = params.get("thumbnail")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers(url, headers=request_headers)
    url = body.strip()
    
    matches = plugintools.find_multiple_matches(url,'(season_id":".*?series_id":")')       
    for generos in matches: 
        url = "https://www.mitele.es"+plugintools.find_single_match(generos,'jpg","href":"(.*?player/)"').replace('\\','')
        
        titulo = plugintools.find_single_match(generos,'title":"(.*?)"').replace('\u00ed','i').replace('\u00eda','e').replace('\u00f1','ñ').replace('\u00fa','u').replace('\u00f3','o')
        
        titulo2 = plugintools.find_single_match(generos,'subtitle":"(.*?)"').replace('\u00ed','i').replace('\u00eda','e').replace('\u00f1','ñ').replace('\u00fa','u').replace('\u00f3','o')
        
        foto = plugintools.find_single_match(generos,'src":"(.*?)".*?').replace('\\','')
        
        synopsis = plugintools.find_single_match(generos,'synopsis":"(.*?)".*?').replace('\\','')
        
        plugintools.add_item(action = "miniserie_mitele_reproducir" , title ="[B][LOWERCASE][CAPITALIZE][COLOR white] "+titulo+" [COLOR gold] "+titulo2+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", url=url, plot=synopsis ,thumbnail =foto,fanart =foto, folder = True )

    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]------------------------------[COLOR yellow]series mitele[COLOR aqua]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://album.mediaset.es//parrillas/2019/10/04/e3ceb5881a0a1fdaad01296d7554868d1570194115.jpg", fanart = "https://album.mediaset.es/eimg/2017/11/03/RDrSzFS5nu4Eyyq5gGEES2.jpg",  folder = False )          
        
        
def miniserie_mitele_reproducir(params):  
    plugintools.log("chopocine.miniserie_mitele_server")    
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]------------------------------[COLOR yellow]dar en reproducir [COLOR aqua]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://album.mediaset.es//parrillas/2019/10/04/e3ceb5881a0a1fdaad01296d7554868d1570194115.jpg", fanart = "https://album.mediaset.es/eimg/2017/11/03/RDrSzFS5nu4Eyyq5gGEES2.jpg",  folder = False )   
    url1 = params.get("url")
    thumbnail = params.get("thumbnail")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:74.0) Gecko/20100101 Firefox/74.0"])
    body,response_headers = plugintools.read_body_and_headers(url1, headers=request_headers)
    url = body.strip()
    dataMediaId = plugintools.find_single_match(url,'"dataMediaId":"(.*?)".*?')
    internal_id = plugintools.find_single_match(url,'"internal_id":"(.*?)".*?')
    api = plugintools.find_single_match(url,'"dataConfig":"(.*?)".*?')

    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:74.0) Gecko/20100101 Firefox/74.0"])
    body,response_headers = plugintools.read_body_and_headers(api, headers=request_headers)
    url5 = body.strip()  
    gbx = plugintools.find_single_match(url5,'gbx":"(.*?)".*?').replace('\\','')
    caronte = plugintools.find_single_match(url5,'caronte":"(.*?)".*?').replace('\\','')
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:74.0) Gecko/20100101 Firefox/74.0"])
    body,response_headers = plugintools.read_body_and_headers(caronte, headers=request_headers)
    url = body.strip()    
    cerbero = plugintools.find_single_match(url,'cerbero":"(.*?)"').replace('\\','')  
    m3u8 = plugintools.find_single_match(url,'hls","stream":"(.*?)"').replace('\\','')    
    bbx = plugintools.find_single_match(url,'bbx":"(.*?)"').replace('\\','')
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:74.0) Gecko/20100101 Firefox/74.0"])
    body,response_headers = plugintools.read_body_and_headers(gbx, headers=request_headers)
    url = body.strip()      
    gbxfinal  = plugintools.find_single_match(url,'gbx":"(.*?)"').replace('\\','')
    s = "regex"
    def dec(s):
        import re, requests, resolveurl, xbmc
        header4={'Accept':'application/json, text/plain, */*','Referer':url1,'Origin':'https://www.mitele.es','User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36','Sec-Fetch-Mode':'cors','Content-Type':'application/json;charset=UTF-8'}
        payload='{"bbx":"'+(bbx)+'","gbx":"'+(gbxfinal)+'"}'
        s = requests.Session()
        url8=s.post(cerbero,headers=header4,data=payload).text
        return url8

    esto = dec(s)
    if 'hdnts' in esto:
        cdn1=plugintools.find_single_match(esto,'"cdn":"(.*?)"')
        final = (m3u8)+'?'+(cdn1)
        plugintools.add_item(action = "play_links" , title ="[B][LOWERCASE][CAPITALIZE][COLOR orange]reproducir[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" ,url = final,thumbnail=thumbnail,fanart=thumbnail, folder=False,  isPlayable = True )       
    else:
        final= (m3u8).replace('master.m3u8','index_0_av.m3u8')    
        plugintools.add_item(action = "play_links" , title ="[B][LOWERCASE][CAPITALIZE][COLOR orange]reproducir[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" ,url = final,thumbnail=thumbnail,fanart= thumbnail, folder=False,  isPlayable = True )
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]------------------------------[COLOR yellow]dar en reproducir [COLOR aqua]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://album.mediaset.es//parrillas/2019/10/04/e3ceb5881a0a1fdaad01296d7554868d1570194115.jpg", fanart = "https://album.mediaset.es/eimg/2017/11/03/RDrSzFS5nu4Eyyq5gGEES2.jpg",  folder = False )




















#---------------------danko------------------------danko---------------danko----------------------danko#---------------------danko------------------------danko---------------danko----------------------danko  #---------------------danko------------------------danko---------------danko----------------------danko  #---------------------danko------------------------danko---------------danko----------------------danko  #---------------------danko------------------------danko---------------danko----------------------danko  #---------------------danko------------------------danko---------------danko----------------------danko  #---------------------danko------------------------danko---------------danko----------------------danko  #---------------------danko------------------------danko---------------danko----------------------danko  #---------------------danko------------------------danko---#---------------------danko------------------------danko---------------danko----------------------danko  #-------------







def danko_menu(params):  
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]------------------------------[COLOR yellow]series danko menu[COLOR aqua]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://beautifulgishi.com/wp-content/uploads/2018/09/series.jpg", fanart = "https://beautifulgishi.com/wp-content/uploads/2018/09/series.jpg",  folder = False ) 
    try:
        request_headers=[]    
        url="http://ab-kkk.com/"
        request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
        body,response_headers = plugintools.read_body_and_headers( url, headers=request_headers)
        url = body.strip()
        detecta = plugintools.find_single_match(url,'content="(SeriesPepito)')
        if 'SeriesPepito' in detecta:   
            plugintools.add_item(action = "series_danko_series_letras" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]series danko [COLOR gold]todas [/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color,  thumbnail ="https://beautifulgishi.com/wp-content/uploads/2018/09/series.jpg", fanart = "https://beautifulgishi.com/wp-content/uploads/2018/09/series.jpg",url="http://ab-kkk.com/", folder = True )    
    
            plugintools.add_item(action = "danko_busca" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]series danko [COLOR gold]buscador [/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color,  thumbnail ="https://beautifulgishi.com/wp-content/uploads/2018/09/series.jpg", fanart = "https://beautifulgishi.com/wp-content/uploads/2018/09/series.jpg", folder = True )      

        else:
            r ='tu compañia te capa el acceso a series danko\nven al  grupo de telegram [COLOR aqua]@tvchopo [COLOR red]y te ayudamos'   
            plugintools.add_item(action = "play_links" ,title="[B][LOWERCASE][CAPITALIZE][COLOR red]"+r+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",   folder=False,  isPlayable = True ) 


    except:
        r ='tu compañia te capa el acceso a series danko\nven al  grupo de telegram [COLOR aqua]@tvchopo [COLOR red]y te ayudamos'   
        plugintools.add_item(action = "" ,title="[B][LOWERCASE][CAPITALIZE][COLOR red]"+r+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",   folder=False,  isPlayable = True )    
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]------------------------------[COLOR yellow]series danko menu[COLOR aqua]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://beautifulgishi.com/wp-content/uploads/2018/09/series.jpg", fanart = "https://beautifulgishi.com/wp-content/uploads/2018/09/series.jpg",  folder = False ) 



def danko_busca(params):  
    plugintools.log("chopocine.pepeseries_temporadas")    
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]------------------------------[COLOR yellow]series danko buscador[COLOR aqua]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://beautifulgishi.com/wp-content/uploads/2018/09/series.jpg", fanart = "https://beautifulgishi.com/wp-content/uploads/2018/09/series.jpg",  folder = False )      
    dialog = xbmcgui.Dialog()
    d = dialog.input('[B][LOWERCASE][CAPITALIZE][COLOR orange]buscar una peli: ejemplo: [COLOR white]la casa de papel[/COLOR][/CAPITALIZE][/LOWERCASE][/B]', type=xbmcgui.INPUT_ALPHANUM).replace(" ", "+")
    url= "http://ab-kkk.com/?s="+d
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers(url, headers=request_headers)
    url = body.strip()
    
    matches = plugintools.find_multiple_matches(url,'(<a href="http://ab-kkk.com/capitulos/.*?class="attachment-thumbnail size-thumbnail wp-post-image)')       
    for generos in matches: 
  

        url = plugintools.find_single_match(generos,'<a href="(.*?)"')
        titulo = plugintools.find_single_match(generos,'<a href="http://ab-kkk.com/capitulos/(.*?)/').replace('-',' ')
        foto = plugintools.find_single_match(generos,'src="(.*?)"')
        plugintools.add_item(action = "series_danko_temporadas" , title ="[B][LOWERCASE][CAPITALIZE][COLOR gold][COLOR white] "+titulo+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", url=url, thumbnail =foto,fanart =foto, folder = True )
        
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]------------------------------[COLOR yellow]series danko buscador[COLOR aqua]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://beautifulgishi.com/wp-content/uploads/2018/09/series.jpg", fanart = "https://beautifulgishi.com/wp-content/uploads/2018/09/series.jpg",  folder = False )



   
    
def series_danko_series_letras(params):
    plugintools.set_view(plugintools.LIST)  
    plugintools.log("chopocine.series_danko_series_letras")    
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]------------------------------[COLOR yellow]series danko[COLOR aqua]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://beautifulgishi.com/wp-content/uploads/2018/09/series.jpg", fanart = "https://beautifulgishi.com/wp-content/uploads/2018/09/series.jpg",  folder = False )       
    url = params.get("url")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers(url, headers=request_headers)
    url = body.strip()
    matches = plugintools.find_multiple_matches(url,'(<li><a href=".*?">.*?</a></li>)')    
    for generos in matches:           
        url = plugintools.find_single_match(generos,'href="(.*?)"')
        titulo = plugintools.find_single_match(generos,'href=".*?">(.*?)</a>')
        plugintools.add_item(action = "series_danko_series" , title ="[B][LOWERCASE][CAPITALIZE][COLOR white]lista de series por la letra [COLOR gold]"+titulo+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://beautifulgishi.com/wp-content/uploads/2018/09/series.jpg", fanart = "https://beautifulgishi.com/wp-content/uploads/2018/09/series.jpg",url=url, folder = True )              
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]------------------------------[COLOR yellow]series danko[COLOR aqua]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://i.imgur.com/Du21mll.jpg", fanart = "https://i.imgur.com/Du21mll.jpg",  folder = False )    



def series_danko_series(params):
    plugintools.set_view(plugintools.LIST)  
    plugintools.log("chopocine.series_danko_series_letras")    
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]------------------------------[COLOR yellow]series danko[COLOR aqua]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://beautifulgishi.com/wp-content/uploads/2018/09/series.jpg", fanart = "https://beautifulgishi.com/wp-content/uploads/2018/09/series.jpg",  folder = False )       
    url = params.get("url")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers(url, headers=request_headers)
    url = body.strip()
 #   siguiente = plugintools.find_single_match(url,'class="next page-numbers" href="(.*?)"')
    matches = plugintools.find_multiple_matches(url,'(<a href="http://ab-kkk.com/capitulos/.*?class="attachment-thumbnail size-thumbnail)')    
    for generos in matches:           
        url = plugintools.find_single_match(generos,'<a href="(http://ab-kkk.com/capitulos.*?)"')
        foto = plugintools.find_single_match(generos,'src="(.*?)"')
        titulo = plugintools.find_single_match(generos,'href="http://ab-kkk.com/capitulos/(.*?)"').replace("/", "").replace("-", " ")
        plugintools.add_item(action = "series_danko_temporadas" , title ="[B][LOWERCASE][CAPITALIZE][COLOR white] [COLOR gold]"+titulo+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail =foto,fanart =foto,url=url, folder = True )  


#    if 'http' in siguiente:
#        plugintools.add_item( action="series_danko_series" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]pagina  ir a la siguiente [COLOR yellow]aqui[/B][/COLOR][/CAPITALIZE][/LOWERCASE]", url= siguiente, thumbnail = "https://www.periodicoelpunto.com/wp-content/uploads/2019/03/flecha-siguiente.png",fanart = "https://www.periodicoelpunto.com/wp-content/uploads/2019/03/flecha-siguiente.png", folder=True ) 
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]------------------------------[COLOR yellow]series danko[COLOR aqua]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://beautifulgishi.com/wp-content/uploads/2018/09/series.jpg", fanart = "https://beautifulgishi.com/wp-content/uploads/2018/09/series.jpg",  folder = False ) 
    
def series_danko_temporadas(params):
    plugintools.set_view(plugintools.LIST)    
    plugintools.log("chopocine.series_24_series")    
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]------------------------------[COLOR yellow]series danko[COLOR aqua]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://beautifulgishi.com/wp-content/uploads/2018/09/series.jpg", fanart = "https://beautifulgishi.com/wp-content/uploads/2018/09/series.jpg",  folder = False )     
    url = params.get("url")
    thumbnail = params.get("thumbnail")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers(url, headers=request_headers)
    url = body.strip()
    
    matches = plugintools.find_multiple_matches(url,'(<td class="sape">.*? </tr>)')       
    for generos in matches: 
  

        url = plugintools.find_single_match(generos,'<a href="(.*?)"')
        titulo = plugintools.find_single_match(generos,'class="color.*?">(.*?)<')

        plugintools.add_item(action = "series_danko_servers" , title ="[B][LOWERCASE][CAPITALIZE][COLOR gold][COLOR white] "+titulo+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail =thumbnail,fanart =thumbnail,url=url,  folder = True )
        
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]------------------------------[COLOR yellow]series danko[COLOR aqua]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://beautifulgishi.com/wp-content/uploads/2018/09/series.jpg", fanart = "https://beautifulgishi.com/wp-content/uploads/2018/09/series.jpg",  folder = False ) 

def series_danko_servers(params):
    plugintools.set_view(plugintools.LIST)    
    plugintools.log("chopocine.series_danko_servers")    
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]------------------------------[COLOR yellow]series danko[COLOR aqua]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://beautifulgishi.com/wp-content/uploads/2018/09/series.jpg", fanart = "https://beautifulgishi.com/wp-content/uploads/2018/09/series.jpg",  folder = False )   
    url = params.get("url")
    title = params.get("title")
    thumbnail = params.get("thumbnail")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers(url, headers=request_headers)
    url = body.strip()
    matches = plugintools.find_multiple_matches(url,'(<a data-enlace=".*?" data-language=".*?" data-tipo="online" data-server=".*?" data-url=")')
    
    for generos in matches: 
  
        url4 = plugintools.find_single_match(generos,'<a data-enlace="(.*?)"')
        titulo = plugintools.find_single_match(generos,'data-server="(.*?)"').replace('Powvideo','powvideo [COLOR red]no elegir').replace('Streamplay','streamplay [COLOR red]no elegir').replace('Vidtodo','vidtodo [COLOR red]no elegir').replace('Waaw','waaw [COLOR red]no elegir').replace('Flix555','Flix555 [COLOR red]no elegir').replace('Verystream','Verystream [COLOR red]no elegir').replace('Videofiles','Videofiles [COLOR red]no elegir')
        idioma = plugintools.find_single_match(generos,'data-language="(.*?)"')

        if 'clipwatching' in url4:
            url= url4
            request_headers=[]
            request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
            body,response_headers = plugintools.read_body_and_headers( url, headers=request_headers)
            url1 = body.strip()
            source = plugintools.find_single_match(url1,'sources: ."(.*?)"')
            if 'mp4' in url:            
                plugintools.add_item(action = "play_links" ,  title ="[B][LOWERCASE][CAPITALIZE][COLOR white][COLOR pink]"+titulo+"  [COLOR pink]"+idioma+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", url = source,thumbnail=thumbnail,fanart = thumbnail,  folder=False,  isPlayable = True )


                 
        if 'upstream' in url4:
            request_headers=[]
            request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])  
            body,response_headers = plugintools.read_body_and_headers( url4, headers=request_headers)
            url1 = body.strip()
            finale = plugintools.find_single_match(url1,'sources: ..file:"(.*?)"')                 
            plugintools.add_item(action = "play_links" ,  title ="[B][LOWERCASE][CAPITALIZE][COLOR white][COLOR gold]"+titulo+"  [COLOR white]"+idioma+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", url = finale,thumbnail=thumbnail,fanart = thumbnail,  folder=False,  isPlayable = True )                 
      
        else:
            plugintools.add_item(action = "play_resolver" , title ="[B][LOWERCASE][CAPITALIZE][COLOR white][COLOR gold]"+titulo+"  [COLOR white]"+idioma+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",url =url4, thumbnail =thumbnail,fanart =thumbnail, folder=False,  isPlayable = True ) 




    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]------------------------------[COLOR yellow]series danko[COLOR aqua]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://beautifulgishi.com/wp-content/uploads/2018/09/series.jpg", fanart = "https://beautifulgishi.com/wp-content/uploads/2018/09/series.jpg",  folder = False )   
#-----------------------pepeseries------------------------pepeseries-----------------------------pepeseries---------------------------------------- #-----------------------pepeseries------------------------pepeseries-----------------------------pepeseries---------------------------------------- #-----------------------pepeseries------------------------pepeseries-----------------------------pepeseries---------------------------------------- #-----------------------pepeseries------------------------pepeseries-----------------------------pepeseries---------------------------------------- #-----------------------pepeseries------------------------pepeseries-----------------------------pepeseries---------------------------------------- #-----------------------pepeseries------------------------pepeseries-----------------------------pepeseries---------------------------------------- #-----------------------pepeseries------------------------pepeseries-----------------------------pepeseries---------------------------------------- #-----------------------pepeseries------------------------pepeseries-----------------------------pepeseries---------------------------------------- #-----------------------pepeseries------------------------pepeseries-----------------------------pepeseries---------------------------------------- #-----------------------pepeseries------------------------pepeseries-----------------------------pepeseries---------------------------------------- #-----------------------pepeseries------------------------pepeseries-----------------------------pepeseries---------------------------------------- #-----------------------pepeseries------------------------pepeseries-----------------------------pepeseries---------------------------------------- #-----------------------pepeseries------------------------pepeseries-----------------------------pepeseries---------------------------------------- #-----------------------pepeseries------------------------pepeseries-----------------------------pepeseries---------------------------------------- #-----------------------pepeseries------------------------pepeseries-----------------------------pepeseries---------------------------------------- #-----------------------pepeseries------------------------pepeseries-----------------------------pepeseries---------------------------------------- #-----------------------pepeseries------------------------pepeseries-----------------------------pepeseries---------------------------------------- #-----------------------pepeseries------------------------pepeseries-----------------------------pepeseries---------------------------------------- #-----------------------pepeseries------------------------pepeseries-----------------------------pepeseries----------------------------------------    
    
    
def pepeseries_menu(params):  
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]------------------------------[COLOR yellow]pepeseries menu[COLOR aqua]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://i.imgur.com/9a16ENI.jpg", fanart = "https://i.imgur.com/9a16ENI.jpg",  folder = False ) 
    try:
        request_headers=[]    
        url="https://pepecine.to"
        request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
        body,response_headers = plugintools.read_body_and_headers( url, headers=request_headers)
        url = body.strip()
        detecta = plugintools.find_single_match(url,'class="dst">(PepeCine)')
        if 'PepeCine' in detecta:
            plugintools.add_item(action = "pepeseries" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]pepeseries todas[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color,  thumbnail ="https://st-listas.20minutos.es/images/2019-06/440207/5476186_640px.jpg?1567524986",url="https://pepecine.to/secure/titles?type=series&onlyStreamable=true&",plot='page=1', fanart = "https://i.imgur.com/x89QdGV.jpg", folder = True )   
    
            plugintools.add_item(action = "pepe_series_generos" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]pepeseries generos[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color,  thumbnail ="https://st-listas.20minutos.es/images/2019-06/440207/5476186_640px.jpg?1567524986", plot="page=1",fanart = "https://i.imgur.com/x89QdGV.jpg", folder = True )  

            plugintools.add_item(action = "pepe_series_anios" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]pepeseries años[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color,  thumbnail ="https://st-listas.20minutos.es/images/2019-06/440207/5476186_640px.jpg?1567524986", plot="page=1",fanart = "https://i.imgur.com/x89QdGV.jpg", folder = True )       


            plugintools.add_item(action = "pepe_series_ultimos_capitulos" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]pepeseries ultimos capitulos[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color,  thumbnail ="https://st-listas.20minutos.es/images/2019-06/440207/5476186_640px.jpg?1567524986", plot="page=1",fanart = "https://i.imgur.com/x89QdGV.jpg", folder = True ) 


            plugintools.add_item(action = "pepeseries_busca" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]pepeseries buscador[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color,  thumbnail ="https://st-listas.20minutos.es/images/2019-06/440207/5476186_640px.jpg?1567524986",fanart = "https://i.imgur.com/x89QdGV.jpg", folder = True ) 
    
            plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]------------------------------[COLOR yellow]pepeseries menu[COLOR aqua]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://i.imgur.com/9a16ENI.jpg", fanart = "https://i.imgur.com/9a16ENI.jpg",  folder = False ) 

        else:
            r ='tu compañia te capa el acceso a pepeseries\nven al  grupo de telegram [COLOR aqua]@tvchopo [COLOR red]y te ayudamos'   
            plugintools.add_item(action = "play_links" ,title="[B][LOWERCASE][CAPITALIZE][COLOR red]"+r+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",   folder=False,  isPlayable = True ) 


    except:
        r ='tu compañia te capa el acceso a pepeseries\nven al  grupo de telegram [COLOR aqua]@tvchopo [COLOR red]y te ayudamos'   
        plugintools.add_item(action = "play_links" ,title="[B][LOWERCASE][CAPITALIZE][COLOR red]"+r+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",   folder=False,  isPlayable = True )  

def pepeseries_busca(params):  
    plugintools.log("chopocine.pepeseries_temporadas")    
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]------------------------------[COLOR yellow]mundoseries[COLOR aqua]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://i.imgur.com/Du21mll.jpg", fanart = "https://i.imgur.com/Du21mll.jpg",  folder = False )       
    dialog = xbmcgui.Dialog()
    d = dialog.input('[B][LOWERCASE][CAPITALIZE][COLOR orange]buscar una peli: ejemplo: [COLOR white]rocky[/COLOR][/CAPITALIZE][/LOWERCASE][/B]', type=xbmcgui.INPUT_ALPHANUM).replace(" ", "%20")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers('https://pepecine.to/secure/search/'+d+'?type=&limit=16', headers=request_headers)
    url = body.strip()
    matches = plugintools.find_multiple_matches(url,'.{"id":.*?,"name":".*?".*?poster":".*?".*?is_series')    
    for generos in matches: 
        plugintools.set_view(plugintools.LIST)    
        ids = plugintools.find_single_match(generos,'.{"id":(.*?),"name":".*?".*?poster":"')
        titulo = plugintools.find_single_match(generos,'"id":.*?,"name":"(.*?)","year":.*?.*?,"')
        anio = plugintools.find_single_match(generos,'","year":(.*?),"')
        foto = plugintools.find_single_match(generos,'poster":"(.*?)","is_series"').replace("\\", "")
       
        plugintools.add_item(action = "pepeseries_temporadas" , title ="[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo+"  [COLOR yellow]"+anio+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail =foto,fanart =foto,url=ids,  folder = True )  




def pepe_series_ultimos_capitulos(params):
    plugintools.log("chopocine.pepe_series_ultimos_capitulos "+repr(params))    
    thumbnail = params.get("thumbnail") 
    fanart = params.get("thumbnail")
    page = params.get("plot")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers('https://verencasa.com/last/estrenos-episodios-online.php', headers=request_headers)
    url = body.strip()
    matches = plugintools.find_multiple_matches(url,"<div class='online(.*?)</div>")
    for generos in matches:
        ids = plugintools.find_single_match(generos,'titles/(.*?)/season')
        season = plugintools.find_single_match(generos,'season/(.*?)/episode')
        episode = plugintools.find_single_match(generos,'/episode/(.*?) target="')
        foto = plugintools.find_single_match(generos,'src=(.*?) class=.*?')
        titulo = plugintools.find_single_match(generos,'alt="(.*?)"')
        url = 'https://pepecine.to/secure/titles/'+ids+'?titleId='+ids+'&seasonNumber='+season+'&episodeNumber='+episode
        plugintools.add_item(action = "pepeseries_episodios" , title = "[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo+"[/COLOR][/CAPITALIZE][/LOWERCASE][/B]", url = url, thumbnail =foto, fanart = foto, folder = True )




def pepe_series_ultimos_capitulos(params):
    plugintools.log("chopocine.pepe_series_ultimos_capitulos "+repr(params))    
    thumbnail = params.get("thumbnail") 
    fanart = params.get("thumbnail")
    page = params.get("plot")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers('https://verencasa.com/last/estrenos-episodios-online.php', headers=request_headers)
    url = body.strip()
    matches = plugintools.find_multiple_matches(url,"<div class='online(.*?)</div>")
    for generos in matches:
        ids = plugintools.find_single_match(generos,'titles/(.*?)/season')
        season = plugintools.find_single_match(generos,'season/(.*?)/episode')
        episode = plugintools.find_single_match(generos,'/episode/(.*?) target="')
        foto = plugintools.find_single_match(generos,'src=(.*?) class=.*?')
        titulo = plugintools.find_single_match(generos,'alt="(.*?)"')
        url = 'https://pepecine.to/secure/titles/'+ids+'?titleId='+ids+'&seasonNumber='+season+'&episodeNumber='+episode
        plugintools.add_item(action = "pepeseries_episodios" , title = "[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo+"[/COLOR][/CAPITALIZE][/LOWERCASE][/B]", url = url, thumbnail =foto, fanart = foto, folder = True )
        
               

def pepe_series_anios(params):
    plugintools.log("chopocine.cinetuxanios "+repr(params))    
    thumbnail = params.get("thumbnail") 
    fanart = params.get("thumbnail")
    page = params.get("plot")
    data = plugintools.read("https://pastebin.com/raw/y47xFPNr")

    matches = plugintools.find_multiple_matches(data,'(".*?")')
    for generos in matches:
        genero = plugintools.find_single_match(generos,'"(.*?)"')
        numero= params.get("plot")
        url = 'https://pepecine.to/secure/titles?type=series&released='+genero+','+genero+'&onlyStreamable=true&'
        plugintools.add_item(action = "pepeseries_series_anios" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]series del año [COLOR white]"+genero+"[/COLOR][/CAPITALIZE][/LOWERCASE][/B]", url = url, plot= page,thumbnail ="https://st-listas.20minutos.es/images/2019-06/440207/5476186_640px.jpg?1567524986", fanart = "https://i.imgur.com/x89QdGV.jpg", folder = True )

def pepeseries_series_anios(params):  
    plugintools.log("chopocine.mundoseries_temporadas") 
    plugintools.set_view(plugintools.TV_SHOWS)    
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]----[COLOR yellow]pepeseries[COLOR aqua]----[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://st-listas.20minutos.es/images/2019-06/440207/5476186_640px.jpg?1567524986", fanart = "https://i.imgur.com/x89QdGV.jpg",  folder = False ) 
    page=  params.get("plot")    
    urlfin = params.get("url")  
    url3= urlfin+page    
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers(url3+'&perPage=25', headers=request_headers)
    url = body.strip()
    siguiente = plugintools.find_single_match(url,'next_page_url":"..?.(.*?)"')
    matches = plugintools.find_multiple_matches(url,'("id":.*?show_videos)')    
    for generos in matches: 
            
        ids = plugintools.find_single_match(generos,'"id":(.*?),"')
        titulo = plugintools.find_single_match(generos,'name":"(.*?)"').replace("\u00ed", "i").replace("\u00e9", "e").replace("\u00e1", "a").replace("\u00f3", "o").replace("\u00fa", "u")
        texto = plugintools.find_single_match(generos,'description":"(.*?)"').replace("\u00ed", "i").replace("\u00e9", "e").replace("\u00e1", "a").replace("\u00f3", "o").replace("\u00fa", "u")
        foto1 = plugintools.find_single_match(generos,'poster":"(.*?)"').replace("\\", "")
        foto2 = plugintools.find_single_match(generos,'backdrop":"(.*?)"').replace("\\", "")
        anio = plugintools.find_single_match(generos,'"year":(.*?)<')
        plugintools.set_view(plugintools.TV_SHOWS)
        plugintools.add_item(action = "pepeseries_temporadas" , title ="[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo+"  [COLOR gold]"+anio+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail =foto1,fanart =foto2,plot="[B][LOWERCASE][CAPITALIZE][COLOR white]"+texto+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",url=ids,  folder = True )  
    plugintools.set_view(plugintools.TV_SHOWS)
    plugintools.add_item( action="pepeseries_series_anios" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]pagina  ir a la siguiente [COLOR yellow]aqui[/B][/COLOR][/CAPITALIZE][/LOWERCASE]", url= urlfin,plot= siguiente, thumbnail = "https://www.periodicoelpunto.com/wp-content/uploads/2019/03/flecha-siguiente.png",fanart = "https://www.periodicoelpunto.com/wp-content/uploads/2019/03/flecha-siguiente.png", folder=True ) 

    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]----[COLOR yellow]pepeseries[COLOR aqua]----[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://st-listas.20minutos.es/images/2019-06/440207/5476186_640px.jpg?1567524986", fanart = "https://i.imgur.com/x89QdGV.jpg",  folder = False ) 

def pepe_series_generos(params):
    plugintools.log("chopocine.cinetuxanios "+repr(params))    
    thumbnail = params.get("thumbnail") 
    fanart = params.get("thumbnail")
    page = params.get("plot")
    data = plugintools.read("https://pastebin.com/raw/4qJp60J4")

    matches = plugintools.find_multiple_matches(data,'(genero=.*?<genero>)')
    for generos in matches:
        genero = plugintools.find_single_match(generos,'genero=(.*?)<genero>')
        numero= params.get("plot")
        url='https://pepecine.to/secure/titles?type=series&genre='+genero+'&onlyStreamable=true&'
        plugintools.add_item(action = "pepeseries" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]series del genero [COLOR white]"+genero+"[/COLOR][/CAPITALIZE][/LOWERCASE][/B]", url = url, plot= page,thumbnail ="https://st-listas.20minutos.es/images/2019-06/440207/5476186_640px.jpg?1567524986", fanart = "https://i.imgur.com/x89QdGV.jpg", folder = True )

def pepeseries(params):  
    plugintools.log("chopocine.mundoseries_temporadas") 
    plugintools.set_view(plugintools.TV_SHOWS)    
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]----[COLOR yellow]pepeseries[COLOR aqua]----[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://st-listas.20minutos.es/images/2019-06/440207/5476186_640px.jpg?1567524986", fanart = "https://i.imgur.com/x89QdGV.jpg",  folder = False ) 
    page=  params.get("plot")    
    urlorin = params.get("url")  
    url3= urlorin+page    
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers(url3+'&perPage=25', headers=request_headers)
    url = body.strip()
    siguiente = plugintools.find_single_match(url,'next_page_url":"..?.(.*?)"')
    matches = plugintools.find_multiple_matches(url,'("id":.*?show_videos)')    
    for generos in matches: 
            
        ids = plugintools.find_single_match(generos,'"id":(.*?),"')
        titulo = plugintools.find_single_match(generos,'name":"(.*?)"').replace("\u00ed", "i").replace("\u00e9", "e").replace("\u00e1", "a").replace("\u00f3", "o").replace("\u00fa", "u")
        texto = plugintools.find_single_match(generos,'description":"(.*?)"').replace("\u00ed", "i").replace("\u00e9", "e").replace("\u00e1", "a").replace("\u00f3", "o").replace("\u00fa", "u")
        foto1 = plugintools.find_single_match(generos,'poster":"(.*?)"').replace("\\", "")
        foto2 = plugintools.find_single_match(generos,'backdrop":"(.*?)"').replace("\\", "")
        anio = plugintools.find_single_match(generos,'"year":(.*?)<')
        plugintools.set_view(plugintools.TV_SHOWS)
        plugintools.add_item(action = "pepeseries_temporadas" , title ="[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo+"  [COLOR gold]"+anio+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail =foto1,fanart =foto2,plot="[B][LOWERCASE][CAPITALIZE][COLOR white]"+texto+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",url=ids,  folder = True )  
    plugintools.set_view(plugintools.TV_SHOWS)
    plugintools.add_item( action="pepeseries" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]pagina  ir a la siguiente [COLOR yellow]aqui[/B][/COLOR][/CAPITALIZE][/LOWERCASE]", url= urlorin,plot= siguiente, thumbnail = "https://www.periodicoelpunto.com/wp-content/uploads/2019/03/flecha-siguiente.png",fanart = "https://www.periodicoelpunto.com/wp-content/uploads/2019/03/flecha-siguiente.png", folder=True ) 

    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]----[COLOR yellow]pepeseries[COLOR aqua]----[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://st-listas.20minutos.es/images/2019-06/440207/5476186_640px.jpg?1567524986", fanart = "https://i.imgur.com/x89QdGV.jpg",  folder = False ) 


def pepeseries_temporadas(params):  
    plugintools.log("chopocine.pepeseries_temporadas") 
    plugintools.set_view(plugintools.LIST)    
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]----[COLOR yellow]pepeseries temporadas[COLOR aqua]----[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://st-listas.20minutos.es/images/2019-06/440207/5476186_640px.jpg?1567524986", fanart = "https://i.imgur.com/x89QdGV.jpg",  folder = False ) 
    thumbnail = params.get("thumbnail")     
    url = params.get("url") 
    numeroid = params.get("url")    
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers('https://pepecine.to/secure/titles/'+url+'?titleId='+url, headers=request_headers)
    url = body.strip()
    matches = plugintools.find_multiple_matches(url,'({"id":.*?,"number":.*?,"episode_count)')    
    for generos in matches:            
        ids = plugintools.find_single_match(generos,'{"id":.*?,"number":(.*?),"episode_count')
        plugintools.add_item(action = "pepeseries_capitulos" , title ="[B][LOWERCASE][CAPITALIZE][COLOR white]temporada [COLOR gold]"+ids+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", plot= numeroid,thumbnail =thumbnail,fanart =thumbnail,url=ids,  folder = True )  
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]----[COLOR yellow]pepeseries temporadas[COLOR aqua]----[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://st-listas.20minutos.es/images/2019-06/440207/5476186_640px.jpg?1567524986", fanart = "https://i.imgur.com/x89QdGV.jpg",  folder = False ) 

def pepeseries_capitulos(params):  
    plugintools.log("chopocine.pepeseries_temporadas") 
    plugintools.set_view(plugintools.LIST)    
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]----[COLOR yellow]pepeseries capitulos[COLOR aqua]----[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://st-listas.20minutos.es/images/2019-06/440207/5476186_640px.jpg?1567524986", fanart = "https://i.imgur.com/x89QdGV.jpg",  folder = False ) 
    thumbnail = params.get("thumbnail")     
    url = params.get("url") 
    numeroid = params.get("plot")
    nuevaurl='https://pepecine.to/secure/titles/'+numeroid+'?titleId='+numeroid+"&title&seasonNumber="+url    
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers('https://pepecine.to/secure/titles/'+numeroid+'?titleId='+numeroid+"&title&seasonNumber="+url, headers=request_headers)
    
    url = body.strip()
    matches = plugintools.find_multiple_matches(url,'("title_id":.*?,"season_id":.*?,"season_number":.*?episode_number":.*?,"allow)')    
    for generos in matches:            
        episodio = plugintools.find_single_match(generos,'"title_id":.*?,"season_id":.*?,"season_number":.*?episode_number":(.*?),"allow')
        
        url = nuevaurl+"&episodeNumber="
        plugintools.add_item(action = "pepeseries_episodios" , title ="[B][LOWERCASE][CAPITALIZE][COLOR white]capitulo [COLOR gold]"+episodio+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail =thumbnail,fanart =thumbnail,url=url+episodio,  folder = True )  

    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]----[COLOR yellow]pepeseries capitulos[COLOR aqua]----[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://st-listas.20minutos.es/images/2019-06/440207/5476186_640px.jpg?1567524986", fanart = "https://i.imgur.com/x89QdGV.jpg",  folder = False ) 

def pepeseries_episodios(params):  
    plugintools.log("chopocine.pepeseries_temporadas") 
    plugintools.set_view(plugintools.LIST)    
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]----[COLOR yellow]pepeseries servidores[COLOR aqua]----[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://st-listas.20minutos.es/images/2019-06/440207/5476186_640px.jpg?1567524986", fanart = "https://i.imgur.com/x89QdGV.jpg",  folder = False ) 
    thumbnail = params.get("thumbnail")     
    url = params.get("url") 

       
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    dialog = xbmcgui.Dialog()
    body,response_headers = plugintools.read_body_and_headers( url, headers=request_headers)
    url1 = body.strip()
    matches = plugintools.find_multiple_matches(url1,'captions":(.*?)category')
    for generos in matches:        
        name = plugintools.find_single_match(generos,'name":".*?-(.*?)<').replace('\\','') 
                
        server = plugintools.find_single_match(generos,'htt.*?./..(.*?)\.').replace('powvideo','powvideo [COLOR red]no elegir').replace('streamplay','streamplay [COLOR red]no elegir').replace('vidtodo','vidtodo [COLOR red]no elegir').replace('waaw','waaw [COLOR red]no elegir')
        url = plugintools.find_single_match(generos,'url":"(.*?)"').replace('\\','').replace('/v/','/api/source/').replace('embed-','')
        if 'clipwatching' in url:
            request_headers=[]
            request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
            body,response_headers = plugintools.read_body_and_headers( url, headers=request_headers)
            url1 = body.strip()
            url = plugintools.find_single_match(url1,'sources: ."(.*?)"')
            if 'mp4' in url:            
                plugintools.add_item(action = "play_links" , title = "[B][LOWERCASE][CAPITALIZE][COLOR white]"+server+"[COLOR orange]  "+name+" [/CAPITALIZE][/LOWERCASE][/B][/COLOR]", url = url,thumbnail=thumbnail,fanart = thumbnail,  folder=False,  isPlayable = True )

            else:
                caido = "enlace borrado"
                plugintools.add_item(action = "play_links" , title = "[B][LOWERCASE][CAPITALIZE][COLOR red]"+caido+"  [COLOR white]"+server+"[COLOR orange]  "+name+" [/CAPITALIZE][/LOWERCASE][/B][/COLOR]", url = url,thumbnail=thumbnail,fanart = thumbnail,  folder=False,  isPlayable = True )
                 
        if 'upstream' in url:
            request_headers=[]
            request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])  
            body,response_headers = plugintools.read_body_and_headers( url, headers=request_headers)
            url1 = body.strip()
            finale = plugintools.find_single_match(url1,'sources: ..file:"(.*?)"')                 
            plugintools.add_item(action = "play_links" , title = "[B][LOWERCASE][CAPITALIZE][COLOR white]"+server+"[COLOR orange]  "+name+" [/CAPITALIZE][/LOWERCASE][/B][/COLOR]", url = finale,thumbnail=thumbnail,fanart = thumbnail,  folder=False,  isPlayable = True )                 
        plugintools.add_item(action = "play_resolver" ,thumbnail=thumbnail,fanart = thumbnail, title ="[B][LOWERCASE][CAPITALIZE][COLOR white]"+server+"[COLOR orange]  "+name+" [/CAPITALIZE][/LOWERCASE][/B][/COLOR]", url = url, folder=False,  isPlayable = True )  

    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]----[COLOR yellow]pepeseries servidores[COLOR aqua]----[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://st-listas.20minutos.es/images/2019-06/440207/5476186_640px.jpg?1567524986", fanart = "https://i.imgur.com/x89QdGV.jpg",  folder = False )   




    
#-----------------------pepeseries------------------------pepeseries-----------------------------pepeseries---------------------------------------- #-----------------------pepeseries------------------------pepeseries-----------------------------pepeseries---------------------------------------- #-----------------------pepeseries------------------------pepeseries-----------------------------pepeseries---------------------------------------- #-----------------------pepeseries------------------------pepeseries-----------------------------pepeseries---------------------------------------- #-----------------------pepeseries------------------------pepeseries-----------------------------pepeseries---------------------------------------- #-----------------------pepeseries------------------------pepeseries-----------------------------pepeseries---------------------------------------- #-----------------------pepeseries------------------------pepeseries-----------------------------pepeseries---------------------------------------- #-----------------------pepeseries------------------------pepeseries-----------------------------pepeseries---------------------------------------- #-----------------------pepeseries------------------------pepeseries-----------------------------pepeseries---------------------------------------- #-----------------------pepeseries------------------------pepeseries-----------------------------pepeseries---------------------------------------- #-----------------------pepeseries------------------------pepeseries-----------------------------pepeseries---------------------------------------- #-----------------------pepeseries------------------------pepeseries-----------------------------pepeseries---------------------------------------- #-----------------------pepeseries------------------------pepeseries-----------------------------pepeseries---------------------------------------- #-----------------------pepeseries------------------------pepeseries-----------------------------pepeseries---------------------------------------- #-----------------------pepeseries------------------------pepeseries-----------------------------pepeseries---------------------------------------- #-----------------------pepeseries------------------------pepeseries-----------------------------pepeseries---------------------------------------- #-----------------------pepeseries------------------------pepeseries-----------------------------pepeseries---------------------------------------- #-----------------------pepeseries------------------------pepeseries-----------------------------pepeseries---------------------------------------- #-----------------------pepeseries------------------------pepeseries-----------------------------pepeseries---------------------------------------- 























    
#----------------------MUNDOSERIES---------------MUNDOSERIES --------------------------MUNDOSERIES ------------------------MUNDOSERIES ---------- 
#----------------------MUNDOSERIES---------------MUNDOSERIES --------------------------MUNDOSERIES ------------------------MUNDOSERIES ---------- #----------------------MUNDOSERIES---------------MUNDOSERIES --------------------------MUNDOSERIES ------------------------MUNDOSERIES ---------- #----------------------MUNDOSERIES---------------MUNDOSERIES --------------------------MUNDOSERIES ------------------------MUNDOSERIES ---------- #----------------------MUNDOSERIES---------------MUNDOSERIES --------------------------MUNDOSERIES ------------------------MUNDOSERIES ---------- #----------------------MUNDOSERIES---------------MUNDOSERIES --------------------------MUNDOSERIES ------------------------MUNDOSERIES ---------- #----------------------MUNDOSERIES---------------MUNDOSERIES --------------------------MUNDOSERIES ------------------------MUNDOSERIES ---------- #----------------------MUNDOSERIES---------------MUNDOSERIES --------------------------MUNDOSERIES ------------------------MUNDOSERIES ---------- #----------------------MUNDOSERIES---------------MUNDOSERIES --------------------------MUNDOSERIES ------------------------MUNDOSERIES ---------- #----------------------MUNDOSERIES---------------MUNDOSERIES --------------------------MUNDOSERIES ------------------------MUNDOSERIES ---------- #----------------------MUNDOSERIES---------------MUNDOSERIES --------------------------MUNDOSERIES ------------------------MUNDOSERIES ---------- 

def mundo_series_menu(params):
    plugintools.log("chopocine.mundo_series_menu ")    
    plugintools.set_view(plugintools.LIST)  


    try:
        request_headers=[]    
        url="https://www.series24.me/ver-serie-completa/"
        request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
        body,response_headers = plugintools.read_body_and_headers( url, headers=request_headers)
        url = body.strip()
        detecta = plugintools.find_single_match(url,'content="(Series24)')
        if 'Series24' in detecta:
            plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]------------------------------[COLOR yellow]mundoseries[COLOR aqua]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://i.imgur.com/Du21mll.jpg", fanart = "https://i.imgur.com/Du21mll.jpg",  folder = False )  
  
            plugintools.add_item(action = "mundoseries_series" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]mundoseries todas [/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color,url="https://www.series24.me/ver-serie-completa/",  thumbnail ="https://i.imgur.com/Du21mll.jpg", fanart ="https://i.imgur.com/Du21mll.jpg", folder = True ) 
    
            plugintools.add_item(action = "mundoseries_series" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]mundoseries tendencias [/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color,url="https://www.series24.me/tendencias/",  thumbnail ="https://i.imgur.com/Du21mll.jpg", fanart ="https://i.imgur.com/Du21mll.jpg", folder = True )   
    
            plugintools.add_item(action = "mundoseries_ultimoscapis" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]mundoseries ultimos capitulos [/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color,url="https://www.series24.me/ver-serie-online/",  thumbnail ="https://i.imgur.com/Du21mll.jpg", fanart ="https://i.imgur.com/Du21mll.jpg", folder = True )    
    
            plugintools.add_item(action = "mundoseries_generos" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]mundoseries generos [/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color,url="https://www.series24.me/ver-serie-online/",  thumbnail ="https://i.imgur.com/Du21mll.jpg", fanart ="https://i.imgur.com/Du21mll.jpg", folder = True )   


            plugintools.add_item(action = "mundoseries_anios" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]mundoseries años [/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color,url="https://www.series24.me/ver-serie-online/",  thumbnail ="https://i.imgur.com/Du21mll.jpg", fanart ="https://i.imgur.com/Du21mll.jpg", folder = True )  

            plugintools.add_item(action = "mundoseries_busca" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]mundoseries buscador [/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color,url="https://www.series24.me/ver-serie-online/",  thumbnail ="https://i.imgur.com/Du21mll.jpg", fanart ="https://i.imgur.com/Du21mll.jpg", folder = True )  

            plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]------------------------------[COLOR yellow]mundoseries[COLOR aqua]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://i.imgur.com/Du21mll.jpg", fanart = "https://i.imgur.com/Du21mll.jpg",  folder = False )    
 
        else:
            r ='tu compañia te capa el acceso a mundoseries\nven al  grupo de telegram [COLOR aqua]@tvchopo [COLOR red]y te ayudamos'   
            plugintools.add_item(action = "play_links" ,title="[B][LOWERCASE][CAPITALIZE][COLOR red]"+r+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",   folder=False,  isPlayable = True ) 


    except:
        r ='tu compañia te capa el acceso a mundoseries\nven al  grupo de telegram [COLOR aqua]@tvchopo [COLOR red]y te ayudamos'   
        plugintools.add_item(action = "play_links" ,title="[B][LOWERCASE][CAPITALIZE][COLOR red]"+r+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",   folder=False,  isPlayable = True )  
 
 
def mundoseries_busca(params):  
    plugintools.log("chopocine.mundoseries_temporadas")    
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]------------------------------[COLOR yellow]mundoseries[COLOR aqua]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://i.imgur.com/Du21mll.jpg", fanart = "https://i.imgur.com/Du21mll.jpg",  folder = False )       
    dialog = xbmcgui.Dialog()
    d = dialog.input('[B][LOWERCASE][CAPITALIZE][COLOR orange]buscar una peli: ejemplo: [COLOR white]rocky[/COLOR][/CAPITALIZE][/LOWERCASE][/B]', type=xbmcgui.INPUT_ALPHANUM).replace(" ", "+")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers("https://www.series24.me/?s="+d, headers=request_headers)
    url = body.strip()
    matches = plugintools.find_multiple_matches(url,'<article><div (.*?)</article>')    
    for generos in matches: 
        plugintools.set_view(plugintools.TV_SHOWS)    
        url = plugintools.find_single_match(generos,'<a href="(.*?)"')
        foto = plugintools.find_single_match(generos,'src="(.*?)"')
        titulo = plugintools.find_single_match(generos,'alt="(.*?)"')
        anio = plugintools.find_single_match(generos,'class="year">(.*?)<')
        texto = plugintools.find_single_match(generos,'class="contenido"><p>(.*?)<')
        plugintools.add_item(action = "mundoseries_temporadas" , title ="[B][LOWERCASE][CAPITALIZE][COLOR yellow]"+titulo+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail =foto,fanart =foto,plot="[B][LOWERCASE][CAPITALIZE][COLOR white]"+texto+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",url=url,  folder = True )  
 
 
 

def mundoseries_generos(params):  
    plugintools.set_view(plugintools.LIST)
    plugintools.log("chopocine.mundoseries_temporadas")    
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]------------------------------[COLOR yellow]mundoseries[COLOR aqua]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://i.imgur.com/Du21mll.jpg", fanart = "https://i.imgur.com/Du21mll.jpg",  folder = False )       
    url = params.get("url")
    plot = params.get("plot")
    thumbnail = params.get("thumbnail")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers( url, headers=request_headers)
    url = body.strip()
    matches = plugintools.find_multiple_matches(url,'" class="menu-item menu-item-type-taxonomy menu-item-object-genres menu-item-(.*?)</li>')    
    for generos in matches:  
        titulo = plugintools.find_single_match(generos,'<a href="https://www.series24.me/series-genero/.*?/">(.*?)</a>')  
        url = plugintools.find_single_match(generos,'a href="(https://www.series24.me/series-genero.*?)"')
        plugintools.add_item(action = "mundoseries_series" , title ="[B][LOWERCASE][CAPITALIZE][COLOR yellow]"+titulo+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", url=url,  thumbnail=thumbnail,fanart =thumbnail,  folder = True ) 



def mundoseries_anios(params):  
    plugintools.set_view(plugintools.LIST)
    plugintools.log("chopocine.mundoseries_temporadas")    
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]------------------------------[COLOR yellow]mundoseries[COLOR aqua]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://i.imgur.com/Du21mll.jpg", fanart = "https://i.imgur.com/Du21mll.jpg",  folder = False )       
    url = params.get("url")
    plot = params.get("plot")
    thumbnail = params.get("thumbnail")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers( url, headers=request_headers)
    url = body.strip()
    matches = plugintools.find_multiple_matches(url,'(<li><a href="https://www.series24.me/series-de/.*?)</li>')    
    for generos in matches:  
        titulo = plugintools.find_single_match(generos,'<a href=".*?/">(.*?)</a>')  
        url = plugintools.find_single_match(generos,'a href="(.*?)"')
        plugintools.add_item(action = "mundoseries_series" , title ="[B][LOWERCASE][CAPITALIZE][COLOR white]series del año [COLOR yellow]"+titulo+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", url=url,  thumbnail=thumbnail,fanart =thumbnail,  folder = True ) 

 
    
def mundoseries_ultimoscapis(params):  
    plugintools.set_view(plugintools.LIST)
    plugintools.log("chopocine.mundoseries_temporadas")    
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]------------------------------[COLOR yellow]mundoseries[COLOR aqua]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://i.imgur.com/Du21mll.jpg", fanart = "https://i.imgur.com/Du21mll.jpg",  folder = False )       
    url = params.get("url")
    plot = params.get("plot")
    thumbnail = params.get("thumbnail")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers( url, headers=request_headers)
    url = body.strip()
    siguiente = plugintools.find_single_match(url,'rel="next" href="(.*?)"')
    matches = plugintools.find_multiple_matches(url,'article class="item se episodes" id="post-(.*?)</article>')    
    for generos in matches:  
        titulo = plugintools.find_single_match(generos,'class="serie">(.*?)<')
        foto = plugintools.find_single_match(generos,'class="poster">.*?<img src="(.*?)"')
        url = plugintools.find_single_match(generos,'a href="(.*?)"')
        plugintools.add_item(action = "mundoseries_servers" , title ="[B][LOWERCASE][CAPITALIZE][COLOR yellow]"+titulo+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", url=url, plot=plot, thumbnail=foto,fanart =foto,  folder = True ) 

    if 'http' in siguiente:
        plugintools.add_item( action="mundoseries_ultimoscapis" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]pagina  ir a la siguiente [COLOR yellow]aqui[/B][/COLOR][/CAPITALIZE][/LOWERCASE]", url= siguiente, thumbnail = "https://www.periodicoelpunto.com/wp-content/uploads/2019/03/flecha-siguiente.png",fanart = "https://www.periodicoelpunto.com/wp-content/uploads/2019/03/flecha-siguiente.png", folder=True ) 
                 
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]------------------------------[COLOR yellow]mundoseries[COLOR aqua]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://i.imgur.com/Du21mll.jpg", fanart = "https://i.imgur.com/Du21mll.jpg",  folder = False )           
    
def mundoseries_series(params):  
    plugintools.log("chopocine.mundoseries_series")    
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]------------------------------[COLOR yellow]mundoseries[COLOR aqua]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://i.imgur.com/Du21mll.jpg", fanart = "https://i.imgur.com/Du21mll.jpg",  folder = False )  
    plugintools.set_view(plugintools.LIST)    
    url = params.get("url")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers( url, headers=request_headers)
    url = body.strip()
    siguiente = plugintools.find_single_match(url,"lass=.current.>.*?</span><a href='(.*?)'")
    matches = plugintools.find_multiple_matches(url,'<article id="post-\d\d(.*?)</article>')    
    for generos in matches:          
        url = plugintools.find_single_match(generos,'href="(.*?)"')
        foto =plugintools.find_single_match(generos,'src="(.*?)"')
        titulo = plugintools.find_single_match(generos,'alt="(.*?)"')
        texto = plugintools.find_single_match(generos,'class="texto">(.*?)<')

        plugintools.add_item(action = "mundoseries_temporadas" , title ="[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",  thumbnail=foto, plot="[B][LOWERCASE][CAPITALIZE][COLOR gold]"+texto+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",url=url, fanart =foto,   folder = True ) 
    if 'http' in siguiente:  
        plugintools.add_item( action="mundoseries_series" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]pagina  ir a la siguiente [COLOR yellow]aqui[/B][/COLOR][/CAPITALIZE][/LOWERCASE]", url= siguiente, thumbnail = "https://www.periodicoelpunto.com/wp-content/uploads/2019/03/flecha-siguiente.png",fanart = "https://www.periodicoelpunto.com/wp-content/uploads/2019/03/flecha-siguiente.png", folder=True )
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]------------------------------[COLOR yellow]mundoseries[COLOR aqua]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://i.imgur.com/Du21mll.jpg", fanart = "https://i.imgur.com/Du21mll.jpg",  folder = False )        
        
def mundoseries_temporadas(params):  
    plugintools.set_view(plugintools.LIST)
    plugintools.log("chopocine.mundoseries_temporadas")    
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]------------------------------[COLOR yellow]mundoseries[COLOR aqua]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://i.imgur.com/Du21mll.jpg", fanart = "https://i.imgur.com/Du21mll.jpg",  folder = False )       
    url = params.get("url")
    plot = params.get("plot")
    thumbnail = params.get("thumbnail")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers( url, headers=request_headers)
    url = body.strip()
    var = plugintools.find_single_match(url,'var id  = (.*?);') 
    request_headers=[]   
    request_headers.append(['User-Agent','Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0'])
    request_headers.append(["Referer","https://www.series24.me/"])           
    custom_post='action=seasons&id='+var
    body,response_headers = plugintools.read_body_and_headers("https://www.series24.me/wp-admin/admin-ajax.php", post=custom_post)
    url = body.strip()
    matches = plugintools.find_multiple_matches(url,"(class='numerando'>.*?class='episodiotitle'>.*?a href='.*?</div>)")    
    for generos in matches:  
        titulo = plugintools.find_single_match(generos,"class='numerando'>(.*?)<")
        titulo2 = plugintools.find_single_match(generos,"<a href='.*?'>(.*?)</a>")
        url = plugintools.find_single_match(generos,"class='episodiotitle'>.*?a href='(.*?)'>.*?<.*?")
        plugintools.add_item(action = "mundoseries_servers" , title ="[B][LOWERCASE][CAPITALIZE][COLOR yellow]"+titulo2+" [COLOR white]---"+titulo+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", url=url, plot=plot, thumbnail=thumbnail,fanart =thumbnail,  folder = True ) 
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]------------------------------[COLOR yellow]mundoseries[COLOR aqua]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://i.imgur.com/Du21mll.jpg", fanart = "https://i.imgur.com/Du21mll.jpg",  folder = False )         
def mundoseries_servers(params):  
    plugintools.log("chopocine.series_papaya_estrenos")
    
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]------------------------------[COLOR yellow]mundoseries[COLOR aqua]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://i.imgur.com/Du21mll.jpg", fanart = "https://i.imgur.com/Du21mll.jpg",  folder = False )  
    thumbnail = params.get("thumbnail")
    url = params.get("url")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers( url, headers=request_headers)
    url = body.strip()
    goun = plugintools.find_multiple_matches(url,"(domain=goun.*?'.*?href='.*?'quality'>.*?.*?flags/.*?.png)")
    goun1 = plugintools.find_single_match(url,"domain=(ok.ru.*?'.*?href='.*?')")
    fembed = plugintools.find_multiple_matches(url,"(domain=goun.*?'.*?href='.*?'quality'>.*?.*?flags/.*?.png)")
    efe1 = plugintools.find_single_match(url,"domain=(ok.ru.*?'.*?href='.*?')") 
    okru = plugintools.find_multiple_matches(url,"(domain=ok.ru.*?'.*?href='.*?'quality'>.*?.*?flags/.*?.png)")
    oku1 = plugintools.find_single_match(url,"domain=(ok.ru.*?'.*?href='.*?')") 
    gamovideo = plugintools.find_multiple_matches(url,"(domain=gamovideo.*?'.*?href='.*?'quality'>.*?.*?flags/.*?.png)")
    gamo1 = plugintools.find_single_match(url,"domain=(gamovideo.*?'.*?href='.*?')") 
    vidoza = plugintools.find_multiple_matches(url,"(domain=vidoza.*?'.*?href='.*?'quality'>.*?.*?flags/.*?.png)")
    vido1 = plugintools.find_single_match(url,"domain=(vidoza.*?'.*?href='.*?')") 
    cloudvideo = plugintools.find_multiple_matches(url,"(domain=cloudvideo.*?href='.*?'quality'>.*?.*?flags/.*?.png)")
    cloud1 = plugintools.find_single_match(url,"domain=(cloudvideo.*?'.*?href='.*?')")
    onlystream = plugintools.find_multiple_matches(url,"(domain=onlystream.*?'.*?href='.*?'quality'>.*?.*?flags/.*?.png)")
    only1 = plugintools.find_single_match(url,"domain=(onlystream.*?'.*?href='.*?')")     
    clipwatching = plugintools.find_multiple_matches(url,"(domain=clipwatching.*?'.*?href='.*?'quality'>.*?.*?flags/.*?.png)")
    clip1 = plugintools.find_single_match(url,"domain=(clipwatching.*?)'") 

    if 'goun' in goun1:
        for generos in goun: 
            server = plugintools.find_single_match(generos,"domain=(goun.*?)'")  
            url = plugintools.find_single_match(generos,"domain=goun.*?'.*?href='(htt.*?//goun.*?)'.*?")
            idioma = plugintools.find_single_match(generos,"domain=goun.*?'.*?href='htt.*?//goun.*?'.*?quality'>.*?.*?flags/(.*?).png").replace('jp','subt')             
            plugintools.add_item(action = "play_resolver" , title ="[B][LOWERCASE][CAPITALIZE][COLOR white]"+server+"  [COLOR gold]idioma  "+idioma+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",thumbnail=thumbnail,fanart =thumbnail,  url=url ,   folder=False,  isPlayable = True ) 

    if 'ok.ru' in oku1:
        for generos in okru: 
            server = plugintools.find_single_match(generos,"domain=(ok.ru.*?)'")  
            url = plugintools.find_single_match(generos,"domain=ok.ru.*?'.*?href='(htt.*?//ok.ru.*?)'.*?")
            idioma = plugintools.find_single_match(generos,"domain=ok.ru.*?'.*?href='htt.*?//ok.ru.*?'.*?quality'>.*?.*?flags/(.*?).png").replace('jp','subt')             
            plugintools.add_item(action = "play_resolver" , title ="[B][LOWERCASE][CAPITALIZE][COLOR white]"+server+"  [COLOR gold]idioma  "+idioma+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",thumbnail=thumbnail,fanart =thumbnail,  url=url ,   folder=False,  isPlayable = True ) 

    if 'vidoza' in vido1:
        for generos in vidoza: 
            server = plugintools.find_single_match(generos,"domain=(vidoza.*?)'")  
            url = plugintools.find_single_match(generos,"domain=vidoza.*?'.*?href='(htt.*?//vidoza.*?)'.*?")
            idioma = plugintools.find_single_match(generos,"domain=vidoza.*?'.*?href='htt.*?//vidoza.*?'.*?quality'>.*?.*?flags/(.*?).png").replace('jp','subt')             
            plugintools.add_item(action = "play_resolver" , title ="[B][LOWERCASE][CAPITALIZE][COLOR white]"+server+"  [COLOR gold]idioma  "+idioma+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",thumbnail=thumbnail,fanart =thumbnail,  url=url ,   folder=False,  isPlayable = True ) 


  
    if 'clipwatching' in clip1:
        for generos in clipwatching: 
            url = plugintools.find_single_match(generos,"domain=clipwatching.*?'.*?href='(https://clipwatching.*?)'.*?")
            server = plugintools.find_single_match(generos,"domain=(clipwatching.*?)'")
            idioma = plugintools.find_single_match(generos,"domain=clipwatching.*?'.*?href='https://clipwatching.*?'.*?quality'>.*?.*?flags/(.*?).png").replace('jp','subt')           
            if 'clipwatching' in url:
                request_headers=[]
                request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
                body,response_headers = plugintools.read_body_and_headers( url, headers=request_headers)
                url1 = body.strip()
                final1 = plugintools.find_single_match(url1,'sources: ."(.*?)"')  
                plugintools.add_item(action = "play_links" , title ="[B][LOWERCASE][CAPITALIZE][COLOR white]"+server+"  [COLOR gold]idioma  "+idioma+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail=thumbnail,  fanart =thumbnail,url=final1,  folder=False,  isPlayable = True ) 
            
    if 'gamovideo' in gamo1:
        for generos in gamovideo: 
            server = plugintools.find_single_match(generos,"domain=(gamovideo.*?)'")  
            url = plugintools.find_single_match(generos,"domain=gamovideo.*?'.*?href='(htt.*?//gamovideo.*?)'.*?")
            idioma = plugintools.find_single_match(generos,"domain=gamovideo.*?'.*?href='htt.*?//gamovideo.*?'.*?quality'>.*?.*?flags/(.*?).png").replace('jp','subt')             
            plugintools.add_item(action = "play_resolver" , title ="[B][LOWERCASE][CAPITALIZE][COLOR white]"+server+"  [COLOR gold]idioma  "+idioma+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",thumbnail=thumbnail,fanart =thumbnail,  url=url ,   folder=False,  isPlayable = True ) 
            
            
    if 'cloudvideo' in cloud1:
        for generos in cloudvideo: 
            url = plugintools.find_single_match(generos,"domain=cloudvideo.*?'.*?href='(htt.*?//cloudvideo.*?)'.*?")
            server = plugintools.find_single_match(generos,"domain=(cloudvideo.*?)'") 
            idioma = plugintools.find_single_match(generos,"domain=cloudvideo.*?'.*?href='htt.*?//cloudvideo.*?'.*?quality'>.*?.*?flags/(.*?).png").replace('jp','subt')             
            plugintools.add_item(action = "play_resolver" , title ="[B][LOWERCASE][CAPITALIZE][COLOR white]"+server+"  [COLOR gold]idioma  "+idioma+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",thumbnail=thumbnail,fanart =thumbnail,  url=url ,   folder=False,  isPlayable = True ) 
            
            
    if 'onlystream' in only1:
        for generos in cloudvideo: 
            url = plugintools.find_single_match(generos,"domain=onlystream.*?'.*?href='(htt.*?//onlys.*?)'.*?").replace('embed-','')
            server = plugintools.find_single_match(generos,"domain=(onlystream.*?)'")        
            idioma = plugintools.find_single_match(generos,"domain=onlystream.*?'.*?href='htt.*?//onlystream.*?'.*?quality'>.*?.*?flags/(.*?).png").replace('jp','subt')             
            plugintools.add_item(action = "play_resolver" , title ="[B][LOWERCASE][CAPITALIZE][COLOR white]"+server+"  [COLOR gold]idioma  "+idioma+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",thumbnail=thumbnail,fanart =thumbnail,  url=url ,   folder=False,  isPlayable = True ) 
            
            
            
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]------------------------------[COLOR yellow]mundoseries[COLOR aqua]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://i.imgur.com/Du21mll.jpg", fanart = "https://i.imgur.com/Du21mll.jpg",  folder = False ) 
    
    
    
 #----------------------MUNDOSERIES---------------MUNDOSERIES --------------------------MUNDOSERIES ------------------------MUNDOSERIES ---------- 
#----------------------MUNDOSERIES---------------MUNDOSERIES --------------------------MUNDOSERIES ------------------------MUNDOSERIES ---------- #----------------------MUNDOSERIES---------------MUNDOSERIES --------------------------MUNDOSERIES ------------------------MUNDOSERIES ---------- #----------------------MUNDOSERIES---------------MUNDOSERIES --------------------------MUNDOSERIES ------------------------MUNDOSERIES ---------- #----------------------MUNDOSERIES---------------MUNDOSERIES --------------------------MUNDOSERIES ------------------------MUNDOSERIES ---------- #----------------------MUNDOSERIES---------------MUNDOSERIES --------------------------MUNDOSERIES ------------------------MUNDOSERIES ---------- #----------------------MUNDOSERIES---------------MUNDOSERIES --------------------------MUNDOSERIES ------------------------MUNDOSERIES ---------- #----------------------MUNDOSERIES---------------MUNDOSERIES --------------------------MUNDOSERIES ------------------------MUNDOSERIES ---------- #----------------------MUNDOSERIES---------------MUNDOSERIES --------------------------MUNDOSERIES ------------------------MUNDOSERIES ---------- #----------------------MUNDOSERIES---------------MUNDOSERIES --------------------------MUNDOSERIES ------------------------MUNDOSERIES ---------- #----------------------MUNDOSERIES---------------MUNDOSERIES --------------------------MUNDOSERIES ------------------------MUNDOSERIES ----------    
    
    
    
    
    
    
#--------------SERIES PAPAYA---------------------SERIES PAPAYA--------------------------------SERIES PAPAYA-----------------------SERIES PAPAYA---
#--------------SERIES PAPAYA---------------------SERIES PAPAYA--------------------------------SERIES PAPAYA-----------------------SERIES PAPAYA---#--------------SERIES PAPAYA---------------------SERIES PAPAYA--------------------------------SERIES PAPAYA-----------------------SERIES PAPAYA---#--------------SERIES PAPAYA---------------------SERIES PAPAYA--------------------------------SERIES PAPAYA-----------------------SERIES PAPAYA---#--------------SERIES PAPAYA---------------------SERIES PAPAYA--------------------------------SERIES PAPAYA-----------------------SERIES PAPAYA---#--------------SERIES PAPAYA---------------------SERIES PAPAYA--------------------------------SERIES PAPAYA-----------------------SERIES PAPAYA---#--------------SERIES PAPAYA---------------------SERIES PAPAYA--------------------------------SERIES PAPAYA-----------------------SERIES PAPAYA---#--------------SERIES PAPAYA---------------------SERIES PAPAYA--------------------------------SERIES PAPAYA-----------------------SERIES PAPAYA---#--------------SERIES PAPAYA---------------------SERIES PAPAYA--------------------------------SERIES PAPAYA-----------------------SERIES PAPAYA---#--------------SERIES PAPAYA---------------------SERIES PAPAYA--------------------------------SERIES PAPAYA-----------------------SERIES PAPAYA---
def menu_seriespapaya(params):
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]------------------------------[COLOR yellow]menu series papaya[COLOR aqua]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://i.imgur.com/9a16ENI.jpg", fanart = "https://i.imgur.com/9a16ENI.jpg",  folder = False )    
    
    
    
    plugintools.add_item(action = "series_papaya_novedades" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]series papaya lo nuevo hoy[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color,  thumbnail ="http://i.imgur.com/P1D92cf.png", fanart ="http://i.imgur.com/P1D92cf.png", url="https://www.seriespapaya.nu", folder = True ) 


    plugintools.add_item(action = "letras_papaya" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]series papaya por letras[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color, thumbnail ="http://i.imgur.com/P1D92cf.png", fanart ="http://i.imgur.com/P1D92cf.png",  folder = True  ) 

    
    plugintools.add_item(action = "series_papaya_estrenos" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]series papaya estrenos[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color, thumbnail ="http://i.imgur.com/P1D92cf.png", fanart ="http://i.imgur.com/P1D92cf.png", url="https://www.seriespapaya.nu/lista-series-estrenos/", folder = True )
    
    plugintools.add_item(action = "series_papaya_estrenos" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]series papaya las mas populares[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color, thumbnail ="http://i.imgur.com/P1D92cf.png", fanart ="http://i.imgur.com/P1D92cf.png", url="https://www.seriespapaya.nu/lista-series-populares/", folder = True )
    
    plugintools.add_item(action = "series_papaya_estrenos" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]series papaya las mas recomendadas[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color, thumbnail ="http://i.imgur.com/P1D92cf.png", fanart ="http://i.imgur.com/P1D92cf.png", url="https://www.seriespapaya.nu/lista-series-recomendadas/", folder = True )

    plugintools.add_item(action = "series_papaya_buscador" , title = "[B][LOWERCASE][CAPITALIZE][COLOR %s]series papaya buscador[/CAPITALIZE][/LOWERCASE][/B][/COLOR]"% Set_Color, thumbnail ="http://i.imgur.com/P1D92cf.png", fanart ="http://i.imgur.com/P1D92cf.png", url="https://www.seriespapaya.nu/lista-series-recomendadas/", folder = True )
    
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]------------------------------[COLOR yellow]menu series papaya[COLOR aqua]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://i.imgur.com/9a16ENI.jpg", fanart = "https://i.imgur.com/9a16ENI.jpg",  folder = False )   

def series_papaya_buscador(params):
    plugintools.log("chopocine.series_papaya_buscador "+repr(params))
    plugintools.set_view(plugintools.LIST)
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR gold]---[COLOR aqua]series papaya resultado de la busqueda[COLOR gold]---[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="http://i.imgur.com/P1D92cf.png", fanart ="http://i.imgur.com/P1D92cf.png",  folder = False ) 
    dialog = xbmcgui.Dialog()
    d = dialog.input('[B][LOWERCASE][CAPITALIZE][COLOR orange]buscar una peli: ejemplo: [COLOR white]rocky[/COLOR][/CAPITALIZE][/LOWERCASE][/B]', type=xbmcgui.INPUT_ALPHANUM).replace(" ", "+")
    request_headers=[]   
    request_headers.append(['User-Agent','Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0'])
    request_headers.append(["Referer","https://www.seriespapaya.nu/busqueda/"])           
    custom_post="searchquery="+d
    body,response_headers = plugintools.read_body_and_headers("https://www.seriespapaya.nu/busqueda/", post=custom_post)
    url = body.strip()
    matches = plugintools.find_multiple_matches(url,'(class="capitulo-caja.*?style="display: table.*? </div>)')
    for generos in matches: 
        titulo = plugintools.find_single_match(generos,'165px; ">\s*(.*?)\s*<')
        url = "https://www.seriespapaya.nu"+plugintools.find_single_match(generos," onclick=.location.href='(.*?)'")
        foto = "https://www.seriespapaya.nu"+plugintools.find_single_match(generos,"image: url.'(.*?)'")
        
        plugintools.add_item(action = "series_papaya_temporadas" , thumbnail=foto,fanart =foto,title ="[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",url= url,   folder = True )
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR gold]---[COLOR aqua]series papaya resultado de la busqueda[COLOR gold]---[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="http://i.imgur.com/P1D92cf.png", fanart ="http://i.imgur.com/P1D92cf.png",  folder = False )   
def series_papaya_estrenos(params):  
    plugintools.log("chopocine.series_papaya_estrenos")
    
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]-----[COLOR aqua]series papaya novedades[COLOR yellow]-----[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="http://i.imgur.com/P1D92cf.png", fanart ="http://i.imgur.com/P1D92cf.png",  folder = False )  
      
    url = params.get("url")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers( url, headers=request_headers)
    url = body.strip()
    matches = plugintools.find_multiple_matches(url,'class="esimagen">(.*?) class="esdur">')
    for generos in matches: 
        plugintools.set_view(plugintools.TV_SHOWS)
        url = "https://www.seriespapaya.nu/"+plugintools.find_single_match(generos,'href="(.*?)"')
        foto ="https://www.seriespapaya.nu/"+ plugintools.find_single_match(generos,'src="(.*?)"')
        titulo = plugintools.find_single_match(generos,' class="esenla">(.*?)<.*?')
        anio = plugintools.find_single_match(generos,'</a> (.*?)<')
        texto = plugintools.find_single_match(generos,'class="essin">(.*?)<')
   
        plugintools.add_item(action = "series_papaya_temporadas" , title ="[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo+"  [COLOR gold]"+anio+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",  thumbnail=foto, plot="[B][LOWERCASE][CAPITALIZE][COLOR gold]"+texto+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",url=url, fanart =foto,   folder = True ) 





def letras_papaya(params):  
    plugintools.log("chopocine.series_papaya")
    
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]-----[COLOR aqua]series papaya letras[COLOR yellow]-----[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="http://i.imgur.com/P1D92cf.png", fanart ="http://i.imgur.com/P1D92cf.png",  folder = False )  
    plugintools.set_view(plugintools.LIST)  
    request_headers=[] 
    request_headers.append(['User-Agent','Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0'])
    request_headers.append(["Referer","https://www.seriespapaya.nu/"])           
    body,response_headers = plugintools.read_body_and_headers("https://www.seriespapaya.nu/")
    url = body.strip()
    matches = plugintools.find_multiple_matches(url,'series que empiezan por .*?" href="lista-series-.*?">.*?</a>')
    for generos in matches: 
        url = plugintools.find_single_match(generos,'href="lista-series-(.*?)/"')
        titulo= plugintools.find_single_match(generos,'href="lista-series.*?">(.*?)</a>')
        plugintools.add_item(action = "seriesletras_papaya" , plot= "0",title ="[B][LOWERCASE][CAPITALIZE][COLOR yellow]series que empiezan por [COLOR white] "+titulo+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",thumbnail ="http://i.imgur.com/P1D92cf.png", fanart ="http://i.imgur.com/P1D92cf.png",url=url,folder = True ) 
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]-----[COLOR aqua]series papaya letras[COLOR yellow]-----[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="http://i.imgur.com/P1D92cf.png", fanart ="http://i.imgur.com/P1D92cf.png",  folder = False )
    
def seriesletras_papaya(params):  
    plugintools.log("chopocine.series_papaya")
    
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]-----[COLOR aqua]series papaya[COLOR yellow]-----[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",thumbnail ="http://i.imgur.com/P1D92cf.png", fanart ="http://i.imgur.com/P1D92cf.png",  folder = False )  
     
    url5 = params.get("url")
    request_headers=[]
    numero= params.get("plot")    
    request_headers.append(['User-Agent','Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0'])
    request_headers.append(["Referer","https://www.seriespapaya.nu/lista-series-"+url5+"/"])           
    custom_post="group_no="+numero+"&letra="+url5
    body,response_headers = plugintools.read_body_and_headers("https://www.seriespapaya.nu/autoload_process.php", post=custom_post)
    url = body.strip()
    matches = plugintools.find_multiple_matches(url,'<div class="list_imagen">(.*?)list_ver">')
    for generos in matches: 
        plugintools.set_view(plugintools.TV_SHOWS)
        foto= "https://www.seriespapaya.nu/"+plugintools.find_single_match(generos,'img src="(.*?)"')
        url= "https://www.seriespapaya.nu/"+plugintools.find_single_match(generos,'href="(.*?)"')
        titulo= plugintools.find_single_match(generos,'list_titulo"><a href=".*?">(.*?)<')
        texto= plugintools.find_single_match(generos,'list_justify">(.*?)<')
        ano= plugintools.find_single_match(generos,'list_ano"><b>.*?:</b> (.*?)<')
        plugintools.add_item(action = "series_papaya_temporadas" ,url=url, thumbnail =foto,  fanart =foto,title ="[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo+"[COLOR gold]  "+ano+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",info_labels={ "year" :ano,  "Plot" :"[COLOR lime]"+texto+"[/COLOR]"},    folder = True ) 
        s='sumar'
    def dec(s):
        a = int("1")
        b = int(numero)
        suma = a+b
        return (str(suma))
    esto = dec(s)
    plugintools.add_item( action="seriesletras_papaya" , title = "[B][LOWERCASE][CAPITALIZE][COLOR lime]ir a la pagina siguiente[/B][/COLOR][/CAPITALIZE][/LOWERCASE]",url=url5, plot= esto, thumbnail = "https://www.periodicoelpunto.com/wp-content/uploads/2019/03/flecha-siguiente.png",fanart = "https://www.periodicoelpunto.com/wp-content/uploads/2019/03/flecha-siguiente.png", folder=True )

    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]-----[COLOR aqua]series papaya[COLOR yellow]-----[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="http://i.imgur.com/P1D92cf.png", fanart ="http://i.imgur.com/P1D92cf.png",  folder = False )  

def series_papaya_novedades(params):  
    plugintools.log("chopocine.series_papaya_novedades")
    
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]---------------------[COLOR aqua]series papaya novedades[COLOR yellow]---------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="http://i.imgur.com/P1D92cf.png", fanart ="http://i.imgur.com/P1D92cf.png",  folder = False )  
    plugintools.set_view(plugintools.MOVIES,502)  
    url = params.get("url")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers( url, headers=request_headers)
    url = body.strip()
    matches = plugintools.find_multiple_matches(url,'<div class="ulticap">.*?</div>.*?<div class="ultitop">.*?<a class="ultiti".*?href=".*?">.*?</div>.*?</div>')
    for generos in matches: 
        url = "https://www.seriespapaya.nu/"+plugintools.find_single_match(generos,'href="(.*?)"')
        foto ="https://www.seriespapaya.nu/"+ plugintools.find_single_match(generos,'src="(.*?)"')
        titulo = plugintools.find_single_match(generos,'href=".*?">(.*?)<.*?')
        tempo = plugintools.find_single_match(generos,'(Temporada.*?). C')
    
   
        plugintools.add_item(action = "series_papaya_servidores" , title ="[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo+"  [COLOR gold]"+tempo+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",  thumbnail=foto, url=url, fanart =foto,   folder = True ) 
        
        
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]---------------------[COLOR aqua]series papaya novedades[COLOR yellow]---------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="http://i.imgur.com/P1D92cf.png", fanart ="http://i.imgur.com/P1D92cf.png",  folder = False )       
        
def series_papaya_temporadas(params):  
    plugintools.log("chopocine.series_papaya")
    
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]----[COLOR aqua]series papaya[COLOR yellow]----[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="http://i.imgur.com/P1D92cf.png", fanart ="http://i.imgur.com/P1D92cf.png",  folder = False )  
    plugintools.set_view(plugintools.MOVIES,502)  
    url = params.get("url")
    thumbnail = params.get("thumbnail")
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers( url, headers=request_headers)
    url = body.strip()
    matches = plugintools.find_multiple_matches(url,'(<a class="visco" href=".*?</a>)')
    for generos in matches: 
        url = "https://www.seriespapaya.nu/"+plugintools.find_single_match(generos,'href="(.*?)"')
        titulo = plugintools.find_single_match(generos,'/>&nbsp; (.*?)<')

    
   
        plugintools.add_item(action = "series_papaya_servidores" , title ="[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",  thumbnail=thumbnail, url=url, fanart =thumbnail,   folder = True ) 

    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]----[COLOR aqua]series papaya[COLOR yellow]----[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="http://i.imgur.com/P1D92cf.png", fanart ="http://i.imgur.com/P1D92cf.png",  folder = False )

    
def series_papaya_servidores(params):  
    plugintools.log("chopocine.series_papaya_servidores")
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]----[COLOR aqua]series papaya[COLOR yellow]----[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="http://i.imgur.com/P1D92cf.png", fanart ="http://i.imgur.com/P1D92cf.png",  folder = False )  
    url = params.get("url")
    thumbnail = params.get("thumbnail")  
    request_headers=[]
    request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
    body,response_headers = plugintools.read_body_and_headers( url, headers=request_headers)
    url = body.strip()
    matches = plugintools.find_multiple_matches(url,'(class="mtos">.*?src="images/reproducir)')
    for generos in matches: 
        idioma = plugintools.find_single_match(generos,' class="didioma">.*?<img src="images/(.*?).png".*?').replace('in','vo')
        server = plugintools.find_single_match(generos,'class="dservidor">.*?<img src=./images/online/.*?.png. /> (.*?)</div>').replace('Streamplay','Streamplay--[COLOR red]no elegir').replace('Powvideo','Powvideo--[COLOR red]no elegir').replace('Jetload','Jetload--[COLOR red]no elegir').replace('Waaw','Waaw--[COLOR red]no elegir').replace('Easyload','Easyload--[COLOR red]no elegir').replace('todo','vidtodo--[COLOR red]no elegir')
        url3 = plugintools.find_single_match(generos,'class="denlace">.*?<a href="(.*?)"')+"/"
        request_headers=[]
        request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
        body,response_headers = plugintools.read_body_and_headers( "https://www.seriespapaya.nu"+url3+"/", headers=request_headers)
        cuerpo = body.strip()
        final = plugintools.find_single_match(cuerpo,"location.href='(.*?)'").replace('vidtodo','vidtodop')  
        if 'clipwatching' in final:
            request_headers=[]

            request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
            body,response_headers = plugintools.read_body_and_headers( final, headers=request_headers)
            url1 = body.strip()
            final1 = plugintools.find_single_match(url1,'sources: ."(.*?)"')  
            plugintools.add_item(action = "play_links" , title ="[B][LOWERCASE][CAPITALIZE][COLOR white]idioma  "+idioma+"---[COLOR gold]servidor "+server+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail=thumbnail,  fanart =thumbnail,url=final1,  folder=False,  isPlayable = True ) 
          

        else:   
            plugintools.add_item(action = "play_resolver" , title ="[B][LOWERCASE][CAPITALIZE][COLOR white]idioma  "+idioma+"---[COLOR gold]servidor "+server+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",  thumbnail=thumbnail, url=final, fanart =thumbnail,  folder=False,  isPlayable = True )
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR yellow]----[COLOR aqua]series papaya[COLOR yellow]----[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="http://i.imgur.com/P1D92cf.png", fanart ="http://i.imgur.com/P1D92cf.png",  folder = False )  
    
    
    
#--------------SERIES PAPAYA---------------------SERIES PAPAYA--------------------------------SERIES PAPAYA-----------------------SERIES PAPAYA---
#--------------SERIES PAPAYA---------------------SERIES PAPAYA--------------------------------SERIES PAPAYA-----------------------SERIES PAPAYA---#--------------SERIES PAPAYA---------------------SERIES PAPAYA--------------------------------SERIES PAPAYA-----------------------SERIES PAPAYA---#--------------SERIES PAPAYA---------------------SERIES PAPAYA--------------------------------SERIES PAPAYA-----------------------SERIES PAPAYA---#--------------SERIES PAPAYA---------------------SERIES PAPAYA--------------------------------SERIES PAPAYA-----------------------SERIES PAPAYA---#--------------SERIES PAPAYA---------------------SERIES PAPAYA--------------------------------SERIES PAPAYA-----------------------SERIES PAPAYA---#--------------SERIES PAPAYA---------------------SERIES PAPAYA--------------------------------SERIES PAPAYA-----------------------SERIES PAPAYA---#--------------SERIES PAPAYA---------------------SERIES PAPAYA--------------------------------SERIES PAPAYA-----------------------SERIES PAPAYA---#--------------SERIES PAPAYA---------------------SERIES PAPAYA--------------------------------SERIES PAPAYA-----------------------SERIES PAPAYA---#--------------SERIES PAPAYA---------------------SERIES PAPAYA--------------------------------SERIES PAPAYA----------------    
    
    
    
    
    
    
    
#-------------reproductores-----------------------------reproductores ----------------------------------reproductores ----------------------  
#-------------reproductores-----------------------------reproductores ----------------------------------reproductores ----------------------  
#-------------reproductores-----------------------------reproductores ----------------------------------reproductores ----------------------  
#-------------reproductores-----------------------------reproductores ----------------------------------reproductores ----------------------  #-------------reproductores-----------------------------reproductores ----------------------------------reproductores ----------------------  #-------------reproductores-----------------------------reproductores ----------------------------------reproductores ----------------------  #-------------reproductores-----------------------------reproductores ----------------------------------reproductores ----------------------  #-------------reproductores-----------------------------reproductores ----------------------------------reproductores ----------------------  #-------------reproductores-----------------------------reproductores ----------------------------------reproductores ----------------------  #-------------reproductores-----------------------------reproductores ----------------------------------reproductores ----------------------  #-------------reproductores-----------------------------reproductores ----------------------------------reproductores ----------------------  
    
def play_resolver(params):
    import resolveurl 
    try:  
        video = resolveurl.resolve( params.get("url") ) 
        plugintools.play_resolved_url( video ) 
    except: 
        u= xbmc.executebuiltin('XBMC.Notification([B][LOWERCASE][CAPITALIZE][COLOR white]enlace  [COLOR red]borrado [/CAPITALIZE][/LOWERCASE][/B][/COLOR],[B][LOWERCASE][CAPITALIZE][COLOR white]elige otro [/CAPITALIZE][/LOWERCASE][/B][/COLOR], 4000)')
        plugintools.add_item(action = "servidores" , title = u,  folder = True ) 


def play_links(params): 
    try:  
        plugintools.play_resolved_url( params.get("url") ) 

    except: 
        u= xbmc.executebuiltin('XBMC.Notification([B][LOWERCASE][CAPITALIZE][COLOR white]enlace  [COLOR red]borrado [/CAPITALIZE][/LOWERCASE][/B][/COLOR],[B][LOWERCASE][CAPITALIZE][COLOR white]elige otro [/CAPITALIZE][/LOWERCASE][/B][/COLOR], 4000)')
        plugintools.add_item(action = "servidores" , title = u,  folder = True ) 

#------------------------------megabuscador----------------------------megabuscador--------------------------------------------------------------
#------------------------------megabuscador----------------------------megabuscador--------------------------------------------------------------
#------------------------------megabuscador----------------------------megabuscador--------------------------------------------------------------
#------------------------------megabuscador----------------------------megabuscador--------------------------------------------------------------
#------------------------------megabuscador----------------------------megabuscador--------------------------------------------------------------
#------------------------------megabuscador----------------------------megabuscador--------------------------------------------------------------
#------------------------------megabuscador----------------------------megabuscador--------------------------------------------------------------
#------------------------------megabuscador----------------------------megabuscador--------------------------------------------------------------
#------------------------------megabuscador----------------------------megabuscador--------------------------------------------------------------


def mega_buscador(params):
    plugintools.log("chopocine.series_papaya_buscador "+repr(params))
    plugintools.set_view(plugintools.LIST)
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR gold]---[COLOR aqua]series papaya resultado de la busqueda[COLOR gold]---[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="http://i.imgur.com/P1D92cf.png", fanart ="http://i.imgur.com/P1D92cf.png",  folder = False ) 
    dialog = xbmcgui.Dialog()
    d = dialog.input('[B][LOWERCASE][CAPITALIZE][COLOR orange]buscar una peli: ejemplo: [COLOR white]rocky[/COLOR][/CAPITALIZE][/LOWERCASE][/B]', type=xbmcgui.INPUT_ALPHANUM).replace(" ", "+")
    try:
        request_headers=[]   
        request_headers.append(['User-Agent','Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0'])
        request_headers.append(["Referer","https://www.seriespapaya.nu/busqueda/"])           
        custom_post="searchquery="+d
        body,response_headers = plugintools.read_body_and_headers("https://www.seriespapaya.nu/busqueda/", post=custom_post)
        url = body.strip()
        matches = plugintools.find_multiple_matches(url,'(class="capitulo-caja.*?style="display: table.*? </div>)')
        for generos in matches: 
            titulo = plugintools.find_single_match(generos,'165px; ">\s*(.*?)\s*<')
            url = "https://www.seriespapaya.nu"+plugintools.find_single_match(generos," onclick=.location.href='(.*?)'")
            foto = "https://www.seriespapaya.nu"+plugintools.find_single_match(generos,"image: url.'(.*?)'")
        
            plugintools.add_item(action = "series_papaya_temporadas" , thumbnail=foto,fanart =foto,title ="[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",url= url,   folder = True )

    except:
        r ='tu compañia te capa el acceso a papaya\nven al  grupo de telegram [COLOR aqua]@tvchopo [COLOR red]y te ayudamos'   
        plugintools.add_item(action = "play_links" ,title="[B][LOWERCASE][CAPITALIZE][COLOR red]"+r+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",   folder=False,  isPlayable = True )
   
    
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR gold]---[COLOR aqua]mundo series resultado de la busqueda[COLOR gold]---[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="http://i.imgur.com/P1D92cf.png", fanart ="http://i.imgur.com/P1D92cf.png",  folder = False ) 
    try:
        request_headers=[]
        request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
        body,response_headers = plugintools.read_body_and_headers("https://www.series24.me/?s="+d, headers=request_headers)
        url = body.strip()
        matches = plugintools.find_multiple_matches(url,'<article><div (.*?)</article>')    
        for generos in matches: 
   
            url = plugintools.find_single_match(generos,'<a href="(.*?)"')
            foto = plugintools.find_single_match(generos,'src="(.*?)"')
            titulo = plugintools.find_single_match(generos,'alt="(.*?)"')
            anio = plugintools.find_single_match(generos,'class="year">(.*?)<')
            texto = plugintools.find_single_match(generos,'class="contenido"><p>(.*?)<')
            plugintools.add_item(action = "mundoseries_temporadas" , title ="[B][LOWERCASE][CAPITALIZE][COLOR yellow]"+titulo+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail =foto,fanart =foto,plot="[B][LOWERCASE][CAPITALIZE][COLOR white]"+texto+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",url=url,  folder = True )  
            
            
    except:
        r ='tu compañia te capa el acceso a mundoseries\nven al  grupo de telegram [COLOR aqua]@tvchopo [COLOR red]y te ayudamos'   
        plugintools.add_item(action = "play_links" ,title="[B][LOWERCASE][CAPITALIZE][COLOR red]"+r+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",   folder=False,  isPlayable = True ) 
    plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR gold]---[COLOR aqua]pepeseries resultado de la busqueda[COLOR gold]---[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://i.imgur.com/9a16ENI.jpg", fanart = "https://i.imgur.com/9a16ENI.jpg",  folder = False )    
    try:
        request_headers=[]
        request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
        body,response_headers = plugintools.read_body_and_headers('https://pepecine.to/secure/search/'+d+'?type=&limit=16', headers=request_headers)
        url = body.strip()
        matches = plugintools.find_multiple_matches(url,'.{"id":.*?,"name":".*?".*?poster":".*?".*?is_series')    
        for generos in matches: 
            plugintools.set_view(plugintools.LIST)    
            ids = plugintools.find_single_match(generos,'.{"id":(.*?),"name":".*?".*?poster":"')
            titulo = plugintools.find_single_match(generos,'"id":.*?,"name":"(.*?)","year":.*?.*?,"')
            anio = plugintools.find_single_match(generos,'","year":(.*?),"')
            foto = plugintools.find_single_match(generos,'poster":"(.*?)","is_series"').replace("\\", "")
       
            plugintools.add_item(action = "pepeseries_temporadas" , title ="[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo+"  [COLOR yellow]"+anio+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail =foto,fanart =foto,url=ids,  folder = True )      
            
 
    except:
        r ='tu compañia te capa el acceso a pepeseries\nven al  grupo de telegram [COLOR aqua]@tvchopo [COLOR red]y te ayudamos'   
        plugintools.add_item(action = "play_links" ,title="[B][LOWERCASE][CAPITALIZE][COLOR red]"+r+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",   folder=False,  isPlayable = True ) 
    
    
    try:
        plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]------------------------------[COLOR yellow]series danko buscador[COLOR aqua]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://beautifulgishi.com/wp-content/uploads/2018/09/series.jpg", fanart = "https://beautifulgishi.com/wp-content/uploads/2018/09/series.jpg",  folder = False )      
        url= "http://ab-kkk.com/?s="+d
        request_headers=[]
        request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
        body,response_headers = plugintools.read_body_and_headers(url, headers=request_headers)
        url = body.strip()   
        matches = plugintools.find_multiple_matches(url,'(<a href="http://ab-kkk.com/capitulos/.*?class="attachment-thumbnail size-thumbnail wp-post-image)')       
        for generos in matches: 
            url = plugintools.find_single_match(generos,'<a href="(.*?)"')
            titulo = plugintools.find_single_match(generos,'<a href="http://ab-kkk.com/capitulos/(.*?)/').replace('-',' ')
            foto = plugintools.find_single_match(generos,'src="(.*?)"')
            plugintools.add_item(action = "series_danko_temporadas" , title ="[B][LOWERCASE][CAPITALIZE][COLOR gold][COLOR white] "+titulo+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", url=url, thumbnail =foto,fanart =foto, folder = True )  
            
    except:
        r ='tu compañia te capa el acceso a pepeseries\nven al  grupo de telegram [COLOR aqua]@tvchopo [COLOR red]y te ayudamos'   
        plugintools.add_item(action = "play_links" ,title="[B][LOWERCASE][CAPITALIZE][COLOR red]"+r+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",   folder=False,  isPlayable = True ) 
 

    try:
        plugintools.add_item(action = "" , title ="[B][LOWERCASE][CAPITALIZE][COLOR yellow]----------[COLOR white] series dilo[COLOR red] busqueda[COLOR yellow]----------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://i.imgur.com/bEWd9YM.jpg", fanart = "https://i.imgur.com/bEWd9YM.jpg",  folder = False ) 
        request_headers=[]
        request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
        body,response_headers = plugintools.read_body_and_headers("https://www.dilo.nu/search?s="+d, headers=request_headers)
        url = body.strip()       
        matches = plugintools.find_multiple_matches(url,'(<div class="col-lg-2 col-md-3 col-6 mb-3">.*?txt-gray-700">Duración)')
        for generos in matches:    
            url = plugintools.find_single_match(generos,'a href="(.*?)"')
            foto = plugintools.find_single_match(generos,'img src="(.*?)"') 
            titulo = plugintools.find_single_match(generos,'weight-500">(.*?)<')
            anio = plugintools.find_single_match(generos,'txt-size-12">(.*?)<')
            texto = plugintools.find_single_match(generos,'description">(.*?)<')
        
            plugintools.add_item(action = "series_dilo_temporadas" ,url= url, title ="[B][LOWERCASE][CAPITALIZE][COLOR white]  "+titulo+"[COLOR aqua]  "+anio+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]" ,thumbnail =foto, fanart = foto, folder = True )      
 

    except:
        r ='tu compañia te capa el acceso a diloseries\nven al  grupo de telegram [COLOR aqua]@tvchopo [COLOR red]y te ayudamos'   
        plugintools.add_item(action = "play_links" ,title="[B][LOWERCASE][CAPITALIZE][COLOR red]"+r+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",   folder=False,  isPlayable = True ) 

        
    try:
        plugintools.add_item(action = "" , title = "[B][LOWERCASE][CAPITALIZE][COLOR aqua]------------------------------[COLOR yellow]retroseriestv [COLOR aqua]--------------------------------------[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail ="https://i.imgur.com/hkMvrC4.jpg", fanart = "https://i.imgur.com/oArwph7.jpg",  folder = False ) 
        url= "https://retroseriestv.com/?s="+d
        request_headers=[]
        request_headers.append(["User-Agent","Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0"])
        body,response_headers = plugintools.read_body_and_headers(url, headers=request_headers)
        url = body.strip()
        matches = plugintools.find_multiple_matches(url,'(class="image">.*?a href=".*?">.*?<p>.*?</p>)')      
        for generos in matches: 
            url = plugintools.find_single_match(generos,'href="(.*?)"')
            titulo = plugintools.find_single_match(generos,'alt="(.*?)"')  
            foto = plugintools.find_single_match(generos,'img src="(.*?)"')
            anio = plugintools.find_single_match(generos,'class="year">(.*?)<.*?')
            texto = plugintools.find_single_match(generos,'class="contenido"><p>(.*?)</p>')        
            plugintools.add_item(action = "retrotv_series_temporadas" , title ="[B][LOWERCASE][CAPITALIZE][COLOR white]"+titulo+" [COLOR gold] "+anio+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]", thumbnail =foto, fanart = foto,url=url, plot=texto, folder = True )
            
            
            
    except:
        r ='tu compañia te capa el acceso a retroseries\nven al  grupo de telegram [COLOR aqua]@tvchopo [COLOR red]y te ayudamos'   
        plugintools.add_item(action = "play_links" ,title="[B][LOWERCASE][CAPITALIZE][COLOR red]"+r+"[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",   folder=False,  isPlayable = True )            
 
run()