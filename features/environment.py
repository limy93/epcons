import os
from behave import use_fixture
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Setup Django environment correctly
os.environ['DJANGO_SETTINGS_MODULE'] = 'epcons.settings'
import django
django.setup()

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

def before_all(context):
    # Set up the WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    context.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def before_scenario(context, scenario):
    # Setup user for scenarios tagged with 'requires_login'
    if 'requires_login' in scenario.tags:
        # Delete any existing users to ensure a clean state
        User.objects.all().delete()
        # Create a user for the tests
        User.objects.create(username='valid_user', password=make_password('valid_password'), is_active=True)

def after_all(context):
    # Clean up and close the browser once tests are done
    context.browser.quit()