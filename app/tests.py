import requests
import scrapy
#
# payload = {'api_key': '07b03daede52b7e442bd62a5fb2db36e',
#            'url': 'https://www.digikala.com/search/category-mobile-phone/product-list/?brands%5B0%5D=1662'}
# r = requests.get('https://api.scraperapi.com/', params=payload)
# print(r.content.find('span'))

import requests

payload = {'api_key': '07b03daede52b7e442bd62a5fb2db36e', 'url': 'https://www.digikala.com/search/category-mobile-phone/product-list/?brands%5B0%5D=1662', 'render': 'true'}
r = requests.get('http://api.scraperapi.com', params=payload)
print(r.text)
# Scrapy users can simply replace the urls in their start_urls and parse function
# ...other scrapy setup code
start_urls = ['http://api.scraperapi.com?api_key=APIKEY&url=' + url + '&render=true']


def parse(self, response):
    # ...your parsing logic here
    yield scrapy.Request('http://api.scraperapi.com/?api_key=APIKEY&url=' + url + '&render=true', self.parse)

