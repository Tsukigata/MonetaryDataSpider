# Scrapy settings for monetarySpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import scrapy
BOT_NAME = 'monetarySpider'

SPIDER_MODULES = ['monetarySpider.spiders']
NEWSPIDER_MODULE = 'monetarySpider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'monetarySpider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'monetarySpider.middlewares.MonetaryspiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware' : 123,
    'monetarySpider.middlewares.IPPOOlS' : 125
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'monetarySpider.pipelines.MonetaryspiderPipeline': 300,
    'monetarySpider.pipelines.MonetaryspiderPipelineRealtime':800
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

#解码格式为utf-8
FEED_EXPORT_ENCODING = 'utf-8'
# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

#可以在这里修改请求IP，由于使用的免费IP所以请求效率并不高，最后这批IP的更新日期为10-30 18：30
#IP来源于快代理，网址https://www.kuaidaili.com/free/inha
IPPOOL = [
    {"ipaddr": "58.215.201.98:56566"},
    {"ipaddr": "101.6.49.56:7890"},
    {"ipaddr": "39.105.144.138:81"},
    {"ipaddr": "121.237.88.172:3000"},
    {"ipaddr": "61.216.156.222:60808"},
    {"ipaddr": "106.55.15.244:8889"},
    {"ipaddr": "150.139.201.10:6969"},
    {"ipaddr": "119.180.134.193:8060"},
    {"ipaddr": "117.88.246.234:3000"},
    {"ipaddr": "106.55.15.244:8889"},
    {"ipaddr": "121.237.88.197:3000"},
    {"ipaddr": "221.225.10.177:8118"},
    {"ipaddr": "113.128.16.209:8118"},
    {"ipaddr": "27.191.60.107:3256"},
    {"ipaddr": "118.193.33.66:7890"},
    {"ipaddr": "175.153.233.52:8118"},
    {"ipaddr": "49.89.222.124:7082"},
    {"ipaddr": "61.216.156.222:60808"},
    {"ipaddr": "101.133.152.90:7788"},
    {"ipaddr": "58.20.234.243:9091"},
    {"ipaddr": "140.249.185.87:6969"},
    {"ipaddr": "8.136.6.248:7788"},
    {"ipaddr": "112.81.43.216:8888"},
    {"ipaddr": "106.55.148.166:7890"},
    {"ipaddr": "113.128.16.209:8118"},
    {"ipaddr": "49.85.112.173:7890"},
    {"ipaddr": "112.229.109.112:8118"},
    {"ipaddr": "120.220.220.95:8085"},
    {"ipaddr": "110.40.166.19:1081"},
    {"ipaddr": "112.81.43.216:8888"}
]