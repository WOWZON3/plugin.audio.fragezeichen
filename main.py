# -*- coding: ISO-8859-1 -*-
# Module: default
# Author: YggDraz1l for EmuZONE
# Created on: 28.06.2018
# License: GPL v.3 https://www.gnu.org/copyleft/gpl.html

encoding="ISO-8859-1"
import sys
from urllib import urlencode
from urlparse import parse_qsl
import xbmcgui
import xbmcplugin

# Get the plugin url in plugin:// notation.
_url = sys.argv[0]
# Get the plugin handle as an integer number.
_handle = int(sys.argv[1])

# Free sample videos are provided by www.vidsplay.com
# Here we use a fixed set of properties simply for demonstrating purposes
# In a "real life" plugin you will need to get info and links to video files/streams
# from some web-site or online service.
VIDEOS = {'001 ... und der Superpapagei': [{'name': '01. Ein Hilferuf',
                       'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/001/folder.jpg',
                       'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/001/001.mp3',
                       'genre': 'Horror'},
                     {'name': '02. Ein Papagei spricht Latein',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/001/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/001/002.mp3',
                      'genre': 'Rock'},
                     {'name': '03. Schneewittchen ist verschwunden',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/001/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/001/003.mp3',
                      'genre': 'Rock'},
                      {'name': '04. Ein unverhoffter Besuch',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/001/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/001/004.mp3',
                      'genre': 'Rock'},
                     {'name': '05. Blackbeard der Pirat',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/001/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/001/005.mp3',
                      'genre': 'Rock'},
                      {'name': '06. Die rätselhafte Botschaft',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/001/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/001/006.mp3',
                      'genre': 'Rock'},
                     {'name': '07. Von Steinen und Gebeinen',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/001/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/001/007.mp3',
                      'genre': 'Rock'},
                      {'name': '08. Blackbeard hat das letzte Wort',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/001/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/001/008.mp3',
                      'genre': 'Rock'}
                      
                      ],
                      

'002 ... und der Phantomsse': [{'name': '01. Die Seemanstruhe',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/002/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/002/001.mp3',
                      'genre': 'Rock'},
{'name': '02. Das Wrack der Argyll Queen',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/002/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/002/002.mp3',
                      'genre': 'Rock'},
{'name': '03. Angriff',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/002/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/002/003.mp3',
                      'genre': 'Rock'},
{'name': '04. Die Goldgräberstadt',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/002/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/002/004.mp3',
                      'genre': 'Rock'},
{'name': '05. Beistand aus der Geisterwelt',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/002/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/002/005.mp3',
                      'genre': 'Rock'},
{'name': '06. Und wieder Java-Jim',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/002/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/002/006.mp3',
                      'genre': 'Rock'},
{'name': '07. Der letzte Fingerzeig',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/002/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/002/007.mp3',
                      'genre': 'Rock'},
{'name': '08. Der Schatz der Argyll Queen',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/002/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/002/008.mp3',
                      'genre': 'Rock'}

 ],

'005 ... und der Fluch des Rubins': [{'name': '01. Ein Anruf für die drei Fragezeichen',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/005/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/005/001.mp3',
                      'genre': 'Rock'},
{'name': '02. Zu Hilfe!',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/005/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/005/002.mp3',
                      'genre': 'Rock'},
{'name': '03. Dreipunkt taucht auf',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/005/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/005/003.mp3',
                      'genre': 'Rock'},
{'name': '04. Ein Herr mit schwarzem Schnurrbart',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/005/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/005/004.mp3',
                      'genre': 'Rock'},
{'name': '05. Bob hat eine Erleuchtung',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/005/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/005/005.mp3',
                      'genre': 'Rock'},
{'name': '06. Mädchenstimme am Telefon',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/005/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/005/006.mp3',
                      'genre': 'Rock'},
{'name': '07. Des Rätsels Lösung',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/005/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/005/007.mp3',
                      'genre': 'Rock'},
{'name': '08. Gebt mir das feurige Auge',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/005/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/005/008.mp3',
                      'genre': 'Rock'} 

 ],

'006 ... und der sprechende Totenkopf': [{'name': '01. Justus kauft einen Koffer',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/006/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/006/001.mp3',
                      'genre': 'Rock'},
{'name': '02. Ein sonderbarer Besuch',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/006/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/006/002.mp3',
                      'genre': 'Rock'},
{'name': '03. Eine geheimnisvolle Botschaft',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/006/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/006/003.mp3',
                      'genre': 'Rock'},
{'name': '04. Abschied von Sokrates',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/006/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/006/004.mp3',
                      'genre': 'Rock'},
{'name': '05. Warnung vom Polizeichef',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/006/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/006/005.mp3',
                      'genre': 'Rock'},
{'name': '06. Die drei Fragezeichen entdecken Spuren',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/006/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/006/006.mp3',
                      'genre': 'Rock'},
{'name': '07. Die Suchaktion beginnt',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/006/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/006/007.mp3',
                      'genre': 'Rock'},
{'name': '08. Wo ist das Geld?',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/006/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/006/008.mp3',
                      'genre': 'Rock'} 


],

'007 ... und der unheimliche Drache': [{'name': '01. Das Ungeheuer aus dem Meer',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/007/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/007/001.mp3',
                      'genre': 'Rock'},
{'name': '02. Ein merkwürdiges Haus',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/007/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/007/002.mp3',
                      'genre': 'Rock'},
{'name': '03. Erste Spuren',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/007/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/007/003.mp3',
                      'genre': 'Rock'},
{'name': '04. Gespenstische Botschaft am Telefon',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/007/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/007/004.mp3',
                      'genre': 'Rock'},
{'name': '05. Alte Chronik - neue Spur',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/007/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/007/005.mp3',
                      'genre': 'Rock'},
{'name': '06. Ein Witzbold',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/007/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/007/006.mp3',
                      'genre': 'Rock'},
{'name': '07. Die Drachenjagd beginnt',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/007/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/007/007.mp3',
                      'genre': 'Rock'},
{'name': '08. Das Geheimnis des alten Tunnels',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/007/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/007/008.mp3',
                      'genre': 'Rock'}

 ],

'008 ... und der grüne Geist': [{'name': '01. Ein Schrei in der Nacht',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/008/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/008/001.mp3',
                      'genre': 'Rock'},
{'name': '02. Die Geheimniskammer',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/008/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/008/002.mp3',
                      'genre': 'Rock'},
{'name': '03. Der Geist kehrt zurück',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/008/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/008/003.mp3',
                      'genre': 'Rock'},
{'name': '04. Ein Pferd geht durch',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/008/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/008/004.mp3',
                      'genre': 'Rock'},
{'name': '05. Wohin mit den Geisterperlen',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/008/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/008/005.mp3',
                      'genre': 'Rock'},
{'name': '06. Das Geheimnis der Geisterperlen',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/008/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/008/006.mp3',
                      'genre': 'Rock'},
{'name': '07. Justus findet eine Spur',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/008/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/008/007.mp3',
                      'genre': 'Rock'},
{'name': '08. Die rätselhafte 39',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/008/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/008/008.mp3',
                      'genre': 'Rock'}  


],

'009 ... und die rätselhaften Bilder': [{'name': '01. Eine schwarze Gestalt',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/009/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/009/001.mp3',
                      'genre': 'Rock'},
{'name': '02. Kundschaft auf dem Schrottplatz',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/009/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/009/002.mp3',
                      'genre': 'Rock'},
{'name': '03. Der Hinkende',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/009/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/009/003.mp3',
                      'genre': 'Rock'},
{'name': '04. Gefangen!',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/009/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/009/004.mp3',
                      'genre': 'Rock'},
{'name': '05. Ein schwarzes Loch',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/009/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/009/005.mp3',
                      'genre': 'Rock'},
{'name': '06. Justus Kombiniert',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/009/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/009/006.mp3',
                      'genre': 'Rock'},
{'name': '07. Zick oder Zack',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/009/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/009/007.mp3',
                      'genre': 'Rock'},
{'name': '08. Justus bringt es an den Tag',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/009/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/009/008.mp3',
                      'genre': 'Rock'}


],

'010 ... und die flüsternde Mumie': [{'name': '01. Eine Mumie flüstert',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/010/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/010/001.mp3',
                      'genre': 'Rock'},
{'name': '02. Der Fluch des Ra-Orkon',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/010/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/010/002.mp3',
                      'genre': 'Rock'},
{'name': '03. Überall lauert Gefahr',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/010/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/010/003.mp3',
                      'genre': 'Rock'},
{'name': '04. Eine gelungene Überraschung',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/010/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/010/004.mp3',
                      'genre': 'Rock'},
{'name': '05. Gefangen',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/010/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/010/005.mp3',
                      'genre': 'Rock'},
{'name': '06. Auf der Flucht',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/010/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/010/006.mp3',
                      'genre': 'Rock'},
{'name': '07. Viel zu viele Fragezeichen',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/010/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/010/007.mp3',
                      'genre': 'Rock'},
{'name': '08. Erstaunliches kommt an den Tag',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/010/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/010/008.mp3',
                      'genre': 'Rock'}


],

'011 ... und das Gespensterschloß': [{'name': '01. Man spricht vom Gespensterschloss',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/011/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/011/001.mp3',
                      'genre': 'Rock'},
{'name': '02. Echo aus dem Jenseits',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/011/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/011/002.mp3',
                      'genre': 'Rock'},
{'name': '03. In der Falle',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/011/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/011/003.mp3',
                      'genre': 'Rock'},
{'name': '04. Der Mann mit der Narbe',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/011/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/011/004.mp3',
                      'genre': 'Rock'},
{'name': '05. Die Warnung der Zigeunerin',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/011/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/011/005.mp3',
                      'genre': 'Rock'},
{'name': '06. Das blaue Phantom',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/011/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/011/006.mp3',
                      'genre': 'Rock'},
{'name': '07. Im Verlies',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/011/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/011/007.mp3',
                      'genre': 'Rock'},
{'name': '08. Erstaunliches kommt an den Tag',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/011/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/011/008.mp3',
                      'genre': 'Rock'}                                                                                                                                   

],

 '004 ... und die schwarze Katze': [{'name': '01. Haltet den Dieb',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/004/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/004/001.mp3',
                      'genre': 'Rock'},
{'name': '02. Peter beweist seinen Mut',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/004/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/004/002.mp3',
                      'genre': 'Rock'},
{'name': '03. Andy wundert sich',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/004/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/004/003.mp3',
                      'genre': 'Rock'},
{'name': '04. Wer sucht eine schwarze Katze',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/004/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/004/004.mp3',
                      'genre': 'Rock'},
{'name': '05. Der Mann mit der Tätowierung',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/004/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/004/005.mp3',
                      'genre': 'Rock'},
{'name': '06. In der Falle',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/004/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/004/006.mp3',
                      'genre': 'Rock'},
{'name': '07. Justus kombiniert',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/004/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/004/007.mp3',
                      'genre': 'Rock'},
{'name': '08. Der Räuber wird entlarvt',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/004/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/004/008.mp3',
                      'genre': 'Rock'}                                       

],
                      

'003 ... und der Karpartenhund': [{'name': '01. Es Spukt bei Mr. Prentice',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/003/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/003/001.mp3',
                      'genre': 'Rock'},
{'name': '02. Die Paste mit der Zauberkraft',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/003/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/003/002.mp3',
                      'genre': 'Rock'},
{'name': '03. Verräterische Flecken',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/003/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/003/003.mp3',
                      'genre': 'Rock'},
{'name': '04. Licht in der Kirche',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/003/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/003/004.mp3',
                      'genre': 'Rock'},
{'name': '05. Diagnose Vergiftung',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/003/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/003/005.mp3',
                      'genre': 'Rock'},
{'name': '06. Es knallt!',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/003/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/003/006.mp3',
                      'genre': 'Rock'},
{'name': '07. Es brennt!',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/003/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/003/007.mp3',
                      'genre': 'Rock'},
{'name': '08. Ein perfektes Alibi',
                      'thumb': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/003/folder.jpg',
                      'video': 'https://raw.githubusercontent.com/EmuZONE/YouTube/master/abks/2021/ddf/003/008.mp3',
                      'genre': 'Rock'}             
                      
                     ]}


def get_url(**kwargs):
    """
    Create a URL for calling the plugin recursively from the given set of keyword arguments.

    :param kwargs: "argument=value" pairs
    :type kwargs: dict
    :return: plugin call URL
    :rtype: str
    """
    return '{0}?{1}'.format(_url, urlencode(kwargs))


def get_categories():
    """
    Get the list of video categories.

    Here you can insert some parsing code that retrieves
    the list of video categories (e.g. 'Movies', 'TV-shows', 'Documentaries' etc.)
    from some site or server.

    .. note:: Consider using `generator functions <https://wiki.python.org/moin/Generators>`_
        instead of returning lists.

    :return: The list of video categories
    :rtype: types.GeneratorType
    """
    return VIDEOS.iterkeys()


def get_videos(category):
    """
    Get the list of videofiles/streams.

    Here you can insert some parsing code that retrieves
    the list of video streams in the given category from some site or server.

    .. note:: Consider using `generators functions <https://wiki.python.org/moin/Generators>`_
        instead of returning lists.

    :param category: Category name
    :type category: str
    :return: the list of videos in the category
    :rtype: list
    """
    return VIDEOS[category]


def list_categories():
    """
    Create the list of video categories in the Kodi interface.
    """
    # Set plugin category. It is displayed in some skins as the name
    # of the current section.
    xbmcplugin.setPluginCategory(_handle, 'My Video Collection')
    # Set plugin content. It allows Kodi to select appropriate views
    # for this type of content.
    xbmcplugin.setContent(_handle, 'videos')
    # Get video categories
    categories = get_categories()
    # Iterate through categories
    for category in categories:
        # Create a list item with a text label and a thumbnail image.
        list_item = xbmcgui.ListItem(label=category)
        # Set graphics (thumbnail, fanart, banner, poster, landscape etc.) for the list item.
        # Here we use the same image for all items for simplicity's sake.
        # In a real-life plugin you need to set each image accordingly.
        list_item.setArt({'thumb': VIDEOS[category][0]['thumb'],
                          'icon': VIDEOS[category][0]['thumb'],
                          'fanart': VIDEOS[category][0]['thumb']})
        # Set additional info for the list item.
        # Here we use a category name for both properties for for simplicity's sake.
        # setInfo allows to set various information for an item.
        # For available properties see the following link:
        # https://codedocs.xyz/xbmc/xbmc/group__python__xbmcgui__listitem.html#ga0b71166869bda87ad744942888fb5f14
        # 'mediatype' is needed for a skin to display info for this ListItem correctly.
        list_item.setInfo('video', {'title': category,
                                    'genre': category,
                                    'mediatype': 'video'})
        # Create a URL for a plugin recursive call.
        # Example: plugin://plugin.video.example/?action=listing&category=Animals
        url = get_url(action='listing', category=category)
        # is_folder = True means that this item opens a sub-list of lower level items.
        is_folder = True
        # Add our item to the Kodi virtual folder listing.
        xbmcplugin.addDirectoryItem(_handle, url, list_item, is_folder)
    # Add a sort method for the virtual folder items (alphabetically, ignore articles)
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    # Finish creating a virtual folder.
    xbmcplugin.endOfDirectory(_handle)


def list_videos(category):
    """
    Create the list of playable videos in the Kodi interface.

    :param category: Category name
    :type category: str
    """
    # Set plugin category. It is displayed in some skins as the name
    # of the current section.
    xbmcplugin.setPluginCategory(_handle, category)
    # Set plugin content. It allows Kodi to select appropriate views
    # for this type of content.
    xbmcplugin.setContent(_handle, 'videos')
    # Get the list of videos in the category.
    videos = get_videos(category)
    # Iterate through videos.
    for video in videos:
        # Create a list item with a text label and a thumbnail image.
        list_item = xbmcgui.ListItem(label=video['name'])
        # Set additional info for the list item.
        # 'mediatype' is needed for skin to display info for this ListItem correctly.
        list_item.setInfo('video', {'title': video['name'],
                                    'genre': video['genre'],
                                    'mediatype': 'video'})
        # Set graphics (thumbnail, fanart, banner, poster, landscape etc.) for the list item.
        # Here we use the same image for all items for simplicity's sake.
        # In a real-life plugin you need to set each image accordingly.
        list_item.setArt({'thumb': video['thumb'], 'icon': video['thumb'], 'fanart': video['thumb']})
        # Set 'IsPlayable' property to 'true'.
        # This is mandatory for playable items!
        list_item.setProperty('IsPlayable', 'true')
        # Create a URL for a plugin recursive call.
        # Example: plugin://plugin.video.example/?action=play&video=http://www.vidsplay.com/wp-content/uploads/2017/04/crab.mp4
        url = get_url(action='play', video=video['video'])
        # Add the list item to a virtual Kodi folder.
        # is_folder = False means that this item won't open any sub-list.
        is_folder = False
        # Add our item to the Kodi virtual folder listing.
        xbmcplugin.addDirectoryItem(_handle, url, list_item, is_folder)
    # Add a sort method for the virtual folder items (alphabetically, ignore articles)
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    # Finish creating a virtual folder.
    xbmcplugin.endOfDirectory(_handle)


def play_video(path):
    """
    Play a video by the provided path.

    :param path: Fully-qualified video URL
    :type path: str
    """
    # Create a playable item with a path to play.
    play_item = xbmcgui.ListItem(path=path)
    # Pass the item to the Kodi player.
    xbmcplugin.setResolvedUrl(_handle, True, listitem=play_item)


def router(paramstring):
    """
    Router function that calls other functions
    depending on the provided paramstring

    :param paramstring: URL encoded plugin paramstring
    :type paramstring: str
    """
    # Parse a URL-encoded paramstring to the dictionary of
    # {<parameter>: <value>} elements
    params = dict(parse_qsl(paramstring))
    # Check the parameters passed to the plugin
    if params:
        if params['action'] == 'listing':
            # Display the list of videos in a provided category.
            list_videos(params['category'])
        elif params['action'] == 'play':
            # Play a video from a provided URL.
            play_video(params['video'])
        else:
            # If the provided paramstring does not contain a supported action
            # we raise an exception. This helps to catch coding errors,
            # e.g. typos in action names.
            raise ValueError('Invalid paramstring: {0}!'.format(paramstring))
    else:
        # If the plugin is called from Kodi UI without any parameters,
        # display the list of video categories
        list_categories()


if __name__ == '__main__':
    # Call the router function and pass the plugin call parameters to it.
    # We use string slicing to trim the leading '?' from the plugin call paramstring
    router(sys.argv[2][1:])
