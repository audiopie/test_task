import re
import json
from conf import DATA_FILE_PATH
from html import escape


class JsonToHtml:

    find_tag = re.compile(r'^\w+')
    find_id = re.compile(r'\#([^#\.]+)')
    find_class = re.compile(r'\.([^#\.]+)')


    def load(self): # Загружаем json файл
        return json.load(open(DATA_FILE_PATH)) # в conf.py указан путь до файла


    def render(self,data):
        if isinstance(data, list):
            item = self.convert_list(data)
        else:
            item = self.convert_data(data)
        return item

    def convert_list(self, list_data):
        items = ''.join(map(self.render_list, list_data))
        return ''.join(['<ul>', items, '</ul>'])


    def render_list(self, tags):
        return '<li>{}</li>'.format(self.convert_data(tags))


    def convert_data(self, words):
        list_items = []
        for k,v in words.items():
            if isinstance(v, list):
                item = self.convert_list(v)
            else:
                item = escape(v)
                tag_open, tag_close = self.grab_tag(k)
            list_items.append('<'+ tag_open + '>' + item + '</' + tag_close + '>')
        return ''.join(list_items)


    def grab_tag(self, value):
        tag = self.find_tag.findall(value)[0]
        ids = self.find_id.findall(value)
        ids = ' id="%s"' % ' '.join(ids) if ids else ''
        cls = self.find_class.findall(value)
        cls = ' class="%s"' % ' '.join(cls) if cls else ''
        return tag + ids + cls, tag


if __name__ == '__main__':
    converter = JsonToHtml()
    data = converter.render(converter.load())
