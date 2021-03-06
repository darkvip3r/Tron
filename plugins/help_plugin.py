#===istalismanplugin===
# -*- coding: utf-8 -*-

#  Talisman plugin
#  help_plugin.py

#  Initial Copyright © 2002-2005 Mike Mintz <mikemintz@gmail.com>
#  Modifications Copyright © 2007 Als <Als@exploit.in>
#  Modifications Copyright © 2009 wd/lotusfeet <dao/yoga>
#  Help Copyright © 2007 dimichxp <dimichxp@gmail.com>

#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.

#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.

def handler_help_help(type, source, parameters):
	groupchat = source[1]
	
	ctglist = []
	if parameters and COMMANDS.has_key(COMM_PREFIX+parameters.strip()):
		rep = COMMANDS[COMM_PREFIX+parameters.strip()]['desc'].decode("utf-8") + u'\nCategories: '
		for cat in COMMANDS[COMM_PREFIX+parameters.strip()]['category']:
			ctglist.append(cat)
		rep += ', '.join(ctglist).decode('utf-8')+u'\nUse: ' + COMMANDS[COMM_PREFIX+parameters.strip()]['syntax'].decode("utf-8") + u'\nExample:'
		for example in COMMANDS[COMM_PREFIX+parameters]['examples']:
			rep += u'\n  >  ' + example.decode("utf-8")
		rep += u'\nNecessary level of access: ' + str(COMMANDS[COMM_PREFIX+parameters.strip()]['access'])
		
		if GROUPCHATS.has_key(groupchat):
			if COMM_PREFIX+parameters.strip() in COMMOFF[groupchat]:
				rep += u'\nThis command has been power-off in this conference!'
			else:
				pass
	else:
		rep = u'Write a word "%scommands" (without quotation marks), to get the list of commands, "%shelp <commands without "%s">" for the receipt of help on a command, %salias_list for a list of aliases, and %salias_acc <alias> to obtain the level of access to certain local aliases and %sgalias_acc <alias> to obtain the level of access to a specific global alias.' % (COMM_PREFIX, COMM_PREFIX, COMM_PREFIX, COMM_PREFIX, COMM_PREFIX, COMM_PREFIX)
				
	reply(type, source, rep)

def handler_help_commands(type, source, parameters):
	date=time.strftime('%d %b %Y (%a)', time.gmtime()).decode('utf-8')
	groupchat=source[1]
	if parameters:
		rep,dsbl = [],[]
		total = 0
		param=parameters.encode("utf-8")
		catcom=set([((param in COMMANDS[x]['category']) and x) or None for x in COMMANDS]) - set([None])
		if not catcom:
			reply(type,source,u'does it exist? :-O')
			return
		for cat in catcom:
			if has_access(source, COMMANDS[cat]['access'],groupchat):
				if groupchat in COMMOFF:
					if cat in COMMOFF[groupchat]:
						dsbl.append(cat)
					else:
						rep.append(cat)
						total += 1
				else:
					rep.append(cat)
					total += 1					
		if rep:
			if type == 'public':
				reply(type,source,u'Look in private!')
			rep.sort()
			answ=u'List of commands is in a category "%s" on %s (total: %s):\n\n%s.' %(parameters,date,total,', '.join(rep))
			if dsbl:
				dsbl.sort()
				answ+=u'\n\nThe followings commands has been power-offs in this conference (total: %s):\n\n%s.' %(len(dsbl),', '.join(dsbl))
			reply('private', source,answ)
		else:
			reply(type,source,u'Insufficient privileges!')
	else:
		cats = set()
		
		for x in [COMMANDS[x]['category'] for x in COMMANDS]:
			cats = cats | set(x)
			
		qcats = len(cats)
		cats = ', '.join(cats).decode('utf-8')
		
		if type == 'public':
			reply(type,source,u'Look in private!')

		reply('private', source, u'List of categories on %s (total: %s):\n\n%s.\n\no view a list of commands contained in the category, type "%scommands <category>" without the quotation marks, example "%scommands *"' % (date,qcats,cats,COMM_PREFIX,COMM_PREFIX))
		
register_command_handler(handler_help_help, COMM_PREFIX+'help', ['help','info','all','*'], 0, 'Show detail information about a certain command.', COMM_PREFIX+'help [command]', [COMM_PREFIX+'help', COMM_PREFIX+'help ping'])
register_command_handler(handler_help_commands, COMM_PREFIX+'commands', ['help','info','all','*'], 0, 'Shows the list of all of categories of commands. At the query of category shows the list of commands being in it.', COMM_PREFIX+'commands [category]', [COMM_PREFIX+'commands',COMM_PREFIX+'commands *'])