# -*- coding: utf-8 -*-
#------------------------------------------------------------
# chopodplay - XBMC Add-on by Torete
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
import unicodedata
import base64
import requests
import shutil
import base64
import time




addon = xbmcaddon.Addon()
addonname = '[B][LOWERCASE][CAPITALIZE][COLOR white]chopo[COLOR gold]dplay[/CAPITALIZE][/LOWERCASE][/B][/COLOR]'
icon = addon.getAddonInfo('icon')
myaddon = xbmcaddon.Addon("plugin.video.chopodplay")
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
       exec action+"(params)"

    plugintools.close_item_list()


#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------
#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------
#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------#---------MENU PRINCIPAL-----------------------MENU PRINCIPAL----------------------------MENU PRINCIPAL---------------------------------------


   

def main_list(params):
    plugintools.log("chopodplay.main_list ")    
    plugintools.set_view(plugintools.LIST)  


 
    plugintools.add_item(action = "menu_principal" , title = "[B][LOWERCASE][CAPITALIZE][COLOR white]este addon deja de funcionar[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",thumbnail ="https://static.wikia.nocookie.net/logopedia/images/a/a6/Discovery_Plus_logo_%28stacked%29.png/revision/latest?cb=20201227091030", fanart = "https://i.imgur.com/Jj8EwmC.jpg", folder = True )
 
 
   
 
    plugintools.add_item(action = "menu_principal" , title = "[B][LOWERCASE][CAPITALIZE][COLOR white]ahora teneis el nuevo addon llamado[/CAPITALIZE][/LOWERCASE][/B][/COLOR]",thumbnail ="https://static.wikia.nocookie.net/logopedia/images/a/a6/Discovery_Plus_logo_%28stacked%29.png/revision/latest?cb=20201227091030", fanart = "https://www.exchange4media.com/news-photo/105426-image8.jpg", folder = True )    
   
    plugintools.add_item(action = "generos" , title = "[B][LOWERCASE][CAPITALIZE][COLOR white]discovery+ [/CAPITALIZE][/LOWERCASE][/B][/COLOR]",thumbnail ="https://static.wikia.nocookie.net/logopedia/images/a/a6/Discovery_Plus_logo_%28stacked%29.png/revision/latest?cb=20201227091030", fanart = "https://www.exchange4media.com/news-photo/105426-image8.jpg", folder = True )      
 
    plugintools.add_item(action = "plugin.video.discoverypluschopo" , title = "[B][LOWERCASE][CAPITALIZE][COLOR white]puedes instalarlo pinchando [COLOR lime]aqui  [/CAPITALIZE][/LOWERCASE][/B][/COLOR]",thumbnail ="https://static.wikia.nocookie.net/logopedia/images/a/a6/Discovery_Plus_logo_%28stacked%29.png/revision/latest?cb=20201227091030", fanart = "https://www.exchange4media.com/news-photo/105426-image8.jpg",url= "plugin://plugin.video.discoverypluschopo", folder = True )      

    plugintools.add_item(action = "generos" , title = "[B][LOWERCASE][CAPITALIZE][COLOR white]ademas puedes instalarlo desde tvchopo a la carta  [/CAPITALIZE][/LOWERCASE][/B][/COLOR]",thumbnail ="https://static.wikia.nocookie.net/logopedia/images/a/a6/Discovery_Plus_logo_%28stacked%29.png/revision/latest?cb=20201227091030", fanart = "https://www.exchange4media.com/news-photo/105426-image8.jpg", folder = True )      
  
    plugintools.add_item(action = "generos" , title = "[B][LOWERCASE][CAPITALIZE][COLOR white]tambien desde nuestra fuente y desde kelebek [/CAPITALIZE][/LOWERCASE][/B][/COLOR]",thumbnail ="https://static.wikia.nocookie.net/logopedia/images/a/a6/Discovery_Plus_logo_%28stacked%29.png/revision/latest?cb=20201227091030", fanart = "https://www.exchange4media.com/news-photo/105426-image8.jpg", folder = True )      
  
    plugintools.add_item(action = "generos" , title = "[B][LOWERCASE][CAPITALIZE][COLOR white]y como no ya lo teneis en el repositorio [/CAPITALIZE][/LOWERCASE][/B][/COLOR]",thumbnail ="https://static.wikia.nocookie.net/logopedia/images/a/a6/Discovery_Plus_logo_%28stacked%29.png/revision/latest?cb=20201227091030", fanart = "https://www.exchange4media.com/news-photo/105426-image8.jpg", folder = True )      
    
  
   
   
  
       

run()