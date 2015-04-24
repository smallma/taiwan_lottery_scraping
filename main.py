# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import time
from random import randint
import sys
import re
import urllib2
from urllib import urlopen
 
reload(sys)
sys.setdefaultencoding('utf8')

links = []
for j in range(3):
    year = j + 102
    for i in range(200):
        counter = '0'
        if (i ) > 9:
            counter = `(i)`
        else:
            counter += `(i)`

        links.append('http://lotto.9800.com.tw/649/' + `year` + '0' + counter + '.html')
print links

# links = ['http://lotto.9800.com.tw/649/102001.html']

lottery_list = open('lottery_list.txt','w')

shop_links=[]
for link in links:
    print link

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

    lotteryType = 0
    try:
        title = section.find('h1').getText()
        if '大樂透' in title:
            lotteryType = 1
    except Exception as e:
        title = ''

    try:
        tables = section.find_all('table')
        tableslen = len(tables)
        td_balls = tables[tableslen - 1].find_all('td', {'class': 'td_ball'})
    except Exception as e:
        td_balls = []


    try:
        desciption = section.find('div', id='info').getText()
        drawNo = desciption.split(' | ')[0].split('：')[1]
        drawDate = desciption.split(' | ')[1].split('：')[1]
    except Exception as e:
        drawNo = ''
        drawDate = ''


    numbers = []
    specialNum = '';
    for td_ball in td_balls:
        try:
            specialDom =  td_ball.find('font')
            if specialDom:
                specialNum = specialDom.getText().encode('utf-8')
            else:
                numbers.append(int(td_ball.getText().encode('utf-8')))
        except Exception as e:
            pass


    print title + desciption
    print 'specialNum: ' + specialNum
    print 'numbers: ' + str(numbers)

    results = '{ "title": "' + title + '", "lotteryType": ' + str(lotteryType) + ',  "drawNo": "' + drawNo + '", "drawDate": "' + drawDate + '", "specialNum": ' + specialNum.encode("utf-8") + ', "normalNums": ' + str(numbers) + ' }'


    lottery_list.write(results + "\n")
    
    
    time.sleep(randint(1,5))
    sys.stdout.flush()
 
lottery_list.close()