import csv

def reader():
    with open("data.csv", 'r') as file:
        data = file.readlines()
    size = len(data)
    for i in range(size):
        data[i] = data[i].strip().split(",")
    return(data,size)

def city_list(data,size):
    dew_city = []
    for i in range(size):
        if data[i][1] == "Average Dew Point":
            dew_city.append(data[i][0])
    return(dew_city)

def final(data, dew_city):
    dew_data = []
    for i in range(size):
        if data[i][0] in dew_city:
            if len(data[i]) > 10:
                dew_data.append(data[i])
    return(dew_data)

def makefile(dew_data):
    with open("dew_data.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        #Make first row
        writer.writerow(["City","PARAMETER","ANNUAL","JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG ","SEP","OCT","NOV","DEC"])
        #Loop through items in data list
        for line in dew_data:
            if len(line) > 0:
                writer.writerow(line)

#Main function starts here
print("Dew data generation started")
#Read the raw file
data,size = reader()
print("Raw file reading completed")
#Create list of cities having dew point
dew_city = city_list(data,size)
#Create list of all data of dew_city
dew_data = final(data, dew_city)
print("Final data ready")
#make csv file for the cleaned data
makefile(dew_data)
print("Dew data generation completed")
