#!/user/bin/env python
#-*- coding: UTF-8 -*- 

import datetime
import time
import schedule
import sys

from parse_rest.connection import register, ParseBatcher
from parse_rest.datatypes import Function

from lottery import latestAward, jackpot
# from test import pytesser
from config import parse

reload(sys)
sys.setdefaultencoding('utf8')

APPLICATION_ID = parse.getApplicationId()
REST_API_KEY = parse.getApiKey()

# Alias the Object type to make clear is not a normal python Object
# from parse_rest.datatypes import Object as ParseObject

# printSubTitle("First register the app")


def _getLatestAward():
	print '=== latest award ==='
	# nowTime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
	latestAwardResults = latestAward.get()
	# latestAwardFile = open('results/latestAward.txt', 'w')
	# latestAwardFile.write(str(latestAwardResults).replace('\'', '"'))
	# latestAwardFile.close()

	# print '  upload latest award   '
	latestAward_func = Function("createDrawsInfo")
	latestAward_func(drawsInfo=latestAwardResults)
	# print '=== ===== end ===== ==='

def _getJackpot():
	print '=== jackpots ==='
	# nowTime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
	jackpotResults = jackpot.get()
	# jackpotFile = open('results/jackpots.txt', 'w')
	# jackpotFile.write(str(jackpotResults).replace('\'', '"'))
	# jackpotFile.close()

	# print '    upload jackpots   '
	updateJackpots_func = Function("updateJackpots")
	updateJackpots_func(jackpots=jackpotResults['jackpots'])
	# print '=== ===== end ===== ==='

def main():
	# _getJackpot()
	# _getLatestAward()

	register(APPLICATION_ID, REST_API_KEY)


	schedule.every(1).minutes.do(_getJackpot)
	schedule.every(1).minutes.do(_getLatestAward)

	while True:
	    schedule.run_pending()
	    time.sleep(1)
	# pytesser.test2()

if __name__ == '__main__':
	main()