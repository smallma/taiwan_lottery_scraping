#-*- coding: UTF-8 -*- 

from lottery import latestAward
import sys
import datetime

reload(sys)
sys.setdefaultencoding('utf8')


if __name__ == '__main__':
	nowTime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
	latestAwardResults = latestAward.get()
	latestAwardFile = open('results/lottery_list_' + nowTime + '.txt', 'w')
	latestAwardFile.write(str(latestAwardResults))
	latestAwardFile.close()