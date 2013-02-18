#===istalismanplugin===
# -*- coding: utf-8 -*-

# author ferym@jabbim.org.ru
# yandex search beta version plugin 1.0-beta
# for only http://jabbrik.ru

# update, fix parse html code


def handler_yandex(type, source, parameters):
    try:
      if parameters:
        req = urllib2.Request('http://yandex.ru/msearch?s=all&query='+parameters.encode('utf-8').replace(' ','%20').replace('@','%40'))
        req.add_header = ('User-agent', 'Mozilla/5.0')
        r = urllib2.urlopen(req)
        target = r.read()
        od = re.search('<li>',target)
        message = target[od.end():]
        message = message[:re.search('</li>',message).start()]
        message = '\n' + message.strip()
        message = message.replace('<a href="','reference to the source: ').replace('" target="_blank">','\n').replace('</a>','').replace('</div>','').replace('<b>','').replace('</b>','').replace('<br/>',' ').replace('<br>',' ').replace('<div class="info">',' ').replace('&lt;','<').replace('&gt;','>').replace('&quot;','"')
        reply(type, source, unicode(message,'UTF-8'))
      else:
        reply(type, source, u'and what to look for then?')
    except:
        reply(type, source, u'Sorry, not found')

register_command_handler(handler_yandex, 'yandex', ['all','mod','more info'], 10, 'Search  yandex', 'yandex <request>', ['yandex jabbrik\nby ferym'])
register_command_handler(handler_yandex, 'index', ['all','mod','more info], 10, 'Search  yandex', 'yandex <request>', ['яндекс jabbrik\nby ferym'])