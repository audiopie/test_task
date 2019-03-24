import re
import json
from conf import DATA_FILE_PATH


class JsonToHtml:

    find_tag = re.compile(r'^\w+')


    def load(self): # Загружаем json файл
        return json.load(open(DATA_FILE_PATH)) # в conf.py указан путь до файла


    def render(self,data):
        if isinstance(data, list):
            item = self.convert_list(data)
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
                item = self.render_list(v)
            else:
                tag_open, tag_close = self.grab_tag(k)
            list_items.append('<'+ tag_open + '>' + v + '</' + tag_close + '>')
        return ''.join(list_items)


    def grab_tag(self, value):
        tag = self.find_tag.findall(value)[0]
        return tag, tag


if __name__ == '__main__':
    converter = JsonToHtml()
    data = converter.render(converter.load())
