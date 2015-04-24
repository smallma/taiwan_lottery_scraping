# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import sys
import urllib2
from urllib import urlopen


reload(sys)
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
    sections = soup.find_all('div', {'class': 'top_dollar_tx'})
except Exception as e:
    sections = []



for section in sections:
	top_dollar = section.find('div', {'class', 'top_dollar'})
	print top_dollar.getText().strip()
	

# try:
#     section = soup.find('div', {'class': 'top_dollar_tx'})
# except Exception as e:
#     section = ''

# try:
#     tables = section.find_all('div', {'class': 'top_dollar'})
#     for table in tables:
#     	award = tables.getText().encode('utf-8')
#     	print award
#     	lottery_list.write('award: ' + award + '\n')

# except Exception as e:
#     pass

sys.stdout.flush()

lottery_list.close()
