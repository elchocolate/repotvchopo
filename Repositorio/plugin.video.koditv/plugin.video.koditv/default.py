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
ii = False
oOOo = False
O0 = [ '180upload.com' , 'allmyvideos.net' , 'bestreams.net' , 'clicknupload.com' , 'cloudzilla.to' , 'movshare.net' , 'novamov.com' , 'nowvideo.sx' , 'videoweed.es' , 'daclips.in' , 'datemule.com' , 'fastvideo.in' , 'faststream.in' , 'filehoot.com' , 'filenuke.com' , 'sharesix.com' , 'plus.google.com' , 'picasaweb.google.com' , 'gorillavid.com' , 'gorillavid.in' , 'grifthost.com' , 'hugefiles.net' , 'ipithos.to' , 'ishared.eu' , 'kingfiles.net' , 'mail.ru' , 'my.mail.ru' , 'videoapi.my.mail.ru' , 'mightyupload.com' , 'mooshare.biz' , 'movdivx.com' , 'movpod.net' , 'movpod.in' , 'movreel.com' , 'mrfile.me' , 'nosvideo.com' , 'openload.io' , 'played.to' , 'bitshare.com' , 'filefactory.com' , 'k2s.cc' , 'oboom.com' , 'rapidgator.net' , 'primeshare.tv' , 'bitshare.com' , 'filefactory.com' , 'k2s.cc' , 'oboom.com' , 'rapidgator.net' , 'sharerepo.com' , 'stagevu.com' , 'streamcloud.eu' , 'streamin.to' , 'thefile.me' , 'thevideo.me' , 'tusfiles.net' , 'uploadc.com' , 'zalaa.com' , 'uploadrocket.net' , 'uptobox.com' , 'v-vids.com' , 'veehd.com' , 'vidbull.com' , 'videomega.tv' , 'vidplay.net' , 'vidspot.net' , 'vidto.me' , 'vidzi.tv' , 'vimeo.com' , 'vk.com' , 'vodlocker.com' , 'xfileload.com' , 'xvidstage.com' , 'zettahost.tv' ]
o0O = [ 'plugin.video.dramasonline' , 'plugin.video.f4mTester' , 'plugin.video.shahidmbcnet' , 'plugin.video.SportsDevil' , 'plugin.stream.vaughnlive.tv' , 'plugin.video.ZemTV-shani' ]
if 10 - 10: O0O0OO0O0O0
class iiiii ( urllib2 . HTTPErrorProcessor ) :
 def http_response ( self , request , response ) :
  return response
 https_response = http_response
 if 64 - 64: iIIi1iI1II111 + ii11i / oOooOoO0Oo0O
iI1 = False ;
if iI1 :
 if 43 - 43: I11i11Ii
 if 65 - 65: i1iIi11iIIi1I
 try :
  import pysrc . pydevd as pydevd
  if 78 - 78: i11ii11iIi11i . oOoO0oo0OOOo + IiiI / Iii1ii1II11i
  pydevd . settrace ( 'localhost' , stdoutToServer = True , stderrToServer = True )
 except ImportError :
  sys . stderr . write ( "Error: " +
 "You must add org.python.pydev.debug.pysrc to your PYTHONPATH." )
  sys . exit ( 1 )
  if 10 - 10: I1iII1iiII + I1Ii111 / OOo
  if 41 - 41: I1II1
Ooo0OO0oOO = xbmcaddon . Addon ( 'plugin.video.koditv' )
oooO0oo0oOOOO = Ooo0OO0oOO . getAddonInfo ( 'version' )
O0oO = xbmc . translatePath ( Ooo0OO0oOO . getAddonInfo ( 'profile' ) . decode ( 'utf-8' ) )
o0oO0 = xbmc . translatePath ( Ooo0OO0oOO . getAddonInfo ( 'path' ) . decode ( 'utf-8' ) )
oo00 = os . path . join ( O0oO , 'favorites' )
o00 = os . path . join ( O0oO , 'history' )
Oo0oO0ooo = os . path . join ( O0oO , 'list_revision' )
o0oOoO00o = os . path . join ( o0oO0 , 'icon.png' )
i1 = os . path . join ( o0oO0 , 'fanart.jpg' )
oOOoo00O0O = os . path . join ( O0oO , 'source_file' )
i1111 = O0oO
i11 = os . path . join ( O0oO , 'LivewebTV' )
downloader = downloader . SimpleDownloader ( )
I11 = Ooo0OO0oOO . getSetting ( 'debug' )
Oo0o0000o0o0 = 'aHR0cDovLw=='
oOo0oooo00o = base64 . b64decode ( Oo0o0000o0o0 )
oO0o0o0ooO0oO = 'Yml0Lmx5Lw=='
oo0o0O00 = base64 . b64decode ( oO0o0o0ooO0oO )
oO = 'Mk1xcnZtTQ=='
i1iiIIiiI111 = base64 . b64decode ( oO )
oooOOOOO = 'JCRMU1Byb0VuY0tleT0gJCQ='
i1iiIII111ii = base64 . b64decode ( oooOOOOO )
i1iIIi1 = oOo0oooo00o + oo0o0O00 + i1iiIIiiI111 + i1iiIII111ii
if os . path . exists ( oo00 ) == True :
 ii11iIi1I = open ( oo00 ) . read ( )
else : ii11iIi1I = [ ]
if 6 - 6: I1I11I1I1I * OooO0OO
if 28 - 28: iIii1
oOOoO0 = [ { "url" : i1iIIi1 , "fanart" : "https://i.imgur.com/s7fUpI5.jpg" , "Genero" : "Tv En Vivo" , "Fecha" : "21.02.2018" , "Creditos" : "Alex" } ]
if 59 - 59: oOOO0OOooOoO0Oo * II + IIi - I11i11Ii + i11ii11iIi11i
if 77 - 77: iIii1 % iIIi1iI1II111 / O0O0OO0O0O0
def OO0O00 ( string ) :
 xbmc . log ( "" )
 if 20 - 20: oOooOoO0Oo0O
 if 13 - 13: I11i11Ii - OooO0OO % OOo / ii11i % iIii1
def oo ( url , headers = None ) :
 return O0o0Oo ;
 if 78 - 78: ii11i - OooO0OO * IiiI + I1iII1iiII + iIii1 + iIii1
 if 11 - 11: iIii1 - IiiI % IIi % iIii1 / Iii1ii1II11i - IiiI
def o0o0oOOOo0oo ( ) :
 try :
  if os . path . exists ( oo00 ) == True :
   ii11iIi1I = open ( oo00 ) . read ( )
   if ii11iIi1I == "[]" :
    os . remove ( oo00 )
   else :
    o0oo0o0O00OO ( '[COLOR yellow][B]- MIS CANALES FAVORITOS[/COLOR][/B]' , 'url' , 4 , os . path . join ( o0oO0 , 'resources' , 'favorite.png' ) , i1 , '' , '' , '' , '' )
    o0oo0o0O00OO ( '' , '' , 100 , '' , i1 , '' , '' , '' , '' )
    if 80 - 80: I11i11Ii
  oOOO0o0o = oOOoO0
  if len ( oOOO0o0o ) > 1 :
   for iiI1 in oOOO0o0o :
    try :
     if 19 - 19: I1I11I1I1I + IIi
     if isinstance ( iiI1 , list ) :
      o0oo0o0O00OO ( iiI1 [ 0 ] . encode ( 'utf-8' ) , iiI1 [ 1 ] . encode ( 'utf-8' ) , 1 , o0oOoO00o , i1 , '' , '' , '' , '' , 'source' )
     else :
      ooo = o0oOoO00o
      ii1I1i1I = i1
      OOoo0O0 = ''
      iiiIi1i1I = ''
      credits = ''
      oOO00oOO = ''
      if iiI1 . has_key ( 'thumbnail' ) :
       ooo = iiI1 [ 'thumbnail' ]
      if iiI1 . has_key ( 'fanart' ) :
       ii1I1i1I = iiI1 [ 'fanart' ]
      if iiI1 . has_key ( 'description' ) :
       OOoo0O0 = iiI1 [ 'description' ]
      if iiI1 . has_key ( 'date' ) :
       iiiIi1i1I = iiI1 [ 'date' ]
      if iiI1 . has_key ( 'genre' ) :
       oOO00oOO = iiI1 [ 'genre' ]
      if iiI1 . has_key ( 'credits' ) :
       credits = iiI1 [ 'credits' ]
      o0oo0o0O00OO ( iiI1 [ 'title' ] . encode ( 'utf-8' ) , iiI1 [ 'url' ] . encode ( 'utf-8' ) , 1 , ooo , ii1I1i1I , OOoo0O0 , oOO00oOO , iiiIi1i1I , credits , 'source' )
    except : traceback . print_exc ( )
  else :
   if len ( oOOO0o0o ) == 1 :
    if isinstance ( oOOO0o0o [ 0 ] , list ) :
     OoOo ( oOOO0o0o [ 0 ] [ 1 ] . encode ( 'utf-8' ) , i1 )
    else :
     OoOo ( oOOO0o0o [ 0 ] [ 'url' ] , oOOO0o0o [ 0 ] [ 'fanart' ] )
 except : traceback . print_exc ( )
 if 18 - 18: O0O0OO0O0O0
def Ii11I ( url = None ) :
 if url is None :
  if not Ooo0OO0oOO . getSetting ( "new_file_source" ) == "" :
   OOO0OOO00oo = Ooo0OO0oOO . getSetting ( 'new_file_source' ) . decode ( 'utf-8' )
  elif not Ooo0OO0oOO . getSetting ( "new_url_source" ) == "" :
   OOO0OOO00oo = Ooo0OO0oOO . getSetting ( 'new_url_source' ) . decode ( 'utf-8' )
 else :
  OOO0OOO00oo = url
 if OOO0OOO00oo == '' or OOO0OOO00oo is None :
  return
 OO0O00 ( 'Adding New Source: ' + OOO0OOO00oo . encode ( 'utf-8' ) )
 if 31 - 31: i1iIi11iIIi1I - I1II1 . II % Iii1ii1II11i - iIIi1iI1II111
 iii11 = None
 if 58 - 58: I1II1 * O0O0OO0O0O0 / Iii1ii1II11i % II - I1Ii111 / OOo
 O0o0Oo = ii11i1 ( OOO0OOO00oo )
 if 29 - 29: I1Ii111 % i11ii11iIi11i + IIi / I1iII1iiII + I1II1 * I1iII1iiII
 if isinstance ( O0o0Oo , BeautifulSOAP ) :
  if O0o0Oo . find ( 'channels_info' ) :
   iii11 = O0o0Oo . channels_info
  elif O0o0Oo . find ( 'items_info' ) :
   iii11 = O0o0Oo . items_info
 if iii11 :
  i1I1iI = { }
  i1I1iI [ 'url' ] = OOO0OOO00oo
  try : i1I1iI [ 'title' ] = iii11 . title . string
  except : pass
  try : i1I1iI [ 'thumbnail' ] = iii11 . thumbnail . string
  except : pass
  try : i1I1iI [ 'fanart' ] = iii11 . fanart . string
  except : pass
  try : i1I1iI [ 'genre' ] = iii11 . genre . string
  except : pass
  try : i1I1iI [ 'description' ] = iii11 . description . string
  except : pass
  try : i1I1iI [ 'date' ] = iii11 . date . string
  except : pass
  try : i1I1iI [ 'credits' ] = iii11 . credits . string
  except : pass
 else :
  if '/' in OOO0OOO00oo :
   oo0OooOOo0 = OOO0OOO00oo . split ( '/' ) [ - 1 ] . split ( '.' ) [ 0 ]
  if '\\' in OOO0OOO00oo :
   oo0OooOOo0 = OOO0OOO00oo . split ( '\\' ) [ - 1 ] . split ( '.' ) [ 0 ]
  if '%' in oo0OooOOo0 :
   oo0OooOOo0 = urllib . unquote_plus ( oo0OooOOo0 )
  o0OO00oO = xbmc . Keyboard ( oo0OooOOo0 , 'Displayed Name, Rename?' )
  o0OO00oO . doModal ( )
  if ( o0OO00oO . isConfirmed ( ) == False ) :
   return
  I11i1I1I = o0OO00oO . getText ( )
  if len ( I11i1I1I ) == 0 :
   return
  i1I1iI = { }
  i1I1iI [ 'title' ] = I11i1I1I
  i1I1iI [ 'url' ] = OOO0OOO00oo
  i1I1iI [ 'fanart' ] = ii1I1i1I
  if 83 - 83: I1Ii111 / IIi
 if os . path . exists ( oOOoo00O0O ) == False :
  iIIIIii1 = [ ]
  iIIIIii1 . append ( i1I1iI )
  oo000OO00Oo = open ( oOOoo00O0O , "w" )
  oo000OO00Oo . write ( json . dumps ( iIIIIii1 ) )
  oo000OO00Oo . close ( )
 else :
  oOOO0o0o = json . loads ( open ( oOOoo00O0O , "r" ) . read ( ) )
  oOOO0o0o . append ( i1I1iI )
  oo000OO00Oo = open ( oOOoo00O0O , "w" )
  oo000OO00Oo . write ( json . dumps ( oOOO0o0o ) )
  oo000OO00Oo . close ( )
 Ooo0OO0oOO . setSetting ( 'new_url_source' , "" )
 Ooo0OO0oOO . setSetting ( 'new_file_source' , "" )
 xbmc . executebuiltin ( "XBMC.Notification(probando,New source added.,5000," + o0oOoO00o + ")" )
 if not url is None :
  if 'xbmcplus.xb.funpic.de' in url :
   xbmc . executebuiltin ( "XBMC.Container.Update(%s?mode=14,replace)" % sys . argv [ 0 ] )
  elif 'community-links' in url :
   xbmc . executebuiltin ( "XBMC.Container.Update(%s?mode=10,replace)" % sys . argv [ 0 ] )
 else : Ooo0OO0oOO . openSettings ( )
 if 51 - 51: oOOO0OOooOoO0Oo * I1iII1iiII + I1I11I1I1I + IiiI
def o0O0O00 ( name ) :
 oOOO0o0o = json . loads ( open ( oOOoo00O0O , "r" ) . read ( ) )
 for o000o in range ( len ( oOOO0o0o ) ) :
  if isinstance ( oOOO0o0o [ o000o ] , list ) :
   if oOOO0o0o [ o000o ] [ 0 ] == name :
    del oOOO0o0o [ o000o ]
    oo000OO00Oo = open ( oOOoo00O0O , "w" )
    oo000OO00Oo . write ( json . dumps ( oOOO0o0o ) )
    oo000OO00Oo . close ( )
    break
  else :
   if oOOO0o0o [ o000o ] [ 'title' ] == name :
    del oOOO0o0o [ o000o ]
    oo000OO00Oo = open ( oOOoo00O0O , "w" )
    oo000OO00Oo . write ( json . dumps ( oOOO0o0o ) )
    oo000OO00Oo . close ( )
    break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 7 - 7: IIi * IiiI % OOo . oOOO0OOooOoO0Oo
def Ii1iIiII1ii1 ( url , browse = False ) :
 if url is None :
  url = 'http://xbmcplus.xb.funpic.de/www-data/filesystem/'
 ooOooo000oOO = BeautifulSoup ( oo ( url ) , convertEntities = BeautifulSoup . HTML_ENTITIES )
 for iiI1 in ooOooo000oOO ( 'a' ) :
  Oo0oOOo = iiI1 [ 'href' ]
  if not Oo0oOOo . startswith ( '?' ) :
   Oo0OoO00oOO0o = iiI1 . string
   if Oo0OoO00oOO0o not in [ 'Parent Directory' , 'recycle_bin/' ] :
    if Oo0oOOo . endswith ( '/' ) :
     if browse :
      o0oo0o0O00OO ( Oo0OoO00oOO0o , url + Oo0oOOo , 15 , o0oOoO00o , ii1I1i1I , '' , '' , '' )
     else :
      o0oo0o0O00OO ( Oo0OoO00oOO0o , url + Oo0oOOo , 14 , o0oOoO00o , ii1I1i1I , '' , '' , '' )
    elif Oo0oOOo . endswith ( '.xml' ) :
     if browse :
      o0oo0o0O00OO ( Oo0OoO00oOO0o , url + Oo0oOOo , 1 , o0oOoO00o , ii1I1i1I , '' , '' , '' , '' , 'download' )
     else :
      if os . path . exists ( oOOoo00O0O ) == True :
       if Oo0OoO00oOO0o in oOOoO0 :
        o0oo0o0O00OO ( Oo0OoO00oOO0o + ' (in use)' , url + Oo0oOOo , 11 , o0oOoO00o , ii1I1i1I , '' , '' , '' , '' , 'download' )
       else :
        o0oo0o0O00OO ( Oo0OoO00oOO0o , url + Oo0oOOo , 11 , o0oOoO00o , ii1I1i1I , '' , '' , '' , '' , 'download' )
      else :
       o0oo0o0O00OO ( Oo0OoO00oOO0o , url + Oo0oOOo , 11 , o0oOoO00o , ii1I1i1I , '' , '' , '' , '' , 'download' )
       if 80 - 80: OOo + I1II1 - I1II1 % iIii1
       if 63 - 63: i11ii11iIi11i - I1Ii111 + iIIi1iI1II111 % I1I11I1I1I / ii11i / I1iII1iiII
def O0o0O00Oo0o0 ( browse = False ) :
 O00O0oOO00O00 = 'http://community-links.googlecode.com/svn/trunk/'
 ooOooo000oOO = BeautifulSoup ( oo ( O00O0oOO00O00 ) , convertEntities = BeautifulSoup . HTML_ENTITIES )
 i1Oo00 = ooOooo000oOO ( 'ul' ) [ 0 ] ( 'li' ) [ 1 : ]
 for iiI1 in i1Oo00 :
  Oo0OoO00oOO0o = iiI1 ( 'a' ) [ 0 ] [ 'href' ]
  if browse :
   o0oo0o0O00OO ( Oo0OoO00oOO0o , O00O0oOO00O00 + Oo0OoO00oOO0o , 1 , o0oOoO00o , ii1I1i1I , '' , '' , '' , '' , 'download' )
  else :
   o0oo0o0O00OO ( Oo0OoO00oOO0o , O00O0oOO00O00 + Oo0OoO00oOO0o , 11 , o0oOoO00o , ii1I1i1I , '' , '' , '' , '' , 'download' )
   if 31 - 31: II . Iii1ii1II11i / iIIi1iI1II111
def ii11i1 ( url , data = None ) :
 global oo000 , ii , oOOo
 ii = False
 oOOo = False
 if url . startswith ( 'http://' ) or url . startswith ( 'https://' ) :
  o000O0o = False
  if '$$TSDOWNLOADER$$' in url :
   ii = True
   url = url . replace ( "$$TSDOWNLOADER$$" , "" )
  if '$$HLSRETRY$$' in url :
   oOOo = True
   url = url . replace ( "$$HLSRETRY$$" , "" )
  if '$$LSProEncKey=' in url :
   o000O0o = url . split ( '$$LSProEncKey=' ) [ 1 ] . split ( '$$' ) [ 0 ]
   iI1iII1 = '$$LSProEncKey=%s$$' % o000O0o
   url = url . replace ( iI1iII1 , "" )
   if 86 - 86: I1II1
  data = oo ( url )
  if o000O0o :
   import pyaes
   o000O0o = o000O0o . encode ( "ascii" )
   print o000O0o
   OOoo0O = 16 - len ( o000O0o )
   o000O0o = o000O0o + ( chr ( 0 ) * ( OOoo0O ) )
   print repr ( o000O0o )
   data = base64 . b64decode ( data )
   Oo0ooOo0o = pyaes . new ( o000O0o , pyaes . MODE_ECB , IV = None )
   data = Oo0ooOo0o . decrypt ( data ) . split ( '\0' ) [ 0 ]
   if 22 - 22: ii11i / O0O0OO0O0O0 * ii11i * i1iIi11iIIi1I . I1II1 / O0O0OO0O0O0
  if re . search ( "#EXTM3U" , data ) or 'm3u' in url :
   if 2 - 2: i11ii11iIi11i / iIIi1iI1II111 / I1iII1iiII % Iii1ii1II11i % OooO0OO
   return data
 elif data == None :
  if not '/' in url or not '\\' in url :
   if 52 - 52: I1iII1iiII
   url = os . path . join ( i11 , url )
  if xbmcvfs . exists ( url ) :
   if url . startswith ( "smb://" ) or url . startswith ( "nfs://" ) :
    o0OO0oOO0O0 = xbmcvfs . copy ( url , os . path . join ( O0oO , 'temp' , 'sorce_temp.txt' ) )
    if o0OO0oOO0O0 :
     data = open ( os . path . join ( O0oO , 'temp' , 'sorce_temp.txt' ) , "r" ) . read ( )
     xbmcvfs . delete ( os . path . join ( O0oO , 'temp' , 'sorce_temp.txt' ) )
    else :
     OO0O00 ( "failed to copy from smb:" )
   else :
    data = open ( url , 'r' ) . read ( )
    if re . match ( "#EXTM3U" , data ) or 'm3u' in url :
     if 8 - 8: OOo
     return data
  else :
   OO0O00 ( "Soup Data not found!" )
   return
 if '<SetViewMode>' in data :
  try :
   oo000 = re . findall ( '<SetViewMode>(.*?)<' , data ) [ 0 ]
   xbmc . executebuiltin ( "Container.SetViewMode(%s)" % oo000 )
   print 'done setview' , oo000
  except : pass
 return BeautifulSOAP ( data , convertEntities = BeautifulStoneSoup . XML_ENTITIES )
 if 7 - 7: I1iII1iiII - i11ii11iIi11i
def OOo00O0 ( data ) :
 try :
  if data and len ( data ) > 0 and data . startswith ( '$pyFunction:' ) :
   data = ooOOOoO ( data . split ( '$pyFunction:' ) [ 1 ] , '' , None , None )
 except : pass
 if 67 - 67: II . iIii1 . iIIi1iI1II111
 return data
 if 10 - 10: I1Ii111 % I1Ii111 - ii11i / I1II1 + OooO0OO
def OoOo ( url , fanart , data = None ) :
 import checkbad
 checkbad . do_block_check ( False )
 ooOooo000oOO = ii11i1 ( url , data )
 if 87 - 87: OOo * I1Ii111 + I1II1 / ii11i / iIii1
 if isinstance ( ooOooo000oOO , BeautifulSOAP ) :
  if 37 - 37: iIii1 - IIi * OOo % O0O0OO0O0O0 - II
  if len ( ooOooo000oOO ( 'channels' ) ) > 0 and Ooo0OO0oOO . getSetting ( 'donotshowbychannels' ) == 'false' :
   o0oO = ooOooo000oOO ( 'channel' )
   for IIiIi1iI in o0oO :
    if 35 - 35: OooO0OO % iIIi1iI1II111 - iIIi1iI1II111
    if 16 - 16: i1iIi11iIIi1I % Iii1ii1II11i - i1iIi11iIIi1I + OooO0OO
    i1I1i = ''
    Ii = 0
    try :
     i1I1i = IIiIi1iI ( 'externallink' ) [ 0 ] . string
     Ii = len ( IIiIi1iI ( 'externallink' ) )
    except : pass
    if 22 - 22: i1iIi11iIIi1I
    if Ii > 1 : i1I1i = ''
    if 33 - 33: I1I11I1I1I
    Oo0OoO00oOO0o = IIiIi1iI ( 'name' ) [ 0 ] . string
    try :
     Oo0OoO00oOO0o = OOo00O0 ( Oo0OoO00oOO0o )
    except : pass
    iI11i1ii11 = IIiIi1iI ( 'thumbnail' ) [ 0 ] . string
    if iI11i1ii11 == None :
     iI11i1ii11 = ''
    iI11i1ii11 = OOo00O0 ( iI11i1ii11 )
    try :
     if not IIiIi1iI ( 'fanart' ) :
      if Ooo0OO0oOO . getSetting ( 'use_thumb' ) == "true" :
       OOooo0O00o = iI11i1ii11
      else :
       OOooo0O00o = fanart
     else :
      OOooo0O00o = IIiIi1iI ( 'fanart' ) [ 0 ] . string
     if OOooo0O00o == None :
      raise
    except :
     OOooo0O00o = fanart
     if 85 - 85: I1iII1iiII - oOoO0oo0OOOo
    try :
     OOoo0O0 = IIiIi1iI ( 'info' ) [ 0 ] . string
     if OOoo0O0 == None :
      raise
    except :
     OOoo0O0 = ''
     if 32 - 32: oOooOoO0Oo0O / ii11i - I1iII1iiII
    try :
     oOO00oOO = IIiIi1iI ( 'genre' ) [ 0 ] . string
     if oOO00oOO == None :
      raise
    except :
     oOO00oOO = ''
     if 91 - 91: iIii1 % I11i11Ii % ii11i
    try :
     iiiIi1i1I = IIiIi1iI ( 'date' ) [ 0 ] . string
     if iiiIi1i1I == None :
      raise
    except :
     iiiIi1i1I = ''
     if 20 - 20: I1II1 % OooO0OO / OooO0OO + OooO0OO
    try :
     credits = IIiIi1iI ( 'credits' ) [ 0 ] . string
     if credits == None :
      raise
    except :
     credits = ''
     if 45 - 45: OOo - oOOO0OOooOoO0Oo - oOooOoO0Oo0O - IiiI . i1iIi11iIIi1I / iIIi1iI1II111
    try :
     if i1I1i == '' :
      o0oo0o0O00OO ( Oo0OoO00oOO0o . encode ( 'utf-8' , 'ignore' ) , url . encode ( 'utf-8' ) , 2 , iI11i1ii11 , OOooo0O00o , OOoo0O0 , oOO00oOO , iiiIi1i1I , credits , True )
     else :
      if 51 - 51: iIIi1iI1II111 + iIii1
      o0oo0o0O00OO ( Oo0OoO00oOO0o . encode ( 'utf-8' ) , i1I1i . encode ( 'utf-8' ) , 1 , iI11i1ii11 , OOooo0O00o , OOoo0O0 , oOO00oOO , iiiIi1i1I , None , 'source' )
    except :
     OO0O00 ( 'There was a problem adding directory from getData(): ' + Oo0OoO00oOO0o . encode ( 'utf-8' , 'ignore' ) )
  else :
   OO0O00 ( 'No Channels: getItems' )
   IIIII11I1IiI ( ooOooo000oOO ( 'item' ) , fanart )
 else :
  i1I ( ooOooo000oOO )
  if 72 - 72: I11i11Ii / IiiI + oOooOoO0Oo0O - oOoO0oo0OOOo
  if 29 - 29: I1Ii111 + OOo % iIIi1iI1II111
def i1I ( data ) :
 I1I11 = data . rstrip ( )
 II1 = re . compile ( r'#EXTINF:(.+?),(.*?)[\n\r]+([^\r\n]+)' ) . findall ( I1I11 )
 o0oO00000 = len ( II1 )
 print 'tsdownloader' , ii
 if 69 - 69: IiiI - oOoO0oo0OOOo + I11i11Ii / II
 for ii1 , I1iI1iIi111i , iiIi1IIi1I in II1 :
  if 84 - 84: IIi * i1iIi11iIIi1I + oOoO0oo0OOOo
  if 'tvg-logo' in ii1 :
   iI11i1ii11 = O0ooO0Oo00o ( ii1 , 'tvg-logo=[\'"](.*?)[\'"]' )
   if iI11i1ii11 :
    if iI11i1ii11 . startswith ( 'http' ) :
     iI11i1ii11 = iI11i1ii11
     if 77 - 77: ii11i * IiiI
    elif not Ooo0OO0oOO . getSetting ( 'logo-folderPath' ) == "" :
     oOooOo0 = Ooo0OO0oOO . getSetting ( 'logo-folderPath' )
     iI11i1ii11 = oOooOo0 + iI11i1ii11
     if 38 - 38: II
    else :
     iI11i1ii11 = iI11i1ii11
     if 84 - 84: ii11i % iIii1 / ii11i % I1I11I1I1I
     if 45 - 45: iIIi1iI1II111
  else :
   iI11i1ii11 = ''
   if 26 - 26: I1I11I1I1I - ii11i - i11ii11iIi11i / IiiI . Iii1ii1II11i % ii11i
  if 'type' in ii1 :
   OO = O0ooO0Oo00o ( ii1 , 'type=[\'"](.*?)[\'"]' )
   if OO == 'yt-dl' :
    iiIi1IIi1I = iiIi1IIi1I + "&mode=18"
   elif OO == 'regex' :
    O00O0oOO00O00 = iiIi1IIi1I . split ( '&regexs=' )
    if 25 - 25: IiiI
    oOo0oO = OOOO0oo0 ( ii11i1 ( '' , data = O00O0oOO00O00 [ 1 ] ) )
    if 35 - 35: OooO0OO - i11ii11iIi11i % I1iII1iiII . oOooOoO0Oo0O % OooO0OO
    I1i1Iiiii ( O00O0oOO00O00 [ 0 ] , I1iI1iIi111i , iI11i1ii11 , '' , '' , '' , '' , '' , None , oOo0oO , o0oO00000 )
    continue
   elif OO == 'ftv' :
    iiIi1IIi1I = 'plugin://plugin.video.F.T.V/?name=' + urllib . quote ( I1iI1iIi111i ) + '&url=' + iiIi1IIi1I + '&mode=125&ch_fanart=na'
  elif ii and '.ts' in iiIi1IIi1I :
   iiIi1IIi1I = 'plugin://plugin.video.f4mTester/?url=' + urllib . quote_plus ( iiIi1IIi1I ) + '&amp;streamtype=TSDOWNLOADER&name=' + urllib . quote ( I1iI1iIi111i )
  elif oOOo and '.m3u8' in iiIi1IIi1I :
   iiIi1IIi1I = 'plugin://plugin.video.f4mTester/?url=' + urllib . quote_plus ( iiIi1IIi1I ) + '&amp;streamtype=HLSRETRY&name=' + urllib . quote ( I1iI1iIi111i )
  I1i1Iiiii ( iiIi1IIi1I , I1iI1iIi111i , iI11i1ii11 , '' , '' , '' , '' , '' , None , '' , o0oO00000 )
def OOo0oO00ooO00 ( name , url , fanart ) :
 ooOooo000oOO = ii11i1 ( url )
 oOO0O00oO0Ooo = ooOooo000oOO . find ( 'channel' , attrs = { 'name' : name . decode ( 'utf-8' ) } )
 oO0Oo0O0o = oOO0O00oO0Ooo ( 'item' )
 try :
  OOooo0O00o = oOO0O00oO0Ooo ( 'fanart' ) [ 0 ] . string
  if OOooo0O00o == None :
   raise
 except :
  OOooo0O00o = fanart
 for IIiIi1iI in oOO0O00oO0Ooo ( 'subchannel' ) :
  name = IIiIi1iI ( 'name' ) [ 0 ] . string
  try :
   name = OOo00O0 ( name )
  except : pass
  try :
   iI11i1ii11 = IIiIi1iI ( 'thumbnail' ) [ 0 ] . string
   if iI11i1ii11 == None :
    raise
   iI11i1ii11 = OOo00O0 ( iI11i1ii11 )
  except :
   iI11i1ii11 = ''
  try :
   if not IIiIi1iI ( 'fanart' ) :
    if Ooo0OO0oOO . getSetting ( 'use_thumb' ) == "true" :
     OOooo0O00o = iI11i1ii11
   else :
    OOooo0O00o = IIiIi1iI ( 'fanart' ) [ 0 ] . string
   if OOooo0O00o == None :
    raise
  except :
   pass
  try :
   OOoo0O0 = IIiIi1iI ( 'info' ) [ 0 ] . string
   if OOoo0O0 == None :
    raise
  except :
   OOoo0O0 = ''
   if 99 - 99: OOo . iIii1 + IIi % OOo . O0O0OO0O0O0 % iIIi1iI1II111
  try :
   oOO00oOO = IIiIi1iI ( 'genre' ) [ 0 ] . string
   if oOO00oOO == None :
    raise
  except :
   oOO00oOO = ''
   if 78 - 78: I1Ii111 + I1II1 - II
  try :
   iiiIi1i1I = IIiIi1iI ( 'date' ) [ 0 ] . string
   if iiiIi1i1I == None :
    raise
  except :
   iiiIi1i1I = ''
   if 38 - 38: I1iII1iiII - OOo + ii11i / Iii1ii1II11i % oOoO0oo0OOOo
  try :
   credits = IIiIi1iI ( 'credits' ) [ 0 ] . string
   if credits == None :
    raise
  except :
   credits = ''
   if 57 - 57: IiiI / IIi
  try :
   o0oo0o0O00OO ( name . encode ( 'utf-8' , 'ignore' ) , url . encode ( 'utf-8' ) , 3 , iI11i1ii11 , OOooo0O00o , OOoo0O0 , oOO00oOO , credits , iiiIi1i1I )
  except :
   OO0O00 ( 'There was a problem adding directory - ' + name . encode ( 'utf-8' , 'ignore' ) )
 IIIII11I1IiI ( oO0Oo0O0o , OOooo0O00o )
 if 29 - 29: ii11i + Iii1ii1II11i * IiiI * I1II1 . i11ii11iIi11i * i11ii11iIi11i
 if 7 - 7: oOOO0OOooOoO0Oo * II % OooO0OO - I1iII1iiII
def i1i ( name , url , fanart ) :
 ooOooo000oOO = ii11i1 ( url )
 oOO0O00oO0Ooo = ooOooo000oOO . find ( 'subchannel' , attrs = { 'name' : name . decode ( 'utf-8' ) } )
 oO0Oo0O0o = oOO0O00oO0Ooo ( 'subitem' )
 IIIII11I1IiI ( oO0Oo0O0o , fanart )
 if 56 - 56: I1Ii111 % iIIi1iI1II111 - i11ii11iIi11i
def IIIII11I1IiI ( items , fanart , dontLink = False ) :
 o0oO00000 = len ( items )
 OO0O00 ( 'Total Items: %s' % o0oO00000 )
 O00o0OO0 = Ooo0OO0oOO . getSetting ( 'add_playlist' )
 IIi1I1iiiii = Ooo0OO0oOO . getSetting ( 'ask_playlist_items' )
 o00oOOooOOo0o = Ooo0OO0oOO . getSetting ( 'use_thumb' )
 O0O0ooOOO = Ooo0OO0oOO . getSetting ( 'parentalblocked' )
 O0O0ooOOO = O0O0ooOOO == "true"
 for oOOo0O00o in items :
  iIiIi11 = False
  OOO = False
  if 32 - 32: I11i11Ii / i1iIi11iIIi1I . oOoO0oo0OOOo
  oooOo0OOOoo0 = 'false'
  try :
   oooOo0OOOoo0 = oOOo0O00o ( 'parentalblock' ) [ 0 ] . string
  except :
   OO0O00 ( 'parentalblock Error' )
   oooOo0OOOoo0 = ''
  if oooOo0OOOoo0 == 'true' and O0O0ooOOO : continue
  if 51 - 51: oOoO0oo0OOOo / Iii1ii1II11i . I1II1 * I1iII1iiII + IiiI * oOOO0OOooOoO0Oo
  try :
   Oo0OoO00oOO0o = oOOo0O00o ( 'title' ) [ 0 ] . string
   if Oo0OoO00oOO0o is None :
    Oo0OoO00oOO0o = 'unknown?'
   try :
    Oo0OoO00oOO0o = OOo00O0 ( Oo0OoO00oOO0o )
   except : pass
   if 73 - 73: IiiI + oOooOoO0Oo0O - iIIi1iI1II111 - OooO0OO - i1iIi11iIIi1I
  except :
   OO0O00 ( 'Name Error' )
   Oo0OoO00oOO0o = ''
   if 99 - 99: IIi . OooO0OO + II + oOooOoO0Oo0O % I1iII1iiII
   if 51 - 51: ii11i
  try :
   if oOOo0O00o ( 'epg' ) :
    if oOOo0O00o . epg_url :
     OO0O00 ( 'Get EPG Regex' )
     iIIiIi1 = oOOo0O00o . epg_url . string
     o0O0o0 = oOOo0O00o . epg_regex . string
     II111iI111I1I = I1i1i1iii ( iIIiIi1 , o0O0o0 )
     if II111iI111I1I :
      Oo0OoO00oOO0o += ' - ' + II111iI111I1I
    elif oOOo0O00o ( 'epg' ) [ 0 ] . string > 1 :
     Oo0OoO00oOO0o += I1111i ( oOOo0O00o ( 'epg' ) [ 0 ] . string )
   else :
    pass
  except :
   OO0O00 ( 'EPG Error' )
  try :
   O00O0oOO00O00 = [ ]
   if len ( oOOo0O00o ( 'link' ) ) > 0 :
    if 14 - 14: I1II1 / I1iII1iiII
    if 32 - 32: i11ii11iIi11i * oOoO0oo0OOOo
    for iiI1 in oOOo0O00o ( 'link' ) :
     if not iiI1 . string == None :
      O00O0oOO00O00 . append ( iiI1 . string )
      if 78 - 78: I1II1 - oOooOoO0Oo0O - I1Ii111 / IIi / i1iIi11iIIi1I
   elif len ( oOOo0O00o ( 'sportsdevil' ) ) > 0 :
    for iiI1 in oOOo0O00o ( 'sportsdevil' ) :
     if not iiI1 . string == None :
      iiI11ii1I1 = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + iiI1 . string
      Ooo0OOoOoO0 = oOOo0O00o ( 'referer' ) [ 0 ] . string
      if Ooo0OOoOoO0 :
       if 70 - 70: OOo
       iiI11ii1I1 = iiI11ii1I1 + '%26referer=' + Ooo0OOoOoO0
      O00O0oOO00O00 . append ( iiI11ii1I1 )
   elif len ( oOOo0O00o ( 'p2p' ) ) > 0 :
    for iiI1 in oOOo0O00o ( 'p2p' ) :
     if not iiI1 . string == None :
      if 'sop://' in iiI1 . string :
       oOOoO0o0oO = 'plugin://plugin.video.p2p-streams/?mode=2url=' + iiI1 . string + '&' + 'name=' + Oo0OoO00oOO0o
       O00O0oOO00O00 . append ( oOOoO0o0oO )
      else :
       o0Oo0oO0oOO00 = 'plugin://plugin.video.p2p-streams/?mode=1&url=' + iiI1 . string + '&' + 'name=' + Oo0OoO00oOO0o
       O00O0oOO00O00 . append ( o0Oo0oO0oOO00 )
   elif len ( oOOo0O00o ( 'vaughn' ) ) > 0 :
    for iiI1 in oOOo0O00o ( 'vaughn' ) :
     if not iiI1 . string == None :
      oo00OO0000oO = 'plugin://plugin.stream.vaughnlive.tv/?mode=PlayLiveStream&amp;channel=' + iiI1 . string
      O00O0oOO00O00 . append ( oo00OO0000oO )
   elif len ( oOOo0O00o ( 'ilive' ) ) > 0 :
    for iiI1 in oOOo0O00o ( 'ilive' ) :
     if not iiI1 . string == None :
      if not 'http' in iiI1 . string :
       I1II1oooO = 'plugin://plugin.video.tbh.ilive/?url=http://www.streamlive.to/view/' + iiI1 . string + '&amp;link=99&amp;mode=iLivePlay'
      else :
       I1II1oooO = 'plugin://plugin.video.tbh.ilive/?url=' + iiI1 . string + '&amp;link=99&amp;mode=iLivePlay'
   elif len ( oOOo0O00o ( 'yt-dl' ) ) > 0 :
    for iiI1 in oOOo0O00o ( 'yt-dl' ) :
     if not iiI1 . string == None :
      i1I1i111Ii = iiI1 . string + '&mode=18'
      O00O0oOO00O00 . append ( i1I1i111Ii )
   elif len ( oOOo0O00o ( 'dm' ) ) > 0 :
    for iiI1 in oOOo0O00o ( 'dm' ) :
     if not iiI1 . string == None :
      oooi1i1iI1iiiI = "plugin://plugin.video.dailymotion_com/?mode=playVideo&url=" + iiI1 . string
      O00O0oOO00O00 . append ( oooi1i1iI1iiiI )
   elif len ( oOOo0O00o ( 'dmlive' ) ) > 0 :
    for iiI1 in oOOo0O00o ( 'dmlive' ) :
     if not iiI1 . string == None :
      oooi1i1iI1iiiI = "plugin://plugin.video.dailymotion_com/?mode=playLiveVideo&url=" + iiI1 . string
      O00O0oOO00O00 . append ( oooi1i1iI1iiiI )
   elif len ( oOOo0O00o ( 'utube' ) ) > 0 :
    for iiI1 in oOOo0O00o ( 'utube' ) :
     if not iiI1 . string == None :
      if ' ' in iiI1 . string :
       Ooo0oOooo0 = 'plugin://plugin.video.youtube/search/?q=' + urllib . quote_plus ( iiI1 . string )
       OOO = Ooo0oOooo0
      elif len ( iiI1 . string ) == 11 :
       Ooo0oOooo0 = 'plugin://plugin.video.youtube/play/?video_id=' + iiI1 . string
      elif ( iiI1 . string . startswith ( 'PL' ) and not '&order=' in iiI1 . string ) or iiI1 . string . startswith ( 'UU' ) :
       Ooo0oOooo0 = 'plugin://plugin.video.youtube/play/?&order=default&playlist_id=' + iiI1 . string
      elif iiI1 . string . startswith ( 'PL' ) or iiI1 . string . startswith ( 'UU' ) :
       Ooo0oOooo0 = 'plugin://plugin.video.youtube/play/?playlist_id=' + iiI1 . string
      elif iiI1 . string . startswith ( 'UC' ) and len ( iiI1 . string ) > 12 :
       Ooo0oOooo0 = 'plugin://plugin.video.youtube/channel/' + iiI1 . string + '/'
       OOO = Ooo0oOooo0
      elif not iiI1 . string . startswith ( 'UC' ) and not ( iiI1 . string . startswith ( 'PL' ) ) :
       Ooo0oOooo0 = 'plugin://plugin.video.youtube/user/' + iiI1 . string + '/'
       OOO = Ooo0oOooo0
     O00O0oOO00O00 . append ( Ooo0oOooo0 )
   elif len ( oOOo0O00o ( 'imdb' ) ) > 0 :
    for iiI1 in oOOo0O00o ( 'imdb' ) :
     if not iiI1 . string == None :
      if Ooo0OO0oOO . getSetting ( 'genesisorpulsar' ) == '0' :
       oOOOoo00 = 'plugin://plugin.video.genesis/?action=play&imdb=' + iiI1 . string
      else :
       oOOOoo00 = 'plugin://plugin.video.pulsar/movie/tt' + iiI1 . string + '/play'
      O00O0oOO00O00 . append ( oOOOoo00 )
   elif len ( oOOo0O00o ( 'f4m' ) ) > 0 :
    for iiI1 in oOOo0O00o ( 'f4m' ) :
     if not iiI1 . string == None :
      if '.f4m' in iiI1 . string :
       iiIiIIIiiI = 'plugin://plugin.video.f4mTester/?url=' + urllib . quote_plus ( iiI1 . string )
      elif '.m3u8' in iiI1 . string :
       iiIiIIIiiI = 'plugin://plugin.video.f4mTester/?url=' + urllib . quote_plus ( iiI1 . string ) + '&amp;streamtype=HLS'
       if 12 - 12: iIIi1iI1II111 - I1iII1iiII
      else :
       iiIiIIIiiI = 'plugin://plugin.video.f4mTester/?url=' + urllib . quote_plus ( iiI1 . string ) + '&amp;streamtype=SIMPLE'
     O00O0oOO00O00 . append ( iiIiIIIiiI )
   elif len ( oOOo0O00o ( 'ftv' ) ) > 0 :
    for iiI1 in oOOo0O00o ( 'ftv' ) :
     if not iiI1 . string == None :
      oOoO00O0 = 'plugin://plugin.video.F.T.V/?name=' + urllib . quote ( Oo0OoO00oOO0o ) + '&url=' + iiI1 . string + '&mode=125&ch_fanart=na'
     O00O0oOO00O00 . append ( oOoO00O0 )
   elif len ( oOOo0O00o ( 'urlsolve' ) ) > 0 :
    if 75 - 75: i11ii11iIi11i . IIi . iIIi1iI1II111 * II
    for iiI1 in oOOo0O00o ( 'urlsolve' ) :
     if not iiI1 . string == None :
      i11II1I11I1 = iiI1 . string + '&mode=19'
      O00O0oOO00O00 . append ( i11II1I11I1 )
   if len ( O00O0oOO00O00 ) < 1 :
    raise
  except :
   OO0O00 ( 'Error <link> element, Passing:' + Oo0OoO00oOO0o . encode ( 'utf-8' , 'ignore' ) )
   continue
  try :
   iIiIi11 = oOOo0O00o ( 'externallink' ) [ 0 ] . string
  except : pass
  if 67 - 67: i11ii11iIi11i - I1iII1iiII / I1I11I1I1I - I11i11Ii
  if iIiIi11 :
   i1II1 = [ iIiIi11 ]
   iIiIi11 = True
  else :
   iIiIi11 = False
  try :
   OOO = oOOo0O00o ( 'jsonrpc' ) [ 0 ] . string
  except : pass
  if OOO :
   if 25 - 25: II / ii11i % iIii1
   i1II1 = [ OOO ]
   if 42 - 42: O0O0OO0O0O0 * ii11i / I1Ii111 . O0O0OO0O0O0 % I1I11I1I1I
   OOO = True
  else :
   OOO = False
  try :
   iI11i1ii11 = oOOo0O00o ( 'thumbnail' ) [ 0 ] . string
   if iI11i1ii11 == None :
    raise
   iI11i1ii11 = OOo00O0 ( iI11i1ii11 )
  except :
   iI11i1ii11 = ''
  try :
   if not oOOo0O00o ( 'fanart' ) :
    if Ooo0OO0oOO . getSetting ( 'use_thumb' ) == "true" :
     OOooo0O00o = iI11i1ii11
    else :
     OOooo0O00o = fanart
   else :
    OOooo0O00o = oOOo0O00o ( 'fanart' ) [ 0 ] . string
   if OOooo0O00o == None :
    raise
  except :
   OOooo0O00o = fanart
  try :
   OOoo0O0 = oOOo0O00o ( 'info' ) [ 0 ] . string
   if OOoo0O0 == None :
    raise
  except :
   OOoo0O0 = ''
   if 41 - 41: oOOO0OOooOoO0Oo / iIIi1iI1II111
  try :
   oOO00oOO = oOOo0O00o ( 'genre' ) [ 0 ] . string
   if oOO00oOO == None :
    raise
  except :
   oOO00oOO = ''
   if 51 - 51: I1I11I1I1I % i11ii11iIi11i
  try :
   iiiIi1i1I = oOOo0O00o ( 'date' ) [ 0 ] . string
   if iiiIi1i1I == None :
    raise
  except :
   iiiIi1i1I = ''
   if 60 - 60: i11ii11iIi11i / I1II1 . i11ii11iIi11i / II . oOOO0OOooOoO0Oo
  oOo0oO = None
  if oOOo0O00o ( 'regex' ) :
   try :
    OO0000o = oOOo0O00o ( 'regex' )
    oOo0oO = OOOO0oo0 ( OO0000o )
   except :
    pass
  try :
   if 42 - 42: oOoO0oo0OOOo
   if len ( O00O0oOO00O00 ) > 1 :
    Oo0o0000o0o0 = 0
    oo000O0OoooO = [ ]
    O0o = True if '$$LSPlayOnlyOne$$' in O00O0oOO00O00 [ 0 ] else False
    if 27 - 27: oOOO0OOooOoO0Oo - OooO0OO / I1Ii111 % oOOO0OOooOoO0Oo + i11ii11iIi11i
    for iiI1 in O00O0oOO00O00 :
     if O00o0OO0 == "false" and not O0o :
      Oo0o0000o0o0 += 1
      I1i1Iiiii ( iiI1 , '%s) %s' % ( Oo0o0000o0o0 , Oo0OoO00oOO0o . encode ( 'utf-8' , 'ignore' ) ) , iI11i1ii11 , OOooo0O00o , OOoo0O0 , oOO00oOO , iiiIi1i1I , True , oo000O0OoooO , oOo0oO , o0oO00000 )
     elif ( O00o0OO0 == "true" and IIi1I1iiiii == 'true' ) or O0o :
      if oOo0oO :
       oo000O0OoooO . append ( iiI1 + '&regexs=' + oOo0oO )
      elif any ( x in iiI1 for x in O0 ) and iiI1 . startswith ( 'http' ) :
       oo000O0OoooO . append ( iiI1 + '&mode=19' )
      else :
       oo000O0OoooO . append ( iiI1 )
     else :
      oo000O0OoooO . append ( iiI1 )
      if 96 - 96: II
    if len ( oo000O0OoooO ) > 1 :
     if 97 - 97: IIi
     I1i1Iiiii ( '' , Oo0OoO00oOO0o . encode ( 'utf-8' ) , iI11i1ii11 , OOooo0O00o , OOoo0O0 , oOO00oOO , iiiIi1i1I , True , oo000O0OoooO , oOo0oO , o0oO00000 )
   else :
    if 48 - 48: I11i11Ii - II
    if dontLink :
     return Oo0OoO00oOO0o , O00O0oOO00O00 [ 0 ] , oOo0oO
    if iIiIi11 :
     if not oOo0oO == None :
      o0oo0o0O00OO ( Oo0OoO00oOO0o . encode ( 'utf-8' ) , i1II1 [ 0 ] . encode ( 'utf-8' ) , 1 , iI11i1ii11 , OOooo0O00o , OOoo0O0 , oOO00oOO , iiiIi1i1I , None , '!!update' , oOo0oO , O00O0oOO00O00 [ 0 ] . encode ( 'utf-8' ) )
      if 56 - 56: I1iII1iiII + i1iIi11iIIi1I + Iii1ii1II11i - IIi . Iii1ii1II11i
     else :
      o0oo0o0O00OO ( Oo0OoO00oOO0o . encode ( 'utf-8' ) , i1II1 [ 0 ] . encode ( 'utf-8' ) , 1 , iI11i1ii11 , OOooo0O00o , OOoo0O0 , oOO00oOO , iiiIi1i1I , None , 'source' , None , None )
      if 84 - 84: IiiI + I11i11Ii - i1iIi11iIIi1I . I1Ii111 * oOooOoO0Oo0O + i11ii11iIi11i
    elif OOO :
     o0oo0o0O00OO ( Oo0OoO00oOO0o . encode ( 'utf-8' ) , i1II1 [ 0 ] , 53 , iI11i1ii11 , OOooo0O00o , OOoo0O0 , oOO00oOO , iiiIi1i1I , None , 'source' )
     if 38 - 38: I1II1 + i1iIi11iIIi1I % IIi % Iii1ii1II11i - OooO0OO / oOooOoO0Oo0O
    else :
     try :
      if '$doregex' in Oo0OoO00oOO0o and not oOOoo0000O0o0 == None :
       II1III , III1 = oOOoo0000O0o0 ( oOo0oO , Oo0OoO00oOO0o )
       if not II1III == None :
        Oo0OoO00oOO0o = II1III
     except : pass
     try :
      if '$doregex' in iI11i1ii11 and not oOOoo0000O0o0 == None :
       II1III , III1 = oOOoo0000O0o0 ( oOo0oO , iI11i1ii11 )
       if not II1III == None :
        iI11i1ii11 = II1III
     except : pass
     I1i1Iiiii ( O00O0oOO00O00 [ 0 ] , Oo0OoO00oOO0o . encode ( 'utf-8' , 'ignore' ) , iI11i1ii11 , OOooo0O00o , OOoo0O0 , oOO00oOO , iiiIi1i1I , True , None , oOo0oO , o0oO00000 )
     if 68 - 68: ii11i * ii11i . I1iII1iiII / i1iIi11iIIi1I % oOoO0oo0OOOo
  except :
   OO0O00 ( 'There was a problem adding item - ' + Oo0OoO00oOO0o . encode ( 'utf-8' , 'ignore' ) )
   if 38 - 38: IIi - I1II1 / iIii1
def OOOO0oo0 ( reg_item ) :
 try :
  oOo0oO = { }
  for iiI1 in reg_item :
   oOo0oO [ iiI1 ( 'name' ) [ 0 ] . string ] = { }
   oOo0oO [ iiI1 ( 'name' ) [ 0 ] . string ] [ 'name' ] = iiI1 ( 'name' ) [ 0 ] . string
   if 66 - 66: iIIi1iI1II111 % I1Ii111 + O0O0OO0O0O0 . Iii1ii1II11i / OooO0OO + I1Ii111
   try :
    oOo0oO [ iiI1 ( 'name' ) [ 0 ] . string ] [ 'expres' ] = iiI1 ( 'expres' ) [ 0 ] . string
    if not oOo0oO [ iiI1 ( 'name' ) [ 0 ] . string ] [ 'expres' ] :
     oOo0oO [ iiI1 ( 'name' ) [ 0 ] . string ] [ 'expres' ] = ''
   except :
    OO0O00 ( "Regex: -- No Referer --" )
   oOo0oO [ iiI1 ( 'name' ) [ 0 ] . string ] [ 'page' ] = iiI1 ( 'page' ) [ 0 ] . string
   try :
    oOo0oO [ iiI1 ( 'name' ) [ 0 ] . string ] [ 'referer' ] = iiI1 ( 'referer' ) [ 0 ] . string
   except :
    OO0O00 ( "Regex: -- No Referer --" )
   try :
    oOo0oO [ iiI1 ( 'name' ) [ 0 ] . string ] [ 'connection' ] = iiI1 ( 'connection' ) [ 0 ] . string
   except :
    OO0O00 ( "Regex: -- No connection --" )
    if 86 - 86: I1iII1iiII
   try :
    oOo0oO [ iiI1 ( 'name' ) [ 0 ] . string ] [ 'notplayable' ] = iiI1 ( 'notplayable' ) [ 0 ] . string
   except :
    OO0O00 ( "Regex: -- No notplayable --" )
    if 5 - 5: oOOO0OOooOoO0Oo * Iii1ii1II11i
   try :
    oOo0oO [ iiI1 ( 'name' ) [ 0 ] . string ] [ 'noredirect' ] = iiI1 ( 'noredirect' ) [ 0 ] . string
   except :
    OO0O00 ( "Regex: -- No noredirect --" )
   try :
    oOo0oO [ iiI1 ( 'name' ) [ 0 ] . string ] [ 'origin' ] = iiI1 ( 'origin' ) [ 0 ] . string
   except :
    OO0O00 ( "Regex: -- No origin --" )
   try :
    oOo0oO [ iiI1 ( 'name' ) [ 0 ] . string ] [ 'accept' ] = iiI1 ( 'accept' ) [ 0 ] . string
   except :
    OO0O00 ( "Regex: -- No accept --" )
   try :
    oOo0oO [ iiI1 ( 'name' ) [ 0 ] . string ] [ 'includeheaders' ] = iiI1 ( 'includeheaders' ) [ 0 ] . string
   except :
    OO0O00 ( "Regex: -- No includeheaders --" )
    if 5 - 5: II
    if 90 - 90: II . IIi / OooO0OO - I1I11I1I1I
   try :
    oOo0oO [ iiI1 ( 'name' ) [ 0 ] . string ] [ 'listrepeat' ] = iiI1 ( 'listrepeat' ) [ 0 ] . string
    if 40 - 40: oOooOoO0Oo0O
   except :
    OO0O00 ( "Regex: -- No listrepeat --" )
    if 25 - 25: oOOO0OOooOoO0Oo + OooO0OO / IIi . I1iII1iiII % iIIi1iI1II111 * IiiI
    if 84 - 84: IIi % OooO0OO + O0O0OO0O0O0
    if 28 - 28: oOoO0oo0OOOo + IiiI * I1II1 % OOo . I1I11I1I1I % iIIi1iI1II111
   try :
    oOo0oO [ iiI1 ( 'name' ) [ 0 ] . string ] [ 'proxy' ] = iiI1 ( 'proxy' ) [ 0 ] . string
   except :
    OO0O00 ( "Regex: -- No proxy --" )
    if 16 - 16: I1I11I1I1I - ii11i / i11ii11iIi11i . i1iIi11iIIi1I + ii11i
   try :
    oOo0oO [ iiI1 ( 'name' ) [ 0 ] . string ] [ 'x-req' ] = iiI1 ( 'x-req' ) [ 0 ] . string
   except :
    OO0O00 ( "Regex: -- No x-req --" )
    if 19 - 19: IiiI - oOoO0oo0OOOo . iIIi1iI1II111
   try :
    oOo0oO [ iiI1 ( 'name' ) [ 0 ] . string ] [ 'x-addr' ] = iiI1 ( 'x-addr' ) [ 0 ] . string
   except :
    OO0O00 ( "Regex: -- No x-addr --" )
    if 60 - 60: i1iIi11iIIi1I + oOoO0oo0OOOo
   try :
    oOo0oO [ iiI1 ( 'name' ) [ 0 ] . string ] [ 'x-forward' ] = iiI1 ( 'x-forward' ) [ 0 ] . string
   except :
    OO0O00 ( "Regex: -- No x-forward --" )
    if 9 - 9: IIi * oOooOoO0Oo0O - ii11i + Iii1ii1II11i / IiiI . IiiI
   try :
    oOo0oO [ iiI1 ( 'name' ) [ 0 ] . string ] [ 'agent' ] = iiI1 ( 'agent' ) [ 0 ] . string
   except :
    OO0O00 ( "Regex: -- No User Agent --" )
   try :
    oOo0oO [ iiI1 ( 'name' ) [ 0 ] . string ] [ 'post' ] = iiI1 ( 'post' ) [ 0 ] . string
   except :
    OO0O00 ( "Regex: -- Not a post" )
   try :
    oOo0oO [ iiI1 ( 'name' ) [ 0 ] . string ] [ 'rawpost' ] = iiI1 ( 'rawpost' ) [ 0 ] . string
   except :
    OO0O00 ( "Regex: -- Not a rawpost" )
   try :
    oOo0oO [ iiI1 ( 'name' ) [ 0 ] . string ] [ 'htmlunescape' ] = iiI1 ( 'htmlunescape' ) [ 0 ] . string
   except :
    OO0O00 ( "Regex: -- Not a htmlunescape" )
    if 49 - 49: i1iIi11iIIi1I
    if 25 - 25: oOooOoO0Oo0O - i11ii11iIi11i . i11ii11iIi11i * OOo
   try :
    oOo0oO [ iiI1 ( 'name' ) [ 0 ] . string ] [ 'readcookieonly' ] = iiI1 ( 'readcookieonly' ) [ 0 ] . string
   except :
    OO0O00 ( "Regex: -- Not a readCookieOnly" )
    if 81 - 81: iIii1 + oOOO0OOooOoO0Oo
   try :
    oOo0oO [ iiI1 ( 'name' ) [ 0 ] . string ] [ 'cookiejar' ] = iiI1 ( 'cookiejar' ) [ 0 ] . string
    if not oOo0oO [ iiI1 ( 'name' ) [ 0 ] . string ] [ 'cookiejar' ] :
     oOo0oO [ iiI1 ( 'name' ) [ 0 ] . string ] [ 'cookiejar' ] = ''
   except :
    OO0O00 ( "Regex: -- Not a cookieJar" )
   try :
    oOo0oO [ iiI1 ( 'name' ) [ 0 ] . string ] [ 'setcookie' ] = iiI1 ( 'setcookie' ) [ 0 ] . string
   except :
    OO0O00 ( "Regex: -- Not a setcookie" )
   try :
    oOo0oO [ iiI1 ( 'name' ) [ 0 ] . string ] [ 'appendcookie' ] = iiI1 ( 'appendcookie' ) [ 0 ] . string
   except :
    OO0O00 ( "Regex: -- Not a appendcookie" )
    if 98 - 98: i11ii11iIi11i
   try :
    oOo0oO [ iiI1 ( 'name' ) [ 0 ] . string ] [ 'ignorecache' ] = iiI1 ( 'ignorecache' ) [ 0 ] . string
   except :
    OO0O00 ( "Regex: -- no ignorecache" )
    if 95 - 95: IIi / IIi
    if 30 - 30: I1Ii111 + oOoO0oo0OOOo / oOoO0oo0OOOo % I1Ii111 . I1Ii111
    if 55 - 55: IIi - I1I11I1I1I + i1iIi11iIIi1I + iIii1 % OooO0OO
    if 41 - 41: I11i11Ii - I1I11I1I1I - OooO0OO
    if 8 - 8: IiiI + II - I1iII1iiII % oOoO0oo0OOOo % I1iII1iiII * OOo
  oOo0oO = urllib . quote ( repr ( oOo0oO ) )
  return oOo0oO
  if 9 - 9: oOoO0oo0OOOo - O0O0OO0O0O0 - I1II1 * OooO0OO + IIi
 except :
  oOo0oO = None
  OO0O00 ( 'regex Error: ' + Oo0OoO00oOO0o . encode ( 'utf-8' , 'ignore' ) )
  if 44 - 44: i1iIi11iIIi1I
def OOOO0OOO ( url ) :
 try :
  for iiI1 in range ( 1 , 51 ) :
   i1i1ii = iII1ii1 ( url )
   if "EXT-X-STREAM-INF" in i1i1ii : return url
   if not "EXTM3U" in i1i1ii : return
   xbmc . sleep ( 2000 )
  return
 except :
  return
  if 12 - 12: I1II1 - IIi . oOooOoO0Oo0O / I1Ii111 . I11i11Ii * IiiI
def oOOoo0000O0o0 ( regexs , url , cookieJar = None , forCookieJarOnly = False , recursiveCall = False , cachedPages = { } , rawPost = False , cookie_jar_file = None ) :
 if not recursiveCall :
  regexs = eval ( urllib . unquote ( regexs ) )
  if 19 - 19: O0O0OO0O0O0 + oOooOoO0Oo0O - oOoO0oo0OOOo - I1I11I1I1I
  if 21 - 21: iIIi1iI1II111 % oOOO0OOooOoO0Oo . i11ii11iIi11i / i1iIi11iIIi1I + oOOO0OOooOoO0Oo
 OOOO0O00o = re . compile ( '\$doregex\[([^\]]*)\]' ) . findall ( url )
 if 62 - 62: ii11i
 i1II = True
 for iI1I in OOOO0O00o :
  if iI1I in regexs :
   if 100 - 100: ii11i + Iii1ii1II11i / oOoO0oo0OOOo . O0O0OO0O0O0
   III1I1Iii1iiI = regexs [ iI1I ]
   if 17 - 17: OooO0OO % ii11i - ii11i
   O0o0O0 = False
   if 'cookiejar' in III1I1Iii1iiI :
    if 11 - 11: i1iIi11iIIi1I % IiiI * iIii1 + IIi + OooO0OO
    O0o0O0 = III1I1Iii1iiI [ 'cookiejar' ]
    if '$doregex' in O0o0O0 :
     cookieJar = oOOoo0000O0o0 ( regexs , III1I1Iii1iiI [ 'cookiejar' ] , cookieJar , True , True , cachedPages )
     if 24 - 24: oOoO0oo0OOOo - OOo % ii11i . I11i11Ii / iIIi1iI1II111
     O0o0O0 = True
    else :
     O0o0O0 = True
     if 36 - 36: i11ii11iIi11i - I1I11I1I1I
   if O0o0O0 :
    if cookieJar == None :
     if 29 - 29: IIi * I1II1
     cookie_jar_file = None
     if 'open[' in III1I1Iii1iiI [ 'cookiejar' ] :
      cookie_jar_file = III1I1Iii1iiI [ 'cookiejar' ] . split ( 'open[' ) [ 1 ] . split ( ']' ) [ 0 ]
      if 10 - 10: II % oOOO0OOooOoO0Oo * oOOO0OOooOoO0Oo . I1I11I1I1I / OooO0OO % I1II1
      if 49 - 49: IiiI / OOo + iIIi1iI1II111 * I1iII1iiII
     cookieJar = I1ii11 ( cookie_jar_file )
     if 74 - 74: oOoO0oo0OOOo - I1iII1iiII . I11i11Ii
     if cookie_jar_file :
      i1III ( cookieJar , cookie_jar_file )
      if 49 - 49: O0O0OO0O0O0 % OooO0OO . Iii1ii1II11i
      if 13 - 13: O0O0OO0O0O0 + I11i11Ii * ii11i % oOooOoO0Oo0O - i1iIi11iIIi1I * I1II1
      if 26 - 26: oOooOoO0Oo0O * i11ii11iIi11i + I1II1
    elif 'save[' in III1I1Iii1iiI [ 'cookiejar' ] :
     cookie_jar_file = III1I1Iii1iiI [ 'cookiejar' ] . split ( 'save[' ) [ 1 ] . split ( ']' ) [ 0 ]
     IiIii1i111 = os . path . join ( O0oO , cookie_jar_file )
     if 43 - 43: iIIi1iI1II111
     i1III ( cookieJar , cookie_jar_file )
   if III1I1Iii1iiI [ 'page' ] and '$doregex' in III1I1Iii1iiI [ 'page' ] :
    Ii1 = oOOoo0000O0o0 ( regexs , III1I1Iii1iiI [ 'page' ] , cookieJar , recursiveCall = True , cachedPages = cachedPages )
    if len ( Ii1 ) == 0 :
     Ii1 = 'http://regexfailed'
    III1I1Iii1iiI [ 'page' ] = Ii1
    if 14 - 14: ii11i % ii11i * O0O0OO0O0O0 - IiiI - I1I11I1I1I
   if 'setcookie' in III1I1Iii1iiI and III1I1Iii1iiI [ 'setcookie' ] and '$doregex' in III1I1Iii1iiI [ 'setcookie' ] :
    III1I1Iii1iiI [ 'setcookie' ] = oOOoo0000O0o0 ( regexs , III1I1Iii1iiI [ 'setcookie' ] , cookieJar , recursiveCall = True , cachedPages = cachedPages )
   if 'appendcookie' in III1I1Iii1iiI and III1I1Iii1iiI [ 'appendcookie' ] and '$doregex' in III1I1Iii1iiI [ 'appendcookie' ] :
    III1I1Iii1iiI [ 'appendcookie' ] = oOOoo0000O0o0 ( regexs , III1I1Iii1iiI [ 'appendcookie' ] , cookieJar , recursiveCall = True , cachedPages = cachedPages )
    if 63 - 63: IiiI
    if 69 - 69: ii11i . I1Ii111 % IIi + ii11i / iIIi1iI1II111 / I1Ii111
   if 'post' in III1I1Iii1iiI and '$doregex' in III1I1Iii1iiI [ 'post' ] :
    III1I1Iii1iiI [ 'post' ] = oOOoo0000O0o0 ( regexs , III1I1Iii1iiI [ 'post' ] , cookieJar , recursiveCall = True , cachedPages = cachedPages )
    if 61 - 61: I1II1 % I1II1 * I1iII1iiII / I1iII1iiII
    if 75 - 75: oOOO0OOooOoO0Oo . IIi
   if 'rawpost' in III1I1Iii1iiI and '$doregex' in III1I1Iii1iiI [ 'rawpost' ] :
    III1I1Iii1iiI [ 'rawpost' ] = oOOoo0000O0o0 ( regexs , III1I1Iii1iiI [ 'rawpost' ] , cookieJar , recursiveCall = True , cachedPages = cachedPages , rawPost = True )
    if 50 - 50: Iii1ii1II11i
    if 60 - 60: IIi * ii11i * I1Ii111 * oOoO0oo0OOOo
   if 'rawpost' in III1I1Iii1iiI and '$epoctime$' in III1I1Iii1iiI [ 'rawpost' ] :
    III1I1Iii1iiI [ 'rawpost' ] = III1I1Iii1iiI [ 'rawpost' ] . replace ( '$epoctime$' , O0ooooo0OOOO0 ( ) )
    if 9 - 9: i1iIi11iIIi1I - I1iII1iiII / iIii1 / I1iII1iiII
   if 'rawpost' in III1I1Iii1iiI and '$epoctime2$' in III1I1Iii1iiI [ 'rawpost' ] :
    III1I1Iii1iiI [ 'rawpost' ] = III1I1Iii1iiI [ 'rawpost' ] . replace ( '$epoctime2$' , I1i111iiIIIi ( ) )
    if 75 - 75: I1I11I1I1I . oOooOoO0Oo0O % I1iII1iiII * I1I11I1I1I % oOooOoO0Oo0O
    if 13 - 13: oOOO0OOooOoO0Oo / O0O0OO0O0O0 % i1iIi11iIIi1I % I1I11I1I1I . I1Ii111
   iIIIii = ''
   if III1I1Iii1iiI [ 'page' ] and III1I1Iii1iiI [ 'page' ] in cachedPages and not 'ignorecache' in III1I1Iii1iiI and forCookieJarOnly == False :
    if 58 - 58: I1iII1iiII / oOOO0OOooOoO0Oo . Iii1ii1II11i / oOooOoO0Oo0O + II
    iIIIii = cachedPages [ III1I1Iii1iiI [ 'page' ] ]
   else :
    if III1I1Iii1iiI [ 'page' ] and not III1I1Iii1iiI [ 'page' ] == '' and III1I1Iii1iiI [ 'page' ] . startswith ( 'http' ) :
     if '$epoctime$' in III1I1Iii1iiI [ 'page' ] :
      III1I1Iii1iiI [ 'page' ] = III1I1Iii1iiI [ 'page' ] . replace ( '$epoctime$' , O0ooooo0OOOO0 ( ) )
     if '$epoctime2$' in III1I1Iii1iiI [ 'page' ] :
      III1I1Iii1iiI [ 'page' ] = III1I1Iii1iiI [ 'page' ] . replace ( '$epoctime2$' , I1i111iiIIIi ( ) )
      if 86 - 86: I1I11I1I1I * i11ii11iIi11i + I1I11I1I1I + i1iIi11iIIi1I
      if 8 - 8: II - iIii1 / IIi
     oo0oOoo = III1I1Iii1iiI [ 'page' ] . split ( '|' )
     oOOO0o00o = oo0oOoo [ 0 ]
     iI11 = None
     if len ( oo0oOoo ) > 1 :
      iI11 = oo0oOoo [ 1 ]
      if 96 - 96: I1II1
      if 85 - 85: I1iII1iiII . Iii1ii1II11i / IIi . iIIi1iI1II111 % II
      if 90 - 90: oOoO0oo0OOOo % iIIi1iI1II111 * ii11i . iIii1
      if 8 - 8: IIi + i1iIi11iIIi1I / iIii1 / I1I11I1I1I
      if 74 - 74: iIIi1iI1II111 / I11i11Ii
      if 78 - 78: oOooOoO0Oo0O . IiiI + IIi - I11i11Ii
      if 31 - 31: oOooOoO0Oo0O . I1II1
      if 83 - 83: iIii1 . iIIi1iI1II111 / oOoO0oo0OOOo / I1II1 - i1iIi11iIIi1I
      if 100 - 100: IiiI
      if 46 - 46: Iii1ii1II11i / ii11i % iIii1 . ii11i * iIii1
     IIi1ii1Ii = urllib2 . ProxyHandler ( urllib2 . getproxies ( ) )
     if 91 - 91: O0O0OO0O0O0 / oOooOoO0Oo0O + iIii1 - O0O0OO0O0O0 + I1II1
     if 18 - 18: i1iIi11iIIi1I / oOOO0OOooOoO0Oo
     if 4 - 4: i1iIi11iIIi1I / I1Ii111 + i1iIi11iIIi1I . ii11i
     II1111II = urllib2 . Request ( oOOO0o00o )
     if 'proxy' in III1I1Iii1iiI :
      IIiii11i = III1I1Iii1iiI [ 'proxy' ]
      if 100 - 100: IIi % ii11i * i1iIi11iIIi1I - iIii1
      if 92 - 92: IIi
      if oOOO0o00o [ : 5 ] == "https" :
       II11iI111i1 = urllib2 . ProxyHandler ( { 'https' : IIiii11i } )
       if 95 - 95: oOooOoO0Oo0O - oOOO0OOooOoO0Oo * i11ii11iIi11i + Iii1ii1II11i
      else :
       II11iI111i1 = urllib2 . ProxyHandler ( { 'http' : IIiii11i } )
       if 10 - 10: I1iII1iiII / O0O0OO0O0O0
      o00oO = urllib2 . build_opener ( II11iI111i1 )
      urllib2 . install_opener ( o00oO )
      if 92 - 92: oOOO0OOooOoO0Oo * oOoO0oo0OOOo * oOoO0oo0OOOo * i11ii11iIi11i . ii11i
      if 16 - 16: IIi % oOooOoO0Oo0O - I1II1 * OooO0OO * I1Ii111 / oOooOoO0Oo0O
     II1111II . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20100101 Firefox/14.0.1' )
     IIiii11i = None
     if 31 - 31: I1I11I1I1I . II * IIi + O0O0OO0O0O0 * OOo
     if 'referer' in III1I1Iii1iiI :
      II1111II . add_header ( 'Referer' , III1I1Iii1iiI [ 'referer' ] )
     if 'accept' in III1I1Iii1iiI :
      II1111II . add_header ( 'Accept' , III1I1Iii1iiI [ 'accept' ] )
     if 'agent' in III1I1Iii1iiI :
      II1111II . add_header ( 'User-agent' , III1I1Iii1iiI [ 'agent' ] )
     if 'x-req' in III1I1Iii1iiI :
      II1111II . add_header ( 'X-Requested-With' , III1I1Iii1iiI [ 'x-req' ] )
     if 'x-addr' in III1I1Iii1iiI :
      II1111II . add_header ( 'x-addr' , III1I1Iii1iiI [ 'x-addr' ] )
     if 'x-forward' in III1I1Iii1iiI :
      II1111II . add_header ( 'X-Forwarded-For' , III1I1Iii1iiI [ 'x-forward' ] )
     if 'setcookie' in III1I1Iii1iiI :
      if 93 - 93: I1Ii111 / ii11i * I11i11Ii % oOooOoO0Oo0O * iIIi1iI1II111 * I1I11I1I1I
      II1111II . add_header ( 'Cookie' , III1I1Iii1iiI [ 'setcookie' ] )
     if 'appendcookie' in III1I1Iii1iiI :
      if 64 - 64: i1iIi11iIIi1I + iIIi1iI1II111 / ii11i / oOoO0oo0OOOo . IIi % oOOO0OOooOoO0Oo
      iiI1I1ii = III1I1Iii1iiI [ 'appendcookie' ]
      iiI1I1ii = iiI1I1ii . split ( ';' )
      for o0ooO in iiI1I1ii :
       OoOOOo0o0ooo , I1iiiiI1iI = o0ooO . split ( '=' )
       iIiiiii1i , OoOOOo0o0ooo = OoOOOo0o0ooo . split ( ':' )
       iiIi1IIiI = cookielib . Cookie ( version = 0 , name = OoOOOo0o0ooo , value = I1iiiiI1iI , port = None , port_specified = False , domain = iIiiiii1i , domain_specified = False , domain_initial_dot = False , path = '/' , path_specified = True , secure = False , expires = None , discard = True , comment = None , comment_url = None , rest = { 'HttpOnly' : None } , rfc2109 = False )
       cookieJar . set_cookie ( iiIi1IIiI )
     if 'origin' in III1I1Iii1iiI :
      II1111II . add_header ( 'Origin' , III1I1Iii1iiI [ 'origin' ] )
     if iI11 :
      iI11 = iI11 . split ( '&' )
      for o0ooO in iI11 :
       if o0ooO . split ( '=' ) == 2 :
        OoOOOo0o0ooo , I1iiiiI1iI = o0ooO . split ( '=' )
       else :
        i1oO0OO0 = o0ooO . split ( '=' )
        OoOOOo0o0ooo = i1oO0OO0 [ 0 ]
        I1iiiiI1iI = '=' . join ( i1oO0OO0 [ 1 : ] )
        if 82 - 82: oOOO0OOooOoO0Oo - oOOO0OOooOoO0Oo + Iii1ii1II11i
       II1111II . add_header ( OoOOOo0o0ooo , I1iiiiI1iI )
       if 8 - 8: I1iII1iiII % iIii1 * OOo % OooO0OO . IIi / IIi
     if not cookieJar == None :
      if 81 - 81: IiiI
      oO0o00oOOooO0 = urllib2 . HTTPCookieProcessor ( cookieJar )
      o00oO = urllib2 . build_opener ( oO0o00oOOooO0 , urllib2 . HTTPBasicAuthHandler ( ) , urllib2 . HTTPHandler ( ) )
      o00oO = urllib2 . install_opener ( o00oO )
      if 79 - 79: IiiI - ii11i + OooO0OO - II
      if 93 - 93: i1iIi11iIIi1I . i11ii11iIi11i - oOoO0oo0OOOo + Iii1ii1II11i
      if 'noredirect' in III1I1Iii1iiI :
       o00oO = urllib2 . build_opener ( oO0o00oOOooO0 , iiiii , urllib2 . HTTPBasicAuthHandler ( ) , urllib2 . HTTPHandler ( ) )
       o00oO = urllib2 . install_opener ( o00oO )
     elif 'noredirect' in III1I1Iii1iiI :
      o00oO = urllib2 . build_opener ( iiiii , urllib2 . HTTPBasicAuthHandler ( ) , urllib2 . HTTPHandler ( ) )
      o00oO = urllib2 . install_opener ( o00oO )
      if 61 - 61: i1iIi11iIIi1I
      if 15 - 15: O0O0OO0O0O0 % i11ii11iIi11i * I1I11I1I1I / II
     if 'connection' in III1I1Iii1iiI :
      if 90 - 90: iIii1
      from keepalive import HTTPHandler
      i1i1i1I = HTTPHandler ( )
      o00oO = urllib2 . build_opener ( i1i1i1I )
      urllib2 . install_opener ( o00oO )
      if 83 - 83: OOo + oOooOoO0Oo0O
      if 22 - 22: OooO0OO % iIii1 * oOooOoO0Oo0O - I1iII1iiII / ii11i
      if 86 - 86: oOooOoO0Oo0O . iIii1 % Iii1ii1II11i / I1I11I1I1I * iIii1 / I1iII1iiII
     oOoOOo000oOoO0 = None
     if 86 - 86: i1iIi11iIIi1I % O0O0OO0O0O0 + OooO0OO % O0O0OO0O0O0
     if 'post' in III1I1Iii1iiI :
      Ooo0o0OOO = III1I1Iii1iiI [ 'post' ]
      if 35 - 35: I1II1 + iIii1
      if 40 - 40: I1iII1iiII
      if 67 - 67: OOo + i1iIi11iIIi1I - iIIi1iI1II111 . OOo * i1iIi11iIIi1I * I1I11I1I1I
      if 90 - 90: OooO0OO . oOOO0OOooOoO0Oo
      OO00O0oOO = Ooo0o0OOO . split ( ',' ) ;
      oOoOOo000oOoO0 = { }
      for Ii1iI111 in OO00O0oOO :
       OoOOOo0o0ooo = Ii1iI111 . split ( ':' ) [ 0 ] ;
       I1iiiiI1iI = Ii1iI111 . split ( ':' ) [ 1 ] ;
       oOoOOo000oOoO0 [ OoOOOo0o0ooo ] = I1iiiiI1iI
      oOoOOo000oOoO0 = urllib . urlencode ( oOoOOo000oOoO0 )
      if 51 - 51: oOOO0OOooOoO0Oo * iIIi1iI1II111 / i1iIi11iIIi1I . OooO0OO % I1II1 / i11ii11iIi11i
     if 'rawpost' in III1I1Iii1iiI :
      oOoOOo000oOoO0 = III1I1Iii1iiI [ 'rawpost' ]
      if 9 - 9: i11ii11iIi11i % i11ii11iIi11i % i1iIi11iIIi1I
      if 30 - 30: oOOO0OOooOoO0Oo + II - oOOO0OOooOoO0Oo . oOOO0OOooOoO0Oo - i1iIi11iIIi1I + iIIi1iI1II111
      if 86 - 86: I11i11Ii
      if 41 - 41: Iii1ii1II11i * I1I11I1I1I / Iii1ii1II11i % OOo
     iIIIii = ''
     try :
      if 18 - 18: i1iIi11iIIi1I . oOooOoO0Oo0O % Iii1ii1II11i % OooO0OO
      if oOoOOo000oOoO0 :
       II1IiiIii = urllib2 . urlopen ( II1111II , oOoOOo000oOoO0 )
      else :
       II1IiiIii = urllib2 . urlopen ( II1111II )
      if II1IiiIii . info ( ) . get ( 'Content-Encoding' ) == 'gzip' :
       from StringIO import StringIO
       import gzip
       oOo0OoOOo0 = StringIO ( II1IiiIii . read ( ) )
       iII11I1Ii1 = gzip . GzipFile ( fileobj = oOo0OoOOo0 )
       iIIIii = iII11I1Ii1 . read ( )
      else :
       iIIIii = II1IiiIii . read ( )
       if 92 - 92: I1I11I1I1I / I1I11I1I1I . I1Ii111
       if 17 - 17: O0O0OO0O0O0 - i1iIi11iIIi1I * I1iII1iiII
       if 5 - 5: I1II1 - I1II1 . oOoO0oo0OOOo + Iii1ii1II11i - I1II1 . OOo
      if 'proxy' in III1I1Iii1iiI and not IIi1ii1Ii is None :
       urllib2 . install_opener ( urllib2 . build_opener ( IIi1ii1Ii ) )
       if 31 - 31: i1iIi11iIIi1I - ii11i - ii11i % I1I11I1I1I
      iIIIii = iii ( iIIIii )
      if 27 - 27: I1I11I1I1I / O0O0OO0O0O0 / I11i11Ii + II
      if 34 - 34: I1II1
      if 'includeheaders' in III1I1Iii1iiI :
       if 91 - 91: ii11i % I1iII1iiII . ii11i % I11i11Ii / i1iIi11iIIi1I * Iii1ii1II11i
       iIIIii += '$$HEADERS_START$$:'
       for oo000OO00Oo in II1IiiIii . headers :
        iIIIii += oo000OO00Oo + ':' + II1IiiIii . headers . get ( oo000OO00Oo ) + '\n'
       iIIIii += '$$HEADERS_END$$:'
       if 10 - 10: i1iIi11iIIi1I . iIii1
      OO0O00 ( iIIIii )
      OO0O00 ( cookieJar )
      if 32 - 32: OooO0OO . oOOO0OOooOoO0Oo . oOooOoO0Oo0O - IiiI + OOo
      II1IiiIii . close ( )
     except :
      pass
     cachedPages [ III1I1Iii1iiI [ 'page' ] ] = iIIIii
     if 88 - 88: iIii1
     if 19 - 19: i1iIi11iIIi1I * oOOO0OOooOoO0Oo + OooO0OO
     if 65 - 65: I1II1 . II . IiiI . iIii1 - I1II1
     if forCookieJarOnly :
      return cookieJar
    elif III1I1Iii1iiI [ 'page' ] and not III1I1Iii1iiI [ 'page' ] . startswith ( 'http' ) :
     if III1I1Iii1iiI [ 'page' ] . startswith ( '$pyFunction:' ) :
      ii111i = ooOOOoO ( III1I1Iii1iiI [ 'page' ] . split ( '$pyFunction:' ) [ 1 ] , '' , cookieJar , III1I1Iii1iiI )
      if forCookieJarOnly :
       return cookieJar
      iIIIii = ii111i
      iIIIii = iii ( iIIIii )
     else :
      iIIIii = III1I1Iii1iiI [ 'page' ]
   if '$pyFunction:playmedia(' in III1I1Iii1iiI [ 'expres' ] or 'ActivateWindow' in III1I1Iii1iiI [ 'expres' ] or 'RunPlugin' in III1I1Iii1iiI [ 'expres' ] or '$PLAYERPROXY$=' in url or any ( x in url for x in o0O ) :
    i1II = False
   if '$doregex' in III1I1Iii1iiI [ 'expres' ] :
    III1I1Iii1iiI [ 'expres' ] = oOOoo0000O0o0 ( regexs , III1I1Iii1iiI [ 'expres' ] , cookieJar , recursiveCall = True , cachedPages = cachedPages )
    if 93 - 93: IiiI
   if not III1I1Iii1iiI [ 'expres' ] == '' :
    if 5 - 5: I1I11I1I1I / I1II1
    if '$LiveStreamCaptcha' in III1I1Iii1iiI [ 'expres' ] :
     ii111i = O00OO0oO ( III1I1Iii1iiI , iIIIii , cookieJar )
     if 25 - 25: oOoO0oo0OOOo % I1Ii111 * IIi
     url = url . replace ( "$doregex[" + iI1I + "]" , ii111i )
     if 6 - 6: iIii1 . oOOO0OOooOoO0Oo * Iii1ii1II11i . I11i11Ii
    elif III1I1Iii1iiI [ 'expres' ] . startswith ( '$pyFunction:' ) or '#$pyFunction' in III1I1Iii1iiI [ 'expres' ] :
     if 98 - 98: I11i11Ii
     ii111i = ''
     if III1I1Iii1iiI [ 'expres' ] . startswith ( '$pyFunction:' ) :
      ii111i = ooOOOoO ( III1I1Iii1iiI [ 'expres' ] . split ( '$pyFunction:' ) [ 1 ] , iIIIii , cookieJar , III1I1Iii1iiI )
     else :
      ii111i = oO0O ( III1I1Iii1iiI [ 'expres' ] , iIIIii , cookieJar , III1I1Iii1iiI )
     if 'ActivateWindow' in III1I1Iii1iiI [ 'expres' ] or 'RunPlugin' in III1I1Iii1iiI [ 'expres' ] : return '' , False
     if forCookieJarOnly :
      return cookieJar
     if 'listrepeat' in III1I1Iii1iiI :
      oOO = III1I1Iii1iiI [ 'listrepeat' ]
      if 11 - 11: O0O0OO0O0O0 - OOo . OOo
      if 31 - 31: I1II1 / oOoO0oo0OOOo * I11i11Ii . Iii1ii1II11i
      return oOO , eval ( ii111i ) , III1I1Iii1iiI , regexs , cookieJar
      if 57 - 57: I1II1 + ii11i % I11i11Ii % i11ii11iIi11i
      if 83 - 83: I1iII1iiII / O0O0OO0O0O0 % ii11i . I1I11I1I1I % OOo . oOooOoO0Oo0O
      if 94 - 94: OooO0OO + ii11i % IiiI
     try :
      url = url . replace ( u"$doregex[" + iI1I + "]" , ii111i )
     except : url = url . replace ( "$doregex[" + iI1I + "]" , ii111i . decode ( "utf-8" ) )
    else :
     if 'listrepeat' in III1I1Iii1iiI :
      oOO = III1I1Iii1iiI [ 'listrepeat' ]
      if 93 - 93: OooO0OO - I1II1 + ii11i * I1iII1iiII + II . iIii1
      if 49 - 49: oOooOoO0Oo0O * I1I11I1I1I - oOoO0oo0OOOo . OOo
      if 89 - 89: IIi + OooO0OO * IIi / IIi
      if 46 - 46: IiiI
      O0000 = re . findall ( III1I1Iii1iiI [ 'expres' ] , iIIIii )
      if 64 - 64: i1iIi11iIIi1I - i11ii11iIi11i
      return oOO , O0000 , III1I1Iii1iiI , regexs , cookieJar
      if 68 - 68: IIi - I1II1 - ii11i / Iii1ii1II11i + I1II1 - IiiI
     ii111i = ''
     if not iIIIii == '' :
      if 75 - 75: iIii1 / I1iII1iiII % ii11i . oOooOoO0Oo0O % oOooOoO0Oo0O % i1iIi11iIIi1I
      Ii1i1i1111 = re . compile ( III1I1Iii1iiI [ 'expres' ] ) . search ( iIIIii )
      try :
       ii111i = Ii1i1i1111 . group ( 1 ) . strip ( )
      except : traceback . print_exc ( )
     elif III1I1Iii1iiI [ 'page' ] == '' or III1I1Iii1iiI [ 'page' ] == None :
      ii111i = III1I1Iii1iiI [ 'expres' ]
      if 57 - 57: OooO0OO % i1iIi11iIIi1I
     if rawPost :
      if 67 - 67: IIi + i11ii11iIi11i * O0O0OO0O0O0 - OOo / oOOO0OOooOoO0Oo % iIii1
      ii111i = urllib . quote_plus ( ii111i )
     if 'htmlunescape' in III1I1Iii1iiI :
      if 92 - 92: OooO0OO - OOo - IIi % oOooOoO0Oo0O / I1II1
      import HTMLParser
      ii111i = HTMLParser . HTMLParser ( ) . unescape ( ii111i )
     try :
      url = url . replace ( "$doregex[" + iI1I + "]" , ii111i )
     except : url = url . replace ( "$doregex[" + iI1I + "]" , ii111i . decode ( "utf-8" ) )
     if 19 - 19: oOoO0oo0OOOo - IiiI
     if 56 - 56: I1Ii111
   else :
    url = url . replace ( "$doregex[" + iI1I + "]" , '' )
 if '$epoctime$' in url :
  url = url . replace ( '$epoctime$' , O0ooooo0OOOO0 ( ) )
 if '$epoctime2$' in url :
  url = url . replace ( '$epoctime2$' , I1i111iiIIIi ( ) )
  if 26 - 26: oOooOoO0Oo0O % oOooOoO0Oo0O
 if '$GUID$' in url :
  import uuid
  url = url . replace ( '$GUID$' , str ( uuid . uuid1 ( ) ) . upper ( ) )
 if '$get_cookies$' in url :
  url = url . replace ( '$get_cookies$' , iIIIII1iiiiII ( cookieJar ) )
  if 54 - 54: I11i11Ii
 if recursiveCall : return url
 if 22 - 22: I11i11Ii + OooO0OO
 if url == "" :
  return
 else :
  return url , i1II
def O0o0O0OO00o ( t ) :
 import hashlib
 o0ooO = hashlib . md5 ( )
 o0ooO . update ( t )
 return o0ooO . hexdigest ( )
 if 92 - 92: I1iII1iiII + II / oOoO0oo0OOOo % IiiI % oOOO0OOooOoO0Oo . oOooOoO0Oo0O
def O0Oo ( encrypted ) :
 I1IiI111I11 = ""
 if 16 - 16: iIIi1iI1II111 / OooO0OO . I1Ii111
 if 58 - 58: oOoO0oo0OOOo / OOo
 if 44 - 44: I1II1
 if 54 - 54: OooO0OO - I1I11I1I1I - II . ii11i
 if 79 - 79: OooO0OO . IiiI
def IIiI1I1 ( media_url ) :
 try :
  import CustomPlayer
  I11I1IIiiII1 = CustomPlayer . MyXBMCPlayer ( )
  IIIIIii1ii11 = xbmcgui . ListItem ( label = str ( Oo0OoO00oOO0o ) , iconImage = "DefaultVideo.png" , thumbnailImage = xbmc . getInfoImage ( "ListItem.Thumb" ) , path = media_url )
  I11I1IIiiII1 . play ( media_url , IIIIIii1ii11 )
  xbmc . sleep ( 1000 )
  while I11I1IIiiII1 . is_active :
   xbmc . sleep ( 200 )
 except :
  traceback . print_exc ( )
 return ''
 if 86 - 86: Iii1ii1II11i * i1iIi11iIIi1I - iIIi1iI1II111 . Iii1ii1II11i % ii11i / I1II1
def IiIIiIIIiIii ( params ) :
 O0o0Oo = json . dumps ( params )
 I1i11II = xbmc . executeJSONRPC ( O0o0Oo )
 if 31 - 31: OOo / oOOO0OOooOoO0Oo * I1iII1iiII . i1iIi11iIIi1I
 try :
  II1IiiIii = json . loads ( I1i11II )
 except UnicodeDecodeError :
  II1IiiIii = json . loads ( I1i11II . decode ( 'utf-8' , 'ignore' ) )
  if 89 - 89: iIIi1iI1II111
 try :
  if 'result' in II1IiiIii :
   return II1IiiIii [ 'result' ]
  return None
 except KeyError :
  logger . warn ( "[%s] %s" % ( params [ 'method' ] , II1IiiIii [ 'error' ] [ 'message' ] ) )
  return None
  if 2 - 2: I1Ii111 . I1Ii111 + I1Ii111 * I1iII1iiII
  if 100 - 100: oOoO0oo0OOOo % OooO0OO / I1I11I1I1I
def iIII11Ii ( proxysettings = None ) :
 if 52 - 52: II / IIi - I1I11I1I1I
 if proxysettings == None :
  if 49 - 49: Iii1ii1II11i / oOoO0oo0OOOo . O0O0OO0O0O0
  xbmc . executeJSONRPC ( '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"network.usehttpproxy", "value":false}, "id":1}' )
 else :
  if 21 - 21: Iii1ii1II11i + O0O0OO0O0O0 + i11ii11iIi11i * I1iII1iiII % iIii1 % i1iIi11iIIi1I
  oOO0OO0OO = proxysettings . split ( ':' )
  oOOoooO = oOO0OO0OO [ 0 ]
  i1ii11 = oOO0OO0OO [ 1 ]
  ii1i = oOO0OO0OO [ 2 ]
  IIioo0OO = None
  IiiI11i1I = None
  if 80 - 80: I1II1 / I1I11I1I1I / Iii1ii1II11i + I11i11Ii - oOoO0oo0OOOo
  if len ( oOO0OO0OO ) > 3 and '@' in oOO0OO0OO [ 3 ] :
   IIioo0OO = oOO0OO0OO [ 3 ] . split ( '@' ) [ 0 ]
   IiiI11i1I = oOO0OO0OO [ 3 ] . split ( '@' ) [ 1 ]
   if 11 - 11: I1iII1iiII * IiiI
   if 15 - 15: Iii1ii1II11i
  xbmc . executeJSONRPC ( '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"network.usehttpproxy", "value":true}, "id":1}' )
  xbmc . executeJSONRPC ( '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"network.httpproxytype", "value":' + str ( ii1i ) + '}, "id":1}' )
  xbmc . executeJSONRPC ( '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"network.httpproxyserver", "value":"' + str ( oOOoooO ) + '"}, "id":1}' )
  xbmc . executeJSONRPC ( '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"network.httpproxyport", "value":' + str ( i1ii11 ) + '}, "id":1}' )
  if 62 - 62: OooO0OO
  if 51 - 51: Iii1ii1II11i
  if not IIioo0OO == None :
   xbmc . executeJSONRPC ( '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"network.httpproxyusername", "value":"' + str ( IIioo0OO ) + '"}, "id":1}' )
   xbmc . executeJSONRPC ( '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"network.httpproxypassword", "value":"' + str ( IiiI11i1I ) + '"}, "id":1}' )
   if 14 - 14: oOOO0OOooOoO0Oo % OOo % oOoO0oo0OOOo - O0O0OO0O0O0
   if 53 - 53: OooO0OO % oOoO0oo0OOOo
def O0ooOo0o0Oo ( ) :
 OooO0oOo = IiIIiIIIiIii ( { 'jsonrpc' : '2.0' , "method" : "Settings.GetSettingValue" , "params" : { "setting" : "network.usehttpproxy" } , 'id' : 1 } ) [ 'value' ]
 if 66 - 66: IiiI * oOoO0oo0OOOo
 ii1i = IiIIiIIIiIii ( { 'jsonrpc' : '2.0' , "method" : "Settings.GetSettingValue" , "params" : { "setting" : "network.httpproxytype" } , 'id' : 1 } ) [ 'value' ]
 if 28 - 28: IiiI % Iii1ii1II11i % I1Ii111 + i11ii11iIi11i / i11ii11iIi11i
 if OooO0oOo :
  oOOoooO = IiIIiIIIiIii ( { 'jsonrpc' : '2.0' , "method" : "Settings.GetSettingValue" , "params" : { "setting" : "network.httpproxyserver" } , 'id' : 1 } ) [ 'value' ]
  i1ii11 = unicode ( IiIIiIIIiIii ( { 'jsonrpc' : '2.0' , "method" : "Settings.GetSettingValue" , "params" : { "setting" : "network.httpproxyport" } , 'id' : 1 } ) [ 'value' ] )
  IIioo0OO = IiIIiIIIiIii ( { 'jsonrpc' : '2.0' , "method" : "Settings.GetSettingValue" , "params" : { "setting" : "network.httpproxyusername" } , 'id' : 1 } ) [ 'value' ]
  IiiI11i1I = IiIIiIIIiIii ( { 'jsonrpc' : '2.0' , "method" : "Settings.GetSettingValue" , "params" : { "setting" : "network.httpproxypassword" } , 'id' : 1 } ) [ 'value' ]
  if 71 - 71: I1II1 * IiiI % oOooOoO0Oo0O % IiiI / i11ii11iIi11i
  if IIioo0OO and IiiI11i1I and oOOoooO and i1ii11 :
   return oOOoooO + ':' + str ( i1ii11 ) + ':' + str ( ii1i ) + ':' + IIioo0OO + '@' + IiiI11i1I
  elif oOOoooO and i1ii11 :
   return oOOoooO + ':' + str ( i1ii11 ) + ':' + str ( ii1i )
 else :
  return None
  if 56 - 56: oOooOoO0Oo0O % O0O0OO0O0O0 * ii11i . IiiI * iIIi1iI1II111
def iI ( media_url , name , iconImage , proxyip , port , proxyuser = None , proxypass = None ) :
 if 99 - 99: I1I11I1I1I - II - OOo % IiiI
 if media_url == None or media_url == '' :
  xbmc . executebuiltin ( "XBMC.Notification(probando,Unable to play empty Url,5000," + o0oOoO00o + ")" )
  return
 IiiIIiiiiii = xbmcgui . DialogProgress ( )
 IiiIIiiiiii . create ( 'Progress' , 'Playing with custom proxy' )
 IiiIIiiiiii . update ( 10 , "" , "setting proxy.." , "" )
 OOOO0o = False
 i1I1iIi1IiI = ''
 if 11 - 11: i1iIi11iIIi1I
 try :
  if 95 - 95: oOOO0OOooOoO0Oo * I1Ii111 % IIi % OooO0OO - OooO0OO
  i1I1iIi1IiI = O0ooOo0o0Oo ( )
  print 'existing_proxy' , i1I1iIi1IiI
  if 97 - 97: I1Ii111 + ii11i . iIIi1iI1II111
  if 64 - 64: I11i11Ii % IIi / O0O0OO0O0O0 - I11i11Ii % I1II1 . iIii1
  if not proxyuser == None :
   iIII11Ii ( proxyip + ':' + port + ':0:' + proxyuser + '@' + proxypass )
  else :
   iIII11Ii ( proxyip + ':' + port + ':0' )
   if 8 - 8: oOoO0oo0OOOo + i1iIi11iIIi1I * I1II1 * Iii1ii1II11i * I1I11I1I1I / oOOO0OOooOoO0Oo
  print 'proxy setting complete playing' , media_url
  OOOO0o = True
  IiiIIiiiiii . update ( 80 , "" , "setting proxy complete, now playing" , "" )
  if 21 - 21: OOo / oOooOoO0Oo0O
  if 11 - 11: I1II1 % OooO0OO - O0O0OO0O0O0 - OOo + IIi + oOOO0OOooOoO0Oo
  import CustomPlayer
  I11I1IIiiII1 = CustomPlayer . MyXBMCPlayer ( )
  I11I1IIiiII1 . pdialogue == IiiIIiiiiii
  IIIIIii1ii11 = xbmcgui . ListItem ( label = str ( name ) , iconImage = iconImage , thumbnailImage = xbmc . getInfoImage ( "ListItem.Thumb" ) , path = media_url )
  I11I1IIiiII1 . play ( media_url , IIIIIii1ii11 )
  xbmc . sleep ( 1000 )
  if 87 - 87: II * I11i11Ii / I1Ii111
  if 6 - 6: I1iII1iiII + oOoO0oo0OOOo - oOooOoO0Oo0O % I1II1 * Iii1ii1II11i
  import time
  oOoO = time . time ( )
  try :
   while I11I1IIiiII1 . is_active :
    xbmc . sleep ( 1000 )
    if I11I1IIiiII1 . urlplayed == False and time . time ( ) - oOoO > 12 :
     print 'failed!!!'
     xbmc . executebuiltin ( "XBMC.Notification(probando,Unable to play check proxy,5000," + o0oOoO00o + ")" )
     break
     if 26 - 26: Iii1ii1II11i / oOoO0oo0OOOo - I11i11Ii + I1I11I1I1I
  except : pass
  if 38 - 38: oOooOoO0Oo0O / I1Ii111 . iIIi1iI1II111 / I11i11Ii / oOoO0oo0OOOo + ii11i
  IiiIIiiiiii . close ( )
  IiiIIiiiiii = None
 except :
  traceback . print_exc ( )
 if IiiIIiiiiii :
  IiiIIiiiiii . close ( )
 if OOOO0o :
  print 'now resetting the proxy back'
  iIII11Ii ( i1I1iIi1IiI )
  print 'reset here'
 return ''
 if 96 - 96: iIii1
def oo ( url , headers = None ) :
 try :
  if headers is None :
   headers = { 'User-Agent' : 'probando-zte' }
   if 18 - 18: iIii1 * I1I11I1I1I - OooO0OO
  if '|' in url :
   url , iI11 = url . split ( '|' )
   iI11 = iI11 . split ( '&' )
   if 31 - 31: oOoO0oo0OOOo - iIIi1iI1II111 % Iii1ii1II11i % OOo
   for o0ooO in iI11 :
    if len ( o0ooO . split ( '=' ) ) == 2 :
     OoOOOo0o0ooo , I1iiiiI1iI = o0ooO . split ( '=' )
    else :
     i1oO0OO0 = o0ooO . split ( '=' )
     OoOOOo0o0ooo = i1oO0OO0 [ 0 ]
     I1iiiiI1iI = '=' . join ( i1oO0OO0 [ 1 : ] )
     if 45 - 45: I1Ii111 + i1iIi11iIIi1I * O0O0OO0O0O0
    print OoOOOo0o0ooo , I1iiiiI1iI
    headers [ OoOOOo0o0ooo ] = I1iiiiI1iI
    if 13 - 13: oOooOoO0Oo0O * OOo - OooO0OO / I1II1 + I1I11I1I1I + oOOO0OOooOoO0Oo
  II1111II = urllib2 . Request ( url , None , headers )
  II1IiiIii = urllib2 . urlopen ( II1111II )
  O0o0Oo = II1IiiIii . read ( )
  II1IiiIii . close ( )
  return O0o0Oo
 except urllib2 . URLError , iii1III1i :
  OO0O00 ( 'URL: ' + url )
  if hasattr ( iii1III1i , 'code' ) :
   OO0O00 ( 'We failed with error code - %s.' % iii1III1i . code )
   xbmc . executebuiltin ( "XBMC.Notification(probando,We failed with error code - " + str ( iii1III1i . code ) + ",10000," + o0oOoO00o + ")" )
  elif hasattr ( iii1III1i , 'reason' ) :
   OO0O00 ( 'We failed to reach a server.' )
   OO0O00 ( 'Reason: %s' % iii1III1i . reason )
   xbmc . executebuiltin ( "XBMC.Notification(probando,We failed to reach a server. - " + str ( iii1III1i . reason ) + ",10000," + o0oOoO00o + ")" )
   if 17 - 17: i1iIi11iIIi1I / i1iIi11iIIi1I
   if 65 - 65: oOOO0OOooOoO0Oo + oOoO0oo0OOOo
def Ooo0O0 ( page_value , referer = None ) :
 if referer :
  referer = [ ( 'Referer' , referer ) ]
 if page_value . startswith ( "http" ) :
  ooo0 = page_value
  page_value = iII1ii1 ( page_value , headers = referer )
  if 55 - 55: oOoO0oo0OOOo
 ooO0o = "(eval\(function\(p,a,c,k,e,(?:r|d).*)"
 if 25 - 25: ii11i - iIii1
 IiI1IiI11iII = re . compile ( ooO0o ) . findall ( page_value )
 OOoOO0OO = ""
 if IiI1IiI11iII and len ( IiI1IiI11iII ) > 0 :
  for I1iiiiI1iI in IiI1IiI11iII :
   i1oo00OoO = iIIi1IIi ( I1iiiiI1iI )
   i111i11I1ii = O0ooO0Oo00o ( i1oo00OoO , '\'(.*?)\'' )
   if 'unescape' in i1oo00OoO :
    i1oo00OoO = urllib . unquote ( i111i11I1ii )
   OOoOO0OO += i1oo00OoO + '\n'
   if 64 - 64: OOo / O0O0OO0O0O0 / I1iII1iiII . oOooOoO0Oo0O
   if 11 - 11: I1I11I1I1I % I11i11Ii
  ooo0 = O0ooO0Oo00o ( OOoOO0OO , 'src="(.*?)"' )
  if 16 - 16: i11ii11iIi11i + IIi % Iii1ii1II11i
  page_value = iII1ii1 ( ooo0 , headers = referer )
  if 80 - 80: IIi * iIIi1iI1II111
  if 78 - 78: Iii1ii1II11i
  if 20 - 20: iIii1 % OooO0OO . OooO0OO / I1I11I1I1I + Iii1ii1II11i . OooO0OO
 O0ooOo0 = O0ooO0Oo00o ( page_value , 'streamer\'.*?\'(.*?)\'\)' )
 oo00ooOoo = O0ooO0Oo00o ( page_value , 'file\',\s\'(.*?)\'' )
 if 28 - 28: OooO0OO
 if 1 - 1: OooO0OO
 return O0ooOo0 + ' playpath=' + oo00ooOoo + ' pageUrl=' + ooo0
 if 48 - 48: iIIi1iI1II111 + iIIi1iI1II111 . II - IIi
def o00oo0000 ( page_value , referer = None ) :
 if referer :
  referer = [ ( 'Referer' , referer ) ]
 if page_value . startswith ( "http" ) :
  page_value = iII1ii1 ( page_value , headers = referer )
 ooO0o = "var a = (.*?);\s*var b = (.*?);\s*var c = (.*?);\s*var d = (.*?);\s*var f = (.*?);\s*var v_part = '(.*?)';"
 IiI1IiI11iII = re . compile ( ooO0o ) . findall ( page_value ) [ 0 ]
 if 44 - 44: oOoO0oo0OOOo % ii11i
 oo0ooO0 , oo000OO00Oo , IIiiiiIiIIii , O0OO , iII11I1Ii1 , I1iiiiI1iI = ( IiI1IiI11iII )
 iII11I1Ii1 = int ( iII11I1Ii1 )
 oo0ooO0 = int ( oo0ooO0 ) / iII11I1Ii1
 oo000OO00Oo = int ( oo000OO00Oo ) / iII11I1Ii1
 IIiiiiIiIIii = int ( IIiiiiIiIIii ) / iII11I1Ii1
 O0OO = int ( O0OO ) / iII11I1Ii1
 if 39 - 39: I1Ii111 + i11ii11iIi11i - ii11i - I1iII1iiII
 O0000 = 'rtmp://' + str ( oo0ooO0 ) + '.' + str ( oo000OO00Oo ) + '.' + str ( IIiiiiIiIIii ) + '.' + str ( O0OO ) + I1iiiiI1iI ;
 return O0000
 if 7 - 7: oOOO0OOooOoO0Oo . Iii1ii1II11i / I1Ii111 . I1II1 * I1I11I1I1I - i1iIi11iIIi1I
def I1 ( url , useragent = None ) :
 str = '#EXTM3U'
 str += '\n#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=361816'
 str += '\n' + url + '&bytes=0-200000'
 oOOoo00O0O = os . path . join ( O0oO , 'testfile.m3u' )
 str += '\n'
 ii1iI1II11ii ( oOOoo00O0O , str )
 if 8 - 8: IIi * iIIi1iI1II111
 return oOOoo00O0O
 if 73 - 73: I1iII1iiII / OOo / I1I11I1I1I / IiiI
def ii1iI1II11ii ( file_name , page_data , append = False ) :
 if append :
  iII11I1Ii1 = open ( file_name , 'a' )
  iII11I1Ii1 . write ( page_data )
  iII11I1Ii1 . close ( )
 else :
  iII11I1Ii1 = open ( file_name , 'wb' )
  iII11I1Ii1 . write ( page_data )
  iII11I1Ii1 . close ( )
  return ''
  if 11 - 11: Iii1ii1II11i + oOOO0OOooOoO0Oo - oOooOoO0Oo0O / IiiI
def iIIi1iI1I1IIi ( file_name ) :
 iII11I1Ii1 = open ( file_name , 'rb' )
 O0OO = iII11I1Ii1 . read ( )
 iII11I1Ii1 . close ( )
 return O0OO
 if 77 - 77: IIi / oOoO0oo0OOOo + IIi % I1iII1iiII - i11ii11iIi11i * i11ii11iIi11i
def I1oO0ooOoO ( page_data ) :
 import re , base64 , urllib ;
 ooO0000o00O = page_data
 while 'geh(' in ooO0000o00O :
  if ooO0000o00O . startswith ( 'lol(' ) : ooO0000o00O = ooO0000o00O [ 5 : - 1 ]
  if 91 - 91: I1I11I1I1I / iIIi1iI1II111 - OooO0OO . i11ii11iIi11i
  ooO0000o00O = re . compile ( '"(.*?)"' ) . findall ( ooO0000o00O ) [ 0 ] ;
  ooO0000o00O = base64 . b64decode ( ooO0000o00O ) ;
  ooO0000o00O = urllib . unquote ( ooO0000o00O ) ;
 print ooO0000o00O
 return ooO0000o00O
 if 82 - 82: oOOO0OOooOoO0Oo * I1II1 / OOo
def IiiIiI ( page_data ) :
 if 23 - 23: I1I11I1I1I
 iIiiIiiIi = iII1ii1 ( page_data ) ;
 i1iiIIIi = '(http.*)'
 import uuid
 Oo0o = str ( uuid . uuid1 ( ) ) . upper ( )
 oOOoOoo0O0 = re . compile ( i1iiIIIi ) . findall ( iIiiIiiIi )
 i1i1ii1111i1i = [ ( 'X-Playback-Session-Id' , Oo0o ) ]
 for iIiI in oOOoOoo0O0 :
  try :
   ii1iIIiii1 = iII1ii1 ( iIiI , headers = i1i1ii1111i1i ) ;
   if 62 - 62: I1II1
  except : pass
  if 1 - 1: oOOO0OOooOoO0Oo / oOOO0OOooOoO0Oo - O0O0OO0O0O0
 return page_data + '|&X-Playback-Session-Id=' + Oo0o
 if 87 - 87: oOoO0oo0OOOo / iIIi1iI1II111 * oOOO0OOooOoO0Oo / I1iII1iiII
 if 19 - 19: II + I11i11Ii . i11ii11iIi11i - oOoO0oo0OOOo
def iIi1I1 ( page_data ) :
 if 63 - 63: iIii1 * I1Ii111 . oOooOoO0Oo0O / I1II1 * oOoO0oo0OOOo . IIi
 if page_data . startswith ( 'http://dag.total-stream.net' ) :
  i1i1ii1111i1i = [ ( 'User-Agent' , 'Verismo-BlackUI_(2.4.7.5.8.0.34)' ) ]
  page_data = iII1ii1 ( page_data , headers = i1i1ii1111i1i ) ;
  if 62 - 62: I11i11Ii / IIi . i11ii11iIi11i * I1iII1iiII
 if '127.0.0.1' in page_data :
  return i11i1Ii1 ( page_data )
 elif O0ooO0Oo00o ( page_data , 'wmsAuthSign%3D([^%&]+)' ) != '' :
  o0oO0oo0000OO = O0ooO0Oo00o ( page_data , '&ver_t=([^&]+)&' ) + '?wmsAuthSign=' + O0ooO0Oo00o ( page_data , 'wmsAuthSign%3D([^%&]+)' ) + '==/mp4:' + O0ooO0Oo00o ( page_data , '\\?y=([^&]+)&' )
 else :
  o0oO0oo0000OO = O0ooO0Oo00o ( page_data , 'href="([^"]+)"[^"]+$' )
  if len ( o0oO0oo0000OO ) == 0 :
   o0oO0oo0000OO = page_data
 o0oO0oo0000OO = o0oO0oo0000OO . replace ( ' ' , '%20' )
 return o0oO0oo0000OO
 if 45 - 45: II * OooO0OO / oOooOoO0Oo0O . OOo % I1Ii111 / I11i11Ii
def O0ooO0Oo00o ( data , re_patten ) :
 II1 = ''
 III1I1Iii1iiI = re . search ( re_patten , data )
 if III1I1Iii1iiI != None :
  II1 = III1I1Iii1iiI . group ( 1 )
 else :
  II1 = ''
 return II1
 if 24 - 24: I1II1 + I1iII1iiII + I1I11I1I1I - oOOO0OOooOoO0Oo + Iii1ii1II11i
def i11i1Ii1 ( page_data ) :
 o0oO0oo0000OO = ''
 if '127.0.0.1' in page_data :
  o0oO0oo0000OO = O0ooO0Oo00o ( page_data , '&ver_t=([^&]+)&' ) + ' live=true timeout=15 playpath=' + O0ooO0Oo00o ( page_data , '\\?y=([a-zA-Z0-9-_\\.@]+)' )
  if 14 - 14: OooO0OO . O0O0OO0O0O0
 if O0ooO0Oo00o ( page_data , 'token=([^&]+)&' ) != '' :
  o0oO0oo0000OO = o0oO0oo0000OO + '?token=' + O0ooO0Oo00o ( page_data , 'token=([^&]+)&' )
 elif O0ooO0Oo00o ( page_data , 'wmsAuthSign%3D([^%&]+)' ) != '' :
  o0oO0oo0000OO = O0ooO0Oo00o ( page_data , '&ver_t=([^&]+)&' ) + '?wmsAuthSign=' + O0ooO0Oo00o ( page_data , 'wmsAuthSign%3D([^%&]+)' ) + '==/mp4:' + O0ooO0Oo00o ( page_data , '\\?y=([^&]+)&' )
 else :
  o0oO0oo0000OO = O0ooO0Oo00o ( page_data , 'HREF="([^"]+)"' )
  if 27 - 27: IIi % iIIi1iI1II111 % II
 if 'dag1.asx' in o0oO0oo0000OO :
  return iIi1I1 ( o0oO0oo0000OO )
  if 99 - 99: i11ii11iIi11i + I11i11Ii + O0O0OO0O0O0 + oOoO0oo0OOOo % OOo / I1I11I1I1I
 if 'devinlivefs.fplive.net' not in o0oO0oo0000OO :
  o0oO0oo0000OO = o0oO0oo0000OO . replace ( 'devinlive' , 'flive' )
 if 'permlivefs.fplive.net' not in o0oO0oo0000OO :
  o0oO0oo0000OO = o0oO0oo0000OO . replace ( 'permlive' , 'flive' )
 return o0oO0oo0000OO
 if 60 - 60: OooO0OO * Iii1ii1II11i - O0O0OO0O0O0 % IIi
 if 52 - 52: I1Ii111 % OOo - O0O0OO0O0O0
def i1IIII1I ( str_eval ) :
 o00oOOoO0oO = ""
 try :
  I11iiIIII1I1 = "w,i,s,e=(" + str_eval + ')'
  exec ( I11iiIIII1I1 )
  o00oOOoO0oO = i1IIi1i1Ii1 ( w , iiI1 , ooO0000o00O , e )
 except : traceback . print_exc ( file = sys . stdout )
 if 45 - 45: ii11i . OOo / Iii1ii1II11i / oOOO0OOooOoO0Oo
 return o00oOOoO0oO
 if 55 - 55: oOOO0OOooOoO0Oo
def i1IIi1i1Ii1 ( w , i , s , e ) :
 IIiIiII = 0 ;
 Oo = 0 ;
 o00o0oOo0O0O = 0 ;
 oO0ooOO = [ ] ;
 iii1iII1 = [ ] ;
 while True :
  if ( IIiIiII < 5 ) :
   iii1iII1 . append ( w [ IIiIiII ] )
  elif ( IIiIiII < len ( w ) ) :
   oO0ooOO . append ( w [ IIiIiII ] ) ;
  IIiIiII += 1 ;
  if ( Oo < 5 ) :
   iii1iII1 . append ( i [ Oo ] )
  elif ( Oo < len ( i ) ) :
   oO0ooOO . append ( i [ Oo ] )
  Oo += 1 ;
  if ( o00o0oOo0O0O < 5 ) :
   iii1iII1 . append ( s [ o00o0oOo0O0O ] )
  elif ( o00o0oOo0O0O < len ( s ) ) :
   oO0ooOO . append ( s [ o00o0oOo0O0O ] ) ;
  o00o0oOo0O0O += 1 ;
  if ( len ( w ) + len ( i ) + len ( s ) + len ( e ) == len ( oO0ooOO ) + len ( iii1iII1 ) + len ( e ) ) :
   break ;
   if 62 - 62: I1I11I1I1I
 O000oOo = '' . join ( oO0ooOO )
 OoOOOO = '' . join ( iii1iII1 )
 Oo = 0 ;
 I1iiIi111I = [ ] ;
 for IIiIiII in range ( 0 , len ( oO0ooOO ) , 2 ) :
  if 34 - 34: O0O0OO0O0O0 - i1iIi11iIIi1I / i11ii11iIi11i % I1iII1iiII
  iI1IiiiI11 = - 1 ;
  if ( ord ( OoOOOO [ Oo ] ) % 2 ) :
   iI1IiiiI11 = 1 ;
   if 80 - 80: OOo + I1iII1iiII * OooO0OO + IiiI
  I1iiIi111I . append ( chr ( int ( O000oOo [ IIiIiII : IIiIiII + 2 ] , 36 ) - iI1IiiiI11 ) ) ;
  Oo += 1 ;
  if ( Oo >= len ( iii1iII1 ) ) :
   Oo = 0 ;
 O0000 = '' . join ( I1iiIi111I )
 if 'eval(function(w,i,s,e)' in O0000 :
  if 75 - 75: I1I11I1I1I / I1iII1iiII / I1II1 / oOOO0OOooOoO0Oo % IIi + i1iIi11iIIi1I
  O0000 = re . compile ( 'eval\(function\(w,i,s,e\).*}\((.*?)\)' ) . findall ( O0000 ) [ 0 ]
  return i1IIII1I ( O0000 )
 else :
  if 4 - 4: iIii1 - oOoO0oo0OOOo - oOOO0OOooOoO0Oo - I1I11I1I1I % O0O0OO0O0O0 / IiiI
  return O0000
  if 50 - 50: IIi + I11i11Ii
def iIIi1IIi ( page_value , regex_for_text = '' , iterations = 1 , total_iteration = 1 ) :
 try :
  i11IiIIi11I = None
  if page_value . startswith ( "http" ) :
   page_value = iII1ii1 ( page_value )
   if 78 - 78: oOOO0OOooOoO0Oo
  if regex_for_text and len ( regex_for_text ) > 0 :
   try :
    page_value = re . compile ( regex_for_text ) . findall ( page_value ) [ 0 ]
   except : return 'NOTPACKED'
   if 83 - 83: ii11i % Iii1ii1II11i % I1iII1iiII % II . I1Ii111 % iIIi1iI1II111
  page_value = iIiIi1ii ( page_value , iterations , total_iteration )
 except :
  page_value = 'UNPACKEDFAILED'
  traceback . print_exc ( file = sys . stdout )
  if 28 - 28: ii11i + ii11i
 if 'sav1live.tv' in page_value :
  page_value = page_value . replace ( 'sav1live.tv' , 'sawlive.tv' )
  if 28 - 28: OOo
 return page_value
 if 52 - 52: i11ii11iIi11i + ii11i
def iIiIi1ii ( sJavascript , iteration = 1 , totaliterations = 2 ) :
 if 71 - 71: iIIi1iI1II111 / OOo
 if sJavascript . startswith ( 'var _0xcb8a=' ) :
  iI1iiII11I = sJavascript . split ( 'var _0xcb8a=' )
  I11iiIIII1I1 = "myarray=" + iI1iiII11I [ 1 ] . split ( "eval(" ) [ 0 ]
  exec ( I11iiIIII1I1 )
  I1I11Ii11I = 62
  IIii1I1I1I = int ( iI1iiII11I [ 1 ] . split ( ",62," ) [ 1 ] . split ( ',' ) [ 0 ] )
  OoOOOo0 = myarray [ 0 ]
  o00IIIIII1II1I = myarray [ 3 ]
  with open ( 'temp file' + str ( iteration ) + '.js' , "wb" ) as oOoOo0OOOOO :
   oOoOo0OOOOO . write ( str ( o00IIIIII1II1I ) )
   if 83 - 83: iIIi1iI1II111 * ii11i
 else :
  if 82 - 82: Iii1ii1II11i + iIIi1iI1II111 - oOOO0OOooOoO0Oo % OOo * O0O0OO0O0O0
  if "rn p}('" in sJavascript :
   iI1iiII11I = sJavascript . split ( "rn p}('" )
  else :
   iI1iiII11I = sJavascript . split ( "rn A}('" )
   if 15 - 15: I1iII1iiII
   if 39 - 39: I1II1 / I1Ii111 / i11ii11iIi11i * II
  OoOOOo0 , I1I11Ii11I , IIii1I1I1I , o00IIIIII1II1I = ( '' , '0' , '0' , '' )
  if 44 - 44: iIIi1iI1II111 + IIi . ii11i + oOoO0oo0OOOo / iIIi1iI1II111 - I1I11I1I1I
  I11iiIIII1I1 = "p1,a1,c1,k1=('" + iI1iiII11I [ 1 ] . split ( ".spli" ) [ 0 ] + ')'
  exec ( I11iiIIII1I1 )
 o00IIIIII1II1I = o00IIIIII1II1I . split ( '|' )
 iI1iiII11I = iI1iiII11I [ 1 ] . split ( "))'" )
 if 83 - 83: oOOO0OOooOoO0Oo * I1I11I1I1I / oOoO0oo0OOOo
 if 32 - 32: I1iII1iiII + Iii1ii1II11i - oOooOoO0Oo0O
 if 39 - 39: oOooOoO0Oo0O * I1II1 * iIIi1iI1II111 . I1I11I1I1I . IiiI + IIi
 if 9 - 9: Iii1ii1II11i + OOo % oOooOoO0Oo0O + I1iII1iiII
 if 56 - 56: oOooOoO0Oo0O + I1Ii111 - iIii1
 if 24 - 24: I1iII1iiII + IIi + I1I11I1I1I - ii11i
 if 49 - 49: I1I11I1I1I . IIi * Iii1ii1II11i % oOOO0OOooOoO0Oo . iIIi1iI1II111
 if 48 - 48: iIIi1iI1II111 * OooO0OO - iIIi1iI1II111 / OooO0OO + Iii1ii1II11i
 if 52 - 52: IiiI % OooO0OO * i1iIi11iIIi1I
 if 4 - 4: I1I11I1I1I % iIIi1iI1II111 - oOooOoO0Oo0O + IIi . OOo % i1iIi11iIIi1I
 if 9 - 9: i1iIi11iIIi1I * i1iIi11iIIi1I . O0O0OO0O0O0 * ii11i
 if 18 - 18: IiiI . i1iIi11iIIi1I % Iii1ii1II11i % OooO0OO
 if 87 - 87: ii11i . oOooOoO0Oo0O * Iii1ii1II11i
 if 100 - 100: IiiI / I11i11Ii - i11ii11iIi11i % OooO0OO - ii11i
 if 17 - 17: I1I11I1I1I / I1iII1iiII % oOoO0oo0OOOo
 if 71 - 71: oOOO0OOooOoO0Oo . II . IiiI
 if 68 - 68: O0O0OO0O0O0 % OOo * IiiI * oOOO0OOooOoO0Oo * i1iIi11iIIi1I + iIIi1iI1II111
 if 66 - 66: I1I11I1I1I % I1Ii111 % oOooOoO0Oo0O
 if 34 - 34: I1iII1iiII / iIii1 % iIIi1iI1II111 . IiiI . I11i11Ii
 if 29 - 29: iIIi1iI1II111 . II
 if 66 - 66: OOo * ii11i % ii11i * oOOO0OOooOoO0Oo - IIi - oOOO0OOooOoO0Oo
 if 70 - 70: II + OOo
 iii1III1i = ''
 O0OO = ''
 if 93 - 93: II + OooO0OO
 if 33 - 33: iIIi1iI1II111
 oo0oO = str ( IiIi1iI11 ( OoOOOo0 , I1I11Ii11I , IIii1I1I1I , o00IIIIII1II1I , iii1III1i , O0OO , iteration ) )
 if 11 - 11: I1Ii111
 if 26 - 26: ii11i * II - I1II1
 if 27 - 27: I1Ii111 * II - IiiI + OooO0OO * OooO0OO
 if 55 - 55: IIi
 if 82 - 82: II - I1II1 + IiiI
 if iteration >= totaliterations :
  if 64 - 64: I1iII1iiII . iIIi1iI1II111 * OooO0OO + oOooOoO0Oo0O - oOoO0oo0OOOo . oOooOoO0Oo0O
  return oo0oO
 else :
  if 70 - 70: oOoO0oo0OOOo - OOo . ii11i % I1I11I1I1I / Iii1ii1II11i - iIIi1iI1II111
  return iIiIi1ii ( oo0oO , iteration + 1 )
  if 55 - 55: iIii1 - IiiI
def IiIi1iI11 ( p , a , c , k , e , d , iteration , v = 1 ) :
 if 100 - 100: iIIi1iI1II111
 if 79 - 79: ii11i
 if 81 - 81: I1II1 + ii11i * II - ii11i . I1II1
 while ( c >= 1 ) :
  c = c - 1
  if ( k [ c ] ) :
   I1ii = str ( oO0o ( c , a ) )
   if v == 1 :
    p = re . sub ( '\\b' + I1ii + '\\b' , k [ c ] , p )
   else :
    p = I1I1 ( p , I1ii , k [ c ] )
    if 99 - 99: IIi / ii11i - OooO0OO * I1Ii111 % i11ii11iIi11i
    if 13 - 13: IiiI
    if 70 - 70: II + iIIi1iI1II111 . OOo * OooO0OO
    if 2 - 2: oOooOoO0Oo0O . I1II1 . oOOO0OOooOoO0Oo
    if 42 - 42: I1II1 % OOo / IiiI - OOo * O0O0OO0O0O0
    if 19 - 19: OOo * i11ii11iIi11i % O0O0OO0O0O0
 return p
 if 24 - 24: I1iII1iiII
 if 10 - 10: I1iII1iiII % OooO0OO / I1II1
 if 28 - 28: I1II1 % IIi
def I1I1 ( source_str , word_to_find , replace_with ) :
 iiIiII11i1 = None
 iiIiII11i1 = source_str . split ( word_to_find )
 if len ( iiIiII11i1 ) > 1 :
  oOo00Ooo0o0 = [ ]
  i1IiII1i1I = 0
  for iI1ii1ii1I in iiIiII11i1 :
   if 18 - 18: OOo * OOo % OOo
   oOo00Ooo0o0 . append ( iI1ii1ii1I )
   ii111i = word_to_find
   if 17 - 17: iIIi1iI1II111 * Iii1ii1II11i * I1Ii111 * i1iIi11iIIi1I * I1I11I1I1I % I11i11Ii
   if 33 - 33: I1Ii111 * I1Ii111 . IIi . O0O0OO0O0O0
   if i1IiII1i1I == len ( iiIiII11i1 ) - 1 :
    ii111i = ''
   else :
    if len ( iI1ii1ii1I ) == 0 :
     if ( len ( iiIiII11i1 [ i1IiII1i1I + 1 ] ) == 0 and word_to_find [ 0 ] . lower ( ) not in 'abcdefghijklmnopqrstuvwxyz1234567890_' ) or ( len ( iiIiII11i1 [ i1IiII1i1I + 1 ] ) > 0 and iiIiII11i1 [ i1IiII1i1I + 1 ] [ 0 ] . lower ( ) not in 'abcdefghijklmnopqrstuvwxyz1234567890_' ) :
      ii111i = replace_with
      if 48 - 48: I1iII1iiII . OooO0OO + Iii1ii1II11i % I1Ii111 / O0O0OO0O0O0
    else :
     if ( iiIiII11i1 [ i1IiII1i1I ] [ - 1 ] . lower ( ) not in 'abcdefghijklmnopqrstuvwxyz1234567890_' ) and ( ( len ( iiIiII11i1 [ i1IiII1i1I + 1 ] ) == 0 and word_to_find [ 0 ] . lower ( ) not in 'abcdefghijklmnopqrstuvwxyz1234567890_' ) or ( len ( iiIiII11i1 [ i1IiII1i1I + 1 ] ) > 0 and iiIiII11i1 [ i1IiII1i1I + 1 ] [ 0 ] . lower ( ) not in 'abcdefghijklmnopqrstuvwxyz1234567890_' ) ) :
      ii111i = replace_with
      if 74 - 74: i1iIi11iIIi1I . iIIi1iI1II111 - i11ii11iIi11i + oOOO0OOooOoO0Oo % O0O0OO0O0O0 % Iii1ii1II11i
   oOo00Ooo0o0 . append ( ii111i )
   i1IiII1i1I += 1
   if 78 - 78: OooO0OO + Iii1ii1II11i + oOOO0OOooOoO0Oo - oOOO0OOooOoO0Oo . O0O0OO0O0O0 / IiiI
  source_str = '' . join ( oOo00Ooo0o0 )
 return source_str
 if 27 - 27: OooO0OO - iIIi1iI1II111 % I1I11I1I1I * II . oOOO0OOooOoO0Oo % ii11i
def IiIi1i ( num , radix ) :
 if 99 - 99: Iii1ii1II11i . II
 i1i1ii = ""
 if num == 0 : return '0'
 while num > 0 :
  i1i1ii = "0123456789abcdefghijklmnopqrstuvwxyz" [ num % radix ] + i1i1ii
  num /= radix
 return i1i1ii
 if 59 - 59: I1I11I1I1I / oOoO0oo0OOOo / I1II1 / iIIi1iI1II111 / Iii1ii1II11i + I1iII1iiII
def oO0o ( cc , a ) :
 I1ii = "" if cc < a else oO0o ( int ( cc / a ) , a )
 cc = ( cc % a )
 IIiI1111i1 = chr ( cc + 29 ) if cc > 35 else str ( IiIi1i ( cc , 36 ) )
 return I1ii + IIiI1111i1
 if 46 - 46: oOOO0OOooOoO0Oo
 if 29 - 29: i1iIi11iIIi1I . Iii1ii1II11i % I1iII1iiII * i1iIi11iIIi1I - I1iII1iiII * ii11i
def iIIIII1iiiiII ( cookieJar ) :
 try :
  iii1i1III = ""
  for o000o , o00Ooo0oo in enumerate ( cookieJar ) :
   iii1i1III += o00Ooo0oo . name + "=" + o00Ooo0oo . value + ";"
 except : pass
 if 49 - 49: O0O0OO0O0O0 % Iii1ii1II11i + II . i1iIi11iIIi1I % iIii1 * I1II1
 return iii1i1III
 if 67 - 67: I11i11Ii
 if 5 - 5: i1iIi11iIIi1I . oOooOoO0Oo0O
def i1III ( cookieJar , COOKIEFILE ) :
 try :
  IiIii1i111 = os . path . join ( O0oO , COOKIEFILE )
  cookieJar . save ( IiIii1i111 , ignore_discard = True )
 except : pass
 if 57 - 57: i11ii11iIi11i
def I1ii11 ( COOKIEFILE ) :
 if 35 - 35: oOooOoO0Oo0O - II / IiiI
 iii11i1 = None
 if COOKIEFILE :
  try :
   IiIii1i111 = os . path . join ( O0oO , COOKIEFILE )
   iii11i1 = cookielib . LWPCookieJar ( )
   iii11i1 . load ( IiIii1i111 , ignore_discard = True )
  except :
   iii11i1 = None
   if 48 - 48: IIi * I1Ii111
 if not iii11i1 :
  iii11i1 = cookielib . LWPCookieJar ( )
  if 15 - 15: IiiI * I1I11I1I1I % ii11i * I1Ii111
 return iii11i1
 if 31 - 31: IiiI * iIIi1iI1II111 . OOo
def ooOOOoO ( fun_call , page_data , Cookie_Jar , m ) :
 oooOO0oOooO00 = ''
 if 37 - 37: oOOO0OOooOoO0Oo
 if i1111 not in sys . path :
  sys . path . append ( i1111 )
  if 37 - 37: oOoO0oo0OOOo / oOOO0OOooOoO0Oo * iIIi1iI1II111
  if 73 - 73: iIii1 * iIii1 / IIi
 try :
  IIii1i11iI1II11 = 'import ' + fun_call . split ( '.' ) [ 0 ]
  if 14 - 14: I1Ii111 + O0O0OO0O0O0
  exec ( IIii1i11iI1II11 )
  if 83 - 83: I1Ii111 / O0O0OO0O0O0 + i1iIi11iIIi1I . iIii1 * I1II1 + oOOO0OOooOoO0Oo
 except :
  if 42 - 42: I11i11Ii % i1iIi11iIIi1I . IIi
  traceback . print_exc ( file = sys . stdout )
  if 7 - 7: I1Ii111 - OOo * I1II1 + I1iII1iiII . I1Ii111
 exec ( 'ret_val=' + fun_call )
 if 85 - 85: iIIi1iI1II111
 if 32 - 32: oOooOoO0Oo0O . IiiI / oOoO0oo0OOOo * I1iII1iiII / I1iII1iiII * OooO0OO
 try :
  return str ( oooOO0oOooO00 )
 except : return oooOO0oOooO00
 if 19 - 19: OooO0OO
def oO0O ( fun_call , page_data , Cookie_Jar , m ) :
 if 55 - 55: I1II1 % I1II1 / iIIi1iI1II111 % iIii1 - I1iII1iiII . oOoO0oo0OOOo
 oooOO0oOooO00 = ''
 if i1111 not in sys . path :
  sys . path . append ( i1111 )
  if 49 - 49: ii11i * I11i11Ii . oOooOoO0Oo0O
 iII11I1Ii1 = open ( os . path . join ( i1111 , 'LSProdynamicCode.py' ) , "wb" )
 iII11I1Ii1 . write ( "# -*- coding: utf-8 -*-\n" )
 iII11I1Ii1 . write ( fun_call . encode ( "utf-8" ) ) ;
 if 90 - 90: I1iII1iiII % I1Ii111 - ii11i % Iii1ii1II11i
 iII11I1Ii1 . close ( )
 import LSProdynamicCode
 oooOO0oOooO00 = LSProdynamicCode . GetLSProData ( page_data , Cookie_Jar , m )
 try :
  return str ( oooOO0oOooO00 )
 except : return oooOO0oOooO00
 if 8 - 8: Iii1ii1II11i * oOoO0oo0OOOo / oOOO0OOooOoO0Oo % OooO0OO - i11ii11iIi11i
 if 71 - 71: iIii1
def Iii ( captchakey , cj , type = 1 ) :
 if 14 - 14: I1II1
 if 79 - 79: OooO0OO
 if 76 - 76: ii11i
 Ooi111i1iIi1 = ""
 OoO0oO = ""
 if 10 - 10: I11i11Ii . i1iIi11iIIi1I / I1iII1iiII * IIi
 if 10 - 10: I1I11I1I1I - oOoO0oo0OOOo
 if 59 - 59: oOooOoO0Oo0O * oOoO0oo0OOOo + I11i11Ii
 if 23 - 23: IIi
 if 13 - 13: ii11i
 OooooOo0 = False
 I1ii1 = None
 OoO0oO = None
 if len ( captchakey ) > 0 :
  I1Ii = captchakey
  if not I1Ii . startswith ( 'http' ) :
   I1Ii = 'http://www.google.com/recaptcha/api/challenge?k=' + I1Ii + '&ajax=1'
   if 44 - 44: ii11i . I1Ii111 + II . IIi
  OooooOo0 = True
  if 7 - 7: I1Ii111 + ii11i * I1I11I1I1I * I1I11I1I1I / i1iIi11iIIi1I - OooO0OO
  oOOOo0o = 'challenge.*?\'(.*?)\''
  iiiii11I1 = '\'(.*?)\''
  Ii1OOOo = iII1ii1 ( I1Ii , cookieJar = cj )
  Ooi111i1iIi1 = re . findall ( oOOOo0o , Ii1OOOo ) [ 0 ]
  I1iI1IiI = 'http://www.google.com/recaptcha/api/reload?c=' ;
  i1i1Ii1I = I1Ii . split ( 'k=' ) [ 1 ]
  I1iI1IiI += Ooi111i1iIi1 + '&k=' + i1i1Ii1I + '&reason=i&type=image&lang=en'
  I1II1III1 = iII1ii1 ( I1iI1IiI , cookieJar = cj )
  I1ii1 = re . findall ( iiiii11I1 , I1II1III1 ) [ 0 ]
  oooo0O0o0OoOO = 'http://www.google.com/recaptcha/api/image?c=' + I1ii1
  if not oooo0O0o0OoOO . startswith ( "http" ) :
   oooo0O0o0OoOO = 'http://www.google.com/recaptcha/api/' + oooo0O0o0OoOO
  import random
  OoOOOo0o0ooo = random . randrange ( 100 , 1000 , 5 )
  III1iiiI1I = os . path . join ( O0oO , str ( OoOOOo0o0ooo ) + "captcha.img" )
  oO0OOO0o0O = open ( III1iiiI1I , "wb" )
  oO0OOO0o0O . write ( iII1ii1 ( oooo0O0o0OoOO , cookieJar = cj ) )
  oO0OOO0o0O . close ( )
  OOOOO0 = Ooo0Oo0o ( captcha = III1iiiI1I )
  OoO0oO = OOOOO0 . get ( )
  os . remove ( III1iiiI1I )
  if 85 - 85: i11ii11iIi11i
 if I1ii1 :
  if type == 1 :
   return 'recaptcha_challenge_field=' + urllib . quote_plus ( I1ii1 ) + '&recaptcha_response_field=' + urllib . quote_plus ( OoO0oO )
  elif type == 2 :
   return 'recaptcha_challenge_field:' + I1ii1 + ',recaptcha_response_field:' + OoO0oO
  else :
   return 'recaptcha_challenge_field=' + urllib . quote_plus ( I1ii1 ) + '&recaptcha_response_field=' + urllib . quote_plus ( OoO0oO )
 else :
  return ''
  if 7 - 7: I11i11Ii + I1II1 % iIii1 / I1iII1iiII + I11i11Ii
  if 41 - 41: OooO0OO + O0O0OO0O0O0 / oOOO0OOooOoO0Oo % I1Ii111
def iII1ii1 ( url , cookieJar = None , post = None , timeout = 20 , headers = None , noredir = False ) :
 if 22 - 22: Iii1ii1II11i % I1iII1iiII * OooO0OO - I1Ii111 + I1iII1iiII - oOoO0oo0OOOo
 if 15 - 15: I1II1
 oO0o00oOOooO0 = urllib2 . HTTPCookieProcessor ( cookieJar )
 if 31 - 31: iIii1 / I11i11Ii . IiiI
 if noredir :
  o00oO = urllib2 . build_opener ( iiiii , oO0o00oOOooO0 , urllib2 . HTTPBasicAuthHandler ( ) , urllib2 . HTTPHandler ( ) )
 else :
  o00oO = urllib2 . build_opener ( oO0o00oOOooO0 , urllib2 . HTTPBasicAuthHandler ( ) , urllib2 . HTTPHandler ( ) )
  if 83 - 83: OOo / ii11i + I11i11Ii / iIii1
 II1111II = urllib2 . Request ( url )
 II1111II . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36' )
 if headers :
  for o0ooO , IIiiii1 in headers :
   II1111II . add_header ( o0ooO , IIiiii1 )
   if 66 - 66: IIi * Iii1ii1II11i
 II1IiiIii = o00oO . open ( II1111II , post , timeout = timeout )
 iIIIii = II1IiiIii . read ( )
 II1IiiIii . close ( )
 return iIIIii ;
 if 2 - 2: OOo . II * oOoO0oo0OOOo + iIIi1iI1II111 - I1I11I1I1I * ii11i
def II111i1ii1iII ( str , reg = None ) :
 if reg :
  str = re . findall ( reg , str ) [ 0 ]
 ooo0OoO = urllib . unquote ( str [ 0 : len ( str ) - 1 ] ) ;
 iiI1111I11i1I = '' ;
 for iiI1 in range ( len ( ooo0OoO ) ) :
  iiI1111I11i1I += chr ( ord ( ooo0OoO [ iiI1 ] ) - ooo0OoO [ len ( ooo0OoO ) - 1 ] ) ;
 iiI1111I11i1I = urllib . unquote ( iiI1111I11i1I )
 if 85 - 85: I1II1 * I11i11Ii % i11ii11iIi11i - IIi
 return iiI1111I11i1I
 if 37 - 37: oOOO0OOooOoO0Oo . oOoO0oo0OOOo * oOoO0oo0OOOo * i1iIi11iIIi1I * iIIi1iI1II111
def iii ( str ) :
 o00O = re . findall ( 'unescape\(\'(.*?)\'' , str )
 if 88 - 88: O0O0OO0O0O0 + iIii1 * Iii1ii1II11i * iIii1 + I1I11I1I1I
 if ( not o00O == None ) and len ( o00O ) > 0 :
  for O0OOO00OooO in o00O :
   if 64 - 64: IiiI . i11ii11iIi11i - oOooOoO0Oo0O . IIi - iIii1
   str = str . replace ( O0OOO00OooO , urllib . unquote ( O0OOO00OooO ) )
 return str
 if 77 - 77: OooO0OO % Iii1ii1II11i / i1iIi11iIIi1I % iIii1 % oOooOoO0Oo0O % IiiI
I1i11II11i1iI = 0
def O00OO0oO ( m , html_page , cookieJar ) :
 global I1i11II11i1iI
 I1i11II11i1iI += 1
 iI1I1I1i1i = m [ 'expres' ]
 ooo0 = m [ 'page' ]
 OOo0O = re . compile ( '\$LiveStreamCaptcha\[([^\]]*)\]' ) . findall ( iI1I1I1i1i ) [ 0 ]
 if 100 - 100: IiiI % IiiI
 I1Ii = re . compile ( OOo0O ) . findall ( html_page ) [ 0 ]
 if 15 - 15: OOo / II
 if not I1Ii . startswith ( "http" ) :
  Iiii111 = 'http://' + "" . join ( ooo0 . split ( '/' ) [ 2 : 3 ] )
  if I1Ii . startswith ( "/" ) :
   I1Ii = Iiii111 + I1Ii
  else :
   I1Ii = Iiii111 + '/' + I1Ii
   if 71 - 71: iIIi1iI1II111 / i11ii11iIi11i . II / II * IIi
 III1iiiI1I = os . path . join ( O0oO , str ( I1i11II11i1iI ) + "captcha.jpg" )
 oO0OOO0o0O = open ( III1iiiI1I , "wb" )
 if 60 - 60: i1iIi11iIIi1I . i11ii11iIi11i - oOoO0oo0OOOo + I1Ii111 * I1Ii111
 II1111II = urllib2 . Request ( I1Ii )
 II1111II . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20100101 Firefox/14.0.1' )
 if 'referer' in m :
  II1111II . add_header ( 'Referer' , m [ 'referer' ] )
 if 'agent' in m :
  II1111II . add_header ( 'User-agent' , m [ 'agent' ] )
 if 'setcookie' in m :
  if 27 - 27: oOOO0OOooOoO0Oo * i11ii11iIi11i . ii11i - ii11i
  II1111II . add_header ( 'Cookie' , m [ 'setcookie' ] )
  if 5 - 5: oOOO0OOooOoO0Oo
  if 84 - 84: i1iIi11iIIi1I * OOo * i1iIi11iIIi1I % oOOO0OOooOoO0Oo / i11ii11iIi11i
  if 100 - 100: oOOO0OOooOoO0Oo . OooO0OO - ii11i . O0O0OO0O0O0 / i1iIi11iIIi1I
  if 71 - 71: II * oOoO0oo0OOOo . I1I11I1I1I
 urllib2 . urlopen ( II1111II )
 II1IiiIii = urllib2 . urlopen ( II1111II )
 if 49 - 49: oOOO0OOooOoO0Oo * iIIi1iI1II111 . oOOO0OOooOoO0Oo
 oO0OOO0o0O . write ( II1IiiIii . read ( ) )
 II1IiiIii . close ( )
 oO0OOO0o0O . close ( )
 OOOOO0 = Ooo0Oo0o ( captcha = III1iiiI1I )
 OoO0oO = OOOOO0 . get ( )
 return OoO0oO
 if 19 - 19: i1iIi11iIIi1I - oOOO0OOooOoO0Oo
def OOOOo000o00OO ( imageregex , html_page , cookieJar , m ) :
 global I1i11II11i1iI
 I1i11II11i1iI += 1
 if 96 - 96: iIIi1iI1II111 . I1II1 % IIi + O0O0OO0O0O0 - I1II1 * IIi
 if 33 - 33: IIi % I11i11Ii - OOo . iIIi1iI1II111 / iIIi1iI1II111
 if not imageregex == '' :
  if html_page . startswith ( "http" ) :
   Iiii111 = iII1ii1 ( html_page , cookieJar = cookieJar )
  else :
   Iiii111 = html_page
  I1Ii = re . compile ( imageregex ) . findall ( html_page ) [ 0 ]
 else :
  I1Ii = html_page
  if 'oneplay.tv/embed' in html_page :
   import oneplay
   Iiii111 = iII1ii1 ( html_page , cookieJar = cookieJar )
   I1Ii = oneplay . getCaptchaUrl ( Iiii111 )
   if 96 - 96: oOooOoO0Oo0O + oOOO0OOooOoO0Oo * iIIi1iI1II111
 III1iiiI1I = os . path . join ( O0oO , str ( I1i11II11i1iI ) + "captcha.jpg" )
 oO0OOO0o0O = open ( III1iiiI1I , "wb" )
 if 86 - 86: OooO0OO
 II1111II = urllib2 . Request ( I1Ii )
 II1111II . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20100101 Firefox/14.0.1' )
 if 'referer' in m :
  II1111II . add_header ( 'Referer' , m [ 'referer' ] )
 if 'agent' in m :
  II1111II . add_header ( 'User-agent' , m [ 'agent' ] )
 if 'accept' in m :
  II1111II . add_header ( 'Accept' , m [ 'accept' ] )
 if 'setcookie' in m :
  if 29 - 29: ii11i - IiiI + i11ii11iIi11i % ii11i % I1II1
  II1111II . add_header ( 'Cookie' , m [ 'setcookie' ] )
  if 84 - 84: oOOO0OOooOoO0Oo + I1Ii111 + OooO0OO + iIii1
  if 62 - 62: O0O0OO0O0O0 + Iii1ii1II11i + I11i11Ii
  if 69 - 69: Iii1ii1II11i
  if 63 - 63: IiiI / Iii1ii1II11i * ii11i . II
  if 85 - 85: O0O0OO0O0O0 / O0O0OO0O0O0 . IiiI . iIIi1iI1II111
 II1IiiIii = urllib2 . urlopen ( II1111II )
 if 67 - 67: i1iIi11iIIi1I / I1iII1iiII . I1II1 . oOooOoO0Oo0O
 oO0OOO0o0O . write ( II1IiiIii . read ( ) )
 II1IiiIii . close ( )
 oO0OOO0o0O . close ( )
 OOOOO0 = Ooo0Oo0o ( captcha = III1iiiI1I )
 OoO0oO = OOOOO0 . get ( )
 return OoO0oO
 if 19 - 19: oOOO0OOooOoO0Oo . I1Ii111 / Iii1ii1II11i
 if 68 - 68: IIi / oOooOoO0Oo0O * I1I11I1I1I / OOo
 if 88 - 88: I1iII1iiII
 if 1 - 1: oOooOoO0Oo0O
 if 48 - 48: IIi * Iii1ii1II11i - IIi - I1II1 + I1II1
 if 40 - 40: O0O0OO0O0O0 . ii11i
 if 2 - 2: I11i11Ii * OOo - OOo + oOooOoO0Oo0O % Iii1ii1II11i / Iii1ii1II11i
 if 3 - 3: oOooOoO0Oo0O
 if 71 - 71: oOOO0OOooOoO0Oo + I11i11Ii - iIii1 - O0O0OO0O0O0 . I1I11I1I1I - IIi
 if 85 - 85: I1Ii111 - Iii1ii1II11i / I1Ii111 + I1II1 - iIii1
 if 49 - 49: IiiI - iIIi1iI1II111 / IiiI * Iii1ii1II11i + II
 if 35 - 35: i1iIi11iIIi1I . i11ii11iIi11i / I11i11Ii / i11ii11iIi11i * OOo
 if 85 - 85: i1iIi11iIIi1I . IIi % I1II1 % I1I11I1I1I
def OOo00ooOoO0o ( name , headname ) :
 if 21 - 21: O0O0OO0O0O0
 if 89 - 89: iIii1 . O0O0OO0O0O0 * iIIi1iI1II111
 Iiii1 = xbmc . Keyboard ( 'default' , 'heading' , True )
 Iiii1 . setDefault ( name )
 Iiii1 . setHeading ( headname )
 Iiii1 . setHiddenInput ( False )
 return Iiii1 . getText ( )
 if 27 - 27: I1II1
 if 52 - 52: II % Iii1ii1II11i + ii11i * OOo . OooO0OO
 if 95 - 95: ii11i . oOOO0OOooOoO0Oo - oOooOoO0Oo0O * IiiI / I1iII1iiII
 if 74 - 74: OOo
class Ooo0Oo0o ( xbmcgui . WindowDialog ) :
 def __init__ ( self , * args , ** kwargs ) :
  self . cptloc = kwargs . get ( 'captcha' )
  self . img = xbmcgui . ControlImage ( 335 , 30 , 624 , 60 , self . cptloc )
  self . addControl ( self . img )
  self . kbd = xbmc . Keyboard ( )
  if 34 - 34: iIii1
 def get ( self ) :
  self . show ( )
  time . sleep ( 2 )
  self . kbd . doModal ( )
  if ( self . kbd . isConfirmed ( ) ) :
   ii1IIiI1IIi = self . kbd . getText ( )
   self . close ( )
   return ii1IIiI1IIi
  self . close ( )
  return False
  if 76 - 76: iIii1 / IiiI + Iii1ii1II11i
def O0ooooo0OOOO0 ( ) :
 import time
 return str ( int ( time . time ( ) * 1000 ) )
 if 86 - 86: O0O0OO0O0O0 + O0O0OO0O0O0 . II % i11ii11iIi11i . IIi
def I1i111iiIIIi ( ) :
 import time
 return str ( int ( time . time ( ) ) )
 if 17 - 17: OooO0OO
def OoO0OOoO0Oo0 ( ) :
 oO00O = [ ]
 II111IiiiI1 = sys . argv [ 2 ]
 if len ( II111IiiiI1 ) >= 2 :
  oooOO0oo0Oo00 = sys . argv [ 2 ]
  oOoOiI111I1III = oooOO0oo0Oo00 . replace ( '?' , '' )
  if ( oooOO0oo0Oo00 [ len ( oooOO0oo0Oo00 ) - 1 ] == '/' ) :
   oooOO0oo0Oo00 = oooOO0oo0Oo00 [ 0 : len ( oooOO0oo0Oo00 ) - 2 ]
  i111IiiI1Ii = oOoOiI111I1III . split ( '&' )
  oO00O = { }
  for iiI1 in range ( len ( i111IiiI1Ii ) ) :
   OooOOOOOo = { }
   OooOOOOOo = i111IiiI1Ii [ iiI1 ] . split ( '=' )
   if ( len ( OooOOOOOo ) ) == 2 :
    oO00O [ OooOOOOOo [ 0 ] ] = OooOOOOOo [ 1 ]
 return oO00O
 if 50 - 50: II + IIi + iIii1
 if 15 - 15: I1I11I1I1I
def IiiI11I1IIiI ( ) :
 oO0Oo0O0o = json . loads ( open ( oo00 ) . read ( ) )
 o0oO00000 = len ( oO0Oo0O0o )
 for iiI1 in oO0Oo0O0o :
  Oo0OoO00oOO0o = iiI1 [ 0 ]
  O00O0oOO00O00 = iiI1 [ 1 ]
  i1iI1i = iiI1 [ 2 ]
  try :
   OOooo0O00o = iiI1 [ 3 ]
   if OOooo0O00o == None :
    raise
  except :
   if Ooo0OO0oOO . getSetting ( 'use_thumb' ) == "true" :
    OOooo0O00o = i1iI1i
   else :
    OOooo0O00o = ii1I1i1I
  try : oo000O0OoooO = iiI1 [ 5 ]
  except : oo000O0OoooO = None
  try : oOo0oO = iiI1 [ 6 ]
  except : oOo0oO = None
  if 59 - 59: oOOO0OOooOoO0Oo
  if iiI1 [ 4 ] == 0 :
   I1i1Iiiii ( O00O0oOO00O00 , Oo0OoO00oOO0o , i1iI1i , OOooo0O00o , '' , '' , '' , 'fav' , oo000O0OoooO , oOo0oO , o0oO00000 )
  else :
   o0oo0o0O00OO ( Oo0OoO00oOO0o , O00O0oOO00O00 , iiI1 [ 4 ] , i1iI1i , ii1I1i1I , '' , '' , '' , '' , 'fav' )
   if 89 - 89: Iii1ii1II11i % ii11i
   if 35 - 35: I1Ii111 + II - Iii1ii1II11i % OOo % I1iII1iiII % Iii1ii1II11i
def ii1IIiII111I ( name , url , iconimage , fanart , mode , playlist = None , regexs = None ) :
 O00OoOoO = [ ]
 try :
  if 58 - 58: I1Ii111
  name = name . encode ( 'utf-8' , 'ignore' )
 except :
  pass
 if os . path . exists ( oo00 ) == False :
  OO0O00 ( 'Making Favorites File' )
  O00OoOoO . append ( ( name , url , iconimage , fanart , mode , playlist , regexs ) )
  oo0ooO0 = open ( oo00 , "w" )
  oo0ooO0 . write ( json . dumps ( O00OoOoO ) )
  oo0ooO0 . close ( )
 else :
  OO0O00 ( 'Appending Favorites' )
  oo0ooO0 = open ( oo00 ) . read ( )
  O0o0Oo = json . loads ( oo0ooO0 )
  O0o0Oo . append ( ( name , url , iconimage , fanart , mode ) )
  oo000OO00Oo = open ( oo00 , "w" )
  oo000OO00Oo . write ( json . dumps ( O0o0Oo ) )
  oo000OO00Oo . close ( )
  if 19 - 19: ii11i * oOooOoO0Oo0O * O0O0OO0O0O0
  if 79 - 79: oOOO0OOooOoO0Oo % IiiI
def Oo0oOO ( name ) :
 O0o0Oo = json . loads ( open ( oo00 ) . read ( ) )
 for o000o in range ( len ( O0o0Oo ) ) :
  if O0o0Oo [ o000o ] [ 0 ] == name :
   del O0o0Oo [ o000o ]
   oo000OO00Oo = open ( oo00 , "w" )
   oo000OO00Oo . write ( json . dumps ( O0o0Oo ) )
   oo000OO00Oo . close ( )
   break
 xbmc . executebuiltin ( "XBMC.Container.Refresh" )
 if 86 - 86: ii11i / iIIi1iI1II111
def iiiIi ( url ) :
 import urlresolver
 ooiiI1ii = urlresolver . HostedMediaFile ( url )
 if ooiiI1ii :
  i11II1I11I1 = urlresolver . resolve ( url )
  O0OooOO = i11II1I11I1
  if isinstance ( O0OooOO , list ) :
   for iI1I in O0OooOO :
    i1i1 = Ooo0OO0oOO . getSetting ( 'quality' )
    if iI1I [ 'quality' ] == 'HD' :
     i11II1I11I1 = iI1I [ 'url' ]
     break
    elif iI1I [ 'quality' ] == 'SD' :
     i11II1I11I1 = iI1I [ 'url' ]
    elif iI1I [ 'quality' ] == '1080p' and Ooo0OO0oOO . getSetting ( '1080pquality' ) == 'true' :
     i11II1I11I1 = iI1I [ 'url' ]
     break
  else :
   i11II1I11I1 = O0OooOO
 else :
  xbmc . executebuiltin ( "XBMC.Notification(probando,Urlresolver donot support this domain. - ,5000)" )
  i11II1I11I1 = url
 return i11II1I11I1
def o0oOoOo0 ( url , listitem , pdialogue = None ) :
 if 38 - 38: I1iII1iiII % II + O0O0OO0O0O0 + iIii1 + IIi / O0O0OO0O0O0
 if url . lower ( ) . startswith ( 'plugin' ) and 'youtube' not in url . lower ( ) :
  print 'playing via runplugin'
  xbmc . executebuiltin ( 'XBMC.RunPlugin(' + url + ')' )
  for iiI1 in range ( 8 ) :
   xbmc . sleep ( 500 )
   try :
    if 94 - 94: iIii1 - oOoO0oo0OOOo + OOo
    if xbmc . getCondVisibility ( "Player.HasMedia" ) and xbmc . Player ( ) . isPlaying ( ) :
     return True
   except : pass
  print 'returning now'
  return False
 import CustomPlayer , time
 if 59 - 59: I1I11I1I1I . i11ii11iIi11i - ii11i + ii11i
 I11I1IIiiII1 = CustomPlayer . MyXBMCPlayer ( )
 I11I1IIiiII1 . pdialogue = pdialogue
 oO0o0Oo = time . time ( )
 if 76 - 76: IIi / Iii1ii1II11i + I1Ii111
 print 'going to play'
 import time
 oOoO = time . time ( )
 I11I1IIiiII1 . play ( url , listitem )
 xbmc . sleep ( 1000 )
 if 2 - 2: O0O0OO0O0O0 - II + IiiI % I1I11I1I1I * OooO0OO
 try :
  while I11I1IIiiII1 . is_active :
   xbmc . sleep ( 400 )
   if 54 - 54: iIIi1iI1II111 - iIii1 . I1II1 % iIii1 + iIii1
   if I11I1IIiiII1 . urlplayed :
    print 'yes played'
    return True
   if time . time ( ) - oOoO > 4 : return False
   if 36 - 36: I1II1 % O0O0OO0O0O0
 except : pass
 print 'not played' , url
 return False
def Iiii1Ii ( name , mu_playlist , queueVideo = None ) :
 oo000O0OoooO = xbmc . PlayList ( xbmc . PLAYLIST_VIDEO )
 if 62 - 62: I11i11Ii % Iii1ii1II11i
 if '$$LSPlayOnlyOne$$' in mu_playlist [ 0 ] :
  mu_playlist [ 0 ] = mu_playlist [ 0 ] . replace ( '$$LSPlayOnlyOne$$' , '' )
  import urlparse
  i1ii1I1IIIII = [ ]
  OoiiI1i111 = 0
  IiiIIiiiiii = xbmcgui . DialogProgress ( )
  IiiIIiiiiii . create ( 'Progress' , 'Trying Multiple Links' )
  for iiI1 in mu_playlist :
   if 54 - 54: Iii1ii1II11i - II
   if 65 - 65: II . IIi + I1II1 / oOoO0oo0OOOo + oOOO0OOooOoO0Oo % I11i11Ii
   if '$$lsname=' in iiI1 :
    iiiiIi1 = iiI1 . split ( '$$lsname=' ) [ 1 ] . split ( '&regexs' ) [ 0 ]
    i1ii1I1IIIII . append ( iiiiIi1 )
    mu_playlist [ OoiiI1i111 ] = iiI1 . split ( '$$lsname=' ) [ 0 ] + ( '&regexs' + iiI1 . split ( '&regexs' ) [ 1 ] if '&regexs' in iiI1 else '' )
   else :
    iiiiIi1 = urlparse . urlparse ( iiI1 ) . netloc
    if iiiiIi1 == '' :
     i1ii1I1IIIII . append ( name )
    else :
     i1ii1I1IIIII . append ( iiiiIi1 )
   o000o = OoiiI1i111
   OoiiI1i111 += 1
   if 98 - 98: I11i11Ii . i11ii11iIi11i . OOo
   iIIIiiiIiI1 = i1ii1I1IIIII [ o000o ]
   if IiiIIiiiiii . iscanceled ( ) : return
   IiiIIiiiiii . update ( OoiiI1i111 / len ( mu_playlist ) * 100 , "" , "Link#%d" % ( OoiiI1i111 ) , iIIIiiiIiI1 )
   print 'auto playnamexx' , iIIIiiiIiI1
   if "&mode=19" in mu_playlist [ o000o ] :
    if 95 - 95: OooO0OO - I1Ii111 - iIIi1iI1II111 . i11ii11iIi11i . iIii1
    iIiIi1IiIi1iI = xbmcgui . ListItem ( iIIIiiiIiI1 , iconImage = i1iI1i , thumbnailImage = i1iI1i )
    iIiIi1IiIi1iI . setInfo ( type = 'Video' , infoLabels = { 'Title' : iIIIiiiIiI1 } )
    iIiIi1IiIi1iI . setProperty ( "IsPlayable" , "true" )
    o00OO0 = iiiIi ( mu_playlist [ o000o ] . replace ( '&mode=19' , '' ) . replace ( ';' , '' ) )
    iIiIi1IiIi1iI . setPath ( o00OO0 )
    if 79 - 79: oOooOoO0Oo0O / I1Ii111 . iIIi1iI1II111
    oOoO0Oo0 = o0oOoOo0 ( o00OO0 , iIiIi1IiIi1iI )
   elif "$doregex" in mu_playlist [ o000o ] :
    if 7 - 7: IIi + OooO0OO
    IiiIIiI1iI1 = mu_playlist [ o000o ] . split ( '&regexs=' )
    if 86 - 86: I11i11Ii / OooO0OO * i11ii11iIi11i
    O00O0oOO00O00 , i1II = oOOoo0000O0o0 ( IiiIIiI1iI1 [ 1 ] , IiiIIiI1iI1 [ 0 ] )
    OOoO0OOoO0ooo = O00O0oOO00O00 . replace ( ';' , '' )
    iIiIi1IiIi1iI = xbmcgui . ListItem ( iIIIiiiIiI1 , iconImage = i1iI1i , thumbnailImage = i1iI1i )
    iIiIi1IiIi1iI . setInfo ( type = 'Video' , infoLabels = { 'Title' : iIIIiiiIiI1 } )
    iIiIi1IiIi1iI . setProperty ( "IsPlayable" , "true" )
    iIiIi1IiIi1iI . setPath ( OOoO0OOoO0ooo )
    if 23 - 23: I11i11Ii - I1I11I1I1I
    oOoO0Oo0 = o0oOoOo0 ( OOoO0OOoO0ooo , iIiIi1IiIi1iI )
    if 96 - 96: I11i11Ii % oOooOoO0Oo0O
   else :
    O00O0oOO00O00 = mu_playlist [ o000o ]
    O00O0oOO00O00 = O00O0oOO00O00 . split ( '&regexs=' ) [ 0 ]
    iIiIi1IiIi1iI = xbmcgui . ListItem ( iIIIiiiIiI1 , iconImage = i1iI1i , thumbnailImage = i1iI1i )
    iIiIi1IiIi1iI . setInfo ( type = 'Video' , infoLabels = { 'Title' : iIIIiiiIiI1 } )
    iIiIi1IiIi1iI . setProperty ( "IsPlayable" , "true" )
    iIiIi1IiIi1iI . setPath ( O00O0oOO00O00 )
    if 99 - 99: O0O0OO0O0O0 . i1iIi11iIIi1I . oOooOoO0Oo0O
    oOoO0Oo0 = o0oOoOo0 ( O00O0oOO00O00 , iIiIi1IiIi1iI )
    print 'played' , oOoO0Oo0
   print 'played' , oOoO0Oo0
   if oOoO0Oo0 : return
  return
 if Ooo0OO0oOO . getSetting ( 'ask_playlist_items' ) == 'true' and not queueVideo :
  import urlparse
  i1ii1I1IIIII = [ ]
  OoiiI1i111 = 0
  for iiI1 in mu_playlist :
   if '$$lsname=' in iiI1 :
    iiiiIi1 = iiI1 . split ( '$$lsname=' ) [ 1 ] . split ( '&regexs' ) [ 0 ]
    i1ii1I1IIIII . append ( iiiiIi1 )
    mu_playlist [ OoiiI1i111 ] = iiI1 . split ( '$$lsname=' ) [ 0 ] + ( '&regexs' + iiI1 . split ( '&regexs' ) [ 1 ] if '&regexs' in iiI1 else '' )
   else :
    iiiiIi1 = urlparse . urlparse ( iiI1 ) . netloc
    if iiiiIi1 == '' :
     i1ii1I1IIIII . append ( name )
    else :
     i1ii1I1IIIII . append ( iiiiIi1 )
     if 59 - 59: O0O0OO0O0O0 . oOooOoO0Oo0O / I1I11I1I1I * I1Ii111 + oOooOoO0Oo0O
   OoiiI1i111 += 1
  Ii1I1i1ii1I1 = xbmcgui . Dialog ( )
  o000o = Ii1I1i1ii1I1 . select ( 'Choose a video source' , i1ii1I1IIIII )
  if o000o >= 0 :
   iIIIiiiIiI1 = i1ii1I1IIIII [ o000o ]
   print 'playnamexx' , iIIIiiiIiI1
   if "&mode=19" in mu_playlist [ o000o ] :
    if 98 - 98: oOOO0OOooOoO0Oo * ii11i . OooO0OO * oOoO0oo0OOOo / I1Ii111 + IIi
    iIiIi1IiIi1iI = xbmcgui . ListItem ( iIIIiiiIiI1 , iconImage = i1iI1i , thumbnailImage = i1iI1i )
    iIiIi1IiIi1iI . setInfo ( type = 'Video' , infoLabels = { 'Title' : iIIIiiiIiI1 } )
    iIiIi1IiIi1iI . setProperty ( "IsPlayable" , "true" )
    o00OO0 = iiiIi ( mu_playlist [ o000o ] . replace ( '&mode=19' , '' ) . replace ( ';' , '' ) )
    iIiIi1IiIi1iI . setPath ( o00OO0 )
    xbmc . Player ( ) . play ( o00OO0 , iIiIi1IiIi1iI )
   elif "$doregex" in mu_playlist [ o000o ] :
    if 25 - 25: OOo
    IiiIIiI1iI1 = mu_playlist [ o000o ] . split ( '&regexs=' )
    if 19 - 19: i11ii11iIi11i % OooO0OO . oOOO0OOooOoO0Oo * IIi
    O00O0oOO00O00 , i1II = oOOoo0000O0o0 ( IiiIIiI1iI1 [ 1 ] , IiiIIiI1iI1 [ 0 ] )
    OOoO0OOoO0ooo = O00O0oOO00O00 . replace ( ';' , '' )
    iIiIi1IiIi1iI = xbmcgui . ListItem ( iIIIiiiIiI1 , iconImage = i1iI1i , thumbnailImage = i1iI1i )
    iIiIi1IiIi1iI . setInfo ( type = 'Video' , infoLabels = { 'Title' : iIIIiiiIiI1 } )
    iIiIi1IiIi1iI . setProperty ( "IsPlayable" , "true" )
    iIiIi1IiIi1iI . setPath ( OOoO0OOoO0ooo )
    xbmc . Player ( ) . play ( OOoO0OOoO0ooo , iIiIi1IiIi1iI )
    if 89 - 89: Iii1ii1II11i . I1II1
   else :
    O00O0oOO00O00 = mu_playlist [ o000o ]
    O00O0oOO00O00 = O00O0oOO00O00 . split ( '&regexs=' ) [ 0 ]
    iIiIi1IiIi1iI = xbmcgui . ListItem ( iIIIiiiIiI1 , iconImage = i1iI1i , thumbnailImage = i1iI1i )
    iIiIi1IiIi1iI . setInfo ( type = 'Video' , infoLabels = { 'Title' : iIIIiiiIiI1 } )
    iIiIi1IiIi1iI . setProperty ( "IsPlayable" , "true" )
    iIiIi1IiIi1iI . setPath ( O00O0oOO00O00 )
    xbmc . Player ( ) . play ( O00O0oOO00O00 , iIiIi1IiIi1iI )
 elif not queueVideo :
  if 7 - 7: OOo % Iii1ii1II11i - i11ii11iIi11i + oOoO0oo0OOOo
  oo000O0OoooO . clear ( )
  oOOo0O00o = 0
  for iiI1 in mu_playlist :
   oOOo0O00o += 1
   OoO0Ooo = xbmcgui . ListItem ( '%s) %s' % ( str ( oOOo0O00o ) , name ) )
   if 21 - 21: i11ii11iIi11i + I1Ii111 * oOoO0oo0OOOo * ii11i - IiiI . oOoO0oo0OOOo
   try :
    if "$doregex" in iiI1 :
     IiiIIiI1iI1 = iiI1 . split ( '&regexs=' )
     if 59 - 59: IiiI - IiiI + iIii1
     O00O0oOO00O00 , i1II = oOOoo0000O0o0 ( IiiIIiI1iI1 [ 1 ] , IiiIIiI1iI1 [ 0 ] )
    elif "&mode=19" in iiI1 :
     O00O0oOO00O00 = iiiIi ( iiI1 . replace ( '&mode=19' , '' ) . replace ( ';' , '' ) )
    if O00O0oOO00O00 :
     oo000O0OoooO . add ( O00O0oOO00O00 , OoO0Ooo )
    else :
     raise
   except Exception :
    oo000O0OoooO . add ( iiI1 , OoO0Ooo )
    pass
    if 32 - 32: I11i11Ii / oOoO0oo0OOOo - iIIi1iI1II111
  xbmc . executebuiltin ( 'playlist.playoffset(video,0)' )
 else :
  if 85 - 85: OooO0OO - iIIi1iI1II111 * O0O0OO0O0O0 . I11i11Ii
  IIIIIii1ii11 = xbmcgui . ListItem ( name )
  oo000O0OoooO . add ( mu_playlist , IIIIIii1ii11 )
  if 20 - 20: iIii1 / I1II1
  if 28 - 28: IIi * I1I11I1I1I % O0O0OO0O0O0 * iIii1 / OooO0OO
def iIII1iIi ( name , url ) :
 if 75 - 75: OooO0OO - I1I11I1I1I % Iii1ii1II11i
 if Ooo0OO0oOO . getSetting ( 'save_location' ) == "" :
  xbmc . executebuiltin ( "XBMC.Notification('probando','Choose a location to save files.',15000," + o0oOoO00o + ")" )
  Ooo0OO0oOO . openSettings ( )
 oooOO0oo0Oo00 = { 'url' : url , 'download_path' : Ooo0OO0oOO . getSetting ( 'save_location' ) }
 downloader . download ( name , oooOO0oo0Oo00 )
 Ii1I1i1ii1I1 = xbmcgui . Dialog ( )
 O0000 = Ii1I1i1ii1I1 . yesno ( 'probando' , 'Do you want to add this file as a source?' )
 if O0000 :
  Ii11I ( os . path . join ( Ooo0OO0oOO . getSetting ( 'save_location' ) , name ) )
  if 80 - 80: OooO0OO / I1II1
def iIIi1i11 ( url , name ) :
 if 34 - 34: IiiI % I1iII1iiII % i11ii11iIi11i
 Ii1iIII11iIIi = [ 'plugin://plugin.video.genesis/?action=shows_search' , 'plugin://plugin.video.genesis/?action=movies_search' , 'plugin://plugin.video.salts/?mode=search&amp;section=Movies' , 'plugin://plugin.video.salts/?mode=search&amp;section=TV' , 'plugin://plugin.video.muchmovies.hd/?action=movies_search' , 'plugin://plugin.video.viooz.co/?action=root_search' , 'plugin://plugin.video.ororotv/?action=shows_search' , 'plugin://plugin.video.yifymovies.hd/?action=movies_search' , 'plugin://plugin.video.cartoonhdtwo/?description&amp;fanart&amp;iconimage&amp;mode=3&amp;name=Search&amp;url=url' , 'plugin://plugin.video.youtube/kodion/search/list/' , 'plugin://plugin.video.dailymotion_com/?mode=search&amp;url' , 'plugin://plugin.video.vimeo/kodion/search/list/' ]
 if 11 - 11: oOOO0OOooOoO0Oo + ii11i . O0O0OO0O0O0 - I1II1
 if 49 - 49: IIi . i1iIi11iIIi1I
 if 24 - 24: iIIi1iI1II111 . oOooOoO0Oo0O - IiiI * oOooOoO0Oo0O
 if 12 - 12: iIIi1iI1II111 + oOOO0OOooOoO0Oo * I11i11Ii . IiiI
 if 71 - 71: II - I1iII1iiII - I1II1
 if 28 - 28: ii11i
 if 7 - 7: I1iII1iiII % oOOO0OOooOoO0Oo * Iii1ii1II11i
 if 58 - 58: oOOO0OOooOoO0Oo / I1I11I1I1I + i1iIi11iIIi1I % iIii1 - oOooOoO0Oo0O
 if 25 - 25: Iii1ii1II11i % oOooOoO0Oo0O * oOoO0oo0OOOo - I11i11Ii * i1iIi11iIIi1I * OOo
 if 30 - 30: I1I11I1I1I % Iii1ii1II11i / I1Ii111 * iIIi1iI1II111 * OooO0OO . i11ii11iIi11i
 if 46 - 46: Iii1ii1II11i - iIIi1iI1II111
 if 70 - 70: I1I11I1I1I + oOoO0oo0OOOo * ii11i . i11ii11iIi11i * I1I11I1I1I
 i1ii1I1IIIII = [ 'Gensis TV' , 'Genesis Movie' , 'Salt movie' , 'salt TV' , 'Muchmovies' , 'viooz' , 'ORoroTV' , 'Yifymovies' , 'cartoonHD' , 'Youtube' , 'DailyMotion' , 'Vimeo' ]
 if 49 - 49: I1iII1iiII
 Ii1I1i1ii1I1 = xbmcgui . Dialog ( )
 o000o = Ii1I1i1ii1I1 . select ( 'Choose a video source' , i1ii1I1IIIII )
 if 25 - 25: iIii1 . oOooOoO0Oo0O * ii11i . I1iII1iiII / iIIi1iI1II111 + OooO0OO
 if o000o >= 0 :
  url = Ii1iIII11iIIi [ o000o ]
  if 68 - 68: oOoO0oo0OOOo
  ii111I11Ii ( url )
  if 6 - 6: OooO0OO
def o0oo0o0O00OO ( name , url , mode , iconimage , fanart , description , genre , date , credits , showcontext = False , regexs = None , reg_url = None , allinfo = { } ) :
 if 77 - 77: I11i11Ii + IiiI . i11ii11iIi11i * I1II1 / oOOO0OOooOoO0Oo / OooO0OO
 if 84 - 84: IiiI / ii11i
 if 33 - 33: I11i11Ii / II - I11i11Ii . oOoO0oo0OOOo
 if regexs and len ( regexs ) > 0 :
  iIIi1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&regexs=" + regexs
 else :
  iIIi1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&fanart=" + urllib . quote_plus ( fanart )
  if 65 - 65: I11i11Ii . I1Ii111 / IIi
 I1i1I11111iI1 = True
 if date == '' :
  date = None
 else :
  description += '\n\nDate: %s' % date
 iIiIi1IiIi1iI = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 if len ( allinfo ) < 1 :
  iIiIi1IiIi1iI . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description , "Genre" : genre , "dateadded" : date , "credits" : credits } )
 else :
  iIiIi1IiIi1iI . setInfo ( type = "Video" , infoLabels = allinfo )
 iIiIi1IiIi1iI . setProperty ( "Fanart_Image" , fanart )
 if showcontext :
  IIIIIIi = [ ]
  O0O0ooOOO = Ooo0OO0oOO . getSetting ( 'parentalblocked' )
  O0O0ooOOO = O0O0ooOOO == "true"
  OO0o = Ooo0OO0oOO . getSetting ( 'parentalblockedpin' )
  if 74 - 74: iIIi1iI1II111 - i1iIi11iIIi1I + I11i11Ii . II . I1Ii111
  if len ( OO0o ) > 0 :
   if O0O0ooOOO :
    IIIIIIi . append ( ( 'Disable Parental Block' , 'XBMC.RunPlugin(%s?mode=55&name=%s)' % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
   else :
    IIIIIIi . append ( ( 'Enable Parental Block' , 'XBMC.RunPlugin(%s?mode=56&name=%s)' % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
    if 95 - 95: i1iIi11iIIi1I / OooO0OO - IIi - i1iIi11iIIi1I - O0O0OO0O0O0
  if showcontext == 'source' :
   if 85 - 85: I1iII1iiII / II
   if name in str ( oOOoO0 ) :
    IIIIIIi . append ( ( 'Remove from Sources' , 'XBMC.RunPlugin(%s?mode=8&name=%s)' % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
    if 67 - 67: I1I11I1I1I % OOo
    if 39 - 39: O0O0OO0O0O0 + oOOO0OOooOoO0Oo
  elif showcontext == 'download' :
   IIIIIIi . append ( ( 'Download' , 'XBMC.RunPlugin(%s?url=%s&mode=9&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , urllib . quote_plus ( name ) ) ) )
  elif showcontext == 'fav' :
   IIIIIIi . append ( ( 'Remove from probando Favorites' , 'XBMC.RunPlugin(%s?mode=6&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  if showcontext == '!!update' :
   iiiiI11ii = (
 '%s?url=%s&mode=17&regexs=%s'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( reg_url ) , regexs )
 )
   IIIIIIi . append ( ( '[COLOR yellow]!!update[/COLOR]' , 'XBMC.RunPlugin(%s)' % iiiiI11ii ) )
  if not name in ii11iIi1I :
   IIIIIIi . append ( ( 'Add to probando Favorites' , 'XBMC.RunPlugin(%s?mode=5&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) , mode ) ) )
  iIiIi1IiIi1iI . addContextMenuItems ( IIIIIIi )
 I1i1I11111iI1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iIIi1 , listitem = iIiIi1IiIi1iI , isFolder = True )
 return I1i1I11111iI1
def oooooOOo0o ( url , title , media_type = 'video' ) :
 if 98 - 98: IiiI / I1I11I1I1I - OooO0OO
 if 82 - 82: oOoO0oo0OOOo . OooO0OO * I1Ii111 * I1I11I1I1I . i1iIi11iIIi1I
 import youtubedl
 if 47 - 47: OOo + ii11i . Iii1ii1II11i
 if not url == '' :
  if media_type == 'audio' :
   youtubedl . single_YD ( url , download = True , audio = True )
  else :
   youtubedl . single_YD ( url , download = True )
 elif xbmc . Player ( ) . isPlaying ( ) == True :
  import YDStreamExtractor
  if YDStreamExtractor . isDownloading ( ) == True :
   if 16 - 16: I1iII1iiII . I1I11I1I1I
   YDStreamExtractor . manageDownloads ( )
  else :
   I1IIIIIi1IIiI = xbmc . Player ( ) . getPlayingFile ( )
   if 26 - 26: I1iII1iiII % I1II1 + I1II1 % I1I11I1I1I * O0O0OO0O0O0 / iIii1
   I1IIIIIi1IIiI = I1IIIIIi1IIiI . split ( '|User-Agent=' ) [ 0 ]
   OoO0Ooo = { 'url' : I1IIIIIi1IIiI , 'title' : title , 'media_type' : media_type }
   youtubedl . single_YD ( '' , download = True , dl_info = OoO0Ooo )
 else :
  xbmc . executebuiltin ( "XBMC.Notification(DOWNLOAD,First Play [COLOR yellow]WHILE playing download[/COLOR] ,10000)" )
  if 64 - 64: OOo % Iii1ii1II11i / i1iIi11iIIi1I % IIi - iIii1
  if 2 - 2: II - I1Ii111 + I1iII1iiII * IiiI / iIii1
def iIIiI11iI1Ii1 ( string ) :
 if isinstance ( string , basestring ) :
  if isinstance ( string , unicode ) :
   string = string . encode ( 'ascii' , 'ignore' )
 return string
def o00oo ( string , encoding = 'utf-8' ) :
 if isinstance ( string , basestring ) :
  if not isinstance ( string , unicode ) :
   string = unicode ( string , encoding , 'ignore' )
 return string
def O0oO0oo0O ( s ) : return "" . join ( filter ( lambda oooOOO0ooOoOOO : ord ( oooOOO0ooOoOOO ) < 128 , s ) )
if 68 - 68: iIIi1iI1II111
def o0oOoO00 ( command ) :
 O0o0Oo = ''
 try :
  O0o0Oo = xbmc . executeJSONRPC ( o00oo ( command ) )
 except UnicodeEncodeError :
  O0o0Oo = xbmc . executeJSONRPC ( iIIiI11iI1Ii1 ( command ) )
  if 94 - 94: IiiI + oOOO0OOooOoO0Oo + IIi
 return o00oo ( O0o0Oo )
 if 82 - 82: oOoO0oo0OOOo - oOoO0oo0OOOo . ii11i / I1II1 + oOOO0OOooOoO0Oo % ii11i
def ii111I11Ii ( url , give_me_result = None , playlist = False ) :
 if 'audio' in url :
  O00OO = o00oo ( '{"jsonrpc":"2.0","method":"Files.GetDirectory","params": {"directory":"%s","media":"video", "properties": ["title", "album", "artist", "duration","thumbnail", "year"]}, "id": 1}' ) % url
 else :
  O00OO = o00oo ( '{"jsonrpc":"2.0","method":"Files.GetDirectory","params":{"directory":"%s","media":"video","properties":[ "plot","playcount","director", "genre","votes","duration","trailer","premiered","thumbnail","title","year","dateadded","fanart","rating","season","episode","studio","mpaa"]},"id":1}' ) % url
 oo000o = json . loads ( o0oOoO00 ( O00OO ) )
 if 37 - 37: iIii1
 if give_me_result :
  return oo000o
 if oo000o . has_key ( 'error' ) :
  return
 else :
  if 33 - 33: IiiI - iIIi1iI1II111 - IiiI
  for iiI1 in oo000o [ 'result' ] [ 'files' ] :
   O000oooOO0Oo0 = { }
   url = iiI1 [ 'file' ]
   Oo0OoO00oOO0o = O0oO0oo0O ( iiI1 [ 'label' ] )
   iI11i1ii11 = O0oO0oo0O ( iiI1 [ 'thumbnail' ] )
   ii1I1i1I = O0oO0oo0O ( iiI1 [ 'fanart' ] )
   O000oooOO0Oo0 = dict ( ( k , v ) for k , v in iiI1 . iteritems ( ) if not v == '0' or not v == - 1 or v == '' )
   O000oooOO0Oo0 . pop ( "file" , None )
   if iiI1 [ 'filetype' ] == 'file' :
    if playlist :
     Iiii1Ii ( Oo0OoO00oOO0o , url , queueVideo = '1' )
     continue
    else :
     I1i1Iiiii ( url , Oo0OoO00oOO0o , iI11i1ii11 , ii1I1i1I , '' , '' , '' , '' , None , '' , total = len ( oo000o [ 'result' ] [ 'files' ] ) , allinfo = O000oooOO0Oo0 )
     if 31 - 31: oOOO0OOooOoO0Oo - IiiI / I1II1 . I11i11Ii / OooO0OO
     if iiI1 [ 'type' ] and iiI1 [ 'type' ] == 'tvshow' :
      xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , 'tvshows' )
     elif iiI1 [ 'episode' ] > 0 :
      xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , 'episodes' )
      if 66 - 66: IiiI
   else :
    o0oo0o0O00OO ( Oo0OoO00oOO0o , url , 53 , iI11i1ii11 , ii1I1i1I , '' , '' , '' , '' , allinfo = O000oooOO0Oo0 )
  xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
  if 72 - 72: II
def I1i1Iiiii ( url , name , iconimage , fanart , description , genre , date , showcontext , playlist , regexs , total , setCookie = "" , allinfo = { } ) :
 if 91 - 91: i1iIi11iIIi1I / oOOO0OOooOoO0Oo + ii11i . I1I11I1I1I - iIIi1iI1II111
 IIIIIIi = [ ]
 O0O0ooOOO = Ooo0OO0oOO . getSetting ( 'parentalblocked' )
 O0O0ooOOO = O0O0ooOOO == "true"
 OO0o = Ooo0OO0oOO . getSetting ( 'parentalblockedpin' )
 if 70 - 70: OooO0OO * OOo - I1I11I1I1I + oOoO0oo0OOOo % I1Ii111 - oOOO0OOooOoO0Oo
 if len ( OO0o ) > 0 :
  if O0O0ooOOO :
   IIIIIIi . append ( ( 'Disable Parental Block' , 'XBMC.RunPlugin(%s?mode=55&name=%s)' % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
  else :
   IIIIIIi . append ( ( 'Enable Parental Block' , 'XBMC.RunPlugin(%s?mode=56&name=%s)' % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) ) )
   if 81 - 81: iIIi1iI1II111 . iIIi1iI1II111
 try :
  name = name . encode ( 'utf-8' )
 except : pass
 I1i1I11111iI1 = True
 OoO00OooO0 = False
 if regexs :
  o00OOo = '17'
  if 'listrepeat' in regexs :
   OoO00OooO0 = True
   if 40 - 40: ii11i + iIii1 * Iii1ii1II11i + OOo
  IIIIIIi . append ( ( '[COLOR white]!!Download Currently Playing!![/COLOR]' , 'XBMC.RunPlugin(%s?url=%s&mode=21&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , urllib . quote_plus ( name ) ) ) )
 elif ( any ( x in url for x in O0 ) and url . startswith ( 'http' ) ) or url . endswith ( '&mode=19' ) :
  url = url . replace ( '&mode=19' , '' )
  o00OOo = '19'
  IIIIIIi . append ( ( '[COLOR white]!!Download Currently Playing!![/COLOR]' , 'XBMC.RunPlugin(%s?url=%s&mode=21&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , urllib . quote_plus ( name ) ) ) )
 elif url . endswith ( '&mode=18' ) :
  url = url . replace ( '&mode=18' , '' )
  o00OOo = '18'
  IIIIIIi . append ( ( '[COLOR white]!!Download!![/COLOR]' , 'XBMC.RunPlugin(%s?url=%s&mode=23&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , urllib . quote_plus ( name ) ) ) )
  if Ooo0OO0oOO . getSetting ( 'dlaudioonly' ) == 'true' :
   IIIIIIi . append ( ( '!!Download [COLOR seablue]Audio!![/COLOR]' , 'XBMC.RunPlugin(%s?url=%s&mode=24&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , urllib . quote_plus ( name ) ) ) )
 elif url . startswith ( 'magnet:?xt=' ) :
  if '&' in url and not '&amp;' in url :
   url = url . replace ( '&' , '&amp;' )
  url = 'plugin://plugin.video.pulsar/play?uri=' + url
  o00OOo = '12'
 else :
  o00OOo = '12'
  IIIIIIi . append ( ( '[COLOR white]!!Download Currently Playing!![/COLOR]' , 'XBMC.RunPlugin(%s?url=%s&mode=21&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( url ) , urllib . quote_plus ( name ) ) ) )
 if 'plugin://plugin.video.youtube/play/?video_id=' in url :
  I1Ii1i11I1I = url . replace ( 'plugin://plugin.video.youtube/play/?video_id=' , 'https://www.youtube.com/watch?v=' )
  IIIIIIi . append ( ( '!!Download [COLOR blue]Audio!![/COLOR]' , 'XBMC.RunPlugin(%s?url=%s&mode=24&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( I1Ii1i11I1I ) , urllib . quote_plus ( name ) ) ) )
 iIIi1 = sys . argv [ 0 ] + "?"
 oo0o000o0oOO0 = False
 if playlist :
  if Ooo0OO0oOO . getSetting ( 'add_playlist' ) == "false" and '$$LSPlayOnlyOne$$' not in playlist [ 0 ] :
   iIIi1 += "url=" + urllib . quote_plus ( url ) + "&mode=" + o00OOo
  else :
   iIIi1 += "mode=13&name=%s&playlist=%s" % ( urllib . quote_plus ( name ) , urllib . quote_plus ( str ( playlist ) . replace ( ',' , '||' ) ) )
   name = name + '[COLOR magenta] (' + str ( len ( playlist ) ) + ' items )[/COLOR]'
   oo0o000o0oOO0 = True
 else :
  iIIi1 += "url=" + urllib . quote_plus ( url ) + "&mode=" + o00OOo
 if regexs :
  iIIi1 += "&regexs=" + regexs
 if not setCookie == '' :
  iIIi1 += "&setCookie=" + urllib . quote_plus ( setCookie )
 if iconimage and not iconimage == '' :
  iIIi1 += "&iconimage=" + urllib . quote_plus ( iconimage )
  if 66 - 66: I1iII1iiII * I1II1 + OooO0OO * I1iII1iiII + I1II1 / oOooOoO0Oo0O
 if date == '' :
  date = None
 else :
  description += '\n\nDate: %s' % date
 iIiIi1IiIi1iI = xbmcgui . ListItem ( name , iconImage = "DefaultVideo.png" , thumbnailImage = iconimage )
 if 86 - 86: OooO0OO . iIii1 - iIii1
 if allinfo == None or len ( allinfo ) < 1 :
  iIiIi1IiIi1iI . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description , "Genre" : genre , "dateadded" : date } )
 else :
  iIiIi1IiIi1iI . setInfo ( type = "Video" , infoLabels = allinfo )
 iIiIi1IiIi1iI . setProperty ( "Fanart_Image" , fanart )
 if 71 - 71: ii11i . i1iIi11iIIi1I % ii11i
 if ( not oo0o000o0oOO0 ) and not any ( x in url for x in o0O ) and not '$PLAYERPROXY$=' in url :
  if regexs :
   if 22 - 22: O0O0OO0O0O0 % I1Ii111 % IIi % IIi . IiiI
   if '$pyFunction:playmedia(' not in urllib . unquote_plus ( regexs ) and 'notplayable' not in urllib . unquote_plus ( regexs ) and 'listrepeat' not in urllib . unquote_plus ( regexs ) :
    if 85 - 85: IIi . iIIi1iI1II111 / I1II1 * IIi - IiiI - O0O0OO0O0O0
    iIiIi1IiIi1iI . setProperty ( 'IsPlayable' , 'true' )
  else :
   iIiIi1IiIi1iI . setProperty ( 'IsPlayable' , 'true' )
 else :
  OO0O00 ( 'NOT setting isplayable' + url )
 if showcontext :
  if 25 - 25: IIi % oOoO0oo0OOOo - I1II1
  if showcontext == 'fav' :
   IIIIIIi . append (
 ( 'Remove from probando Favorites' , 'XBMC.RunPlugin(%s?mode=6&name=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) ) )
 )
  elif not name in ii11iIi1I :
   try :
    O0OoOOooO0O = (
 '%s?mode=5&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=0'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage ) , urllib . quote_plus ( fanart ) )
 )
   except :
    O0OoOOooO0O = (
 '%s?mode=5&name=%s&url=%s&iconimage=%s&fanart=%s&fav_mode=0'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( name ) , urllib . quote_plus ( url ) , urllib . quote_plus ( iconimage . encode ( "utf-8" ) ) , urllib . quote_plus ( fanart . encode ( "utf-8" ) ) )
 )
   if playlist :
    O0OoOOooO0O += 'playlist=' + urllib . quote_plus ( str ( playlist ) . replace ( ',' , '||' ) )
   if regexs :
    O0OoOOooO0O += "&regexs=" + regexs
   IIIIIIi . append ( ( 'Add to probando Favorites' , 'XBMC.RunPlugin(%s)' % O0OoOOooO0O ) )
  iIiIi1IiIi1iI . addContextMenuItems ( IIIIIIi )
 try :
  if not playlist is None :
   if Ooo0OO0oOO . getSetting ( 'add_playlist' ) == "false" :
    Ii11iIII = name . split ( ') ' ) [ 1 ]
    o0 = [
 ( 'Play ' + Ii11iIII + ' PlayList' , 'XBMC.RunPlugin(%s?mode=13&name=%s&playlist=%s)'
 % ( sys . argv [ 0 ] , urllib . quote_plus ( Ii11iIII ) , urllib . quote_plus ( str ( playlist ) . replace ( ',' , '||' ) ) ) )
 ]
    iIiIi1IiIi1iI . addContextMenuItems ( o0 )
 except : pass
 if 80 - 80: O0O0OO0O0O0 % I1Ii111
 I1i1I11111iI1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iIIi1 , listitem = iIiIi1IiIi1iI , totalItems = total , isFolder = OoO00OooO0 )
 if 54 - 54: I1iII1iiII + I1I11I1I1I - ii11i % IIi % oOOO0OOooOoO0Oo
 if 19 - 19: I1Ii111 / ii11i % I11i11Ii . oOooOoO0Oo0O
 return I1i1I11111iI1
 if 57 - 57: IIi . oOoO0oo0OOOo - IiiI - O0O0OO0O0O0 * II / I1iII1iiII
 if 79 - 79: I1Ii111 + I1iII1iiII % oOoO0oo0OOOo * I1iII1iiII
def iiii11IiIiI ( url , name , iconimage , setresolved = True , reg = None ) :
 print 'playsetresolved' , url , setresolved
 if url == None :
  xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
  return
 if setresolved :
  III1 = True
  if '$$LSDirect$$' in url :
   url = url . replace ( '$$LSDirect$$' , '' )
   III1 = False
  if reg and 'notplayable' in reg :
   III1 = False
   if 8 - 8: II + IiiI
  iIiIi1IiIi1iI = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage )
  iIiIi1IiIi1iI . setInfo ( type = 'Video' , infoLabels = { 'Title' : name } )
  iIiIi1IiIi1iI . setProperty ( "IsPlayable" , "true" )
  iIiIi1IiIi1iI . setPath ( url )
  if not III1 :
   xbmc . Player ( ) . play ( url )
  else :
   xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , iIiIi1IiIi1iI )
   if 9 - 9: I1II1 + I1iII1iiII
 else :
  xbmc . executebuiltin ( 'XBMC.RunPlugin(' + url + ')' )
  if 8 - 8: I1II1 * oOoO0oo0OOOo / iIii1 - IiiI - oOooOoO0Oo0O
  if 100 - 100: OOo . ii11i . ii11i
  if 55 - 55: OOo
  if 37 - 37: oOOO0OOooOoO0Oo / O0O0OO0O0O0 / oOoO0oo0OOOo
def I1111i ( link ) :
 O00O0oOO00O00 = urllib . urlopen ( link )
 o0o = O00O0oOO00O00 . read ( )
 O00O0oOO00O00 . close ( )
 oOO00OO0o0O = o0o . split ( "Jetzt" )
 III1IiiIiiI1i = oOO00OO0o0O [ 1 ] . split ( 'programm/detail.php?const_id=' )
 OoO0o00OoO = III1IiiIiiI1i [ 1 ] . split ( '<br /><a href="/' )
 Oo00Oooo00o = OoO0o00OoO [ 0 ] [ 40 : len ( OoO0o00OoO [ 0 ] ) ]
 II11II1I = III1IiiIiiI1i [ 2 ] . split ( "</a></p></div>" )
 O0OO00000o00 = II11II1I [ 0 ] [ 17 : len ( II11II1I [ 0 ] ) ]
 O0OO00000o00 = O0OO00000o00 . encode ( 'utf-8' )
 return "  - " + O0OO00000o00 + " - " + Oo00Oooo00o
 if 83 - 83: OOo - IIi - oOOO0OOooOoO0Oo % I11i11Ii - iIii1 . I1iII1iiII
 if 96 - 96: oOoO0oo0OOOo + II . I11i11Ii
def I1i1i1iii ( url , regex ) :
 O0o0Oo = oo ( url )
 try :
  oOOo0O00o = re . findall ( regex , O0o0Oo ) [ 0 ]
  return oOOo0O00o
 except :
  OO0O00 ( 'regex failed' )
  OO0O00 ( regex )
  return
  if 54 - 54: i1iIi11iIIi1I . I11i11Ii / I1Ii111 % i11ii11iIi11i / II
  if 65 - 65: Iii1ii1II11i . Iii1ii1II11i - OOo + oOoO0oo0OOOo / O0O0OO0O0O0
  if 90 - 90: ii11i + Iii1ii1II11i
def IiI ( d , root = "root" , nested = 0 ) :
 if 16 - 16: oOoO0oo0OOOo / IiiI / iIii1 / ii11i
 III = lambda IiiIOoO : '<' + IiiIOoO + '>'
 oO00o00 = lambda IiiIOoO : '</' + IiiIOoO + '>\n'
 if 51 - 51: oOoO0oo0OOOo * ii11i . oOooOoO0Oo0O . OooO0OO - I1II1 / i11ii11iIi11i
 OoO0ooO = lambda I1iiiiI1iI , I1i1i111Ii1I : I1i1i111Ii1I + III ( oo0 ) + str ( I1iiiiI1iI ) + oO00o00 ( oo0 )
 I1i1i111Ii1I = III ( root ) + '\n' if root else ""
 if 93 - 93: iIIi1iI1II111 - IiiI . i11ii11iIi11i
 for oo0 , oOOOoo in d . iteritems ( ) :
  iiiii1i = type ( oOOOoo )
  if nested == 0 : oo0 = 'regex'
  if iiiii1i is list :
   for I1iiiiI1iI in oOOOoo :
    I1iiiiI1iI = escape ( I1iiiiI1iI )
    I1i1i111Ii1I = OoO0ooO ( I1iiiiI1iI , I1i1i111Ii1I )
    if 48 - 48: oOooOoO0Oo0O . oOoO0oo0OOOo * iIIi1iI1II111 / I1Ii111 . i11ii11iIi11i * I1I11I1I1I
  if iiiii1i is dict :
   I1i1i111Ii1I = OoO0ooO ( '\n' + IiI ( oOOOoo , None , nested + 1 ) , I1i1i111Ii1I )
  if iiiii1i is not list and iiiii1i is not dict :
   if not oOOOoo is None : oOOOoo = escape ( oOOOoo )
   if 37 - 37: oOoO0oo0OOOo - I11i11Ii - oOOO0OOooOoO0Oo + I1I11I1I1I . ii11i
   if oOOOoo is None :
    I1i1i111Ii1I = OoO0ooO ( oOOOoo , I1i1i111Ii1I )
   else :
    if 59 - 59: oOooOoO0Oo0O - II % I1iII1iiII . I1I11I1I1I + I11i11Ii * I1I11I1I1I
    I1i1i111Ii1I = OoO0ooO ( oOOOoo . encode ( "utf-8" ) , I1i1i111Ii1I )
    if 5 - 5: i1iIi11iIIi1I - oOOO0OOooOoO0Oo
 I1i1i111Ii1I += oO00o00 ( root ) if root else ""
 if 86 - 86: oOOO0OOooOoO0Oo * I1I11I1I1I + iIIi1iI1II111 * II + O0O0OO0O0O0 - I1Ii111
 return I1i1i111Ii1I
xbmcplugin . setContent ( int ( sys . argv [ 1 ] ) , 'movies' )
if 70 - 70: O0O0OO0O0O0
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
 if 57 - 57: I1I11I1I1I % I1II1 + IIi * OooO0OO . oOoO0oo0OOOo
oooOO0oo0Oo00 = OoO0OOoO0Oo0 ( )
if 78 - 78: oOooOoO0Oo0O / I11i11Ii . I1II1
O00O0oOO00O00 = None
Oo0OoO00oOO0o = None
o00OOo = None
oo000O0OoooO = None
i1iI1i = None
ii1I1i1I = i1
oo000O0OoooO = None
O0Ooo0O = None
oOo0oO = None
if 18 - 18: I11i11Ii
try :
 O00O0oOO00O00 = urllib . unquote_plus ( oooOO0oo0Oo00 [ "url" ] ) . decode ( 'utf-8' )
except :
 pass
try :
 Oo0OoO00oOO0o = urllib . unquote_plus ( oooOO0oo0Oo00 [ "name" ] )
except :
 pass
try :
 i1iI1i = urllib . unquote_plus ( oooOO0oo0Oo00 [ "iconimage" ] )
except :
 pass
try :
 ii1I1i1I = urllib . unquote_plus ( oooOO0oo0Oo00 [ "fanart" ] )
except :
 pass
try :
 o00OOo = int ( oooOO0oo0Oo00 [ "mode" ] )
except :
 pass
try :
 oo000O0OoooO = eval ( urllib . unquote_plus ( oooOO0oo0Oo00 [ "playlist" ] ) . replace ( '||' , ',' ) )
except :
 pass
try :
 O0Ooo0O = int ( oooOO0oo0Oo00 [ "fav_mode" ] )
except :
 pass
try :
 oOo0oO = oooOO0oo0Oo00 [ "regexs" ]
except :
 pass
i1i1Ii1IiIII = ''
try :
 i1i1Ii1IiIII = urllib . unquote_plus ( oooOO0oo0Oo00 [ "playitem" ] )
except :
 pass
 if 9 - 9: I1I11I1I1I - OOo + iIIi1iI1II111 / iIii1 % I11i11Ii
OO0O00 ( "Mode: " + str ( o00OOo ) )
if 97 - 97: I1iII1iiII * IIi
if 78 - 78: I1I11I1I1I . I1II1 + OOo * iIii1 - I11i11Ii
if not O00O0oOO00O00 is None :
 OO0O00 ( "URL: " + str ( O00O0oOO00O00 . encode ( 'utf-8' ) ) )
OO0O00 ( "Name: " + str ( Oo0OoO00oOO0o ) )
if 27 - 27: OooO0OO % I11i11Ii . oOoO0oo0OOOo % II
if not i1i1Ii1IiIII == '' :
 ooO0000o00O = ii11i1 ( '' , data = i1i1Ii1IiIII )
 Oo0OoO00oOO0o , O00O0oOO00O00 , oOo0oO = IIIII11I1IiI ( ooO0000o00O , None , dontLink = True )
 o00OOo = 117
if o00OOo == None :
 OO0O00 ( "getSources" )
 o0o0oOOOo0oo ( )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 10 - 10: oOOO0OOooOoO0Oo / oOooOoO0Oo0O
elif o00OOo == 1 :
 OO0O00 ( "getData" )
 O0o0Oo = None
 if 50 - 50: O0O0OO0O0O0 - oOooOoO0Oo0O . OOo + iIIi1iI1II111 . I11i11Ii
 if oOo0oO and len ( oOo0oO ) > 0 :
  O0o0Oo , i1II = oOOoo0000O0o0 ( oOo0oO , O00O0oOO00O00 )
  if 91 - 91: I1iII1iiII . iIii1 % oOoO0oo0OOOo - iIii1 . OOo % O0O0OO0O0O0
  if 25 - 25: ii11i
  if O0o0Oo . startswith ( 'http' ) or O0o0Oo . startswith ( 'smb' ) or O0o0Oo . startswith ( 'nfs' ) or O0o0Oo . startswith ( '/' ) :
   O00O0oOO00O00 = O0o0Oo
   O0o0Oo = None
   if 63 - 63: IIi
   if 96 - 96: I1I11I1I1I
 OoOo ( O00O0oOO00O00 , ii1I1i1I , O0o0Oo )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 34 - 34: Iii1ii1II11i / IiiI - i11ii11iIi11i . iIIi1iI1II111 . I1II1
 if 63 - 63: iIii1
elif o00OOo == 2 :
 OO0O00 ( "getChannelItems" )
 OOo0oO00ooO00 ( Oo0OoO00oOO0o , O00O0oOO00O00 , ii1I1i1I )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 11 - 11: iIii1 - ii11i
elif o00OOo == 3 :
 OO0O00 ( "getSubChannelItems" )
 i1i ( Oo0OoO00oOO0o , O00O0oOO00O00 , ii1I1i1I )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 92 - 92: IiiI
elif o00OOo == 4 :
 OO0O00 ( "getFavorites" )
 IiiI11I1IIiI ( )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 15 - 15: oOOO0OOooOoO0Oo / oOOO0OOooOoO0Oo + ii11i % oOooOoO0Oo0O
elif o00OOo == 5 :
 OO0O00 ( "addFavorite" )
 try :
  Oo0OoO00oOO0o = Oo0OoO00oOO0o . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  Oo0OoO00oOO0o = Oo0OoO00oOO0o . split ( '  - ' ) [ 0 ]
 except :
  pass
 ii1IIiII111I ( Oo0OoO00oOO0o , O00O0oOO00O00 , i1iI1i , ii1I1i1I , O0Ooo0O )
 if 12 - 12: IIi
elif o00OOo == 6 :
 OO0O00 ( "rmFavorite" )
 try :
  Oo0OoO00oOO0o = Oo0OoO00oOO0o . split ( '\\ ' ) [ 1 ]
 except :
  pass
 try :
  Oo0OoO00oOO0o = Oo0OoO00oOO0o . split ( '  - ' ) [ 0 ]
 except :
  pass
 Oo0oOO ( Oo0OoO00oOO0o )
 if 36 - 36: II . oOOO0OOooOoO0Oo * oOooOoO0Oo0O - I1iII1iiII
elif o00OOo == 7 :
 OO0O00 ( "addSource" )
 Ii11I ( O00O0oOO00O00 )
 if 60 - 60: I1II1 . iIii1 / ii11i + I1II1 * II
elif o00OOo == 8 :
 OO0O00 ( "rmSource" )
 o0O0O00 ( Oo0OoO00oOO0o )
 if 82 - 82: O0O0OO0O0O0 . ii11i * i11ii11iIi11i - I1I11I1I1I + OooO0OO
elif o00OOo == 9 :
 OO0O00 ( "download_file" )
 iIII1iIi ( Oo0OoO00oOO0o , O00O0oOO00O00 )
 if 48 - 48: I1Ii111
elif o00OOo == 10 :
 OO0O00 ( "getCommunitySources" )
 O0o0O00Oo0o0 ( )
 if 96 - 96: IIi . oOooOoO0Oo0O
elif o00OOo == 11 :
 OO0O00 ( "addSource" )
 Ii11I ( O00O0oOO00O00 )
 if 39 - 39: I1II1 + IiiI
elif o00OOo == 12 :
 OO0O00 ( "setResolvedUrl" )
 if not O00O0oOO00O00 . startswith ( "plugin://plugin" ) or not any ( x in O00O0oOO00O00 for x in o0O ) :
  III1 = True
  if '$$LSDirect$$' in O00O0oOO00O00 :
   O00O0oOO00O00 = O00O0oOO00O00 . replace ( '$$LSDirect$$' , '' )
   III1 = False
  oOOo0O00o = xbmcgui . ListItem ( path = O00O0oOO00O00 )
  if not III1 :
   xbmc . Player ( ) . play ( O00O0oOO00O00 )
  else :
   xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , oOOo0O00o )
 else :
  if 80 - 80: I1II1 % IiiI / Iii1ii1II11i
  xbmc . executebuiltin ( 'XBMC.RunPlugin(' + O00O0oOO00O00 + ')' )
  if 54 - 54: oOoO0oo0OOOo % IiiI - I1II1 - I1I11I1I1I
  if 71 - 71: IIi . O0O0OO0O0O0
elif o00OOo == 13 :
 OO0O00 ( "play_playlist" )
 Iiii1Ii ( Oo0OoO00oOO0o , oo000O0OoooO )
 if 56 - 56: iIIi1iI1II111 * iIii1 + iIii1 * ii11i / IIi * II
elif o00OOo == 14 :
 OO0O00 ( "get_xml_database" )
 Ii1iIiII1ii1 ( O00O0oOO00O00 )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 25 - 25: ii11i . I1I11I1I1I * O0O0OO0O0O0 + oOoO0oo0OOOo * I1I11I1I1I
elif o00OOo == 15 :
 OO0O00 ( "browse_xml_database" )
 Ii1iIiII1ii1 ( O00O0oOO00O00 , True )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 67 - 67: iIii1
elif o00OOo == 16 :
 OO0O00 ( "browse_community" )
 O0o0O00Oo0o0 ( O00O0oOO00O00 , browse = True )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 88 - 88: oOoO0oo0OOOo
elif o00OOo == 17 or o00OOo == 117 :
 OO0O00 ( "getRegexParsed" )
 if 8 - 8: I1Ii111
 O0o0Oo = None
 if oOo0oO and 'listrepeat' in urllib . unquote_plus ( oOo0oO ) :
  oOO , O0000 , III1I1Iii1iiI , oOo0oO , iii11i1 = oOOoo0000O0o0 ( oOo0oO , O00O0oOO00O00 )
  if 82 - 82: oOooOoO0Oo0O
  O0OO = ''
  if 75 - 75: i1iIi11iIIi1I % i11ii11iIi11i + I1II1 % oOooOoO0Oo0O / oOOO0OOooOoO0Oo
  if 4 - 4: O0O0OO0O0O0 - I1II1 % I1Ii111 * II % I1iII1iiII
  o0OoOoo = III1I1Iii1iiI [ 'name' ]
  O0OoO0o0Oooo = oOo0oO . pop ( o0OoOoo )
  if 61 - 61: i1iIi11iIIi1I . iIIi1iI1II111 - OooO0OO - I1Ii111 / O0O0OO0O0O0 - i1iIi11iIIi1I
  O00O0oOO00O00 = ''
  import copy
  O0oo0oOo = ''
  i111iI1i1iI = 0
  for IiiI1i111I1i in O0000 :
   if 97 - 97: I1II1 % i11ii11iIi11i * i11ii11iIi11i % oOoO0oo0OOOo
   try :
    i111iI1i1iI += 1
    o0OoOooOO0o0 = copy . deepcopy ( oOo0oO )
    if 55 - 55: iIIi1iI1II111 % i11ii11iIi11i . oOooOoO0Oo0O * oOoO0oo0OOOo / oOooOoO0Oo0O . OooO0OO
    i1Iii = oOO
    iiI1 = 0
    for iiI1 in range ( len ( IiiI1i111I1i ) ) :
     if 57 - 57: oOOO0OOooOoO0Oo
     if len ( o0OoOooOO0o0 ) > 0 :
      for IiI11I1Ii11II , oo0ooOoOOoO in o0OoOooOO0o0 . iteritems ( ) :
       if oo0ooOoOOoO is not None :
        for Oo0000o , iI1IiiiIIiiII in oo0ooOoOOoO . iteritems ( ) :
         if iI1IiiiIIiiII is not None :
          if 94 - 94: Iii1ii1II11i + oOOO0OOooOoO0Oo . IIi
          if 69 - 69: iIIi1iI1II111 - iIIi1iI1II111
          if 41 - 41: oOOO0OOooOoO0Oo % I1iII1iiII
          if 67 - 67: iIIi1iI1II111 % II
          if type ( iI1IiiiIIiiII ) is dict :
           for IIII1I , o0oOo0000ooO in iI1IiiiIIiiII . iteritems ( ) :
            if o0oOo0000ooO is not None :
             ii111i = None
             if isinstance ( IiiI1i111I1i , tuple ) :
              try :
               ii111i = IiiI1i111I1i [ iiI1 ] . decode ( 'utf-8' )
              except :
               ii111i = IiiI1i111I1i [ iiI1 ]
             else :
              try :
               ii111i = IiiI1i111I1i . decode ( 'utf-8' )
              except :
               ii111i = IiiI1i111I1i
               if 15 - 15: IIi . I1iII1iiII + Iii1ii1II11i . ii11i % IIi + iIIi1iI1II111
             if '[' + o0OoOoo + '.param' + str ( iiI1 + 1 ) + '][DE]' in o0oOo0000ooO :
              o0oOo0000ooO = o0oOo0000ooO . replace ( '[' + o0OoOoo + '.param' + str ( iiI1 + 1 ) + '][DE]' , unescape ( ii111i ) )
             iI1IiiiIIiiII [ IIII1I ] = o0oOo0000ooO . replace ( '[' + o0OoOoo + '.param' + str ( iiI1 + 1 ) + ']' , ii111i )
             if 22 - 22: I1iII1iiII + oOoO0oo0OOOo . IIi + I1Ii111 * iIii1 . O0O0OO0O0O0
             if 90 - 90: I1II1 * Iii1ii1II11i - oOoO0oo0OOOo + I1iII1iiII
          else :
           ii111i = None
           if isinstance ( IiiI1i111I1i , tuple ) :
            try :
             ii111i = IiiI1i111I1i [ iiI1 ] . decode ( 'utf-8' )
            except :
             ii111i = IiiI1i111I1i [ iiI1 ]
           else :
            try :
             ii111i = IiiI1i111I1i . decode ( 'utf-8' )
            except :
             ii111i = IiiI1i111I1i
           if '[' + o0OoOoo + '.param' + str ( iiI1 + 1 ) + '][DE]' in iI1IiiiIIiiII :
            if 53 - 53: oOooOoO0Oo0O . oOooOoO0Oo0O + I1iII1iiII - iIii1 + I1II1
            iI1IiiiIIiiII = iI1IiiiIIiiII . replace ( '[' + o0OoOoo + '.param' + str ( iiI1 + 1 ) + '][DE]' , unescape ( ii111i ) )
            if 44 - 44: II - oOOO0OOooOoO0Oo
           oo0ooOoOOoO [ Oo0000o ] = iI1IiiiIIiiII . replace ( '[' + o0OoOoo + '.param' + str ( iiI1 + 1 ) + ']' , ii111i )
           if 100 - 100: OOo . IiiI - OooO0OO + iIIi1iI1II111 * IiiI
           if 59 - 59: i1iIi11iIIi1I
     ii111i = None
     if isinstance ( IiiI1i111I1i , tuple ) :
      try :
       ii111i = IiiI1i111I1i [ iiI1 ] . decode ( 'utf-8' )
      except :
       ii111i = IiiI1i111I1i [ iiI1 ]
     else :
      try :
       ii111i = IiiI1i111I1i . decode ( 'utf-8' )
      except :
       ii111i = IiiI1i111I1i
     if '[' + o0OoOoo + '.param' + str ( iiI1 + 1 ) + '][DE]' in i1Iii :
      i1Iii = i1Iii . replace ( '[' + o0OoOoo + '.param' + str ( iiI1 + 1 ) + '][DE]' , ii111i )
     i1Iii = i1Iii . replace ( '[' + o0OoOoo + '.param' + str ( iiI1 + 1 ) + ']' , escape ( ii111i ) )
     if 43 - 43: oOoO0oo0OOOo + oOooOoO0Oo0O
    i1Iii = i1Iii . replace ( '[' + o0OoOoo + '.param' + str ( 0 ) + ']' , str ( i111iI1i1iI ) )
    if 47 - 47: IIi
    try :
     if iii11i1 and '[' + o0OoOoo + '.cookies]' in i1Iii :
      i1Iii = i1Iii . replace ( '[' + o0OoOoo + '.cookies]' , iIIIII1iiiiII ( iii11i1 ) )
    except : pass
    if 92 - 92: I1I11I1I1I % O0O0OO0O0O0 % oOoO0oo0OOOo
    if 23 - 23: i1iIi11iIIi1I * iIii1
    if 80 - 80: II / O0O0OO0O0O0 + oOooOoO0Oo0O
    if 38 - 38: I1Ii111 % IIi + I11i11Ii * oOooOoO0Oo0O * OOo
    OoO0o0OO = ''
    if 10 - 10: OOo - iIii1 % i1iIi11iIIi1I - II - I11i11Ii
    if len ( o0OoOooOO0o0 ) > 0 :
     OoO0o0OO = IiI ( o0OoOooOO0o0 , 'lsproroot' )
     OoO0o0OO = OoO0o0OO . split ( '<lsproroot>' ) [ 1 ] . split ( '</lsproroot' ) [ 0 ]
     if 10 - 10: I1Ii111 - I1I11I1I1I . II
     if 8 - 8: ii11i % OOo + oOoO0oo0OOOo
    try :
     O0oo0oOo += '\n<item>%s\n%s</item>' % ( i1Iii , OoO0o0OO )
    except : O0oo0oOo += '\n<item>%s\n%s</item>' % ( i1Iii . encode ( "utf-8" ) , OoO0o0OO )
   except : traceback . print_exc ( file = sys . stdout )
   if 24 - 24: I1iII1iiII / OooO0OO / OooO0OO % i1iIi11iIIi1I - OOo * OOo
   if 58 - 58: Iii1ii1II11i
   if 60 - 60: i1iIi11iIIi1I
   if 90 - 90: Iii1ii1II11i
   if 37 - 37: Iii1ii1II11i + iIIi1iI1II111 . iIIi1iI1II111 * oOoO0oo0OOOo % II / iIii1
  OO0O00 ( repr ( O0oo0oOo ) )
  OoOo ( '' , '' , O0oo0oOo )
  xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 else :
  O00O0oOO00O00 , i1II = oOOoo0000O0o0 ( oOo0oO , O00O0oOO00O00 )
  print repr ( O00O0oOO00O00 ) , i1II , 'imhere'
  if not ( oOo0oO and 'notplayable' in oOo0oO and not O00O0oOO00O00 ) :
   if O00O0oOO00O00 :
    if '$PLAYERPROXY$=' in O00O0oOO00O00 :
     O00O0oOO00O00 , II11iI111i1 = O00O0oOO00O00 . split ( '$PLAYERPROXY$=' )
     print 'proxy' , II11iI111i1
     if 18 - 18: oOooOoO0Oo0O
     O0oOo00oooO = None
     IiiIiI1IIi1IIIii = None
     if len ( II11iI111i1 ) > 0 and '@' in II11iI111i1 :
      II11iI111i1 = II11iI111i1 . split ( ':' )
      O0oOo00oooO = II11iI111i1 [ 0 ]
      IiiIiI1IIi1IIIii = II11iI111i1 [ 1 ] . split ( '@' ) [ 0 ]
      OOO0o = II11iI111i1 [ 1 ] . split ( '@' ) [ 1 ]
      O0O00OO = II11iI111i1 [ 2 ]
     else :
      OOO0o , O0O00OO = II11iI111i1 . split ( ':' )
      if 43 - 43: OOo + oOooOoO0Oo0O . I1iII1iiII . I1Ii111
     iI ( O00O0oOO00O00 , Oo0OoO00oOO0o , i1iI1i , OOO0o , O0O00OO , O0oOo00oooO , IiiIiI1IIi1IIIii )
    else :
     iiii11IiIiI ( O00O0oOO00O00 , Oo0OoO00oOO0o , i1iI1i , i1II , oOo0oO )
   else :
    xbmc . executebuiltin ( "XBMC.Notification(probando,Failed to extract regex. - " + "this" + ",4000," + o0oOoO00o + ")" )
elif o00OOo == 18 :
 OO0O00 ( "youtubedl" )
 try :
  import youtubedl
 except Exception :
  xbmc . executebuiltin ( "XBMC.Notification(probando,Please [COLOR yellow]install Youtube-dl[/COLOR] module ,10000," ")" )
 iiIi1IIi1I = youtubedl . single_YD ( O00O0oOO00O00 )
 iiii11IiIiI ( iiIi1IIi1I , Oo0OoO00oOO0o , i1iI1i )
elif o00OOo == 19 :
 OO0O00 ( "Genesiscommonresolvers" )
 iiii11IiIiI ( iiiIi ( O00O0oOO00O00 ) , Oo0OoO00oOO0o , i1iI1i , True )
 if 30 - 30: IIi - O0O0OO0O0O0 + i11ii11iIi11i / oOoO0oo0OOOo % iIIi1iI1II111
elif o00OOo == 21 :
 OO0O00 ( "download current file using youtube-dl service" )
 oooooO00OOO = 'video'
 if '[mp3]' in Oo0OoO00oOO0o :
  oooooO00OOO = 'audio'
  Oo0OoO00oOO0o = Oo0OoO00oOO0o . replace ( '[mp3]' , '' )
 oooooOOo0o ( '' , Oo0OoO00oOO0o , oooooO00OOO )
elif o00OOo == 23 :
 OO0O00 ( "get info then download" )
 oooooO00OOO = 'video'
 if '[mp3]' in Oo0OoO00oOO0o :
  oooooO00OOO = 'audio'
  Oo0OoO00oOO0o = Oo0OoO00oOO0o . replace ( '[mp3]' , '' )
 oooooOOo0o ( O00O0oOO00O00 , Oo0OoO00oOO0o , oooooO00OOO )
elif o00OOo == 24 :
 OO0O00 ( "Audio only youtube download" )
 oooooOOo0o ( O00O0oOO00O00 , Oo0OoO00oOO0o , 'audio' )
elif o00OOo == 25 :
 OO0O00 ( "Searchin Other plugins" )
 iIIi1i11 ( O00O0oOO00O00 , Oo0OoO00oOO0o )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o00OOo == 55 :
 OO0O00 ( "enabled lock" )
 OO0o = Ooo0OO0oOO . getSetting ( 'parentalblockedpin' )
 o0OO00oO = xbmc . Keyboard ( '' , 'Enter Pin' )
 o0OO00oO . doModal ( )
 if not ( o0OO00oO . isConfirmed ( ) == False ) :
  I11i1I1I = o0OO00oO . getText ( )
  if I11i1I1I == OO0o :
   Ooo0OO0oOO . setSetting ( 'parentalblocked' , "false" )
   xbmc . executebuiltin ( "XBMC.Notification(probando,Parental Block Disabled,5000," + o0oOoO00o + ")" )
  else :
   xbmc . executebuiltin ( "XBMC.Notification(probando,Wrong Pin??,5000," + o0oOoO00o + ")" )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
elif o00OOo == 56 :
 OO0O00 ( "disable lock" )
 Ooo0OO0oOO . setSetting ( 'parentalblocked' , "true" )
 xbmc . executebuiltin ( "XBMC.Notification(probando,Parental block enabled,5000," + o0oOoO00o + ")" )
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 53 - 53: i1iIi11iIIi1I
elif o00OOo == 53 :
 OO0O00 ( "Requesting JSON-RPC Items" )
 ii111I11Ii ( O00O0oOO00O00 )
 if 61 - 61: iIIi1iI1II111 * IiiI * i11ii11iIi11i % oOooOoO0Oo0O / Iii1ii1II11i % IIi
if not oo000 == None :
 print 'setting view mode'
 xbmc . executebuiltin ( "Container.SetViewMode(%s)" % oo000 )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3