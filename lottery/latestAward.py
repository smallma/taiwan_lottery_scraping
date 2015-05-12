#-*- coding: UTF-8 -*- 

from common import scraping

layoutSections = ['contents_box01', 'contents_box02', 'contents_box03', 'contents_box04', 'contents_box05']
lotteryMap = {
	'contents_logo_01': {
		'name': 'BINGO BINGO',
		'normalCount': 10,
		'specialCount': 1,
		'typeId': 1,
	},
	'contents_logo_02': {
		'name': '威力彩',
		'normalCount': 6,
		'specialCount': 1,
		'typeId': 2,
	},
	'contents_logo_03': {
		'name': '38樂合彩',
		'normalCount': 6,
		'specialCount': 0,
		'typeId': 3,
	},
	'contents_logo_04': {
		'name': '大樂透',
		'normalCount': 6,
		'specialCount': 1,
		'typeId': 4,
	},
	'contents_logo_05': {
		'name': '49樂合彩',
		'normalCount': 6,
		'specialCount': 0,
		'typeId': 5,
	},
	'contents_logo_06': {
		'name': '今彩539',
		'normalCount': 5,
		'specialCount': 0,
		'typeId': 6,
	},
	'contents_logo_07': {
		'name': '39樂合彩',
		'normalCount': 5,
		'specialCount': 0,
		'typeId': 7,
	},
	'contents_logo_08': {
		'name': '3星彩',
		'normalCount': 3,
		'specialCount': 0,
		'typeId': 8,
	},
	'contents_logo_09': {
		'name': '4星彩',
		'normalCount': 4,
		'specialCount': 0,
		'typeId': 9,
	},
	'contents_logo_10': {
		'name': '大福彩',
		'normalCount': 7,
		'specialCount': 0,
		'typeId': 10,
	}
}


def get():
    url = 'http://www.taiwanlottery.com.tw/index_new.aspx'
    html = scraping.getHtml(url)
    awards = []

    for layoutSection in layoutSections:
    	drawSections = scraping.find_all(html, 'div', {'class', layoutSection})
    	for section in drawSections:
    		award = {
    			# 'title': '',
    			# 'name': '',
    			'drawNo': '',
    			'typeId': '',
    			'special': [],
    			'winningNumbers': []
    		}

    		divs = section.find_all('div')
    		name = divs[0].get('id')
    		specialCount = lotteryMap[name]['normalCount']
    		normalCount = lotteryMap[name]['normalCount']
    		
    		# award['name'] = lotteryMap[name]['name'].decode('utf8')

    		title = section.find('span', {'class', 'font_black15'})
    		# award['title'] = title.getText().decode('utf8')
    		award['drawNo'] = str(title.getText().split(' 第')[1].split('期')[0])
    		awardDate = str(title.getText().split(' 第')[0]).split('/')
    		award['drawDate'] = str(int(awardDate[0]) + 1911) + '/' + awardDate[1] + '/' + awardDate[2]
    		award['typeId'] = lotteryMap[name]['typeId']

    		if specialCount > 0:
    			i = 0
    			ballReds = section.find_all('div', {'class', 'ball_red'})
    			for ballRed in ballReds:
    				if i > specialCount:
    					continue
    				i += 1
    				award['special'].append(int(ballRed.getText()))


    		normalDivs = section.find_all('div', {'class', 'ball_tx'})
    		for i in range(normalCount):
    			award['winningNumbers'].append(int(normalDivs[i].getText()))

    		awards.append(award)
    return awards