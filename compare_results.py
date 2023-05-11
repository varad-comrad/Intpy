import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv('results_intpy.csv')
s1 = df1.mean(axis=0)
df2 = pd.read_csv('results_no_intpy.csv')
s2 = df2.mean(axis=0)
s3 = (s1-s2)/s2

s3.plot(title='relative difference between intpy and vanilla')
plt.show()