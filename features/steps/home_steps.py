from behave import given, when, then
from selenium.webdriver.common.by import By

@given('I am on the home page')
def step_impl(context):
    context.browser.get('http://127.0.0.1:8000/')  # Make sure this URL is correct for your local dev environment

@when('I click on the "About" button')
def step_impl(context):
    about_button = context.browser.find_element(By.LINK_TEXT, "About")
    about_button.click()

@when('I click on the "Explore Countries" button')
def step_impl(context):
    countries_button = context.browser.find_element(By.LINK_TEXT, "Explore Countries")
    countries_button.click()

@then('I should see the page title "{title}"')
def step_impl(context, title):
    assert title in context.browser.title

@then('I should be redirected to the About page')
def step_impl(context):
    assert "About the Project" in context.browser.title

@then('I should be redirected to the Explore Countries page')
def step_impl(context):
    assert "Select a Country" in context.browser.title  # Adjust this title to match your countries list page title