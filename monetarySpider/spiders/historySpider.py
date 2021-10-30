import scrapy
import json
from monetarySpider.items import MonetarydataItem
from scrapy.http.request import Request
import datetime
import calendar
import requests
from lxml import etree
import time
#爬取目标网站:新浪财经
#该爬虫设置了代理池，代理池中的内容在settings中进行修改，由于使用的是免费IP所以爬虫效率并不稳定
#关于代理池的设定在middlewas和settings中的IPPOOLS中进行
def judge(url):#判断该页的内容是否为空
    response = requests.get(url)#使用requests的get请求
    resp = etree.HTML(response.text)
    if resp.xpath('//tbody//tr/th[1]/text()') == []:#xpath提取内容
        return False
    else: 
        return True

class HistoryspiderSpider(scrapy.Spider):
    name = 'historySpider'
    allowed_domains = ['market.finance.sina.com.cn']
    #由于与实时爬虫在同一个项目中，所以设定了两套item及其pipeline处理机制，后续的数据处理机制在pipelines中进行
    custom_settings = {
        'ITEM_PIPELINES':{'monetarySpider.pipelines.MonetaryspiderPipeline':300}
    }
    def start_requests(self):#首先获取各个股票的股票代码
        #沪深A股
        for page in range(1,2):#现爬取第一页，沪深A股一共有58页
            base_url ='http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData?page='+str(page)+'&num=80&sort=symbol&asc=1&node=hs_a&symbol=&_s_r_a=page'
            yield Request(url = base_url,callback = self.parse_index)
        #考虑到爬虫效率问题，在这里只爬取沪深A股，后两者可以单独再进行爬取
        '''
        #创业板
        for page in range(1,2):#现爬取第一页，创业板一共有15页，下同
            base_url ='http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData?page='+str(page)+'&num=80&sort=symbol&asc=1&node=cyb&symbol=&_s_r_a=page'
            yield Request(url = base_url,callback = self.parse_index)   
        #科创板
        for page in range(1,2):#现爬取第一页，科创版一共有5页
            base_url ='http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData?page='+str(page)+'&num=80&sort=symbol&asc=1&node=kcb&symbol=&_s_r_a=page'
            yield Request(url = base_url,callback = self.parse_index)'''   
    def parse_index(self,response):#针对股票代码制定关于历史数据的url构造
        resp = json.loads(response.text)#请求的时json文件，要将其转化为字典
        date = datetime.date(2021,10,22)#从10月22号开始计算
        datedelta = datetime.timedelta(days = 1)#时间间隔为一天
        base_url = 'http://market.finance.sina.com.cn/transHis.php?symbol='
        for i in range(80):#每页有80个上市公司
            stock_code = resp[i]['symbol']#获取股票代码
            for day in range(14):#从所定日期开始向前14天
                #考虑到周末休市，所以要将星期六和星期天筛选出来
                if calendar.weekday(date.year, date.month, date.day) == 5 or calendar.weekday(date.year, date.month, date.day) == 6:
                    date = date - datedelta
                    continue
                for index in range(1,80):#每个指定网页最多有80页数据
                    #构造url
                    url = base_url + str(stock_code) + '&date=' + date.isoformat() + '&page=' + str(index)
                    '''由于不确定每页数据最后到底有多少，所以为了提高效率，分别在20，40，60页
                    时检测以此网站内容的有效性,如果监测页无效就停止向后的页面进行爬取'''
                    if index == 20 or index == 40 or index == 60:
                        time.sleep(2)#由于使用requests没有ip代理，为了防止被ban，所以降低检测的效率
                        if judge(url) == False:#使用预定义的judge函数判断
                            break
                    yield Request(url = url,callback = self.parse_data,meta = {'stock_code':stock_code,'date':date.isoformat(),'index':index})
                date = date - datedelta#天数减小一天
            date = datetime.date(2021,10,22)#这家公司请求结束后，下家公司的请求日期初始化
    def parse_data(self,response):
        item = MonetarydataItem()
        deal_time = response.xpath('//tbody//tr/th[1]/text()').extract()[1:-1]#交易时间
        if deal_time == []:#用于判断当前页是否有效（是否有内容）
            item['stock_code'] = response.meta['stock_code']
            item['date'] = response.meta['date']
            item['index'] = response.meta['index']
            print("Nil!")
            return None#无内容返回None
        deal_price = response.xpath('//tbody//tr/td[1]/text()').extract()[1:-1]#成交价格
        price_change = response.xpath('//tbody//tr/td[2]/text()').extract()[1:-1]#每次成交的价格变动
        deal_amount = response.xpath('//tbody//tr/td[3]/text()').extract()[1:-1]#成交量（手）
        deal_amount_price = response.xpath('//tbody//tr/td[4]/text()').extract()[1:-1]#成交额
        deal_attribute = response.xpath('//tbody//tr/th[2]//text()').extract()[:-1]#交易的属性时买盘还是卖盘或是中性盘
        #print(deal_time,deal_price)
        for i in range(len(deal_time)):#将每一条交易记录单独作为一个item，将其全部爬取
            item['index'] = response.meta['index']
            item['stock_code'] = response.meta['stock_code']
            item['date'] = response.meta['date']
            item['deal_time'] = deal_time[i]
            item['deal_price'] = deal_price[i]
            item['price_change'] = price_change[i]
            item['deal_amount'] = deal_amount[i]
            item['deal_amount_price'] = deal_amount_price[i]
            item['deal_attribute'] = deal_attribute[i]
            print('Success')
            yield item
           
       