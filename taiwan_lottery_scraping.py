# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import sys
import urllib2
from urllib import urlopen, urlencode


reload(sys)
sys.setdefaultencoding('utf8')

links = []


lottery_list = open('lottery_realtime_award.txt', 'w')

link = 'http://www.taiwanlottery.com.tw/index_new.aspx'
formData = urlencode({
    'Lotto649Control_history$DropDownList1': '2',
    'Lotto649Control_history$chk': 'radYM',
    'Lotto649Control_history$dropYear': '104',
    'Lotto649Control_history$dropMonth': '3',
    'Lotto649Control_history$btnSubmit': '查詢'
})

try:
    handler = urllib2.HTTPHandler()
    opener = urllib2.build_opener(handler)
    request = urllib2.Request(link, data=formData)
    request.add_header('Content-Type', 'application/json')
    request.get_method = lambda: 'POST'
    html = urllib2.urlopen(request)
    soup = BeautifulSoup(html, fromEncoding="GB2312")
except Exception, e:
    print 'skip ' + link


# try:
#     table = soup.findChildren('tr')
#     section = table[0]
# except Exception as e:
#     section = ''

rows = soup.findChildren('td')

print rows
try:
    for row in rows:
        print row.getText()
        cells = row.findChildren('td')
        for cell in cells:
            value = cell.string
            print value
except Exception as e:
    pass
# lottery_list.write('award: ' + award + '\n')
sys.stdout.flush()

lottery_list.close()
