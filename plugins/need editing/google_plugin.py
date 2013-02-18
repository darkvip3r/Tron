#===istalismanplugin===
# -*- coding: utf-8 -*-

#  Talisman plugin
#  google_plugin.py

#  Initial Copyright © 2009 Als <Als@admin.ru.net>

#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.

#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.


def google_remove_html(text):
	nobold = text.replace('<b>', '').replace('</b>', '')
	nobreaks = nobold.replace('<br>', ' ')
	noescape = nobreaks.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>').replace('&quot;', '"')
	return noescape

def google_search(query):
	try:
		req = urllib2.urlopen('http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=%s' % urllib2.quote(query.encode('utf8')))
	except urllib2.HTTPError, e:
		reply(type,source,str(e))
		return
	answ=json.load(req)
	results=answ['responseData']['results']
	if results:
		titleNoFormatting=results[0]['titleNoFormatting']
		content=results[0]['content']
		url=results[0]['unescapedUrl']
		return google_remove_html(titleNoFormatting+u'\n'+content+u'\n'+url)
	elif answ['responseDetails']:
		return answ['responseDetails']
	else:
		return


def handler_google_google(type, source, parameters):
	results = google_search(parameters)
	if results:
		reply(type, source, results)
	else:
		reply(type, source, u'nothing found')

try:
	import json
	register_command_handler(handler_google_google, COMM_PREFIX+'google', ['fun','all'], 0, 'search in google.', COMM_PREFIX+'google <query>', [COMM_PREFIX+'google something'])
except ImportError:
	try:
		import simplejson as json
		register_command_handler(handler_google_google, COMM_PREFIX+'google', ['fun','all'], 0, 'search in google.', COMM_PREFIX+'google <query>', [COMM_PREFIX+'google something'])
	except:
		print '====================================================\nYou need Python 2.6.x or simple_json package installed to use google_plugin.py!!!\n====================================================\n'
