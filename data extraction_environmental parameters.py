# -*- coding: utf-8 -*-
#Copyright@ CHEN SHISHENG
"""
@author: CHEN SHISHENG, chenshisheng@u.nus.edu

Codes for data extraction of environmental parameters
"""

import os 
import numpy as np
import pandas as pd
import glob
import csv
from datetime import datetime
from dateutil import parser

#%%
"""sound pressure data"""
#grab excel files only
pattern = 'filepath\\*.xlsx'

#Save all file matches xlsx_files
xlsx_files = glob.glob(pattern, recursive=True)

#e.g., extract indoor sensor data
frames1 = []
#Iterate over csv_files
for file in xlsx_files:
    if 'indoor' in file:
        #  Read xlsx into a DataFrame
        df = pd.read_excel(file)
        df.columns = df.iloc[0]
        df = df.iloc[1:].reset_index(drop=True)
        frames1.append(df)
#Concatenate frames into dataframe
indoor = pd.concat(frames1)
indoor.astype({
    'Start': 'datetime64',
    'Stop': 'datetime64',
    'LAFmax': 'float64',
    'LAFmin': 'float64',
    'LCpeak': 'float64',
    'LAeq': 'float64'
}).dtypes
keep_same = {'Start', 'Stop'}
indoor.columns = ['{}{}'.format(c, '' if c in keep_same else '_indoor') for c in indoor.columns]

#combined dataframes
dfs = [indoor]
df_final = reduce(lambda left,right: pd.merge(left,right,on='Start'), dfs)
writer=pd.ExcelWriter("combined_sound.xlsx")
df_final.to_excel(writer,sheet_name='sound',index=False)
writer.save()



#%%
"""temperature and RH"""
# grab excel files only
pattern = 'filepath\\*.csv'
writer=pd.ExcelWriter("combined_Temp&RH.xlsx")

# Save all file matches: xlsx_files
xlsx_files = glob.glob(pattern, recursive=True)

dfs=[]
#e.g., extract sensor data with series number 170327921
# Create an empty list: frames
frames1 = []
#  Iterate over csv_files
for file in xlsx_files:
    if '170327921' in file:
        #  Read xlsx into a DataFrame
        df = pd.read_csv(file, header=13,skip_blank_lines=False)
        df = df.iloc[:,0:3]
        ts=[]
        for i in range(0,len(df)):
            ts.append(parser.parse(df['Time'][i]))
        ts=pd.DataFrame(ts)
        df['Time']=ts
        frames1.append(df)
# Concatenate frames into dataframe
data = pd.concat(frames1)
data = data.iloc[:,0:3]
data.columns=['Time', 'Out_Ta_1.1m', 'Out_RH_1.1m']
data=data.drop_duplicates()
data=data.dropna()
data.to_excel(writer,sheet_name='170327921',index=False)
dfs.append(data)

#combined dataframes
df_final = reduce(lambda left,right: pd.merge(left,right,on='Time'), dfs)
df_final=df_final.drop_duplicates()
df_final=df_final.dropna()
df_final.to_excel(writer,sheet_name='Temp&RH',index=False)
writer.save()
 


#%%
"""omnidirectional wind speed"""
# grab excel files only
pattern = 'filepath\\*.csv'
writer=pd.ExcelWriter("combined_omni wind.xlsx")

# Save all file matches: xlsx_files
xlsx_files = glob.glob(pattern, recursive=True)

dfs=[]
frames1 = []
#  Iterate over csv_files
for file in xlsx_files:
    if 'omni_wind_data' in file:
        with open(file) as fd:
            reader=csv.reader(fd)
            interestingrows=[row for idx, row in enumerate(reader) if idx ==2] #extract start timestamp
        T_str=interestingrows[0][1].replace("'", "")
        T_obj=datetime.strptime(T_str, '%y-%m-%d %H:%M:%S')
        
        #read temperature data
        df = pd.read_csv(file, header=10)
        df = df.iloc[:,1:9]
        df_converted=df*5 #convert raw data to real value
        df_converted.columns=['1.1m ID1','1.1m ID2','1.1m ID3','1.1m ID4','0.6m ID1','0.6m ID2','0.6m ID3','0.6m ID4']
        df_cont=pd.concat([df, df_converted], axis=1)
        df_cont['Time'] = pd.date_range(start=T_obj, periods=len(df_cont), freq='1S') #create timestamp
        frames1.append(df_cont)
# Concatenate frames into dataframe
data = pd.concat(frames1)
data=data.drop_duplicates()
data.to_excel(writer,sheet_name='combined_omni',index=False)
writer.save()
  


#%%
"""illuminance"""
# grab excel files only
pattern = 'filepath\\*.txt'
writer=pd.ExcelWriter("combined_light.xlsx")

# Save all file matches: xlsx_files
xlsx_files = glob.glob(pattern, recursive=True)

dfs=[]
frames1 = []
#  Iterate over csv_files
for file in xlsx_files:
    if 'illuminance data' in file:
        df = open(file, "r")
        contents=df.read()
        df.close()
        contents_ = contents.split('\n',5)[-1]
        file_csv=file.replace('txt', 'csv')
        with open(file_csv,"w") as file:
            file.write(contents_ + "\n")
        df1=pd.read_csv(file_csv,engine='python',sep=' ', header=None)
        T_str=df1[0][0].replace("'00", ":00")
        T_obj=parser.parse(T_str)
        lux=df1[[3]]
        lux['Time']=pd.date_range(start=T_obj, periods=len(lux), freq='5T')
        frames1.append(lux)
# Concatenate frames into dataframe
data = pd.concat(frames1)
data=data.drop_duplicates()
data.columns=['lux_indoor', 'Time']
dfs.append(data)
data.to_excel(writer,sheet_name='lux',index=False)
writer.save()



#%% 
"""ultrasonic wind speed"""
# grab excel files only
pattern = 'filepath\\*'
# Save all file matches: xlsx_files
xlsx_files = glob.glob(pattern, recursive=True)

frames1 = []
#  Iterate over csv_files
for file in xlsx_files:
    if 'ultra wind speed data' in file:
        df = open(file, "r")
        contents=df.read()
        df.close()
        contents_ = contents.split('\n',1)[-1]
        file_csv=file+'.csv'
        with open(file_csv,"w", encoding="utf-8") as f:
            f.write(contents_ + "\n")
        
        csv=pd.read_csv(file_csv,engine='python', header=None)
        new=csv[0].str.split(expand = True)
        wind=new.iloc[:,2:6]
        wind.columns=['X','Y','Z','Direction']
        wind.dropna(inplace=True)
        date=new[0].str.split('[',expand = True)[1]
        time=new[1].str.split(']',expand = True)[0]
        tt=pd.concat([date,time],axis=1)
        tt.columns=['date','hms']
        tt['Time_str']=tt['date']+' '+tt['hms']
        tt['Time']=pd.to_datetime(tt['Time_str'], format='%Y-%m-%d %H:%M:%S.%f')
        data1=pd.concat([tt['Time'],wind], axis=1)
        frames1.append(data1)
data = pd.concat(frames1)
data=data.drop_duplicates()
data=data.dropna()
data.to_csv("combined_ultrasonic data.csv",index=False)
