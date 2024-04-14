from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I am on the login page')
def step_impl(context):
    context.browser.get('http://127.0.0.1:8000/accounts/login')

@when('I enter valid credentials')
def step_impl(context):
    context.browser.find_element(By.ID, "id_username").send_keys("default_user")
    context.browser.find_element(By.ID, "id_password").send_keys("defaultpassword")

@when('I enter invalid credentials')
def step_impl(context):
    context.browser.find_element(By.ID, "id_username").send_keys("invalid_user")
    context.browser.find_element(By.ID, "id_password").send_keys("invalid_password")

@when('I submit the login form')
def step_impl(context):
    context.browser.find_element(By.CSS_SELECTOR, "form button[type='submit']").click()

@then('I should be redirected to the dashboard')
def step_impl(context):
    WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.ID, "dashboard-content"))
    )

@then('I should see an error message indicating login failure')
def step_impl(context):
    WebDriverWait(context.browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger"))
    )
    error_message = context.browser.find_element(By.CSS_SELECTOR, ".alert-danger").text
    assert "Please enter a correct username and password. Note that both fields may be case-sensitive." in error_message