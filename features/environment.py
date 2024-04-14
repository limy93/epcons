from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def before_all(context):
    # Set up the WebDriver
    options = webdriver.ChromeOptions()
    # Add any Chrome options you need
    # options.add_argument('headless')  # Uncomment if you don't need a GUI
    # options.add_argument('window-size=1200x600')  # Uncomment to specify window size
    context.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def after_all(context):
    # Clean up and close the browser once tests are done
    context.browser.quit()