from behave import *
from foodi.factories import FoodFactory
from foodi.accounts.factories import UserFactory, ProfileFactory
from foodi.models import Food
from splinter.browser import Browser
from IPython import embed


@given(u'there is a profile with top 5 five foods')
def step_impl(context):
    for row in context.table:
        food_names = row['foods'].split(', ')
        foods = Food.objects.filter(name__in=food_names)
        user = UserFactory(username=row['username'], foods=foods)
        profile = user.profile

@when(u'I go to my analytics')
def step_impl(context):
    context.browser.visit('http://localhost:8000/analytics/')

@then(u'I see my top 5 foods')
def step_impl(context):
    foods = context.browser.find_by_css('.food')
    user = UserFactory(email='log.me.in@test.test')

    assert len(foods) == len(user.profile.top_5_foods())
