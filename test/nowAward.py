# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import sys
import urllib2
from urllib import urlopen, urlencode


reload(sys)
sys.setdefaultencoding('utf8')

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


jackpots = []

sequence = 0
for section in sections:
	top_dollar = section.find('div', {'class', 'top_dollar'})
	money = int(top_dollar.getText().strip().encode('utf-8'))

	if sequence == 0:
		jackpots.append({
            "typeId": 2,
            "money": money
        })
	elif sequence == 1:
		jackpots.append({
            "typeId": 4,
            "money": money
        })
	elif sequence == 2:
		jackpots.append({
            "typeId": 10,
            "money": money
        })
	sequence += 1
	
	
print {'jackpots': jackpots}


# updateUrl = 'https://www.parse.com/1/functions/updateAwards'
# formData = urlencode({'awards': awards})

# try:
#     handler = urllib2.HTTPHandler()
#     opener = urllib2.build_opener(handler)
#     request = urllib2.Request(updateUrl, data=formData)
#     request.add_header('X-Parse-Application-Id', 'ut6fRJ9i2DJ5SToZ6yizI8bW0QXXPeuGqg78RVkQ')
#     request.add_header('X-Parse-REST-API-Key', 'bHvXXFvufPveBXQyZrGNg6zVSrSacsw3dDQJhfOJ')
#     request.add_header('Content-Type', 'application/json')
#     request.get_method = lambda: 'POST'
#     print '1'
#     html = urllib2.urlopen(request)
#     print '2'
#     # soup = BeautifulSoup(html, fromEncoding="GB2312")
# except Exception, e:
# 	print e
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
