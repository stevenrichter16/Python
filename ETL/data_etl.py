# -*- coding: utf-8 -*-
"""
Data ETL with a weather dataset
"""

import pandas as pd

df1 = pd.read_csv("ABCWeather.csv")

df1.head() # TempF

df1['TemperatureC'] = df['TemperatureC'].apply(lambda x: x * (9/5) + 32)

df1.rename(columns={"TemperatureC":"TemperatureF"}, inplace=True)

df1.rename(columns={"Wind SpeedMPH":"WindMPH"},inplace=True)

df1.replace("Calm",0, inplace=True)

df1_m2006 = df1[(df['Year']==2006) & (df['Month']==3)]

df1_m2006 = df1_m2006['WindMPH']

df1_m2006 = list(filter(lambda x: float(x) >= 0,df1_m2006))

df1_m2006 = list(map(lambda x: float(x), df1_m2006))

sum1 = 0
for i in df1_m2006:
    sum1 += i
avg1 = sum1 / len(df1_m2006)

df2 = pd.read_csv("KLMWeather.csv")

df2.rename(columns={"Wind SpeedMPH":"WindMPH"},inplace=True)

df2.replace("Calm",0, inplace=True)

df2_m2006 = df2[(df['Year']==2006) & (df2['Month']==3)]

df2_m2006 = df2_m2006['WindMPH']

df2_m2006 = list(filter(lambda x: float(x) >= 0,df2_m2006))

df2_m2006 = list(map(lambda x: float(x), df2_m2006))

sum2 = 0
for i in df2_m2006:
    sum2 += i
avg2 = sum2 / len(df2_m2006)

df3 = pd.read_csv("PQRWeather.csv")

df3['Wind SpeedKPH'] = df3['Wind SpeedKPH'].apply(lambda x: x * 0.621371)

df3.rename(columns={"Wind SpeedKPH":"WindMPH"},inplace=True)

df3.replace("Calm",0, inplace=True)

df3_m2006 = df3[(df['Year']==2006) & (df3['Month']==3)]

df3_m2006 = df3_m2006['WindMPH']

df3_m2006 = list(filter(lambda x: float(x) >= 0,df3_m2006))

df3_m2006 = list(map(lambda x: float(x), df3_m2006))

sum3 = 0
for i in df3_m2006:
    sum3 += i
avg3 = sum3 / len(df3_m2006)

df4 = pd.read_csv("XYZWeather.txt",delimiter=';')

df4.replace("Calm",0, inplace=True)

df4.rename(columns={"Wind SpeedMPH":"WindMPH"},inplace=True)

df4_m2006 = df4[(df['Year']==2006) & (df4['Month']==3)]

df4_m2006 = df4['WindMPH']

df4_m2006 = list(filter(lambda x: float(x) >= 0,df4_m2006))

df4_m2006 = list(map(lambda x: float(x), df4_m2006))

sum4 = 0
for i in df4_m2006:
    sum4 += i
avg4 = sum4 / len(df4_m2006)

# Problem 2

df1[df1['Month'] == 2]

df1_temps

