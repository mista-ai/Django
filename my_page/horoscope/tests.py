from django.test import TestCase
from .views import zodiac_dict

# Create your tests here.

class TestHoroscope(TestCase):

    def test_index(self):
        response = self.client.get('/horoscope/')
        self.assertEqual(response.status_code, 200)

    def test_libra(self):
        response = self.client.get('/horoscope/libra')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
                      response.content.decode())

    def test_redirect(self):
        zodiacs = tuple(zodiac_dict)
        for sign_number in range(1, 13):
            response = self.client.get(f'/horoscope/{sign_number}')
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.url, f'/horoscope/{zodiacs[sign_number-1]}')

    def test_signs(self):
        for sign, content in zodiac_dict.items():
            response = self.client.get(f'/horoscope/{sign}')
            self.assertEqual(response.status_code, 200)
            self.assertIn(content, response.content.decode())