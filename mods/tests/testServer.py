from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager


class ServerTest(TestCase):

    '''Test du serveur allumé et lesTaches dans le titre'''
    def test_server_on(self):

        browser = webdriver.Chrome('./chromedriver')
        browser.get('http://127.0.0.1:8000/mods/listing')
        time.sleep(1)
        print(browser.title)
        assert 'Mods Minecraft' in browser.title
        time.sleep(1)
        browser.quit()  


test = ServerTest()
test.test_server_on()