from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re





class NewModTest(TestCase):

    '''Test d'ajout et supression d'un mod '''
    def test_add_mod(self):
        ts= 'fsfedhfddfsggdf'
        browser = webdriver.Chrome('./chromedriver')
        browser.get('http://localhost:8000/mods/')
        time.sleep(1)
        name = browser.find_element_by_id("id_title")
        desc = browser.find_element_by_id("id_description")
        crea = browser.find_element_by_id("id_creator")
        vers = browser.find_element_by_id("id_version")
        down = browser.find_element_by_id("id_download")
        img = browser.find_element_by_id("id_img")

        name.send_keys(ts)
        time.sleep(1)

        desc.send_keys("pa qui officia deserunt mollit anim id est laborum.")
        time.sleep(1)

        crea.send_keys("best_crea")
        time.sleep(1)

        vers.send_keys("2.28")
        time.sleep(1)

        down.send_keys("http://fsdf.fr")
        time.sleep(1)

        img.send_keys("http://fsdf.fr")
        time.sleep(1)

        browser.find_element_by_id("sub").click()
        time.sleep(1)


        nom = browser.find_element_by_css_selector("body > main > div.jumbotron > div > div.col-12 > div.card > div.card-body > h5.card-title")
        print(nom.text)
        #Là la tache doit etre crée
        # noms = browser.find_elements_by_css_selector("body > main > div.jumbotron > div > div.col-12 > div.card > div.card-body > h5.card-title")
        time.sleep(1)
        modFound = False
        if( ts == nom.text ):
            modFound = True
            print(modFound)
        time.sleep(1)
        
        #le mod est crée
        print("Mod crée:")
        self.assertEqual(True,modFound)

        #on va la supprimer
        return_button = browser.find_element_by_id('returnHome')
        return_button.click()
        time.sleep(10)
        supp_button = browser.find_element_by_id(ts+'supp')
        supp_button.click()
        
        #on verrifie qu'elle est supprimée
        noms = browser.find_elements_by_css_selector("body > main > div.jumbotron > div > div.w-100 > div.card > div.card-body > a > h5.card-title")
        modFound = False
        for nom in noms:
            if( re.match(ts, nom.text) ):
                modFound = True
        print("Mod supprimé:")
        self.assertEqual(False,modFound)
        time.sleep(1)

        browser.quit()



test = NewModTest()
test.test_add_mod()