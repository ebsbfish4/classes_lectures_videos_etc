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


    print(dates)
    print(colors)

    # Try and except is best thought of as a final straw. You
    # should have something else before to check.
    try:
        whatColor = input('What color do you wish to know the date of?')
        if whatColor in colors:
            coldex = colors.index(whatColor)
            print(coldex)
            the_date = dates[coldex]
            print('The date of',whatColor,'is',the_date)
        else:
            print('Color not found, or is not a color')
                
    # This is a syntax difference form python 2.7.
    # used to look like Exception, e
    except Exception as e:
        print(e)

    print('continuing')
