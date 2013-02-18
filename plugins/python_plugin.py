#===istalismanplugin===
# -*- coding: utf-8 -*-

#  Talisman plugin
#  python_plugin.py

#  Initial Copyright © 2002-2005 Mike Mintz <mikemintz@gmail.com>
#  Modifications Copyright © 2007 Als <Als@exploit.in>
#  Parts of code Copyright © Bohdan Turkynewych aka Gh0st <tb0hdan[at]gmail.com>
#  Modifications Copyright © 2009 wd/lotusfeet <dao/yoga>

#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.

#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.

def shell_del_specs_sym(s):
	for c in [';', '&', '|', '`', '$', '\\','>','<']:
		s = s.replace(c, '#')
	return s

def handler_python_ssh(type, source, parameters):
	return_value=''
	if os.name=='posix':
		parameters=shell_del_specs_sym(parameters)
		pipe = os.popen('sh -c "%s" 2>&1' % (parameters.encode('utf8')))
		return_value = pipe.read()
		pipe.close()
	elif os.name=='nt':
		parameters=shell_del_specs_sym(parameters)
		pipe = os.popen('%s' % (parameters.encode('utf8')))
		return_value = pipe.read().decode('cp866')
		pipe.close
	reply(type, source, return_value)

def handler_python_eval(type, source, parameters):
	try:
		return_value = str(eval(unicode(parameters)))
	except:
		return_value = str(sys.exc_info()[0]) + ' - ' + str(sys.exc_info()[1])
	reply(type, source, return_value)

def handler_python_exec(type, source, parameters):
	if '\n' in parameters and parameters[-1] != '\n':
		parameters += '\n'
	try:
		exec unicode(parameters) in globals()
	except:
		reply(type, source, str(sys.exc_info()[0]) + ' - ' + str(sys.exc_info()[1]))

def handler_python_sh(type, source, parameters):
	return_value=''
	if os.name=='posix':
		pipe = os.popen('sh -c "%s" 2>&1' % (parameters.encode('utf8')))				
		return_value = pipe.read()
		pipe.close
	elif os.name=='nt':
		pipe = os.popen('%s' % (parameters.encode('utf8')))
		return_value = pipe.read().decode('cp866')
		pipe.close
	reply(type, source, return_value)
	
def handler_python_calc(type, source, parameters):
	parameters = parameters.strip()
	if re.sub('([' + string.digits +']|[\+\-\/\*\^\.])','',parameters).strip() == '':
	    try:
    		return_value = str(eval(parameters))
		time.sleep(1)
	    except:
		return_value = u'Научи меня это делать! :)'
	else:
		return_value = u'Ты глюк!'
	reply(type, source, return_value)

register_command_handler(handler_python_eval, COMM_PREFIX+'eval', ['superadmin','all', '*'], 100, 'Расчитывает и показывает заданное выражение питона.', COMM_PREFIX+'eval <выражение>', [COMM_PREFIX+'eval 1+1'])
register_command_handler(handler_python_exec, COMM_PREFIX+'exec', ['superadmin','all', '*'], 100, 'Выполняет выражение питона.', COMM_PREFIX+'exec <выражение>', [COMM_PREFIX+'exec pass'])
register_command_handler(handler_python_sh, COMM_PREFIX+'sh', ['superadmin','all', '*'], 100, 'Выполняет шелл команду.', COMM_PREFIX+'sh <команда>', [COMM_PREFIX+'sh ls'])
register_command_handler(handler_python_ssh, COMM_PREFIX+'ssh', ['superadmin','all', '*'], 100, 'Выполняет шелл команду, экранируя специальные символы, такие как: >, & и пр.', COMM_PREFIX+'ssh <команда>', [COMM_PREFIX+'ssh ls'])
register_command_handler(handler_python_calc, COMM_PREFIX+'calc', ['info','all', '*'], 10, 'Калькулятор.', COMM_PREFIX+'calc <выражение>', [COMM_PREFIX+'calc 1+2'])