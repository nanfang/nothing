from scrapy.item import Item, Field

class BookItem(Item):
    name = Field()
    id = Field()
