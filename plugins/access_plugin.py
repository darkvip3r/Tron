#===istalismanplugin===
# -*- coding: utf-8 -*-

#  Talisman plugin
#  access_plugin.py

#  Initial Copyright © 2002-2005 Mike Mintz <mikemintz@gmail.com>
#  Modifications Copyright © 2007 Als <Als@exploit.in>
#  Modifications Copyright © 2009 wd/lotusfeet <dao/yoga>

#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.

#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.

def handler_access_login(type, source, parameters):
	if type == 'private':
		reply(type, source, u'Please use that command here!')
	jid = get_true_jid(source)
	if parameters.strip() == ADMIN_PASSWORD:
		GLOBACCESS[jid]=300
		reply('public', source, u'Password Comfirmed.. Welcome Back Master :)')
	else:
		reply('private', source, u'Wrong password!')
		
def handler_user_login(type, source, parameters):
	if type == 'private':
		reply(type, source, u'Please use that command here!')
	jid = get_true_jid(source)
	if parameters.strip() == USER_PASSWORD:
		GLOBACCESS[jid]=100
		reply('private', source, u'Password Comfirmed. Hello user. whats next?')
	else:
		reply('private', source, u'Wrong password!')		

def handler_access_logout(type, source, parameters):
	jid = get_true_jid(source)
	del GLOBACCESS[jid]
	reply(type, source, u'Loging out...... ')

def handler_access_view_access(type, source, parameters):
	accdesc={'-100':u'(fully banned from bots interface)','-1':u'(blocked)','0':u'(none)','1':u'(poor member :D )','10':u'(user)','11':u'(member)','15':u'(moderator)','16':u'(moderator)','20':u'(admin)','30':u'(owner)','40':u'(joiner)','100':u'(admin)','300':u'(superadmin)'}
	if not parameters:
		level=str(user_level(source[1]+'/'+source[2], source[1]))
		if level in accdesc.keys():
			levdesc=accdesc[level]
		else:
			levdesc=''		
		reply(type, source, level+u' '+levdesc)
	else:
		if not source[1] in GROUPCHATS:
			reply(type, source, u'This is possible only in the conference!')
			return
		nicks = GROUPCHATS[source[1]].keys()
		if parameters.strip() in nicks:
			level=str(user_level(source[1]+'/'+parameters.strip(),source[1]))
			if level in accdesc.keys():
				levdesc=accdesc[level]
			else:
				levdesc=''
			reply(type, source, level+' '+levdesc)
		else:
			reply(type, source, u'the user is not here!')

def handler_access_set_access(type, source, parameters):
	if not source[1] in GROUPCHATS:
		reply(type, source, u'only use this in the conference room')
		return
	splitdata = string.split(parameters)
	if len(splitdata) > 1:
		try:
			int(splitdata[1].strip())
		except:
			reply(type, source, u'Bad Request. Read help on using the command!')
			return				
		if int(splitdata[1].strip())>300 or int(splitdata[1].strip())<-100:
			reply(type, source, u'Bad Request. Read help on using the command')
			return		
	nicks=GROUPCHATS[source[1]]
	if not splitdata[0].strip() in nicks and GROUPCHATS[source[1]][splitdata[0].strip()]['ishere']==0:
		reply(type, source, u'the user is not here!')
		return
	tjidto=get_true_jid(source[1]+'/'+splitdata[0].strip())
	tjidsource=get_true_jid(source)
	groupchat=source[1]
	jidacc=user_level(source, groupchat)
	toacc=user_level(tjidto, groupchat)

	if len(splitdata) > 1:
		if tjidsource in ADMINS:
			pass
		else:
			if tjidto==tjidsource:
				if int(splitdata[1]) > int(jidacc):
					reply(type, source, u'the user is not here!')
					return
			elif int(toacc) > int(jidacc):
				reply(type, source, u'You do not have Admin Privileges')
				return		
			elif int(splitdata[1]) >= int(jidacc):
				reply(type, source, u'the user is not here!')
				return	
	else:
		if tjidsource in ADMINS:
			pass
		else:
			if tjidto==tjidsource:
				pass
			elif int(toacc) > int(jidacc):
				reply(type, source, u'You do not have Admin Privileges')
				return

	if len(splitdata) == 1:		
		change_access_perm(source[1], tjidto)
		if splitdata[0].strip()==source[2]:
			reply(type, source, u'Permanent access removed. This will take effect when i am restarted')
		else:
			reply(type, source, u'Permanent access %s removed. This will take effect when i am restarted' % splitdata[0].strip())
	elif len(splitdata) == 2:
		change_access_temp(source[1], tjidto, splitdata[1].strip())
		reply(type, source, u'temporally access granted!')
	elif len(splitdata) == 3:
		change_access_perm(source[1], tjidto, splitdata[1].strip())
		reply(type, source, u'permanent access granted!')		
		
def handler_access_set_access_glob(type, source, parameters):
	if not source[1] in GROUPCHATS:
		reply(type, source, u'You can only do this in the conference!')
		return
	if parameters:
		splitdata = parameters.strip().split()
		if len(splitdata)<1 or len(splitdata)>2:
			reply(type, source, u'hmm could you Repeat that? i was busy listening to music!')
			return
		nicks=GROUPCHATS[source[1]].keys()
		if not splitdata[0].strip() in nicks and GROUPCHATS[source[1]][splitdata[0].strip()]['ishere']==0:
			reply(type, source, u'the user is not here!')
			return
		tjidto=get_true_jid(source[1]+'/'+splitdata[0])
		if len(splitdata)==2:
			change_access_perm_glob(tjidto, int(splitdata[1]))
			reply(type, source, u'access given!!!')
		else:
			change_access_perm_glob(tjidto)
			reply(type, source, u'Removed!')
			
def get_access_levels():
	global GLOBACCESS
	global ACCBYCONFFILE
	GLOBACCESS = eval(read_file(GLOBACCESS_FILE))
	for jid in ADMINS:
		GLOBACCESS[jid] = 300
		write_file(GLOBACCESS_FILE, str(GLOBACCESS))
	ACCBYCONFFILE = eval(read_file(ACCBYCONF_FILE))

register_command_handler(handler_access_login, COMM_PREFIX+'login', ['access','admin','all','*'], 0, 'Login as bot admin. Type this command only in Private!', COMM_PREFIX+'login <password>', [COMM_PREFIX+'login jay63xNer'])
register_command_handler(handler_user_login, COMM_PREFIX+'ulogin', ['access','admin','all','*'], 0, 'Login as a user. Type this command only in Private!', COMM_PREFIX+'ulogin <password>', [COMM_PREFIX+'login jay63xNer'])
register_command_handler(handler_access_login, COMM_PREFIX+'logout', ['access','admin','all','*'], 0, 'Logout as bot admin.', COMM_PREFIX+'logout', [COMM_PREFIX+'logout'])
register_command_handler(handler_access_view_access, COMM_PREFIX+'showacc', ['access','admin','all','*'], 0, 'Shows the access level specified nickname.\n-100 - complete ignore all messages from from such user at kernel level\n-1 - can not do anything\n0 - a very limited number of commands and macros, automatically assigned as visitor\n10 - standard set of commands and macros, automatically assigned participant\n11 - extended set of commands and macros (such as access to !!!), automatically assigned as member\n15 (16) - moderator set of commands and macros, automatically assigned as moderator\n20 - admin set of commands and macros, automatically assigned as admin\n30 - owner set of commands and macros, automatically assigned as owner\n40 - not implemented for all commands, allows the user access to some commands and leave th bot from the conferences\n100 - bot admin, all commands are allowed', COMM_PREFIX+'access [nick]', [COMM_PREFIX+'access', COMM_PREFIX+'access guy'])
register_command_handler(handler_access_set_access, COMM_PREFIX+'givetemp', ['access','admin','all','*'], 300, 'Set or remove local access for a particular nickname.\nWrite without level after the nick to remove the access, required the bot rejoin conference. If the third parameter "forever" specified, the change take place forever, otherwise the access dissapear when the bot rejoin the conference.\n-100 - complete ignore all messages from from such user at kernel level\n-1 - can not do anything\n0 - a very limited number of commands and macros, automatically assigned as visitor\n10 - standard set of commands and macros, automatically assigned participant\n11 - extended set of commands and macros (such as access to !!!), automatically assigned as member\n15 (16) - moderator set of commands and macros, automatically assigned as moderator\n20 - admin set of commands and macros, automatically assigned as admin\n30 - owner set of commands and macros, automatically assigned as owner\n40 - not implemented for all commands, allows the user access to some commands and leave th bot from the conferences\n100 - bot admin, all commands are allowed', COMM_PREFIX+'access_set <nick> <level> [forever]', [COMM_PREFIX+'access_set guy 100', COMM_PREFIX+'access_set guy 100 something'])
register_command_handler(handler_access_set_access_glob, COMM_PREFIX+'giveacc', ['access','superadmin','all','*'], 300, 'Set or remove global access for a particular nickname.\nWrite without level after the nick to remove the access.', COMM_PREFIX+'giveacc <nick> <level>', [COMM_PREFIX+'giveacc Nickname 300',COMM_PREFIX+'giveacc (nickname)'])

register_stage0_init(get_access_levels)
