import os, xbmc, xbmcaddon

#########################################################
### Global Variables ####################################
#########################################################
PATH           = xbmcaddon.Addon().getAddonInfo('path')
ART            = os.path.join(PATH, 'resources', 'art')
#########################################################

#########################################################
### User Edit Variables #################################
#########################################################
ADDON_ID       = xbmcaddon.Addon().getAddonInfo('id')
ADDONTITLE     = '[COLOR red]CHOPO-WIZARD[/COLOR]'
BUILDERNAME    = 'WHIZ'
EXCLUDES       = [ADDON_ID, 'plugin.program.CHOPO-WIZARD']
# Enable/Disable the text file caching with 'Yes' or 'No' and age being how often it rechecks in minutes
CACHETEXT      = 'Yes'
CACHEAGE       = 30
# Text File with build info in it.
BUILDFILE      = 'https://pastebin.com/raw/xmPtenwb'
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
### Theming Menu Items ##################################
#########################################################

ICONBUILDS     = 'https://i.imgur.com/nlNeHIc.jpg'
ICONMAINT      = 'https://ih0.redbubble.net/image.382735244.0192/poster,840x830,f8f8f8-pad,750x1000,f8f8f8.u1.jpg'
ICONAPK        = 'https://i.imgur.com/RdOWl4p.jpg'
ICONADDONS     = 'https://i.imgur.com/RdOWl4p.jpg'
ICONYOUTUBE    = 'https://i.imgur.com/RdOWl4p.jpg'
ICONSAVE       = 'https://i.imgur.com/I6eo0eJ.jpg'
ICONCONTACT    = 'https://iwheelsurvive.com/wp-content/uploads/Telegram-logo.png'
ICONSETTINGS   = 'https://lh5.ggpht.com/gv992ET6R_InCoMXXwIbdRLJczqOHFfLxIeY-bN2nFq0r8MDe-y-cF2aWq6Qy9P_K-4=w300'
ICONSPEED      = 'https://i.imgur.com/RdOWl4p.jpg'
ICONTRAKT      = 'https://i.imgur.com/RdOWl4p.jpg'
ICONREAL       = 'https://i.imgur.com/RdOWl4p.jpg'
ICONLOGIN      = 'https://i.imgur.com/RdOWl4p.jpg'
# Hide the ====== seperators 'Yes' or 'No'
HIDESPACERS    = 'No'
# Character used in seperator
SPACER         = '='

# You can edit these however you want, just make sure that you have a %s in each of the
# THEME's so it grabs the text from the menu item
COLOR1         = 'red'
COLOR2         = 'white'
# Primary menu items   / %s is the menu item and is required
THEME1         = '[B][LOWERCASE][CAPITALIZE][COLOR white][COLOR '+COLOR1+'][COLOR blue][/B][B][COLOR white]%s[/COLOR][/CAPITALIZE][/LOWERCASE][/B]'
# Build Names          / %s is the menu item and is required
THEME2         = '[COLOR '+COLOR2+']%s[/COLOR]'
# Alternate items      / %s is the menu item and is required
THEME3         = '[LOWERCASE][CAPITALIZE][COLOR aquamarine]%s[/COLOR][/CAPITALIZE][/LOWERCASE]'
# Current Build Header / %s is the menu item and is required
THEME4         = '[LOWERCASE][CAPITALIZE][COLOR white]Version WIZARD Instalada: [COLOR aquamarine]%s[/COLOR][/CAPITALIZE][/LOWERCASE]'
# Current Theme Header / %s is the menu item and is required
THEME5         = '[LOWERCASE][CAPITALIZE][COLOR '+COLOR1+']Current Theme: [COLOR '+COLOR2+']%s[/COLOR][/CAPITALIZE][/LOWERCASE]'
# Current Theme Header / %s is the menu item and is required
THEME6         = '[LOWERCASE][CAPITALIZE][COLOR '+COLOR1+']Version CHOPO-WIZARD a instalar:[COLOR '+COLOR2+']%s[/COLOR][/CAPITALIZE][/LOWERCASE]'

# Message for Contact Page
# Enable 'Contact' menu item 'Yes' hide or 'No' dont hide
HIDECONTACT    = 'No'
# You can add \n to do line breaks
CONTACT        = '[B][LOWERCASE][CAPITALIZE][COLOR lime]\r\n\r\nGracias por utilizar CHOPO-WIZARD \r\n\r\nSi quieres ponerte en contacto unete ha nuestro grupo de telegram[COLOR yellow] https://t.me/tvchopo[/COLOR][/CAPITALIZE][/LOWERCASE][/B]'
#Images used for the contact window.  http:// for default icon and fanart
CONTACTICON    = 'https://i.imgur.com/RdOWl4p.jpg'
CONTACTFANART  = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQaSP9B5B2ljInyudorKEcpCR5DL0E5OQ7aRY0VYB-3DAx9QsGh'
#########################################################

#########################################################
### Auto Update                   #######################
###        For Those With No Repo #######################
#########################################################
# Enable Auto Update 'Yes' or 'No'
AUTOUPDATE     = 'No'
# Url to wizard version
WIZARDFILE     = 'https://i.imgur.com/RdOWl4p.jpg'
#########################################################

#########################################################
### Auto Install                 ########################
###        Repo If Not Installed ########################
#########################################################
# Enable Auto Install 'Yes' or 'No'
AUTOINSTALL    = 'No'
# Addon ID for the repository
REPOID         = 'repository.repoCHOPO-WIZARD'
# Url to Addons.xml file in your repo folder(this is so we can get the latest version)
REPOADDONXML   = 'https://raw.githubusercontent.com/elchocolate/repotvchopo/master/Repositorio/addons.xml'
# Url to folder zip is located in
REPOZIPURL     = 'https://raw.githubusercontent.com/elchocolate/repotvchopo/master/Repositorio/'
#########################################################

#########################################################
### Notification Window #################################
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
