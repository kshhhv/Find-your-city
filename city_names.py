from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as soup
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
#navigate to the url
driver.get("http://www.weatherbase.com/weather/city.php3?c=IN&name=India")
time.sleep(2)

html = driver.page_source
page_soup = soup(html, features="html.parser")
driver.close()
list_city = []
for name in page_soup.find_all("li"):
    if (len(list_city)) < 678:
        list_city.append(name.text)

with open("city.txt", 'w', newline='') as file:
    for city in list_city:
        file.write(city)
        file.write("\n")
