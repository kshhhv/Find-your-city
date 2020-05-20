from selenium import webdriver
from bs4 import BeautifulSoup as soup
import time
import csv
from selenium.webdriver.common.keys import Keys

#returns soup of the data from city page
def getSoup(city):
    driver = webdriver.Chrome()
    #navigate to the url
    driver.get("http://www.weatherbase.com/weather/city.php3?c=IN&name=India")
    #search city and click
    driver.implicitly_wait(15)
    driver.find_element_by_link_text(city).click()
    driver.implicitly_wait(15)
    #Show all data of the city
    driver.find_element_by_link_text("Show All Data").click()
    #driver.find_element_by_link_text("Monthly - All Data").click()
    time.sleep(5)
    html = driver.page_source
    page_soup = soup(html, features="html.parser")
    driver.close()
    return page_soup

#returns data in list format if city name is given
def getData(city):
    #calls getSoup to have soup of the city
    soup = getSoup(city)
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
            data[i] = data[i] + a_parameter[1:]
            i = i + 1
    #return data in list format
    return data

#makes csv file for a city
def makeCSV(city):
    #calls getData to get data in list format
    data_city = getData(city)
    x = ".csv"
    #Creates csv file with city name
    with open(city+x, 'w', newline='') as file:
        writer = csv.writer(file)
        #Make first row
        writer.writerow(["PARAMETER","ANNUAL","JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG ","SEP","OCT","NOV","DEC"])
        #Loop through items in data list
        for para in data_city:
            if (len(para)) > 0:
                #write data
                writer.writerow(para)


#main function starts here

print("sample test case started")

city = input("Type city name: ")
makeCSV(city)

print("sample test case successfully completed")
