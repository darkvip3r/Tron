#===istalismanplugin===
# -*- coding: utf-8 -*-

#  Talisman plugin
#  stanza_plugin.py

#  Initial Copyright © 2007 dimichxp <dimichxp@gmail.com>
#  Modifications Copyright © 2009 wd/lotusfeet <dao/yoga>

#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.

#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.

def handler_stanza(source, type, parameters):
	if parameters:
		node=xmpp.simplexml.XML2Node(unicode(parameters).encode('utf8'))
		JCON.send(node)
		return
	rep = u'What are you going to send?'
	reply(source, type, rep)
	
register_command_handler(handler_stanza, COMM_PREFIX+'stanza', ['superadmin','all','*','muc'], 100, 'Processor XML-stanza! Allows you to send jabber (xmpp)-server сырой (raw) XML-code, a standard protocol XMPP.', COMM_PREFIX+'stanza <payload>', [COMM_PREFIX+'stanza aaabbb'])