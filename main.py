# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import time
from random import randint
import sys
import re
import urllib2
from urllib import urlopen

from datetime import date
from time import mktime
from time import strftime
from datetime import datetime
import datetime

 
reload(sys)
sys.setdefaultencoding('utf8')

links = []

for kind in ['649', '539', '38']:
    for j in range(3):
        year = j + 102
        counter = '0'
        for i in range(1, 400):
            if (i ) > 99:
                counter = `(i)`
            elif i < 10:
                counter = '00' + `(i)`
            else:
                counter = '0' + `(i)`

            links.append('http://lotto.9800.com.tw/' + kind + '/' + `year` + counter + '.html')
print links

# links = ['http://lotto.9800.com.tw/539/102001.html']

nowTime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

lottery_list = open('lottery_list_' + str(nowTime)+ '.txt','w')
lottery_list.write('{ "drawsInfo": [\n')
shop_links = []
for link in links:

    print '\n\n * ' + link

    try:
        html = urllib2.urlopen(link);
        soup = BeautifulSoup(html, fromEncoding="GB2312")
    except Exception, e:
        print 'skip ' + link
        continue

    try:
        section = soup.find('div', {'class': 'leftbox'})
    except Exception as e:
        section = ''

    typeId = 0
    try:
        title = section.find('h1').getText()
        if '威力彩' in title:
            typeId = 2
        if '大樂透' in title:
            typeId = 4
        if '539' in title:
            typeId = 6
    except Exception as e:
        title = ''

    try:
        tables = section.find_all('table')
        tableslen = len(tables)
        td_balls = tables[tableslen - 1].find_all('td', {'class': 'td_ball'})
    except Exception as e:
        td_balls = []


    drawNo = ''
    drawUnixTime = ''

    try:
        desciption = section.find('div', id='info').getText()
        drawNo = desciption.split(' | ')[0].split('：')[1]
        drawDate = desciption.split(' | ')[1].split('：')[1].split('-')
        start = date(int(drawDate[0]), int(drawDate[1]), int(drawDate[2]))
        ms = mktime(start.timetuple())
        ms += 72000
        drawUnixTime = datetime.fromtimestamp(ms).strftime('%Y-%m-%d %H:%M:%S')
    except Exception as e:
        pass


    numbers = []
    special = '';
    for td_ball in td_balls:
        try:
            specialDom =  td_ball.find('font')
            if specialDom:
                special = int(specialDom.getText().encode('utf-8'))
            else:
                numbers.append(int(td_ball.getText().encode('utf-8')))
        except Exception as e:
            pass


    # print title + desciption
    # print 'special: ' + special
    # print 'numbers: ' + str(numbers)

    results = '{ "title": "' + title + '", "typeId": ' + str(typeId) + ',  "drawNo": "' + drawNo + '", "drawDate": "' + drawUnixTime + '", "special": [' + special + '], "winningNumbers": ' + str(numbers) + ' },'


    print results

    lottery_list.write(results + "\n")
    
    
    time.sleep(randint(1, 2))
    sys.stdout.flush()

lottery_list.write("]}\n")
lottery_list.close()