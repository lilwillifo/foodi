from django.test import TestCase
from expects import *

class UserSavesFood(TestCase):
    def setup(self):
        Users.objects.create(name="")

    def test_something(self):
        expect([]).to(be_empty)
