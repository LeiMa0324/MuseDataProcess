import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

data = pd.read_csv("Data/varyNumofShared.csv")

thru_data = data[["# of shared","Hamlet throughput", "Greta throughput"]]
thru_data = thru_data[1:]
lat_data = data[["# of shared","Hamlet latency", "Greta latency"]]
lat_data = lat_data[1:]
mem_data = data[["# of shared","Hamlet memory", "Greta memory"]]
mem_data = mem_data[1:]

def throughput(dataset):
    dataset['# of shared'] = dataset['# of shared'].astype(int)

    dataset['Hamlet throughput'] = dataset['Hamlet throughput'].astype(int)
    dataset['Greta throughput'] = dataset['Greta throughput'].astype(int)

    hamlet_list = dataset['Hamlet throughput']
    greta_list = dataset['Greta throughput']

    fontSize =18
    x = dataset['# of shared']
    plt.xlabel("# of shared",fontsize = fontSize)
    plt.ylabel("Throughput(log)", fontsize =fontSize)
    plt.xticks(x,fontsize =fontSize)
    plt.yticks(fontsize =fontSize)
    plt.plot(x, hamlet_list, "-^b", label ='Hamlet',linewidth =2,markersize=10)
    plt.plot(x, greta_list, "-vm", label ='Greta',linewidth =2,markersize=10)
    plt.yscale('log')
    plt.ylim((1,100000))
    plt.legend(fontsize=fontSize, loc =1)
    plt.title("Throughput under different # of shared", fontSize = fontSize)

    plt.savefig("plots/varyShared/throughput.png")
    plt.show()

def latency(dataset):
    dataset['# of shared'] = dataset['# of shared'].astype(int)

    dataset['Hamlet latency'] = dataset['Hamlet latency'].astype(int)
    dataset['Greta latency'] = dataset['Greta latency'].astype(int)

    hamlet_list = dataset['Hamlet latency'].map(lambda x: x / 1000)
    greta_list = dataset['Greta latency'].map(lambda x: x / 1000)

    fontSize = 18
    x = dataset['# of shared']
    plt.xlabel("# of shared", fontsize=fontSize)
    plt.ylabel("latency(sec)", fontsize=fontSize)
    plt.xticks(x, fontsize=fontSize)
    plt.yticks(fontsize=fontSize)
    plt.plot(x, hamlet_list, "-^b", label='Hamlet', linewidth=2, markersize=10)
    plt.plot(x, greta_list, "-vm", label='Greta', linewidth=2, markersize=10)
    plt.yscale('log')
    plt.legend(fontsize=fontSize, loc=1)
    plt.title("Latency under different # of shared", fontSize=fontSize)
    plt.savefig("plots/varyShared/latency.png")

    plt.show()

def memory(dataset):
    dataset['# of shared'] = dataset['# of shared'].astype(int)

    dataset['Hamlet memory'] = dataset['Hamlet memory'].astype(int)
    dataset['Greta memory'] = dataset['Greta memory'].astype(int)

    hamlet_list = dataset['Hamlet memory'].map(lambda x: x/10000)
    greta_list = dataset['Greta memory'].map(lambda x: x/10000)

    fontSize =18
    x = dataset['# of shared']
    plt.xlabel("# of shared",fontsize = fontSize)
    plt.ylabel("memory(byte)", fontsize =fontSize)
    plt.xticks(x,fontsize =fontSize)
    plt.yticks(fontsize =fontSize)
    plt.plot(x, hamlet_list, "-^b", label ='Hamlet',linewidth =2,markersize=10)
    plt.plot(x, greta_list, "-vm", label ='Greta',linewidth =2,markersize=10)
    plt.legend(fontsize=fontSize, loc =1)
    plt.yscale("log")
    plt.ylim((50,500))
    plt.title("Memory under different # of shared", fontSize = fontSize)
    plt.savefig("plots/varyShared/memory.png")

    plt.show()


throughput(thru_data)
latency(lat_data)
memory(mem_data)
