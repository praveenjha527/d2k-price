from lxml import html
import gevent.monkey

gevent.monkey.patch_socket()
import requests

from gevent.pool import Pool

pagination_limit = 55099

companies_link_xpath = '//table[@class="table table-striped col-md-12 col-sm-12 col-xs-12"]//tr//td//a/@href'


def url_crawler():
    all_url = []
    count = 0
    count += 1
    for item in range(pagination_limit):
        url = 'https://www.zaubacorp.com/company-list/p-' + str(item) + '-company.html'
        page = requests.get(url)
        tree = html.fromstring(page.text)
        company_url = tree.xpath(companies_link_xpath)
        all_url.append(company_url)
    return all_url

def StartCrawl():
    pass