from Selenium import webdriver
import time
from Selenium.webdriver.common.keys import Keys
print("sample test case started")
driver = webdriver.Chrome()
#navigate to the url
driver.get("http://www.weatherbase.com/weather/city.php3?c=IN&name=India")
#search city and click
driver.find_element_by_link_text("Bangalore").click()
#Show all data of the city
driver.find_element_by_link_text("Show All Data").click()
time.sleep(2)

#close the browser
driver.close()
print("sample test case successfully completed")
