################################################################################
#      Copyright (C) 2015 Surfacingx                                           #
#                                                                              #
#  This Program is free software; you can redistribute it and/or modify        #
#  it under the terms of the GNU General Public License as published by        #
#  the Free Software Foundation; either version 2, or (at your option)         #
#  any later version.                                                          #
#                                                                              #
#  This Program is distributed in the hope that it will be useful,             #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of              #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the                #
#  GNU General Public License for more details.                                #
#                                                                              #
#  You should have received a copy of the GNU General Public License           #
#  along with XBMC; see the file COPYING.  If not, write to                    #
#  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.       #
#  http://www.gnu.org/copyleft/gpl.html                                        #
################################################################################

import xbmc, xbmcaddon, xbmcgui, xbmcplugin, os, sys, xbmcvfs, glob
import shutil
import urllib2,urllib
import re
import uservar
import fnmatch
try:    from sqlite3 import dbapi2 as database
except: from pysqlite2 import dbapi2 as database
from datetime import date, datetime, timedelta
from urlparse import urljoin
from resources.libs import extract, downloader, notify, debridit, traktit, loginit, skinSwitch, uploadLog, yt, speedtest, wizard as wiz

ADDON_ID         = uservar.ADDON_ID
ADDONTITLE       = uservar.ADDONTITLE
ADDON            = wiz.addonId(ADDON_ID)
VERSION          = wiz.addonInfo(ADDON_ID,'version')
ADDONPATH        = wiz.addonInfo(ADDON_ID, 'path')
DIALOG           = xbmcgui.Dialog()
DP               = xbmcgui.DialogProgress()
HOME             = xbmc.translatePath('special://home/')
LOG              = xbmc.translatePath('special://logpath/')
PROFILE          = xbmc.translatePath('special://profile/')
TEMPDIR          = xbmc.translatePath('special://temp')
ADDONS           = os.path.join(HOME,      'addons')
USERDATA         = os.path.join(HOME,      'userdata')
PLUGIN           = os.path.join(ADDONS,    ADDON_ID)
PACKAGES         = os.path.join(ADDONS,    'packages')
ADDOND           = os.path.join(USERDATA,  'addon_data')
ADDONDATA        = os.path.join(USERDATA,  'addon_data', ADDON_ID)
ADVANCED         = os.path.join(USERDATA,  'advancedsettings.xml')
SOURCES          = os.path.join(USERDATA,  'sources.xml')
FAVOURITES       = os.path.join(USERDATA,  'favourites.xml')
PROFILES         = os.path.join(USERDATA,  'profiles.xml')
GUISETTINGS      = os.path.join(USERDATA,  'guisettings.xml')
THUMBS           = os.path.join(USERDATA,  'Thumbnails')
DATABASE         = os.path.join(USERDATA,  'Database')
MYVIDEOS	     = os.path.join(DATABASE,  'MyVideos116.db')
FANART           = os.path.join(PLUGIN,    'fanart.jpg')
ICON             = os.path.join(PLUGIN,    'icon.png')
ART              = os.path.join(PLUGIN,    'resources', 'art')
WIZLOG           = os.path.join(ADDONDATA, 'wizard.log')
SPEEDTESTFOLD    = os.path.join(ADDONDATA, 'SpeedTest')
ARCHIVE_CACHE    = os.path.join(TEMPDIR,   'archive_cache')
SKIN             = xbmc.getSkinDir()
BUILDNAME        = wiz.getS('buildname')
DEFAULTSKIN      = wiz.getS('defaultskin')
DEFAULTNAME      = wiz.getS('defaultskinname')
DEFAULTIGNORE    = wiz.getS('defaultskinignore')

BUILDTHEME       = wiz.getS('buildtheme')
BUILDLATEST      = wiz.getS('latestversion')
SHOW15           = wiz.getS('show15')
SHOW16           = wiz.getS('show16')
SHOW17           = wiz.getS('show17')
SHOW18           = wiz.getS('show18')
SHOWADULT        = wiz.getS('adult')
SHOWMAINT        = wiz.getS('showmaint')
AUTOCLEANUP      = wiz.getS('autoclean')
AUTOCACHE        = wiz.getS('clearcache')
AUTOPACKAGES     = wiz.getS('clearpackages')
AUTOTHUMBS       = wiz.getS('clearthumbs')
AUTOFEQ          = wiz.getS('autocleanfeq')
AUTONEXTRUN      = wiz.getS('nextautocleanup')
INCLUDEVIDEO     = wiz.getS('includevideo')
INCLUDEALL       = wiz.getS('includeall')
INCLUDEPLACENTA    = wiz.getS('includeplacenta')
INCLUDEEXODUSREDUX    = wiz.getS('includeexodusredux')
INCLUDE13CLOWNS = wiz.getS('include13clowns')
INCLUDEZANNI = wiz.getS('includezanni')
INCLUDEGAIA     = wiz.getS('includegaia')
INCLUDESEREN     = wiz.getS('includeseren')
INCLUDEMAGICALITY   = wiz.getS('includemagicality')
SEPERATE         = wiz.getS('seperate')
NOTIFY           = wiz.getS('notify')
NOTEID           = wiz.getS('noteid')
NOTEDISMISS      = wiz.getS('notedismiss')
TRAKTSAVE        = wiz.getS('traktlastsave')
REALSAVE         = wiz.getS('debridlastsave')
LOGINSAVE        = wiz.getS('loginlastsave')
KEEPMYVIDEOS     = wiz.getS('keepmyvideos')
KEEPFAVS         = wiz.getS('keepfavourites')
KEEPSOURCES      = wiz.getS('keepsources')
KEEPPROFILES     = wiz.getS('keepprofiles')
KEEPADVANCED     = wiz.getS('keepadvanced')
KEEPREPOS        = wiz.getS('keeprepos')
KEEPSUPER        = wiz.getS('keepsuper')
KEEPWHITELIST    = wiz.getS('keepwhitelist')
KEEPTRAKT        = wiz.getS('keeptrakt')
KEEPREAL         = wiz.getS('keepdebrid')
KEEPLOGIN        = wiz.getS('keeplogin')
DEVELOPER        = wiz.getS('developer')
THIRDPARTY       = wiz.getS('enable3rd')
THIRD1NAME       = wiz.getS('wizard1name')
THIRD1URL        = wiz.getS('wizard1url')
THIRD2NAME       = wiz.getS('wizard2name')
THIRD2URL        = wiz.getS('wizard2url')
THIRD3NAME       = wiz.getS('wizard3name')
THIRD3URL        = wiz.getS('wizard3url')
BACKUPLOCATION   = ADDON.getSetting('path') if not ADDON.getSetting('path') == '' else 'special://home/'
BACKUPROMS       = wiz.getS('rompath')
MYBUILDS         = os.path.join(BACKUPLOCATION, 'MisBuilds', '')
AUTOFEQ          = int(float(AUTOFEQ)) if AUTOFEQ.isdigit() else 0
TODAY            = date.today()
TOMORROW         = TODAY + timedelta(days=1)
THREEDAYS        = TODAY + timedelta(days=3)

KODIV            = float(xbmc.getInfoLabel("System.BuildVersion")[:4])
if KODIV > 17:
	from resources.libs import zfile as zipfile
else:
	import zipfile

MCNAME           = wiz.mediaCenter()
EXCLUDES         = uservar.EXCLUDES
CACHETEXT        = uservar.CACHETEXT
CACHEAGE         = uservar.CACHEAGE if str(uservar.CACHEAGE).isdigit() else 30
BUILDFILE        = uservar.BUILDFILE
APKFILE          = uservar.APKFILE
YOUTUBETITLE     = uservar.YOUTUBETITLE
YOUTUBEFILE      = uservar.YOUTUBEFILE
ADDONFILE        = uservar.ADDONFILE
ADVANCEDFILE     = uservar.ADVANCEDFILE
UPDATECHECK      = uservar.UPDATECHECK if str(uservar.UPDATECHECK).isdigit() else 1
NEXTCHECK        = TODAY + timedelta(days=UPDATECHECK)
NOTIFICATION     = uservar.NOTIFICATION
ENABLE           = uservar.ENABLE
HEADERMESSAGE    = uservar.HEADERMESSAGE
AUTOUPDATE       = uservar.AUTOUPDATE
BUILDERNAME      = uservar.BUILDERNAME
WIZARDFILE       = uservar.WIZARDFILE
HIDECONTACT      = uservar.HIDECONTACT
CONTACT          = uservar.CONTACT
CONTACTICON      = uservar.CONTACTICON if not uservar.CONTACTICON == 'http://' else ICON
CONTACTFANART    = uservar.CONTACTFANART if not uservar.CONTACTFANART == 'http://' else FANART
HIDESPACERS      = uservar.HIDESPACERS
COLOR1           = uservar.COLOR1
COLOR2           = uservar.COLOR2
THEME1           = uservar.THEME1
THEME2           = uservar.THEME2
THEME3           = uservar.THEME3
THEME4           = uservar.THEME4
THEME5           = uservar.THEME5
THEME6           = uservar.THEME6
ICONBUILDS       = uservar.ICONBUILDS if not uservar.ICONBUILDS == 'http://' else ICON
ICONMAINT        = uservar.ICONMAINT if not uservar.ICONMAINT == 'http://' else ICON
ICONAPK          = uservar.ICONAPK if not uservar.ICONAPK == 'http://' else ICON
ICONADDONS       = uservar.ICONADDONS if not uservar.ICONADDONS == 'http://' else ICON
ICONYOUTUBE      = uservar.ICONYOUTUBE if not uservar.ICONYOUTUBE == 'http://' else ICON
ICONSAVE         = uservar.ICONSAVE if not uservar.ICONSAVE == 'http://' else ICON
ICONTRAKT        = uservar.ICONTRAKT if not uservar.ICONTRAKT == 'http://' else ICON
ICONREAL         = uservar.ICONREAL if not uservar.ICONREAL == 'http://' else ICON
ICONLOGIN        = uservar.ICONLOGIN if not uservar.ICONLOGIN == 'http://' else ICON
ICONCONTACT      = uservar.ICONCONTACT if not uservar.ICONCONTACT == 'http://' else ICON
ICONSETTINGS     = uservar.ICONSETTINGS if not uservar.ICONSETTINGS == 'http://' else ICON
LOGFILES         = wiz.LOGFILES
TRAKTID          = traktit.TRAKTID
DEBRIDID         = debridit.DEBRIDID
LOGINID          = loginit.LOGINID
MODURL           = 'http://tribeca.tvaddons.ag/tools/maintenance/modules/'
MODURL2          = 'http://mirrors.kodi.tv/addons/jarvis/'
INSTALLMETHODS   = ['Always Ask', 'Reload Profile', 'Force Close']
DEFAULTPLUGINS   = ['metadata.album.universal', 'metadata.artists.universal', 'metadata.common.fanart.tv', 'metadata.common.imdb.com', 'metadata.common.musicbrainz.org', 'metadata.themoviedb.org', 'metadata.tvdb.com', 'service.xbmc.versioncheck']
try:
    INSTALLMETHOD    = int(float(wiz.getS('installmethod')))
except:
    INSTALLMETHOD    = 0

###########################
###### Menu Items   #######
###########################
#addDir (display,mode,name=None,url=None,menu=None,overwrite=True,fanart=FANART,icon=ICON, themeit=None)
#addFile(display,mode,name=None,url=None,menu=None,overwrite=True,fanart=FANART,icon=ICON, themeit=None)

def index():
	if AUTOUPDATE == 'Yes':
		if wiz.workingURL(WIZARDFILE) == True:
			ver = wiz.checkWizard('version')
			if ver > VERSION: addFile('[COLOR lime]%s [v%s] [B][ACTUALIZACION v%s][/COLOR]' % (ADDONTITLE, VERSION, ver), 'wizardupdate', themeit=THEME2)
			else: addFile('[COLOR lime]%s [v%s][/COLOR]' % (ADDONTITLE, VERSION), '', themeit=THEME2)
		else: addFile('[COLOR lime]%s v%s[/COLOR]' % (ADDONTITLE, VERSION), '', themeit=THEME2)
	else: addFile('[COLOR lime]%s v%s[/COLOR]' % (ADDONTITLE, VERSION), '', themeit=THEME2)

	if HIDESPACERS == 'No': addFile(wiz.sep(), '', themeit=THEME3)
	addDir ('Mantenimiento'   ,'maint',    icon=ICONMAINT,    themeit=THEME1)
	if not ADDONFILE == 'http://': addDir ('Instalador de dependencias para tvchopo' ,'addons', icon=ICONADDONS, themeit=THEME1)
	if HIDESPACERS == 'No': addFile(wiz.sep(), '', themeit=THEME3)
	
	if DEVELOPER == 'true': addDir('Developer Menu','developer', icon=ICONSETTINGS, themeit=THEME1)
	setView('files', 'viewType')


def addonMenu(name=None, url=None):
    if not ADDONFILE == 'http://':
        if url == None:
            TEMPADDONFILE = wiz.textCache(uservar.ADDONFILE)
            if TEMPADDONFILE == False: ADDONWORKING  = wiz.workingURL(uservar.ADDONFILE)
        else:
            TEMPADDONFILE = wiz.textCache(url)
            if TEMPADDONFILE == False: ADDONWORKING  = wiz.workingURL(url)
        if not TEMPADDONFILE == False:
            link = TEMPADDONFILE.replace('\n','').replace('\r','').replace('\t','').replace('repository=""', 'repository="none"').replace('repositoryurl=""', 'repositoryurl="http://"').replace('repositoryxml=""', 'repositoryxml="http://"')
            match = re.compile('name="(.+?)".+?lugin="(.+?)".+?rl="(.+?)".+?epository="(.+?)".+?epositoryxml="(.+?)".+?epositoryurl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?dult="(.+?)".+?escription="(.+?)"').findall(link)
            if len(match) > 0:
                x = 0
                for aname, plugin, aurl, repository, repositoryxml, repositoryurl, icon, fanart, adult, description in match:
                    if plugin.lower() == 'section':
                        x += 1
                        addDir ("%s" % aname, 'addons', aname, aurl, description=description, icon=icon, fanart=fanart, themeit=THEME3)
                    elif plugin.lower() == 'skin':
                        if not SHOWADULT == 'true' and adult.lower() == 'yes': continue
                        x += 1
                        addFile("%s" % aname, 'skinpack', aname, aurl, description=description, icon=icon, fanart=fanart, themeit=THEME2)
                    elif plugin.lower() == 'pack':
                        if not SHOWADULT == 'true' and adult.lower() == 'yes': continue
                        x += 1
                        addFile("%s" % aname, 'addonpack', aname, aurl, description=description, icon=icon, fanart=fanart, themeit=THEME2)
                    else:
                        if not SHOWADULT == 'true' and adult.lower() == 'yes': continue
                        try:
                            add    = xbmcaddon.Addon(id=plugin).getAddonInfo('path')
                            if os.path.exists(add):
                                aname   = "[CAPITALIZE] %s [/CAPITALIZE][COLOR white]  [COLOR lime][CAPITALIZE]ya esta Instalado[/CAPITALIZE][/COLOR]" % aname
                        except:
                            pass
                        x += 1
                        addFile(aname, 'addoninstall', plugin, url, description=description, icon=icon, fanart=fanart, themeit=THEME2)
                    if x < 1:
                        addFile("No addons added to this menu yet!", '', themeit=THEME2)
            else:
                addFile('Text File not formated correctly!', '', themeit=THEME3)
                wiz.log("[Addon Menu] ERROR: Invalid Format.")
        else:
            wiz.log("[Addon Menu] ERROR: URL for Addon list not working.")
            addFile('Url for txt file not valid', '', themeit=THEME3)
            addFile('%s' % ADDONWORKING, '', themeit=THEME3)
    else: wiz.log("[Addon Menu] No Addon list added.")
    setView('files', 'viewType')

def packInstaller(name, url):
    if not wiz.workingURL(url) == True: wiz.LogNotify("[COLOR %s]Instalador de Addons[/COLOR]" % COLOR1, '[COLOR %s]%s:[/COLOR] [COLOR %s]Zip Url Invalida[/COLOR]' % (COLOR1, name, COLOR2)); return
    if not os.path.exists(PACKAGES): os.makedirs(PACKAGES)
    DP.create(ADDONTITLE,'[COLOR %s]Descargando:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR2, COLOR1, name), '', '[COLOR %s]Espera[/COLOR]' % COLOR2)
    urlsplits = url.split('/')
    lib = xbmc.makeLegalFilename(os.path.join(PACKAGES, urlsplits[-1]))
    try: os.remove(lib)
    except: pass
    downloader.download(url, lib, DP)
    title = '[COLOR %s]Instalando:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR2, COLOR1, name)
    DP.update(0, title,'', '[COLOR %s]Espera[/COLOR]' % COLOR2)
    percent, errors, error = extract.all(lib,ADDONS,DP, title=title)
    installed = grabAddons(lib)
    if KODIV >= 17: wiz.addonDatabase(installed, 1, True)
    DP.close()
    wiz.LogNotify("[COLOR %s]Instalador de Addons[/COLOR]" % COLOR1, '[COLOR %s]%s: Instalado![/COLOR]' % (COLOR2, name))
    wiz.ebi('UpdateAddonRepos()')
    wiz.ebi('UpdateLocalAddons()')
    wiz.refresh()



def addonInstaller(plugin, url):
    if not ADDONFILE == 'http://':
        if url == None: url = ADDONFILE
        ADDONWORKING = wiz.workingURL(url)
        if ADDONWORKING == True:
            link = wiz.textCache(url).replace('\n','').replace('\r','').replace('\t','').replace('repository=""', 'repository="none"').replace('repositoryurl=""', 'repositoryurl="http://"').replace('repositoryxml=""', 'repositoryxml="http://"')
            match = re.compile('name="(.+?)".+?lugin="%s".+?rl="(.+?)".+?epository="(.+?)".+?epositoryxml="(.+?)".+?epositoryurl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?dult="(.+?)".+?escription="(.+?)"' % plugin).findall(link)
            if len(match) > 0:
                for name, url, repository, repositoryxml, repositoryurl, icon, fanart, adult, description in match:
                    if os.path.exists(os.path.join(ADDONS, plugin)):
                        do        = ['[COLOR lime][B]Abrir Addon[/B][/COLOR]', '[COLOR red][B]Borrar Addon[/B][/COLOR]']
                        selected = DIALOG.select("[COLOR %s][COLOR yellow][B]Addon ya instalado, que quieres hacer?[/B][/COLOR]" % COLOR2, do)
                        if selected == 0:
                            wiz.ebi('RunAddon(%s)' % plugin)
                            xbmc.sleep(500)
                            return True
                        elif selected == 1:
                            wiz.cleanHouse(os.path.join(ADDONS, plugin))
                            try: wiz.removeFolder(os.path.join(ADDONS, plugin))
                            except: pass
                            if DIALOG.yesno(ADDONTITLE, "[COLOR %s]Quieres borrar la carpeta addon_data de:" % COLOR2, "[COLOR %s]%s[/COLOR]?[/COLOR]" % (COLOR1, plugin), yeslabel="[COLOR springgreen]Borrar[/COLOR]", nolabel="[COLOR red]Saltar[/COLOR]"):
                                removeAddonData(plugin)
                            wiz.refresh()
                            return True
                        else:
                            return False
                    repo = os.path.join(ADDONS, repository)
                    if not repository.lower() == 'none' and not os.path.exists(repo):
                        wiz.log("Repository not installed, installing it")
                        if DIALOG.yesno(ADDONTITLE, "[COLOR %s]Would you like to install the repository for [COLOR %s]%s[/COLOR]:" % (COLOR2, COLOR1, plugin), "[COLOR %s]%s[/COLOR]?[/COLOR]" % (COLOR1, repository), yeslabel="[COLOR springgreen]Yes Install[/COLOR]", nolabel="[COLOR red]No Skip[/COLOR]"):
                            ver = wiz.parseDOM(wiz.openURL(repositoryxml), 'addon', ret='version', attrs = {'id': repository})
                            if len(ver) > 0:
                                repozip = '%s%s-%s.zip' % (repositoryurl, repository, ver[0])
                                wiz.log(repozip)
                                if KODIV >= 17: wiz.addonDatabase(repository, 1)
                                installAddon(repository, repozip)
                                wiz.ebi('UpdateAddonRepos()')
                                #wiz.ebi('UpdateLocalAddons()')
                                wiz.log("Installing Addon from Kodi")
                                install = installFromKodi(plugin)
                                wiz.log("Install from Kodi: %s" % install)
                                if install:
                                    wiz.refresh()
                                    return True
                            else:
                                wiz.log("[Addon Installer] Repository not installed: Unable to grab url! (%s)" % repository)
                        else: wiz.log("[Addon Installer] Repository for %s not installed: %s" % (plugin, repository))
                    elif repository.lower() == 'none':
                        wiz.log("No repository, installing addon")
                        pluginid = plugin
                        zipurl = url
                        installAddon(plugin, url)
                        wiz.refresh()
                        return True
                    else:
                        wiz.log("Repository installed, installing addon")
                        install = installFromKodi(plugin, False)
                        if install:
                            wiz.refresh()
                            return True
                    if os.path.exists(os.path.join(ADDONS, plugin)): return True
                    ver2 = wiz.parseDOM(wiz.openURL(repositoryxml), 'addon', ret='version', attrs = {'id': plugin})
                    if len(ver2) > 0:
                        url = "%s%s-%s.zip" % (url, plugin, ver2[0])
                        wiz.log(str(url))
                        if KODIV >= 17: wiz.addonDatabase(plugin, 1)
                        installAddon(plugin, url)
                        wiz.refresh()
                    else:
                        wiz.log("no match"); return False
            else: wiz.log("[Addon Installer] Invalid Format")
        else: wiz.log("[Addon Installer] Text File: %s" % ADDONWORKING)
    else: wiz.log("[Addon Installer] Not Enabled.")

def installFromKodi(plugin, over=True):
    if over == True:
        xbmc.sleep(2000)
    #wiz.ebi('InstallAddon(%s)' % plugin)
    wiz.ebi('RunPlugin(plugin://%s)' % plugin)
    if not wiz.whileWindow('yesnodialog'):
        return False
    xbmc.sleep(500)
    if wiz.whileWindow('okdialog'):
        return False
    wiz.whileWindow('progressdialog')
    if os.path.exists(os.path.join(ADDONS, plugin)): return True
    else: return False

def installAddon(name, url):
    if not wiz.workingURL(url) == True: wiz.LogNotify("[COLOR %s]Instalador de Addons[/COLOR]" % COLOR1, '[COLOR %s]%s:[/COLOR] [COLOR %s]Url del Zip Invalida[/COLOR]' % (COLOR1, name, COLOR2)); return
    if not os.path.exists(PACKAGES): os.makedirs(PACKAGES)
    DP.create(ADDONTITLE,'[COLOR %s]Descargando:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR2, COLOR1, name), '', '[COLOR %s]Espera[/COLOR]' % COLOR2)
    urlsplits = url.split('/')
    lib=os.path.join(PACKAGES, urlsplits[-1])
    try: os.remove(lib)
    except: pass
    downloader.download(url, lib, DP)
    title = '[COLOR %s]Instalando:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR2, COLOR1, name)
    DP.update(0, title,'', '[COLOR %s]Espera[/COLOR]' % COLOR2)
    percent, errors, error = extract.all(lib,ADDONS,DP, title=title)
    DP.update(0, title,'', '[COLOR %s]Instalando Dependencias[/COLOR]' % COLOR2)
    installed(name)
    installlist = grabAddons(lib)
    wiz.log(str(installlist))
    if KODIV >= 17: wiz.addonDatabase(installlist, 1, True)
    installDep(name, DP)
    DP.close()
    wiz.ebi('UpdateAddonRepos()')
    wiz.ebi('UpdateLocalAddons()')
    wiz.refresh()
    for item in installlist:
        if item.startswith('skin.') == True and not item == 'skin.shortcuts':
            if not BUILDNAME == '' and DEFAULTIGNORE == 'true': wiz.setS('defaultskinignore', 'true')
            wiz.swapSkins(item, 'Skin Installer')

def installDep(name, DP=None):
    dep=os.path.join(ADDONS,name,'addon.xml')
    if os.path.exists(dep):
        source = open(dep,mode='r'); link = source.read(); source.close();
        match  = wiz.parseDOM(link, 'import', ret='addon')
        for depends in match:
            if not 'xbmc.python' in depends:
                if not DP == None:
                    DP.update(0, '', '[COLOR %s]%s[/COLOR]' % (COLOR1, depends))
                try:
                    add   = xbmcaddon.Addon(id=depends)
                    name2 = add.getAddonInfo('name')
                except:
                    wiz.createTemp(depends)
                    if KODIV >= 17: wiz.addonDatabase(depends, 1)
                # continue
                # dependspath=os.path.join(ADDONS, depends)
                # if not os.path.exists(dependspath):
                    # zipname = '%s-%s.zip' % (depends, match2[match.index(depends)])
                    # depzip = urljoin("%s%s/" % (MODURL2, depends), zipname)
                    # if not wiz.workingURL(depzip) == True:
                        # depzip = urljoin(MODURL, '%s.zip' % depends)
                        # if not wiz.workingURL(depzip) == True:
                            # wiz.createTemp(depends)
                            # if KODIV >= 17: wiz.addonDatabase(depends, 1)
                            # continue
                    # lib=os.path.join(PACKAGES, '%s.zip' % depends)
                    # try: os.remove(lib)
                    # except: pass
                    # DP.update(0, '[COLOR %s]Downloading Dependency:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR2, COLOR1, depends),'', 'Please Wait')
                    # downloader.download(depzip, lib, DP)
                    # xbmc.sleep(100)
                    # title = '[COLOR %s]Installing Dependency:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR2, COLOR1, depends)
                    # DP.update(0, title,'', 'Please Wait')
                    # percent, errors, error = extract.all(lib,ADDONS,DP, title=title)
                    # if KODIV >= 17: wiz.addonDatabase(depends, 1)
                    # installed(depends)
                    # installDep(depends)
                    # xbmc.sleep(100)
                    # DP.close()

def installed(addon):
    url = os.path.join(ADDONS,addon,'addon.xml')
    if os.path.exists(url):
        try:
            list  = open(url,mode='r'); g = list.read(); list.close()
            name = wiz.parseDOM(g, 'addon', ret='name', attrs = {'id': addon})
            icon  = os.path.join(ADDONS,addon,'icon.png')
            wiz.LogNotify('[COLOR %s]%s[/COLOR]' % (COLOR1, name[0]), '[COLOR %s]Addon Enabled[/COLOR]' % COLOR2, '2000', icon)
        except: pass



def maintMenu(view=None):
    on = '[COLOR springgreen]ON[/COLOR]'; off = '[COLOR red]OFF[/COLOR]'
    autoclean   = 'true' if AUTOCLEANUP    == 'true' else 'false'
    cache       = 'true' if AUTOCACHE      == 'true' else 'false'
    packages    = 'true' if AUTOPACKAGES   == 'true' else 'false'
    thumbs      = 'true' if AUTOTHUMBS     == 'true' else 'false'
    maint       = 'true' if SHOWMAINT      == 'true' else 'false'
    thirdparty  = 'true' if THIRDPARTY     == 'true' else 'false'
    errors = int(errorChecking(count=True))
    errorsfound = str(errors) + ' Errore(s) Encontrados' if errors > 0 else 'No hay'
    wizlogsize = ': [COLOR red]No hay[/COLOR]' if not os.path.exists(WIZLOG) else ": [COLOR springgreen]%s[/COLOR]" % wiz.convertSize(os.path.getsize(WIZLOG))
    sizepack   = wiz.getSize(PACKAGES)
    sizethumb  = wiz.getSize(THUMBS)
    archive    = wiz.getSize(ARCHIVE_CACHE)
    sizecache  = (wiz.getCacheSize())-archive
    totalsize  = sizepack+sizethumb+sizecache
    feq        = ['Siempre', 'Cada dia', 'Cada 3 dias', 'Semanalmente']
    addDir ('Herramientas de Addons',       'maint', 'addon',  icon='https://i.imgur.com/IRGSjgD.jpg', themeit=THEME1)
    if view == "addon" or SHOWMAINT == 'true':
        addFile('Borrar Addons',                  'removeaddons',    icon=ICONMAINT, themeit=THEME3)
        addDir ('Borrar Addon_data',              'removeaddondata', icon=ICONMAINT, themeit=THEME3)
        addDir ('Activar/Desactivar Addons',          'enableaddons',    icon=ICONMAINT, themeit=THEME3)
        addFile('Activar/Desactivar Addons porno',    'toggleadult',     icon=ICONMAINT, themeit=THEME3)
        addFile('Forzar Actualizacion de Addons',            'forceupdate',     icon=ICONMAINT, themeit=THEME3)
    addDir ('Otras Herramientas'     ,'maint', 'misc',   icon='https://i.imgur.com/gQmN80S.jpg', themeit=THEME1)
    if view == "misc" or SHOWMAINT == 'true':
        addDir ('Test de Velocidad',                     'speedtest',       icon=ICONMAINT, themeit=THEME3)
        addFile('Escanear Repositorios rotos',   'checkrepos',      icon=ICONMAINT, themeit=THEME3)
        addFile('Recargar skin',                    'forceskin',       icon=ICONMAINT, themeit=THEME3)
        addFile('Recargar Perfil',                 'forceprofile',    icon=ICONMAINT, themeit=THEME3)
        addFile('Forzar cierre de Kodi',               'forceclose',      icon=ICONMAINT, themeit=THEME3)
        addFile('Ver errores en el log: %s' % (errorsfound), 'viewerrorlog', icon=ICONMAINT, themeit=THEME3)
        if errors > 0: addFile('View Last Error In Log', 'viewerrorlast', icon=ICONMAINT, themeit=THEME3)
        addFile('Ver el Log',                  'viewlog',         icon=ICONMAINT, themeit=THEME3)
        addFile('Ver el Log del wizard',           'viewwizlog',      icon=ICONMAINT, themeit=THEME3)
        addFile('Limpiar Log%s del wizard' % wizlogsize,'clearwizlog',     icon=ICONMAINT, themeit=THEME3)
    addDir ('Copias de Seguridad'     ,'maint', 'backup',   icon='https://i.imgur.com/7D99ZYk.jpg', themeit=THEME1)
    if view == "backup" or SHOWMAINT == 'true':
        addFile('Limpiar carpeta de copias de seguridad',        'clearbackup',     icon=ICONMAINT,   themeit=THEME3)
        addFile('Ubicacion de las copias: [COLOR %s]%s[/COLOR]' % (COLOR2, MYBUILDS),'settings', 'Maintenance', icon=ICONMAINT, themeit=THEME3)
        #addFile('Extract a ZipFile',              'extractazip',     icon=ICONMAINT,   themeit=THEME3)
        addFile('[Copia]: Build (Copia completa)',               'backupbuild',     icon=ICONMAINT,   themeit=THEME3)
        addFile('[Copia]: Skin y Menu',               'backuptheme',     icon=ICONMAINT,   themeit=THEME3)
        addFile('[Copia]: Addons',          'backupaddonpack', icon=ICONMAINT,   themeit=THEME3)
        addFile('[Copia]: Addon_data',          'backupaddon',     icon=ICONMAINT,   themeit=THEME3)
        addFile('[Restaurar]: Build Local',         'restorezip',      icon=ICONMAINT,   themeit=THEME3)
        addFile('[Restaurar]: Ajustes Kodi (guisettings)',         'restoregui',      icon=ICONMAINT,   themeit=THEME3)
        addFile('[Restaurar]: Addon_data Local',    'restoreaddon',    icon=ICONMAINT,   themeit=THEME3)
        addFile('[Restaurar]: Build Externa',      'restoreextzip',   icon=ICONMAINT,   themeit=THEME3)
        addFile('[Restaurar]: Skin y Menus',     'restoretheme',   icon=ICONMAINT,   themeit=THEME3)
    
    if view == "tweaks" or SHOWMAINT == 'true':
        if not ADVANCEDFILE == 'http://' and not ADVANCEDFILE == '':
            addDir ('Advanced Settings',            'advancedsetting',  icon=ICONMAINT, themeit=THEME3)
        else:
            if os.path.exists(ADVANCED):
				addFile('Ver actual AdvancedSettings.xml',   'currentsettings', icon=ICONMAINT, themeit=THEME3)
				addFile('Borrar actual AdvancedSettings.xml', 'removeadvanced',  icon=ICONMAINT, themeit=THEME3)
            addFile('Configuracion rapida de AdvancedSettings.xml',    'autoadvanced',    icon=ICONMAINT, themeit=THEME3)
	addFile('Auto Limpieza al Inicio: %s' % autoclean.replace('true',on).replace('false',off) ,'togglesetting', 'autoclean',   icon=ICONMAINT, themeit=THEME3)
	
	addDir ('[I]<< Volver al Menu Principal DEL INSTALADOR CHOPO[/I]', icon=ICONMAINT, themeit=THEME2)	    

#########################################NET TOOLS#############################################
def net_tools(view=None):
    if HIDESPACERS == 'No': addFile(wiz.sep(), '', themeit=THEME3)
    addDir ('Test de Velocidad de Internet' ,'speedtestM', icon=ICONAPK, themeit=THEME1)
    
    addDir ('Ver direccion IP y MAC',        'viewIP',    icon=ICONMAINT, themeit=THEME1)
    setView('files', 'viewType')
    if HIDESPACERS == 'No': addFile(wiz.sep(), '', themeit=THEME3)

def viewIP():
    mac,inter_ip,ip,city,state,country,isp = wiz.net_info()
    addFile('[COLOR %s]Mac:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR1, COLOR2, mac), '', icon=ICONMAINT, themeit=THEME2)
    addFile('[COLOR %s]IP Interna: [COLOR %s]%s[/COLOR]' % (COLOR1, COLOR2, inter_ip), '', icon=ICONMAINT, themeit=THEME2)
    addFile('[COLOR %s]IP Externa:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR1, COLOR2, ip), '', icon=ICONMAINT, themeit=THEME2)
    addFile('[COLOR %s]Ciudad:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR1, COLOR2, city), '', icon=ICONMAINT, themeit=THEME2)
    addFile('[COLOR %s]Autonomia/Estado:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR1, COLOR2, state), '', icon=ICONMAINT, themeit=THEME2)
    addFile('[COLOR %s]Pais:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR1, COLOR2, country), '', icon=ICONMAINT, themeit=THEME2)
    addFile('[COLOR %s]ISP:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR1, COLOR2, isp), '', icon=ICONMAINT, themeit=THEME2)
    setView('files', 'viewType')

def speedTest():
    if HIDESPACERS == 'No': addFile(wiz.sep(), '', themeit=THEME3)
    addFile('[COLOR white]Empezar test de velocidad[/COLOR]',             'runspeedtest',      icon=ICONMAINT, themeit=THEME3)
    
    if os.path.exists(SPEEDTESTFOLD):
        speedimg = glob.glob(os.path.join(SPEEDTESTFOLD, '*.png'))
        speedimg.sort(key=lambda f: os.path.getmtime(f), reverse=True)
        if len(speedimg) > 0:
            addFile('[COLOR white]Limpiar Resultados[/COLOR]',          'clearspeedtest',    icon=ICONMAINT, themeit=THEME3)
            addFile(wiz.sep('[COLOR white]Test Anteriores[/COLOR]'), '', icon=ICONMAINT, themeit=THEME3)
            for item in speedimg:
                created = datetime.fromtimestamp(os.path.getmtime(item)).strftime('%m/%d/%Y %H:%M:%S')
                img = item.replace(os.path.join(SPEEDTESTFOLD, ''), '')
                addFile('%s: [I]Realizado el %s[/I]' % (img, created), 'viewspeedtest', img, icon=ICONMAINT, themeit=THEME3)
        if HIDESPACERS == 'No': addFile(wiz.sep(), '', themeit=THEME3)

def clearSpeedTest():
    speedimg = glob.glob(os.path.join(SPEEDTESTFOLD, '*.png'))
    for file in speedimg:
        wiz.removeFile(file)

def viewSpeedTest(img=None):
    img = os.path.join(SPEEDTESTFOLD, img)
    notify.speedTest(img)

def runSpeedTest():
    try:
        found = speedtest.speedtest()
        if not os.path.exists(SPEEDTESTFOLD): os.makedirs(SPEEDTESTFOLD)
        urlsplits = found[0].split('/')
        dest = os.path.join(SPEEDTESTFOLD, urlsplits[-1])
        urllib.urlretrieve(found[0], dest)
        viewSpeedTest(urlsplits[-1])
    except:
        wiz.log("[Speed Test] Error Running Speed Test")
        pass

def advancedWindow(url=None):
    if not ADVANCEDFILE == 'http://':
        if url == None:
            TEMPADVANCEDFILE = wiz.textCache(uservar.ADVANCEDFILE)
            if TEMPADVANCEDFILE == False: ADVANCEDWORKING  = wiz.workingURL(uservar.ADVANCEDFILE)
        else:
            TEMPADVANCEDFILE = wiz.textCache(url)
            if TEMPADVANCEDFILE == False: ADVANCEDWORKING  = wiz.workingURL(url)
        addFile('Click Configuracion rapida de AdvancedSettings.xml', 'autoadvanced', icon=ICONMAINT, themeit=THEME3)
	addFile('Forzar Cierre de Kodi',               'forceclose',      icon=ICONMAINT, themeit=THEME3)		
		
        if os.path.exists(ADVANCED):
            addFile('Ver el AdvancedSettings.xml instalado', 'currentsettings', icon=ICONMAINT, themeit=THEME3)
            addFile('Borrar el AdvancedSettings.xml instalado', 'removeadvanced',  icon=ICONMAINT, themeit=THEME3)
        if not TEMPADVANCEDFILE == False:
            if HIDESPACERS == 'No': addFile(wiz.sep(), '', icon=ICONMAINT, themeit=THEME3)
            link = TEMPADVANCEDFILE.replace('\n','').replace('\r','').replace('\t','')
            match = re.compile('name="(.+?)".+?ection="(.+?)".+?rl="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
            if len(match) > 0:
                for name, section, url, icon, fanart, description in match:
                    if section.lower() == "yes":
                        addDir ("%s" % name, 'advancedsetting', url, description=description, icon=icon, fanart=fanart, themeit=THEME3)
                    else:
                        addFile(name, 'writeadvanced', name, url, description=description, icon=icon, fanart=fanart, themeit=THEME2)
            else: wiz.log("[Advanced Settings] ERROR: Invalid Format.")
        else: wiz.log("[Advanced Settings] URL not working: %s" % ADVANCEDWORKING)
    else: wiz.log("[Advanced Settings] not Enabled")

def writeAdvanced(name, url):
    ADVANCEDWORKING = wiz.workingURL(url)
    if ADVANCEDWORKING == True:
        if os.path.exists(ADVANCED): choice = DIALOG.yesno(ADDONTITLE, "[COLOR %s]Quieres sobreescribir el actual Buffer con [COLOR %s]%s[/COLOR]?[/COLOR]" % (COLOR2, COLOR1, name), yeslabel="[COLOR springgreen]Si[/COLOR]", nolabel="[COLOR red]No[/COLOR]")
        else: choice = DIALOG.yesno(ADDONTITLE, "[COLOR %s]Quieres descargarlo e instalarlo[COLOR %s]%s[/COLOR]?[/COLOR]" % (COLOR2, COLOR1, name), yeslabel="[COLOR springgreen]Instalar[/COLOR]", nolabel="[COLOR red]Cancelar[/COLOR]")

        if choice == 1:
            file = wiz.openURL(url)
            f = open(ADVANCED, 'w');
            f.write(file)
            f.close()
            DIALOG.ok(ADDONTITLE, '[COLOR %s]El archivo AdvancedSettings.xml ha sido creado. Al pulsar OK, Kodi se cerrara para aplicar los cambios.[/COLOR]' % COLOR2)
            wiz.killxbmc(True)
        else: wiz.log("[Advanced Settings] install canceled"); wiz.LogNotify('[COLOR %s]%s[/COLOR]' % (COLOR1, ADDONTITLE), "[COLOR %s]Write Cancelled![/COLOR]" % COLOR2); return
    else: wiz.log("[Advanced Settings] URL not working: %s" % ADVANCEDWORKING); wiz.LogNotify('[COLOR %s]%s[/COLOR]' % (COLOR1, ADDONTITLE), "[COLOR %s]URL Not Working[/COLOR]" % COLOR2)

def viewAdvanced():
    f = open(ADVANCED)
    a = f.read().replace('\t', '    ')
    wiz.TextBox(ADDONTITLE, a)
    f.close()

def removeAdvanced():
    if os.path.exists(ADVANCED):
        wiz.removeFile(ADVANCED)
    else: LogNotify("[COLOR %s]%s[/COLOR]" % (COLOR1, ADDONTITLE), "[COLOR %s]AdvancedSettings.xml not found[/COLOR]")

def showAutoAdvanced():
    notify.autoConfig()

def getIP():
    site  = 'http://whatismyipaddress.com/'
    if not wiz.workingURL(site): return 'Unknown', 'Unknown', 'Unknown'
    page  = wiz.openURL(site).replace('\n','').replace('\r','')
    if not 'Access Denied' in page:
        ipmatch   = re.compile('whatismyipaddress.com/ip/(.+?)"').findall(page)
        ipfinal   = ipmatch[0] if (len(ipmatch) > 0) else 'Unknown'
        details   = re.compile('"font-size:14px;">(.+?)</td>').findall(page)
        provider  = details[0] if (len(details) > 0) else 'Unknown'
        location  = details[1]+', '+details[2]+', '+details[3] if (len(details) > 2) else 'Unknown'
        return ipfinal, provider, location
    else: return 'Unknown', 'Unknown', 'Unknown'

def systemInfo():
    infoLabel = ['System.FriendlyName',
                 'System.BuildVersion',
                 'System.CpuUsage',
                 'System.ScreenMode',
                 'Network.IPAddress',
                 'Network.MacAddress',
                 'System.Uptime',
                 'System.TotalUptime',
                 'System.FreeSpace',
                 'System.UsedSpace',
                 'System.TotalSpace',
                 'System.Memory(free)',
                 'System.Memory(used)',
                 'System.Memory(total)']
    data      = []; x = 0
    for info in infoLabel:
        temp = wiz.getInfo(info)
        y = 0
        while temp == "Busy" and y < 10:
            temp = wiz.getInfo(info); y += 1; wiz.log("%s sleep %s" % (info, str(y))); xbmc.sleep(200)
        data.append(temp)
        x += 1
    storage_free  = data[8] if 'Una' in data[8] else wiz.convertSize(int(float(data[8][:-8]))*1024*1024)
    storage_used  = data[9] if 'Una' in data[9] else wiz.convertSize(int(float(data[9][:-8]))*1024*1024)
    storage_total = data[10] if 'Una' in data[10] else wiz.convertSize(int(float(data[10][:-8]))*1024*1024)
    ram_free      = wiz.convertSize(int(float(data[11][:-2]))*1024*1024)
    ram_used      = wiz.convertSize(int(float(data[12][:-2]))*1024*1024)
    ram_total     = wiz.convertSize(int(float(data[13][:-2]))*1024*1024)
    exter_ip, provider, location = getIP()

    picture = []; music = []; video = []; programs = []; repos = []; scripts = []; skins = []

    fold = glob.glob(os.path.join(ADDONS, '*/'))
    for folder in sorted(fold, key = lambda x: x):
        foldername = os.path.split(folder[:-1])[1]
        if foldername == 'packages': continue
        xml = os.path.join(folder, 'addon.xml')
        if os.path.exists(xml):
            f      = open(xml)
            a      = f.read()
            prov   = re.compile("<provides>(.+?)</provides>").findall(a)
            if len(prov) == 0:
                if foldername.startswith('skin'): skins.append(foldername)
                elif foldername.startswith('repo'): repos.append(foldername)
                else: scripts.append(foldername)
            elif not (prov[0]).find('executable') == -1: programs.append(foldername)
            elif not (prov[0]).find('video') == -1: video.append(foldername)
            elif not (prov[0]).find('audio') == -1: music.append(foldername)
            elif not (prov[0]).find('image') == -1: picture.append(foldername)

    addFile('Media Center Info:', '', icon=ICONMAINT, themeit=THEME2)
    addFile('[COLOR %s]Name:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR1, COLOR2, data[0]), '', icon=ICONMAINT, themeit=THEME3)
    addFile('[COLOR %s]Version:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR1, COLOR2, data[1]), '', icon=ICONMAINT, themeit=THEME3)
    addFile('[COLOR %s]Platform:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR1, COLOR2, wiz.platform().title()), '', icon=ICONMAINT, themeit=THEME3)
    addFile('[COLOR %s]CPU Usage:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR1, COLOR2, data[2]), '', icon=ICONMAINT, themeit=THEME3)
    addFile('[COLOR %s]Screen Mode:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR1, COLOR2, data[3]), '', icon=ICONMAINT, themeit=THEME3)

    addFile('Uptime:', '', icon=ICONMAINT, themeit=THEME2)
    addFile('[COLOR %s]Current Uptime:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR1, COLOR2, data[6]), '', icon=ICONMAINT, themeit=THEME2)
    addFile('[COLOR %s]Total Uptime:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR1, COLOR2, data[7]), '', icon=ICONMAINT, themeit=THEME2)

    addFile('Local Storage:', '', icon=ICONMAINT, themeit=THEME2)
    addFile('[COLOR %s]Used Storage:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR1, COLOR2, storage_used), '', icon=ICONMAINT, themeit=THEME2)
    addFile('[COLOR %s]Free Storage:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR1, COLOR2, storage_free), '', icon=ICONMAINT, themeit=THEME2)
    addFile('[COLOR %s]Total Storage:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR1, COLOR2, storage_total), '', icon=ICONMAINT, themeit=THEME2)

    addFile('Ram Usage:', '', icon=ICONMAINT, themeit=THEME2)
    addFile('[COLOR %s]Used Memory:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR1, COLOR2, ram_free), '', icon=ICONMAINT, themeit=THEME2)
    addFile('[COLOR %s]Free Memory:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR1, COLOR2, ram_used), '', icon=ICONMAINT, themeit=THEME2)
    addFile('[COLOR %s]Total Memory:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR1, COLOR2, ram_total), '', icon=ICONMAINT, themeit=THEME2)

    addFile('Network:', '', icon=ICONMAINT, themeit=THEME2)
    addFile('[COLOR %s]Local IP:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR1, COLOR2, data[4]), '', icon=ICONMAINT, themeit=THEME2)
    addFile('[COLOR %s]External IP:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR1, COLOR2, exter_ip), '', icon=ICONMAINT, themeit=THEME2)
    addFile('[COLOR %s]Provider:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR1, COLOR2, provider), '', icon=ICONMAINT, themeit=THEME2)
    addFile('[COLOR %s]Location:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR1, COLOR2, location), '', icon=ICONMAINT, themeit=THEME2)
    addFile('[COLOR %s]MacAddress:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR1, COLOR2, data[5]), '', icon=ICONMAINT, themeit=THEME2)

    addFile('Network:', '', icon=ICONSPEED, themeit=THEME2)
    addFile('[COLOR %s]Local IP:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR1, COLOR2, data[4]), '', icon=ICONSPEED, themeit=THEME2)
    addFile('[COLOR %s]External IP:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR1, COLOR2, exter_ip), '', icon=ICONSPEED, themeit=THEME2)
    addFile('[COLOR %s]Provider:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR1, COLOR2, provider), '', icon=ICONSPEED, themeit=THEME2)
    addFile('[COLOR %s]Location:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR1, COLOR2, location), '', icon=ICONSPEED, themeit=THEME2)
    addFile('[COLOR %s]MacAddress:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR1, COLOR2, data[5]), '', icon=ICONSPEED, themeit=THEME2)

    totalcount = len(picture) + len(music) + len(video) + len(programs) + len(scripts) + len(skins) + len(repos)
    addFile('Addons([COLOR %s]%s[/COLOR]):' % (COLOR1, totalcount), '', icon=ICONMAINT, themeit=THEME2)
    addFile('[COLOR %s]Video Addons:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR1, COLOR2, str(len(video))), '', icon=ICONMAINT, themeit=THEME2)
    addFile('[COLOR %s]Program Addons:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR1, COLOR2, str(len(programs))), '', icon=ICONMAINT, themeit=THEME2)
    addFile('[COLOR %s]Music Addons:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR1, COLOR2, str(len(music))), '', icon=ICONMAINT, themeit=THEME2)
    addFile('[COLOR %s]Picture Addons:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR1, COLOR2, str(len(picture))), '', icon=ICONMAINT, themeit=THEME2)
    addFile('[COLOR %s]Repositories:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR1, COLOR2, str(len(repos))), '', icon=ICONMAINT, themeit=THEME2)
    addFile('[COLOR %s]Skins:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR1, COLOR2, str(len(skins))), '', icon=ICONMAINT, themeit=THEME2)
    addFile('[COLOR %s]Scripts/Modules:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR1, COLOR2, str(len(scripts))), '', icon=ICONMAINT, themeit=THEME2)

def saveMenu():
    on = '[COLOR springgreen]ON[/COLOR]'; off = '[COLOR red]OFF[/COLOR]'
    myvideos   = 'true' if KEEPMYVIDEOS  == 'true' else 'false'
    sources    = 'true' if KEEPSOURCES   == 'true' else 'false'
    advanced   = 'true' if KEEPADVANCED  == 'true' else 'false'
    profiles   = 'true' if KEEPPROFILES  == 'true' else 'false'
    favourites = 'true' if KEEPFAVS      == 'true' else 'false'
    repos      = 'true' if KEEPREPOS     == 'true' else 'false'
    super      = 'true' if KEEPSUPER     == 'true' else 'false'
    whitelist  = 'true' if KEEPWHITELIST == 'true' else 'false'

    addFile('Importar Base de Datos',              'managedata', 'import', icon=ICONSAVE,  themeit=THEME1)
    addFile('Exportar Base de Datos',              'managedata', 'export', icon=ICONSAVE,  themeit=THEME1)
    addFile('Mantener Videoteca \'MyVideos116.db\': %s' % myvideos.replace('true',on).replace('false',off)          ,'togglesetting', 'keepmyvideos', icon=ICONSAVE, themeit=THEME1)
    addFile('Mantener Fuentes de contenido \'Sources.xml\': %s' % sources.replace('true',on).replace('false',off)           ,'togglesetting', 'keepsources',    icon=ICONSAVE,  themeit=THEME1)
    addFile('Mantener Perfiles \'Profiles.xml\': %s' % profiles.replace('true',on).replace('false',off)         ,'togglesetting', 'keepprofiles',   icon=ICONSAVE,  themeit=THEME1)
    addFile('Mantener Buffer \'Advancedsettings.xml\': %s' % advanced.replace('true',on).replace('false',off) ,'togglesetting', 'keepadvanced',   icon=ICONSAVE,  themeit=THEME1)
    addFile('Mantener Favoritos \'Favourites.xml\': %s' % favourites.replace('true',on).replace('false',off)     ,'togglesetting', 'keepfavourites', icon=ICONSAVE,  themeit=THEME1)
    addFile('Mantener Super Favourites: %s' % super.replace('true',on).replace('false',off)            ,'togglesetting', 'keepsuper',      icon=ICONSAVE,  themeit=THEME1)
    addFile('Mantener Repo\'s instaladas: %s' % repos.replace('true',on).replace('false',off)           ,'togglesetting', 'keeprepos',      icon=ICONSAVE,  themeit=THEME1)
    addFile('Mantener Mi Lista Blanca \'WhiteList\': %s' % whitelist.replace('true',on).replace('false',off)        ,'togglesetting', 'keepwhitelist',  icon=ICONSAVE,  themeit=THEME1)
    if whitelist == 'true':
        addFile('Edit My Whitelist',        'whitelist', 'edit',   icon=ICONSAVE,  themeit=THEME1)
        addFile('View My Whitelist',        'whitelist', 'view',   icon=ICONSAVE,  themeit=THEME1)
        addFile('Clear My Whitelist',       'whitelist', 'clear',  icon=ICONSAVE,  themeit=THEME1)
        addFile('Import My Whitelist',      'whitelist', 'import', icon=ICONSAVE,  themeit=THEME1)
        addFile('Export My Whitelist',      'whitelist', 'export', icon=ICONSAVE,  themeit=THEME1)
    setView('files', 'viewType')

def traktMenu():
    trakt = '[COLOR springgreen]ON[/COLOR]' if KEEPTRAKT == 'true' else '[COLOR red]OFF[/COLOR]'
    last = str(TRAKTSAVE) if not TRAKTSAVE == '' else 'Trakt hasnt been saved yet.'
    addFile('[I]Register FREE Account at http://trakt.tv[/I]', '', icon=ICONTRAKT, themeit=THEME3)
    addFile('Save Trakt Data: %s' % trakt, 'togglesetting', 'keeptrakt', icon=ICONTRAKT, themeit=THEME3)
    if KEEPTRAKT == 'true': addFile('Last Save: %s' % str(last), '', icon=ICONTRAKT, themeit=THEME3)
    if HIDESPACERS == 'No': addFile(wiz.sep(), '', icon=ICONTRAKT, themeit=THEME3)

    for trakt in traktit.ORDER:
        if xbmc.getCondVisibility('System.HasAddon(%s)' % TRAKTID[trakt]['plugin']):
            name   = TRAKTID[trakt]['name']
            path   = TRAKTID[trakt]['path']
            saved  = TRAKTID[trakt]['saved']
            file   = TRAKTID[trakt]['file']
            user   = wiz.getS(saved)
            auser  = traktit.traktUser(trakt)
            icon   = TRAKTID[trakt]['icon']   if os.path.exists(path) else ICONTRAKT
            fanart = TRAKTID[trakt]['fanart'] if os.path.exists(path) else FANART
            menu = createMenu('saveaddon', 'Trakt', trakt)
            menu2 = createMenu('save', 'Trakt', trakt)
            menu.append((THEME2 % '%s Settings' % name,              'RunPlugin(plugin://%s/?mode=opensettings&name=%s&url=trakt)' %   (ADDON_ID, trakt)))

            addFile('[+]-> %s' % name,     '', icon=icon, fanart=fanart, themeit=THEME3)
            if not os.path.exists(path): addFile('[COLOR red]Addon Data: Not Installed[/COLOR]', '', icon=icon, fanart=fanart, menu=menu)
            elif not auser:              addFile('[COLOR red]Addon Data: Not Registered[/COLOR]','authtrakt', trakt, icon=icon, fanart=fanart, menu=menu)
            else:                        addFile('[COLOR springgreen]Addon Data: %s[/COLOR]' % auser,'authtrakt', trakt, icon=icon, fanart=fanart, menu=menu)
            if user == "":
                if os.path.exists(file): addFile('[COLOR red]Saved Data: Save File Found(Import Data)[/COLOR]','importtrakt', trakt, icon=icon, fanart=fanart, menu=menu2)
                else :                   addFile('[COLOR red]Saved Data: Not Saved[/COLOR]','savetrakt', trakt, icon=icon, fanart=fanart, menu=menu2)
            else:                        addFile('[COLOR springgreen]Saved Data: %s[/COLOR]' % user, '', icon=icon, fanart=fanart, menu=menu2)

    if HIDESPACERS == 'No': addFile(wiz.sep(), '', themeit=THEME3)
    addFile('Save All Trakt Data',          'savetrakt',    'all', icon=ICONTRAKT,  themeit=THEME3)
    addFile('Recover All Saved Trakt Data', 'restoretrakt', 'all', icon=ICONTRAKT,  themeit=THEME3)
    addFile('Import Trakt Data',            'importtrakt',  'all', icon=ICONTRAKT,  themeit=THEME3)
    addFile('Clear All Addon Trakt Data',         'addontrakt',   'all', icon=ICONTRAKT,  themeit=THEME3)
    addFile('Clear All Saved Trakt Data',   'cleartrakt',   'all', icon=ICONTRAKT,  themeit=THEME3)
    setView('files', 'viewType')

def realMenu():
    real = '[COLOR springgreen]ON[/COLOR]' if KEEPREAL == 'true' else '[COLOR red]OFF[/COLOR]'
    last = str(REALSAVE) if not REALSAVE == '' else 'Real Debrid hasnt been saved yet.'
    addFile('[I]http://real-debrid.com is a PAID service.[/I]', '', icon=ICONREAL, themeit=THEME3)
    addFile('Save Real Debrid Data: %s' % real, 'togglesetting', 'keepdebrid', icon=ICONREAL, themeit=THEME3)
    if KEEPREAL == 'true': addFile('Last Save: %s' % str(last), '', icon=ICONREAL, themeit=THEME3)
    if HIDESPACERS == 'No': addFile(wiz.sep(), '', icon=ICONREAL, themeit=THEME3)

    for debrid in debridit.ORDER:
        if xbmc.getCondVisibility('System.HasAddon(%s)' % DEBRIDID[debrid]['plugin']):
            name   = DEBRIDID[debrid]['name']
            path   = DEBRIDID[debrid]['path']
            saved  = DEBRIDID[debrid]['saved']
            file   = DEBRIDID[debrid]['file']
            user   = wiz.getS(saved)
            auser  = debridit.debridUser(debrid)
            icon   = DEBRIDID[debrid]['icon']   if os.path.exists(path) else ICONREAL
            fanart = DEBRIDID[debrid]['fanart'] if os.path.exists(path) else FANART
            menu = createMenu('saveaddon', 'Debrid', debrid)
            menu2 = createMenu('save', 'Debrid', debrid)
            menu.append((THEME2 % '%s Settings' % name,              'RunPlugin(plugin://%s/?mode=opensettings&name=%s&url=debrid)' %   (ADDON_ID, debrid)))

            addFile('[+]-> %s' % name,     '', icon=icon, fanart=fanart, themeit=THEME3)
            if not os.path.exists(path): addFile('[COLOR red]Addon Data: Not Installed[/COLOR]', '', icon=icon, fanart=fanart, menu=menu)
            elif not auser:              addFile('[COLOR red]Addon Data: Not Registered[/COLOR]','authdebrid', debrid, icon=icon, fanart=fanart, menu=menu)
            else:                        addFile('[COLOR springgreen]Addon Data: %s[/COLOR]' % auser,'authdebrid', debrid, icon=icon, fanart=fanart, menu=menu)
            if user == "":
                if os.path.exists(file): addFile('[COLOR red]Saved Data: Save File Found(Import Data)[/COLOR]','importdebrid', debrid, icon=icon, fanart=fanart, menu=menu2)
                else :                   addFile('[COLOR red]Saved Data: Not Saved[/COLOR]','savedebrid', debrid, icon=icon, fanart=fanart, menu=menu2)
            else:                        addFile('[COLOR springgreen]Saved Data: %s[/COLOR]' % user, '', icon=icon, fanart=fanart, menu=menu2)

    if HIDESPACERS == 'No': addFile(wiz.sep(), '', themeit=THEME3)
    addFile('Save All Debrid Data',          'savedebrid',    'all', icon=ICONREAL,  themeit=THEME3)
    addFile('Recover All Saved Debrid Data', 'restoredebrid', 'all', icon=ICONREAL,  themeit=THEME3)
    addFile('Import Debrid Data',            'importdebrid',  'all', icon=ICONREAL,  themeit=THEME3)
    addFile('Clear All Addon Debrid Data',               'addondebrid',   'all', icon=ICONREAL,  themeit=THEME3)
    addFile('Clear All Saved Debrid Data',   'cleardebrid',   'all', icon=ICONREAL,  themeit=THEME3)
    setView('files', 'viewType')

def loginMenu():
    login = '[COLOR springgreen]ON[/COLOR]' if KEEPLOGIN == 'true' else '[COLOR red]OFF[/COLOR]'
    last = str(LOGINSAVE) if not LOGINSAVE == '' else 'Login data hasnt been saved yet.'
    addFile('[I]Several of these addons are PAID services.[/I]', '', icon=ICONLOGIN, themeit=THEME3)
    addFile('Save API Keys: %s' % login, 'togglesetting', 'keeplogin', icon=ICONLOGIN, themeit=THEME3)
    if KEEPLOGIN == 'true': addFile('Last Save: %s' % str(last), '', icon=ICONLOGIN, themeit=THEME3)
    if HIDESPACERS == 'No': addFile(wiz.sep(), '', icon=ICONLOGIN, themeit=THEME3)

    for login in loginit.ORDER:
        if xbmc.getCondVisibility('System.HasAddon(%s)' % LOGINID[login]['plugin']):
            name   = LOGINID[login]['name']
            path   = LOGINID[login]['path']
            saved  = LOGINID[login]['saved']
            file   = LOGINID[login]['file']
            user   = wiz.getS(saved)
            auser  = loginit.loginUser(login)
            icon   = LOGINID[login]['icon']   if os.path.exists(path) else ICONLOGIN
            fanart = LOGINID[login]['fanart'] if os.path.exists(path) else FANART
            menu = createMenu('saveaddon', 'Login', login)
            menu2 = createMenu('save', 'Login', login)
            menu.append((THEME2 % '%s Settings' % name,              'RunPlugin(plugin://%s/?mode=opensettings&name=%s&url=login)' %   (ADDON_ID, login)))

            addFile('[+]-> %s' % name,     '', icon=icon, fanart=fanart, themeit=THEME3)
            if not os.path.exists(path): addFile('[COLOR red]Addon Data: Not Installed[/COLOR]', '', icon=icon, fanart=fanart, menu=menu)
            elif not auser:              addFile('[COLOR red]Addon Data: Not Registered[/COLOR]','authlogin', login, icon=icon, fanart=fanart, menu=menu)
            else:                        addFile('[COLOR springgreen]Addon Data: %s[/COLOR]' % auser,'authlogin', login, icon=icon, fanart=fanart, menu=menu)
            if user == "":
                if os.path.exists(file): addFile('[COLOR red]Saved Data: Save File Found(Import Data)[/COLOR]','importlogin', login, icon=icon, fanart=fanart, menu=menu2)
                else :                   addFile('[COLOR red]Saved Data: Not Saved[/COLOR]','savelogin', login, icon=icon, fanart=fanart, menu=menu2)
            else:                        addFile('[COLOR springgreen]Saved Data: %s[/COLOR]' % user, '', icon=icon, fanart=fanart, menu=menu2)

    if HIDESPACERS == 'No': addFile(wiz.sep(), '', themeit=THEME3)
    addFile('Save All Login Info',          'savelogin',    'all', icon=ICONLOGIN,  themeit=THEME3)
    addFile('Recover All Saved Login Info', 'restorelogin', 'all', icon=ICONLOGIN,  themeit=THEME3)
    addFile('Import Login Info',            'importlogin',  'all', icon=ICONLOGIN,  themeit=THEME3)
    addFile('Clear All Addon Login Info',         'addonlogin',   'all', icon=ICONLOGIN,  themeit=THEME3)
    addFile('Clear All Saved Login Info',   'clearlogin',   'all', icon=ICONLOGIN,  themeit=THEME3)
    setView('files', 'viewType')

def fixUpdate():
    if KODIV < 17:
        dbfile = os.path.join(DATABASE, wiz.latestDB('Addons'))
        try:
            os.remove(dbfile)
        except Exception, e:
            wiz.log("Unable to remove %s, Purging DB" % dbfile)
            wiz.purgeDb(dbfile)
    else:
        if os.path.exists(os.path.join(USERDATA, 'autoexec.py')):
            temp = os.path.join(USERDATA, 'autoexec_temp.py')
            if os.path.exists(temp): xbmcvfs.delete(temp)
            xbmcvfs.rename(os.path.join(USERDATA, 'autoexec.py'), temp)
        xbmcvfs.copy(os.path.join(PLUGIN, 'resources', 'libs', 'autoexec.py'), os.path.join(USERDATA, 'autoexec.py'))
        dbfile = os.path.join(DATABASE, wiz.latestDB('Addons'))
        try:
            os.remove(dbfile)
        except Exception, e:
            wiz.log("Unable to remove %s, Purging DB" % dbfile)
            wiz.purgeDb(dbfile)
        wiz.killxbmc(True)

def removeAddonMenu():
    fold = glob.glob(os.path.join(ADDONS, '*/'))
    addonnames = []; addonids = []
    for folder in sorted(fold, key = lambda x: x):
        foldername = os.path.split(folder[:-1])[1]
        if foldername in EXCLUDES: continue
        elif foldername in DEFAULTPLUGINS: continue
        elif foldername == 'packages': continue
        xml = os.path.join(folder, 'addon.xml')
        if os.path.exists(xml):
            f      = open(xml)
            a      = f.read()
            match  = wiz.parseDOM(a, 'addon', ret='id')

            addid  = foldername if len(match) == 0 else match[0]
            try:
                add = xbmcaddon.Addon(id=addid)
                addonnames.append(add.getAddonInfo('name'))
                addonids.append(addid)
            except:
                pass
    if len(addonnames) == 0:
        wiz.LogNotify("[COLOR %s]%s[/COLOR]" % (COLOR1, ADDONTITLE), "[COLOR %s]No Addons To Remove[/COLOR]" % COLOR2)
        return
    if KODIV > 16:
        selected = DIALOG.multiselect("%s: Elige los addons que quieres borrar." % ADDONTITLE, addonnames)
    else:
        selected = []; choice = 0
        tempaddonnames = ["-- Click here to Continue --"] + addonnames
        while not choice == -1:
            choice = DIALOG.select("%s: Elige los addons que quieres borrar." % ADDONTITLE, tempaddonnames)
            if choice == -1: break
            elif choice == 0: break
            else:
                choice2 = (choice-1)
                if choice2 in selected:
                    selected.remove(choice2)
                    tempaddonnames[choice] = addonnames[choice2]
                else:
                    selected.append(choice2)
                    tempaddonnames[choice] = "[COLOR %s]%s[/COLOR]" % (COLOR1, addonnames[choice2])
    if selected == None: return
    if len(selected) > 0:
        wiz.addonUpdates('set')
        for addon in selected:
            removeAddon(addonids[addon], addonnames[addon], True)

        xbmc.sleep(500)

        if INSTALLMETHOD == 1: todo = 1
        elif INSTALLMETHOD == 2: todo = 0
        else: todo = DIALOG.yesno(ADDONTITLE, "[COLOR %s]Quieres [COLOR %s]Forzar el cierre de[/COLOR] Kodi o [COLOR %s]Recargar el perfil[/COLOR]?La Opcion recomendada es Cerrar.[/COLOR]" % (COLOR2, COLOR1, COLOR1), yeslabel="[COLOR red]Recargar[/COLOR]", nolabel="[COLOR spinggreen]Cerrar Kodi[/COLOR]")
        if todo == 1: wiz.reloadFix('remove addon')
        else: wiz.addonUpdates('reset'); wiz.killxbmc(True)

def removeAddonDataMenu():
    if os.path.exists(ADDOND):
        addFile('[COLOR red][BORRAR][/COLOR] Toda la carpeta Addon_Data', 'removedata', 'all', themeit=THEME2)
        addFile('[COLOR red][BORRAR][/COLOR] Addon_Data de Addons Desinstalados', 'removedata', 'uninstalled', themeit=THEME2)
        addFile('[COLOR red][BORRAR][/COLOR] Carpetas vacias de Addon_Data', 'removedata', 'empty', themeit=THEME2)
        addFile('[COLOR red][BORRAR][/COLOR] Carpeta %s de Addon_Data' % ADDONTITLE, 'resetaddon', themeit=THEME2)
        if HIDESPACERS == 'No': addFile(wiz.sep(), '', themeit=THEME3)
        fold = glob.glob(os.path.join(ADDOND, '*/'))
        for folder in sorted(fold, key = lambda x: x):
            foldername = folder.replace(ADDOND, '').replace('\\', '').replace('/', '')
            icon = os.path.join(folder.replace(ADDOND, ADDONS), 'icon.png')
            fanart = os.path.join(folder.replace(ADDOND, ADDONS), 'fanart.png')
            folderdisplay = foldername
            replace = {'audio.':'[COLOR orange][AUDIO] [/COLOR]', 'metadata.':'[COLOR cyan][METADATA] [/COLOR]', 'module.':'[COLOR orange][MODULE] [/COLOR]', 'plugin.':'[COLOR blue][PLUGIN] [/COLOR]', 'program.':'[COLOR orange][PROGRAM] [/COLOR]', 'repository.':'[COLOR gold][REPO] [/COLOR]', 'script.':'[COLOR springgreen][SCRIPT] [/COLOR]', 'service.':'[COLOR springgreen][SERVICE] [/COLOR]', 'skin.':'[COLOR dodgerblue][SKIN] [/COLOR]', 'video.':'[COLOR orange][VIDEO] [/COLOR]', 'weather.':'[COLOR yellow][WEATHER] [/COLOR]'}
            for rep in replace:
                folderdisplay = folderdisplay.replace(rep, replace[rep])
            if foldername in EXCLUDES: folderdisplay = '[COLOR springgreen][BLOQUEADO][/COLOR] %s' % folderdisplay
            else: folderdisplay = '[COLOR red][BORRAR][/COLOR] %s' % folderdisplay
            addFile(' %s' % folderdisplay, 'removedata', foldername, icon=icon, fanart=fanart, themeit=THEME2)
    else:
        addFile('No Addon data folder found.', '', themeit=THEME3)
    setView('files', 'viewType')

def enableAddons():
    addFile("[I][COLOR red]Atencion: Desactivar algunos addons puede causar problemas[/COLOR][/I]", '', icon=ICONMAINT)
    fold = glob.glob(os.path.join(ADDONS, '*/'))
    x = 0
    for folder in sorted(fold, key = lambda x: x):
        foldername = os.path.split(folder[:-1])[1]
        if foldername in EXCLUDES: continue
        if foldername in DEFAULTPLUGINS: continue
        addonxml = os.path.join(folder, 'addon.xml')
        if os.path.exists(addonxml):
            x += 1
            fold   = folder.replace(ADDONS, '')[1:-1]
            f      = open(addonxml)
            a      = f.read().replace('\n','').replace('\r','').replace('\t','')
            match  = wiz.parseDOM(a, 'addon', ret='id')
            match2 = wiz.parseDOM(a, 'addon', ret='name')
            try:
                pluginid = match[0]
                name = match2[0]
            except:
                continue
            try:
                add    = xbmcaddon.Addon(id=pluginid)
                state  = "[COLOR springgreen][Activado][/COLOR]"
                goto   = "false"
            except:
                state  = "[COLOR red][Desactivado][/COLOR]"
                goto   = "true"
                pass
            icon   = os.path.join(folder, 'icon.png') if os.path.exists(os.path.join(folder, 'icon.png')) else ICON
            fanart = os.path.join(folder, 'fanart.jpg') if os.path.exists(os.path.join(folder, 'fanart.jpg')) else FANART
            addFile("%s %s" % (state, name), 'toggleaddon', fold, goto, icon=icon, fanart=fanart)
            f.close()
    if x == 0:
        addFile("No Addons Found to Enable or Disable.", '', icon=ICONMAINT)
    setView('files', 'viewType')

def changeFeq():
    feq        = ['Cada inicio de Kodi', 'Cada dia', 'Cada 3 dias', 'Semanalmente']
    change     = DIALOG.select("[COLOR %s]Cada cuanto quieres que se limpie Kodi?[/COLOR]" % COLOR2, feq)
    if not change == -1:
        wiz.setS('autocleanfeq', str(change))
        wiz.LogNotify('[COLOR %s]Auto Limpieza[/COLOR]' % COLOR1, '[COLOR %s]Frecuencia: %s[/COLOR]' % (COLOR2, feq[change]))

def developer():
    addFile('Convert Text Files to 0.1.7',         'converttext',           themeit=THEME1)
    addFile('Create QR Code',                      'createqr',              themeit=THEME1)
    addFile('Test Notifications',                  'testnotify',            themeit=THEME1)
    addFile('Test Update',                         'testupdate',            themeit=THEME1)
    addFile('Test First Run',                      'testfirst',             themeit=THEME1)
    addFile('Test First Run Settings',             'testfirstrun',          themeit=THEME1)
    setView('files', 'viewType')

###########################
###### Build Install ######
###########################




def testTheme(path):
    zfile = zipfile.ZipFile(path)
    for item in zfile.infolist():
        wiz.log(str(item.filename))
        if '/settings.xml' in item.filename:
            return True
    return False

def testGui(path):
    zfile = zipfile.ZipFile(path)
    for item in zfile.infolist():
        if '/guisettings.xml' in item.filename:
            return True
    return False

def grabAddons(path):
    zfile = zipfile.ZipFile(path)
    addonlist = []
    for item in zfile.infolist():
        if str(item.filename).find('addon.xml') == -1: continue
        info = str(item.filename).split('/')
        if not info[-2] in addonlist:
            addonlist.append(info[-2])
    return addonlist

def apkInstaller(apk, url):
    wiz.log(apk)
    wiz.log(url)
    if wiz.platform() == 'android':
        yes = DIALOG.yesno(ADDONTITLE, "[COLOR %s]Quieres descargar e instalar:" % COLOR2, "[COLOR %s]%s[/COLOR]" % (COLOR1, apk), yeslabel="[COLOR springgreen]Descargar[/COLOR]", nolabel="[COLOR red]Cancelar[/COLOR]")
        if not yes: wiz.LogNotify("[COLOR %s]%s[/COLOR]" % (COLOR1, ADDONTITLE), '[COLOR %s]ERROR: Instalacion Cancelada[/COLOR]' % COLOR2); return
        display = apk
        if not os.path.exists(PACKAGES): os.makedirs(PACKAGES)
        if not wiz.workingURL(url) == True: wiz.LogNotify("[COLOR %s]%s[/COLOR]" % (COLOR1, ADDONTITLE), '[COLOR %s]APK Installer: Invalid Apk Url![/COLOR]' % COLOR2); return
        DP.create(ADDONTITLE,'[COLOR %s]Descargando:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR2, COLOR1, display),'', 'Espera')
        lib=os.path.join(PACKAGES, "%s.apk" % apk.replace('\\', '').replace('/', '').replace(':', '').replace('*', '').replace('?', '').replace('"', '').replace('<', '').replace('>', '').replace('|', ''))
        try: os.remove(lib)
        except: pass
        downloader.download(url, lib, DP)
        xbmc.sleep(100)
        DP.close()
        notify.apkInstaller(apk)
        wiz.ebi('StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:'+lib+'")')
    else: wiz.LogNotify("[COLOR %s]%s[/COLOR]" % (COLOR1, ADDONTITLE), '[COLOR %s]ERROR: None Android Device[/COLOR]' % COLOR2)

def romInstaller(name, url):
    myroms = xbmc.translatePath(BACKUPROMS)
    if myroms == '':
        if DIALOG.yesno(ADDONTITLE, "[COLOR %s]It seems that you do not have an extract location setup for Rom Packs" % COLOR2, "Would you like to set one?[/COLOR]", yeslabel="[COLOR springgreen]Set Location[/COLOR]", nolabel="[COLOR red]Cancel Download[/COLOR]"):
            wiz.openS()
            myroms = wiz.getS('rompath')
            if myroms == '': return
    yes = DIALOG.yesno(ADDONTITLE, "[COLOR %s]Are you sure you would like to download and extract [COLOR %s]%s[/COLOR] to:" % (COLOR2, COLOR1, name), "[COLOR %s]%s[/COLOR]" % (COLOR1, myroms), yeslabel="[COLOR springgreen]Download[/COLOR]", nolabel="[COLOR red]Cancel[/COLOR]")
    if not yes: wiz.LogNotify("[COLOR %s]%s[/COLOR]" % (COLOR1, ADDONTITLE), '[COLOR %s]ERROR: Install Cancelled[/COLOR]' % COLOR2); return
    display = name
    if not os.path.exists(PACKAGES): os.makedirs(PACKAGES)
    if not wiz.workingURL(url) == True: wiz.LogNotify("[COLOR %s]%s[/COLOR]" % (COLOR1, ADDONTITLE), '[COLOR %s]APK Installer: Invalid Rom Url![/COLOR]' % COLOR2); return
    DP.create(ADDONTITLE,'[COLOR %s]Downloading:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR2, COLOR1, display),'', 'Please Wait')
    lib=os.path.join(PACKAGES, "%s.zip" % name.replace('\\', '').replace('/', '').replace(':', '').replace('*', '').replace('?', '').replace('"', '').replace('<', '').replace('>', '').replace('|', ''))
    try: os.remove(lib)
    except: pass
    downloader.download(url, lib, DP)
    xbmc.sleep(100)
    percent, errors, error = extract.all(lib,myroms,DP, title=display)
    try: os.remove(lib)
    except: pass
    wiz.LogNotify("[COLOR %s]%s[/COLOR]" % (COLOR1, ADDONTITLE), '[COLOR %s]Rom Pack Installed[/COLOR]' % COLOR2)
    DP.close()

###########################
###### Misc Functions######
###########################

def createMenu(type, add, name):
    if   type == 'saveaddon':
        menu_items=[]
        add2  = urllib.quote_plus(add.lower().replace(' ', ''))
        add3  = add.replace('Debrid', 'Real Debrid')
        name2 = urllib.quote_plus(name.lower().replace(' ', ''))
        name = name.replace('url', 'URL Resolver')
        menu_items.append((THEME2 % name.title(),             ' '))
        menu_items.append((THEME3 % 'Save %s Data' % add3,               'RunPlugin(plugin://%s/?mode=save%s&name=%s)' %    (ADDON_ID, add2, name2)))
        menu_items.append((THEME3 % 'Restore %s Data' % add3,            'RunPlugin(plugin://%s/?mode=restore%s&name=%s)' % (ADDON_ID, add2, name2)))
        menu_items.append((THEME3 % 'Clear %s Data' % add3,              'RunPlugin(plugin://%s/?mode=clear%s&name=%s)' %   (ADDON_ID, add2, name2)))
    elif type == 'save'    :
        menu_items=[]
        add2  = urllib.quote_plus(add.lower().replace(' ', ''))
        add3  = add.replace('Debrid', 'Real Debrid')
        name2 = urllib.quote_plus(name.lower().replace(' ', ''))
        name = name.replace('url', 'URL Resolver')
        menu_items.append((THEME2 % name.title(),             ' '))
        menu_items.append((THEME3 % 'Register %s' % add3,                'RunPlugin(plugin://%s/?mode=auth%s&name=%s)' %    (ADDON_ID, add2, name2)))
        menu_items.append((THEME3 % 'Save %s Data' % add3,               'RunPlugin(plugin://%s/?mode=save%s&name=%s)' %    (ADDON_ID, add2, name2)))
        menu_items.append((THEME3 % 'Restore %s Data' % add3,            'RunPlugin(plugin://%s/?mode=restore%s&name=%s)' % (ADDON_ID, add2, name2)))
        menu_items.append((THEME3 % 'Import %s Data' % add3,             'RunPlugin(plugin://%s/?mode=import%s&name=%s)' %  (ADDON_ID, add2, name2)))
        menu_items.append((THEME3 % 'Clear Addon %s Data' % add3,        'RunPlugin(plugin://%s/?mode=addon%s&name=%s)' %   (ADDON_ID, add2, name2)))
    elif type == 'install'  :
        menu_items=[]
        name2 = urllib.quote_plus(name)
        menu_items.append((THEME2 % name,                                'RunAddon(%s, ?mode=viewbuild&name=%s)'  % (ADDON_ID, name2)))
        menu_items.append((THEME3 % 'Fresh Install',                     'RunPlugin(plugin://%s/?mode=install&name=%s&url=fresh)'  % (ADDON_ID, name2)))
        menu_items.append((THEME3 % 'Normal Install',                    'RunPlugin(plugin://%s/?mode=install&name=%s&url=normal)' % (ADDON_ID, name2)))
        menu_items.append((THEME3 % 'Apply guiFix',                      'RunPlugin(plugin://%s/?mode=install&name=%s&url=gui)'    % (ADDON_ID, name2)))
        menu_items.append((THEME3 % 'Build Information',                 'RunPlugin(plugin://%s/?mode=buildinfo&name=%s)'  % (ADDON_ID, name2)))
    menu_items.append((THEME2 % '%s Settings' % ADDONTITLE,              'RunPlugin(plugin://%s/?mode=settings)' % ADDON_ID))
    return menu_items

def toggleCache(state):
    cachelist = ['includevideo', 'includeall', 'include13clowns', 'includeexodusredux', 'includegaia', 'includemagicality', 'includeplacenta', 'includeseren', 'includezanni' ]
    titlelist = ['Include Video Addons', 'Include All Addons', 'Include 13Clowns', 'Include Exodus Redux', 'Include Gaia', 'Include Magicality', 'Include Placenta', 'Include Seren', 'Include Zanni']
    if state in ['true', 'false']:
        for item in cachelist:
            wiz.setS(item, state)
    else:
        if not state in ['includevideo', 'includeall'] and wiz.getS('includeall') == 'true':
            try:
                item = titlelist[cachelist.index(state)]
                DIALOG.ok(ADDONTITLE, "[COLOR %s]You will need to turn off [COLOR %s]Include All Addons[/COLOR] to disable[/COLOR] [COLOR %s]%s[/COLOR]" % (COLOR2, COLOR1, COLOR1, item))
            except:
                wiz.LogNotify("[COLOR %s]Toggle Cache[/COLOR]" % COLOR1, "[COLOR %s]Invalid id: %s[/COLOR]" % (COLOR2, state))
        else:
            new = 'true' if wiz.getS(state) == 'false' else 'false'
            wiz.setS(state, new)

def playVideo(url):
    if 'watch?v=' in url:
        a, b = url.split('?')
        find = b.split('&')
        for item in find:
            if item.startswith('v='):
                url = item[2:]
                break
            else: continue
    elif 'embed' in url or 'youtu.be' in url:
        a = url.split('/')
        if len(a[-1]) > 5:
            url = a[-1]
        elif len(a[-2]) > 5:
            url = a[-2]
    wiz.log("YouTube URL: %s" % url)
    if wiz.getCond('System.HasAddon(plugin.video.youtube)') == 1:
        url = 'plugin://plugin.video.youtube/play/?video_id=%s' % url
        xbmc.Player().play(url)
    xbmc.sleep(2000)
    if xbmc.Player().isPlayingVideo() == 0:
        yt.PlayVideo(url)

def viewLogFile():
    mainlog = wiz.Grab_Log(True)
    oldlog  = wiz.Grab_Log(True, True)
    which = 0; logtype = mainlog
    if not oldlog == False and not mainlog == False:
        which = DIALOG.select(ADDONTITLE, ["View %s" % mainlog.replace(LOG, ""), "View %s" % oldlog.replace(LOG, "")])
        if which == -1: wiz.LogNotify('[COLOR %s]View Log[/COLOR]' % COLOR1, '[COLOR %s]View Log Cancelled![/COLOR]' % COLOR2); return
    elif mainlog == False and oldlog == False:
        wiz.LogNotify('[COLOR %s]View Log[/COLOR]' % COLOR1, '[COLOR %s]No Log File Found![/COLOR]' % COLOR2)
        return
    elif not mainlog == False: which = 0
    elif not oldlog == False: which = 1

    logtype = mainlog if which == 0 else oldlog
    msg     = wiz.Grab_Log(False) if which == 0 else wiz.Grab_Log(False, True)

    wiz.TextBox("%s - %s" % (ADDONTITLE, logtype), msg)

def errorList(file):
    errors = []
    a=open(file).read()
    b=a.replace('\n','[CR]').replace('\r','')
    match = re.compile("-->Python callback/script returned the following error<--(.+?)-->End of Python script error report<--").findall(b)
    for item in match:
        errors.append(item)
    return errors

def errorChecking(log=None, count=None, last=None):
    errors = []; error1 = []; error2 = [];
    if log == None:
        curr = wiz.Grab_Log(True, False)
        old = wiz.Grab_Log(True, True)
        if old == False and curr == False:
            if count == None:
                wiz.LogNotify('[COLOR %s]View Error Log[/COLOR]' % COLOR1, '[COLOR %s]No Log File Found![/COLOR]' % COLOR2)
                return
            else:
                return 0
        if not curr == False:
            error1 = errorList(curr)
        if not old == False:
            error2 = errorList(old)
        if len(error2) > 0:
            for item in error2: errors = [item] + errors
        if len(error1) > 0:
            for item in error1: errors = [item] + errors
    else:
        error1 = errorList(log)
        if len(error1) > 0:
            for item in error1: errors = [item] + errors
    if not count == None:
        return len(errors)
    elif len(errors) > 0:
        if last == None:
            i = 0; string = ''
            for item in errors:
                i += 1
                string += "[COLOR red]ERROR NUMBER %s:[/COLOR]%s\n" % (str(i), item.replace(HOME, '/').replace('                                        ', ''))
        else:
            string = "[COLOR red]Last Error in Log:[/COLOR]%s\n" % (errors[0].replace(HOME, '/').replace('                                        ', ''))
        wiz.TextBox("%s: Errors in Log" % ADDONTITLE, string)
    else:
        wiz.LogNotify('[COLOR %s]View Error Log[/COLOR]' % COLOR1, '[COLOR %s]No Errors Found![/COLOR]' % COLOR2)

ACTION_PREVIOUS_MENU            =  10   ## ESC action
ACTION_NAV_BACK                 =  92   ## Backspace action
ACTION_MOVE_LEFT                =   1   ## Left arrow key
ACTION_MOVE_RIGHT               =   2   ## Right arrow key
ACTION_MOVE_UP                  =   3   ## Up arrow key
ACTION_MOVE_DOWN                =   4   ## Down arrow key
ACTION_MOUSE_WHEEL_UP           = 104   ## Mouse wheel up
ACTION_MOUSE_WHEEL_DOWN         = 105   ## Mouse wheel down
ACTION_MOVE_MOUSE               = 107   ## Down arrow key
ACTION_SELECT_ITEM              =   7   ## Number Pad Enter
ACTION_BACKSPACE                = 110   ## ?
ACTION_MOUSE_LEFT_CLICK         = 100
ACTION_MOUSE_LONG_CLICK         = 108

def LogViewer(default=None):
    class LogViewer(xbmcgui.WindowXMLDialog):
        def __init__(self,*args,**kwargs):
            self.default = kwargs['default']

        def onInit(self):
            self.title      = 101
            self.msg        = 102
            self.scrollbar  = 103
            self.upload     = 201
            self.kodi       = 202
            self.kodiold    = 203
            self.wizard     = 204
            self.okbutton   = 205
            f = open(self.default, 'r')
            self.logmsg = f.read()
            f.close()
            self.titlemsg = "%s: %s" % (ADDONTITLE, self.default.replace(LOG, '').replace(ADDONDATA, ''))
            self.showdialog()

        def showdialog(self):
            self.getControl(self.title).setLabel(self.titlemsg)
            self.getControl(self.msg).setText(wiz.highlightText(self.logmsg))
            self.setFocusId(self.scrollbar)

        def onClick(self, controlId):
            if   controlId == self.okbutton: self.close()
            elif controlId == self.upload: self.close(); uploadLog.Main()
            elif controlId == self.kodi:
                newmsg = wiz.Grab_Log(False)
                filename = wiz.Grab_Log(True)
                if newmsg == False:
                    self.titlemsg = "%s: View Log Error" % ADDONTITLE
                    self.getControl(self.msg).setText("Log File Does Not Exists!")
                else:
                    self.titlemsg = "%s: %s" % (ADDONTITLE, filename.replace(LOG, ''))
                    self.getControl(self.title).setLabel(self.titlemsg)
                    self.getControl(self.msg).setText(wiz.highlightText(newmsg))
                    self.setFocusId(self.scrollbar)
            elif controlId == self.kodiold:
                newmsg = wiz.Grab_Log(False, True)
                filename = wiz.Grab_Log(True, True)
                if newmsg == False:
                    self.titlemsg = "%s: View Log Error" % ADDONTITLE
                    self.getControl(self.msg).setText("Log File Does Not Exists!")
                else:
                    self.titlemsg = "%s: %s" % (ADDONTITLE, filename.replace(LOG, ''))
                    self.getControl(self.title).setLabel(self.titlemsg)
                    self.getControl(self.msg).setText(wiz.highlightText(newmsg))
                    self.setFocusId(self.scrollbar)
            elif controlId == self.wizard:
                newmsg = wiz.Grab_Log(False, False, True)
                filename = wiz.Grab_Log(True, False, True)
                if newmsg == False:
                    self.titlemsg = "%s: View Log Error" % ADDONTITLE
                    self.getControl(self.msg).setText("Log File Does Not Exists!")
                else:
                    self.titlemsg = "%s: %s" % (ADDONTITLE, filename.replace(ADDONDATA, ''))
                    self.getControl(self.title).setLabel(self.titlemsg)
                    self.getControl(self.msg).setText(wiz.highlightText(newmsg))
                    self.setFocusId(self.scrollbar)

        def onAction(self, action):
            if   action == ACTION_PREVIOUS_MENU: self.close()
            elif action == ACTION_NAV_BACK: self.close()
    if default == None: default = wiz.Grab_Log(True)
    lv = LogViewer( "LogViewer.xml" , ADDON.getAddonInfo('path'), 'DefaultSkin', default=default)
    lv.doModal()
    del lv

def removeAddon(addon, name, over=False):
    if not over == False:
        yes = 1
    else:
        yes = DIALOG.yesno(ADDONTITLE, '[COLOR %s]Are you sure you want to delete the addon:'% COLOR2, 'Name: [COLOR %s]%s[/COLOR]' % (COLOR1, name), 'ID: [COLOR %s]%s[/COLOR][/COLOR]' % (COLOR1, addon), yeslabel='[COLOR springgreen]Remove Addon[/COLOR]', nolabel='[COLOR red]Don\'t Remove[/COLOR]')
    if yes == 1:
        folder = os.path.join(ADDONS, addon)
        wiz.log("Removing Addon %s" % addon)
        wiz.cleanHouse(folder)
        xbmc.sleep(200)
        try: shutil.rmtree(folder)
        except Exception ,e: wiz.log("Error removing %s" % addon, xbmc.LOGNOTICE)
        removeAddonData(addon, name, over)
    if over == False:
        wiz.LogNotify("[COLOR %s]%s[/COLOR]" % (COLOR1, ADDONTITLE), "[COLOR %s]%s Removed[/COLOR]" % (COLOR2, name))

def removeAddonData(addon, name=None, over=False):
    if addon == 'all':
        if DIALOG.yesno(ADDONTITLE, '[COLOR %s]Quieres eliminar [COLOR %s]TODOS[/COLOR] los datos de la carpeta Addon_data?[/COLOR]' % (COLOR2, COLOR1), yeslabel='[COLOR springgreen]Eliminar Data[/COLOR]', nolabel='[COLOR red]No Eliminar[/COLOR]'):
            wiz.cleanHouse(ADDOND)
        else: wiz.LogNotify('[COLOR %s]Borrar Addon_data[/COLOR]' % COLOR1, '[COLOR %s]Cancelado![/COLOR]' % COLOR2)
    elif addon == 'uninstalled':
        if DIALOG.yesno(ADDONTITLE, '[COLOR %s]Quieres eliminar [COLOR %s]TODOS[/COLOR] los datos de la carpeta Addon_data de addons desinstalados?[/COLOR]' % (COLOR2, COLOR1), yeslabel='[COLOR springgreen]Eliminar Data[/COLOR]', nolabel='[COLOR red]No Eliminar[/COLOR]'):
            total = 0
            for folder in glob.glob(os.path.join(ADDOND, '*')):
                foldername = folder.replace(ADDOND, '').replace('\\', '').replace('/', '')
                if foldername in EXCLUDES: pass
                elif os.path.exists(os.path.join(ADDONS, foldername)): pass
                else: wiz.cleanHouse(folder); total += 1; wiz.log(folder); shutil.rmtree(folder)
            wiz.LogNotify('[COLOR %s]Clean up Uninstalled[/COLOR]' % COLOR1, '[COLOR %s]%s Folders(s) Removed[/COLOR]' % (COLOR2, total))
        else: wiz.LogNotify('[COLOR %s]Remove Addon Data[/COLOR]' % COLOR1, '[COLOR %s]Cancelled![/COLOR]' % COLOR2)
    elif addon == 'empty':
        if DIALOG.yesno(ADDONTITLE, '[COLOR %s]Quieres eliminar [COLOR %s]TODAS[/COLOR] las carpetas vacias de userdata?[/COLOR]' % (COLOR2, COLOR1), yeslabel='[COLOR springgreen]Borrar Data[/COLOR]', nolabel='[COLOR red]No Eliminar[/COLOR]'):
            total = wiz.emptyfolder(ADDOND)
            wiz.LogNotify('[COLOR %s]Borrar carpetas vacias[/COLOR]' % COLOR1, '[COLOR %s]%s Carpeta(s) Borradoas[/COLOR]' % (COLOR2, total))
        else: wiz.LogNotify('[COLOR %s]Borrar carpetas vacias[/COLOR]' % COLOR1, '[COLOR %s]Cancelados![/COLOR]' % COLOR2)
    else:
        addon_data = os.path.join(USERDATA, 'addon_data', addon)
        if addon in EXCLUDES:
            wiz.LogNotify("[COLOR %s]Plugin protegido[/COLOR]" % COLOR1, "[COLOR %s]No esta permitido eliminarlo[/COLOR]" % COLOR2)
        elif os.path.exists(addon_data):
            if DIALOG.yesno(ADDONTITLE, '[COLOR %s]Quieres borrar de addon_data:[/COLOR]' % COLOR2, '[COLOR %s]%s[/COLOR]' % (COLOR1, addon), yeslabel='[COLOR springgreen]Eliminar Data[/COLOR]', nolabel='[COLOR red]No eliminar[/COLOR]'):
                wiz.cleanHouse(addon_data)
                try:
                    shutil.rmtree(addon_data)
                except:
                    wiz.log("Error deleting: %s" % addon_data)
            else:
                wiz.log('Addon data for %s was not removed' % addon)
    wiz.refresh()

def restoreit(type):
    if type == 'build':
        x = freshStart('restore')
        if x == False: wiz.LogNotify("[COLOR %s]%s[/COLOR]" % (COLOR1, ADDONTITLE), "[COLOR %s]Restauracion local Cancelada[/COLOR]" % COLOR2); return
    if not wiz.currSkin() in ['skin.confluence', 'skin.estuary']:
        wiz.skinToDefault('Restore Backup')
    wiz.restoreLocal(type)

def restoreextit(type):
    if type == 'build':
        x = freshStart('restore')
        if x == False: wiz.LogNotify("[COLOR %s]%s[/COLOR]" % (COLOR1, ADDONTITLE), "[COLOR %s]Restauracion externa Cancelada[/COLOR]" % COLOR2); return
    wiz.restoreExternal(type)

def buildInfo(name):
    if wiz.workingURL(BUILDFILE) == True:
        if wiz.checkBuild(name, 'url'):
            name, version, url, gui, kodi, theme, icon, fanart, preview, adult, info, description = wiz.checkBuild(name, 'all')
            adult = 'Yes' if adult.lower() == 'yes' else 'No'
            extend = False
            if not info == "http://":
                try:
                    tname, extracted, zipsize, skin, created, programs, video, music, picture, repos, scripts = wiz.checkInfo(info)
                    extend = True
                except:
                    extend = False
            if extend == True:
                msg  = "[COLOR %s]Nombre de la Build:[/COLOR] [COLOR %s]%s[/COLOR][CR][CR]" % (COLOR2, COLOR1, name)
                msg += "[COLOR %s]Version de la Build:[/COLOR] v[COLOR %s]%s[/COLOR][CR][CR]" % (COLOR2, COLOR1, version)
                msg += "[COLOR %s]Ultima actualizacion:[/COLOR] [COLOR %s]%s[/COLOR][CR][CR]" % (COLOR2, COLOR1, created)
                if not theme == "http://":
                    themecount = wiz.themeCount(name, False)
                    msg += "[COLOR %s]Build Theme(s):[/COLOR] [COLOR %s]%s[/COLOR][CR][CR]" % (COLOR2, COLOR1, ', '.join(themecount))
                msg += "[COLOR %s]Version Kodi:[/COLOR] [COLOR %s]%s[/COLOR][CR][CR]" % (COLOR2, COLOR1, kodi)
                msg += "[COLOR %s]Extracted Size:[/COLOR] [COLOR %s]%s[/COLOR][CR][CR]" % (COLOR2, COLOR1, wiz.convertSize(int(float(extracted))))
                msg += "[COLOR %s]Zip Size:[/COLOR] [COLOR %s]%s[/COLOR][CR][CR]" % (COLOR2, COLOR1, wiz.convertSize(int(float(zipsize))))
                msg += "[COLOR %s]Skin Name:[/COLOR] [COLOR %s]%s[/COLOR][CR][CR]" % (COLOR2, COLOR1, skin)
                msg += "[COLOR %s]Adult Content:[/COLOR] [COLOR %s]%s[/COLOR][CR][CR]" % (COLOR2, COLOR1, adult)
                msg += "[COLOR %s]Description:[/COLOR] [COLOR %s]%s[/COLOR][CR][CR]" % (COLOR2, COLOR1, description)
                msg += "[COLOR %s]Programs:[/COLOR] [COLOR %s]%s[/COLOR][CR][CR]" % (COLOR2, COLOR1, programs)
                msg += "[COLOR %s]Video:[/COLOR] [COLOR %s]%s[/COLOR][CR][CR]" % (COLOR2, COLOR1, video)
                msg += "[COLOR %s]Music:[/COLOR] [COLOR %s]%s[/COLOR][CR][CR]" % (COLOR2, COLOR1, music)
                msg += "[COLOR %s]Pictures:[/COLOR] [COLOR %s]%s[/COLOR][CR][CR]" % (COLOR2, COLOR1, picture)
                msg += "[COLOR %s]Repositories:[/COLOR] [COLOR %s]%s[/COLOR][CR][CR]" % (COLOR2, COLOR1, repos)
                msg += "[COLOR %s]Scripts:[/COLOR] [COLOR %s]%s[/COLOR]" % (COLOR2, COLOR1, scripts)
            else:
                msg  = "[COLOR %s]Build Name:[/COLOR] [COLOR %s]%s[/COLOR][CR]" % (COLOR2, COLOR1, name)
                msg += "[COLOR %s]Build Version:[/COLOR] [COLOR %s]%s[/COLOR][CR]" % (COLOR2, COLOR1, version)
                if not theme == "http://":
                    themecount = wiz.themeCount(name, False)
                    msg += "[COLOR %s]Build Theme(s):[/COLOR] [COLOR %s]%s[/COLOR][CR]" % (COLOR2, COLOR1, ', '.join(themecount))
                msg += "[COLOR %s]Kodi Version:[/COLOR] [COLOR %s]%s[/COLOR][CR]" % (COLOR2, COLOR1, kodi)
                msg += "[COLOR %s]Adult Content:[/COLOR] [COLOR %s]%s[/COLOR][CR]" % (COLOR2, COLOR1, adult)
                msg += "[COLOR %s]Description:[/COLOR] [COLOR %s]%s[/COLOR][CR]" % (COLOR2, COLOR1, description)

            wiz.TextBox(ADDONTITLE, msg)
        else: wiz.log("Invalid Build Name!")
    else: wiz.log("Build text file not working: %s" % WORKINGURL)

def buildVideo(name):
    if wiz.workingURL(BUILDFILE) == True:
        videofile = wiz.checkBuild(name, 'preview')
        if videofile and not videofile == 'http://': playVideo(videofile)
        else: wiz.log("[%s]Unable to find url for video preview" % name)
    else: wiz.log("Build text file not working: %s" % WORKINGURL)

def dependsList(plugin):
    addonxml = os.path.join(ADDONS, plugin, 'addon.xml')
    if os.path.exists(addonxml):
        source = open(addonxml,mode='r'); link = source.read(); source.close();
        match  = wiz.parseDOM(link, 'import', ret='addon')
        items  = []
        for depends in match:
            if not 'xbmc.python' in depends:
                items.append(depends)
        return items
    return []

def manageSaveData(do):
    if do == 'import':
        TEMP = os.path.join(ADDONDATA, 'temp')
        if not os.path.exists(TEMP): os.makedirs(TEMP)
        source = DIALOG.browse(1, '[COLOR %s]Select the location of the SaveData.zip[/COLOR]' % COLOR2, 'files', '.zip', False, False, HOME)
        if not source.endswith('.zip'):
            wiz.LogNotify("[COLOR %s]%s[/COLOR]" % (COLOR1, ADDONTITLE), "[COLOR %s]Import Data Error![/COLOR]" % (COLOR2))
            return
        source   = xbmc.translatePath(source)
        tempfile = xbmc.translatePath(os.path.join(MYBUILDS, 'SaveData.zip'))
        if not tempfile == source:
            goto = xbmcvfs.copy(source, tempfile)
        if extract.all(xbmc.translatePath(tempfile), TEMP) == False:
            wiz.log("Error trying to extract the zip file!")
            wiz.LogNotify("[COLOR %s]%s[/COLOR]" % (COLOR1, ADDONTITLE), "[COLOR %s]Import Data Error![/COLOR]" % (COLOR2))
            return
        trakt  = os.path.join(TEMP, 'trakt')
        login  = os.path.join(TEMP, 'login')
        debrid = os.path.join(TEMP, 'debrid')
        super  = os.path.join(TEMP, 'plugin.program.super.favourites')
        xmls   = os.path.join(TEMP, 'xmls')
        x = 0
        overwrite = DIALOG.yesno(ADDONTITLE, "[COLOR %s]Would you rather we overwrite all Save Data files or ask you for each file being imported?[/COLOR]" % (COLOR2), yeslabel="[COLOR springgreen]Overwrite All[/COLOR]", nolabel="[COLOR red]No Ask[/COLOR]")
        if os.path.exists(trakt):
            x += 1
            files = os.listdir(trakt)
            if not os.path.exists(traktit.TRAKTFOLD): os.makedirs(traktit.TRAKTFOLD)
            for item in files:
                old  = os.path.join(traktit.TRAKTFOLD, item)
                temp = os.path.join(trakt, item)
                if os.path.exists(old):
                    if overwrite == 1: os.remove(old)
                    else:
                        if not DIALOG.yesno(ADDONTITLE, "[COLOR %s]Would you like replace the current [COLOR %s]%s[/COLOR] file?" % (COLOR2, COLOR1, item), yeslabel="[COLOR springgreen]Yes Replace[/COLOR]", nolabel="[COLOR red]No Skip[/COLOR]"): continue
                        else: os.remove(old)
                shutil.copy(temp, old)
            traktit.importlist('all')
            traktit.traktIt('restore', 'all')
        if os.path.exists(login):
            x += 1
            files = os.listdir(login)
            if not os.path.exists(loginit.LOGINFOLD): os.makedirs(loginit.LOGINFOLD)
            for item in files:
                old  = os.path.join(loginit.LOGINFOLD, item)
                temp = os.path.join(login, item)
                if os.path.exists(old):
                    if overwrite == 1: os.remove(old)
                    else:
                        if not DIALOG.yesno(ADDONTITLE, "[COLOR %s]Would you like replace the current [COLOR %s]%s[/COLOR] file?" % (COLOR2, COLOR1, item), yeslabel="[COLOR springgreen]Yes Replace[/COLOR]", nolabel="[COLOR red]No Skip[/COLOR]"): continue
                        else: os.remove(old)
                shutil.copy(temp, old)
            loginit.importlist('all')
            loginit.loginIt('restore', 'all')
        if os.path.exists(debrid):
            x += 1
            files = os.listdir(debrid)
            if not os.path.exists(debridit.REALFOLD): os.makedirs(debridit.REALFOLD)
            for item in files:
                old  = os.path.join(debridit.REALFOLD, item)
                temp = os.path.join(debrid, item)
                if os.path.exists(old):
                    if overwrite == 1: os.remove(old)
                    else:
                        if not DIALOG.yesno(ADDONTITLE, "[COLOR %s]Would you like replace the current [COLOR %s]%s[/COLOR] file?" % (COLOR2, COLOR1, item), yeslabel="[COLOR springgreen]Yes Replace[/COLOR]", nolabel="[COLOR red]No Skip[/COLOR]"): continue
                        else: os.remove(old)
                shutil.copy(temp, old)
            debridit.importlist('all')
            debridit.debridIt('restore', 'all')
        if os.path.exists(xmls):
            x += 1
            files = ['advancedsettings.xml', 'sources.xml', 'favourites.xml', 'profiles.xml']
            for item in files:
                old = os.path.join(USERDATA, item)
                new = os.path.join(xmls, item)
                if not os.path.exists(new): continue
                if os.path.exists(old):
                    if not overwrite == 1:
                        if not DIALOG.yesno(ADDONTITLE, "[COLOR %s]Would you like replace the current [COLOR %s]%s[/COLOR] file?" % (COLOR2, COLOR1, item), yeslabel="[COLOR springgreen]Yes Replace[/COLOR]", nolabel="[COLOR red]No Skip[/COLOR]"): continue
                os.remove(old)
                shutil.copy(new, old)
        if os.path.exists(super):
            x += 1
            old = os.path.join(ADDOND, 'plugin.program.super.favourites')
            if os.path.exists(old):
                cont = DIALOG.yesno(ADDONTITLE, "[COLOR %s]Would you like replace the current [COLOR %s]Super Favourites[/COLOR] addon_data folder with the new one?" % (COLOR2, COLOR1), yeslabel="[COLOR springgreen]Yes Replace[/COLOR]", nolabel="[COLOR red]No Skip[/COLOR]")
            else: cont = 1
            if cont == 1:
                wiz.cleanHouse(old)
                wiz.removeFolder(old)
                xbmcvfs.copy(super, old)
        wiz.cleanHouse(TEMP)
        wiz.removeFolder(TEMP)
        if not tempfile == source:
            xbmcvfs.delete(tempfile)
        if x == 0: wiz.LogNotify("[COLOR %s]%s[/COLOR]" % (COLOR1, ADDONTITLE), "[COLOR %s]Save Data Import Failed[/COLOR]" % COLOR2)
        else: wiz.LogNotify("[COLOR %s]%s[/COLOR]" % (COLOR1, ADDONTITLE), "[COLOR %s]Save Data Import Complete[/COLOR]" % COLOR2)
    elif do == 'export':
        mybuilds = xbmc.translatePath(MYBUILDS)
        dir   = [traktit.TRAKTFOLD, debridit.REALFOLD, loginit.LOGINFOLD]
        xmls  = ['advancedsettings.xml', 'sources.xml', 'favourites.xml', 'profiles.xml']
        keepx = [KEEPADVANCED, KEEPSOURCES, KEEPFAVS, KEEPPROFILES]
        traktit.traktIt('update', 'all')
        loginit.loginIt('update', 'all')
        debridit.debridIt('update', 'all')
        source = DIALOG.browse(3, '[COLOR %s]Select where you wish to export the savedata zip?[/COLOR]' % COLOR2, 'files', '', False, True, HOME)
        source = xbmc.translatePath(source)
        tempzip = os.path.join(mybuilds, 'SaveData.zip')
        superfold = os.path.join(ADDOND, 'plugin.program.super.favourites')
        zipf = zipfile.ZipFile(tempzip, mode='w')
        for fold in dir:
            if os.path.exists(fold):
                files = os.listdir(fold)
                for file in files:
                    fn = os.path.join(fold, file)
                    zipf.write(fn, fn[len(ADDONDATA):], zipfile.ZIP_DEFLATED)
        if KEEPSUPER == 'true' and os.path.exists(superfold):
            for base, dirs, files in os.walk(superfold):
                for file in files:
                    fn = os.path.join(base, file)
                    zipf.write(fn, fn[len(ADDOND):], zipfile.ZIP_DEFLATED)
        for item in xmls:
            if keepx[xmls.index(item)] == 'true' and os.path.exists(os.path.join(USERDATA, item)):
                zipf.write(os.path.join(USERDATA, item), os.path.join('xmls', item), zipfile.ZIP_DEFLATED)
        zipf.close()
        if source == mybuilds:
            DIALOG.ok(ADDONTITLE, "[COLOR %s]Save data has been backed up to:[/COLOR]" % (COLOR2), "[COLOR %s]%s[/COLOR]" % (COLOR1, tempzip))
        else:
            try:
                xbmcvfs.copy(tempzip, os.path.join(source, 'SaveData.zip'))
                DIALOG.ok(ADDONTITLE, "[COLOR %s]Save data has been backed up to:[/COLOR]" % (COLOR2), "[COLOR %s]%s[/COLOR]" % (COLOR1, os.path.join(source, 'SaveData.zip')))
            except:
                DIALOG.ok(ADDONTITLE, "[COLOR %s]Save data has been backed up to:[/COLOR]" % (COLOR2), "[COLOR %s]%s[/COLOR]" % (COLOR1, tempzip))

###########################
###### Fresh Install ######
###########################

#############################
###DELETE CACHE##############
####THANKS GUYS @ NaN #######



##########################
### DEVELOPER MENU #######
##########################
def testnotify():
    url = wiz.workingURL(NOTIFICATION)
    if url == True:
        try:
            id, msg = wiz.splitNotify(NOTIFICATION)
            if id == False: wiz.LogNotify("[COLOR %s]%s[/COLOR]" % (COLOR1, ADDONTITLE), "[COLOR %s]Notification: Not Formated Correctly[/COLOR]" % COLOR2); return
            notify.notification(msg, True)
        except Exception, e:
            wiz.log("Error on Notifications Window: %s" % str(e), xbmc.LOGERROR)
    else: wiz.LogNotify("[COLOR %s]%s[/COLOR]" % (COLOR1, ADDONTITLE), "[COLOR %s]Invalid URL for Notification[/COLOR]" % COLOR2)

def testupdate():
    if BUILDNAME == "":
        notify.updateWindow()
    else:
        notify.updateWindow(BUILDNAME, BUILDVERSION, BUILDLATEST, wiz.checkBuild(BUILDNAME, 'icon'), wiz.checkBuild(BUILDNAME, 'fanart'))

def testfirst():
    notify.firstRun()

def testfirstRun():
    notify.firstRunSettings()

###########################
## Making the Directory####
###########################

def addDir(display, mode=None, name=None, url=None, menu=None, description=ADDONTITLE, overwrite=True, fanart=FANART, icon=ICON, themeit=None):
    u = sys.argv[0]
    if not mode == None: u += "?mode=%s" % urllib.quote_plus(mode)
    if not name == None: u += "&name="+urllib.quote_plus(name)
    if not url == None: u += "&url="+urllib.quote_plus(url)
    ok=True
    if themeit: display = themeit % display
    liz=xbmcgui.ListItem(display, iconImage="DefaultFolder.png", thumbnailImage=icon)
    liz.setInfo( type="Video", infoLabels={ "Title": display, "Plot": description} )
    liz.setProperty( "Fanart_Image", fanart )
    if not menu == None: liz.addContextMenuItems(menu, replaceItems=overwrite)
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
    return ok

def addFile(display, mode=None, name=None, url=None, menu=None, description=ADDONTITLE, overwrite=True, fanart=FANART, icon=ICON, themeit=None):
    u = sys.argv[0]
    if not mode == None: u += "?mode=%s" % urllib.quote_plus(mode)
    if not name == None: u += "&name="+urllib.quote_plus(name)
    if not url == None: u += "&url="+urllib.quote_plus(url)
    ok=True
    if themeit: display = themeit % display
    liz=xbmcgui.ListItem(display, iconImage="DefaultFolder.png", thumbnailImage=icon)
    liz.setInfo( type="Video", infoLabels={ "Title": display, "Plot": description} )
    liz.setProperty( "Fanart_Image", fanart )
    if not menu == None: liz.addContextMenuItems(menu, replaceItems=overwrite)
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
    return ok

def get_params():
    param=[]
    paramstring=sys.argv[2]
    if len(paramstring)>=2:
        params=sys.argv[2]
        cleanedparams=params.replace('?','')
        if (params[len(params)-1]=='/'):
            params=params[0:len(params)-2]
        pairsofparams=cleanedparams.split('&')
        param={}
        for i in range(len(pairsofparams)):
            splitparams={}
            splitparams=pairsofparams[i].split('=')
            if (len(splitparams))==2:
                param[splitparams[0]]=splitparams[1]

        return param

################KODI VERSION##########################################
def KodiVer():
    if KODIV >= 16.0 and KODIV <= 16.9:vername = 'Jarvis'
    elif KODIV >= 17.0 and KODIV <= 17.9:vername = 'Krypton'
    elif KODIV >= 18.0 and KODIV <= 18.9:vername = 'Leia'
    else: vername = "Unknown"
    return vername
######################################################################################################################
######################################################################################################################
params=get_params()
url=None
name=None
mode=None

try:     mode=urllib.unquote_plus(params["mode"])
except:  pass
try:     name=urllib.unquote_plus(params["name"])
except:  pass
try:     url=urllib.unquote_plus(params["url"])
except:  pass

wiz.log('[ Version : \'%s\' ] [ Mode : \'%s\' ] [ Name : \'%s\' ] [ Url : \'%s\' ]' % (VERSION, mode if not mode == '' else None, name, url))

def setView(content, viewType):
    if wiz.getS('auto-view')=='true':
        views = wiz.getS(viewType)
        if views == '50' and KODIV >= 17 and SKIN == 'skin.estuary': views = '55'
        if views == '500' and KODIV >= 17 and SKIN == 'skin.estuary': views = '50'
        wiz.ebi("Container.SetViewMode(%s)" %  views)

if   mode==None             : index()

elif mode=='wizardupdate'   : wiz.wizardUpdate()
elif mode=='builds'         : buildMenu()
elif mode=='viewbuild'      : viewBuild(name)
elif mode=='buildinfo'      : buildInfo(name)
elif mode=='buildpreview'   : buildVideo(name)
elif mode=='install'        : buildWizard(name, url)
elif mode=='theme'          : buildWizard(name, mode, url)
elif mode=='viewthirdparty' : viewThirdList(name)
elif mode=='installthird'   : thirdPartyInstall(name, url)
elif mode=='editthird'      : editThirdParty(name); wiz.refresh()

elif mode=='maint'          : maintMenu(name)
elif mode=='kodi17fix'      : wiz.kodi17Fix()
elif mode=='unknownsources' : skinSwitch.swapUS()
elif mode=='advancedsetting': advancedWindow(name)
elif mode=='autoadvanced'   : showAutoAdvanced(); wiz.refresh()
elif mode=='removeadvanced' : removeAdvanced(); wiz.refresh()
elif mode=='asciicheck'     : wiz.asciiCheck()
elif mode=='extractazip'    : wiz.extractAZip()
elif mode=='backupbuild'    : wiz.backUpOptions('build')
elif mode=='backupgui'      : wiz.backUpOptions('guifix')
elif mode=='backuptheme'    : wiz.backUpOptions('theme')
elif mode=='backupaddonpack': wiz.backUpOptions('addon pack')
elif mode=='backupaddon'    : wiz.backUpOptions('addondata')
elif mode=='oldThumbs'      : wiz.oldThumbs()
elif mode=='clearbackup'    : wiz.cleanupBackup()
elif mode=='convertpath'    : wiz.convertSpecial(HOME)
elif mode=='currentsettings': viewAdvanced()
elif mode=='fullclean'      : totalClean(); wiz.refresh()
elif mode=='clearcache'     : clearCache(); wiz.refresh()
elif mode=='clearpackages'  : wiz.clearPackages(); wiz.refresh()
elif mode=='clearcrash'     : wiz.clearCrash(); wiz.refresh()
elif mode=='clearthumb'     : clearThumb(); wiz.refresh()
elif mode=='cleararchive'   : clearArchive(); wiz.refresh()
elif mode=='checksources'   : wiz.checkSources(); wiz.refresh()
elif mode=='checkrepos'     : wiz.checkRepos(); wiz.refresh()
elif mode=='freshstart'     : freshStart()
elif mode=='forceupdate'    : wiz.forceUpdate()
elif mode=='forceprofile'   : wiz.reloadProfile(wiz.getInfo('System.ProfileName'))
elif mode=='forceclose'     : wiz.killxbmc()
elif mode=='forceskin'      : wiz.ebi("ReloadSkin()"); wiz.refresh()
elif mode=='hidepassword'   : wiz.hidePassword()
elif mode=='unhidepassword' : wiz.unhidePassword()
elif mode=='enableaddons'   : enableAddons()
elif mode=='toggleaddon'    : wiz.toggleAddon(name, url); wiz.refresh()
elif mode=='togglecache'    : toggleCache(name); wiz.refresh()
elif mode=='toggleadult'    : wiz.toggleAdult(); wiz.refresh()
elif mode=='changefeq'      : changeFeq(); wiz.refresh()
elif mode=='uploadlog'      : uploadLog.Main()
elif mode=='viewlog'        : LogViewer()
elif mode=='viewwizlog'     : LogViewer(WIZLOG)
elif mode=='viewerrorlog'   : errorChecking()
elif mode=='viewerrorlast'  : errorChecking(last=True)
elif mode=='clearwizlog'    : f = open(WIZLOG, 'w'); f.close(); wiz.LogNotify("[COLOR %s]%s[/COLOR]" % (COLOR1, ADDONTITLE), "[COLOR %s]Log del wizard limpiado[/COLOR]" % COLOR2)
elif mode=='purgedb'        : purgeDb()
elif mode=='fixaddonupdate' : fixUpdate()
elif mode=='removeaddons'   : removeAddonMenu()
elif mode=='removeaddon'    : removeAddon(name)
elif mode=='removeaddondata': removeAddonDataMenu()
elif mode=='removedata'     : removeAddonData(name)
elif mode=='resetaddon'     : total = wiz.cleanHouse(ADDONDATA, ignore=True); wiz.LogNotify("[COLOR %s]%s[/COLOR]" % (COLOR1, ADDONTITLE), "[COLOR %s]Addon_Data reset[/COLOR]" % COLOR2)
elif mode=='systeminfo'     : systemInfo()
elif mode=='restorezip'     : restoreit('build')
elif mode=='restoretheme'   : restoreit('theme')
elif mode=='restoregui'     : restoreit('gui')
elif mode=='restoreaddon'   : restoreit('addondata')
elif mode=='restoreextzip'  : restoreextit('build')
elif mode=='restoreextgui'  : restoreextit('gui')
elif mode=='restoreextaddon': restoreextit('addondata')
elif mode=='writeadvanced'  : writeAdvanced(name, url)
elif mode=='speedtest'      : net_tools()
elif mode=='runspeedtest'   : runSpeedTest(); wiz.refresh()
elif mode=='clearspeedtest' : clearSpeedTest(); wiz.refresh()
elif mode=='viewspeedtest'  : viewSpeedTest(name); wiz.refresh()
elif mode=="viewIP"         : viewIP();

elif mode=='speedtestM'     : speedTest()

elif mode=='apk'            : apkMenu(name, url)
elif mode=='apkscrape'      : apkScraper(name)
elif mode=='apkinstall'     : apkInstaller(name, url)
elif mode=='rominstall'     : romInstaller(name, url)

elif mode=='youtube'        : youtubeMenu(name, url)
elif mode=='viewVideo'      : playVideo(url)

elif mode=='addons'         : addonMenu(name, url)
elif mode=='addonpack'      : packInstaller(name, url)
elif mode=='skinpack'       : skinInstaller(name, url)
elif mode=='addoninstall'   : addonInstaller(name, url)

elif mode=='savedata'       : saveMenu()
elif mode=='togglesetting'  : wiz.setS(name, 'false' if wiz.getS(name) == 'true' else 'true'); wiz.refresh()
elif mode=='managedata'     : manageSaveData(name)
elif mode=='whitelist'      : wiz.whiteList(name)

elif mode=='trakt'          : traktMenu()
elif mode=='savetrakt'      : traktit.traktIt('update',      name)
elif mode=='restoretrakt'   : traktit.traktIt('restore',     name)
elif mode=='addontrakt'     : traktit.traktIt('clearaddon',  name)
elif mode=='cleartrakt'     : traktit.clearSaved(name)
elif mode=='authtrakt'      : traktit.activateTrakt(name); wiz.refresh()
elif mode=='updatetrakt'    : traktit.autoUpdate('all')
elif mode=='importtrakt'    : traktit.importlist(name); wiz.refresh()

elif mode=='realdebrid'     : realMenu()
elif mode=='savedebrid'     : debridit.debridIt('update',      name)
elif mode=='restoredebrid'  : debridit.debridIt('restore',     name)
elif mode=='addondebrid'    : debridit.debridIt('clearaddon',  name)
elif mode=='cleardebrid'    : debridit.clearSaved(name)
elif mode=='authdebrid'     : debridit.activateDebrid(name); wiz.refresh()
elif mode=='updatedebrid'   : debridit.autoUpdate('all')
elif mode=='importdebrid'   : debridit.importlist(name); wiz.refresh()

elif mode=='login'          : loginMenu()
elif mode=='savelogin'      : loginit.loginIt('update',      name)
elif mode=='restorelogin'   : loginit.loginIt('restore',     name)
elif mode=='addonlogin'     : loginit.loginIt('clearaddon',  name)
elif mode=='clearlogin'     : loginit.clearSaved(name)
elif mode=='authlogin'      : loginit.activateLogin(name); wiz.refresh()
elif mode=='updatelogin'    : loginit.autoUpdate('all')
elif mode=='importlogin'    : loginit.importlist(name); wiz.refresh()

elif mode=='contact'        : notify.contact(CONTACT)
elif mode=='settings'       : wiz.openS(name); wiz.refresh()
elif mode=='forcetext'      : wiz.forceText()
elif mode=='opensettings'   : id = eval(url.upper()+'ID')[name]['plugin']; addonid = wiz.addonId(id); addonid.openSettings(); wiz.refresh()

elif mode=='developer'      : developer()
elif mode=='converttext'    : wiz.convertText()
elif mode=='createqr'       : wiz.createQR()
elif mode=='testnotify'     : testnotify()
elif mode=='testupdate'     : testupdate()
elif mode=='testfirst'      : testfirst()
elif mode=='testfirstrun'   : testfirstRun()

xbmcplugin.endOfDirectory(int(sys.argv[1]))
