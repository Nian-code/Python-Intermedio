from seleniumwire import webdriver  # Import from seleniumwire
from webdriver_manager.chrome import ChromeDriverManager

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(ChromeDriverManager().install())


# Go to the Google home page
driver.get('https://www.google.com')

# Access requests via the `requests` attribute
for request in driver.requests:
    if request.response.status_code == 200:
        print(request.response.status_code)