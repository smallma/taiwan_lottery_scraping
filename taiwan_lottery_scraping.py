# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import sys
import urllib2
from urllib import urlopen


# reload(sys)
sys.setdefaultencoding('utf8')

links = []


lottery_list = open('lottery_realtime_award.txt', 'w')

link = 'http://www.taiwanlottery.com.tw/index_new.aspx'
formData = {
    'Lotto649Control_history$DropDownList1': 2,
    'Lotto649Control_history$chk': 'radYM',
    'Lotto649Control_history$dropYear': 104,
    'Lotto649Control_history$dropMonth': 3,
    'Lotto649Control_history$btnSubmit': '查詢'
}

try:
    request = urllib2.Request(link)
    request.get_method = lambda: 'POST'
    html = urllib2.urlopen(request, formData)
    soup = BeautifulSoup(html, fromEncoding="GB2312")
except Exception, e:
    print 'skip ' + link


try:
    section = soup.find('div', {'class': 'top_dollar_tx'})
except Exception as e:
    section = ''

try:
    tables = section.find_all('div', {'class': 'top_dollar'})
    award = tables.getText()
except Exception as e:
    award = ''

lottery_list.write('award: ' + award + '\n')
sys.stdout.flush()

lottery_list.close()
