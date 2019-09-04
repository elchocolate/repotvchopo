# -*- coding: utf-8 -*-
"""
openload.io urlresolver plugin
Copyright (C) 2015 tknorris

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""
import os
import xbmc
import json
from resolveurl import common
from resolveurl.common import i18n
from resolveurl.resolver import ResolveUrl, ResolverError
import urllib
import requests
import base64
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')
logger = common.log_utils.Logger.get_logger(__name__)
logger.disable()

API_BASE_URL = 'https://api.openload.co/1'
INFO_URL = API_BASE_URL + '/streaming/info'
GET_URL = API_BASE_URL + '/streaming/get?file={media_id}'
FILE_URL = API_BASE_URL + '/file/info?file={media_id}'
OL_PATH = os.path.join(common.plugins_path, 'ol_gmu.py')

class OpenLoadResolver(ResolveUrl):
    name = "openload"
    domains = ["openload.io", "openload.co", "oload.tv", "oload.stream"]
    pattern = '(?://|\.)(o(?:pen)??load\.(?:io|co|tv|stream))/(?:embed|f)/([0-9a-zA-Z-_]+)'

    def __init__(self):
        self.net = common.Net()
    def get_media_url(self,host,media_id):
        url = "https://openload.co/embed/"+str(media_id)
        r = requests.get(url).content
        data = {"code":r}
        result = requests.post("http://81.2.255.124:5000/openloadapi",data=data,verify = False).content
        result = result.replace("\n","")
        if len(result) > 60:
            pass
        else:
            return 'https://openload.co/stream/%s?mime=true|User-Agent=Mozilla/5.0' % result
    
    def get_url(self, host, media_id):
        return 'https://openload.co/embed/%s' % media_id