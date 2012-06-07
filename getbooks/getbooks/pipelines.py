from __future__ import unicode_literals
class GetbooksPipeline(object):
    def __init__(self):
        self.file = open('books.txt', 'wb')

    def process_item(self, item, spider):
        name ,id = item['name'], item['id'] 
        row = '%s.mp3 http://my.eapoo.com/freedownload/%s\n' % (name, id)
        self.file.write(row.encode('utf-8')) 
        return item
