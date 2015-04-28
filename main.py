#-*- coding: UTF-8 -*- 

from lottery import latestAward
import sys


reload(sys)
sys.setdefaultencoding('utf8')


if __name__ == '__main__':
    latestAward.get()
