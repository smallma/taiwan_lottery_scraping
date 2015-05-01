#-*- coding: UTF-8 -*- 

from common import scraping


def get():
    url = 'http://www.taiwanlottery.com.tw/index_new.aspx'
    html = scraping.getHtml(url)
    jackpots = []
    sequence = 0

    sections = scraping.find_all(html, 'div', {'class': 'top_dollar_tx'})

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

    return {'jackpots': jackpots}