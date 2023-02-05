import xbmcaddon

import os

#########################################################
#         Global Variables - DON'T EDIT!!!              #
#########################################################
ADDON_ID = xbmcaddon.Addon().getAddonInfo('id')
PATH = xbmcaddon.Addon().getAddonInfo('path')
ART = os.path.join(PATH, 'resources', 'media')
#########################################################

#########################################################
#        User Edit Variables                            #
#########################################################
ADDON_ID       = xbmcaddon.Addon().getAddonInfo('id')
ADDONTITLE     = '[COLOR red]INSTALADOR DE WIZARD[/COLOR]'
BUILDERNAME    = 'WHIZ'
EXCLUDES       = [ADDON_ID, 'plugin.program.CHOPO-WIZARD']
# Enable/Disable the text file caching with 'Yes' or 'No' and age being how often it rechecks in minutes
CACHETEXT      = 'Yes'
CACHEAGE       = 30
# Text File with build info in it.
BUILDFILE      = 'https://pastebin.com/raw/Scv0p5KF'
# How often you would like it to check for build updates in days
# 0 being every startup of kodi
UPDATECHECK    = 0
# Text File with apk info in it.  Leave as 'http://' to ignore
APKFILE        = 'https://'
# Text File with Youtube Videos urls.  Leave as 'http://' to ignore
YOUTUBETITLE   = ''
YOUTUBEFILE    = ''
# Text File for addon installer.  Leave as 'http://' to ignore
ADDONFILE      = 'https://'
# Text File for advanced settings.  Leave as 'http://' to ignore
ADVANCEDFILE   = 'https://'
#########################################################

#########################################################
#        Theming Menu Items                             #
#########################################################
# If you want to use locally stored icons the place them in the Resources/Art/
# folder of the wizard then use os.path.join(ART, 'imagename.png')
# do not place quotes around os.path.join
# Example:  ICONMAINT     = os.path.join(ART, 'mainticon.png')
#           ICONSETTINGS  = 'https://www.yourhost.com/repo/wizard/settings.png'
# Leave as http:// for default icon
ICONBUILDS = os.path.join(ART, 'builds.png')
ICONMAINT = os.path.join(ART, 'maintenance.png')
ICONSPEED = os.path.join(ART, 'speed.png')
ICONAPK = os.path.join(ART, 'apkinstaller.png')
ICONADDONS = os.path.join(ART, 'addoninstaller.png')
ICONYOUTUBE = os.path.join(ART, 'youtube.png')
ICONSAVE = os.path.join(ART, 'savedata.png')
ICONTRAKT = os.path.join(ART, 'keeptrakt.png')
ICONREAL = os.path.join(ART, 'keepdebrid.png')
ICONLOGIN = os.path.join(ART, 'keeplogin.png')
ICONCONTACT = os.path.join(ART, 'information.png')
ICONSETTINGS = os.path.join(ART, 'settings.png')
# Hide the section separators 'Yes' or 'No'
HIDESPACERS = 'No'
# Character used in separator
SPACER = '='

# You can edit these however you want, just make sure that you have a %s in each of the
# THEME's so it grabs the text from the menu item
COLOR1 = 'gold'
COLOR2 = 'white'
# Primary menu items   / {0} is the menu item and is required
THEME1 = u'[COLOR {color1}][I][/I][/COLOR] [COLOR {color2}]{{}}[/COLOR]'.format(color1=COLOR1, color2=COLOR2)
# Build Names          / {0} is the menu item and is required
THEME2 = u'[COLOR {color1}]{{}}[/COLOR]'.format(color1=COLOR1)
# Alternate items      / {0} is the menu item and is required
THEME3 = u'[COLOR {color1}]{{}}[/COLOR]'.format(color1=COLOR1)
# Current Build Header / {0} is the menu item and is required
THEME4 = u'[COLOR {color1}]WIZARD INSTALADO:[/COLOR] [COLOR {color2}]{{}}[/COLOR]'.format(color1=COLOR1, color2=COLOR2)
# Current Theme Header / {0} is the menu item and is required
THEME5 = u'[COLOR {color1}]Current Theme:[/COLOR] [COLOR {color2}]{{}}[/COLOR]'.format(color1=COLOR1, color2=COLOR2)

# Message for Contact Page
# Enable 'Contact' menu item 'Yes' hide or 'No' dont hide
HIDECONTACT = 'No'
# You can add \n to do line breaks
CONTACT        = '[B][LOWERCASE][CAPITALIZE][COLOR lime]\r\n\r\nGracias por utilizar CHOPO-WIZARD \r\n\r\nSi quieres ponerte en contacto unete ha nuestro grupo de telegram[COLOR yellow] @tvchopo[/COLOR][/CAPITALIZE][/LOWERCASE][/B]'
# Images used for the contact window.  http:// for default icon and fanart
CONTACTICON    = 'https://i.imgur.com/RdOWl4p.jpg'
CONTACTFANART  = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQaSP9B5B2ljInyudorKEcpCR5DL0E5OQ7aRY0VYB-3DAx9QsGh'
#########################################################

#########################################################
#        Auto Update For Those With No Repo             #
#########################################################
# Enable Auto Update 'Yes' or 'No'
AUTOUPDATE = 'Yes'
#########################################################
WIZARDFILE     = 'https://i.imgur.com/RdOWl4p.jpg'
#########################################################
#        Auto Install Repo If Not Installed             #
#########################################################
# Enable Auto Install 'Yes' or 'No'
AUTOINSTALL = 'Yes'
# Addon ID for the repository
REPOID = 'repository.chopowizard'
# Url to Addons.xml file in your repo folder(this is so we can get the latest version)
REPOID         = 'repository.repoCHOPO-WIZARD'
# Url to Addons.xml file in your repo folder(this is so we can get the latest version)
REPOADDONXML   = 'https://raw.githubusercontent.com/elchocolate/repotvchopo/master/Repositorio/addons.xml'
# Url to folder zip is located in
REPOZIPURL     = 'https://raw.githubusercontent.com/elchocolate/repotvchopo/master/Repositorio/'
#########################################################

#########################################################
#        Notification Window                            #
#########################################################
# Enable Notification screen Yes or No
ENABLE         = 'Yes'
# Url to notification file
NOTIFICATION   = 'https://pastebin.com/raw/gGYV35HH'
# Use either 'Text' or 'Image'
HEADERTYPE     = 'Image'
# Font size of header
FONTHEADER     = 'Font14'
HEADERMESSAGE  = 'CHOPO-WIZARD'
# url to image if using Image 424x180
HEADERIMAGE    = 'http://'
# Font for Notification Window
FONTSETTINGS   = 'Font13'
# Background for Notification Window
BACKGROUND     = 'https://i.imgur.com/RdOWl4p.jpg'
#########################################################
