#-------------------------------------------------------------------------#
# Tron's configuration file                                               #  
#for help. join us on http://socialzone.mine.nu                           #
# Tron's Config file Rev 1.1                                              #
#-------------------------------------------------------------------------#
CONNECT_SERVER = xtreme.im
PORT = 5222 
JID = tron@xtreme.im
PASSWORD = 
RESOURCE = PyTron

# TLS/SSL, if no need, comment or leave as is
#---------------------------------------------
USE_TLS_SSL = 1

# Proxy server, if there is a proxy, simply uncomment this params
#----------------------------------------------------------------
# PROXY_HOST = 148.233.239.23
# PROXY_PORT = 80
# PROXY_USER = someuser
# PROXY_PASSWORD = secret

# Default chatroom, uncomment and specify if needed
#--------------------------------------------------
DEFAULT_CHATROOM = socialzone@conference.xmpp.ru

# Chatroom nick
#---------------
DEFAULT_NICK = Tron

# Keep-alive period in seconds
#-----------------------------
KEEP_ALIVE = 300

# Jabber accounts that will administrate fatal
#---------------------------------------------
ADMINS = admin-of-bot@xtreme.im
ADMIN_PASSWORD = 
USER_PASSWORD = tron4 # this will be explained in the next release

# Controls delivery of all private-messages in bot-roster to admin jids
#----------------------------------------------------------------------
ADMINS_DELIVERY = 1

# Controls delivery of all core exceptions to admin jids, for debug
#------------------------------------------------------------------
ERRORS_DELIVERY = 1

# Controls autosubscribe
#-----------------------
AUTO_SUBSCRIBE = 1

# fatal-bot will try to reconnect on disconnections
#--------------------------------------------------
AUTO_RESTART = 1

# Controls hide/show of tron-bot console at startup
#---------------------------------------------------
SHOW_CONSOLE = 1

# Tron's Command prefix. For example: . or !
#----------------------------------------------------------
COMM_PREFIX = $

# Msg chatrooms&private limits
#-----------------------------
MSG_CHATROOM_LIMIT = 5000
MSG_PRIVATE_LIMIT = 10000

# Where to store HTML files from chatrooms logs
# To disable logging simply comment this param
#----------------------------------------------
 PUBLIC_LOG_DIR = logs

# Where to store logs of private chats
# To disable logging simply comment this param
#---------------------------------------------
 #PRIVATE_LOG_DIR = privlogs

# If not null bot reloads plugins and core with changed source-code
# Specifies interval (in minutes) when check and reload changed code
#-------------------------------------------------------------------
RELOAD_CODE = 0

# End of tron's configuration file
#------------------------------------
