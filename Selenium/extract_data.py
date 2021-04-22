from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time 

options = Options()
options.page_load_strategy = 'eager'


driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get("https://nian-code.github.io/nicoll-CV/%5BMichel%20Prieto%5D%20-%20Main.html")
#print(driver.title)
nombre = driver.find_element_by_xpath('//span[@id= "hostname"]')
print(nombre.text)
velocidad = driver.find_element_by_xpath('//span[@class = "value" and starts-with(., "1")]')
print(velocidad.text)
time.sleep(1)
driver.close()


#usuario = driver.find_element_by_id("email").send_keys("nicolidaly_11@hotmail.com")
# passa    = driver.find_element_by_id("pass").send_keys("Nicolmp4.2")

# driver.find_element_by_class_name("_42ft._4jy0._6lth._4jy6._4jy1.selected._51sy").click()
#driver.execute_script('''window.open("http://platzi.com","_blank");''')
