import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



def hip_map(coor):
    plt.figure(figsize=(10,10))
    sns.heatmap(coor, annot=True)
    plt.xticks(ticks=range(len(coor)),labels=coor,fontsize=13)
    plt.yticks(ticks=range(len(coor)),labels=coor,fontsize=13,rotation=0)
    plt.tight_layout()
    plt.savefig("Shape/hipmap.png")
    plt.close()