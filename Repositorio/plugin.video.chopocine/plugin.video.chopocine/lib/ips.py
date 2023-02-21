import six
from six . moves import urllib_request
import xbmc, xbmcvfs
import os

def cookie():
    import re,base64
    import requests
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8","Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3","Content-Type": "application/x-www-form-urlencoded", "Upgrade-Insecure-Requests": "1","Pragma": "no-cache","Cache-Control": "no-cache"}
 
    url = "https://www.croxyproxy.rocks/requests?fso="
 
    payload = {'url':'https://www.gnula2.co/estrenos/','proxyServerId':'94','demo':'0','frontOrigin':'https://www.croxyproxy.rocks'}
    x = requests.post(url,headers=headers,data=payload,verify=False)
    return(x.headers['access-control-allow-origin'])
