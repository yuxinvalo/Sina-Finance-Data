# coding: utf-8


import scrapy
from urllib.parse import urlparse, parse_qs

class AllStocks(scrapy.Spider):
    name = "allStocks"   
    def start_requests(self):
        pages = 464
        urls = []
        for i in range(0, 464):
            x = i + 1
            url = 'http://stock.finance.sina.com.cn/usstock/api/jsonp.php//US_CategoryService.getList?page='+str(x)+'&num=20&sort=&asc=0&market=&id='
            urls.append(url)
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

        
    def parse(self, response):
        num = str(parse_qs(urlparse(response.url).query)['page'][0])
        filename = 'allStocks-%s.json' % num
        data = str(response.body, 'gbk')
        data = data[2:-3]
        open(filename, 'w').write(data)
            

# 60k url: https://stock.finance.sina.com.cn/usstock/api/jsonp_v2.php/var%20_MSFT_60_1548714405787=/US_MinKService.getMinK?symbol=MSFT&type=60&___qn=3
