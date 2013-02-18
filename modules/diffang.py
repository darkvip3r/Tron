#===istalismanplugin===
# -*- coding: utf-8 -*-

#  Talisman plugin
#  trans_plugin.py

	
def find_trans_plugins():
   print '\nLOADING TRANS_PLUGINS'
   valid_trans_plugins = []
   invalid_trans_plugins = []
   possibilities = os.listdir('trans_plugins')
   for possibility in possibilities:
      if possibility[-3:].lower() == '.py':
         try:
            fp = file(PLUGIN_DIR + '/' + possibility)
            data = fp.read(23)
            if data == '#===istalismanplugin===':
               valid_plugins.append(possibility)
            else:
               invalid_plugins.append(possibility)
         except:
            pass
   if invalid_trans_plugins:
      print '\nfailed to load',len(invalid_plugins),'plug-ins:'
      invalid_plugins.sort()
      invp=', '.join(invalid_plugins)
      print invp
      print 'plugins header is not corresponding\n'
   else:
      print '\nthere are not unloadable plug-ins'
   return valid_trans_plugins

def load_trans_plugins():
   plugins = find_plugins()
   for plugin in plugins:
      try:
         fp = file(PLUGIN_DIR + '/' + plugin)
         exec fp in globals()
         fp.close()
      except:
         raise
   plugins.sort()
   print '\nloaded',len(plugins),'plug-ins:'
   loaded=', '.join(plugins)
   print loaded,'\n'
