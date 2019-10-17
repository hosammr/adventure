from behave import given, when, then  
from game import Game

@given(u'the user asks for description')

@when(u'the user asks for description')

@then(u'the name {location} should be shown')
def test_location(context, location):
    assert context.name.location == location


@then(u'the description should be  {description:}')
def test_description(context, description):
    assert context.description == description