from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then

@given('I am on the "Password Reset" page')
def step_impl(context):
    context.browser.get('http://127.0.0.1:8000/password_reset')
    assert "Password Reset" in context.browser.title

@when('I submit a valid email address for password reset')
def step_impl(context):
    email_field = context.browser.find_element(By.ID, "email")
    email_field.clear()
    email_field.send_keys("known_user@example.com")   # Ensure this is a valid email for testing
    email_field.send_keys(Keys.RETURN)

@then('I should see a simplified confirmation message')
def step_impl(context):
    # Waiting for the redirect to the confirmation message page
    WebDriverWait(context.browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Password Reset Email Sent')]")),
        message="Confirmation page did not load or was not found."
    )
    # Verifying the confirmation text
    message_text = context.browser.find_element(By.CSS_SELECTOR, "div.py-5.text-center p.lead").text
    assert "Please check your email for the link to reset your password." in message_text

    # Optional: Verify the presence of the "Return to Login Page" button
    WebDriverWait(context.browser, 10).until(
        EC.visibility_of_element_located((By.LINK_TEXT, "Return to Login Page")),
        message="Return to Login Page link not found."
    )