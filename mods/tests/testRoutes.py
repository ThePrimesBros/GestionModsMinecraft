from django.urls import reverse
from django.test import TestCase
from mods.views import task,listing,scrap,detail,edite,delete


class HomePageTestContent(TestCase):

    routes = {
    "" : task,
    "/listing" :  listing,
    "/scrap" :  scrap,
    "/detail/1" :  detail,
    "/edit/1" :  edite,
    "/del/1" :  delete,
    }

    '''Test unitaire de la page accueil sur la racine du projet'''
    def test_root_url_resolves_to_home_view(self):
        for route,function in self.routes.items():
            found = resolve(route)
            self.assertEqual(found.func,function)

test = HomePageTestContent()
test.test_root_url_resolves_to_home_view()