from behave import *
from foodi.accounts.factories import User

# Then we can copy the snippets into our file
@given('I empty the User table')
def impl(context):
    assert True

@given('I go to the signup page')
def impl(context):
    assert False

@given('I enter a username and password')
def impl(context):
    assert False

@then('I have created an account')
def impl(context):
    assert False
