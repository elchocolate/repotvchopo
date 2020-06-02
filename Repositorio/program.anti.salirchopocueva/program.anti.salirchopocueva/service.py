# -*- coding: UTF-8 -*-
#######################################################################
# ----------------------------------------------------------------------------
# te sacamos de la chopocueva en cada inicio
# ----------------------------------------------------------------------------
#######################################################################


import shutil

import xbmc

addon_path = xbmc.translatePath(('special://home/addons/plugin.program.chikirywizard')).decode('utf-8')
addon_path = xbmc.translatePath(('special://home/addons/plugin.video.eventos')).decode('utf-8')
addon_path = xbmc.translatePath(('special://home/addons/plugin.program.videotecachikiry')).decode('utf-8')
addon_path = xbmc.translatePath(('special://home/addons/repository.chikiryrepo')).decode('utf-8')
addon_path = xbmc.translatePath(('special://home/addons/program.anti.salirchopocueva')).decode('utf-8')



shutil.rmtree(addon_path, ignore_errors=True)