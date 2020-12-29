import csv
import plotly.figure_factory as ff
import pandas as pd
import statistics
import random
import plotly.graph_objects as go 

data = pd.read_csv("data.csv")
final_data = data["temp"].tolist()

data_mean = statistics.mean(final_data)
data_std =  statistics.stdev(final_data)

print("temp mean: ",data_mean)
print("temp std dev: ",data_std)

def show_fig(mean_list):
    df= mean_list
    fig = ff.create_distplot([df],["temp"],show_hist=False)
    fig.add_trace(go.Scatter(x=[data_mean,data_mean], y=[0,1],mode="lines",name="MEAN"))
    fig.show()

def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(final_data)-1)
        value = final_data[random_index]
        dataset.append( value)
    mean = statistics.mean(dataset)
    return mean

def random_set_of_std_dev():
    mean_list = []
    for i in range(0,1000):
        setOfMean = random_set_of_mean(100)
        mean_list.append(setOfMean)    
    std_dev = statistics.stdev(mean_list)    
    print("Standard deviation of sample: ",std_dev)

def setup():
    mean_list = []
    for i in range(0,1000):
        setOfMean = random_set_of_mean(100)
        mean_list.append(setOfMean)
    show_fig(mean_list)
    mean = statistics.mean(mean_list)
    print("Mean of sample: ",mean)

setup()

temp_mean = statistics.mean(final_data)
print("The temp mean is ",temp_mean)

random_set_of_std_dev()