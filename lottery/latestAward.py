#-*- coding: UTF-8 -*- 

from common import scraping

layoutSections = ['contents_box01', 'contents_box02', 'contents_box03', 'contents_box04']
mappingMap = {
	'contents_logo_01': {
		'name': u'BINGO BINGO',
		'normalCount': 10,
		'specialCount': 1
	},
	'contents_logo_02': {
		'name': u'威力彩',
		'normalCount': 6,
		'specialCount': 1
	},
	'contents_logo_03': {
		'name': u'38樂合彩',
		'normalCount': 6,
		'specialCount': 0
	},
	'contents_logo_04': {
		'name': u'大樂透',
		'normalCount': 6,
		'specialCount': 1
	},
	'contents_logo_05': {
		'name': u'49樂合彩',
		'normalCount': 6,
		'specialCount': 0
	},
	'contents_logo_06': {
		'name': u'今彩539',
		'normalCount': 5,
		'specialCount': 0
	},
	'contents_logo_07': {
		'name': u'39樂合彩',
		'normalCount': 5,
		'specialCount': 0
	},
	'contents_logo_08': {
		'name': u'3星彩',
		'normalCount': 3,
		'specialCount': 0
	},
	'contents_logo_09': {
		'name': u'4星彩',
		'normalCount': 4,
		'specialCount': 0
	},
	'contents_logo_10': {
		'name': u'大福彩',
		'normalCount': 7,
		'specialCount': 0
	}
}


def get():
    url = 'http://www.taiwanlottery.com.tw/index_new.aspx'
    html = scraping.getHtml(url)
    # print html
    
    for layoutSection in layoutSections:
    	drawSections = scraping.find_all(html, 'div', {'class', layoutSection})
    	for section in drawSections:
    		divs = section.find_all('div')
    		name = divs[0].get('id')
    		print mappingMap[name]['name'] + ': ' + str(mappingMap[name]['normalCount'])
    		specialCount = mappingMap[name]['normalCount']
    		normalCount = mappingMap[name]['normalCount']

    		title = section.find('span', {'class', 'font_black15'})
    		print 'title: ' + title.getText()
    		
    		if specialCount:
    			ballReds = section.find_all('div', {'class', 'ball_red'})
    			for ballRed in ballReds:
    				print 'Special Num: ' + str(int(ballRed.getText()))

    		normalDivs = section.find_all('div', {'class', 'ball_tx'})	
    		for i in range(normalCount):
    			print 'noraml num: ' + normalDivs[i].getText()

    		print '-------------------------\n'
