import logging
import mysql.connector


class MySQLPipeline(object):
    def __init__(self, db_config):
        self.logger = logging.getLogger(__name__)
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
        try:
            self.cnx = mysql.connector.connect(**self.db_config)
            self.cursor = self.cnx.cursor()
        except mysql.connector.Error as err:
            self.logger.error('MySQL DB CONNECTION ERROR!')
            self.logger.error(err)

    def close_spider(self, spider):
        self.cursor.close()
        self.cnx.close()

    def process_item(self, item, spider):
        add_boc_atmdist = 'INSERT INTO TB_BOC_ATMDIST ' \
                          '(ss, cs, address_type, device_type, address, status, page_url) ' \
                          'VALUES (%s, %s, %s, %s, %s, %s, %s)'
        self.cursor.execute(add_boc_atmdist, (item['ss'], item['cs'], item['address_type'], item['device_type'],
                                              item['address'], item['status'], item['page_url']))
        self.cnx.commit()
        return item
