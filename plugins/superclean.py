#===istalismanplugin===
# -*- coding: utf-8 -*-

#  Tron plugin
#  super_clean.py



def handler_sclean_conf(type, source, parameters):
	if GROUPCHATS.has_key(source[1]):
		for x in range(1, 500):
			msg(source[1], '')
			time.sleep(0.1)
		reply('public',source,u'')
















register_command_handler(handler_sclean_conf, COMM_PREFIX+'sclean', ['fun','muc','all','*'], 15, 'Clean current conference (with null character).', COMM_PREFIX+'sclean', [COMM_PREFIX+'sclean'])