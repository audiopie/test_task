import re
import json
from conf import DATA_FILE_PATH


class JsonToHtml:

    find_tag = re.compile(r'^\w+')


    def load(self): # Загружаем json файл
        return json.load(open(DATA_FILE_PATH)) # в conf.py указан путь до файла


    def render(self,data):
        item = self.convert_data(data)
        print(item)
        return item


    def convert_data(self, words):
        list_items = []
        for key in words:
            for k, v in key.items():
                tag_open, tag_close = self.grab_tag(k)
                list_items.append('<'+ tag_open + '>' + v + '</' + tag_close + '>')
        return ''.join(list_items)


    def grab_tag(self, value):
        tag = self.find_tag.findall(value)[0]
        return tag, tag


if __name__ == '__main__':
    converter = JsonToHtml()
    data = converter.render(converter.load())
