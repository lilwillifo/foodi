from aloe import before, step, world
from aloe.tools import guess_types
from aloe_django.steps.models import get_model
from nose.tools import assert_true

from django.contrib.auth.models import User
from foodi.models import Food

from rest_framework.test import APIClient


@before.each_feature
def before_each_feature(feature):
    world.client = APIClient()

@step('I search for "([^"]+)"')
def step_search_food(self, food_name):
    get_model(Food).objects.get_or_create(name=food_name)
