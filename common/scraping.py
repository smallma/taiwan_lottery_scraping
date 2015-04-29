import urllib2
from urllib import urlopen, urlencode
from bs4 import BeautifulSoup


def getHtml(url):
    html = urllib2.urlopen(url).read()
    soup = BeautifulSoup(html, fromEncoding="GB18030")
    return soup


def find_all(soup, dom, attrs=''):
    try:
        if attrs:
            sections = soup.find_all(dom, attrs)
        else:
            sections = soup.find_all(dom)
    except Exception as e:
        print e
        sections = []

    return sections


def find(soup, dom, attrs=''):
    try:
        if attrs:
            sections = soup.find(dom, attrs)
        else:
            sections = soup.find(dom)
    except Exception, e:
        print e
        sections = ''

    return sections

def findById(soup, dom, id):
    try:
        sections = soup.find(dom, id=id)
    except Exception, e:
        print e
        sections = ''

    return sections


def exeRestApi(url, method, headers, formData):
    # handler = urllib2.HTTPHandler()
    # opener = urllib2.build_opener(handler)
    request = urllib2.Request(url, data=formData)
    for header in headers:
        request.add_header(header.key, header.value)
    request.get_method = lambda: method
    html = urllib2.urlopen(request)
    soup = BeautifulSoup(html, fromEncoding="GB2312")
    return soup
