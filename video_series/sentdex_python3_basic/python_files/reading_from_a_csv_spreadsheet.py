#! python3

# csv stands for comma seperated variables
import csv

with open('/home/drew/sentdex_python3_basics/example.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    dates = []
    colors = []
    for row in readCSV:
        color = row[3]
        date = row[0]
        dates.append(date)
        colors.append(color)


    #print(dates)
    #print(colors)

    whatColor = input('What color do you wish to know the date of?')
    coldex = colors.index(whatColor)
    print(coldex)
    the_date = dates[coldex]
    print('The date of',whatColor,'is',the_date)
    
        
    
