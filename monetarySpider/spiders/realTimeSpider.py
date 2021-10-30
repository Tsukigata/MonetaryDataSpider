import scrapy
import json
from monetarySpider.items import MonetaryRealItem
from scrapy.http.request import Request
import time

#由于使用的IP质量不高所以导致数据的实时性有所下降，关于代理池的设定在middlewas和settings中的IPPOOLS中进行
class RealtimespiderSpider(scrapy.Spider):
    name = 'realTimeSpider'
    allowed_domains = ['vip.stock.finance.sina.com.cn']
    start_urls = ['http://vip.stock.finance.sina.com.cn/']
    #使用另一套数据处理机制
    custom_settings = {
        'ITEM_PIPELINES':{'monetarySpider.pipelines.MonetaryspiderPipelineRealtime':300}
    }
    def start_requests(self):
        while True:#一旦运行就需要手动停止
            #沪深A股
            for page in range(1,5):#这里爬取5页，沪深A股一共有58页，下同
                base_url ='http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData?page='+str(page)+'&num=80&sort=symbol&asc=1&node=hs_a&symbol=&_s_r_a=page'
                yield Request(url = base_url,callback = self.parse_index,dont_filter = True)
                
            #创业板
            for page in range(1,4):#这里爬取5页，创业板一共有15页，下同
                base_url ='http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData?page='+str(page)+'&num=80&sort=symbol&asc=1&node=cyb&symbol=&_s_r_a=page'
                yield Request(url = base_url,callback = self.parse_index,dont_filter = True)   
            #科创板
            for page in range(1,2):#这里爬取5页，科创版一共有5页
                base_url ='http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData?page='+str(page)+'&num=80&sort=symbol&asc=1&node=kcb&symbol=&_s_r_a=page'
                yield Request(url = base_url,callback = self.parse_index,dont_filter = True)
            time.sleep(1)#1s的时间间隔，再次进行爬取
    def parse_index(self,response):
        resp = json.loads(response.text)
        date = time.strftime('%Y-%m-%d')#将当前的时间获取
        item = MonetaryRealItem()
        for i in range(80):
            item['date'] = date#交易日期
            item['stock_code'] = resp[i]['symbol']#股票代码
            item['ticktime'] = resp[i]['ticktime']#交易具体时间
            item['volume'] = str(resp[i]['volume'])#累计成交量
            item['amount'] = str(resp[i]['amount'])#累计成交额
            item['price'] = str(resp[i]['trade'])#股票当前价格
            item['pricechange'] = str(resp[i]['pricechange'])#价格变动
            item['changepercent'] = str(resp[i]['changepercent'])#价格变动百分比
            yield item
        
        
