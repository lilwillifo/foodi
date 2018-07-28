from behave import *
from foodi.factories import FoodFactory
from foodi.accounts.factories import UserFactory
from foodi.models import Food
from splinter.browser import Browser


@given(u'there are a number of foods')
def step_impl(context):
    foods = [FoodFactory(name=row['food']) for row in context.table]

@given(u'there are many users, each with different foods')
def step_impl(context):
    for row in context.table:
        food_names = row['foods'].split(', ')
        foods = Food.objects.filter(name__in=food_names)
        UserFactory(username=row['username'], foods=foods)

@given(u'I am a logged in user')
def step_impl(context):
        context.browser = Browser('chrome')
        user_to_login = UserFactory(email='log.me.in@test.test')
        # All properties (other than email) will be inherited from our UserFactory.
        # Therefore our password for this user will be 'pass'.

        # We visit the login page
        # context.config.server_url is by default set to http://localhost:8081
        # (Thanks to Cynthia Kiser for pointing this out.)
        # In this example we're visiting http://localhost:8081/accounts/login/
        context.browser.visit('http://localhost:8000/login/')

        # Next, we log in our user by interacting with the login form
        # Splinter has a handy fill function that helps us fill form fields based
        # on their name.  We'll use it to fill in the username and password fields.
        context.browser.fill('username', user_to_login.email)
        context.browser.fill('password', 'pass')

        # Finally we find the submit button (by its CSS attribute) and click on it!
        context.browser.find_by_css('form input[type=submit]').first.click()

@when(u'I go to my diary')
def step_impl(context):
    context.browser.visit('http://localhost:8000/diary/')

@then(u'I see my foods')
def step_impl(context):
    foods = context.browser.find_by_css('.food')
    user = UserFactory(email='log.me.in@test.test')

    # We can now assert that the number of users on the page
    # is equal to the number we expect
    assert len(foods) == user.profile.foods.count()
