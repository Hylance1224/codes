import scrapy
from GoogleCrawler.items import GoogleItem
from GoogleCrawler.Filter import filters
import re
import pymysql


def connect_sql():
    db = pymysql.connect(
        host='localhost',
        port=1108,
        user='root',
        passwd='root',
        db='googleplaystore',
        charset='utf8mb4'
    )
    return db


def getData():
    database = connect_sql()
    cursor = database.cursor()
    sql = "select id from education"
    cursor.execute(sql)
    results = cursor.fetchall()
    urls = []
    for result in results:
        app_id = result[0]
        url = 'https://play.google.com/store/apps/details?id='+app_id + '&hl=en'
        urls.append(url)
    database.close()
    return urls


class GoogleSpider(scrapy.Spider):
    name = 'google'
    allowed_domains = ['play.google.com']

    # start_urls = ['https://play.google.com/store/apps/details?id=appinventor.ai_kayipkayik.gps_map&hl=en']
    start_urls = getData()
    def parse(self, response):
        item = GoogleItem()
        rule = "https://play.google.com/store/apps/details\?id=(.*)&hl=en"
        r = re.findall(rule, response.url)
        item['appID'] = r[0]
        texts = response.xpath("//div[@jsname='bN97Pc']").extract()
        text = texts[1]
        text = filters(text)
        release_text = text.replace("'", "''")
        item['releaseText'] = release_text
        # print (item['releaseText'])
        yield item

