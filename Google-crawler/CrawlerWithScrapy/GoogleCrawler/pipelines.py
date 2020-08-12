# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
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

def writeSQL(item):
    database = connect_sql()
    cursor = database.cursor()
    sql = "INSERT INTO releasetext_education(app_id, release_text) VALUES('%s', '%s')" % (
              item["appID"],  item['releaseText'])
    # cursor.execute(sql)
    # database.commit()
    # try:
    #     cursor.execute(sql)
    #     database.commit()
    # except:
    #     pass
    cursor.execute(sql)
    database.commit()
    database.close()

class GooglecrawlerPipeline:
    def process_item(self, item, spider):
        writeSQL(item)
        return item
