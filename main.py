import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from nemodar.boxplt import box_plot
from nemodar.hipmap import hip_map
from nemodar.histogram import histo_gram

df_train = pd.read_csv("data/StudentsPerformance.csv")
# print(" تعداد  ردیف و ستون ها>>> ",df_train.shape)
# print("داده های تکراری ",df_train.duplicated().sum())
# print("داده های خالی ",df_train.isnull().sum())
# print(df_train.info())

nemodar_numrec = df_train.select_dtypes(include=np.number).columns.tolist()
print("ستون های عددی ",nemodar_numrec)

                            # *******  نمودار boxplot   *******
box_plot(df_train,nemodar_numrec)

                           # *******  نمودار Histogram   *******

histo_gram(df_train,nemodar_numrec)

                           # *******  نمودار Histogram   *******
hipmap_coor = df_train.select_dtypes(include=np.number)
co_or = hipmap_coor.corr()
hip_map(co_or)








































