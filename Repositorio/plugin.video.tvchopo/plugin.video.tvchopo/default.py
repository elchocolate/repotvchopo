# -*- coding: utf-8 -*-
import urllib
import urllib2
import re
import os
import xbmcplugin
import xbmcgui
import xbmcaddon
import xbmcvfs
import traceback
import cookielib , base64
from BeautifulSoup import BeautifulStoneSoup , BeautifulSoup , BeautifulSOAP
oo000 = None
try :
 from xml . sax . saxutils import escape
except : traceback . print_exc ( )
try :
 import json
except :
 import simplejson as json
import SimpleDownloader as downloader
import time
if 9 - 9: Ii . o0o00Oo0O - iI11I1II1I1I
try :
 import ssl
 ssl . _create_default_https_context = ssl . _create_unverified_context
except :
 pass
 if 71 - 71: ii
import zipfile
if 11 - 11: ii1I - ooO0OO000o
def ii11i ( _in , _out ) :
 try :
  oOooOoO0Oo0O = zipfile . ZipFile ( _in , 'r' )
  oOooOoO0Oo0O . extractall ( _out )
 except Exception , iI1 :
  print str ( iI1 )
  return False
  if 43 - 43: I11i11Ii
 return True
 if 65 - 65: i1iIi11iIIi1I
 if 78 - 78: i11ii11iIi11i . oOoO0oo0OOOo + IiiI / Iii1ii1II11i
def iI111iI ( ) :
 print "SportsDevil"
 IiII = "http://repo.adryanlist.org/plugin.video.SportsDevil-2016-12-31_JX.zip"
 iI1Ii11111iIi = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) ) . decode ( "utf-8" )
 i1i1II = os . path . join ( iI1Ii11111iIi , 'packages' , 'spd.zip' )
 if 96 - 96: o0OO0 - Oo0ooO0oo0oO . I1i1iI1i - o00ooo0 / o00 * Oo0oO0ooo
 urllib . urlretrieve ( IiII , i1i1II )
 ii11i ( i1i1II , iI1Ii11111iIi )
 if 56 - 56: ooO00oOoo - O0OOo
 try :
  os . remove ( i1i1II )
 except :
  pass
  if 8 - 8: IiiI * Iii1ii1II11i * iI11I1II1I1I . Oo0oO0ooo / Oo0oO0ooo % Oo0oO0ooo
 xbmc . executebuiltin ( "UpdateLocalAddons" )
 xbmc . executebuiltin ( "UpdateAddonRepos" )
 if 22 - 22: o00ooo0 . Oo0oO0ooo
 if 41 - 41: ooO00oOoo . O0OOo * Oo0oO0ooo % Ii
def o000o0o00o0Oo ( ) :
 if os . path . exists ( os . path . join ( xbmc . translatePath ( "special://home/addons/" ) . decode ( "utf-8" ) , 'repository.dss' ) ) :
  return
  if 80 - 80: ii . I11i11Ii
 IiII = "http://repo.adryanlist.org/repository.shani-2.8.zip"
 iI1Ii11111iIi = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) ) . decode ( "utf-8" )
 i1i1II = os . path . join ( iI1Ii11111iIi , 'packages' , 'isr.zip' )
 if 87 - 87: o0OO0 / O0OOo + ooO00oOoo - O0OOo . O0OOo / ooO0OO000o
 urllib . urlretrieve ( IiII , i1i1II )
 ii11i ( i1i1II , iI1Ii11111iIi )
 if 11 - 11: I11i11Ii % IiiI - i1iIi11iIIi1I
 try :
  os . remove ( i1i1II )
 except :
  pass
  if 58 - 58: Ii % ooO00oOoo
 xbmc . executebuiltin ( "UpdateLocalAddons" )
 xbmc . executebuiltin ( "UpdateAddonRepos" )
 if 54 - 54: Oo0ooO0oo0oO % o0o00Oo0O + I11i11Ii - o00 / I1i1iI1i
 if 31 - 31: i11ii11iIi11i + ooO0OO000o
def i11IiIiiIIIII ( ) :
 if os . path . exists ( os . path . join ( xbmc . translatePath ( "special://home/addons/" ) . decode ( "utf-8" ) , 'repository.adryan' ) ) :
  return
  if 22 - 22: o00ooo0 * o0o00Oo0O / IiiI
 IiII = "http://repo.adryanlist.org/repository.adryan-1.0.zip"
 iI1Ii11111iIi = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) ) . decode ( "utf-8" )
 i1i1II = os . path . join ( iI1Ii11111iIi , 'packages' , 'isr.zip' )
 if 64 - 64: o00ooo0 % ii1I % ii
 urllib . urlretrieve ( IiII , i1i1II )
 ii11i ( i1i1II , iI1Ii11111iIi )
 if 3 - 3: o00 + o0o00Oo0O
 try :
  os . remove ( i1i1II )
 except :
  pass
  if 42 - 42: Oo0ooO0oo0oO / ii1I + Ii - o00ooo0
 xbmc . executebuiltin ( "UpdateLocalAddons" )
 xbmc . executebuiltin ( "UpdateAddonRepos" )
 if 78 - 78: i11ii11iIi11i
 if 18 - 18: o0o00Oo0O - o00 / o00 + O0OOo % O0OOo - Oo0oO0ooo
i11IiIiiIIIII ( )
O0O00Ooo = False
OOoooooO = False
i1iIIIiI1I = [ '180upload.com' , 'allmyvideos.net' , 'bestreams.net' , 'clicknupload.com' , 'cloudzilla.to' , 'movshare.net' , 'novamov.com' , 'nowvideo.sx' , 'videoweed.es' , 'daclips.in' , 'datemule.com' , 'fastvideo.in' , 'faststream.in' , 'filehoot.com' , 'filenuke.com' , 'sharesix.com' , 'plus.google.com' , 'picasaweb.google.com' , 'gorillavid.com' , 'gorillavid.in' , 'grifthost.com' , 'hugefiles.net' , 'ipithos.to' , 'ishared.eu' , 'kingfiles.net' , 'mail.ru' , 'my.mail.ru' , 'videoapi.my.mail.ru' , 'mightyupload.com' , 'mooshare.biz' , 'movdivx.com' , 'movpod.net' , 'movpod.in' , 'movreel.com' , 'mrfile.me' , 'nosvideo.com' , 'openload.io' , 'played.to' , 'bitshare.com' , 'filefactory.com' , 'k2s.cc' , 'oboom.com' , 'rapidgator.net' , 'primeshare.tv' , 'bitshare.com' , 'filefactory.com' , 'k2s.cc' , 'oboom.com' , 'rapidgator.net' , 'sharerepo.com' , 'stagevu.com' , 'streamcloud.eu' , 'streamin.to' , 'thefile.me' , 'thevideo.me' , 'tusfiles.net' , 'uploadc.com' , 'zalaa.com' , 'uploadrocket.net' , 'uptobox.com' , 'v-vids.com' , 'veehd.com' , 'vidbull.com' , 'videomega.tv' , 'vidplay.net' , 'vidspot.net' , 'vidto.me' , 'vidzi.tv' , 'vimeo.com' , 'vk.com' , 'vodlocker.com' , 'xfileload.com' , 'xvidstage.com' , 'zettahost.tv' ]
OOoO000O0OO = [ 'plugin.video.dramasonline' , 'plugin.video.f4mTester' , 'plugin.video.shahidmbcnet' , 'plugin.video.SportsDevil' , 'plugin.stream.vaughnlive.tv' , 'plugin.video.ZemTV-shani' ]
if 23 - 23: Ii + I11i11Ii
class oOo ( urllib2 . HTTPErrorProcessor ) :
 def http_response ( self , request , response ) :
  return response
 https_response = http_response
 if 63 - 63: i1iIi11iIIi1I
ooOoOoo0O = False ;
if ooOoOoo0O :
 if 76 - 76: o0o00Oo0O / IiiI . I11i11Ii * o00ooo0 - Oo0ooO0oo0oO
 if 76 - 76: Ii / iI11I1II1I1I . Iii1ii1II11i % Oo0ooO0oo0oO / ii % o0OO0
 try :
  import pysrc . pydevd as pydevd
  if 75 - 75: o00
  pydevd . settrace ( 'localhost' , stdoutToServer = True , stderrToServer = True )
 except ImportError :
  sys . stderr . write ( "Error: " +
 "You must add org.python.pydev.debug.pysrc to your PYTHONPATH." )
  sys . exit ( 1 )
  if 97 - 97: Ii
  if 32 - 32: i1iIi11iIIi1I * o0o00Oo0O % o0OO0 % o00ooo0 . Oo0oO0ooo
o0OOOOO00o0O0 = xbmcaddon . Addon ( 'plugin.video.tvchopo' )
o0o0OOO0o0 = o0OOOOO00o0O0 . getAddonInfo ( 'version' )
ooOOOo0oo0O0 = xbmc . translatePath ( o0OOOOO00o0O0 . getAddonInfo ( 'profile' ) . decode ( 'utf-8' ) )
o0 = xbmc . translatePath ( o0OOOOO00o0O0 . getAddonInfo ( 'path' ) . decode ( 'utf-8' ) )
I11II1i = os . path . join ( ooOOOo0oo0O0 , 'favorites' )
IIIII = os . path . join ( ooOOOo0oo0O0 , 'history' )
ooooooO0oo = os . path . join ( ooOOOo0oo0O0 , 'list_revision' )
IIiiiiiiIi1I1 = os . path . join ( o0 , 'icon.png' )
I1IIIii = os . path . join ( o0 , 'fanart.jpg' )
oOoOooOo0o0 = os . path . join ( ooOOOo0oo0O0 , 'source_file' )
OOOO = ooOOOo0oo0O0
if 87 - 87: o0OO0 / I1i1iI1i - ii1I * Oo0ooO0oo0oO / ii . o0o00Oo0O
iii11I111 = os . path . join ( ooOOOo0oo0O0 , 'LivewebTV' )
downloader = downloader . SimpleDownloader ( )
OOOO00ooo0Ooo = o0OOOOO00o0O0 . getSetting ( 'debug' )
if os . path . exists ( I11II1i ) == True :
 OOOooOooo00O0 = open ( I11II1i ) . read ( )
else : OOOooOooo00O0 = [ ]
if 100 - 100: Ii / oOoO0oo0OOOo % ooO00oOoo - Iii1ii1II11i / o0OO0
ii11i1 = [ { "url" : "http://bit.ly/2Bl86eR$$LSProEncKey=tvchopo$$" , "fanart" : "http://i.imgur.com/p5pDbCT.jpg" } ]
if 29 - 29: Iii1ii1II11i % I11i11Ii + O0OOo / IiiI + Oo0ooO0oo0oO * IiiI
if 42 - 42: o00ooo0 + o0OO0
if 76 - 76: ooO00oOoo - i11ii11iIi11i
if 70 - 70: O0OOo
if 61 - 61: Iii1ii1II11i . Iii1ii1II11i
if 10 - 10: oOoO0oo0OOOo * o00 . I1i1iI1i + ooO0OO000o - O0OOo * ii1I
if 56 - 56: IiiI * Oo0oO0ooo * ooO0OO000o
def oO0ooO0OoOOOO ( string ) :
 if OOOO00ooo0Ooo == 'true' :
  xbmc . log ( "[addon.tvchopo-%s]: %s" % ( o0o0OOO0o0 , string ) )
  if 46 - 46: Oo0ooO0oo0oO / Iii1ii1II11i
  if 24 - 24: I1i1iI1i . o00 % Oo0ooO0oo0oO + O0OOo % oOoO0oo0OOOo
def I11III1II ( url , headers = None ) :
 try :
  if headers is None :
   headers = { 'User-agent' : 'THEKING' }
   if 16 - 16: I11i11Ii * o0OO0 % Oo0oO0ooo
   if 86 - 86: I11i11Ii + o00ooo0 % Ii * o0OO0 . O0OOo * I1i1iI1i
   if 44 - 44: o0OO0
   if 88 - 88: ooO00oOoo % o00ooo0 . ooO0OO000o
   if 38 - 38: IiiI
   if 57 - 57: o0o00Oo0O / o0OO0 * ooO00oOoo / oOoO0oo0OOOo . ooO0OO000o
   if 26 - 26: o00
   if 91 - 91: i11ii11iIi11i . Iii1ii1II11i + i11ii11iIi11i - o00 / ii
   if 39 - 39: Iii1ii1II11i / O0OOo - ooO0OO000o
   if 98 - 98: Iii1ii1II11i / I1i1iI1i % o0OO0 . oOoO0oo0OOOo
   if 91 - 91: o0OO0 % i1iIi11iIIi1I
   if 64 - 64: I1i1iI1i % o00 - ooO00oOoo - o0OO0
  if '|' in url :
   url , i1ii1iiI = url . split ( '|' )
   i1ii1iiI = i1ii1iiI . split ( '&' )
   if 98 - 98: o00 * o00 / o00 + I1i1iI1i
   for ii111111I1iII in i1ii1iiI :
    if len ( ii111111I1iII . split ( '=' ) ) == 2 :
     O00ooo0O0 , i1iIi1iIi1i = ii111111I1iII . split ( '=' )
    else :
     I1I1iIiII1 = ii111111I1iII . split ( '=' )
     O00ooo0O0 = I1I1iIiII1 [ 0 ]
     i1iIi1iIi1i = '=' . join ( I1I1iIiII1 [ 1 : ] )
     if 4 - 4: O0OOo + o0o00Oo0O * Oo0ooO0oo0oO
    print O00ooo0O0 , i1iIi1iIi1i
    headers [ O00ooo0O0 ] = i1iIi1iIi1i
    if 55 - 55: i1iIi11iIIi1I + iI11I1II1I1I / oOoO0oo0OOOo * o0OO0 - Ii - o00ooo0
  ii1ii1ii = urllib2 . Request ( url , None , headers )
  oooooOoo0ooo = urllib2 . urlopen ( ii1ii1ii )
  I1I1IiI1 = oooooOoo0ooo . read ( )
  oooooOoo0ooo . close ( )
  return I1I1IiI1
 except urllib2 . URLError , iI1 :
  oO0ooO0OoOOOO ( 'URL: ' + url )
  if hasattr ( iI1 , 'code' ) :
   oO0ooO0OoOOOO ( 'We failed with error code - %s.' % iI1 . code )
   xbmc . executebuiltin ( "XBMC.Notification(tvchopo,We failed with error code - " + str ( iI1 . code ) + ",10000," + IIiiiiiiIi1I1 + ")" )
  elif hasattr ( iI1 , 'reason' ) :
   oO0ooO0OoOOOO ( 'We failed to reach a server.' )
   oO0ooO0OoOOOO ( 'Reason: %s' % iI1 . reason )
   xbmc . executebuiltin ( "XBMC.Notification(tvchopo,We failed to reach a server. - " + str ( iI1 . reason ) + ",10000," + IIiiiiiiIi1I1 + ")" )
   if 5 - 5: IiiI * O0OOo + oOoO0oo0OOOo . Oo0ooO0oo0oO + oOoO0oo0OOOo
def oO ( ) :
 try :
  if os . path . exists ( I11II1i ) == True :
   OOOooOooo00O0 = open ( I11II1i ) . read ( )
   if OOOooOooo00O0 == "[]" :
    os . remove ( I11II1i )
   else :
    iIi1IIIi1 ( '[COLOR yellow][B]- MIS CANALES FAVORITOS[/COLOR][/B]' , 'url' , 4 , os . path . join ( o0 , 'resources' , 'favorite.png' ) , I1IIIii , '' , '' , '' , '' )
    if 86 - 86: I1i1iI1i % oOoO0oo0OOOo / I11i11Ii / oOoO0oo0OOOo
    if 42 - 42: i11ii11iIi11i
    if 67 - 67: ooO00oOoo . o00 . o0o00Oo0O
    if 10 - 10: Iii1ii1II11i % Iii1ii1II11i - iI11I1II1I1I / Oo0ooO0oo0oO + o00ooo0
    if 87 - 87: o0OO0 * Iii1ii1II11i + Oo0ooO0oo0oO / iI11I1II1I1I / o00
    if 37 - 37: o00 - O0OOo * o0OO0 % Ii - ooO00oOoo
    if 83 - 83: I1i1iI1i / I11i11Ii
    if 34 - 34: Oo0oO0ooo
    if 57 - 57: o0OO0 . I1i1iI1i . ii1I
    if 42 - 42: I1i1iI1i + Iii1ii1II11i % o0o00Oo0O
    if 6 - 6: o0OO0
    iIi1IIIi1 ( '' , '' , 100 , '' , I1IIIii , '' , '' , '' , '' )
    if 68 - 68: oOoO0oo0OOOo - i11ii11iIi11i
    if 28 - 28: i11ii11iIi11i . Oo0ooO0oo0oO / Oo0ooO0oo0oO + i1iIi11iIIi1I . Iii1ii1II11i
    if 1 - 1: iI11I1II1I1I / ooO0OO000o
    if 33 - 33: I1i1iI1i
    if 18 - 18: IiiI % o00 * o0o00Oo0O
    if 87 - 87: Ii
    if 93 - 93: Iii1ii1II11i - i11ii11iIi11i % Ii . o00 / o00 - ooO00oOoo
    if 9 - 9: Iii1ii1II11i / i1iIi11iIIi1I - I11i11Ii / ii / iI11I1II1I1I - IiiI
    if 91 - 91: o00 % ii1I % iI11I1II1I1I
    if 20 - 20: Oo0ooO0oo0oO % o00ooo0 / o00ooo0 + o00ooo0
    if 45 - 45: o0OO0 - Oo0oO0ooo - ii - i11ii11iIi11i . ooO0OO000o / o0o00Oo0O
  oo0o00O = ii11i1
  if 51 - 51: o00ooo0 - i11ii11iIi11i * o00
  if len ( oo0o00O ) > 1 :
   for oooo0O0 in oo0o00O :
    try :
     if 51 - 51: i11ii11iIi11i / i11ii11iIi11i
     if isinstance ( oooo0O0 , list ) :
      iIi1IIIi1 ( oooo0O0 [ 0 ] . encode ( 'utf-8' ) , oooo0O0 [ 1 ] . encode ( 'utf-8' ) , 1 , IIiiiiiiIi1I1 , I1IIIii , '' , '' , '' , '' , 'source' )
     else :
      ooOOO0 = IIiiiiiiIi1I1
      o0o = I1IIIii
      O0OOoO00OO0o = ''
      I1111IIIIIi = ''
      credits = ''
      Iiii1i1 = ''
      if oooo0O0 . has_key ( 'thumbnail' ) :
       ooOOO0 = oooo0O0 [ 'thumbnail' ]
      if oooo0O0 . has_key ( 'fanart' ) :
       o0o = oooo0O0 [ 'fanart' ]
      if oooo0O0 . has_key ( 'description' ) :
       O0OOoO00OO0o = oooo0O0 [ 'description' ]
      if oooo0O0 . has_key ( 'date' ) :
       I1111IIIIIi = oooo0O0 [ 'date' ]
      if oooo0O0 . has_key ( 'genre' ) :
       Iiii1i1 = oooo0O0 [ 'genre' ]
      if oooo0O0 . has_key ( 'credits' ) :
       credits = oooo0O0 [ 'credits' ]
      iIi1IIIi1 ( oooo0O0 [ 'title' ] . encode ( 'utf-8' ) , oooo0O0 [ 'url' ] . encode ( 'utf-8' ) , 1 , ooOOO0 , o0o , O0OOoO00OO0o , Iiii1i1 , I1111IIIIIi , credits , 'source' )
    except : traceback . print_exc ( )
  else :
   if len ( oo0o00O ) == 1 :
    if isinstance ( oo0o00O [ 0 ] , list ) :
     OO ( oo0o00O [ 0 ] [ 1 ] . encode ( 'utf-8' ) , I1IIIii )
    else :
     OO ( oo0o00O [ 0 ] [ 'url' ] , oo0o00O [ 0 ] [ 'fanart' ] )
 except : traceback . print_exc ( )
 if 77 - 77: i1iIi11iIIi1I
def I1iII1iIi1I ( url = None ) :
 if url is None :
  if not o0OOOOO00o0O0 . getSetting ( "new_file_source" ) == "" :
   oO0O00OoOO0 = o0OOOOO00o0O0 . getSetting ( 'new_file_source' ) . decode ( 'utf-8' )
  elif not o0OOOOO00o0O0 . getSetting ( "new_url_source" ) == "" :
   oO0O00OoOO0 = o0OOOOO00o0O0 . getSetting ( 'new_url_source' ) . decode ( 'utf-8' )
 else :
  oO0O00OoOO0 = url
 if oO0O00OoOO0 == '' or oO0O00OoOO0 is None :
  return
 oO0ooO0OoOOOO ( 'Adding New Source: ' + oO0O00OoOO0 . encode ( 'utf-8' ) )
 if 82 - 82: ooO0OO000o . Oo0oO0ooo - iI11I1II1I1I - Oo0oO0ooo * ooO0OO000o
 ooO0oOOooOo0 = None
 if 38 - 38: ooO00oOoo
 I1I1IiI1 = Ooo00o0Oooo ( oO0O00OoOO0 )
 if 84 - 84: IiiI % ooO0OO000o . Ii / i11ii11iIi11i
 if isinstance ( I1I1IiI1 , BeautifulSOAP ) :
  if I1I1IiI1 . find ( 'channels_info' ) :
   ooO0oOOooOo0 = I1I1IiI1 . channels_info
  elif I1I1IiI1 . find ( 'items_info' ) :
   ooO0oOOooOo0 = I1I1IiI1 . items_info
 if ooO0oOOooOo0 :
  o0O = { }
  o0O [ 'url' ] = oO0O00OoOO0
  try : o0O [ 'title' ] = ooO0oOOooOo0 . title . string
  except : pass
  try : o0O [ 'thumbnail' ] = ooO0oOOooOo0 . thumbnail . string
  except : pass
  try : o0O [ 'fanart' ] = ooO0oOOooOo0 . fanart . string
  except : pass
  try : o0O [ 'genre' ] = ooO0oOOooOo0 . genre . string
  except : pass
  try : o0O [ 'description' ] = ooO0oOOooOo0 . description . string
  except : pass
  try : o0O [ 'date' ] = ooO0oOOooOo0 . date . string
  except : pass
  try : o0O [ 'credits' ] = ooO0oOOooOo0 . credits . string
  except : pass
 else :
  if '/' in oO0O00OoOO0 :
   IiIIii1iII1II = oO0O00OoOO0 . split ( '/' ) [ - 1 ] . split ( '.' ) [ 0 ]
  if '\\' in oO0O00OoOO0 :
   IiIIii1iII1II = oO0O00OoOO0 . split ( '\\' ) [ - 1 ] . split ( '.' ) [ 0 ]
  if '%' in IiIIii1iII1II :
   IiIIii1iII1II = urllib . unquote_plus ( IiIIii1iII1II )
  Iii1I1I11iiI1 = xbmc . Keyboard ( IiIIii1iII1II , 'Displayed Name, Rename?' )
  Iii1I1I11iiI1 . doModal ( )
  if ( Iii1I1I11iiI1 . isConfirmed ( ) == False ) :
   return
  I1I1i1I = Iii1I1I11iiI1 . getText ( )
  if len ( I1I1i1I ) == 0 :
   return
  o0O = { }
  o0O [ 'title' ] = I1I1i1I
  o0O [ 'url' ] = oO0O00OoOO0
  o0O [ 'fanart' ] = o0o
  if 30 - 30: ii
 if os . path . exists ( oOoOooOo0o0 ) == False :
  I1Ii1iI1 = [ ]
  I1Ii1iI1 . append ( o0O )
  oO0 = open ( oOoOooOo0o0 , "w" )
  oO0 . write ( json . dumps ( I1Ii1iI1 ) )
  oO0 . close ( )
 else :
  oo0o00O = json . loads ( open ( oOoOooOo0o0 , "r" ) . read ( ) )
  oo0o00O . append ( o0O )
  oO0 = open ( oOoOooOo0o0 , "w" )
  oO0 . write ( json . dumps ( oo0o00O ) )
  oO0 . close ( )
 o0OOOOO00o0O0 . setSetting ( 'new_url_source' , "" )
 o0OOOOO00o0O0 . setSetting ( 'new_file_source' , "" )
 xbmc . executebuiltin ( "XBMC.Notification(tvchopo,New source added.,5000," + IIiiiiiiIi1I1 + ")" )
 if not url is None :
  if 'xbmcplus.xb.funpic.de' in url :
   xbmc . executebuiltin ( "XBMC.Container.Update(%s?mode=14,replace)" % sys . argv [ 0 ] )
  elif 'community-links' in url :
   xbmc . executebuiltin ( "XBMC.Container.Update(%s?mode=10,replace)" % sys . argv [ 0 ] )
 else : o0OOOOO00o0O0 . openSettings ( )
 if 75 - 75: O0OOo + oOoO0oo0OOOo + IiiI * I1i1iI1i % o0OO0 . o00
def oOI1Ii1I1 ( name ) :
 oo0o00O = json . loads ( open ( oOoOooOo0o0 , "r" ) . read ( ) )
 for IiII111iI1ii1 in range ( len ( oo0o00O ) ) :
  if isinstance ( oo0o00O [ IiII111iI1ii1 ] , list ) :
   if oo0o00O [ IiII111iI1ii1 ] [ 0 ] == name :
    del oo0o00O [ IiII111iI1ii1 ]
    oO0 = open ( oOoOooOo0o0 , "w" )
    oO0 . write ( json . dumps ( oo0o00O ) )
    oO0 . close ( )
    break
  else :
   if oo0o00O [ IiII111iI1ii1 ] [ 'title' ] == name :
    del oo0o00O [ IiII111iI1ii1 ]
    oO0 = open ( oOoOooOo0o0 , "w" )
    oO0 . write ( json . dumps ( oo0o00O ) )
    oO0 . close ( )
    break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 37 - 37: o0OO0 - ooO00oOoo % i1iIi11iIIi1I
def OOOoo0OO ( url , browse = False ) :
 if url is None :
  url = 'http://xbmcplus.xb.funpic.de/www-data/filesystem/'
 oO0o0 = BeautifulSoup ( I11III1II ( url ) , convertEntities = BeautifulSoup . HTML_ENTITIES )
 for oooo0O0 in oO0o0 ( 'a' ) :
  iI1Ii11iIiI1 = oooo0O0 [ 'href' ]
  if not iI1Ii11iIiI1 . startswith ( '?' ) :
   OO0Oooo0oOO0O = oooo0O0 . string
   if OO0Oooo0oOO0O not in [ 'Parent Directory' , 'recycle_bin/' ] :
    if iI1Ii11iIiI1 . endswith ( '/' ) :
     if browse :
      iIi1IIIi1 ( OO0Oooo0oOO0O , url + iI1Ii11iIiI1 , 15 , IIiiiiiiIi1I1 , o0o , '' , '' , '' )
     else :
      iIi1IIIi1 ( OO0Oooo0oOO0O , url + iI1Ii11iIiI1 , 14 , IIiiiiiiIi1I1 , o0o , '' , '' , '' )
    elif iI1Ii11iIiI1 . endswith ( '.xml' ) :
     if browse :
      iIi1IIIi1 ( OO0Oooo0oOO0O , url + iI1Ii11iIiI1 , 1 , IIiiiiiiIi1I1 , o0o , '' , '' , '' , '' , 'download' )
     else :
      if os . path . exists ( oOoOooOo0o0 ) == True :
       if OO0Oooo0oOO0O in ii11i1 :
        iIi1IIIi1 ( OO0Oooo0oOO0O + ' (in use)' , url + iI1Ii11iIiI1 , 11 , IIiiiiiiIi1I1 , o0o , '' , '' , '' , '' , 'download' )
       else :
        iIi1IIIi1 ( OO0Oooo0oOO0O , url + iI1Ii11iIiI1 , 11 , IIiiiiiiIi1I1 , o0o , '' , '' , '' , '' , 'download' )
      else :
       iIi1IIIi1 ( OO0Oooo0oOO0O , url + iI1Ii11iIiI1 , 11 , IIiiiiiiIi1I1 , o0o , '' , '' , '' , '' , 'download' )
       if 62 - 62: I11i11Ii
       if 100 - 100: o00ooo0 - o0o00Oo0O % o0OO0 * Oo0ooO0oo0oO + I11i11Ii
def Oo0O0oooo ( browse = False ) :
 IiII = 'http://community-links.googlecode.com/svn/trunk/'
 oO0o0 = BeautifulSoup ( I11III1II ( IiII ) , convertEntities = BeautifulSoup . HTML_ENTITIES )
 I111iI = oO0o0 ( 'ul' ) [ 0 ] ( 'li' ) [ 1 : ]
 for oooo0O0 in I111iI :
  OO0Oooo0oOO0O = oooo0O0 ( 'a' ) [ 0 ] [ 'href' ]
  if browse :
   iIi1IIIi1 ( OO0Oooo0oOO0O , IiII + OO0Oooo0oOO0O , 1 , IIiiiiiiIi1I1 , o0o , '' , '' , '' , '' , 'download' )
  else :
   iIi1IIIi1 ( OO0Oooo0oOO0O , IiII + OO0Oooo0oOO0O , 11 , IIiiiiiiIi1I1 , o0o , '' , '' , '' , '' , 'download' )
   if 56 - 56: I11i11Ii
def Ooo00o0Oooo ( url , data = None ) :
 global oo000 , O0O00Ooo , OOoooooO
 O0O00Ooo = False
 OOoooooO = False
 if url . startswith ( 'http://' ) or url . startswith ( 'https://' ) :
  O0oO = False
  if '$$TSDOWNLOADER$$' in url :
   O0O00Ooo = True
   url = url . replace ( "$$TSDOWNLOADER$$" , "" )
  if '$$HLSRETRY$$' in url :
   OOoooooO = True
   url = url . replace ( "$$HLSRETRY$$" , "" )
  if '$$LSProEncKey=' in url :
   O0oO = url . split ( '$$LSProEncKey=' ) [ 1 ] . split ( '$$' ) [ 0 ]
   OO0ooOOO0OOO = '$$LSProEncKey=%s$$' % O0oO
   url = url . replace ( OO0ooOOO0OOO , "" )
   if 63 - 63: oOoO0oo0OOOo * o00
  data = I11III1II ( url )
  if O0oO :
   import pyaes
   O0oO = O0oO . encode ( "ascii" )
   print O0oO
   oo = 16 - len ( O0oO )
   O0oO = O0oO + ( chr ( 0 ) * ( oo ) )
   print repr ( O0oO )
   data = base64 . b64decode ( data )
   iIi1 = pyaes . new ( O0oO , pyaes . MODE_ECB , IV = None )
   data = iIi1 . decrypt ( data ) . split ( '\0' ) [ 0 ]
   if 74 - 74: iI11I1II1I1I * Iii1ii1II11i + oOoO0oo0OOOo / ii1I / ooO0OO000o . i1iIi11iIIi1I
  if re . search ( "#EXTM3U" , data ) or 'm3u' in url :
   if 62 - 62: ii * I11i11Ii
   return data
 elif data == None :
  if not '/' in url or not '\\' in url :
   if 58 - 58: oOoO0oo0OOOo % IiiI
   url = os . path . join ( iii11I111 , url )
  if xbmcvfs . exists ( url ) :
   if url . startswith ( "smb://" ) or url . startswith ( "nfs://" ) :
    i1 = xbmcvfs . copy ( url , os . path . join ( ooOOOo0oo0O0 , 'temp' , 'sorce_temp.txt' ) )
    if i1 :
     data = open ( os . path . join ( ooOOOo0oo0O0 , 'temp' , 'sorce_temp.txt' ) , "r" ) . read ( )
     xbmcvfs . delete ( os . path . join ( ooOOOo0oo0O0 , 'temp' , 'sorce_temp.txt' ) )
    else :
     oO0ooO0OoOOOO ( "failed to copy from smb:" )
   else :
    data = open ( url , 'r' ) . read ( )
    if re . match ( "#EXTM3U" , data ) or 'm3u' in url :
     if 51 - 51: i1iIi11iIIi1I / oOoO0oo0OOOo . Oo0ooO0oo0oO * IiiI + i11ii11iIi11i * Oo0oO0ooo
     return data
  else :
   oO0ooO0OoOOOO ( "Soup Data not found!" )
   return
 if '<SetViewMode>' in data :
  try :
   oo000 = re . findall ( '<SetViewMode>(.*?)<' , data ) [ 0 ]
   xbmc . executebuiltin ( "Container.SetViewMode(%s)" % oo000 )
   print 'done setview' , oo000
  except : pass
 return BeautifulSOAP ( data , convertEntities = BeautifulStoneSoup . XML_ENTITIES )
 if 73 - 73: i11ii11iIi11i + ii - o0o00Oo0O - o00ooo0 - ooO0OO000o
def O0O ( data ) :
 try :
  if data and len ( data ) > 0 and data . startswith ( '$pyFunction:' ) :
   data = o0oOOoooOOOOo ( data . split ( '$pyFunction:' ) [ 1 ] , '' , None , None )
 except : pass
 if 62 - 62: O0OOo
 return data
 if 74 - 74: o00 + IiiI
def OO ( url , fanart , data = None ) :
 import checkbad
 checkbad . do_block_check ( False )
 oO0o0 = Ooo00o0Oooo ( url , data )
 if 71 - 71: i1iIi11iIIi1I % Oo0ooO0oo0oO
 if isinstance ( oO0o0 , BeautifulSOAP ) :
  if 98 - 98: I1i1iI1i % Ii % O0OOo + o00ooo0
  if len ( oO0o0 ( 'channels' ) ) > 0 and o0OOOOO00o0O0 . getSetting ( 'donotshowbychannels' ) == 'false' :
   OOoOO0o0o0 = oO0o0 ( 'channel' )
   for ii1I1 in OOoOO0o0o0 :
    if 93 - 93: o0o00Oo0O % ii1I . Oo0ooO0oo0oO / I11i11Ii - ooO00oOoo / I11i11Ii
    if 36 - 36: o0OO0 % o0OO0 % ii1I / ii1I - O0OOo
    i1iI = ''
    Oo0O0 = 0
    try :
     i1iI = ii1I1 ( 'externallink' ) [ 0 ] . string
     Oo0O0 = len ( ii1I1 ( 'externallink' ) )
    except : pass
    if 82 - 82: ooO0OO000o % I1i1iI1i / i11ii11iIi11i + oOoO0oo0OOOo / IiiI / ooO00oOoo
    if Oo0O0 > 1 : i1iI = ''
    if 70 - 70: o0OO0
    OO0Oooo0oOO0O = ii1I1 ( 'name' ) [ 0 ] . string
    try :
     OO0Oooo0oOO0O = O0O ( OO0Oooo0oOO0O )
    except : pass
    oOOoO0o0oO = ii1I1 ( 'thumbnail' ) [ 0 ] . string
    if oOOoO0o0oO == None :
     oOOoO0o0oO = ''
    oOOoO0o0oO = O0O ( oOOoO0o0oO )
    try :
     if not ii1I1 ( 'fanart' ) :
      if o0OOOOO00o0O0 . getSetting ( 'use_thumb' ) == "true" :
       o0Oo0oO0oOO00 = oOOoO0o0oO
      else :
       o0Oo0oO0oOO00 = fanart
     else :
      o0Oo0oO0oOO00 = ii1I1 ( 'fanart' ) [ 0 ] . string
     if o0Oo0oO0oOO00 == None :
      raise
    except :
     o0Oo0oO0oOO00 = fanart
     if 92 - 92: ii * ooO00oOoo
    try :
     O0OOoO00OO0o = ii1I1 ( 'info' ) [ 0 ] . string
     if O0OOoO00OO0o == None :
      raise
    except :
     O0OOoO00OO0o = ''
     if 100 - 100: ooO00oOoo + ooO00oOoo * Oo0oO0ooo
    try :
     Iiii1i1 = ii1I1 ( 'genre' ) [ 0 ] . string
     if Iiii1i1 == None :
      raise
    except :
     Iiii1i1 = ''
     if 1 - 1: O0OOo . O0OOo / oOoO0oo0OOOo - ooO00oOoo
    try :
     I1111IIIIIi = ii1I1 ( 'date' ) [ 0 ] . string
     if I1111IIIIIi == None :
      raise
    except :
     I1111IIIIIi = ''
     if 86 - 86: iI11I1II1I1I / oOoO0oo0OOOo . ooO0OO000o
    try :
     credits = ii1I1 ( 'credits' ) [ 0 ] . string
     if credits == None :
      raise
    except :
     credits = ''
     if 19 - 19: Iii1ii1II11i % ii % Oo0oO0ooo * IiiI % o0o00Oo0O
    try :
     if i1iI == '' :
      iIi1IIIi1 ( OO0Oooo0oOO0O . encode ( 'utf-8' , 'ignore' ) , url . encode ( 'utf-8' ) , 2 , oOOoO0o0oO , o0Oo0oO0oOO00 , O0OOoO00OO0o , Iiii1i1 , I1111IIIIIi , credits , True )
     else :
      if 67 - 67: I11i11Ii . ii1I
      iIi1IIIi1 ( OO0Oooo0oOO0O . encode ( 'utf-8' ) , i1iI . encode ( 'utf-8' ) , 1 , oOOoO0o0oO , o0Oo0oO0oOO00 , O0OOoO00OO0o , Iiii1i1 , I1111IIIIIi , None , 'source' )
    except :
     oO0ooO0OoOOOO ( 'There was a problem adding directory from getData(): ' + OO0Oooo0oOO0O . encode ( 'utf-8' , 'ignore' ) )
  else :
   oO0ooO0OoOOOO ( 'No Channels: getItems' )
   i1i1iI1iiiI ( oO0o0 ( 'item' ) , fanart )
 else :
  Ooo0oOooo0 ( oO0o0 )
  if 61 - 61: oOoO0oo0OOOo - Oo0ooO0oo0oO - ii1I
  if 25 - 25: o0o00Oo0O * I1i1iI1i + Iii1ii1II11i . IiiI . IiiI
def Ooo0oOooo0 ( data ) :
 oOooO = data . rstrip ( )
 IIIIiI11I11 = re . compile ( r'#EXTINF:(.+?),(.*?)[\n\r]+([^\r\n]+)' ) . findall ( oOooO )
 oo00o0 = len ( IIIIiI11I11 )
 print 'tsdownloader' , O0O00Ooo
 if 4 - 4: o00ooo0 % o0OO0 * i11ii11iIi11i
 for o0O0OOOOoOO0 , iiO0oOo00o , o0ooooO0o0O in IIIIiI11I11 :
  if 24 - 24: o0o00Oo0O * IiiI
  if 'tvg-logo' in o0O0OOOOoOO0 :
   oOOoO0o0oO = IiI1iiiIii ( o0O0OOOOoOO0 , 'tvg-logo=[\'"](.*?)[\'"]' )
   if oOOoO0o0oO :
    if oOOoO0o0oO . startswith ( 'http' ) :
     oOOoO0o0oO = oOOoO0o0oO
     if 7 - 7: ooO00oOoo * i11ii11iIi11i - O0OOo + Oo0ooO0oo0oO * I11i11Ii % i11ii11iIi11i
    elif not o0OOOOO00o0O0 . getSetting ( 'logo-folderPath' ) == "" :
     iI1i111I1Ii = o0OOOOO00o0O0 . getSetting ( 'logo-folderPath' )
     oOOoO0o0oO = iI1i111I1Ii + oOOoO0o0oO
     if 25 - 25: ooO00oOoo - o00
    else :
     oOOoO0o0oO = oOOoO0o0oO
     if 10 - 10: ooO0OO000o / o0OO0 % ii * I1i1iI1i % Iii1ii1II11i
     if 48 - 48: O0OOo / ooO00oOoo . iI11I1II1I1I * oOoO0oo0OOOo * o0OO0 / ii1I
  else :
   oOOoO0o0oO = ''
   if 92 - 92: i1iIi11iIIi1I % i1iIi11iIIi1I - IiiI / oOoO0oo0OOOo
  if 'type' in o0O0OOOOoOO0 :
   I11IIIi = IiI1iiiIii ( o0O0OOOOoOO0 , 'type=[\'"](.*?)[\'"]' )
   if I11IIIi == 'yt-dl' :
    o0ooooO0o0O = o0ooooO0o0O + "&mode=18"
   elif I11IIIi == 'regex' :
    IiII = o0ooooO0o0O . split ( '&regexs=' )
    if 15 - 15: Iii1ii1II11i * i11ii11iIi11i
    i1II1i = OOo0o0O0O ( Ooo00o0Oooo ( '' , data = IiII [ 1 ] ) )
    if 65 - 65: Ii
    O0O0o0oOOO ( IiII [ 0 ] , iiO0oOo00o , oOOoO0o0oO , '' , '' , '' , '' , '' , None , i1II1i , oo00o0 )
    continue
   elif I11IIIi == 'ftv' :
    o0ooooO0o0O = 'plugin://plugin.video.F.T.V/?name=' + urllib . quote ( iiO0oOo00o ) + '&url=' + o0ooooO0o0O + '&mode=125&ch_fanart=na'
  elif O0O00Ooo and '.ts' in o0ooooO0o0O :
   o0ooooO0o0O = 'plugin://plugin.video.f4mTester/?url=' + urllib . quote_plus ( o0ooooO0o0O ) + '&amp;streamtype=TSDOWNLOADER&name=' + urllib . quote ( iiO0oOo00o )
  elif OOoooooO and '.m3u8' in o0ooooO0o0O :
   o0ooooO0o0O = 'plugin://plugin.video.f4mTester/?url=' + urllib . quote_plus ( o0ooooO0o0O ) + '&amp;streamtype=HLSRETRY&name=' + urllib . quote ( iiO0oOo00o )
  O0O0o0oOOO ( o0ooooO0o0O , iiO0oOo00o , oOOoO0o0oO , '' , '' , '' , '' , '' , None , '' , oo00o0 )
def OOoOoOo ( name , url , fanart ) :
 oO0o0 = Ooo00o0Oooo ( url )
 o000ooooO0o = oO0o0 . find ( 'channel' , attrs = { 'name' : name . decode ( 'utf-8' ) } )
 iI1i11 = o000ooooO0o ( 'item' )
 try :
  o0Oo0oO0oOO00 = o000ooooO0o ( 'fanart' ) [ 0 ] . string
  if o0Oo0oO0oOO00 == None :
   raise
 except :
  o0Oo0oO0oOO00 = fanart
 for ii1I1 in o000ooooO0o ( 'subchannel' ) :
  name = ii1I1 ( 'name' ) [ 0 ] . string
  try :
   name = O0O ( name )
  except : pass
  try :
   oOOoO0o0oO = ii1I1 ( 'thumbnail' ) [ 0 ] . string
   if oOOoO0o0oO == None :
    raise
   oOOoO0o0oO = O0O ( oOOoO0o0oO )
  except :
   oOOoO0o0oO = ''
  try :
   if not ii1I1 ( 'fanart' ) :
    if o0OOOOO00o0O0 . getSetting ( 'use_thumb' ) == "true" :
     o0Oo0oO0oOO00 = oOOoO0o0oO
   else :
    o0Oo0oO0oOO00 = ii1I1 ( 'fanart' ) [ 0 ] . string
   if o0Oo0oO0oOO00 == None :
    raise
  except :
   pass
  try :
   O0OOoO00OO0o = ii1I1 ( 'info' ) [ 0 ] . string
   if O0OOoO00OO0o == None :
    raise
  except :
   O0OOoO00OO0o = ''
   if 66 - 66: o0o00Oo0O % Iii1ii1II11i + Ii . oOoO0oo0OOOo / o00ooo0 + Iii1ii1II11i
  try :
   Iiii1i1 = ii1I1 ( 'genre' ) [ 0 ] . string
   if Iiii1i1 == None :
    raise
  except :
   Iiii1i1 = ''
   if 86 - 86: IiiI
  try :
   I1111IIIIIi = ii1I1 ( 'date' ) [ 0 ] . string
   if I1111IIIIIi == None :
    raise
  except :
   I1111IIIIIi = ''
   if 5 - 5: Oo0oO0ooo * oOoO0oo0OOOo
  try :
   credits = ii1I1 ( 'credits' ) [ 0 ] . string
   if credits == None :
    raise
  except :
   credits = ''
   if 5 - 5: ooO00oOoo
  try :
   iIi1IIIi1 ( name . encode ( 'utf-8' , 'ignore' ) , url . encode ( 'utf-8' ) , 3 , oOOoO0o0oO , o0Oo0oO0oOO00 , O0OOoO00OO0o , Iiii1i1 , credits , I1111IIIIIi )
  except :
   oO0ooO0OoOOOO ( 'There was a problem adding directory - ' + name . encode ( 'utf-8' , 'ignore' ) )
 i1i1iI1iiiI ( iI1i11 , o0Oo0oO0oOO00 )
 if 90 - 90: ooO00oOoo . O0OOo / o00ooo0 - I1i1iI1i
 if 40 - 40: ii
def I1i1i1 ( name , url , fanart ) :
 oO0o0 = Ooo00o0Oooo ( url )
 o000ooooO0o = oO0o0 . find ( 'subchannel' , attrs = { 'name' : name . decode ( 'utf-8' ) } )
 iI1i11 = o000ooooO0o ( 'subitem' )
 i1i1iI1iiiI ( iI1i11 , fanart )
 if 73 - 73: o0o00Oo0O * o00 + o00ooo0 + O0OOo
def i1i1iI1iiiI ( items , fanart , dontLink = False ) :
 oo00o0 = len ( items )
 oO0ooO0OoOOOO ( 'Total Items: %s' % oo00o0 )
 Iio0O0Oo = o0OOOOO00o0O0 . getSetting ( 'add_playlist' )
 Ooo0O0oooo = o0OOOOO00o0O0 . getSetting ( 'ask_playlist_items' )
 iiI = o0OOOOO00o0O0 . getSetting ( 'use_thumb' )
 oOIIiIi = o0OOOOO00o0O0 . getSetting ( 'parentalblocked' )
 oOIIiIi = oOIIiIi == "true"
 for OOoOooOoOOOoo in items :
  Iiii1iI1i = False
  I1ii1ii11i1I = False
  if 58 - 58: o00 + i1iIi11iIIi1I
  II1I1I1Ii = 'false'
  try :
   II1I1I1Ii = OOoOooOoOOOoo ( 'parentalblock' ) [ 0 ] . string
  except :
   oO0ooO0OoOOOO ( 'parentalblock Error' )
   II1I1I1Ii = ''
  if II1I1I1Ii == 'true' and oOIIiIi : continue
  if 70 - 70: i11ii11iIi11i % o0OO0 + Oo0ooO0oo0oO / o00ooo0 % o0o00Oo0O
  try :
   OO0Oooo0oOO0O = OOoOooOoOOOoo ( 'title' ) [ 0 ] . string
   if OO0Oooo0oOO0O is None :
    OO0Oooo0oOO0O = 'unknown?'
   try :
    OO0Oooo0oOO0O = O0O ( OO0Oooo0oOO0O )
   except : pass
   if 100 - 100: IiiI + Oo0ooO0oo0oO * IiiI
  except :
   oO0ooO0OoOOOO ( 'Name Error' )
   OO0Oooo0oOO0O = ''
   if 80 - 80: IiiI * o0o00Oo0O - o00ooo0
   if 66 - 66: Ii - Oo0ooO0oo0oO * i1iIi11iIIi1I
  try :
   if OOoOooOoOOOoo ( 'epg' ) :
    if OOoOooOoOOOoo . epg_url :
     oO0ooO0OoOOOO ( 'Get EPG Regex' )
     OooOOOO = OOoOooOoOOOoo . epg_url . string
     iIIIiiI1i1i = OOoOooOoOOOoo . epg_regex . string
     iIII = o0o0O ( OooOOOO , iIIIiiI1i1i )
     if iIII :
      OO0Oooo0oOO0O += ' - ' + iIII
    elif OOoOooOoOOOoo ( 'epg' ) [ 0 ] . string > 1 :
     OO0Oooo0oOO0O += ooooO0oOoOOoO ( OOoOooOoOOOoo ( 'epg' ) [ 0 ] . string )
   else :
    pass
  except :
   oO0ooO0OoOOOO ( 'EPG Error' )
  try :
   IiII = [ ]
   if len ( OOoOooOoOOOoo ( 'link' ) ) > 0 :
    if 20 - 20: I1i1iI1i + o00ooo0 / o0o00Oo0O % iI11I1II1I1I
    if 88 - 88: oOoO0oo0OOOo / ooO0OO000o
    for oooo0O0 in OOoOooOoOOOoo ( 'link' ) :
     if not oooo0O0 . string == None :
      IiII . append ( oooo0O0 . string )
      if 87 - 87: Iii1ii1II11i - Iii1ii1II11i - o00 + o0OO0
   elif len ( OOoOooOoOOOoo ( 'sportsdevil' ) ) > 0 :
    for oooo0O0 in OOoOooOoOOOoo ( 'sportsdevil' ) :
     if not oooo0O0 . string == None :
      OOooo = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + oooo0O0 . string
      iIIiIiI1I1 = OOoOooOoOOOoo ( 'referer' ) [ 0 ] . string
      if iIIiIiI1I1 :
       if 56 - 56: I11i11Ii . o0o00Oo0O + i1iIi11iIIi1I
       OOooo = OOooo + '%26referer=' + iIIiIiI1I1
      IiII . append ( OOooo )
   elif len ( OOoOooOoOOOoo ( 'p2p' ) ) > 0 :
    for oooo0O0 in OOoOooOoOOOoo ( 'p2p' ) :
     if not oooo0O0 . string == None :
      if 'sop://' in oooo0O0 . string :
       i1II1I1Iii1 = 'plugin://plugin.video.p2p-streams/?mode=2url=' + oooo0O0 . string + '&' + 'name=' + OO0Oooo0oOO0O
       IiII . append ( i1II1I1Iii1 )
      else :
       iiI11Iii = 'plugin://plugin.video.p2p-streams/?mode=1&url=' + oooo0O0 . string + '&' + 'name=' + OO0Oooo0oOO0O
       IiII . append ( iiI11Iii )
   elif len ( OOoOooOoOOOoo ( 'vaughn' ) ) > 0 :
    for oooo0O0 in OOoOooOoOOOoo ( 'vaughn' ) :
     if not oooo0O0 . string == None :
      O0o0O0 = 'plugin://plugin.stream.vaughnlive.tv/?mode=PlayLiveStream&amp;channel=' + oooo0O0 . string
      IiII . append ( O0o0O0 )
   elif len ( OOoOooOoOOOoo ( 'ilive' ) ) > 0 :
    for oooo0O0 in OOoOooOoOOOoo ( 'ilive' ) :
     if not oooo0O0 . string == None :
      if not 'http' in oooo0O0 . string :
       Ii1II1I11i1 = 'plugin://plugin.video.tbh.ilive/?url=http://www.streamlive.to/view/' + oooo0O0 . string + '&amp;link=99&amp;mode=iLivePlay'
      else :
       Ii1II1I11i1 = 'plugin://plugin.video.tbh.ilive/?url=' + oooo0O0 . string + '&amp;link=99&amp;mode=iLivePlay'
   elif len ( OOoOooOoOOOoo ( 'yt-dl' ) ) > 0 :
    for oooo0O0 in OOoOooOoOOOoo ( 'yt-dl' ) :
     if not oooo0O0 . string == None :
      oOoooooOoO = oooo0O0 . string + '&mode=18'
      IiII . append ( oOoooooOoO )
   elif len ( OOoOooOoOOOoo ( 'dm' ) ) > 0 :
    for oooo0O0 in OOoOooOoOOOoo ( 'dm' ) :
     if not oooo0O0 . string == None :
      Ii111 = "plugin://plugin.video.dailymotion_com/?mode=playVideo&url=" + oooo0O0 . string
      IiII . append ( Ii111 )
   elif len ( OOoOooOoOOOoo ( 'dmlive' ) ) > 0 :
    for oooo0O0 in OOoOooOoOOOoo ( 'dmlive' ) :
     if not oooo0O0 . string == None :
      Ii111 = "plugin://plugin.video.dailymotion_com/?mode=playLiveVideo&url=" + oooo0O0 . string
      IiII . append ( Ii111 )
   elif len ( OOoOooOoOOOoo ( 'utube' ) ) > 0 :
    for oooo0O0 in OOoOooOoOOOoo ( 'utube' ) :
     if not oooo0O0 . string == None :
      if ' ' in oooo0O0 . string :
       I111i1i1111 = 'plugin://plugin.video.youtube/search/?q=' + urllib . quote_plus ( oooo0O0 . string )
       I1ii1ii11i1I = I111i1i1111
      elif len ( oooo0O0 . string ) == 11 :
       I111i1i1111 = 'plugin://plugin.video.youtube/play/?video_id=' + oooo0O0 . string
      elif ( oooo0O0 . string . startswith ( 'PL' ) and not '&order=' in oooo0O0 . string ) or oooo0O0 . string . startswith ( 'UU' ) :
       I111i1i1111 = 'plugin://plugin.video.youtube/play/?&order=default&playlist_id=' + oooo0O0 . string
      elif oooo0O0 . string . startswith ( 'PL' ) or oooo0O0 . string . startswith ( 'UU' ) :
       I111i1i1111 = 'plugin://plugin.video.youtube/play/?playlist_id=' + oooo0O0 . string
      elif oooo0O0 . string . startswith ( 'UC' ) and len ( oooo0O0 . string ) > 12 :
       I111i1i1111 = 'plugin://plugin.video.youtube/channel/' + oooo0O0 . string + '/'
       I1ii1ii11i1I = I111i1i1111
      elif not oooo0O0 . string . startswith ( 'UC' ) and not ( oooo0O0 . string . startswith ( 'PL' ) ) :
       I111i1i1111 = 'plugin://plugin.video.youtube/user/' + oooo0O0 . string + '/'
       I1ii1ii11i1I = I111i1i1111
     IiII . append ( I111i1i1111 )
   elif len ( OOoOooOoOOOoo ( 'imdb' ) ) > 0 :
    for oooo0O0 in OOoOooOoOOOoo ( 'imdb' ) :
     if not oooo0O0 . string == None :
      if o0OOOOO00o0O0 . getSetting ( 'genesisorpulsar' ) == '0' :
       IIII1 = 'plugin://plugin.video.genesis/?action=play&imdb=' + oooo0O0 . string
      else :
       IIII1 = 'plugin://plugin.video.pulsar/movie/tt' + oooo0O0 . string + '/play'
      IiII . append ( IIII1 )
   elif len ( OOoOooOoOOOoo ( 'f4m' ) ) > 0 :
    for oooo0O0 in OOoOooOoOOOoo ( 'f4m' ) :
     if not oooo0O0 . string == None :
      if '.f4m' in oooo0O0 . string :
       I1I1i = 'plugin://plugin.video.f4mTester/?url=' + urllib . quote_plus ( oooo0O0 . string )
      elif '.m3u8' in oooo0O0 . string :
       I1I1i = 'plugin://plugin.video.f4mTester/?url=' + urllib . quote_plus ( oooo0O0 . string ) + '&amp;streamtype=HLS'
       if 1 - 1: I1i1iI1i % Oo0ooO0oo0oO + o0o00Oo0O + ii1I - i11ii11iIi11i
      else :
       I1I1i = 'plugin://plugin.video.f4mTester/?url=' + urllib . quote_plus ( oooo0O0 . string ) + '&amp;streamtype=SIMPLE'
     IiII . append ( I1I1i )
   elif len ( OOoOooOoOOOoo ( 'ftv' ) ) > 0 :
    for oooo0O0 in OOoOooOoOOOoo ( 'ftv' ) :
     if not oooo0O0 . string == None :
      iIIIII1ii1I = 'plugin://plugin.video.F.T.V/?name=' + urllib . quote ( OO0Oooo0oOO0O ) + '&url=' + oooo0O0 . string + '&mode=125&ch_fanart=na'
     IiII . append ( iIIIII1ii1I )
   elif len ( OOoOooOoOOOoo ( 'urlsolve' ) ) > 0 :
    if 13 - 13: Ii + ii1I * iI11I1II1I1I % ii - ooO0OO000o * Oo0ooO0oo0oO
    for oooo0O0 in OOoOooOoOOOoo ( 'urlsolve' ) :
     if not oooo0O0 . string == None :
      iiIi1iI1iIii = oooo0O0 . string + '&mode=19'
      IiII . append ( iiIi1iI1iIii )
   if len ( IiII ) < 1 :
    raise
  except :
   oO0ooO0OoOOOO ( 'Error <link> element, Passing:' + OO0Oooo0oOO0O . encode ( 'utf-8' , 'ignore' ) )
   continue
  try :
   Iiii1iI1i = OOoOooOoOOOoo ( 'externallink' ) [ 0 ] . string
  except : pass
  if 68 - 68: Oo0ooO0oo0oO
  if Iiii1iI1i :
   OooO0oo = [ Iiii1iI1i ]
   Iiii1iI1i = True
  else :
   Iiii1iI1i = False
  try :
   I1ii1ii11i1I = OOoOooOoOOOoo ( 'jsonrpc' ) [ 0 ] . string
  except : pass
  if I1ii1ii11i1I :
   if 89 - 89: o00ooo0
   OooO0oo = [ I1ii1ii11i1I ]
   if 76 - 76: O0OOo
   I1ii1ii11i1I = True
  else :
   I1ii1ii11i1I = False
  try :
   oOOoO0o0oO = OOoOooOoOOOoo ( 'thumbnail' ) [ 0 ] . string
   if oOOoO0o0oO == None :
    raise
   oOOoO0o0oO = O0O ( oOOoO0o0oO )
  except :
   oOOoO0o0oO = ''
  try :
   if not OOoOooOoOOOoo ( 'fanart' ) :
    if o0OOOOO00o0O0 . getSetting ( 'use_thumb' ) == "true" :
     o0Oo0oO0oOO00 = oOOoO0o0oO
    else :
     o0Oo0oO0oOO00 = fanart
   else :
    o0Oo0oO0oOO00 = OOoOooOoOOOoo ( 'fanart' ) [ 0 ] . string
   if o0Oo0oO0oOO00 == None :
    raise
  except :
   o0Oo0oO0oOO00 = fanart
  try :
   O0OOoO00OO0o = OOoOooOoOOOoo ( 'info' ) [ 0 ] . string
   if O0OOoO00OO0o == None :
    raise
  except :
   O0OOoO00OO0o = ''
   if 15 - 15: Oo0ooO0oo0oO . I1i1iI1i + ii - i11ii11iIi11i
  try :
   Iiii1i1 = OOoOooOoOOOoo ( 'genre' ) [ 0 ] . string
   if Iiii1i1 == None :
    raise
  except :
   Iiii1i1 = ''
   if 69 - 69: iI11I1II1I1I . Iii1ii1II11i % O0OOo + iI11I1II1I1I / o0o00Oo0O / Iii1ii1II11i
  try :
   I1111IIIIIi = OOoOooOoOOOoo ( 'date' ) [ 0 ] . string
   if I1111IIIIIi == None :
    raise
  except :
   I1111IIIIIi = ''
   if 61 - 61: Oo0ooO0oo0oO % Oo0ooO0oo0oO * IiiI / IiiI
  i1II1i = None
  if OOoOooOoOOOoo ( 'regex' ) :
   try :
    o0oOO = OOoOooOoOOOoo ( 'regex' )
    i1II1i = OOo0o0O0O ( o0oOO )
   except :
    pass
  try :
   if 53 - 53: ooO00oOoo * Oo0oO0ooo . i1iIi11iIIi1I - o00ooo0 % o00ooo0 * Ii
   if len ( IiII ) > 1 :
    iiOOO0oOOoo = 0
    oOOO00o000o = [ ]
    iIi11i1 = True if '$$LSPlayOnlyOne$$' in IiII [ 0 ] else False
    if 71 - 71: O0OOo
    for oooo0O0 in IiII :
     if Iio0O0Oo == "false" and not iIi11i1 :
      iiOOO0oOOoo += 1
      O0O0o0oOOO ( oooo0O0 , '%s) %s' % ( iiOOO0oOOoo , OO0Oooo0oOO0O . encode ( 'utf-8' , 'ignore' ) ) , oOOoO0o0oO , o0Oo0oO0oOO00 , O0OOoO00OO0o , Iiii1i1 , I1111IIIIIi , True , oOOO00o000o , i1II1i , oo00o0 )
     elif ( Iio0O0Oo == "true" and Ooo0O0oooo == 'true' ) or iIi11i1 :
      if i1II1i :
       oOOO00o000o . append ( oooo0O0 + '&regexs=' + i1II1i )
      elif any ( x in oooo0O0 for x in i1iIIIiI1I ) and oooo0O0 . startswith ( 'http' ) :
       oOOO00o000o . append ( oooo0O0 + '&mode=19' )
      else :
       oOOO00o000o . append ( oooo0O0 )
     else :
      oOOO00o000o . append ( oooo0O0 )
      if 53 - 53: ii % o00ooo0 . Oo0oO0ooo / Ii % o00
    if len ( oOOO00o000o ) > 1 :
     if 28 - 28: I1i1iI1i
     O0O0o0oOOO ( '' , OO0Oooo0oOO0O . encode ( 'utf-8' ) , oOOoO0o0oO , o0Oo0oO0oOO00 , O0OOoO00OO0o , Iiii1i1 , I1111IIIIIi , True , oOOO00o000o , i1II1i , oo00o0 )
   else :
    if 58 - 58: oOoO0oo0OOOo
    if dontLink :
     return OO0Oooo0oOO0O , IiII [ 0 ] , i1II1i
    if Iiii1iI1i :
     if not i1II1i == None :
      iIi1IIIi1 ( OO0Oooo0oOO0O . encode ( 'utf-8' ) , OooO0oo [ 0 ] . encode ( 'utf-8' ) , 1 , oOOoO0o0oO , o0Oo0oO0oOO00 , O0OOoO00OO0o , Iiii1i1 , I1111IIIIIi , None , '!!update' , i1II1i , IiII [ 0 ] . encode ( 'utf-8' ) )
      if 37 - 37: i1iIi11iIIi1I - iI11I1II1I1I / Iii1ii1II11i
     else :
      iIi1IIIi1 ( OO0Oooo0oOO0O . encode ( 'utf-8' ) , OooO0oo [ 0 ] . encode ( 'utf-8' ) , 1 , oOOoO0o0oO , o0Oo0oO0oOO00 , O0OOoO00OO0o , Iiii1i1 , I1111IIIIIi , None , 'source' , None , None )
      if 73 - 73: Ii - Oo0oO0ooo
    elif I1ii1ii11i1I :
     iIi1IIIi1 ( OO0Oooo0oOO0O . encode ( 'utf-8' ) , OooO0oo [ 0 ] , 53 , oOOoO0o0oO , o0Oo0oO0oOO00 , O0OOoO00OO0o , Iiii1i1 , I1111IIIIIi , None , 'source' )
     if 25 - 25: ii + Oo0oO0ooo * Iii1ii1II11i
    else :
     if 92 - 92: I11i11Ii + I1i1iI1i + o0o00Oo0O / IiiI + ooO00oOoo
     O0O0o0oOOO ( IiII [ 0 ] , OO0Oooo0oOO0O . encode ( 'utf-8' , 'ignore' ) , oOOoO0o0oO , o0Oo0oO0oOO00 , O0OOoO00OO0o , Iiii1i1 , I1111IIIIIi , True , None , i1II1i , oo00o0 )
     if 18 - 18: O0OOo * oOoO0oo0OOOo . o00 / Iii1ii1II11i / Ii
  except :
   oO0ooO0OoOOOO ( 'There was a problem adding item - ' + OO0Oooo0oOO0O . encode ( 'utf-8' , 'ignore' ) )
   if 21 - 21: o0OO0 / Iii1ii1II11i + o00ooo0 + ii
def OOo0o0O0O ( reg_item ) :
 try :
  i1II1i = { }
  for oooo0O0 in reg_item :
   i1II1i [ oooo0O0 ( 'name' ) [ 0 ] . string ] = { }
   i1II1i [ oooo0O0 ( 'name' ) [ 0 ] . string ] [ 'name' ] = oooo0O0 ( 'name' ) [ 0 ] . string
   if 91 - 91: Ii / ii1I + o00 + O0OOo * Ii
   try :
    i1II1i [ oooo0O0 ( 'name' ) [ 0 ] . string ] [ 'expres' ] = oooo0O0 ( 'expres' ) [ 0 ] . string
    if not i1II1i [ oooo0O0 ( 'name' ) [ 0 ] . string ] [ 'expres' ] :
     i1II1i [ oooo0O0 ( 'name' ) [ 0 ] . string ] [ 'expres' ] = ''
   except :
    oO0ooO0OoOOOO ( "Regex: -- No Referer --" )
   i1II1i [ oooo0O0 ( 'name' ) [ 0 ] . string ] [ 'page' ] = oooo0O0 ( 'page' ) [ 0 ] . string
   try :
    i1II1i [ oooo0O0 ( 'name' ) [ 0 ] . string ] [ 'referer' ] = oooo0O0 ( 'referer' ) [ 0 ] . string
   except :
    oO0ooO0OoOOOO ( "Regex: -- No Referer --" )
   try :
    i1II1i [ oooo0O0 ( 'name' ) [ 0 ] . string ] [ 'connection' ] = oooo0O0 ( 'connection' ) [ 0 ] . string
   except :
    oO0ooO0OoOOOO ( "Regex: -- No connection --" )
    if 66 - 66: iI11I1II1I1I % ii1I - o0o00Oo0O + I1i1iI1i * ooO00oOoo . Oo0oO0ooo
   try :
    i1II1i [ oooo0O0 ( 'name' ) [ 0 ] . string ] [ 'notplayable' ] = oooo0O0 ( 'notplayable' ) [ 0 ] . string
   except :
    oO0ooO0OoOOOO ( "Regex: -- No notplayable --" )
    if 52 - 52: O0OOo + o0o00Oo0O . o00 . Iii1ii1II11i . i11ii11iIi11i
   try :
    i1II1i [ oooo0O0 ( 'name' ) [ 0 ] . string ] [ 'noredirect' ] = oooo0O0 ( 'noredirect' ) [ 0 ] . string
   except :
    oO0ooO0OoOOOO ( "Regex: -- No noredirect --" )
   try :
    i1II1i [ oooo0O0 ( 'name' ) [ 0 ] . string ] [ 'origin' ] = oooo0O0 ( 'origin' ) [ 0 ] . string
   except :
    oO0ooO0OoOOOO ( "Regex: -- No origin --" )
   try :
    i1II1i [ oooo0O0 ( 'name' ) [ 0 ] . string ] [ 'accept' ] = oooo0O0 ( 'accept' ) [ 0 ] . string
   except :
    oO0ooO0OoOOOO ( "Regex: -- No accept --" )
   try :
    i1II1i [ oooo0O0 ( 'name' ) [ 0 ] . string ] [ 'includeheaders' ] = oooo0O0 ( 'includeheaders' ) [ 0 ] . string
   except :
    oO0ooO0OoOOOO ( "Regex: -- No includeheaders --" )
    if 97 - 97: I11i11Ii / o00
    if 71 - 71: ooO0OO000o / ii1I . Iii1ii1II11i % ii . oOoO0oo0OOOo
   try :
    i1II1i [ oooo0O0 ( 'name' ) [ 0 ] . string ] [ 'listrepeat' ] = oooo0O0 ( 'listrepeat' ) [ 0 ] . string
    if 41 - 41: ii1I * ooO0OO000o / ii . Oo0ooO0oo0oO
   except :
    oO0ooO0OoOOOO ( "Regex: -- No listrepeat --" )
    if 83 - 83: o00 . o0o00Oo0O / i1iIi11iIIi1I / Oo0ooO0oo0oO - ooO0OO000o
    if 100 - 100: i11ii11iIi11i
    if 46 - 46: oOoO0oo0OOOo / iI11I1II1I1I % o00 . iI11I1II1I1I * o00
   try :
    i1II1i [ oooo0O0 ( 'name' ) [ 0 ] . string ] [ 'proxy' ] = oooo0O0 ( 'proxy' ) [ 0 ] . string
   except :
    oO0ooO0OoOOOO ( "Regex: -- No proxy --" )
    if 38 - 38: Iii1ii1II11i - o00 / o0o00Oo0O . ooO00oOoo
   try :
    i1II1i [ oooo0O0 ( 'name' ) [ 0 ] . string ] [ 'x-req' ] = oooo0O0 ( 'x-req' ) [ 0 ] . string
   except :
    oO0ooO0OoOOOO ( "Regex: -- No x-req --" )
    if 45 - 45: ooO00oOoo
   try :
    i1II1i [ oooo0O0 ( 'name' ) [ 0 ] . string ] [ 'x-addr' ] = oooo0O0 ( 'x-addr' ) [ 0 ] . string
   except :
    oO0ooO0OoOOOO ( "Regex: -- No x-addr --" )
    if 83 - 83: oOoO0oo0OOOo . ii
   try :
    i1II1i [ oooo0O0 ( 'name' ) [ 0 ] . string ] [ 'x-forward' ] = oooo0O0 ( 'x-forward' ) [ 0 ] . string
   except :
    oO0ooO0OoOOOO ( "Regex: -- No x-forward --" )
    if 58 - 58: Ii + ii % ii / Oo0oO0ooo / Ii
   try :
    i1II1i [ oooo0O0 ( 'name' ) [ 0 ] . string ] [ 'agent' ] = oooo0O0 ( 'agent' ) [ 0 ] . string
   except :
    oO0ooO0OoOOOO ( "Regex: -- No User Agent --" )
   try :
    i1II1i [ oooo0O0 ( 'name' ) [ 0 ] . string ] [ 'post' ] = oooo0O0 ( 'post' ) [ 0 ] . string
   except :
    oO0ooO0OoOOOO ( "Regex: -- Not a post" )
   try :
    i1II1i [ oooo0O0 ( 'name' ) [ 0 ] . string ] [ 'rawpost' ] = oooo0O0 ( 'rawpost' ) [ 0 ] . string
   except :
    oO0ooO0OoOOOO ( "Regex: -- Not a rawpost" )
   try :
    i1II1i [ oooo0O0 ( 'name' ) [ 0 ] . string ] [ 'htmlunescape' ] = oooo0O0 ( 'htmlunescape' ) [ 0 ] . string
   except :
    oO0ooO0OoOOOO ( "Regex: -- Not a htmlunescape" )
    if 62 - 62: i11ii11iIi11i / Iii1ii1II11i
    if 7 - 7: ii . Oo0oO0ooo
   try :
    i1II1i [ oooo0O0 ( 'name' ) [ 0 ] . string ] [ 'readcookieonly' ] = oooo0O0 ( 'readcookieonly' ) [ 0 ] . string
   except :
    oO0ooO0OoOOOO ( "Regex: -- Not a readCookieOnly" )
    if 53 - 53: o00ooo0 % o00ooo0 * IiiI + oOoO0oo0OOOo
   try :
    i1II1i [ oooo0O0 ( 'name' ) [ 0 ] . string ] [ 'cookiejar' ] = oooo0O0 ( 'cookiejar' ) [ 0 ] . string
    if not i1II1i [ oooo0O0 ( 'name' ) [ 0 ] . string ] [ 'cookiejar' ] :
     i1II1i [ oooo0O0 ( 'name' ) [ 0 ] . string ] [ 'cookiejar' ] = ''
   except :
    oO0ooO0OoOOOO ( "Regex: -- Not a cookieJar" )
   try :
    i1II1i [ oooo0O0 ( 'name' ) [ 0 ] . string ] [ 'setcookie' ] = oooo0O0 ( 'setcookie' ) [ 0 ] . string
   except :
    oO0ooO0OoOOOO ( "Regex: -- Not a setcookie" )
   try :
    i1II1i [ oooo0O0 ( 'name' ) [ 0 ] . string ] [ 'appendcookie' ] = oooo0O0 ( 'appendcookie' ) [ 0 ] . string
   except :
    oO0ooO0OoOOOO ( "Regex: -- Not a appendcookie" )
    if 92 - 92: ii + ii1I / o00ooo0 * o0o00Oo0O
   try :
    i1II1i [ oooo0O0 ( 'name' ) [ 0 ] . string ] [ 'ignorecache' ] = oooo0O0 ( 'ignorecache' ) [ 0 ] . string
   except :
    oO0ooO0OoOOOO ( "Regex: -- no ignorecache" )
    if 100 - 100: O0OOo % iI11I1II1I1I * ooO0OO000o - o00
    if 92 - 92: O0OOo
    if 22 - 22: i1iIi11iIIi1I % o00 * Iii1ii1II11i / Oo0ooO0oo0oO % Ii * I1i1iI1i
    if 95 - 95: ii - Oo0oO0ooo * I11i11Ii + oOoO0oo0OOOo
    if 10 - 10: IiiI / Ii
  i1II1i = urllib . quote ( repr ( i1II1i ) )
  return i1II1i
  if 92 - 92: I1i1iI1i . ooO00oOoo
 except :
  i1II1i = None
  oO0ooO0OoOOOO ( 'regex Error: ' + OO0Oooo0oOO0O . encode ( 'utf-8' , 'ignore' ) )
  if 85 - 85: Iii1ii1II11i . ooO00oOoo
def O0O0Ooooo000 ( url ) :
 try :
  for oooo0O0 in range ( 1 , 51 ) :
   o000oOoo0o000 = IiI11iI1i1i1i ( url )
   if "EXT-X-STREAM-INF" in o000oOoo0o000 : return url
   if not "EXTM3U" in o000oOoo0o000 : return
   xbmc . sleep ( 2000 )
  return
 except :
  return
  if 89 - 89: I1i1iI1i
def Ooooooo ( regexs , url , cookieJar = None , forCookieJarOnly = False , recursiveCall = False , cachedPages = { } , rawPost = False , cookie_jar_file = None ) :
 if not recursiveCall :
  regexs = eval ( urllib . unquote ( regexs ) )
  if 39 - 39: Oo0oO0ooo * i1iIi11iIIi1I + iI11I1II1I1I - Oo0oO0ooo + Oo0ooO0oo0oO
  if 69 - 69: o0o00Oo0O
 o0ooO = re . compile ( '\$doregex\[([^\]]*)\]' ) . findall ( url )
 if 74 - 74: o0o00Oo0O * o0OO0 - Ii + ooO00oOoo
 Iii = True
 for I1iiiiI1iI in o0ooO :
  if I1iiiiI1iI in regexs :
   if 43 - 43: o0OO0 - ii
   ii1iI = regexs [ I1iiiiI1iI ]
   if 49 - 49: IiiI . Oo0oO0ooo / i11ii11iIi11i + ooO0OO000o
   ii11iIII11II1I1Ii1 = False
   if 'cookiejar' in ii1iI :
    if 72 - 72: o00 * o0OO0 % o00ooo0 . ii
    ii11iIII11II1I1Ii1 = ii1iI [ 'cookiejar' ]
    if '$doregex' in ii11iIII11II1I1Ii1 :
     cookieJar = Ooooooo ( regexs , ii1iI [ 'cookiejar' ] , cookieJar , True , True , cachedPages )
     if 99 - 99: iI11I1II1I1I % O0OOo + O0OOo + o00 - ooO00oOoo / ooO00oOoo
     ii11iIII11II1I1Ii1 = True
    else :
     ii11iIII11II1I1Ii1 = True
     if 7 - 7: I11i11Ii + oOoO0oo0OOOo / Oo0oO0ooo
   if ii11iIII11II1I1Ii1 :
    if cookieJar == None :
     if 79 - 79: i11ii11iIi11i - iI11I1II1I1I + o00ooo0 - ooO00oOoo
     cookie_jar_file = None
     if 'open[' in ii1iI [ 'cookiejar' ] :
      cookie_jar_file = ii1iI [ 'cookiejar' ] . split ( 'open[' ) [ 1 ] . split ( ']' ) [ 0 ]
      if 93 - 93: ooO0OO000o . I11i11Ii - i1iIi11iIIi1I + oOoO0oo0OOOo
      if 61 - 61: ooO0OO000o
     cookieJar = Ii1ii111i1 ( cookie_jar_file )
     if 31 - 31: Oo0ooO0oo0oO + o0o00Oo0O
     if cookie_jar_file :
      oO0oOOoo00000 ( cookieJar , cookie_jar_file )
      if 52 - 52: I11i11Ii
      if 51 - 51: Oo0oO0ooo
      if 88 - 88: ii
    elif 'save[' in ii1iI [ 'cookiejar' ] :
     cookie_jar_file = ii1iI [ 'cookiejar' ] . split ( 'save[' ) [ 1 ] . split ( ']' ) [ 0 ]
     OO00 = os . path . join ( ooOOOo0oo0O0 , cookie_jar_file )
     if 28 - 28: o0OO0 - Ii . Iii1ii1II11i + Oo0oO0ooo / Iii1ii1II11i
     oO0oOOoo00000 ( cookieJar , cookie_jar_file )
   if ii1iI [ 'page' ] and '$doregex' in ii1iI [ 'page' ] :
    i11iIiI11I1i = Ooooooo ( regexs , ii1iI [ 'page' ] , cookieJar , recursiveCall = True , cachedPages = cachedPages )
    if len ( i11iIiI11I1i ) == 0 :
     i11iIiI11I1i = 'http://regexfailed'
    ii1iI [ 'page' ] = i11iIiI11I1i
    if 41 - 41: o00ooo0
   if 'setcookie' in ii1iI and ii1iI [ 'setcookie' ] and '$doregex' in ii1iI [ 'setcookie' ] :
    ii1iI [ 'setcookie' ] = Ooooooo ( regexs , ii1iI [ 'setcookie' ] , cookieJar , recursiveCall = True , cachedPages = cachedPages )
   if 'appendcookie' in ii1iI and ii1iI [ 'appendcookie' ] and '$doregex' in ii1iI [ 'appendcookie' ] :
    ii1iI [ 'appendcookie' ] = Ooooooo ( regexs , ii1iI [ 'appendcookie' ] , cookieJar , recursiveCall = True , cachedPages = cachedPages )
    if 77 - 77: ooO00oOoo
    if 65 - 65: ooO0OO000o . I11i11Ii % o0OO0 * i11ii11iIi11i
   if 'post' in ii1iI and '$doregex' in ii1iI [ 'post' ] :
    ii1iI [ 'post' ] = Ooooooo ( regexs , ii1iI [ 'post' ] , cookieJar , recursiveCall = True , cachedPages = cachedPages )
    if 38 - 38: oOoO0oo0OOOo / o00 % i1iIi11iIIi1I
    if 11 - 11: o00 - o0OO0 + ooO0OO000o - iI11I1II1I1I
   if 'rawpost' in ii1iI and '$doregex' in ii1iI [ 'rawpost' ] :
    ii1iI [ 'rawpost' ] = Ooooooo ( regexs , ii1iI [ 'rawpost' ] , cookieJar , recursiveCall = True , cachedPages = cachedPages , rawPost = True )
    if 7 - 7: Oo0oO0ooo - I1i1iI1i / ooO0OO000o * o00ooo0 . o00 * o00
    if 61 - 61: I1i1iI1i % O0OOo - i11ii11iIi11i / i1iIi11iIIi1I
   if 'rawpost' in ii1iI and '$epoctime$' in ii1iI [ 'rawpost' ] :
    ii1iI [ 'rawpost' ] = ii1iI [ 'rawpost' ] . replace ( '$epoctime$' , Ii1iI111 ( ) )
    if 51 - 51: Oo0oO0ooo * o0o00Oo0O / ooO0OO000o . o00ooo0 % Oo0ooO0oo0oO / I11i11Ii
   if 'rawpost' in ii1iI and '$epoctime2$' in ii1iI [ 'rawpost' ] :
    ii1iI [ 'rawpost' ] = ii1iI [ 'rawpost' ] . replace ( '$epoctime2$' , ii1iii1I1I ( ) )
    if 95 - 95: Oo0oO0ooo
    if 51 - 51: ooO0OO000o + Oo0oO0ooo . ii1I . Iii1ii1II11i + oOoO0oo0OOOo * I11i11Ii
   OOoOoo0 = ''
   if ii1iI [ 'page' ] and ii1iI [ 'page' ] in cachedPages and not 'ignorecache' in ii1iI and forCookieJarOnly == False :
    if 17 - 17: o00ooo0 + o0OO0 . i11ii11iIi11i - i1iIi11iIIi1I * Ii
    OOoOoo0 = cachedPages [ ii1iI [ 'page' ] ]
   else :
    if ii1iI [ 'page' ] and not ii1iI [ 'page' ] == '' and ii1iI [ 'page' ] . startswith ( 'http' ) :
     if '$epoctime$' in ii1iI [ 'page' ] :
      ii1iI [ 'page' ] = ii1iI [ 'page' ] . replace ( '$epoctime$' , Ii1iI111 ( ) )
     if '$epoctime2$' in ii1iI [ 'page' ] :
      ii1iI [ 'page' ] = ii1iI [ 'page' ] . replace ( '$epoctime2$' , ii1iii1I1I ( ) )
      if 20 - 20: I11i11Ii . ii % Oo0ooO0oo0oO
      if 63 - 63: I11i11Ii % iI11I1II1I1I
     I1ii = ii1iI [ 'page' ] . split ( '|' )
     O00O0O = I1ii [ 0 ]
     i1ii1iiI = None
     if len ( I1ii ) > 1 :
      i1ii1iiI = I1ii [ 1 ]
      if 19 - 19: i11ii11iIi11i * I1i1iI1i / I1i1iI1i . ii - Oo0ooO0oo0oO + Ii
      if 88 - 88: Ii - O0OOo
      if 67 - 67: Oo0ooO0oo0oO . i1iIi11iIIi1I + oOoO0oo0OOOo - ii
      if 70 - 70: Oo0ooO0oo0oO / ooO0OO000o - iI11I1II1I1I - o00
      if 11 - 11: iI11I1II1I1I . ii . ooO0OO000o / ii1I - I1i1iI1i
      if 30 - 30: oOoO0oo0OOOo
      if 21 - 21: Ii / ooO00oOoo % Oo0ooO0oo0oO * o0o00Oo0O . I1i1iI1i - iI11I1II1I1I
      if 26 - 26: ooO0OO000o * oOoO0oo0OOOo
      if 10 - 10: ooO0OO000o . o00
      if 32 - 32: o00ooo0 . Oo0oO0ooo . ii - i11ii11iIi11i + o0OO0
     ooO0oO00O0o = urllib2 . ProxyHandler ( urllib2 . getproxies ( ) )
     if 70 - 70: ooO00oOoo
     if 16 - 16: o00 - ii % i1iIi11iIIi1I
     if 36 - 36: Oo0ooO0oo0oO
     ii1ii1ii = urllib2 . Request ( O00O0O )
     if 'proxy' in ii1iI :
      O0o = ii1iI [ 'proxy' ]
      if 42 - 42: ooO0OO000o
      if 32 - 32: o00ooo0 % Iii1ii1II11i - Oo0ooO0oo0oO * IiiI + I1i1iI1i
      if O00O0O [ : 5 ] == "https" :
       II1I = urllib2 . ProxyHandler ( { 'https' : O0o } )
       if 84 - 84: o0o00Oo0O * ii - Oo0oO0ooo * Oo0oO0ooo
      else :
       II1I = urllib2 . ProxyHandler ( { 'http' : O0o } )
       if 8 - 8: O0OOo / ii1I . o0OO0
      i1I1IiI = urllib2 . build_opener ( II1I )
      urllib2 . install_opener ( i1I1IiI )
      if 66 - 66: i11ii11iIi11i
      if 56 - 56: o0o00Oo0O
     ii1ii1ii . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20100101 Firefox/14.0.1' )
     O0o = None
     if 61 - 61: IiiI / Oo0ooO0oo0oO / i1iIi11iIIi1I * o0o00Oo0O
     if 'referer' in ii1iI :
      ii1ii1ii . add_header ( 'Referer' , ii1iI [ 'referer' ] )
     if 'accept' in ii1iI :
      ii1ii1ii . add_header ( 'Accept' , ii1iI [ 'accept' ] )
     if 'agent' in ii1iI :
      ii1ii1ii . add_header ( 'User-agent' , ii1iI [ 'agent' ] )
     if 'x-req' in ii1iI :
      ii1ii1ii . add_header ( 'X-Requested-With' , ii1iI [ 'x-req' ] )
     if 'x-addr' in ii1iI :
      ii1ii1ii . add_header ( 'x-addr' , ii1iI [ 'x-addr' ] )
     if 'x-forward' in ii1iI :
      ii1ii1ii . add_header ( 'X-Forwarded-For' , ii1iI [ 'x-forward' ] )
     if 'setcookie' in ii1iI :
      if 23 - 23: o0OO0 - Oo0ooO0oo0oO + I1i1iI1i
      ii1ii1ii . add_header ( 'Cookie' , ii1iI [ 'setcookie' ] )
     if 'appendcookie' in ii1iI :
      if 12 - 12: I11i11Ii / O0OOo % IiiI / Ii % ii
      IiIi1II11i = ii1iI [ 'appendcookie' ]
      IiIi1II11i = IiIi1II11i . split ( ';' )
      for ii111111I1iII in IiIi1II11i :
       O00ooo0O0 , i1iIi1iIi1i = ii111111I1iII . split ( '=' )
       II1II1iIIi11 , O00ooo0O0 = O00ooo0O0 . split ( ':' )
       IiI1iII1II111 = cookielib . Cookie ( version = 0 , name = O00ooo0O0 , value = i1iIi1iIi1i , port = None , port_specified = False , domain = II1II1iIIi11 , domain_specified = False , domain_initial_dot = False , path = '/' , path_specified = True , secure = False , expires = None , discard = True , comment = None , comment_url = None , rest = { 'HttpOnly' : None } , rfc2109 = False )
       cookieJar . set_cookie ( IiI1iII1II111 )
     if 'origin' in ii1iI :
      ii1ii1ii . add_header ( 'Origin' , ii1iI [ 'origin' ] )
     if i1ii1iiI :
      i1ii1iiI = i1ii1iiI . split ( '&' )
      for ii111111I1iII in i1ii1iiI :
       if ii111111I1iII . split ( '=' ) == 2 :
        O00ooo0O0 , i1iIi1iIi1i = ii111111I1iII . split ( '=' )
       else :
        I1I1iIiII1 = ii111111I1iII . split ( '=' )
        O00ooo0O0 = I1I1iIiII1 [ 0 ]
        i1iIi1iIi1i = '=' . join ( I1I1iIiII1 [ 1 : ] )
        if 28 - 28: oOoO0oo0OOOo * i11ii11iIi11i . I1i1iI1i % I1i1iI1i / I1i1iI1i * ooO00oOoo
       ii1ii1ii . add_header ( O00ooo0O0 , i1iIi1iIi1i )
       if 64 - 64: ooO0OO000o - I11i11Ii
     if not cookieJar == None :
      if 68 - 68: O0OOo - Oo0ooO0oo0oO - iI11I1II1I1I / oOoO0oo0OOOo + Oo0ooO0oo0oO - i11ii11iIi11i
      O00Oo = urllib2 . HTTPCookieProcessor ( cookieJar )
      i1I1IiI = urllib2 . build_opener ( O00Oo , urllib2 . HTTPBasicAuthHandler ( ) , urllib2 . HTTPHandler ( ) )
      i1I1IiI = urllib2 . install_opener ( i1I1IiI )
      if 15 - 15: o00ooo0 / ooO0OO000o . o00 / ooO0OO000o % o00ooo0
      if 4 - 4: Oo0oO0ooo . Oo0oO0ooo % Iii1ii1II11i % o00ooo0 / o00ooo0
      if 'noredirect' in ii1iI :
       i1I1IiI = urllib2 . build_opener ( O00Oo , oOo , urllib2 . HTTPBasicAuthHandler ( ) , urllib2 . HTTPHandler ( ) )
       i1I1IiI = urllib2 . install_opener ( i1I1IiI )
     elif 'noredirect' in ii1iI :
      i1I1IiI = urllib2 . build_opener ( oOo , urllib2 . HTTPBasicAuthHandler ( ) , urllib2 . HTTPHandler ( ) )
      i1I1IiI = urllib2 . install_opener ( i1I1IiI )
      if 29 - 29: i1iIi11iIIi1I * O0OOo * Iii1ii1II11i / Ii
      if 26 - 26: Oo0oO0ooo % ooO00oOoo % o0OO0 % o00ooo0
     if 'connection' in ii1iI :
      if 55 - 55: O0OOo % ii / ii % ii
      from keepalive import HTTPHandler
      oOoOoo0 = HTTPHandler ( )
      i1I1IiI = urllib2 . build_opener ( oOoOoo0 )
      urllib2 . install_opener ( i1I1IiI )
      if 16 - 16: I11i11Ii
      if 6 - 6: Oo0ooO0oo0oO - Iii1ii1II11i + o00ooo0 + ii1I / o0o00Oo0O / IiiI
      if 42 - 42: ii1I . I11i11Ii / ii1I + o00ooo0
     O0o0O0OO00o = None
     if 92 - 92: IiiI + ooO00oOoo / i1iIi11iIIi1I % i11ii11iIi11i % Oo0oO0ooo . ii
     if 'post' in ii1iI :
      O0Oo = ii1iI [ 'post' ]
      if 7 - 7: Oo0oO0ooo % iI11I1II1I1I + I1i1iI1i - o00ooo0 * o0OO0
      if 94 - 94: oOoO0oo0OOOo . o0o00Oo0O / o00ooo0 . Iii1ii1II11i - ii1I
      if 26 - 26: i11ii11iIi11i - Oo0ooO0oo0oO . IiiI
      if 65 - 65: Iii1ii1II11i % o0o00Oo0O % iI11I1II1I1I * o00ooo0
      iIIIIIiI1I1 = O0Oo . split ( ',' ) ;
      O0o0O0OO00o = { }
      for I11I1IIiiII1 in iIIIIIiI1I1 :
       O00ooo0O0 = I11I1IIiiII1 . split ( ':' ) [ 0 ] ;
       i1iIi1iIi1i = I11I1IIiiII1 . split ( ':' ) [ 1 ] ;
       O0o0O0OO00o [ O00ooo0O0 ] = i1iIi1iIi1i
      O0o0O0OO00o = urllib . urlencode ( O0o0O0OO00o )
      if 31 - 31: I11i11Ii * o0OO0 + ii - o00 / ii
     if 'rawpost' in ii1iI :
      O0o0O0OO00o = ii1iI [ 'rawpost' ]
      if 19 - 19: Oo0oO0ooo * O0OOo * IiiI + o0o00Oo0O / o0o00Oo0O
      if 73 - 73: iI11I1II1I1I / iI11I1II1I1I - o0OO0
      if 91 - 91: o0OO0 + I11i11Ii
      if 59 - 59: I11i11Ii + Ii + ii1I / I1i1iI1i
     OOoOoo0 = ''
     try :
      if 44 - 44: I1i1iI1i . oOoO0oo0OOOo * I11i11Ii + ii - o00 - Oo0oO0ooo
      if O0o0O0OO00o :
       oooooOoo0ooo = urllib2 . urlopen ( ii1ii1ii , O0o0O0OO00o )
      else :
       oooooOoo0ooo = urllib2 . urlopen ( ii1ii1ii )
      if oooooOoo0ooo . info ( ) . get ( 'Content-Encoding' ) == 'gzip' :
       from StringIO import StringIO
       import gzip
       I1iii = StringIO ( oooooOoo0ooo . read ( ) )
       oOO0OO0O = gzip . GzipFile ( fileobj = I1iii )
       OOoOoo0 = oOO0OO0O . read ( )
      else :
       OOoOoo0 = oooooOoo0ooo . read ( )
       if 78 - 78: o00ooo0 / ooO0OO000o % oOoO0oo0OOOo
       if 52 - 52: Oo0ooO0oo0oO - o00 * o0OO0
       if 17 - 17: ii + Oo0ooO0oo0oO * I1i1iI1i * oOoO0oo0OOOo
      if 'proxy' in ii1iI and not ooO0oO00O0o is None :
       urllib2 . install_opener ( urllib2 . build_opener ( ooO0oO00O0o ) )
       if 36 - 36: o0o00Oo0O + i1iIi11iIIi1I
      OOoOoo0 = iIIIi1i1I11i ( OOoOoo0 )
      if 55 - 55: i1iIi11iIIi1I - Oo0ooO0oo0oO
      if 84 - 84: ooO00oOoo + i1iIi11iIIi1I - oOoO0oo0OOOo * oOoO0oo0OOOo
      if 'includeheaders' in ii1iI :
       if 61 - 61: ii . o0OO0 . ii / i1iIi11iIIi1I
       OOoOoo0 += '$$HEADERS_START$$:'
       for oO0 in oooooOoo0ooo . headers :
        OOoOoo0 += oO0 + ':' + oooooOoo0ooo . headers . get ( oO0 ) + '\n'
       OOoOoo0 += '$$HEADERS_END$$:'
       if 72 - 72: ii1I
      oO0ooO0OoOOOO ( OOoOoo0 )
      oO0ooO0OoOOOO ( cookieJar )
      if 82 - 82: oOoO0oo0OOOo + ii / Ii * Iii1ii1II11i . ii
      oooooOoo0ooo . close ( )
     except :
      pass
     cachedPages [ ii1iI [ 'page' ] ] = OOoOoo0
     if 63 - 63: Iii1ii1II11i
     if 6 - 6: O0OOo / Iii1ii1II11i
     if 57 - 57: I1i1iI1i
     if forCookieJarOnly :
      return cookieJar
    elif ii1iI [ 'page' ] and not ii1iI [ 'page' ] . startswith ( 'http' ) :
     if ii1iI [ 'page' ] . startswith ( '$pyFunction:' ) :
      oO0oO00oOo0OOO = o0oOOoooOOOOo ( ii1iI [ 'page' ] . split ( '$pyFunction:' ) [ 1 ] , '' , cookieJar , ii1iI )
      if forCookieJarOnly :
       return cookieJar
      OOoOoo0 = oO0oO00oOo0OOO
      OOoOoo0 = iIIIi1i1I11i ( OOoOoo0 )
     else :
      OOoOoo0 = ii1iI [ 'page' ]
   if '$pyFunction:playmedia(' in ii1iI [ 'expres' ] or 'ActivateWindow' in ii1iI [ 'expres' ] or 'RunPlugin' in ii1iI [ 'expres' ] or '$PLAYERPROXY$=' in url or any ( x in url for x in OOoO000O0OO ) :
    Iii = False
   if '$doregex' in ii1iI [ 'expres' ] :
    ii1iI [ 'expres' ] = Ooooooo ( regexs , ii1iI [ 'expres' ] , cookieJar , recursiveCall = True , cachedPages = cachedPages )
    if 23 - 23: ii1I . IiiI * i11ii11iIi11i
   if not ii1iI [ 'expres' ] == '' :
    if 15 - 15: oOoO0oo0OOOo
    if '$LiveStreamCaptcha' in ii1iI [ 'expres' ] :
     oO0oO00oOo0OOO = oOoOoO000OO ( ii1iI , OOoOoo0 , cookieJar )
     if 38 - 38: IiiI
     url = url . replace ( "$doregex[" + I1iiiiI1iI + "]" , oO0oO00oOo0OOO )
     if 23 - 23: i1iIi11iIIi1I % I1i1iI1i - Oo0ooO0oo0oO % iI11I1II1I1I . oOoO0oo0OOOo
    elif ii1iI [ 'expres' ] . startswith ( '$pyFunction:' ) or '#$pyFunction' in ii1iI [ 'expres' ] :
     if 24 - 24: Oo0oO0ooo / ii + o00ooo0 % iI11I1II1I1I - Oo0ooO0oo0oO . Oo0ooO0oo0oO
     oO0oO00oOo0OOO = ''
     if ii1iI [ 'expres' ] . startswith ( '$pyFunction:' ) :
      oO0oO00oOo0OOO = o0oOOoooOOOOo ( ii1iI [ 'expres' ] . split ( '$pyFunction:' ) [ 1 ] , OOoOoo0 , cookieJar , ii1iI )
     else :
      oO0oO00oOo0OOO = iIi ( ii1iI [ 'expres' ] , OOoOoo0 , cookieJar , ii1iI )
     if 'ActivateWindow' in ii1iI [ 'expres' ] or 'RunPlugin' in ii1iI [ 'expres' ] : return '' , False
     if forCookieJarOnly :
      return cookieJar
     if 'listrepeat' in ii1iI :
      oo00O0 = ii1iI [ 'listrepeat' ]
      if 49 - 49: ooO0OO000o - I11i11Ii / I1i1iI1i
      if 74 - 74: I1i1iI1i - Oo0ooO0oo0oO + ii1I . I11i11Ii + Oo0ooO0oo0oO - I1i1iI1i
      return oo00O0 , eval ( oO0oO00oOo0OOO ) , ii1iI , regexs , cookieJar
      if 17 - 17: o0o00Oo0O . ooO00oOoo . o0o00Oo0O + o0o00Oo0O / i1iIi11iIIi1I . O0OOo
      if 62 - 62: Iii1ii1II11i % o00 * i11ii11iIi11i - ii1I
      if 66 - 66: Ii / IiiI - ii / ii1I . Ii
     try :
      url = url . replace ( u"$doregex[" + I1iiiiI1iI + "]" , oO0oO00oOo0OOO )
     except : url = url . replace ( "$doregex[" + I1iiiiI1iI + "]" , oO0oO00oOo0OOO . decode ( "utf-8" ) )
    else :
     if 'listrepeat' in ii1iI :
      oo00O0 = ii1iI [ 'listrepeat' ]
      if 16 - 16: i1iIi11iIIi1I % Iii1ii1II11i + I1i1iI1i - o0o00Oo0O . o00 / ooO00oOoo
      if 35 - 35: o0OO0 / ooO00oOoo / ooO0OO000o - iI11I1II1I1I + ooO0OO000o . ooO00oOoo
      if 81 - 81: o00 * Oo0ooO0oo0oO - Iii1ii1II11i * o00ooo0 % oOoO0oo0OOOo * oOoO0oo0OOOo
      if 59 - 59: iI11I1II1I1I
      I1ii1Ii1ii11i = re . findall ( ii1iI [ 'expres' ] , OOoOoo0 )
      if 94 - 94: Oo0oO0ooo + ooO00oOoo / Oo0ooO0oo0oO
      return oo00O0 , I1ii1Ii1ii11i , ii1iI , regexs , cookieJar
      if 91 - 91: I1i1iI1i / ii1I * ii1I
     oO0oO00oOo0OOO = ''
     if not OOoOoo0 == '' :
      if 25 - 25: iI11I1II1I1I . Oo0ooO0oo0oO * o0OO0 - o00ooo0
      oOO000O = re . compile ( ii1iI [ 'expres' ] ) . search ( OOoOoo0 )
      try :
       oO0oO00oOo0OOO = oOO000O . group ( 1 ) . strip ( )
      except : traceback . print_exc ( )
     elif ii1iI [ 'page' ] == '' or ii1iI [ 'page' ] == None :
      oO0oO00oOo0OOO = ii1iI [ 'expres' ]
      if 99 - 99: ii1I / o0o00Oo0O - oOoO0oo0OOOo % IiiI - Oo0ooO0oo0oO + ii
     if rawPost :
      if 98 - 98: Oo0ooO0oo0oO + ii1I . I11i11Ii - ooO0OO000o - IiiI
      oO0oO00oOo0OOO = urllib . quote_plus ( oO0oO00oOo0OOO )
     if 'htmlunescape' in ii1iI :
      if 24 - 24: i1iIi11iIIi1I - ii1I + I1i1iI1i
      import HTMLParser
      oO0oO00oOo0OOO = HTMLParser . HTMLParser ( ) . unescape ( oO0oO00oOo0OOO )
     try :
      url = url . replace ( "$doregex[" + I1iiiiI1iI + "]" , oO0oO00oOo0OOO )
     except : url = url . replace ( "$doregex[" + I1iiiiI1iI + "]" , oO0oO00oOo0OOO . decode ( "utf-8" ) )
     if 38 - 38: ii / Iii1ii1II11i . o0o00Oo0O / ii1I / i1iIi11iIIi1I + iI11I1II1I1I
     if 96 - 96: o00
   else :
    url = url . replace ( "$doregex[" + I1iiiiI1iI + "]" , '' )
 if '$epoctime$' in url :
  url = url . replace ( '$epoctime$' , Ii1iI111 ( ) )
 if '$epoctime2$' in url :
  url = url . replace ( '$epoctime2$' , ii1iii1I1I ( ) )
  if 18 - 18: o00 * I1i1iI1i - o00ooo0
 if '$GUID$' in url :
  import uuid
  url = url . replace ( '$GUID$' , str ( uuid . uuid1 ( ) ) . upper ( ) )
 if '$get_cookies$' in url :
  url = url . replace ( '$get_cookies$' , II1i1III ( cookieJar ) )
  if 34 - 34: ooO00oOoo - Ii / iI11I1II1I1I
 if recursiveCall : return url
 if 87 - 87: Iii1ii1II11i / ii - i1iIi11iIIi1I % oOoO0oo0OOOo % Oo0oO0ooo % i1iIi11iIIi1I
 if url == "" :
  return
 else :
  return url , Iii
def Ii1 ( t ) :
 import hashlib
 ii111111I1iII = hashlib . md5 ( )
 ii111111I1iII . update ( t )
 return ii111111I1iII . hexdigest ( )
 if 34 - 34: o00 - ii . I11i11Ii / ooO0OO000o
def II1II ( encrypted ) :
 oo0O = ""
 if 95 - 95: ii . o0o00Oo0O . IiiI * i1iIi11iIIi1I . o00ooo0
 if 9 - 9: Oo0ooO0oo0oO . Oo0oO0ooo
 if 31 - 31: o0OO0 / iI11I1II1I1I
 if 84 - 84: Oo0ooO0oo0oO
 if 87 - 87: O0OOo + IiiI
def i1iIIIIIIiII1 ( media_url ) :
 try :
  import CustomPlayer
  iii11 = CustomPlayer . MyXBMCPlayer ( )
  i1oO = xbmcgui . ListItem ( label = str ( OO0Oooo0oOO0O ) , iconImage = "DefaultVideo.png" , thumbnailImage = xbmc . getInfoImage ( "ListItem.Thumb" ) , path = media_url )
  iii11 . play ( media_url , i1oO )
  xbmc . sleep ( 1000 )
  while iii11 . is_active :
   xbmc . sleep ( 200 )
 except :
  traceback . print_exc ( )
 return ''
 if 30 - 30: i1iIi11iIIi1I . i11ii11iIi11i
def o0Oii1111i ( params ) :
 I1I1IiI1 = json . dumps ( params )
 O0ooOO = xbmc . executeJSONRPC ( I1I1IiI1 )
 if 28 - 28: Ii / IiiI . iI11I1II1I1I / ooO0OO000o
 try :
  oooooOoo0ooo = json . loads ( O0ooOO )
 except UnicodeDecodeError :
  oooooOoo0ooo = json . loads ( O0ooOO . decode ( 'utf-8' , 'ignore' ) )
  if 72 - 72: ii / I11i11Ii + o00ooo0 / oOoO0oo0OOOo * o00ooo0
 try :
  if 'result' in oooooOoo0ooo :
   return oooooOoo0ooo [ 'result' ]
  return None
 except KeyError :
  logger . warn ( "[%s] %s" % ( params [ 'method' ] , oooooOoo0ooo [ 'error' ] [ 'message' ] ) )
  return None
  if 34 - 34: o0o00Oo0O * o0o00Oo0O % ii + o00 * iI11I1II1I1I % o00ooo0
  if 25 - 25: I1i1iI1i + oOoO0oo0OOOo . IiiI % oOoO0oo0OOOo * Oo0ooO0oo0oO
def ii1IiIi11 ( proxysettings = None ) :
 if 22 - 22: o0OO0
 if proxysettings == None :
  if 33 - 33: iI11I1II1I1I / o00ooo0
  xbmc . executeJSONRPC ( '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"network.usehttpproxy", "value":false}, "id":1}' )
 else :
  if 1 - 1: o00ooo0
  IiiiI1 = proxysettings . split ( ':' )
  OOOo0 = IiiiI1 [ 0 ]
  OOo0Oo0OOo0 = IiiiI1 [ 1 ]
  i1i11I = IiiiI1 [ 2 ]
  iiIiI = None
  i1oOOOOOOOoO = None
  if 12 - 12: o00 . Oo0oO0ooo . oOoO0oo0OOOo / o0o00Oo0O
  if len ( IiiiI1 ) > 3 and '@' in IiiiI1 [ 3 ] :
   iiIiI = IiiiI1 [ 3 ] . split ( '@' ) [ 0 ]
   i1oOOOOOOOoO = IiiiI1 [ 3 ] . split ( '@' ) [ 1 ]
   if 58 - 58: IiiI - ooO0OO000o % o0OO0 + ooO00oOoo . oOoO0oo0OOOo / Oo0oO0ooo
   if 8 - 8: Iii1ii1II11i . i11ii11iIi11i * I1i1iI1i + ooO0OO000o % Ii
  xbmc . executeJSONRPC ( '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"network.usehttpproxy", "value":true}, "id":1}' )
  xbmc . executeJSONRPC ( '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"network.httpproxytype", "value":' + str ( i1i11I ) + '}, "id":1}' )
  xbmc . executeJSONRPC ( '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"network.httpproxyserver", "value":"' + str ( OOOo0 ) + '"}, "id":1}' )
  xbmc . executeJSONRPC ( '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"network.httpproxyport", "value":' + str ( OOo0Oo0OOo0 ) + '}, "id":1}' )
  if 8 - 8: O0OOo * o0o00Oo0O
  if 73 - 73: IiiI / o0OO0 / I1i1iI1i / i11ii11iIi11i
  if not iiIiI == None :
   xbmc . executeJSONRPC ( '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"network.httpproxyusername", "value":"' + str ( iiIiI ) + '"}, "id":1}' )
   xbmc . executeJSONRPC ( '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"network.httpproxypassword", "value":"' + str ( i1oOOOOOOOoO ) + '"}, "id":1}' )
   if 11 - 11: oOoO0oo0OOOo + Oo0oO0ooo - ii / i11ii11iIi11i
   if 34 - 34: O0OOo
def i1iI1 ( ) :
 IIi11i1II = o0Oii1111i ( { 'jsonrpc' : '2.0' , "method" : "Settings.GetSettingValue" , "params" : { "setting" : "network.usehttpproxy" } , 'id' : 1 } ) [ 'value' ]
 if 73 - 73: IiiI - I11i11Ii * ii1I / Ii * Oo0ooO0oo0oO % ooO0OO000o
 i1i11I = o0Oii1111i ( { 'jsonrpc' : '2.0' , "method" : "Settings.GetSettingValue" , "params" : { "setting" : "network.httpproxytype" } , 'id' : 1 } ) [ 'value' ]
 if 56 - 56: ii * i1iIi11iIIi1I . i1iIi11iIIi1I . Iii1ii1II11i
 if IIi11i1II :
  OOOo0 = o0Oii1111i ( { 'jsonrpc' : '2.0' , "method" : "Settings.GetSettingValue" , "params" : { "setting" : "network.httpproxyserver" } , 'id' : 1 } ) [ 'value' ]
  OOo0Oo0OOo0 = unicode ( o0Oii1111i ( { 'jsonrpc' : '2.0' , "method" : "Settings.GetSettingValue" , "params" : { "setting" : "network.httpproxyport" } , 'id' : 1 } ) [ 'value' ] )
  iiIiI = o0Oii1111i ( { 'jsonrpc' : '2.0' , "method" : "Settings.GetSettingValue" , "params" : { "setting" : "network.httpproxyusername" } , 'id' : 1 } ) [ 'value' ]
  i1oOOOOOOOoO = o0Oii1111i ( { 'jsonrpc' : '2.0' , "method" : "Settings.GetSettingValue" , "params" : { "setting" : "network.httpproxypassword" } , 'id' : 1 } ) [ 'value' ]
  if 24 - 24: i1iIi11iIIi1I . I1i1iI1i * o00ooo0 % o00 / Oo0ooO0oo0oO
  if iiIiI and i1oOOOOOOOoO and OOOo0 and OOo0Oo0OOo0 :
   return OOOo0 + ':' + str ( OOo0Oo0OOo0 ) + ':' + str ( i1i11I ) + ':' + iiIiI + '@' + i1oOOOOOOOoO
  elif OOOo0 and OOo0Oo0OOo0 :
   return OOOo0 + ':' + str ( OOo0Oo0OOo0 ) + ':' + str ( i1i11I )
 else :
  return None
  if 58 - 58: I11i11Ii - Iii1ii1II11i % o0o00Oo0O . I11i11Ii % i11ii11iIi11i % Oo0oO0ooo
def oOo0OooOo ( media_url , name , iconImage , proxyip , port , proxyuser = None , proxypass = None ) :
 if 51 - 51: I1i1iI1i . i1iIi11iIIi1I
 if media_url == None or media_url == '' :
  xbmc . executebuiltin ( "XBMC.Notification(tvchopo,Unable to play empty Url,5000," + IIiiiiiiIi1I1 + ")" )
  return
 IiiIiiIi = xbmcgui . DialogProgress ( )
 IiiIiiIi . create ( 'Progress' , 'Playing with custom proxy' )
 IiiIiiIi . update ( 10 , "" , "setting proxy.." , "" )
 i1iiIIIi = False
 Oo0o = ''
 if 93 - 93: Oo0ooO0oo0oO
 try :
  if 43 - 43: Iii1ii1II11i / I11i11Ii . O0OOo
  Oo0o = i1iI1 ( )
  print 'existing_proxy' , Oo0o
  if 62 - 62: iI11I1II1I1I + o00 . i1iIi11iIIi1I / Oo0oO0ooo % o0o00Oo0O . ooO00oOoo
  if 93 - 93: Ii % iI11I1II1I1I % Ii + IiiI / IiiI / ooO0OO000o
  if not proxyuser == None :
   ii1IiIi11 ( proxyip + ':' + port + ':0:' + proxyuser + '@' + proxypass )
  else :
   ii1IiIi11 ( proxyip + ':' + port + ':0' )
   if 49 - 49: Oo0ooO0oo0oO . Iii1ii1II11i . Ii - ooO0OO000o / o00ooo0
  print 'proxy setting complete playing' , media_url
  i1iiIIIi = True
  IiiIiiIi . update ( 80 , "" , "setting proxy complete, now playing" , "" )
  if 62 - 62: Oo0ooO0oo0oO
  if 1 - 1: Oo0oO0ooo / Oo0oO0ooo - Ii
  import CustomPlayer
  iii11 = CustomPlayer . MyXBMCPlayer ( )
  iii11 . pdialogue == IiiIiiIi
  i1oO = xbmcgui . ListItem ( label = str ( name ) , iconImage = iconImage , thumbnailImage = xbmc . getInfoImage ( "ListItem.Thumb" ) , path = media_url )
  iii11 . play ( media_url , i1oO )
  xbmc . sleep ( 1000 )
  if 87 - 87: i1iIi11iIIi1I / o0o00Oo0O * Oo0oO0ooo / IiiI
  if 19 - 19: ooO00oOoo + ii1I . I11i11Ii - i1iIi11iIIi1I
  import time
  iIi1I1 = time . time ( )
  try :
   while iii11 . is_active :
    xbmc . sleep ( 1000 )
    if iii11 . urlplayed == False and time . time ( ) - iIi1I1 > 12 :
     print 'failed!!!'
     xbmc . executebuiltin ( "XBMC.Notification(tvchopo,Unable to play check proxy,5000," + IIiiiiiiIi1I1 + ")" )
     break
     if 63 - 63: o00 * Iii1ii1II11i . ii / Oo0ooO0oo0oO * i1iIi11iIIi1I . O0OOo
  except : pass
  if 62 - 62: ii1I / O0OOo . I11i11Ii * IiiI
  IiiIiiIi . close ( )
  IiiIiiIi = None
 except :
  traceback . print_exc ( )
 if IiiIiiIi :
  IiiIiiIi . close ( )
 if i1iiIIIi :
  print 'now resetting the proxy back'
  ii1IiIi11 ( Oo0o )
  print 'reset here'
 return ''
 if 21 - 21: IiiI
 if 81 - 81: I1i1iI1i / iI11I1II1I1I - O0OOo * ooO00oOoo . I11i11Ii * Iii1ii1II11i
def o0000 ( page_value , referer = None ) :
 if referer :
  referer = [ ( 'Referer' , referer ) ]
 if page_value . startswith ( "http" ) :
  i111i1i = page_value
  page_value = IiI11iI1i1i1i ( page_value , headers = referer )
  if 19 - 19: ooO0OO000o - ii1I - Oo0ooO0oo0oO / Oo0ooO0oo0oO + oOoO0oo0OOOo
 OO0Oooo0oo = "(eval\(function\(p,a,c,k,e,(?:r|d).*)"
 if 42 - 42: o00ooo0 * ooO00oOoo . Oo0oO0ooo * I11i11Ii + oOoO0oo0OOOo
 i1i1II11II1 = re . compile ( OO0Oooo0oo ) . findall ( page_value )
 II1IIIii = ""
 if i1i1II11II1 and len ( i1i1II11II1 ) > 0 :
  for i1iIi1iIi1i in i1i1II11II1 :
   iIIIiIi1I1i = OoOOoO0oOo ( i1iIi1iIi1i )
   O0ooOOOO0O0 = IiI1iiiIii ( iIIIiIi1I1i , '\'(.*?)\'' )
   if 'unescape' in iIIIiIi1I1i :
    iIIIiIi1I1i = urllib . unquote ( O0ooOOOO0O0 )
   II1IIIii += iIIIiIi1I1i + '\n'
   if 38 - 38: ooO00oOoo % Oo0ooO0oo0oO - ii
   if 87 - 87: i11ii11iIi11i % I11i11Ii
  i111i1i = IiI1iiiIii ( II1IIIii , 'src="(.*?)"' )
  if 77 - 77: iI11I1II1I1I - ii1I . o0OO0
  page_value = IiI11iI1i1i1i ( i111i1i , headers = referer )
  if 26 - 26: IiiI * Oo0oO0ooo . ii1I
  if 59 - 59: o0o00Oo0O + ii1I - IiiI
  if 62 - 62: Ii % Oo0ooO0oo0oO . Oo0oO0ooo . Oo0ooO0oo0oO
 ooOo0O0O0oOO0 = IiI1iiiIii ( page_value , 'streamer\'.*?\'(.*?)\'\)' )
 iIiIIi = IiI1iiiIii ( page_value , 'file\',\s\'(.*?)\'' )
 if 14 - 14: IiiI / Oo0ooO0oo0oO - iI11I1II1I1I - o0OO0 % O0OOo
 if 49 - 49: O0OOo * o0OO0 / IiiI / i1iIi11iIIi1I * iI11I1II1I1I
 return ooOo0O0O0oOO0 + ' playpath=' + iIiIIi + ' pageUrl=' + i111i1i
 if 57 - 57: oOoO0oo0OOOo - o0OO0 / O0OOo % Ii
def I11 ( page_value , referer = None ) :
 if referer :
  referer = [ ( 'Referer' , referer ) ]
 if page_value . startswith ( "http" ) :
  page_value = IiI11iI1i1i1i ( page_value , headers = referer )
 OO0Oooo0oo = "var a = (.*?);\s*var b = (.*?);\s*var c = (.*?);\s*var d = (.*?);\s*var f = (.*?);\s*var v_part = '(.*?)';"
 i1i1II11II1 = re . compile ( OO0Oooo0oo ) . findall ( page_value ) [ 0 ]
 if 100 - 100: Iii1ii1II11i + Ii - ii1I
 IIii1 , oO0 , IiiiI111I , III1I11i1iIi , oOO0OO0O , i1iIi1iIi1i = ( i1i1II11II1 )
 oOO0OO0O = int ( oOO0OO0O )
 IIii1 = int ( IIii1 ) / oOO0OO0O
 oO0 = int ( oO0 ) / oOO0OO0O
 IiiiI111I = int ( IiiiI111I ) / oOO0OO0O
 III1I11i1iIi = int ( III1I11i1iIi ) / oOO0OO0O
 if 69 - 69: i1iIi11iIIi1I * ooO0OO000o * O0OOo . o00 - Iii1ii1II11i
 I1ii1Ii1ii11i = 'rtmp://' + str ( IIii1 ) + '.' + str ( oO0 ) + '.' + str ( IiiiI111I ) + '.' + str ( III1I11i1iIi ) + i1iIi1iIi1i ;
 return I1ii1Ii1ii11i
 if 39 - 39: o00ooo0 * I11i11Ii % i11ii11iIi11i . oOoO0oo0OOOo
def iiii111IiIIi1 ( url , useragent = None ) :
 str = '#EXTM3U'
 str += '\n#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=361816'
 str += '\n' + url + '&bytes=0-200000'
 oOoOooOo0o0 = os . path . join ( ooOOOo0oo0O0 , 'testfile.m3u' )
 str += '\n'
 Oo0000o0O0O ( oOoOooOo0o0 , str )
 if 1 - 1: Iii1ii1II11i % oOoO0oo0OOOo . IiiI . I11i11Ii - I11i11Ii - Oo0oO0ooo
 return oOoOooOo0o0
 if 33 - 33: I11i11Ii / i11ii11iIi11i
def Oo0000o0O0O ( file_name , page_data , append = False ) :
 if append :
  oOO0OO0O = open ( file_name , 'a' )
  oOO0OO0O . write ( page_data )
  oOO0OO0O . close ( )
 else :
  oOO0OO0O = open ( file_name , 'wb' )
  oOO0OO0O . write ( page_data )
  oOO0OO0O . close ( )
  return ''
  if 12 - 12: ooO0OO000o
def IiIii1ii ( file_name ) :
 oOO0OO0O = open ( file_name , 'rb' )
 III1I11i1iIi = oOO0OO0O . read ( )
 oOO0OO0O . close ( )
 return III1I11i1iIi
 if 8 - 8: i11ii11iIi11i + oOoO0oo0OOOo . iI11I1II1I1I % o0o00Oo0O
def iI11Ii111 ( page_data ) :
 import re , base64 , urllib ;
 OOo00OO00Oo = page_data
 while 'geh(' in OOo00OO00Oo :
  if OOo00OO00Oo . startswith ( 'lol(' ) : OOo00OO00Oo = OOo00OO00Oo [ 5 : - 1 ]
  if 23 - 23: ooO00oOoo - Oo0ooO0oo0oO + o00ooo0 - oOoO0oo0OOOo * oOoO0oo0OOOo . i1iIi11iIIi1I
  OOo00OO00Oo = re . compile ( '"(.*?)"' ) . findall ( OOo00OO00Oo ) [ 0 ] ;
  OOo00OO00Oo = base64 . b64decode ( OOo00OO00Oo ) ;
  OOo00OO00Oo = urllib . unquote ( OOo00OO00Oo ) ;
 print OOo00OO00Oo
 return OOo00OO00Oo
 if 47 - 47: o0OO0 % iI11I1II1I1I
def IiI1IIIII1I ( page_data ) :
 if 35 - 35: o00ooo0 - o00ooo0 + ii1I - o0o00Oo0O - ooO00oOoo
 oOO0o0oo0 = IiI11iI1i1i1i ( page_data ) ;
 oOo000O = '(http.*)'
 import uuid
 iII = str ( uuid . uuid1 ( ) ) . upper ( )
 ooO0o0O0Oo = re . compile ( oOo000O ) . findall ( oOO0o0oo0 )
 IiiIIi = [ ( 'X-Playback-Session-Id' , iII ) ]
 for O00o0O in ooO0o0O0Oo :
  try :
   iIIIiI = IiI11iI1i1i1i ( O00o0O , headers = IiiIIi ) ;
   if 93 - 93: O0OOo . iI11I1II1I1I % Ii . oOoO0oo0OOOo % O0OOo + o0o00Oo0O
  except : pass
  if 65 - 65: o00ooo0 + i11ii11iIi11i - ii
 return page_data + '|&X-Playback-Session-Id=' + iII
 if 51 - 51: i1iIi11iIIi1I + o0OO0 / o00 - ii1I
 if 51 - 51: i1iIi11iIIi1I - Iii1ii1II11i * I1i1iI1i
def ii1111Ii1i ( page_data ) :
 if 48 - 48: o0o00Oo0O * o00ooo0 - o0o00Oo0O / o00ooo0 + oOoO0oo0OOOo
 if page_data . startswith ( 'http://dag.total-stream.net' ) :
  IiiIIi = [ ( 'User-Agent' , 'Verismo-BlackUI_(2.4.7.5.8.0.34)' ) ]
  page_data = IiI11iI1i1i1i ( page_data , headers = IiiIIi ) ;
  if 52 - 52: i11ii11iIi11i % o00ooo0 * ooO0OO000o
 if '127.0.0.1' in page_data :
  return I1IiIii11I ( page_data )
 elif IiI1iiiIii ( page_data , 'wmsAuthSign%3D([^%&]+)' ) != '' :
  i1iii1ii = IiI1iiiIii ( page_data , '&ver_t=([^&]+)&' ) + '?wmsAuthSign=' + IiI1iiiIii ( page_data , 'wmsAuthSign%3D([^%&]+)' ) + '==/mp4:' + IiI1iiiIii ( page_data , '\\?y=([^&]+)&' )
 else :
  i1iii1ii = IiI1iiiIii ( page_data , 'href="([^"]+)"[^"]+$' )
  if len ( i1iii1ii ) == 0 :
   i1iii1ii = page_data
 i1iii1ii = i1iii1ii . replace ( ' ' , '%20' )
 return i1iii1ii
 if 18 - 18: i11ii11iIi11i . ooO0OO000o % oOoO0oo0OOOo % o00ooo0
def IiI1iiiIii ( data , re_patten ) :
 IIIIiI11I11 = ''
 ii1iI = re . search ( re_patten , data )
 if ii1iI != None :
  IIIIiI11I11 = ii1iI . group ( 1 )
 else :
  IIIIiI11I11 = ''
 return IIIIiI11I11
 if 87 - 87: iI11I1II1I1I . ii * oOoO0oo0OOOo
def I1IiIii11I ( page_data ) :
 i1iii1ii = ''
 if '127.0.0.1' in page_data :
  i1iii1ii = IiI1iiiIii ( page_data , '&ver_t=([^&]+)&' ) + ' live=true timeout=15 playpath=' + IiI1iiiIii ( page_data , '\\?y=([a-zA-Z0-9-_\\.@]+)' )
  if 100 - 100: i11ii11iIi11i / ii1I - I11i11Ii % o00ooo0 - iI11I1II1I1I
 if IiI1iiiIii ( page_data , 'token=([^&]+)&' ) != '' :
  i1iii1ii = i1iii1ii + '?token=' + IiI1iiiIii ( page_data , 'token=([^&]+)&' )
 elif IiI1iiiIii ( page_data , 'wmsAuthSign%3D([^%&]+)' ) != '' :
  i1iii1ii = IiI1iiiIii ( page_data , '&ver_t=([^&]+)&' ) + '?wmsAuthSign=' + IiI1iiiIii ( page_data , 'wmsAuthSign%3D([^%&]+)' ) + '==/mp4:' + IiI1iiiIii ( page_data , '\\?y=([^&]+)&' )
 else :
  i1iii1ii = IiI1iiiIii ( page_data , 'HREF="([^"]+)"' )
  if 17 - 17: I1i1iI1i / IiiI % i1iIi11iIIi1I
 if 'dag1.asx' in i1iii1ii :
  return ii1111Ii1i ( i1iii1ii )
  if 71 - 71: Oo0oO0ooo . ooO00oOoo . i11ii11iIi11i
 if 'devinlivefs.fplive.net' not in i1iii1ii :
  i1iii1ii = i1iii1ii . replace ( 'devinlive' , 'flive' )
 if 'permlivefs.fplive.net' not in i1iii1ii :
  i1iii1ii = i1iii1ii . replace ( 'permlive' , 'flive' )
 return i1iii1ii
 if 68 - 68: Ii % o0OO0 * i11ii11iIi11i * Oo0oO0ooo * ooO0OO000o + o0o00Oo0O
 if 66 - 66: I1i1iI1i % Iii1ii1II11i % ii
def II11 ( str_eval ) :
 iIiii = ""
 try :
  O0O0o0oO0O00 = "w,i,s,e=(" + str_eval + ')'
  exec ( O0O0o0oO0O00 )
  iIiii = o0O0oO0 ( w , oooo0O0 , OOo00OO00Oo , e )
 except : traceback . print_exc ( file = sys . stdout )
 if 77 - 77: o0o00Oo0O . o00ooo0
 return iIiii
 if 39 - 39: O0OOo . ooO0OO000o
def o0O0oO0 ( w , i , s , e ) :
 iIiIi1iI11iiI = 0 ;
 iiI1Ii11II1I = 0 ;
 I1Ii11II1I1 = 0 ;
 IiI1iI1IiiIi1 = [ ] ;
 OoO0oo = [ ] ;
 while True :
  if ( iIiIi1iI11iiI < 5 ) :
   OoO0oo . append ( w [ iIiIi1iI11iiI ] )
  elif ( iIiIi1iI11iiI < len ( w ) ) :
   IiI1iI1IiiIi1 . append ( w [ iIiIi1iI11iiI ] ) ;
  iIiIi1iI11iiI += 1 ;
  if ( iiI1Ii11II1I < 5 ) :
   OoO0oo . append ( i [ iiI1Ii11II1I ] )
  elif ( iiI1Ii11II1I < len ( i ) ) :
   IiI1iI1IiiIi1 . append ( i [ iiI1Ii11II1I ] )
  iiI1Ii11II1I += 1 ;
  if ( I1Ii11II1I1 < 5 ) :
   OoO0oo . append ( s [ I1Ii11II1I1 ] )
  elif ( I1Ii11II1I1 < len ( s ) ) :
   IiI1iI1IiiIi1 . append ( s [ I1Ii11II1I1 ] ) ;
  I1Ii11II1I1 += 1 ;
  if ( len ( w ) + len ( i ) + len ( s ) + len ( e ) == len ( IiI1iI1IiiIi1 ) + len ( OoO0oo ) + len ( e ) ) :
   break ;
   if 72 - 72: o0o00Oo0O + I11i11Ii - o00 - i11ii11iIi11i
 o0i1I11iI1iiI = '' . join ( IiI1iI1IiiIi1 )
 I1 = '' . join ( OoO0oo )
 iiI1Ii11II1I = 0 ;
 iioO0o = [ ] ;
 for iIiIi1iI11iiI in range ( 0 , len ( IiI1iI1IiiIi1 ) , 2 ) :
  if 50 - 50: o00 / o00 + Oo0ooO0oo0oO * O0OOo / Iii1ii1II11i
  I1IIiiI1II1 = - 1 ;
  if ( ord ( I1 [ iiI1Ii11II1I ] ) % 2 ) :
   I1IIiiI1II1 = 1 ;
   if 5 - 5: o00
  iioO0o . append ( chr ( int ( o0i1I11iI1iiI [ iIiIi1iI11iiI : iIiIi1iI11iiI + 2 ] , 36 ) - I1IIiiI1II1 ) ) ;
  iiI1Ii11II1I += 1 ;
  if ( iiI1Ii11II1I >= len ( OoO0oo ) ) :
   iiI1Ii11II1I = 0 ;
 I1ii1Ii1ii11i = '' . join ( iioO0o )
 if 'eval(function(w,i,s,e)' in I1ii1Ii1ii11i :
  if 62 - 62: oOoO0oo0OOOo . ii . Oo0ooO0oo0oO . i11ii11iIi11i * o00
  I1ii1Ii1ii11i = re . compile ( 'eval\(function\(w,i,s,e\).*}\((.*?)\)' ) . findall ( I1ii1Ii1ii11i ) [ 0 ]
  return II11 ( I1ii1Ii1ii11i )
 else :
  if 78 - 78: o0OO0 / i11ii11iIi11i - o0OO0 * ii . oOoO0oo0OOOo
  return I1ii1Ii1ii11i
  if 96 - 96: I11i11Ii % ii1I . IiiI . o0o00Oo0O
def OoOOoO0oOo ( page_value , regex_for_text = '' , iterations = 1 , total_iteration = 1 ) :
 try :
  Ii1Iii11 = None
  if page_value . startswith ( "http" ) :
   page_value = IiI11iI1i1i1i ( page_value )
   if 97 - 97: Oo0ooO0oo0oO / o0OO0 . ooO0OO000o
  if regex_for_text and len ( regex_for_text ) > 0 :
   try :
    page_value = re . compile ( regex_for_text ) . findall ( page_value ) [ 0 ]
   except : return 'NOTPACKED'
   if 44 - 44: o00ooo0 % I1i1iI1i . ooO00oOoo
  page_value = Ii11Iii ( page_value , iterations , total_iteration )
 except :
  page_value = 'UNPACKEDFAILED'
  traceback . print_exc ( file = sys . stdout )
  if 68 - 68: I11i11Ii % o0o00Oo0O
 if 'sav1live.tv' in page_value :
  page_value = page_value . replace ( 'sav1live.tv' , 'sawlive.tv' )
  if 74 - 74: ii1I + oOoO0oo0OOOo + iI11I1II1I1I * oOoO0oo0OOOo * iI11I1II1I1I + I1i1iI1i
 return page_value
 if 64 - 64: iI11I1II1I1I / o0o00Oo0O % Oo0oO0ooo . ii + Oo0oO0ooo + o0OO0
def Ii11Iii ( sJavascript , iteration = 1 , totaliterations = 2 ) :
 if 79 - 79: ii - Oo0oO0ooo * Oo0oO0ooo . oOoO0oo0OOOo
 if sJavascript . startswith ( 'var _0xcb8a=' ) :
  Oo00ooO0OoOo = sJavascript . split ( 'var _0xcb8a=' )
  O0O0o0oO0O00 = "myarray=" + Oo00ooO0OoOo [ 1 ] . split ( "eval(" ) [ 0 ]
  exec ( O0O0o0oO0O00 )
  o0oOO00 = 62
  ii11iiIi = int ( Oo00ooO0OoOo [ 1 ] . split ( ",62," ) [ 1 ] . split ( ',' ) [ 0 ] )
  i11iI11I1I = myarray [ 0 ]
  Ii1iiIi1I11i = myarray [ 3 ]
  with open ( 'temp file' + str ( iteration ) + '.js' , "wb" ) as O0 :
   O0 . write ( str ( Ii1iiIi1I11i ) )
   if 68 - 68: i1iIi11iIIi1I . i1iIi11iIIi1I - Iii1ii1II11i / I1i1iI1i . O0OOo / ii1I
 else :
  if 12 - 12: Iii1ii1II11i * ii1I * I1i1iI1i
  if "rn p}('" in sJavascript :
   Oo00ooO0OoOo = sJavascript . split ( "rn p}('" )
  else :
   Oo00ooO0OoOo = sJavascript . split ( "rn A}('" )
   if 23 - 23: Oo0ooO0oo0oO / o0o00Oo0O / I11i11Ii
   if 49 - 49: I1i1iI1i . IiiI % o0OO0 / o00ooo0
  i11iI11I1I , o0oOO00 , ii11iiIi , Ii1iiIi1I11i = ( '' , '0' , '0' , '' )
  if 95 - 95: o0o00Oo0O * oOoO0oo0OOOo * Oo0oO0ooo . O0OOo / iI11I1II1I1I
  O0O0o0oO0O00 = "p1,a1,c1,k1=('" + Oo00ooO0OoOo [ 1 ] . split ( ".spli" ) [ 0 ] + ')'
  exec ( O0O0o0oO0O00 )
 Ii1iiIi1I11i = Ii1iiIi1I11i . split ( '|' )
 Oo00ooO0OoOo = Oo00ooO0OoOo [ 1 ] . split ( "))'" )
 if 28 - 28: Oo0oO0ooo + o0OO0 - O0OOo / iI11I1II1I1I - I11i11Ii
 if 45 - 45: o0o00Oo0O / ii1I * o0OO0 * i11ii11iIi11i
 if 35 - 35: Iii1ii1II11i / o00 % I11i11Ii + iI11I1II1I1I
 if 79 - 79: oOoO0oo0OOOo / O0OOo
 if 77 - 77: i1iIi11iIIi1I
 if 46 - 46: ooO00oOoo
 if 72 - 72: o00 * Oo0ooO0oo0oO
 if 67 - 67: ii1I
 if 5 - 5: ooO0OO000o . ii
 if 57 - 57: I11i11Ii
 if 35 - 35: ii - ooO00oOoo / i11ii11iIi11i
 if 50 - 50: oOoO0oo0OOOo
 if 33 - 33: I1i1iI1i
 if 98 - 98: oOoO0oo0OOOo % ooO0OO000o
 if 95 - 95: iI11I1II1I1I - ooO00oOoo - Oo0ooO0oo0oO + ooO00oOoo % Iii1ii1II11i . I11i11Ii
 if 41 - 41: o0o00Oo0O + o0OO0 . ii1I - ooO0OO000o * IiiI . i11ii11iIi11i
 if 68 - 68: IiiI
 if 20 - 20: ooO00oOoo - ooO00oOoo
 if 37 - 37: Oo0oO0ooo
 if 37 - 37: i1iIi11iIIi1I / Oo0oO0ooo * o0o00Oo0O
 if 73 - 73: o00 * o00 / O0OOo
 if 43 - 43: Iii1ii1II11i . ii1I . Oo0oO0ooo + o0o00Oo0O * o00ooo0 * o0o00Oo0O
 iI1 = ''
 III1I11i1iIi = ''
 if 41 - 41: Iii1ii1II11i + o00ooo0 % ii . Iii1ii1II11i + o00 . o00
 if 31 - 31: Ii + ooO0OO000o . o00 * oOoO0oo0OOOo
 OO0ooo0 = str ( II1II1iI ( i11iI11I1I , o0oOO00 , ii11iiIi , Ii1iiIi1I11i , iI1 , III1I11i1iIi , iteration ) )
 if 58 - 58: o0o00Oo0O . Oo0oO0ooo / ii . i11ii11iIi11i / i1iIi11iIIi1I * ooO0OO000o
 if 53 - 53: o00ooo0 - o0o00Oo0O / IiiI % o00 * I11i11Ii % Oo0ooO0oo0oO
 if 69 - 69: Iii1ii1II11i
 if 83 - 83: IiiI
 if 38 - 38: ooO00oOoo + ii . ii1I
 if iteration >= totaliterations :
  if 19 - 19: o00 - IiiI - o00ooo0 - oOoO0oo0OOOo . o00 . ooO00oOoo
  return OO0ooo0
 else :
  if 48 - 48: o00 + Oo0oO0ooo
  return Ii11Iii ( OO0ooo0 , iteration + 1 )
  if 60 - 60: I1i1iI1i + o00 . Oo0oO0ooo / ii1I . iI11I1II1I1I
def II1II1iI ( p , a , c , k , e , d , iteration , v = 1 ) :
 if 14 - 14: Oo0ooO0oo0oO
 if 79 - 79: o00ooo0
 if 76 - 76: iI11I1II1I1I
 while ( c >= 1 ) :
  c = c - 1
  if ( k [ c ] ) :
   Oo = str ( i111i1iIi1 ( c , a ) )
   if v == 1 :
    p = re . sub ( '\\b' + Oo + '\\b' , k [ c ] , p )
   else :
    p = OoO0oO ( p , Oo , k [ c ] )
    if 10 - 10: ii1I . ooO0OO000o / IiiI * O0OOo
    if 10 - 10: I1i1iI1i - i1iIi11iIIi1I
    if 59 - 59: ii * i1iIi11iIIi1I + ii1I
    if 23 - 23: O0OOo
    if 13 - 13: iI11I1II1I1I
    if 77 - 77: Ii - iI11I1II1I1I / o0OO0 / O0OOo / i11ii11iIi11i
 return p
 if 56 - 56: ii * o0o00Oo0O
 if 85 - 85: ii % oOoO0oo0OOOo * iI11I1II1I1I
 if 44 - 44: iI11I1II1I1I . Iii1ii1II11i + ooO00oOoo . O0OOo
def OoO0oO ( source_str , word_to_find , replace_with ) :
 II1i11 = None
 II1i11 = source_str . split ( word_to_find )
 if len ( II1i11 ) > 1 :
  Ii1IIIII = [ ]
  iiiIIiiii11 = 0
  for IIi in II1i11 :
   if 8 - 8: o00ooo0 % Oo0ooO0oo0oO / ooO0OO000o + Oo0oO0ooo + IiiI
   Ii1IIIII . append ( IIi )
   oO0oO00oOo0OOO = word_to_find
   if 96 - 96: i11ii11iIi11i
   if 92 - 92: i1iIi11iIIi1I / Ii + Iii1ii1II11i
   if iiiIIiiii11 == len ( II1i11 ) - 1 :
    oO0oO00oOo0OOO = ''
   else :
    if len ( IIi ) == 0 :
     if ( len ( II1i11 [ iiiIIiiii11 + 1 ] ) == 0 and word_to_find [ 0 ] . lower ( ) not in 'abcdefghijklmnopqrstuvwxyz1234567890_' ) or ( len ( II1i11 [ iiiIIiiii11 + 1 ] ) > 0 and II1i11 [ iiiIIiiii11 + 1 ] [ 0 ] . lower ( ) not in 'abcdefghijklmnopqrstuvwxyz1234567890_' ) :
      oO0oO00oOo0OOO = replace_with
      if 87 - 87: oOoO0oo0OOOo % iI11I1II1I1I
    else :
     if ( II1i11 [ iiiIIiiii11 ] [ - 1 ] . lower ( ) not in 'abcdefghijklmnopqrstuvwxyz1234567890_' ) and ( ( len ( II1i11 [ iiiIIiiii11 + 1 ] ) == 0 and word_to_find [ 0 ] . lower ( ) not in 'abcdefghijklmnopqrstuvwxyz1234567890_' ) or ( len ( II1i11 [ iiiIIiiii11 + 1 ] ) > 0 and II1i11 [ iiiIIiiii11 + 1 ] [ 0 ] . lower ( ) not in 'abcdefghijklmnopqrstuvwxyz1234567890_' ) ) :
      oO0oO00oOo0OOO = replace_with
      if 72 - 72: Oo0ooO0oo0oO . Oo0ooO0oo0oO - Iii1ii1II11i
   Ii1IIIII . append ( oO0oO00oOo0OOO )
   iiiIIiiii11 += 1
   if 48 - 48: i1iIi11iIIi1I - O0OOo + i1iIi11iIIi1I - I11i11Ii * Ii . o00
  source_str = '' . join ( Ii1IIIII )
 return source_str
 if 35 - 35: Oo0oO0ooo . o0o00Oo0O + i1iIi11iIIi1I + Oo0ooO0oo0oO + ii1I
def OooOooO0O0o0 ( num , radix ) :
 if 59 - 59: i1iIi11iIIi1I + o00 - Oo0ooO0oo0oO . IiiI + I11i11Ii % o0OO0
 o000oOoo0o000 = ""
 if num == 0 : return '0'
 while num > 0 :
  o000oOoo0o000 = "0123456789abcdefghijklmnopqrstuvwxyz" [ num % radix ] + o000oOoo0o000
  num /= radix
 return o000oOoo0o000
 if 37 - 37: o00 + o00 % IiiI
def i111i1iIi1 ( cc , a ) :
 Oo = "" if cc < a else i111i1iIi1 ( int ( cc / a ) , a )
 cc = ( cc % a )
 iIi1i1iIi1Ii1 = chr ( cc + 29 ) if cc > 35 else str ( OooOooO0O0o0 ( cc , 36 ) )
 return Oo + iIi1i1iIi1Ii1
 if 66 - 66: i11ii11iIi11i % IiiI
 if 21 - 21: oOoO0oo0OOOo - ii % Ii
def II1i1III ( cookieJar ) :
 try :
  Oo00O0OO = ""
  for IiII111iI1ii1 , oOOOoo0o in enumerate ( cookieJar ) :
   Oo00O0OO += oOOOoo0o . name + "=" + oOOOoo0o . value + ";"
 except : pass
 if 44 - 44: o0o00Oo0O % ii1I
 return Oo00O0OO
 if 42 - 42: ooO0OO000o - i11ii11iIi11i - ii . o00 / oOoO0oo0OOOo
 if 56 - 56: Ii - iI11I1II1I1I . ooO0OO000o
def oO0oOOoo00000 ( cookieJar , COOKIEFILE ) :
 try :
  OO00 = os . path . join ( ooOOOo0oo0O0 , COOKIEFILE )
  cookieJar . save ( OO00 , ignore_discard = True )
 except : pass
 if 81 - 81: Oo0oO0ooo / oOoO0oo0OOOo * Oo0oO0ooo . o0o00Oo0O
def Ii1ii111i1 ( COOKIEFILE ) :
 if 61 - 61: i11ii11iIi11i * Oo0ooO0oo0oO + ooO00oOoo . iI11I1II1I1I % I1i1iI1i . ooO00oOoo
 O0o0oo0oOO0oO = None
 if COOKIEFILE :
  try :
   OO00 = os . path . join ( ooOOOo0oo0O0 , COOKIEFILE )
   O0o0oo0oOO0oO = cookielib . LWPCookieJar ( )
   O0o0oo0oOO0oO . load ( OO00 , ignore_discard = True )
  except :
   O0o0oo0oOO0oO = None
   if 15 - 15: i11ii11iIi11i * ooO0OO000o
 if not O0o0oo0oOO0oO :
  O0o0oo0oOO0oO = cookielib . LWPCookieJar ( )
  if 59 - 59: ooO00oOoo + i11ii11iIi11i / Oo0ooO0oo0oO
 return O0o0oo0oOO0oO
 if 97 - 97: i1iIi11iIIi1I * o00 % O0OOo . o00 - ooO00oOoo - Oo0ooO0oo0oO
def o0oOOoooOOOOo ( fun_call , page_data , Cookie_Jar , m ) :
 oo0O0o00 = ''
 if 39 - 39: O0OOo + o0o00Oo0O / ii1I % Oo0oO0ooo / o0OO0 * Oo0oO0ooo
 if OOOO not in sys . path :
  sys . path . append ( OOOO )
  if 77 - 77: Oo0oO0ooo . ooO00oOoo % oOoO0oo0OOOo
  if 42 - 42: Oo0oO0ooo % o00 % IiiI % o0OO0 + I1i1iI1i % oOoO0oo0OOOo
 try :
  iI1iIIiii = 'import ' + fun_call . split ( '.' ) [ 0 ]
  if 52 - 52: o00ooo0 % Oo0ooO0oo0oO * I11i11Ii % I1i1iI1i + Oo0ooO0oo0oO / o00
  exec ( iI1iIIiii )
  if 80 - 80: ii + Oo0oO0ooo
 except :
  if 95 - 95: ooO00oOoo / o0OO0 * ooO00oOoo - ii * ii % i11ii11iIi11i
  traceback . print_exc ( file = sys . stdout )
  if 43 - 43: i1iIi11iIIi1I . ooO00oOoo
 exec ( 'ret_val=' + fun_call )
 if 12 - 12: ooO00oOoo + Oo0ooO0oo0oO + I1i1iI1i . Oo0oO0ooo / o00ooo0
 if 29 - 29: Oo0oO0ooo . O0OOo - ooO0OO000o
 try :
  return str ( oo0O0o00 )
 except : return oo0O0o00
 if 68 - 68: iI11I1II1I1I + ooO0OO000o / o0OO0
def iIi ( fun_call , page_data , Cookie_Jar , m ) :
 if 91 - 91: oOoO0oo0OOOo % iI11I1II1I1I . I11i11Ii
 oo0O0o00 = ''
 if OOOO not in sys . path :
  sys . path . append ( OOOO )
  if 70 - 70: I1i1iI1i % ooO0OO000o % o0o00Oo0O . ii1I / ooO00oOoo
 oOO0OO0O = open ( os . path . join ( OOOO , 'LSProdynamicCode.py' ) , "wb" )
 oOO0OO0O . write ( "# -*- coding: utf-8 -*-\n" )
 oOO0OO0O . write ( fun_call . encode ( "utf-8" ) ) ;
 if 100 - 100: Iii1ii1II11i * Ii % o0OO0 / i1iIi11iIIi1I / O0OOo + Iii1ii1II11i
 oOO0OO0O . close ( )
 import LSProdynamicCode
 oo0O0o00 = LSProdynamicCode . GetLSProData ( page_data , Cookie_Jar , m )
 try :
  return str ( oo0O0o00 )
 except : return oo0O0o00
 if 59 - 59: ooO00oOoo - Oo0oO0ooo
 if 14 - 14: iI11I1II1I1I - iI11I1II1I1I
def i111i1I1ii1i ( captchakey , cj , type = 1 ) :
 if 100 - 100: Oo0oO0ooo . o00ooo0 - iI11I1II1I1I . Ii / ooO0OO000o
 if 71 - 71: ooO00oOoo * i1iIi11iIIi1I . I1i1iI1i
 if 49 - 49: Oo0oO0ooo * o0o00Oo0O . Oo0oO0ooo
 ii1II1II = ""
 i11i11II11i = ""
 if 9 - 9: oOoO0oo0OOOo - Iii1ii1II11i * O0OOo . O0OOo - I11i11Ii
 if 74 - 74: Iii1ii1II11i * Ii / I11i11Ii - o0o00Oo0O . O0OOo
 if 39 - 39: O0OOo / o0o00Oo0O * Oo0oO0ooo
 if 17 - 17: o00ooo0 / iI11I1II1I1I - i11ii11iIi11i + I11i11Ii % Oo0ooO0oo0oO
 if 14 - 14: IiiI % Oo0oO0ooo + Iii1ii1II11i + i11ii11iIi11i
 OOOoOOo0o = False
 IiI1Iii1 = None
 i11i11II11i = None
 if len ( captchakey ) > 0 :
  Ooooo = captchakey
  if not Ooooo . startswith ( 'http' ) :
   Ooooo = 'http://www.google.com/recaptcha/api/challenge?k=' + Ooooo + '&ajax=1'
   if 43 - 43: Oo0ooO0oo0oO
  OOOoOOo0o = True
  if 57 - 57: o0o00Oo0O / IiiI
  IiIi = 'challenge.*?\'(.*?)\''
  oO0Oo00oo = '\'(.*?)\''
  OoOoooO000OO = IiI11iI1i1i1i ( Ooooo , cookieJar = cj )
  ii1II1II = re . findall ( IiIi , OoOoooO000OO ) [ 0 ]
  O00Ooo = 'http://www.google.com/recaptcha/api/reload?c=' ;
  i1oOOO0ooOO = Ooooo . split ( 'k=' ) [ 1 ]
  O00Ooo += ii1II1II + '&k=' + i1oOOO0ooOO + '&reason=i&type=image&lang=en'
  i11 = IiI11iI1i1i1i ( O00Ooo , cookieJar = cj )
  IiI1Iii1 = re . findall ( oO0Oo00oo , i11 ) [ 0 ]
  IiI1iiI11 = 'http://www.google.com/recaptcha/api/image?c=' + IiI1Iii1
  if not IiI1iiI11 . startswith ( "http" ) :
   IiI1iiI11 = 'http://www.google.com/recaptcha/api/' + IiI1iiI11
  import random
  O00ooo0O0 = random . randrange ( 100 , 1000 , 5 )
  OOoOOOO00 = os . path . join ( ooOOOo0oo0O0 , str ( O00ooo0O0 ) + "captcha.img" )
  IIii1III = open ( OOoOOOO00 , "wb" )
  IIii1III . write ( IiI11iI1i1i1i ( IiI1iiI11 , cookieJar = cj ) )
  IIii1III . close ( )
  ooooOoo0OO = Oo0 ( captcha = OOoOOOO00 )
  i11i11II11i = ooooOoo0OO . get ( )
  os . remove ( OOoOOOO00 )
  if 96 - 96: I1i1iI1i % o00ooo0 % o0OO0 * I1i1iI1i / Oo0ooO0oo0oO
 if IiI1Iii1 :
  if type == 1 :
   return 'recaptcha_challenge_field=' + urllib . quote_plus ( IiI1Iii1 ) + '&recaptcha_response_field=' + urllib . quote_plus ( i11i11II11i )
  elif type == 2 :
   return 'recaptcha_challenge_field:' + IiI1Iii1 + ',recaptcha_response_field:' + i11i11II11i
  else :
   return 'recaptcha_challenge_field=' + urllib . quote_plus ( IiI1Iii1 ) + '&recaptcha_response_field=' + urllib . quote_plus ( i11i11II11i )
 else :
  return ''
  if 13 - 13: iI11I1II1I1I - i11ii11iIi11i
  if 100 - 100: Ii / Ii
def IiI11iI1i1i1i ( url , cookieJar = None , post = None , timeout = 20 , headers = None , noredir = False ) :
 if 89 - 89: o00 . Ii * o0o00Oo0O
 if 44 - 44: ii1I . I11i11Ii / Ii + Oo0oO0ooo
 O00Oo = urllib2 . HTTPCookieProcessor ( cookieJar )
 if 27 - 27: Oo0ooO0oo0oO
 if noredir :
  i1I1IiI = urllib2 . build_opener ( oOo , O00Oo , urllib2 . HTTPBasicAuthHandler ( ) , urllib2 . HTTPHandler ( ) )
 else :
  i1I1IiI = urllib2 . build_opener ( O00Oo , urllib2 . HTTPBasicAuthHandler ( ) , urllib2 . HTTPHandler ( ) )
  if 52 - 52: ooO00oOoo % oOoO0oo0OOOo + iI11I1II1I1I * o0OO0 . o00ooo0
 ii1ii1ii = urllib2 . Request ( url )
 ii1ii1ii . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36' )
 if headers :
  for ii111111I1iII , OoOooOO0oOOo0O in headers :
   ii1ii1ii . add_header ( ii111111I1iII , OoOooOO0oOOo0O )
   if 42 - 42: o00 / IiiI + i1iIi11iIIi1I . i1iIi11iIIi1I % Oo0ooO0oo0oO
 oooooOoo0ooo = i1I1IiI . open ( ii1ii1ii , post , timeout = timeout )
 OOoOoo0 = oooooOoo0ooo . read ( )
 oooooOoo0ooo . close ( )
 return OOoOoo0 ;
 if 16 - 16: ii1I + i11ii11iIi11i % oOoO0oo0OOOo + o00ooo0 * i1iIi11iIIi1I
def i1o0oo0 ( str , reg = None ) :
 if reg :
  str = re . findall ( reg , str ) [ 0 ]
 OoO0OOoO0Oo0 = urllib . unquote ( str [ 0 : len ( str ) - 1 ] ) ;
 oO00O = '' ;
 for oooo0O0 in range ( len ( OoO0OOoO0Oo0 ) ) :
  oO00O += chr ( ord ( OoO0OOoO0Oo0 [ oooo0O0 ] ) - OoO0OOoO0Oo0 [ len ( OoO0OOoO0Oo0 ) - 1 ] ) ;
 oO00O = urllib . unquote ( oO00O )
 if 21 - 21: Oo0ooO0oo0oO % Oo0oO0ooo % i11ii11iIi11i % ii
 return oO00O
 if 31 - 31: I11i11Ii
def iIIIi1i1I11i ( str ) :
 O0oI1ii1Ii1 = re . findall ( 'unescape\(\'(.*?)\'' , str )
 if 73 - 73: o0o00Oo0O . o0OO0 + Ii + iI11I1II1I1I - I1i1iI1i / oOoO0oo0OOOo
 if ( not O0oI1ii1Ii1 == None ) and len ( O0oI1ii1Ii1 ) > 0 :
  for OO0OOOOo0000O in O0oI1ii1Ii1 :
   if 25 - 25: o00 - i1iIi11iIIi1I
   str = str . replace ( OO0OOOOo0000O , urllib . unquote ( OO0OOOOo0000O ) )
 return str
 if 10 - 10: o0o00Oo0O % Oo0oO0ooo . i11ii11iIi11i + IiiI + Iii1ii1II11i
oOOO0 = 0
def oOoOoO000OO ( m , html_page , cookieJar ) :
 global oOOO0
 oOOO0 += 1
 Iii1i11iiI1 = m [ 'expres' ]
 i111i1i = m [ 'page' ]
 oOOoOooO0oO0o = re . compile ( '\$LiveStreamCaptcha\[([^\]]*)\]' ) . findall ( Iii1i11iiI1 ) [ 0 ]
 if 59 - 59: Oo0oO0ooo
 Ooooo = re . compile ( oOOoOooO0oO0o ) . findall ( html_page ) [ 0 ]
 if 89 - 89: oOoO0oo0OOOo % iI11I1II1I1I
 if not Ooooo . startswith ( "http" ) :
  III11I1 = 'http://' + "" . join ( i111i1i . split ( '/' ) [ 2 : 3 ] )
  if Ooooo . startswith ( "/" ) :
   Ooooo = III11I1 + Ooooo
  else :
   Ooooo = III11I1 + '/' + Ooooo
   if 61 - 61: oOoO0oo0OOOo - i11ii11iIi11i + I11i11Ii * Oo0ooO0oo0oO % i11ii11iIi11i
 OOoOOOO00 = os . path . join ( ooOOOo0oo0O0 , str ( oOOO0 ) + "captcha.jpg" )
 IIii1III = open ( OOoOOOO00 , "wb" )
 if 24 - 24: O0OOo - I1i1iI1i * o0OO0
 ii1ii1ii = urllib2 . Request ( Ooooo )
 ii1ii1ii . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20100101 Firefox/14.0.1' )
 if 'referer' in m :
  ii1ii1ii . add_header ( 'Referer' , m [ 'referer' ] )
 if 'agent' in m :
  ii1ii1ii . add_header ( 'User-agent' , m [ 'agent' ] )
 if 'setcookie' in m :
  if 87 - 87: o00ooo0 - Iii1ii1II11i % Iii1ii1II11i . o0OO0 / Iii1ii1II11i
  ii1ii1ii . add_header ( 'Cookie' , m [ 'setcookie' ] )
  if 6 - 6: oOoO0oo0OOOo / iI11I1II1I1I * ii * Ii
  if 79 - 79: Oo0oO0ooo % i11ii11iIi11i
  if 81 - 81: Ii + Ii * i11ii11iIi11i + Oo0oO0ooo
  if 32 - 32: o0o00Oo0O . ii
 urllib2 . urlopen ( ii1ii1ii )
 oooooOoo0ooo = urllib2 . urlopen ( ii1ii1ii )
 if 15 - 15: I11i11Ii . i11ii11iIi11i
 IIii1III . write ( oooooOoo0ooo . read ( ) )
 oooooOoo0ooo . close ( )
 IIii1III . close ( )
 ooooOoo0OO = Oo0 ( captcha = OOoOOOO00 )
 i11i11II11i = ooooOoo0OO . get ( )
 return i11i11II11i
 if 17 - 17: Ii / i1iIi11iIIi1I . i11ii11iIi11i / I11i11Ii
def Ii1oOooOOOOo0o ( imageregex , html_page , cookieJar , m ) :
 global oOOO0
 oOOO0 += 1
 if 97 - 97: Iii1ii1II11i / I11i11Ii % o0o00Oo0O + ii1I - O0OOo
 if 38 - 38: IiiI % ooO00oOoo + Ii + o00 + O0OOo / Ii
 if not imageregex == '' :
  if html_page . startswith ( "http" ) :
   III11I1 = IiI11iI1i1i1i ( html_page , cookieJar = cookieJar )
  else :
   III11I1 = html_page
  Ooooo = re . compile ( imageregex ) . findall ( html_page ) [ 0 ]
 else :
  Ooooo = html_page
  if 'oneplay.tv/embed' in html_page :
   import oneplay
   III11I1 = IiI11iI1i1i1i ( html_page , cookieJar = cookieJar )
   Ooooo = oneplay . getCaptchaUrl ( III11I1 )
   if 94 - 94: o00 - i1iIi11iIIi1I + o0OO0
 OOoOOOO00 = os . path . join ( ooOOOo0oo0O0 , str ( oOOO0 ) + "captcha.jpg" )
 IIii1III = open ( OOoOOOO00 , "wb" )
 if 59 - 59: I1i1iI1i . I11i11Ii - iI11I1II1I1I + iI11I1II1I1I
 ii1ii1ii = urllib2 . Request ( Ooooo )
 ii1ii1ii . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20100101 Firefox/14.0.1' )
 if 'referer' in m :
  ii1ii1ii . add_header ( 'Referer' , m [ 'referer' ] )
 if 'agent' in m :
  ii1ii1ii . add_header ( 'User-agent' , m [ 'agent' ] )
 if 'accept' in m :
  ii1ii1ii . add_header ( 'Accept' , m [ 'accept' ] )
 if 'setcookie' in m :
  if 56 - 56: o0OO0 + O0OOo
  ii1ii1ii . add_header ( 'Cookie' , m [ 'setcookie' ] )
  if 32 - 32: ooO0OO000o + oOoO0oo0OOOo % O0OOo / oOoO0oo0OOOo + Iii1ii1II11i
  if 2 - 2: Ii - ooO00oOoo + i11ii11iIi11i % I1i1iI1i * o00ooo0
  if 54 - 54: o0o00Oo0O - o00 . Oo0ooO0oo0oO % o00 + o00
  if 36 - 36: Oo0ooO0oo0oO % Ii
  if 47 - 47: ii1I + ooO0OO000o . i1iIi11iIIi1I * o0OO0 . I1i1iI1i / ii1I
 oooooOoo0ooo = urllib2 . urlopen ( ii1ii1ii )
 if 50 - 50: ooO00oOoo / ii1I % ii
 IIii1III . write ( oooooOoo0ooo . read ( ) )
 oooooOoo0ooo . close ( )
 IIii1III . close ( )
 ooooOoo0OO = Oo0 ( captcha = OOoOOOO00 )
 i11i11II11i = ooooOoo0OO . get ( )
 return i11i11II11i
 if 83 - 83: Iii1ii1II11i * Iii1ii1II11i + Oo0ooO0oo0oO
 if 57 - 57: o0o00Oo0O - o0o00Oo0O . Iii1ii1II11i / IiiI / o00ooo0
 if 20 - 20: Oo0ooO0oo0oO * ooO0OO000o - oOoO0oo0OOOo - o0OO0 * ooO00oOoo
 if 6 - 6: O0OOo + Oo0ooO0oo0oO / i1iIi11iIIi1I + Oo0oO0ooo % ooO0OO000o / i11ii11iIi11i
 if 45 - 45: ii
 if 9 - 9: I1i1iI1i . i11ii11iIi11i * ii1I . ii
 if 32 - 32: oOoO0oo0OOOo . Iii1ii1II11i % I11i11Ii - ooO0OO000o
 if 11 - 11: o0o00Oo0O + I11i11Ii
 if 80 - 80: o0OO0 % o0OO0 % o0o00Oo0O - Ii . o00 / o0o00Oo0O
 if 13 - 13: I11i11Ii + o0o00Oo0O - Iii1ii1II11i % i1iIi11iIIi1I / o00ooo0 . ii1I
 if 60 - 60: i1iIi11iIIi1I . Oo0oO0ooo % I11i11Ii - ooO00oOoo
 if 79 - 79: ii / Iii1ii1II11i . o0o00Oo0O
 if 79 - 79: o0OO0 - ooO0OO000o
def Ii1iiI1 ( name , headname ) :
 if 76 - 76: o00ooo0 * iI11I1II1I1I
 if 31 - 31: Ii + Oo0ooO0oo0oO - o0o00Oo0O
 OOoo00O000Oo = xbmc . Keyboard ( 'default' , 'heading' , True )
 OOoo00O000Oo . setDefault ( name )
 OOoo00O000Oo . setHeading ( headname )
 OOoo00O000Oo . setHiddenInput ( False )
 return OOoo00O000Oo . getText ( )
 if 58 - 58: i11ii11iIi11i - oOoO0oo0OOOo . Ii % Ii / ii1I / o0OO0
 if 24 - 24: I11i11Ii * ii1I % O0OOo / o0o00Oo0O + Ii
 if 12 - 12: Iii1ii1II11i / o00ooo0
 if 5 - 5: ii
class Oo0 ( xbmcgui . WindowDialog ) :
 def __init__ ( self , * args , ** kwargs ) :
  self . cptloc = kwargs . get ( 'captcha' )
  self . img = xbmcgui . ControlImage ( 335 , 30 , 624 , 60 , self . cptloc )
  self . addControl ( self . img )
  self . kbd = xbmc . Keyboard ( )
  if 18 - 18: I11i11Ii % ii - o00 . Ii * i1iIi11iIIi1I % o00ooo0
 def get ( self ) :
  self . show ( )
  time . sleep ( 2 )
  self . kbd . doModal ( )
  if ( self . kbd . isConfirmed ( ) ) :
   Ii1I1 = self . kbd . getText ( )
   self . close ( )
   return Ii1I1
  self . close ( )
  return False
  if 98 - 98: Oo0oO0ooo * iI11I1II1I1I . o00ooo0 * i1iIi11iIIi1I / Iii1ii1II11i + O0OOo
def Ii1iI111 ( ) :
 import time
 return str ( int ( time . time ( ) * 1000 ) )
 if 25 - 25: o0OO0
def ii1iii1I1I ( ) :
 import time
 return str ( int ( time . time ( ) ) )
 if 19 - 19: I11i11Ii % o00ooo0 . Oo0oO0ooo * O0OOo
def oOo0OOOOoO ( ) :
 OoO0Ooo = [ ]
 Ii1I1I = sys . argv [ 2 ]
 if len ( Ii1I1I ) >= 2 :
  oOO = sys . argv [ 2 ]
  oOOO0oOoo = oOO . replace ( '?' , '' )
  if ( oOO [ len ( oOO ) - 1 ] == '/' ) :
   oOO = oOO [ 0 : len ( oOO ) - 2 ]
  o0O0ooooooo00 = oOOO0oOoo . split ( '&' )
  OoO0Ooo = { }
  for oooo0O0 in range ( len ( o0O0ooooooo00 ) ) :
   I1111ii11IIII = { }
   I1111ii11IIII = o0O0ooooooo00 [ oooo0O0 ] . split ( '=' )
   if ( len ( I1111ii11IIII ) ) == 2 :
    OoO0Ooo [ I1111ii11IIII [ 0 ] ] = I1111ii11IIII [ 1 ]
 return OoO0Ooo
 if 48 - 48: iI11I1II1I1I % ii1I + oOoO0oo0OOOo % IiiI
 if 79 - 79: oOoO0oo0OOOo % I11i11Ii % o00ooo0 / ii1I % i11ii11iIi11i
def oo0o00OO ( ) :
 iI1i11 = json . loads ( open ( I11II1i ) . read ( ) )
 oo00o0 = len ( iI1i11 )
 for oooo0O0 in iI1i11 :
  OO0Oooo0oOO0O = oooo0O0 [ 0 ]
  IiII = oooo0O0 [ 1 ]
  oOoo00o0oOO = oooo0O0 [ 2 ]
  try :
   o0Oo0oO0oOO00 = oooo0O0 [ 3 ]
   if o0Oo0oO0oOO00 == None :
    raise
  except :
   if o0OOOOO00o0O0 . getSetting ( 'use_thumb' ) == "true" :
    o0Oo0oO0oOO00 = oOoo00o0oOO
   else :
    o0Oo0oO0oOO00 = o0o
  try : oOOO00o000o = oooo0O0 [ 5 ]
  except : oOOO00o000o = None
  try : i1II1i = oooo0O0 [ 6 ]
  except : i1II1i = None
  if 61 - 61: ii1I * IiiI + iI11I1II1I1I / oOoO0oo0OOOo - o0o00Oo0O * iI11I1II1I1I
  if oooo0O0 [ 4 ] == 0 :
   O0O0o0oOOO ( IiII , OO0Oooo0oOO0O , oOoo00o0oOO , o0Oo0oO0oOO00 , '' , '' , '' , 'fav' , oOOO00o000o , i1II1i , oo00o0 )
  else :
   iIi1IIIi1 ( OO0Oooo0oOO0O , IiII , oooo0O0 [ 4 ] , oOoo00o0oOO , o0o , '' , '' , '' , '' , 'fav' )
   if 56 - 56: Oo0ooO0oo0oO
   if 49 - 49: O0OOo . ooO0OO000o
def IioOooOOo00ooO ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 o0OO0oooo = [ ]
 try :
  if 40 - 40: ooO00oOoo - oOoO0oo0OOOo * I1i1iI1i - Oo0oO0ooo / oOoO0oo0OOOo
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( I11II1i ) == False :
  oO0ooO0OoOOOO ( 'Making Favorites File' )
  o0OO0oooo . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  IIii1 = open ( I11II1i , "w" )
  IIii1 . write ( json . dumps ( o0OO0oooo ) )
  IIii1 . close ( )
 else :
  oO0ooO0OoOOOO ( 'Appending Favorites' )
  IIii1 = open ( I11II1i ) . read ( )
  I1I1IiI1 = json . loads ( IIii1 )
  I1I1IiI1 . append ( ( name , url , iconimage , fanart , mode ) )
  oO0 = open ( I11II1i , "w" )
  oO0 . write ( json . dumps ( I1I1IiI1 ) )
  oO0 . close ( )
  if 71 - 71: o0OO0 / ii % Oo0oO0ooo / oOoO0oo0OOOo % ooO00oOoo
  if 19 - 19: ooO00oOoo + Oo0oO0ooo / o0OO0 / ooO0OO000o
def OoO0O0oo0o ( name ) :
 I1I1IiI1 = json . loads ( open ( I11II1i ) . read ( ) )
 for IiII111iI1ii1 in range ( len ( I1I1IiI1 ) ) :
  if I1I1IiI1 [ IiII111iI1ii1 ] [ 0 ] == name :
   del I1I1IiI1 [ IiII111iI1ii1 ]
   oO0 = open ( I11II1i , "w" )
   oO0 . write ( json . dumps ( I1I1IiI1 ) )
   oO0 . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 46 - 46: oOoO0oo0OOOo - o0o00Oo0O
def O00OoooOoOo0o00o ( url ) :
 import urlresolver
 iIIi1 = urlresolver . HostedMediaFile ( url )
 if iIIi1 :
  iiIi1iI1iIii = urlresolver . resolve ( url )
  ooo0o0 = iiIi1iI1iIii
  if isinstance ( ooo0o0 , list ) :
   for I1iiiiI1iI in ooo0o0 :
    O00Oooo00 = o0OOOOO00o0O0 . getSetting ( 'quality' )
    if I1iiiiI1iI [ 'quality' ] == 'HD' :
     iiIi1iI1iIii = I1iiiiI1iI [ 'url' ]
     break
    elif I1iiiiI1iI [ 'quality' ] == 'SD' :
     iiIi1iI1iIii = I1iiiiI1iI [ 'url' ]
    elif I1iiiiI1iI [ 'quality' ] == '1080p' and o0OOOOO00o0O0 . getSetting ( '1080pquality' ) == 'true' :
     iiIi1iI1iIii = I1iiiiI1iI [ 'url' ]
     break
  else :
   iiIi1iI1iIii = ooo0o0
 else :
  xbmc . executebuiltin ( "XBMC.Notification(tvchopo,Urlresolver donot support this domain. - ,5000)" )
  iiIi1iI1iIii = url
 return iiIi1iI1iIii
def ooO0 ( url , listitem , pdialogue = None ) :
 if 34 - 34: ii1I % Oo0oO0ooo
 if url . lower ( ) . startswith ( 'plugin' ) and 'youtube' not in url . lower ( ) :
  print 'playing via runplugin'
  xbmc . executebuiltin ( 'XBMC.RunPlugin(' + url + ')' )
  for oooo0O0 in range ( 8 ) :
   xbmc . sleep ( 500 )
   try :
    if 80 - 80: ii / iI11I1II1I1I + Iii1ii1II11i / ii1I / IiiI
    if xbmc . getCondVisibility ( "Player.HasMedia" ) and xbmc . Player ( ) . isPlaying ( ) :
     return True
   except : pass
  print 'returning now'
  return False
 import CustomPlayer , time
 if 94 - 94: ii1I
 iii11 = CustomPlayer . MyXBMCPlayer ( )
 iii11 . pdialogue = pdialogue
 iiIIi1 = time . time ( )
 if 65 - 65: ii1I . Iii1ii1II11i / O0OOo
 print 'going to play'
 import time
 iIi1I1 = time . time ( )
 iii11 . play ( url , listitem )
 xbmc . sleep ( 1000 )
 if 11 - 11: Oo0oO0ooo * O0OOo / O0OOo - Oo0ooO0oo0oO
 try :
  while iii11 . is_active :
   xbmc . sleep ( 400 )
   if 68 - 68: I11i11Ii % Oo0oO0ooo - Oo0oO0ooo / I11i11Ii + Iii1ii1II11i - i1iIi11iIIi1I
   if iii11 . urlplayed :
    print 'yes played'
    return True
   if time . time ( ) - iIi1I1 > 4 : return False
   if 65 - 65: O0OOo - ii1I
 except : pass
 print 'not played' , url
 return False
def O00Ooiii ( name , mu_playlist , queueVideo = None ) :
 oOOO00o000o = xbmc . PlayList ( xbmc . PLAYLIST_VIDEO )
 if 93 - 93: I1i1iI1i * ooO0OO000o / o00ooo0 - IiiI
 if '$$LSPlayOnlyOne$$' in mu_playlist [ 0 ] :
  mu_playlist [ 0 ] = mu_playlist [ 0 ] . replace ( '$$LSPlayOnlyOne$$' , '' )
  import urlparse
  Oo0oo = [ ]
  Oo00OOoOo = 0
  IiiIiiIi = xbmcgui . DialogProgress ( )
  IiiIiiIi . create ( 'Progress' , 'Trying Multiple Links' )
  for oooo0O0 in mu_playlist :
   if 87 - 87: ii
   if 64 - 64: ii1I
   if '$$lsname=' in oooo0O0 :
    I1ii1i1iiii = oooo0O0 . split ( '$$lsname=' ) [ 1 ] . split ( '&regexs' ) [ 0 ]
    Oo0oo . append ( I1ii1i1iiii )
    mu_playlist [ Oo00OOoOo ] = oooo0O0 . split ( '$$lsname=' ) [ 0 ] + ( '&regexs' + oooo0O0 . split ( '&regexs' ) [ 1 ] if '&regexs' in oooo0O0 else '' )
   else :
    I1ii1i1iiii = urlparse . urlparse ( oooo0O0 ) . netloc
    if I1ii1i1iiii == '' :
     Oo0oo . append ( name )
    else :
     Oo0oo . append ( I1ii1i1iiii )
   IiII111iI1ii1 = Oo00OOoOo
   Oo00OOoOo += 1
   if 45 - 45: o00ooo0 / O0OOo . ii + i11ii11iIi11i
   O00oO000Oo0 = Oo0oo [ IiII111iI1ii1 ]
   if IiiIiiIi . iscanceled ( ) : return
   IiiIiiIi . update ( Oo00OOoOo / len ( mu_playlist ) * 100 , "" , "Link#%d" % ( Oo00OOoOo ) , O00oO000Oo0 )
   print 'auto playnamexx' , O00oO000Oo0
   if "&mode=19" in mu_playlist [ IiII111iI1ii1 ] :
    if 26 - 26: i1iIi11iIIi1I + o0o00Oo0O - iI11I1II1I1I
    iiI1 = xbmcgui . ListItem ( O00oO000Oo0 , iconImage = oOoo00o0oOO , thumbnailImage = oOoo00o0oOO )
    iiI1 . setInfo ( type = 'Video' , infoLabels = { 'Title' : O00oO000Oo0 } )
    iiI1 . setProperty ( "IsPlayable" , "true" )
    I1IIIIIi1IIiI = O00OoooOoOo0o00o ( mu_playlist [ IiII111iI1ii1 ] . replace ( '&mode=19' , '' ) . replace ( ';' , '' ) )
    iiI1 . setPath ( I1IIIIIi1IIiI )
    if 26 - 26: IiiI % Oo0ooO0oo0oO + Oo0ooO0oo0oO % I1i1iI1i * Ii / o00
    OOoO0oO00o = ooO0 ( I1IIIIIi1IIiI , iiI1 )
   elif "$doregex" in mu_playlist [ IiII111iI1ii1 ] :
    if 78 - 78: i1iIi11iIIi1I * ooO00oOoo - ii - i11ii11iIi11i
    o0OOo = mu_playlist [ IiII111iI1ii1 ] . split ( '&regexs=' )
    if 42 - 42: o0o00Oo0O % o00ooo0 - iI11I1II1I1I + ooO00oOoo % I11i11Ii + O0OOo
    IiII , Iii = Ooooooo ( o0OOo [ 1 ] , o0OOo [ 0 ] )
    o0OoO0oo0O0o = IiII . replace ( ';' , '' )
    iiI1 = xbmcgui . ListItem ( O00oO000Oo0 , iconImage = oOoo00o0oOO , thumbnailImage = oOoo00o0oOO )
    iiI1 . setInfo ( type = 'Video' , infoLabels = { 'Title' : O00oO000Oo0 } )
    iiI1 . setProperty ( "IsPlayable" , "true" )
    iiI1 . setPath ( o0OoO0oo0O0o )
    if 6 - 6: ooO0OO000o % ooO00oOoo
    OOoO0oO00o = ooO0 ( o0OoO0oo0O0o , iiI1 )
    if 41 - 41: Oo0oO0ooo - ooO0OO000o . ooO0OO000o + I11i11Ii
   else :
    IiII = mu_playlist [ IiII111iI1ii1 ]
    IiII = IiII . split ( '&regexs=' ) [ 0 ]
    iiI1 = xbmcgui . ListItem ( O00oO000Oo0 , iconImage = oOoo00o0oOO , thumbnailImage = oOoo00o0oOO )
    iiI1 . setInfo ( type = 'Video' , infoLabels = { 'Title' : O00oO000Oo0 } )
    iiI1 . setProperty ( "IsPlayable" , "true" )
    iiI1 . setPath ( IiII )
    if 59 - 59: iI11I1II1I1I % o00ooo0 . Ii
    OOoO0oO00o = ooO0 ( IiII , iiI1 )
    print 'played' , OOoO0oO00o
   print 'played' , OOoO0oO00o
   if OOoO0oO00o : return
  return
 if o0OOOOO00o0O0 . getSetting ( 'ask_playlist_items' ) == 'true' and not queueVideo :
  import urlparse
  Oo0oo = [ ]
  Oo00OOoOo = 0
  for oooo0O0 in mu_playlist :
   if '$$lsname=' in oooo0O0 :
    I1ii1i1iiii = oooo0O0 . split ( '$$lsname=' ) [ 1 ] . split ( '&regexs' ) [ 0 ]
    Oo0oo . append ( I1ii1i1iiii )
    mu_playlist [ Oo00OOoOo ] = oooo0O0 . split ( '$$lsname=' ) [ 0 ] + ( '&regexs' + oooo0O0 . split ( '&regexs' ) [ 1 ] if '&regexs' in oooo0O0 else '' )
   else :
    I1ii1i1iiii = urlparse . urlparse ( oooo0O0 ) . netloc
    if I1ii1i1iiii == '' :
     Oo0oo . append ( name )
    else :
     Oo0oo . append ( I1ii1i1iiii )
     if 59 - 59: IiiI . o0OO0 . o00ooo0 * oOoO0oo0OOOo * i11ii11iIi11i + i1iIi11iIIi1I
   Oo00OOoOo += 1
  O0OOoOooO00 = xbmcgui . Dialog ( )
  IiII111iI1ii1 = O0OOoOooO00 . select ( 'Choose a video source' , Oo0oo )
  if IiII111iI1ii1 >= 0 :
   O00oO000Oo0 = Oo0oo [ IiII111iI1ii1 ]
   print 'playnamexx' , O00oO000Oo0
   if "&mode=19" in mu_playlist [ IiII111iI1ii1 ] :
    if 89 - 89: o0OO0
    iiI1 = xbmcgui . ListItem ( O00oO000Oo0 , iconImage = oOoo00o0oOO , thumbnailImage = oOoo00o0oOO )
    iiI1 . setInfo ( type = 'Video' , infoLabels = { 'Title' : O00oO000Oo0 } )
    iiI1 . setProperty ( "IsPlayable" , "true" )
    I1IIIIIi1IIiI = O00OoooOoOo0o00o ( mu_playlist [ IiII111iI1ii1 ] . replace ( '&mode=19' , '' ) . replace ( ';' , '' ) )
    iiI1 . setPath ( I1IIIIIi1IIiI )
    xbmc . Player ( ) . play ( I1IIIIIi1IIiI , iiI1 )
   elif "$doregex" in mu_playlist [ IiII111iI1ii1 ] :
    if 87 - 87: o00 % i1iIi11iIIi1I
    o0OOo = mu_playlist [ IiII111iI1ii1 ] . split ( '&regexs=' )
    if 62 - 62: i11ii11iIi11i + O0OOo / o00 * Ii
    IiII , Iii = Ooooooo ( o0OOo [ 1 ] , o0OOo [ 0 ] )
    o0OoO0oo0O0o = IiII . replace ( ';' , '' )
    iiI1 = xbmcgui . ListItem ( O00oO000Oo0 , iconImage = oOoo00o0oOO , thumbnailImage = oOoo00o0oOO )
    iiI1 . setInfo ( type = 'Video' , infoLabels = { 'Title' : O00oO000Oo0 } )
    iiI1 . setProperty ( "IsPlayable" , "true" )
    iiI1 . setPath ( o0OoO0oo0O0o )
    xbmc . Player ( ) . play ( o0OoO0oo0O0o , iiI1 )
    if 37 - 37: o00
   else :
    IiII = mu_playlist [ IiII111iI1ii1 ]
    IiII = IiII . split ( '&regexs=' ) [ 0 ]
    iiI1 = xbmcgui . ListItem ( O00oO000Oo0 , iconImage = oOoo00o0oOO , thumbnailImage = oOoo00o0oOO )
    iiI1 . setInfo ( type = 'Video' , infoLabels = { 'Title' : O00oO000Oo0 } )
    iiI1 . setProperty ( "IsPlayable" , "true" )
    iiI1 . setPath ( IiII )
    xbmc . Player ( ) . play ( IiII , iiI1 )
 elif not queueVideo :
  if 33 - 33: i11ii11iIi11i - o0o00Oo0O - i11ii11iIi11i
  oOOO00o000o . clear ( )
  OOoOooOoOOOoo = 0
  for oooo0O0 in mu_playlist :
   OOoOooOoOOOoo += 1
   O000oooOO0Oo0 = xbmcgui . ListItem ( '%s) %s' % ( str ( OOoOooOoOOOoo ) , name ) )
   if 31 - 31: Oo0oO0ooo - i11ii11iIi11i / Oo0ooO0oo0oO . ii1I / o00ooo0
   try :
    if "$doregex" in oooo0O0 :
     o0OOo = oooo0O0 . split ( '&regexs=' )
     if 66 - 66: i11ii11iIi11i
     IiII , Iii = Ooooooo ( o0OOo [ 1 ] , o0OOo [ 0 ] )
    elif "&mode=19" in oooo0O0 :
     IiII = O00OoooOoOo0o00o ( oooo0O0 . replace ( '&mode=19' , '' ) . replace ( ';' , '' ) )
    if IiII :
     oOOO00o000o . add ( IiII , O000oooOO0Oo0 )
    else :
     raise
   except Exception :
    oOOO00o000o . add ( oooo0O0 , O000oooOO0Oo0 )
    pass
    if 72 - 72: ooO00oOoo
  xbmc . executebuiltin ( 'playlist.playoffset(video,0)' )
 else :
  if 91 - 91: ooO0OO000o / Oo0oO0ooo + iI11I1II1I1I . I1i1iI1i - o0o00Oo0O
  i1oO = xbmcgui . ListItem ( name )
  oOOO00o000o . add ( mu_playlist , i1oO )
  if 70 - 70: o00ooo0 * o0OO0 - I1i1iI1i + i1iIi11iIIi1I % Iii1ii1II11i - Oo0oO0ooo
  if 81 - 81: o0o00Oo0O . o0o00Oo0O
def OoO00OooO0 ( name , url ) :
 if o0OOOOO00o0O0 . getSetting ( 'save_location' ) == "" :
  xbmc . executebuiltin ( "XBMC.Notification('tvchopo','Choose a location to save files.',15000," + IIiiiiiiIi1I1 + ")" )
  o0OOOOO00o0O0 . openSettings ( )
 oOO = { 'url' : url , 'download_path' : o0OOOOO00o0O0 . getSetting ( 'save_location' ) }
 downloader . download ( name , oOO )
 O0OOoOooO00 = xbmcgui . Dialog ( )
 I1ii1Ii1ii11i = O0OOoOooO00 . yesno ( 'tvchopo' , 'Do you want to add this file as a source?' )
 if I1ii1Ii1ii11i :
  I1iII1iIi1I ( os . path . join ( o0OOOOO00o0O0 . getSetting ( 'save_location' ) , name ) )
  if 98 - 98: Oo0ooO0oo0oO + o00ooo0
def OOOOIIIIiI11Ii1i ( url , name ) :
 if 100 - 100: o00 + I1i1iI1i + O0OOo + o00 / ii1I
 Oo0oOO0O00 = [ 'plugin://plugin.video.genesis/?action=shows_search' , 'plugin://plugin.video.genesis/?action=movies_search' , 'plugin://plugin.video.salts/?mode=search&amp;section=Movies' , 'plugin://plugin.video.salts/?mode=search&amp;section=TV' , 'plugin://plugin.video.muchmovies.hd/?action=movies_search' , 'plugin://plugin.video.viooz.co/?action=root_search' , 'plugin://plugin.video.ororotv/?action=shows_search' , 'plugin://plugin.video.yifymovies.hd/?action=movies_search' , 'plugin://plugin.video.cartoonhdtwo/?description&amp;fanart&amp;iconimage&amp;mode=3&amp;name=Search&amp;url=url' , 'plugin://plugin.video.youtube/kodion/search/list/' , 'plugin://plugin.video.dailymotion_com/?mode=search&amp;url' , 'plugin://plugin.video.vimeo/kodion/search/list/' ]
 if 55 - 55: O0OOo % i1iIi11iIIi1I % IiiI
 if 29 - 29: Oo0oO0ooo / iI11I1II1I1I + Iii1ii1II11i % o00 % I1i1iI1i
 if 46 - 46: iI11I1II1I1I
 if 70 - 70: ii1I . I1i1iI1i
 if 74 - 74: I1i1iI1i
 if 58 - 58: iI11I1II1I1I * i11ii11iIi11i * ooO00oOoo * O0OOo . ii
 if 6 - 6: Iii1ii1II11i - o0OO0 * Ii + oOoO0oo0OOOo / O0OOo % Oo0ooO0oo0oO
 if 38 - 38: Oo0ooO0oo0oO % Oo0oO0ooo % ooO0OO000o - i1iIi11iIIi1I - iI11I1II1I1I
 if 9 - 9: IiiI % Iii1ii1II11i . Iii1ii1II11i
 if 28 - 28: ii % o0OO0 + Iii1ii1II11i + o0o00Oo0O . ooO00oOoo
 if 80 - 80: Ii % Iii1ii1II11i
 if 54 - 54: IiiI + I1i1iI1i - iI11I1II1I1I % O0OOo % Oo0oO0ooo
 Oo0oo = [ 'Gensis TV' , 'Genesis Movie' , 'Salt movie' , 'salt TV' , 'Muchmovies' , 'viooz' , 'ORoroTV' , 'Yifymovies' , 'cartoonHD' , 'Youtube' , 'DailyMotion' , 'Vimeo' ]
 if 19 - 19: Iii1ii1II11i / iI11I1II1I1I % ii1I . ii
 O0OOoOooO00 = xbmcgui . Dialog ( )
 IiII111iI1ii1 = O0OOoOooO00 . select ( 'Choose a video source' , Oo0oo )
 if 57 - 57: O0OOo . i1iIi11iIIi1I - i11ii11iIi11i - Ii * ooO00oOoo / IiiI
 if IiII111iI1ii1 >= 0 :
  url = Oo0oOO0O00 [ IiII111iI1ii1 ]
  if 79 - 79: Iii1ii1II11i + IiiI % i1iIi11iIIi1I * IiiI
  iiii11IiIiI ( url )
  if 8 - 8: ooO00oOoo + i11ii11iIi11i
def iIi1IIIi1 ( name , url , mode , iconimage , fanart , description , genre , date , credits , showcontext = False , regexs = None , reg_url = None , allinfo = { } ) :
 if 9 - 9: Oo0ooO0oo0oO + IiiI
 if 8 - 8: Oo0ooO0oo0oO * i1iIi11iIIi1I / o00 - i11ii11iIi11i - ii
 if 100 - 100: o0OO0 . iI11I1II1I1I . iI11I1II1I1I
 if regexs and len ( regexs ) > 0 :
  oOOo0ooO0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&regexs=" + regexs
 else :
  oOOo0ooO0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&fanart=" + urllib . quote_plus ( fanart )
  if 38 - 38: ooO00oOoo
 I1II1 = True
 if date == '' :
  date = None
 else :
  description += '\n\nDate: %s' % date
 iiI1 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 if len ( allinfo ) < 1 :
  iiI1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description , "Genre" : genre , "dateadded" : date , "credits" : credits } )
 else :
  iiI1 . setInfo ( type = "Video" , infoLabels = allinfo )
 iiI1 . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  O0o0OO00O = [ ]
  oOIIiIi = o0OOOOO00o0O0 . getSetting ( 'parentalblocked' )
  oOIIiIi = oOIIiIi == "true"
  OooOooO = o0OOOOO00o0O0 . getSetting ( 'parentalblockedpin' )
  if 74 - 74: I1i1iI1i
  if len ( OooOooO ) > 0 :
   if oOIIiIi :
    O0o0OO00O . append ( ( 'Disable Parental Block' , 'XBMC.RunPlugin(%s?mode=55&name=%s)' % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
   else :
    O0o0OO00O . append ( ( 'Enable Parental Block' , 'XBMC.RunPlugin(%s?mode=56&name=%s)' % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
    if 98 - 98: o0OO0 / ii % o00ooo0 * ooO0OO000o - i11ii11iIi11i
  if showcontext == 'source' :
   if 95 - 95: I11i11Ii % ooO00oOoo * I11i11Ii + o0o00Oo0O . ooO00oOoo % ii
   if name in str ( ii11i1 ) :
    O0o0OO00O . append ( ( 'Remove from Sources' , 'XBMC.RunPlugin(%s?mode=8&name=%s)' % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
    if 6 - 6: oOoO0oo0OOOo - O0OOo * IiiI + oOoO0oo0OOOo % IiiI
    if 100 - 100: i11ii11iIi11i % ooO00oOoo - I1i1iI1i % I1i1iI1i % I1i1iI1i / O0OOo
  elif showcontext == 'download' :
   O0o0OO00O . append ( ( 'Download' , 'XBMC.RunPlugin(%s?url=%s&mode=9&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , urllib . quote_plus ( name ) ) ) )
  elif showcontext == 'fav' :
   O0o0OO00O . append ( ( 'Remove from tvchopo Favorites' , 'XBMC.RunPlugin(%s?mode=6&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if showcontext == '!!update' :
   OOO000Oo = (
 '%s?url=%s&mode=17&regexs=%s'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( reg_url ) , regexs )
 )
   O0o0OO00O . append ( ( '[COLOR yellow]!!update[/COLOR]' , 'XBMC.RunPlugin(%s)' % OOO000Oo ) )
  if not name in OOOooOooo00O0 :
   O0o0OO00O . append ( ( 'Add to tvchopo Favorites' , 'XBMC.RunPlugin(%s?mode=5&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  iiI1 . addContextMenuItems ( O0o0OO00O )
 I1II1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOOo0ooO0 , listitem = iiI1 , isFolder = True )
 return I1II1
def I1IIIi1i ( url , title , media_type = 'video' ) :
 if 54 - 54: ooO0OO000o . ii1I / Iii1ii1II11i % I11i11Ii / ooO00oOoo
 if 65 - 65: oOoO0oo0OOOo . oOoO0oo0OOOo - o0OO0 + i1iIi11iIIi1I / Ii
 import youtubedl
 if not url == '' :
  if media_type == 'audio' :
   youtubedl . single_YD ( url , download = True , audio = True )
  else :
   youtubedl . single_YD ( url , download = True )
 elif xbmc . Player ( ) . isPlaying ( ) == True :
  import YDStreamExtractor
  if YDStreamExtractor . isDownloading ( ) == True :
   if 90 - 90: iI11I1II1I1I + oOoO0oo0OOOo
   YDStreamExtractor . manageDownloads ( )
  else :
   IiI = xbmc . Player ( ) . getPlayingFile ( )
   if 16 - 16: i1iIi11iIIi1I / i11ii11iIi11i / o00 / iI11I1II1I1I
   IiI = IiI . split ( '|User-Agent=' ) [ 0 ]
   O000oooOO0Oo0 = { 'url' : IiI , 'title' : title , 'media_type' : media_type }
   youtubedl . single_YD ( '' , download = True , dl_info = O000oooOO0Oo0 )
 else :
  xbmc . executebuiltin ( "XBMC.Notification(DOWNLOAD,First Play [COLOR yellow]WHILE playing download[/COLOR] ,10000)" )
  if 44 - 44: i1iIi11iIIi1I . i1iIi11iIIi1I + ii * Ii / I1i1iI1i + ooO00oOoo
  if 17 - 17: Oo0ooO0oo0oO + ooO0OO000o
def I1i11I11Iii ( string ) :
 if isinstance ( string , basestring ) :
  if isinstance ( string , unicode ) :
   string = string . encode ( 'ascii' , 'ignore' )
 return string
def i1i1I11I ( string , encoding = 'utf-8' ) :
 if isinstance ( string , basestring ) :
  if not isinstance ( string , unicode ) :
   string = unicode ( string , encoding , 'ignore' )
 return string
def iiiIi111i1i ( s ) : return "" . join ( filter ( lambda OOo0OOooo0 : ord ( OOo0OOooo0 ) < 128 , s ) )
if 93 - 93: o0o00Oo0O - i11ii11iIi11i . I11i11Ii
def oOOOoo ( command ) :
 I1I1IiI1 = ''
 try :
  I1I1IiI1 = xbmc . executeJSONRPC ( i1i1I11I ( command ) )
 except UnicodeEncodeError :
  I1I1IiI1 = xbmc . executeJSONRPC ( I1i11I11Iii ( command ) )
  if 29 - 29: I11i11Ii + Ii . o0o00Oo0O
 return i1i1I11I ( I1I1IiI1 )
 if 75 - 75: ooO00oOoo + iI11I1II1I1I
def iiii11IiIiI ( url , give_me_result = None , playlist = False ) :
 if 'audio' in url :
  IiiiI1I1IIIi = i1i1I11I ( '{"jsonrpc":"2.0","method":"Files.GetDirectory","params": {"directory":"%s","media":"video", "properties": ["title", "album", "artist", "duration","thumbnail", "year"]}, "id": 1}' ) % url
 else :
  IiiiI1I1IIIi = i1i1I11I ( '{"jsonrpc":"2.0","method":"Files.GetDirectory","params":{"directory":"%s","media":"video","properties":[ "plot","playcount","director", "genre","votes","duration","trailer","premiered","thumbnail","title","year","dateadded","fanart","rating","season","episode","studio","mpaa"]},"id":1}' ) % url
 I1i = json . loads ( oOOOoo ( IiiiI1I1IIIi ) )
 if 59 - 59: ii - ooO00oOoo % IiiI . I1i1iI1i + ii1I * I1i1iI1i
 if give_me_result :
  return I1i
 if I1i . has_key ( 'error' ) :
  return
 else :
  if 5 - 5: ooO0OO000o - Oo0oO0ooo
  for oooo0O0 in I1i [ 'result' ] [ 'files' ] :
   O0O00oO0OoO0o = { }
   url = oooo0O0 [ 'file' ]
   OO0Oooo0oOO0O = iiiIi111i1i ( oooo0O0 [ 'label' ] )
   oOOoO0o0oO = iiiIi111i1i ( oooo0O0 [ 'thumbnail' ] )
   o0o = iiiIi111i1i ( oooo0O0 [ 'fanart' ] )
   O0O00oO0OoO0o = dict ( ( k , v ) for k , v in oooo0O0 . iteritems ( ) if not v == '0' or not v == - 1 or v == '' )
   O0O00oO0OoO0o . pop ( "file" , None )
   if oooo0O0 [ 'filetype' ] == 'file' :
    if playlist :
     O00Ooiii ( OO0Oooo0oOO0O , url , queueVideo = '1' )
     continue
    else :
     O0O0o0oOOO ( url , OO0Oooo0oOO0O , oOOoO0o0oO , o0o , '' , '' , '' , '' , None , '' , total = len ( I1i [ 'result' ] [ 'files' ] ) , allinfo = O0O00oO0OoO0o )
     if 5 - 5: Oo0ooO0oo0oO % i1iIi11iIIi1I % Oo0oO0ooo % O0OOo
     if oooo0O0 [ 'type' ] and oooo0O0 [ 'type' ] == 'tvshow' :
      xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , 'tvshows' )
     elif oooo0O0 [ 'episode' ] > 0 :
      xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , 'episodes' )
      if 17 - 17: o00ooo0 + ooO0OO000o + ii / Oo0ooO0oo0oO / Oo0oO0ooo
   else :
    iIi1IIIi1 ( OO0Oooo0oOO0O , url , 53 , oOOoO0o0oO , o0o , '' , '' , '' , '' , allinfo = O0O00oO0OoO0o )
  xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
  if 80 - 80: IiiI % ii1I / I1i1iI1i
def O0O0o0oOOO ( url , name , iconimage , fanart , description , genre , date , showcontext , playlist , regexs , total , setCookie = "" , allinfo = { } ) :
 if 56 - 56: ii1I . Ii
 O0o0OO00O = [ ]
 oOIIiIi = o0OOOOO00o0O0 . getSetting ( 'parentalblocked' )
 oOIIiIi = oOIIiIi == "true"
 OooOooO = o0OOOOO00o0O0 . getSetting ( 'parentalblockedpin' )
 if 15 - 15: ooO0OO000o * o0OO0 % o00 / Ii - o0OO0 + i1iIi11iIIi1I
 if len ( OooOooO ) > 0 :
  if oOIIiIi :
   O0o0OO00O . append ( ( 'Disable Parental Block' , 'XBMC.RunPlugin(%s?mode=55&name=%s)' % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  else :
   O0o0OO00O . append ( ( 'Enable Parental Block' , 'XBMC.RunPlugin(%s?mode=56&name=%s)' % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
   if 9 - 9: I1i1iI1i - o0OO0 + o0o00Oo0O / o00 % ii1I
 try :
  name = name . encode ( 'utf-8' )
 except : pass
 I1II1 = True
 oO000o0OO0OO0 = False
 if regexs :
  i11ii1I1 = '17'
  if 'listrepeat' in regexs :
   oO000o0OO0OO0 = True
   if 10 - 10: Oo0oO0ooo / ii
  O0o0OO00O . append ( ( '[COLOR white]!!Download Currently Playing!![/COLOR]' , 'XBMC.RunPlugin(%s?url=%s&mode=21&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , urllib . quote_plus ( name ) ) ) )
 elif ( any ( x in url for x in i1iIIIiI1I ) and url . startswith ( 'http' ) ) or url . endswith ( '&mode=19' ) :
  url = url . replace ( '&mode=19' , '' )
  i11ii1I1 = '19'
  O0o0OO00O . append ( ( '[COLOR white]!!Download Currently Playing!![/COLOR]' , 'XBMC.RunPlugin(%s?url=%s&mode=21&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , urllib . quote_plus ( name ) ) ) )
 elif url . endswith ( '&mode=18' ) :
  url = url . replace ( '&mode=18' , '' )
  i11ii1I1 = '18'
  O0o0OO00O . append ( ( '[COLOR white]!!Download!![/COLOR]' , 'XBMC.RunPlugin(%s?url=%s&mode=23&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , urllib . quote_plus ( name ) ) ) )
  if o0OOOOO00o0O0 . getSetting ( 'dlaudioonly' ) == 'true' :
   O0o0OO00O . append ( ( '!!Download [COLOR seablue]Audio!![/COLOR]' , 'XBMC.RunPlugin(%s?url=%s&mode=24&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , urllib . quote_plus ( name ) ) ) )
 elif url . startswith ( 'magnet:?xt=' ) :
  if '&' in url and not '&amp;' in url :
   url = url . replace ( '&' , '&amp;' )
  url = 'plugin://plugin.video.pulsar/play?uri=' + url
  i11ii1I1 = '12'
 else :
  i11ii1I1 = '12'
  O0o0OO00O . append ( ( '[COLOR white]!!Download Currently Playing!![/COLOR]' , 'XBMC.RunPlugin(%s?url=%s&mode=21&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , urllib . quote_plus ( name ) ) ) )
 if 'plugin://plugin.video.youtube/play/?video_id=' in url :
  IiiiIIiii = url . replace ( 'plugin://plugin.video.youtube/play/?video_id=' , 'https://www.youtube.com/watch?v=' )
  O0o0OO00O . append ( ( '!!Download [COLOR blue]Audio!![/COLOR]' , 'XBMC.RunPlugin(%s?url=%s&mode=24&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( IiiiIIiii ) , urllib . quote_plus ( name ) ) ) )
 oOOo0ooO0 = sys . argv [ 0 ] + "?"
 OO0 = False
 if playlist :
  if o0OOOOO00o0O0 . getSetting ( 'add_playlist' ) == "false" and '$$LSPlayOnlyOne$$' not in playlist [ 0 ] :
   oOOo0ooO0 += "url=" + urllib . quote_plus ( url ) + "&mode=" + i11ii1I1
  else :
   oOOo0ooO0 += "mode=13&name=%s&playlist=%s" % ( urllib . quote_plus ( name ) , urllib . quote_plus ( str ( playlist ) . replace ( ',' , '||' ) ) )
   name = name + '[COLOR magenta] (' + str ( len ( playlist ) ) + ' items )[/COLOR]'
   OO0 = True
 else :
  oOOo0ooO0 += "url=" + urllib . quote_plus ( url ) + "&mode=" + i11ii1I1
 if regexs :
  oOOo0ooO0 += "&regexs=" + regexs
 if not setCookie == '' :
  oOOo0ooO0 += "&setCookie=" + urllib . quote_plus ( setCookie )
 if iconimage and not iconimage == '' :
  oOOo0ooO0 += "&iconimage=" + urllib . quote_plus ( iconimage )
  if 81 - 81: Ii + o00ooo0 % Ii - ii1I
 if date == '' :
  date = None
 else :
  description += '\n\nDate: %s' % date
 iiI1 = xbmcgui . ListItem ( name , iconImage = "DefaultVideo.png" , thumbnailImage = iconimage )
 if 9 - 9: o0OO0
 if allinfo == None or len ( allinfo ) < 1 :
  iiI1 . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description , "Genre" : genre , "dateadded" : date } )
 else :
  iiI1 . setInfo ( type = "Video" , infoLabels = allinfo )
 iiI1 . setProperty ( "Fanart_Image" , fanart )
 if 2 - 2: iI11I1II1I1I * I11i11Ii % ii1I % Iii1ii1II11i + ii + I11i11Ii
 if ( not OO0 ) and not any ( x in url for x in OOoO000O0OO ) and not '$PLAYERPROXY$=' in url :
  if regexs :
   if 16 - 16: Oo0ooO0oo0oO
   if '$pyFunction:playmedia(' not in urllib . unquote_plus ( regexs ) and 'notplayable' not in urllib . unquote_plus ( regexs ) and 'listrepeat' not in urllib . unquote_plus ( regexs ) :
    if 63 - 63: o00
    iiI1 . setProperty ( 'IsPlayable' , 'true' )
  else :
   iiI1 . setProperty ( 'IsPlayable' , 'true' )
 else :
  oO0ooO0OoOOOO ( 'NOT setting isplayable' + url )
 if showcontext :
  if 11 - 11: o00 - iI11I1II1I1I
  if showcontext == 'fav' :
   O0o0OO00O . append (
 ( 'Remove from tvchopo Favorites' , 'XBMC.RunPlugin(%s?mode=6&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) )
 )
  elif not name in OOOooOooo00O0 :
   try :
    ooOo0O0 = (
 '%s?mode=5&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=0'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) )
 )
   except :
    ooOo0O0 = (
 '%s?mode=5&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=0'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage . encode ( "utf-8" ) ) , urllib . quote_plus ( fanart . encode ( "utf-8" ) ) )
 )
   if playlist :
    ooOo0O0 += 'playlist=' + urllib . quote_plus ( str ( playlist ) . replace ( ',' , '||' ) )
   if regexs :
    ooOo0O0 += "&regexs=" + regexs
   O0o0OO00O . append ( ( 'Add to tvchopo Favorites' , 'XBMC.RunPlugin(%s)' % ooOo0O0 ) )
  iiI1 . addContextMenuItems ( O0o0OO00O )
 try :
  if not playlist is None :
   if o0OOOOO00o0O0 . getSetting ( 'add_playlist' ) == "false" :
    ooo0 = name . split ( ') ' ) [ 1 ]
    I11OOO0 = [
 ( 'Play ' + ooo0 + ' PlayList' , 'XBMC.RunPlugin(%s?mode=13&name=%s&playlist=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( ooo0 ) , urllib . quote_plus ( str ( playlist ) . replace ( ',' , '||' ) ) ) )
 ]
    iiI1 . addContextMenuItems ( I11OOO0 )
 except : pass
 if 16 - 16: o00 / iI11I1II1I1I + Oo0ooO0oo0oO * o00 * I1i1iI1i
 I1II1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOOo0ooO0 , listitem = iiI1 , totalItems = total , isFolder = oO000o0OO0OO0 )
 if 8 - 8: ooO00oOoo
 if 15 - 15: i1iIi11iIIi1I / o00ooo0 % o0o00Oo0O + Iii1ii1II11i
 return I1II1
 if 96 - 96: O0OOo . ii
 if 39 - 39: Oo0ooO0oo0oO + i11ii11iIi11i
def oOoOOOO0OOO ( url , name , iconimage , setresolved = True , reg = None ) :
 print 'playsetresolved' , url , setresolved
 if url == None :
  xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
  return
 if setresolved :
  O0oo0oO00o = True
  if '$$LSDirect$$' in url :
   url = url . replace ( '$$LSDirect$$' , '' )
   O0oo0oO00o = False
  if reg and 'notplayable' in reg :
   O0oo0oO00o = False
   if 35 - 35: o00 * iI11I1II1I1I / O0OOo * ii1I * o0o00Oo0O % iI11I1II1I1I
  iiI1 = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
  iiI1 . setInfo ( type = 'Video' , infoLabels = { 'Title' : name } )
  iiI1 . setProperty ( "IsPlayable" , "true" )
  iiI1 . setPath ( url )
  if not O0oo0oO00o :
   xbmc . Player ( ) . play ( url )
  else :
   xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , iiI1 )
   if 97 - 97: Ii + i1iIi11iIIi1I * Oo0ooO0oo0oO % o00 . Oo0oO0ooo
 else :
  xbmc . executebuiltin ( 'XBMC.RunPlugin(' + url + ')' )
  if 4 - 4: o0o00Oo0O . o00 - iI11I1II1I1I
  if 19 - 19: Oo0ooO0oo0oO % i11ii11iIi11i / o00ooo0 + ooO0OO000o % ii
  if 89 - 89: o00ooo0
  if 51 - 51: o00
def ooooO0oOoOOoO ( link ) :
 IiII = urllib . urlopen ( link )
 O00O0Oo0 = IiII . read ( )
 IiII . close ( )
 OoO = O00O0Oo0 . split ( "Jetzt" )
 iI11IiI1i1 = OoO [ 1 ] . split ( 'programm/detail.php?const_id=' )
 ooO = iI11IiI1i1 [ 1 ] . split ( '<br /><a href="/' )
 oOoO0 = ooO [ 0 ] [ 40 : len ( ooO [ 0 ] ) ]
 Iii1II1ii = iI11IiI1i1 [ 2 ] . split ( "</a></p></div>" )
 ooOo00 = Iii1II1ii [ 0 ] [ 17 : len ( Iii1II1ii [ 0 ] ) ]
 ooOo00 = ooOo00 . encode ( 'utf-8' )
 return "  - " + ooOo00 + " - " + oOoO0
 if 98 - 98: i11ii11iIi11i . iI11I1II1I1I % ii % i1iIi11iIIi1I - Iii1ii1II11i
 if 86 - 86: oOoO0oo0OOOo . Oo0oO0ooo
def o0o0O ( url , regex ) :
 I1I1IiI1 = I11III1II ( url )
 try :
  OOoOooOoOOOoo = re . findall ( regex , I1I1IiI1 ) [ 0 ]
  return OOoOooOoOOOoo
 except :
  oO0ooO0OoOOOO ( 'regex failed' )
  oO0ooO0OoOOOO ( regex )
  return
  if 10 - 10: o00 * o00ooo0 - O0OOo . I1i1iI1i - Oo0ooO0oo0oO
  if 94 - 94: I11i11Ii % Oo0oO0ooo + i11ii11iIi11i
  if 90 - 90: ii1I + o0o00Oo0O - o0OO0 . o00 + iI11I1II1I1I
def O0ooo0ooOoo0o ( d , root = "root" , nested = 0 ) :
 if 48 - 48: Oo0ooO0oo0oO * iI11I1II1I1I
 I1IiI11I1Ii11II = lambda oo0ooOoOOoO : '<' + oo0ooOoOOoO + '>'
 Oo0000o = lambda oo0ooOoOOoO : '</' + oo0ooOoOOoO + '>\n'
 if 33 - 33: oOoO0oo0OOOo * I1i1iI1i
 iiIiII1 = lambda i1iIi1iIi1i , ii111iI : ii111iI + I1IiI11I1Ii11II ( ii11I1 ) + str ( i1iIi1iIi1i ) + Oo0000o ( ii11I1 )
 ii111iI = I1IiI11I1Ii11II ( root ) + '\n' if root else ""
 if 26 - 26: ooO00oOoo . o00ooo0 + I11i11Ii . oOoO0oo0OOOo + Oo0ooO0oo0oO
 for ii11I1 , I1Ii1I in d . iteritems ( ) :
  Ii1111iiI = type ( I1Ii1I )
  if nested == 0 : ii11I1 = 'regex'
  if Ii1111iiI is list :
   for i1iIi1iIi1i in I1Ii1I :
    i1iIi1iIi1i = escape ( i1iIi1iIi1i )
    ii111iI = iiIiII1 ( i1iIi1iIi1i , ii111iI )
    if 15 - 15: O0OOo . IiiI + oOoO0oo0OOOo . iI11I1II1I1I % O0OOo + o0o00Oo0O
  if Ii1111iiI is dict :
   ii111iI = iiIiII1 ( '\n' + O0ooo0ooOoo0o ( I1Ii1I , None , nested + 1 ) , ii111iI )
  if Ii1111iiI is not list and Ii1111iiI is not dict :
   if not I1Ii1I is None : I1Ii1I = escape ( I1Ii1I )
   if 22 - 22: IiiI + i1iIi11iIIi1I . O0OOo + Iii1ii1II11i * o00 . Ii
   if I1Ii1I is None :
    ii111iI = iiIiII1 ( I1Ii1I , ii111iI )
   else :
    if 90 - 90: Oo0ooO0oo0oO * oOoO0oo0OOOo - i1iIi11iIIi1I + IiiI
    ii111iI = iiIiII1 ( I1Ii1I . encode ( "utf-8" ) , ii111iI )
    if 53 - 53: ii . ii + IiiI - o00 + Oo0ooO0oo0oO
 ii111iI += Oo0000o ( root ) if root else ""
 if 44 - 44: ooO00oOoo - Oo0oO0ooo
 return ii111iI
xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , 'movies' )
if 100 - 100: o0OO0 . i11ii11iIi11i - o00ooo0 + o0o00Oo0O * i11ii11iIi11i
try :
 xbmcplugin . addSortMethod ( int ( sys . argv [ 1 ] ) , xbmcplugin . SORT_METHOD_UNSORTED )
except :
 pass
try :
 xbmcplugin . addSortMethod ( int ( sys . argv [ 1 ] ) , xbmcplugin . SORT_METHOD_LABEL )
except :
 pass
try :
 xbmcplugin . addSortMethod ( int ( sys . argv [ 1 ] ) , xbmcplugin . SORT_METHOD_DATE )
except :
 pass
try :
 xbmcplugin . addSortMethod ( int ( sys . argv [ 1 ] ) , xbmcplugin . SORT_METHOD_GENRE )
except :
 pass
 if 59 - 59: ooO0OO000o
oOO = oOo0OOOOoO ( )
if 43 - 43: i1iIi11iIIi1I + ii
IiII = None
OO0Oooo0oOO0O = None
i11ii1I1 = None
oOOO00o000o = None
oOoo00o0oOO = None
o0o = I1IIIii
oOOO00o000o = None
i1I111iIii1i1 = None
i1II1i = None
if 80 - 80: ooO00oOoo / Ii + ii
try :
 IiII = urllib . unquote_plus ( oOO [ "url" ] ) . decode ( 'utf-8' )
except :
 pass
try :
 OO0Oooo0oOO0O = urllib . unquote_plus ( oOO [ "name" ] )
except :
 pass
try :
 oOoo00o0oOO = urllib . unquote_plus ( oOO [ "iconimage" ] )
except :
 pass
try :
 o0o = urllib . unquote_plus ( oOO [ "fanart" ] )
except :
 pass
try :
 i11ii1I1 = int ( oOO [ "mode" ] )
except :
 pass
try :
 oOOO00o000o = eval ( urllib . unquote_plus ( oOO [ "playlist" ] ) . replace ( '||' , ',' ) )
except :
 pass
try :
 i1I111iIii1i1 = int ( oOO [ "fav_mode" ] )
except :
 pass
try :
 i1II1i = oOO [ "regexs" ]
except :
 pass
III11i1iI11 = ''
try :
 III11i1iI11 = urllib . unquote_plus ( oOO [ "playitem" ] )
except :
 pass
 if 58 - 58: o0OO0
oO0ooO0OoOOOO ( "Mode: " + str ( i11ii1I1 ) )
if 98 - 98: IiiI * i11ii11iIi11i
if 10 - 10: o0OO0 - o00 % ooO0OO000o - ooO00oOoo - ii1I
if not IiII is None :
 oO0ooO0OoOOOO ( "URL: " + str ( IiII . encode ( 'utf-8' ) ) )
oO0ooO0OoOOOO ( "Name: " + str ( OO0Oooo0oOO0O ) )
if 10 - 10: Iii1ii1II11i - I1i1iI1i . ooO00oOoo
if not III11i1iI11 == '' :
 OOo00OO00Oo = Ooo00o0Oooo ( '' , data = III11i1iI11 )
 OO0Oooo0oOO0O , IiII , i1II1i = i1i1iI1iiiI ( OOo00OO00Oo , None , dontLink = True )
 i11ii1I1 = 117
if i11ii1I1 == None :
 oO0ooO0OoOOOO ( "getSources" )
 oO ( )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 8 - 8: iI11I1II1I1I % o0OO0 + i1iIi11iIIi1I
elif i11ii1I1 == 1 :
 oO0ooO0OoOOOO ( "getData" )
 I1I1IiI1 = None
 if 24 - 24: IiiI / o00ooo0 / o00ooo0 % ooO0OO000o - o0OO0 * o0OO0
 if i1II1i and len ( i1II1i ) > 0 :
  I1I1IiI1 , Iii = Ooooooo ( i1II1i , IiII )
  if 58 - 58: oOoO0oo0OOOo
  if 60 - 60: ooO0OO000o
  if I1I1IiI1 . startswith ( 'http' ) or I1I1IiI1 . startswith ( 'smb' ) or I1I1IiI1 . startswith ( 'nfs' ) or I1I1IiI1 . startswith ( '/' ) :
   IiII = I1I1IiI1
   I1I1IiI1 = None
   if 90 - 90: oOoO0oo0OOOo
   if 37 - 37: oOoO0oo0OOOo + o0o00Oo0O . o0o00Oo0O * i1iIi11iIIi1I % ooO00oOoo / o00
 OO ( IiII , o0o , I1I1IiI1 )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 18 - 18: ii
 if 57 - 57: O0OOo . oOoO0oo0OOOo * IiiI - ii
elif i11ii1I1 == 2 :
 oO0ooO0OoOOOO ( "getChannelItems" )
 OOoOoOo ( OO0Oooo0oOO0O , IiII , o0o )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 75 - 75: Ii / IiiI . Oo0oO0ooo . ii1I . ii1I / I1i1iI1i
elif i11ii1I1 == 3 :
 oO0ooO0OoOOOO ( "getSubChannelItems" )
 I1i1i1 ( OO0Oooo0oOO0O , IiII , o0o )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 94 - 94: O0OOo + I11i11Ii
elif i11ii1I1 == 4 :
 oO0ooO0OoOOOO ( "getFavorites" )
 oo0o00OO ( )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 56 - 56: oOoO0oo0OOOo % IiiI
elif i11ii1I1 == 5 :
 oO0ooO0OoOOOO ( "addFavorite" )
 try :
  OO0Oooo0oOO0O = OO0Oooo0oOO0O . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  OO0Oooo0oOO0O = OO0Oooo0oOO0O . split ( '  - ' ) [ 0 ]
 except :
  pass
 IioOooOOo00ooO ( OO0Oooo0oOO0O , IiII , oOoo00o0oOO , o0o , i1I111iIii1i1 )
 if 40 - 40: Oo0ooO0oo0oO / Oo0oO0ooo
elif i11ii1I1 == 6 :
 oO0ooO0OoOOOO ( "rmFavorite" )
 try :
  OO0Oooo0oOO0O = OO0Oooo0oOO0O . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  OO0Oooo0oOO0O = OO0Oooo0oOO0O . split ( '  - ' ) [ 0 ]
 except :
  pass
 OoO0O0oo0o ( OO0Oooo0oOO0O )
 if 29 - 29: o00ooo0 - o00ooo0 / O0OOo
elif i11ii1I1 == 7 :
 iI111iI ( )
 o000o0o00o0Oo ( )
 if 49 - 49: I1i1iI1i + o0OO0 % i11ii11iIi11i - i1iIi11iIIi1I - o0o00Oo0O - ii
elif i11ii1I1 == 8 :
 oO0ooO0OoOOOO ( "rmSource" )
 oOI1Ii1I1 ( OO0Oooo0oOO0O )
 if 4 - 4: ooO0OO000o - o0OO0 % i1iIi11iIIi1I * Ii
elif i11ii1I1 == 9 :
 oO0ooO0OoOOOO ( "download_file" )
 OoO00OooO0 ( OO0Oooo0oOO0O , IiII )
 if 18 - 18: i1iIi11iIIi1I % o0o00Oo0O
elif i11ii1I1 == 10 :
 oO0ooO0OoOOOO ( "getCommunitySources" )
 Oo0O0oooo ( )
 if 66 - 66: iI11I1II1I1I % Ii / I11i11Ii
elif i11ii1I1 == 11 :
 oO0ooO0OoOOOO ( "addSource" )
 I1iII1iIi1I ( IiII )
 if 47 - 47: Iii1ii1II11i * o0OO0 + iI11I1II1I1I - o0OO0 / Oo0oO0ooo
elif i11ii1I1 == 12 :
 oO0ooO0OoOOOO ( "setResolvedUrl" )
 if not IiII . startswith ( "plugin://plugin" ) or not any ( x in IiII for x in OOoO000O0OO ) :
  O0oo0oO00o = True
  if '$$LSDirect$$' in IiII :
   IiII = IiII . replace ( '$$LSDirect$$' , '' )
   O0oo0oO00o = False
  OOoOooOoOOOoo = xbmcgui . ListItem ( path = IiII )
  if not O0oo0oO00o :
   xbmc . Player ( ) . play ( IiII )
  else :
   xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , OOoOooOoOOOoo )
 else :
  if 86 - 86: Oo0oO0ooo
  xbmc . executebuiltin ( 'XBMC.RunPlugin(' + IiII + ')' )
  if 43 - 43: I11i11Ii / o00 / O0OOo + iI11I1II1I1I + ii
  if 33 - 33: ooO0OO000o - Oo0oO0ooo - O0OOo
elif i11ii1I1 == 13 :
 oO0ooO0OoOOOO ( "play_playlist" )
 O00Ooiii ( OO0Oooo0oOO0O , oOOO00o000o )
 if 92 - 92: i11ii11iIi11i * Oo0oO0ooo
elif i11ii1I1 == 14 :
 oO0ooO0OoOOOO ( "get_xml_database" )
 OOOoo0OO ( IiII )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 92 - 92: o0OO0
elif i11ii1I1 == 15 :
 oO0ooO0OoOOOO ( "browse_xml_database" )
 OOOoo0OO ( IiII , True )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 7 - 7: o00
elif i11ii1I1 == 16 :
 oO0ooO0OoOOOO ( "browse_community" )
 Oo0O0oooo ( IiII , browse = True )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 73 - 73: i11ii11iIi11i % Iii1ii1II11i
elif i11ii1I1 == 17 or i11ii1I1 == 117 :
 oO0ooO0OoOOOO ( "getRegexParsed" )
 if 32 - 32: Oo0ooO0oo0oO + o00 + iI11I1II1I1I * i1iIi11iIIi1I
 I1I1IiI1 = None
 if i1II1i and 'listrepeat' in urllib . unquote_plus ( i1II1i ) :
  oo00O0 , I1ii1Ii1ii11i , ii1iI , i1II1i , O0o0oo0oOO0oO = Ooooooo ( i1II1i , IiII )
  if 62 - 62: Ii
  III1I11i1iIi = ''
  if 2 - 2: I11i11Ii
  if 69 - 69: ii / i1iIi11iIIi1I * ooO00oOoo
  Oo0o0ooO0ooo = ii1iI [ 'name' ]
  i111IIiIII1i = i1II1i . pop ( Oo0o0ooO0ooo )
  if 74 - 74: ooO0OO000o / o0o00Oo0O
  IiII = ''
  import copy
  O0oo0ooo0 = ''
  iII1 = 0
  for ooO0oO0 in I1ii1Ii1ii11i :
   if 87 - 87: ii % ii / Oo0oO0ooo / o0OO0
   try :
    iII1 += 1
    Ii1iiIIi1i = copy . deepcopy ( i1II1i )
    if 44 - 44: IiiI
    ooO0O = oo00O0
    oooo0O0 = 0
    for oooo0O0 in range ( len ( ooO0oO0 ) ) :
     if 30 - 30: IiiI - i11ii11iIi11i + Oo0ooO0oo0oO
     if len ( Ii1iiIIi1i ) > 0 :
      for Oooo , iI1I in Ii1iiIIi1i . iteritems ( ) :
       if iI1I is not None :
        for Iii1IiI1iI1I , Iiii in iI1I . iteritems ( ) :
         if Iiii is not None :
          if 90 - 90: Ii
          if 48 - 48: ooO0OO000o / Oo0ooO0oo0oO . Oo0oO0ooo
          if 60 - 60: oOoO0oo0OOOo - iI11I1II1I1I / Iii1ii1II11i % o00 * ii - iI11I1II1I1I
          if 10 - 10: oOoO0oo0OOOo % I1i1iI1i
          if type ( Iiii ) is dict :
           for oOoO000 , Oo00o00Oo in Iiii . iteritems ( ) :
            if Oo00o00Oo is not None :
             oO0oO00oOo0OOO = None
             if isinstance ( ooO0oO0 , tuple ) :
              try :
               oO0oO00oOo0OOO = ooO0oO0 [ oooo0O0 ] . decode ( 'utf-8' )
              except :
               oO0oO00oOo0OOO = ooO0oO0 [ oooo0O0 ]
             else :
              try :
               oO0oO00oOo0OOO = ooO0oO0 . decode ( 'utf-8' )
              except :
               oO0oO00oOo0OOO = ooO0oO0
               if 50 - 50: O0OOo % i1iIi11iIIi1I
             if '[' + Oo0o0ooO0ooo + '.param' + str ( oooo0O0 + 1 ) + '][DE]' in Oo00o00Oo :
              Oo00o00Oo = Oo00o00Oo . replace ( '[' + Oo0o0ooO0ooo + '.param' + str ( oooo0O0 + 1 ) + '][DE]' , unescape ( oO0oO00oOo0OOO ) )
             Iiii [ oOoO000 ] = Oo00o00Oo . replace ( '[' + Oo0o0ooO0ooo + '.param' + str ( oooo0O0 + 1 ) + ']' , oO0oO00oOo0OOO )
             if 75 - 75: o0OO0 * O0OOo
             if 88 - 88: i11ii11iIi11i * IiiI * Oo0ooO0oo0oO / i1iIi11iIIi1I * i11ii11iIi11i
          else :
           oO0oO00oOo0OOO = None
           if isinstance ( ooO0oO0 , tuple ) :
            try :
             oO0oO00oOo0OOO = ooO0oO0 [ oooo0O0 ] . decode ( 'utf-8' )
            except :
             oO0oO00oOo0OOO = ooO0oO0 [ oooo0O0 ]
           else :
            try :
             oO0oO00oOo0OOO = ooO0oO0 . decode ( 'utf-8' )
            except :
             oO0oO00oOo0OOO = ooO0oO0
           if '[' + Oo0o0ooO0ooo + '.param' + str ( oooo0O0 + 1 ) + '][DE]' in Iiii :
            if 100 - 100: IiiI . I11i11Ii
            Iiii = Iiii . replace ( '[' + Oo0o0ooO0ooo + '.param' + str ( oooo0O0 + 1 ) + '][DE]' , unescape ( oO0oO00oOo0OOO ) )
            if 62 - 62: O0OOo + ooO0OO000o % O0OOo
           iI1I [ Iii1IiI1iI1I ] = Iiii . replace ( '[' + Oo0o0ooO0ooo + '.param' + str ( oooo0O0 + 1 ) + ']' , oO0oO00oOo0OOO )
           if 50 - 50: ii + o0OO0 * I11i11Ii - o00ooo0 / Ii
           if 5 - 5: o0o00Oo0O - I11i11Ii
     oO0oO00oOo0OOO = None
     if isinstance ( ooO0oO0 , tuple ) :
      try :
       oO0oO00oOo0OOO = ooO0oO0 [ oooo0O0 ] . decode ( 'utf-8' )
      except :
       oO0oO00oOo0OOO = ooO0oO0 [ oooo0O0 ]
     else :
      try :
       oO0oO00oOo0OOO = ooO0oO0 . decode ( 'utf-8' )
      except :
       oO0oO00oOo0OOO = ooO0oO0
     if '[' + Oo0o0ooO0ooo + '.param' + str ( oooo0O0 + 1 ) + '][DE]' in ooO0O :
      ooO0O = ooO0O . replace ( '[' + Oo0o0ooO0ooo + '.param' + str ( oooo0O0 + 1 ) + '][DE]' , oO0oO00oOo0OOO )
     ooO0O = ooO0O . replace ( '[' + Oo0o0ooO0ooo + '.param' + str ( oooo0O0 + 1 ) + ']' , escape ( oO0oO00oOo0OOO ) )
     if 44 - 44: ooO0OO000o . ooO0OO000o + Oo0ooO0oo0oO * o00ooo0
    ooO0O = ooO0O . replace ( '[' + Oo0o0ooO0ooo + '.param' + str ( 0 ) + ']' , str ( iII1 ) )
    if 16 - 16: ooO0OO000o
    try :
     if O0o0oo0oOO0oO and '[' + Oo0o0ooO0ooo + '.cookies]' in ooO0O :
      ooO0O = ooO0O . replace ( '[' + Oo0o0ooO0ooo + '.cookies]' , II1i1III ( O0o0oo0oOO0oO ) )
    except : pass
    if 100 - 100: o0o00Oo0O - ii1I
    if 48 - 48: o0OO0 % O0OOo + o0o00Oo0O
    if 27 - 27: Iii1ii1II11i / Oo0ooO0oo0oO
    if 33 - 33: ii % Iii1ii1II11i . o0o00Oo0O / Iii1ii1II11i
    O0OoOo = ''
    if 94 - 94: i11ii11iIi11i + i11ii11iIi11i + Iii1ii1II11i . i11ii11iIi11i * o00ooo0
    if len ( Ii1iiIIi1i ) > 0 :
     O0OoOo = O0ooo0ooOoo0o ( Ii1iiIIi1i , 'lsproroot' )
     O0OoOo = O0OoOo . split ( '<lsproroot>' ) [ 1 ] . split ( '</lsproroot' ) [ 0 ]
     if 62 - 62: IiiI / iI11I1II1I1I
     if 55 - 55: o00ooo0 / i11ii11iIi11i + o00 . Oo0oO0ooo
    try :
     O0oo0ooo0 += '\n<item>%s\n%s</item>' % ( ooO0O , O0OoOo )
    except : O0oo0ooo0 += '\n<item>%s\n%s</item>' % ( ooO0O . encode ( "utf-8" ) , O0OoOo )
   except : traceback . print_exc ( file = sys . stdout )
   if 47 - 47: o0o00Oo0O
   if 83 - 83: o0o00Oo0O + oOoO0oo0OOOo / o0o00Oo0O / I1i1iI1i
   if 68 - 68: ii1I . I1i1iI1i . ii1I + Oo0oO0ooo % I11i11Ii
   if 32 - 32: oOoO0oo0OOOo . iI11I1II1I1I % o0OO0 . o0o00Oo0O . oOoO0oo0OOOo / o00
   if 45 - 45: iI11I1II1I1I
  oO0ooO0OoOOOO ( repr ( O0oo0ooo0 ) )
  OO ( '' , '' , O0oo0ooo0 )
  xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 else :
  IiII , Iii = Ooooooo ( i1II1i , IiII )
  print repr ( IiII ) , Iii , 'imhere'
  if not ( i1II1i and 'notplayable' in i1II1i and not IiII ) :
   if IiII :
    if '$PLAYERPROXY$=' in IiII :
     IiII , II1I = IiII . split ( '$PLAYERPROXY$=' )
     print 'proxy' , II1I
     if 41 - 41: o00 % o00 - Oo0oO0ooo % i11ii11iIi11i - ii - o00
     oOOo00O0O0 = None
     iiIIiiI = None
     if len ( II1I ) > 0 and '@' in II1I :
      II1I = II1I . split ( ':' )
      oOOo00O0O0 = II1I [ 0 ]
      iiIIiiI = II1I [ 1 ] . split ( '@' ) [ 0 ]
      O0oo0O0OO0Oo = II1I [ 1 ] . split ( '@' ) [ 1 ]
      oO00o0oO0O = II1I [ 2 ]
     else :
      O0oo0O0OO0Oo , oO00o0oO0O = II1I . split ( ':' )
      if 38 - 38: Iii1ii1II11i - o00ooo0 * IiiI
     oOo0OooOo ( IiII , OO0Oooo0oOO0O , oOoo00o0oOO , O0oo0O0OO0Oo , oO00o0oO0O , oOOo00O0O0 , iiIIiiI )
    else :
     oOoOOOO0OOO ( IiII , OO0Oooo0oOO0O , oOoo00o0oOO , Iii , i1II1i )
   else :
    xbmc . executebuiltin ( "XBMC.Notification(tvchopo,Failed to extract regex. - " + "this" + ",4000," + IIiiiiiiIi1I1 + ")" )
elif i11ii1I1 == 18 :
 oO0ooO0OoOOOO ( "youtubedl" )
 try :
  import youtubedl
 except Exception :
  xbmc . executebuiltin ( "XBMC.Notification(tvchopo,Please [COLOR yellow]install Youtube-dl[/COLOR] module ,10000," ")" )
 o0ooooO0o0O = youtubedl . single_YD ( IiII )
 oOoOOOO0OOO ( o0ooooO0o0O , OO0Oooo0oOO0O , oOoo00o0oOO )
elif i11ii1I1 == 19 :
 oO0ooO0OoOOOO ( "Genesiscommonresolvers" )
 oOoOOOO0OOO ( O00OoooOoOo0o00o ( IiII ) , OO0Oooo0oOO0O , oOoo00o0oOO , True )
 if 13 - 13: I11i11Ii * o0OO0
elif i11ii1I1 == 21 :
 oO0ooO0OoOOOO ( "download current file using youtube-dl service" )
 I1IIIi1i ( '' , OO0Oooo0oOO0O , 'video' )
elif i11ii1I1 == 23 :
 oO0ooO0OoOOOO ( "get info then download" )
 I1IIIi1i ( IiII , OO0Oooo0oOO0O , 'video' )
elif i11ii1I1 == 24 :
 oO0ooO0OoOOOO ( "Audio only youtube download" )
 I1IIIi1i ( IiII , OO0Oooo0oOO0O , 'audio' )
elif i11ii1I1 == 25 :
 oO0ooO0OoOOOO ( "Searchin Other plugins" )
 OOOOIIIIiI11Ii1i ( IiII , OO0Oooo0oOO0O )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif i11ii1I1 == 55 :
 oO0ooO0OoOOOO ( "enabled lock" )
 OooOooO = o0OOOOO00o0O0 . getSetting ( 'parentalblockedpin' )
 Iii1I1I11iiI1 = xbmc . Keyboard ( '' , 'Enter Pin' )
 Iii1I1I11iiI1 . doModal ( )
 if not ( Iii1I1I11iiI1 . isConfirmed ( ) == False ) :
  I1I1i1I = Iii1I1I11iiI1 . getText ( )
  if I1I1i1I == OooOooO :
   o0OOOOO00o0O0 . setSetting ( 'parentalblocked' , "false" )
   xbmc . executebuiltin ( "XBMC.Notification(tvchopo,Parental Block Disabled,5000," + IIiiiiiiIi1I1 + ")" )
  else :
   xbmc . executebuiltin ( "XBMC.Notification(tvchopo,Wrong Pin??,5000," + IIiiiiiiIi1I1 + ")" )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif i11ii1I1 == 56 :
 oO0ooO0OoOOOO ( "disable lock" )
 o0OOOOO00o0O0 . setSetting ( 'parentalblocked' , "true" )
 xbmc . executebuiltin ( "XBMC.Notification(tvchopo,Parental block enabled,5000," + IIiiiiiiIi1I1 + ")" )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 41 - 41: Oo0oO0ooo
elif i11ii1I1 == 53 :
 oO0ooO0OoOOOO ( "Requesting JSON-RPC Items" )
 iiii11IiIiI ( IiII )
 if 16 - 16: iI11I1II1I1I
if not oo000 == None :
 print 'setting view mode'
 xbmc . executebuiltin ( "Container.SetViewMode(%s)" % oo000 )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3