from common import scraping


def get():
    url = 'http://www.taiwanlottery.com.tw/index_new.aspx'
    html = scraping.getHtml(url)
    print html
