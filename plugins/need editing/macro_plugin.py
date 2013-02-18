#===istalismanplugin===
# -*- coding: utf-8 -*-

#  Talisman plugin
#  macro_plugin.py

#  Initial Copyright © 2007 dimichxp <dimichxp@gmail.com>
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

def macroadd_handler(type, source, parameters):
	pl = MACROS.parse_cmd(parameters)
	if (len(pl)<2):
		reply(type, source, u'Few arguments!')
		return
	else:
		if pl[1].split()[0] in COMMAND_HANDLERS or pl[1].split()[0] in MACROS.gmacrolist or pl[1].split()[0] in MACROS.macrolist[source[1]]:
			real_access = MACROS.get_access(pl[1].split()[0], source[1])
			if real_access < 0 and pl[1].split()[0] in COMMAND_HANDLERS:
				real_access = COMMANDS[pl[1].split()[0]]['access']
			else:
				pass
			if real_access:
				if not has_access(source, real_access, source[1]):
					reply(type, source, u'Dreaming! ]:->')
					return
		else:
			reply(type, source, u'I do not see the command inside the macro!')
			return	
		command=pl[1].split(' ')
		MACROS.add(pl[0], pl[1], source[1])
		
		if command[0] in COMMAND_HANDLERS:
			gaccess=COMMANDS[command[0]]['access']
			MACROS.give_access(pl[0],gaccess,source[1])
			time.sleep(1)
		elif command[0] in MACROS.accesslist[source[1]]:
			gaccess=MACROS.accesslist[source[1]][command[0]]
			MACROS.give_access(pl[0],gaccess,source[1])
			time.sleep(1)
		
		MACROS.flush()
		reply(type, source, u'Added!')
	
def gmacroadd_handler(type, source, parameters):
	pl = MACROS.parse_cmd(parameters)
	if (len(pl)<2):
		rep = u'Few arguments!'
	else:
		command=pl[1].split(' ')
		MACROS.add(pl[0], pl[1])
		
		if command[0] in COMMAND_HANDLERS:
			gaccess=COMMANDS[command[0]]['access']
			MACROS.give_access(pl[0],gaccess)
			time.sleep(1)
			write_file('dynamic/macroaccess.txt', str(MACROS.gaccesslist))
		elif command[0] in MACROS.gaccesslist:
			gaccess=MACROS.gaccesslist[command[0]]
			MACROS.give_access(pl[0],gaccess)
			time.sleep(1)
			write_file('dynamic/macroaccess.txt', str(MACROS.gaccesslist))
		
		write_file('dynamic/macros.txt', str(MACROS.gmacrolist))
		rep = u'Added!'
	reply(type, source, rep)

def macrodel_handler(type, source, parameters):
	if parameters:
		MACROS.remove(parameters, source[1])
		MACROS.remove_access(parameters, source[1])
#		write_file('dynamic/'+source[1]+'macros.txt', str(MACROS.macrolist[source[1]]))
		MACROS.flush()
		rep = u'Deleted!'
	else:
		rep = u'Few arguments!'
	reply(type, source, rep)
	
def gmacrodel_handler(type, source, parameters):
	if parameters:
		MACROS.remove(parameters)
		MACROS.remove_access(parameters)
		write_file('dynamic/macros.txt', str(MACROS.gmacrolist))
		rep = u'Deleted!'
	else:
		rep = u'Few arguments!'
	reply(type, source, rep)

def macroexpand_handler(type, source, parameters):
	if parameters:
		rep=MACROS.comexp(parameters, source)
		if not rep:
			rep = u'Not disclosed. Insufficient privileges!'
	else:
		rep = u'Few arguments!'
	reply(type, source, rep)
	
def gmacroexpand_handler(type, source, parameters):
	if parameters:
		rep=MACROS.comexp(parameters, source, '1')
	else:
		rep = u'Few arguments!'
	reply(type, source, rep)

def macroinfo_handler(type, source, parameters):
	rep=''
	if parameters:
		try:
			if MACROS.macrolist[source[1]].has_key(parameters):
				rep = parameters+' -> '+MACROS.macrolist[source[1]][parameters]
		except:
			rep = u'There is no alias!'
	elif (parameters == 'all')  or (parameters == '*'):
		rep += '\n'.join([x+' -> '+ MACROS.macrolist[source[1]][x] for x in MACROS.macrolist[source[1]]])
	if not rep:
		rep=u'Not disclosed. Insufficient privileges!'
	reply(type, source, rep)
	
def gmacroinfo_handler(type, source, parameters):
	rep=''
	if parameters:
		if MACROS.gmacrolist.has_key(parameters):
			rep = parameters+' -> '+MACROS.gmacrolist[parameters]
		else:
			rep = u'There is no alias!'
	elif (parameters == 'all') or (parameters == '*'):
		rep += '\n'.join([x+' -> '+ MACROS.macrolist[x] for x in MACROS.macrolist])
	reply(type, source, rep)
	
def macrolist_handler(type, source, parameters):
	groupchat = source[1]
	is_gch = True
	
	if not GROUPCHATS.has_key(groupchat):
		is_gch = False
	
	rep,dsbll,dsblg,glist,llist=u'List of aliases: ',[],[],[],[]
	tglist = MACROS.gmacrolist.keys()
	
	if is_gch:
		if MACROS.macrolist[groupchat]:
			for macro in MACROS.macrolist[groupchat].keys():
				if macro in COMMOFF[groupchat]:
					dsbll.append(macro)
				else:
					llist.append(macro)
			dsbll.sort()
			llist.sort()
			if llist:
				rep += u'\nLOCAL\n'+', '.join(llist)
			if dsbll:
				rep+=u'\n\nThe following local aliases are disabled in this conference:\n'+', '.join(dsbll)
		else:
			rep+=''
	
		for macro in tglist:
			if macro in COMMOFF[groupchat]:
				dsblg.append(macro)
			else:
				glist.append(macro)
		dsblg.sort()
		glist.sort()
	else:
		dsblg = []
		tglist.sort()
		glist = tglist
	
	if glist:
		rep+=u'\nGLOBAL\n'+', '.join(glist)
	else:
		rep+=''
	
	if dsblg:
		rep+=u'\n\n The following global aliases are disabled in this conference:\n'+', '.join(dsblg)

	if type=='public':
		reply(type, source, u'Look in private!')
	if glist or llist:
		reply('private', source, rep)
	elif not glist and not llist:
		rep='List of aliases is empty!'
		reply('private', source, rep)
	
def macroaccess_handler(type, source, parameters):
	if parameters:
		args,access = parameters.split(' '),10
		if len(args)==2:
			macro = args[0]
			if macro in COMMAND_HANDLERS:
				if not user_level(source,source[1])==100:
					reply(type,source,u'Dreaming! ]:->')
					return
				else:
					pass
			elif macro in MACROS.gmacrolist or macro in MACROS.macrolist[source[1]]:
				real_access = MACROS.get_access(macro, source[1])
				if real_access < 0:
					pass
				else:
					if not has_access(source, real_access, source[1]):
						reply(type,source,u'Dreaming! ]:->')
						return
			try:
				access = int(args[1])
			except:
				reply(type,source,u'Invalid syntax!')
				return
			MACROS.give_access(macro,access,source[1])
			reply(type,source,u'Дал!')
			time.sleep(1)
			MACROS.flush()
		elif MACROS.accesslist[source[1]].has_key(args[0]):
			groupchat=source[1]
			alias=args[0]
			rep=MACROS.accesslist[groupchat][alias]
			reply(type,source,str(rep))
		elif not MACROS.accesslist[source[1]].has_key(args[0]):
			command = ''
			if args[0] in MACROS.macrolist[source[1]]:
				macro_body=MACROS.macrolist[source[1]][args[0]]
				command=macro_body.split(' ')[0]
			else:
				reply(type,source,u'Select an existing alias!')
			
			if command in COMMAND_HANDLERS:
				rep=COMMANDS[command]['access']
				reply(type,source,str(rep))
			elif command in MACROS.accesslist[source[1]]:
				rep=MACROS.accesslist[source[1]][command]
				reply(type,source,str(rep))
			else:
				reply(type,source,u'The body of an alias does not contain a command or another existing alias, or access is not set!')
	else:
		reply(type,source,u'What a nonsense?')
			
def gmacroaccess_handler(type, source, parameters):
	if parameters:
		args = parameters.split(' ')
		if len(args)==2:
			macro = args[0]
			access = args[1]
			MACROS.give_access(macro,access)
			reply(type,source,u'Дал!')
			time.sleep(1)
			write_file('dynamic/macroaccess.txt', str(MACROS.gaccesslist))
		elif MACROS.gaccesslist.has_key(args[0]):
			alias=args[0]
			rep=MACROS.gaccesslist[alias]
			reply(type,source,str(rep))
		elif not MACROS.gaccesslist.has_key(args[0]):
			command = ''
			if args[0] in MACROS.gmacrolist:
				macro_body=MACROS.gmacrolist[args[0]]
				command=macro_body.split(' ')[0]
			else:
				reply(type,source,u'Select an existing alias!')
			
			if command in COMMAND_HANDLERS:
				rep=COMMANDS[command]['access']
				reply(type,source,str(rep))
			elif command in MACROS.gaccesslist:
				rep=MACROS.gaccesslist[command]
				reply(type,source,str(rep))
			else:
				reply(type,source,u'The body of an alias does not contain a command or another existing alias, or access is not set!')
	else:
		reply(type,source,u'What a nonsense?')	

register_command_handler(macroadd_handler, COMM_PREFIX+'alias_add', ['admin','alias','all','*'], 20, 'Add an alias. The alias must be enclosed in apostrophes `` !!!', COMM_PREFIX+'alias_add [name] [`body alias`]', [COMM_PREFIX+'alias_add glitch `say /me thought that all buggy`'])
register_command_handler(gmacroadd_handler, COMM_PREFIX+'galias_add', ['superadmin','alias','all','*'], 100, 'Add a global alias. The alias must be enclosed in quotes `` !!!', COMM_PREFIX+'galias_add [name] [`body alias`]', [COMM_PREFIX+'galias_add glitch `say /me thought that all buggy`'])
register_command_handler(macrodel_handler, COMM_PREFIX+'alias_del', ['admin','alias','all','*'], 20, 'Delete an alias.', COMM_PREFIX+'alias_del [name]', [COMM_PREFIX+'alias_del glitch'])
register_command_handler(gmacrodel_handler, COMM_PREFIX+'galias_del', ['superadmin','alias','all','*'], 100, 'Delete a global alias.', COMM_PREFIX+'galias_del [name]', [COMM_PREFIX+'galias_del glitch'])
register_command_handler(macroexpand_handler, COMM_PREFIX+'alias_exp', ['admin','alias','info','all','*'], 20, ' Expand an alias, i.e look at the finished alias raw.', COMM_PREFIX+'alias_exp [name] [parameters]', [COMM_PREFIX+'alias_exp admin бот'])
register_command_handler(gmacroexpand_handler, COMM_PREFIX+'galias_exp', ['superadmin','alias','info','all','*'], 100, 'Expand a global alias, ie look at the finished alias raw.', COMM_PREFIX+'galias_exp [name] [parameters]', [COMM_PREFIX+'galias_exp admin bot'])
register_command_handler(macroinfo_handler, COMM_PREFIX+'alias_info', ['admin','alias','info','all','*'], 20, 'View alias, i.e just watch looks like an alias. To see all the aliases instead write the name of a certain alias "all" or "*" without quotes.', COMM_PREFIX+'alias_info [name]', [COMM_PREFIX+'alias_info glitch',COMM_PREFIX+'alias_info all'])
register_command_handler(gmacroinfo_handler, COMM_PREFIX+'galias_info', ['superadmin','alias','info','all','*'], 100, 'View an alias (any), i.e just watch looks like an alias. To see all the aliases instead write the name of a certain alias "all" or "*" without quotes.', COMM_PREFIX+'galias_info [name]', [COMM_PREFIX+'galias_info glitch',COMM_PREFIX+'galias_info *'])
register_command_handler(macrolist_handler, COMM_PREFIX+'alias_list', ['help','alias','info','all','*'], 10, 'List all aliases.', COMM_PREFIX+'alias_list', [COMM_PREFIX+'alias_list'])
register_command_handler(macroaccess_handler, COMM_PREFIX+'alias_acc', ['admin','alias','all','*'], 20, 'Change access to a particular alias.', COMM_PREFIX+'alias_acc [alias] [access]', [COMM_PREFIX+'alias_acc glitch 10'])
register_command_handler(gmacroaccess_handler, COMM_PREFIX+'galias_acc', ['superadmin','alias','all','*'], 100, 'Change access to a specific alias (any).', COMM_PREFIX+'galias_acc [alias] [access]', [COMM_PREFIX+'galias_acc admin 20'])