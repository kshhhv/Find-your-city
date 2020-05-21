from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as soup
import time
import csv
from selenium.webdriver.common.keys import Keys

#returns soup of the data from city page
def souper(city, driver):
    #search city and click
    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.LINK_TEXT, city))
    ).click()
    #Go to all data
    element = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Show All Data"))
    ).click()
    time.sleep(3)
    html = driver.page_source
    page_soup = soup(html, features="html.parser")

    makeCSV(city,page_soup)


    driver.back()
    driver.back()

#returns data in list format if city name is given
def getData(city, soup):
    #calls getSoup to have soup of the city
    #soup = getSoup(city)
    #initialize data list
    data = []
    #filter out all the tables in page
    tables = soup.find_all("table")
    #add available parameters in the data looping through all tables
    for table in tables:
        n_parameter = []
        trs = table.tbody.find_all("tr")  # contains 2 rows
        if len(trs[0].find_all("td")) == 2:
            for td in trs[0].find_all("td"):
                text = td.text.strip()
                n_parameter.append(text)
        if len(n_parameter) != 0 :
            if len(n_parameter[0]) > 2:
                data.append([n_parameter[0]])

    #counter to match data with parameter
    i = 0
    #add data in the list corressponding to parameter
    for table in tables:
        a_parameter = []
        trs = table.tbody.find_all("tr")  # contains 2 rows
        if (len(trs)) == 2:
            for td in trs[1].find_all("td"):
                a_parameter.append(td.text)
        #neglect trash
        if len(a_parameter) > 10:
            data[i] = [city] + data[i] + a_parameter[1:]
            i = i + 1
    #return data in list format
    return data

#makes csv file for a city
def makeCSV(city, soup):
    #calls getData to get data in list format
    data_city = getData(city, soup)
    x = ".csv"
    #Creates csv file with city name
    with open("data.csv", 'a', newline='') as file:
        writer = csv.writer(file)
        #Make first row
        writer.writerow(["City","PARAMETER","ANNUAL","JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG ","SEP","OCT","NOV","DEC"])
        #Loop through items in data list
        for para in data_city:
            if (len(para)) > 0:
                #write data
                writer.writerow(para)


#main function starts here

print("sample test case started")
with open("city.txt", 'r') as file:
    names = file.readlines()

print(len(names))
print("Cities list generated")
driver = webdriver.Chrome()
#navigate to the url
driver.get("http://www.weatherbase.com/weather/city.php3?c=IN&name=India")

i=0
for city in names[i:]:
    city = city.strip()
    print("Starting...", city)
    souper(city, driver)
    print(i, " done", city)
    i = i +1

driver.close()
print("sample test case successfully completed")
