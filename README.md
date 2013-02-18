Tron
====

The python xmpp bot

 First open config.py With notepad++ or pyton IDE
 
 then edit this: 
 
#-------------------------------------------------------------------------#
# Tron's configuration file                                               #  
#for help. join us on http://socialzone.mine.nu                           #
# Tron's Config file Rev 1.1                                              #
#-------------------------------------------------------------------------#
CONNECT_SERVER = gmail.com
PORT = 5222 
JID = socialzoneuk@gmail.com
PASSWORD = **********
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
DEFAULT_CHATROOM = support@conference.socialzone.mine.nu

# Chatroom nick
#---------------
DEFAULT_NICK = Tron

# Keep-alive period in seconds
#-----------------------------
KEEP_ALIVE = 300

# Jabber accounts that will administrate fatal
#---------------------------------------------
ADMINS = marcus@socialzone.mine.nu
ADMIN_PASSWORD = ************
USER_PASSWORD = tron4 # this will be explained in the next release