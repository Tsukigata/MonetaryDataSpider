# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MonetaryspiderPipeline:
    fp = None

    # 爬虫过程开始执行1次
    def open_spider(self, spider):
        print('爬虫开始')
        

    # 爬虫结束执行1次
    def close_spider(self, spider):
        print('爬虫结束')
        

    # 对提交的item对象，进行存储
    # 爬虫每次提交item，该方法被执行一次
    def process_item(self, item, spider):
        #取出数据
        stock_code = item['stock_code']
        date = item['date']
        deal_time = item['deal_time']  
        deal_price = item['deal_price'] 
        price_change = item['price_change']  
        deal_amount = item['deal_amount']  
        deal_amount_price = item['deal_amount_price']  
        deal_attribute = item['deal_attribute']
        #打开文件存储，注意修改文件的路径
        self.fp = open('D:\monetarySpider\data\\' + str(stock_code) + '-'+str(date) + '.txt', 'a', encoding='utf-8')
        self.fp.write(stock_code + '\t' + date + '\t'  + deal_time + '\t' + deal_price + '\t' + price_change + '\t' + deal_amount + '\t' + deal_amount_price + '\t' + deal_attribute + '\t' +'\n')
        #关闭文件
        self.fp.close()
        return item

class MonetaryspiderPipelineRealtime:
    fp = None
    id_set = set()
    # 爬虫过程开始执行1次,用来打开文件
    def open_spider(self, spider):
        print('爬虫开始')
        

    # 爬虫结束执行1次
    def close_spider(self, spider):
        print('爬虫结束')
        self.fp.close()

    # 对提交的item对象，进行存储
    # 爬虫每次提交item，该方法被执行一次
    def process_item(self, item, spider):
        # 1. 取出数据
        stock_code = item['stock_code']
        date = item['date']
        ticktime = item['ticktime']  
        price = item['price'] 
        pricechange = item['pricechange']  
        amount = item['amount']  
        volume = item['volume']  
        changepercent = item['changepercent']
        #考虑到实施爬虫的特殊性，在这里加入数据去重机制，通过集合完成
        if item['ticktime'] + item['stock_code']  not in self.id_set:
            # 2. 打开文件存储，注意修改文件的路径
            self.fp = open('D:\monetarySpider\RealData\\' + str(stock_code) + str(date) + '.txt', 'a', encoding='utf-8')
            self.fp.write(stock_code + '\t' + date + '\t'  + ticktime + '\t' + price + '\t' + pricechange + '\t' + volume + '\t' + amount + '\t' + changepercent + '\t' +'\n')
            self.id_set.add(item['ticktime'] + item['stock_code'])
            return item