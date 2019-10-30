from behave import given, when, then
from game import Game

@given(u'the user starts moving from location to another')

@when(u'the user starts moving from location to another')

@then(u'the name {location} where he is located')
def test_location(context, location):
    assert context.name.location == location

@then(u'the target should be {target:}')
def test_target(context, target):
    assert context.target == target
    
