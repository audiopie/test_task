import unittest

from main import JsonToHtml

class TestJsonToHtml(unittest.TestCase):

    def test_task(self):
        data = {"p.my-class#my-id": "hello", "p.my-class1.my-class2": "example<a>asd</a>"}
        converter = JsonToHtml()
        data = converter.render(data)
        self.assertEqual(data, '<p id="my-id" class="my-class">hello</p><p class="my-class1 my-class2">example&lt;a&gt;asd&lt;/a&gt;</p>')


if __name__ == '__main__':
    unittest.main()
