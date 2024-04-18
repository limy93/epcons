from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
import time

def generate_unique_username(base="testuser"):
    """Generate a unique username using a base name and the current timestamp."""
    return f"{base}_{int(time.time())}"

@given('I am on the registration page')
def step_impl(context):
    context.browser.get('http://127.0.0.1:8000/register')
    assert "Register" in context.browser.title

@when('I enter valid registration information')
def step_impl(context):
    unique_username = generate_unique_username()
    context.browser.find_element(By.ID, "id_username").send_keys(unique_username)
    context.browser.find_element(By.ID, "id_email").send_keys(f"{unique_username}@example.com")
    context.browser.find_element(By.ID, "id_password1").send_keys("validpassword123")
    context.browser.find_element(By.ID, "id_password2").send_keys("validpassword123")

@when('I enter invalid registration information')
def step_impl(context):
    unique_username = generate_unique_username()
    context.browser.find_element(By.ID, "id_username").send_keys(unique_username)
    context.browser.find_element(By.ID, "id_email").send_keys(f"{unique_username}@example.com")
    context.browser.find_element(By.ID, "id_password1").send_keys("password123")
    context.browser.find_element(By.ID, "id_password2").send_keys("password321")   # Intentionally different

@when('I submit the registration form')
def step_impl(context):
    context.browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

@then('I should be registered and redirected to the dashboard')
def step_impl(context):
    WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.ID, "dashboard-content")),
        message="Dashboard was not reached after registration."
    )
    # Confirm presence of the dashboard identifier to ensure redirection success
    assert "Dashboard" in context.browser.find_element(By.CSS_SELECTOR, "#dashboard-content h2").text

@then('I should see an error message indicating registration failure')
def step_impl(context):
    WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'alert-danger')),
        message="Expected error message was not displayed."
    )
    error_message = context.browser.find_element(By.CLASS_NAME, 'alert-danger').text
    assert "The two password fields didn’t match." in error_message