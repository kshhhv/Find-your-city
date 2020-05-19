from selenium import webdriver
from bs4 import BeautifulSoup as soup
import time
from selenium.webdriver.common.keys import Keys

print("sample test case started")
driver = webdriver.Chrome()
#navigate to the url
driver.get("http://www.weatherbase.com/weather/city.php3?c=IN&name=India")
#search city and click
driver.implicitly_wait(15)
driver.find_element_by_link_text("Bangalore").click()
driver.implicitly_wait(15)
#Show all data of the city
driver.find_element_by_link_text("Show All Data").click()
#driver.find_element_by_link_text("Monthly - All Data").click()
html = driver.page_source
soup = soup(html, features="html.parser")
f = open("Bangalore.html", "w", encoding="utf-8")
f.write(str(soup))
f.close()
driver.close()
print("sample test case successfully completed")
