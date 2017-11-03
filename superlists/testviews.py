from django.template.loader import render_to_string
from django.test import TestCase


class SuperListTest(TestCase):

    def test_home_page_returns_correct_html(self):
        import pdb
        pdb.set_trace()
        response = self.client.get('')
        html = response.content
        expected_html = render_to_string('home.html')
        self.assertEqual(html, expected_html)


# class SuperListTest(unittest.TestCase):

#     def test_home_page_returns_correct_html(self):
#         request = HttpRequest()
#         response = home_page(request)
#         html = response.content.decode('utf8')
#         expected_html = render_to_string('home.html')
#         self.assertEqual(html, expected_html)
