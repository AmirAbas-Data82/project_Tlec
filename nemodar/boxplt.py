import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



def box_plot(df,col):
    plt.figure(figsize=(10,6))
    plt.boxplot(df[col], vert=False)
    plt.xlabel(" X ",fontsize=15)
    plt.yticks(ticks=range(1,len(col)+1),labels=col,fontsize=12)
    plt.tight_layout()
    plt.savefig("Shape/boxplot.png")
    plt.close()



    # plt.ylabel(ylabel=col,fontsize=15)