#Author: Ardavan Ghahramani 
#Graphing calculations

import matplotlib.pyplot as plt

class Graphs: 
   
    def __init__(self):
        self.name = []
        self.cat = []
        self.price = []
   
    def BarGraph(x_axis_data, y_axis_data, x_axis_label, y_axis_label, title):
        plt.bar(x_axis_data, y_axis_data)
        plt.xlabel(x_axis_label)
        plt.ylabel(y_axis_label)
        plt.title(title)
        plt.show()
        
    def LineGraph(x_axis_data, y_axis_data, x_axis_label, y_axis_label, title):
        plt.plot(x_axis_data, y_axis_data)
        plt.xlabel(x_axis_label)
        plt.ylabel(y_axis_label)
        plt.title(title)
        plt.show()
        
    def SaveGraph(x_axis_data, y_axis_data, x_axis_label, y_axis_label, title):
        plt.bar(x_axis_data, y_axis_data)
        plt.xlabel(x_axis_label)
        plt.ylabel(y_axis_label)
        plt.title(title)
        plt.savefig('BarGraph.jpg', format = 'jpg')