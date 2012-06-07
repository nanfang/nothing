# Scrapy settings for getbooks project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'getbooks'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['getbooks.spiders']
NEWSPIDER_MODULE = 'getbooks.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

ITEM_PIPELINES = [
    'getbooks.pipelines.GetbooksPipeline',
        ]
