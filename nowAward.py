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

try:
    html = urllib2.urlopen(link)
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
