import csv
import math
import xkcd
import matplotlib.pyplot as plt
import pylab
from adjustText import adjust_text

#Read the raw file and return it in list
def read():
    with open("dew_data.csv", 'r') as file:
        file_data = file.readlines()

    size = len(file_data)
    for i in range(size):
        file_data[i] = file_data[i].strip().split(",")

    return (file_data,size)

def dew_avail(data,size):
    data_req = []
    for i in range(size):
        #Check if the parameter is required
        if data[i][1] in param_req:
            data_req.append(data[i])

    size = len(data_req)
    return (data_req,size)

def merger(data_req,size):
    data_merging = []
    for i in range(size):
        #Need only one row for every city
        if i%2 == 0:
            #initalize list for this city
            city_data = []
            #Loop through every data of each city
            for j in range(15):
                #Skip string data
                if j > 1:
                    #Humidex caluclation
                    celsius = (float(data_req[i][j]) -32) * 5 / 9
                    kelvin = celsius + 273.15
                    hum_e = 6.11 * math.e ** (5417.7530 * ((1/273.16) - (1/kelvin)))
                    hum_h = (0.5555)*(hum_e - 10.0)
                    data_req[i][j] = celsius
                    humidex = data_req[i][j] + hum_h
                    tupl = [j-2, data_req[i][j], data_req[i+1][j], humidex]
                    city_data.append(tupl)
                elif j == 1:
                    city_data.append("Month order, Temp, Dew point, Humidex")
                else:
                    city_data.append(data_req[i][0])
            #Merge city data to whole
            data_merging.append(city_data)
    return(data_merging)

def sorter(data_merged):
    data_sorting = []
    #Loop throup every city
    for line in data_merged:
        #Sort data according to average temperature per month
        sorted_line = sorted(line[3:], key = lambda x: x[1])
        sorted_line.insert(0, line[2])
        sorted_line.insert(0, line[1])
        sorted_line.insert(0, line[0])
        data_sorting.append(sorted_line)
    return(data_sorting)

def averager(data_sorted):
    final_data = []
    #Loop through every city
    for line in data_sorted:
        win_sum = 0
        #Take sum and then average of 4 coldest months
        for i in range(3,7):
            win_sum += float(line[i][1])
        win_av = int(win_sum/4)
        hum_sum = 0
        #Take sum and then average of 4 hottest(humidex) month
        for i in range(-4,0):
            hum_sum += float(line[i][3])
        hum_av = int(hum_sum/4)
        #Make sublist of city, winter average and humidex average
        final_data.append([line[0], win_av, hum_av])
    return(final_data)

def data_pointer(final_data):
    xl = []
    yl = []
    nl = []
    #Loop through every city
    for city in final_data:
        xl.append(city[2])
        yl.append(city[1])
        nl.append(city[0])
    return(xl,yl,nl)

def plotter(x,y,z):
    #intiate graph in xkcd format
    plt.xkcd()
    #plot white(invisible) data points
    plt.scatter(x, y, c = 'white')
    #Add annotations then adjust it
    texts = [plt.text(x[i], y[i], n[i], ha='center', va='center', fontsize = 8, color ='grey') for i in range(len(x))]
    adjust_text(texts)

    # x-axis label
    plt.xlabel('Summer Heat and Humidity (Humidex)')
    # y-axis label
    plt.ylabel('Winter Temperature (in celsius)')

    # function to show the plot
    plt.show()

#Main function starts here
print("xkcd: WHERE TO LIVE IN INDIA started")
data,size = read()
print("Raw data reading completed")

#Take data only for Avg Temp and Dew Point
param_req = ['Average Temperature', 'Average Dew Point']
data_req,size = dew_avail(data,size)
print("Data cleaning completed")

#Caluclate Humidex and merge it with temperature
data_merged = merger(data_req,size)
print("City humidex caluclated")

#Sort data of each city as per average monthly temp
data_sorted = sorter(data_merged)
print("Average temperature caluclated and merged")

#Finalize data with winter and humidex average
final_data = averager(data_sorted)
print("Final data ready")

#Initialize value for data points
x,y,n = data_pointer(final_data)
print("Data points generated")

#Plot the graph
plotter(x,y,n)
print("Graph generation in progress...")
print("xkcd: WHERE TO LIVE IN INDIA created")
