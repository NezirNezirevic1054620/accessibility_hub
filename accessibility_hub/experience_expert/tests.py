import unittest

from selenium import webdriver


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_app(self):
        self.browser.get(" http://127.0.0.1:8000/")

        self.assertIn(member="Django Tailwind", container=self.browser.title)
