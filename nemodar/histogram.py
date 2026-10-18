import matplotlib.pyplot as plt

def histo_gram(df,col):
    plt.figure(figsize=(10,10))
    df[col].hist(bins=50)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.tight_layout()
    plt.savefig("Shape/Histogram.png")
    plt.close()

