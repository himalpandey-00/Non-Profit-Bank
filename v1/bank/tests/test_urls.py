from django.test import SimpleTestCase
from django.urls import reverse, resolve
#from ..views import Home, BankDetail, BankList

class TestUrls(SimpleTestCase):
    
    def test_list_url_is_resolved(self):
        assert 1 == 2