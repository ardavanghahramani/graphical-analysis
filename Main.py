#Author: Ardavan Ghahramani 
#Python application aimed at analyzing input data variables,
#,displaying, and writing graphical results.

from Graphs import*

#name list
name = []
#category list
cat = []
#price list
price = []

while True: 
    print('\nPlease enter a designated number for the following function you would like to use.')
    u_i = int(input("1. Log a new item.\n2. Create a bar graph of the existing data.\n3. Create a line graph of the existing data.\n4. Save the existing data's graph.\n5. Exit\n"))
    if u_i == 1: 
        name.append(input('Input name: '))
        cat.append(int(input('Input category (input integer only): ')))
        price.append(float(input('Input price: ')))
    elif u_i == 2: 
        print('Choose how to graph.')
        graphz = int(input('1. Category\n2. Price\n'))
        if graphz == 1:
            Graphs.BarGraph(name, cat, 'Names', 'Category', 'X & Y Graph')
        else:
            Graphs.BarGraph(name, price, 'Names', 'Price', 'X & Y Graph')
    elif u_i == 3:
        print('Choose how to graph.')
        graphz = int(input('1. Category\n2. Price\n'))
        if graphz == 1:
            Graphs.LineGraph(name, cat, 'Names', 'Category', 'X & Y Graph')
        else: 
            Graphs.LineGraph(name, price, 'Names', 'Price', 'X & Y Graph')
    elif u_i == 4: 
        print('Choose how to graph.')
        graphz = int(input('1. Category\n2. Price\n'))
        if graphz == 1:
            Graphs.SaveGraph(name, cat, 'Names', 'Category', 'X & Y Graph')
        else: 
            Graphs.SaveGraph(name, price, 'Names', 'Price', 'X & Y Graph')
        print('BarGraph is saved as a jpg image.')
    elif u_i == 5: 
        print('You have quit the program.')
        break
    else: 
        print('\n***Invalid entry, please enter a number from 0 through 5.***')
