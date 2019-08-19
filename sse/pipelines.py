import mysql.connector
import logging


class MySQLPipeline(object):
    def __init__(self, db_config):
        self.db_config = db_config
        self.cnx = None
        self.cursor = None

    @classmethod
    def from_crawler(cls, crawler):
        db_config = {
            'user': crawler.settings.get('MYSQL_USER'),
            'password': crawler.settings.get('MYSQL_PASSWORD'),
            'host': crawler.settings.get('MYSQL_HOST'),
            'port': crawler.settings.get('MYSQL_PORT'),
            'database': crawler.settings.get('MYSQL_DB')
        }
        return cls(db_config)

    def open_spider(self, spider):
        self.cnx = mysql.connector.connect(**self.db_config)
        self.cursor = self.cnx.cursor()

    def close_spider(self, spider):
        self.cursor.close()
        self.cnx.close()

    def process_item(self, item, spider):
        add_quotes = 'INSERT INTO TB_STOCK_QUOTES '\
                     '(stock_code, stock_name, open_price, high_price, low_price, last_price, prev_price, chg_rate, '\
                     'volume, amount, trade_phase, chg_price, amp_rate, cpxxsubtype, cpxxprodusta, stock_total, '\
                     'trade_date, trade_time) '\
                     'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

        self.cursor.execute(add_quotes, (item['stock_code'], item['stock_name'], item['open_price'], item['high_price'],
                                         item['low_price'], item['last_price'], item['prev_price'], item['chg_rate'],
                                         item['volume'], item['amount'], item['trade_phase'], item['chg_price'],
                                         item['amp_rate'], item['cpxxsubtype'], item['cpxxprodusta'],
                                         item['stock_total'], item['trade_date'], item['trade_time']))

        self.cnx.commit()
        return item
