# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 11:48:00 2021

@author: CHEN SHISHENG
"""
import glob
import os 
import numpy as np
import pandas as pd
import csv
from datetime import datetime
s
from dateutil import parser
def run():
    
    #%%
    #_______sound data
    # grab excel files only
    pattern = 'F:\\nBOX\\semi research\\001phase 2 analysis\\env data\\*\\sound\\*.xlsx'
    
    # Save all file matches: xlsx_files
    xlsx_files = glob.glob(pattern, recursive=True)
    
    # Create an empty list: frames
    frames1 = []
    #  Iterate over csv_files
    for file in xlsx_files:
        if 'indoor' in file:
            
            #  Read xlsx into a DataFrame
            df = pd.read_excel(file)
            df.columns = df.iloc[0]
            df = df.iloc[1:].reset_index(drop=True)
            # Append df to frames
            frames1.append(df)
    # Concatenate frames into dataframe
    indoor = pd.concat(frames1)
    indoor.astype({'Start': 'datetime64','Stop': 'datetime64','LAFmax': 'float64',
                   'LAFmin': 'float64','LCpeak': 'float64','LAeq': 'float64'}).dtypes
    
    keep_same = {'Start', 'Stop'}
    indoor.columns = ['{}{}'.format(c, '' if c in keep_same else '_indoor') for c in indoor.columns]
    
    frames2 = []
    #  Iterate over csv_files
    for file in xlsx_files:
        if 'outdoor' in file:
            #  Read xlsx into a DataFrame
            print(file)
            df = pd.read_excel(file)
            df.columns = df.iloc[0]
            df = df.iloc[1:].reset_index(drop=True)   
            # Append df to frames
            frames2.append(df)
    # Concatenate frames into dataframe
    outdoor = pd.concat(frames2)
    outdoor.astype({'Start': 'datetime64','Stop': 'datetime64','LAFmax': 'float64',
                   'LAFmin': 'float64','LCpeak': 'float64','LAeq': 'float64'}).dtypes
    keep_same = {'Start', 'Stop'}
    outdoor.columns = ['{}{}'.format(c, '' if c in keep_same else '_outdoor') for c in outdoor.columns]
    
    #merge C1 C2 C3 C4
    dfs = [indoor,outdoor]
    df_final = reduce(lambda left,right: pd.merge(left,right,on='Start'), dfs)
    #save
    writer=pd.ExcelWriter("combined_sound.xlsx")
    indoor.to_excel(writer,sheet_name='indoor raw',index=False)
    outdoor.to_excel(writer,sheet_name='outdoor raw',index=False)
    df_final.to_excel(writer,sheet_name='indoor&outdoor',index=False)
    writer.save()
    #%%
    #_______temperature and RH
    # grab excel files only
    pattern = 'F:\\nBOX\\semi research\\001phase 2 analysis\\env data\\*\\TEM\\*.csv'
    writer=pd.ExcelWriter("combined_Temp&RH.xlsx")
    
    # Save all file matches: xlsx_files
    xlsx_files = glob.glob(pattern, recursive=True)
    
    dfs=[]
    #170327921
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
            # df.columns = df.iloc[0]
            # df = df.iloc[1:].reset_index(drop=True)
            # Append df to frames
            frames1.append(df)
    # Concatenate frames into dataframe
    data = pd.concat(frames1)
    data = data.iloc[:,0:3]
    data.columns=['Time', 'Out_Ta_1.1m', 'Out_RH_1.1m']
    data=data.drop_duplicates()
    data=data.dropna()
    data.to_excel(writer,sheet_name='170327921',index=False)
    
    dfs.append(data)
    
    #170327925
    # Create an empty list: frames
    frames2 = []
    #  Iterate over csv_files
    for file in xlsx_files:
        if '170327925' in file:
            #  Read xlsx into a DataFrame
            df = pd.read_csv(file, header=13,skip_blank_lines=False)
            df = df.iloc[:,0:3]
            ts=[]
            for i in range(0,len(df)):
                ts.append(parser.parse(df['Time'][i]))
            ts=pd.DataFrame(ts)
            df['Time']=ts
            # df.columns = df.iloc[0]
            # df = df.iloc[1:].reset_index(drop=True)
            # Append df to frames
            frames2.append(df)
    # Concatenate frames into dataframe
    data = pd.concat(frames2)
    data = data.iloc[:,0:3]
    data.columns=['Time', 'In_Ta_1.1m', 'In_RH_1.1m']
    data=data.drop_duplicates()
    data=data.dropna()
    data.to_excel(writer,sheet_name='170327925',index=False)
    dfs.append(data)
    
    #170321191
    # Create an empty list: frames
    frames3 = []
    #  Iterate over csv_files
    for file in xlsx_files:
        if '170321191' in file:
            #  Read xlsx into a DataFrame
            df = pd.read_csv(file, header=11,skip_blank_lines=False)
            df = df.iloc[:,0:3]
            ts=[]
            for i in range(0,len(df)):
                ts.append(parser.parse(df['Time'][i]))
            ts=pd.DataFrame(ts)
            df['Time']=ts
            # df.columns = df.iloc[0]
            # df = df.iloc[1:].reset_index(drop=True)
            # Append df to frames
            frames3.append(df)
    # Concatenate frames into dataframe
    data = pd.concat(frames3)
    data = data.iloc[:,0:3]
    data.columns=['Time', 'Out_Tfloor', 'Out_Tglobe']
    data=data.drop_duplicates()
    data=data.dropna()
    data.to_excel(writer,sheet_name='170321191',index=False)
    dfs.append(data)
    
    #170321192
    # Create an empty list: frames
    frames4 = []
    #  Iterate over csv_files
    for file in xlsx_files:
        if '170321192' in file:
            #  Read xlsx into a DataFrame
            df = pd.read_csv(file, header=11,skip_blank_lines=False)
            df = df.iloc[:,0:3]
            ts=[]
            for i in range(0,len(df)):
                ts.append(parser.parse(df['Time'][i]))
            ts=pd.DataFrame(ts)
            df['Time']=ts
            # df.columns = df.iloc[0]
            # df = df.iloc[1:].reset_index(drop=True)
            # Append df to frames
            frames4.append(df)
    # Concatenate frames into dataframe
    data = pd.concat(frames4)
    data = data.iloc[:,0:3]
    data.columns=['Time', 'In_Tfloor', 'In_Ta_0.1m']
    data=data.drop_duplicates()
    data=data.dropna()
    data.to_excel(writer,sheet_name='170321192',index=False)
    dfs.append(data)

     #170325544
    # Create an empty list: frames
    frames5 = []
    #  Iterate over csv_files
    for file in xlsx_files:
        if '170325544' in file:
           
            #  Read xlsx into a DataFrame
            df = pd.read_csv(file, header=11,skip_blank_lines=False)
            df = df.iloc[:,0:3]
            ts=[]
            for i in range(0,len(df)):
                ts.append(parser.parse(df['Time'][i]))
            ts=pd.DataFrame(ts)
            df['Time']=ts

            # df.columns = df.iloc[0]
            # df = df.iloc[1:].reset_index(drop=True)
            # Append df to frames
            frames5.append(df)
    # Concatenate frames into dataframe
    data = pd.concat(frames5)
    data = data.iloc[:,0:3]
    data.columns=['Time', 'In_Ta_0.6m', 'In_Tglobe']
    data=data.drop_duplicates()
    data.set_index('Time', inplace=True)
    data=data.resample('5T').mean()
    data=data.dropna()
   

    data.to_excel(writer,sheet_name='170325544',index=True)
    dfs.append(data)

    # dfs = [df.set_index('Time') for df in dfs]
    # dfs[0].join(dfs[1:])
    
   
    
    df_final = reduce(lambda left,right: pd.merge(left,right,on='Time'), dfs)
    df_final=df_final.drop_duplicates()
    df_final=df_final.dropna()
    df_final.to_excel(writer,sheet_name='combined_Temp&RH',index=False)
    
    
    writer.save()
 
  #%%
    #_______omnidirectional wind speed
    # grab excel files only
    pattern = 'F:\\nBOX\\semi research\\001phase 2 analysis\\env data\\*\\windspeed\\*.csv'
    writer=pd.ExcelWriter("combined_omni wind.xlsx")
    
    # Save all file matches: xlsx_files
    xlsx_files = glob.glob(pattern, recursive=True)
    
    dfs=[]
    #170327921
    # Create an empty list: frames
    frames1 = []
    #  Iterate over csv_files
    for file in xlsx_files:
        if 'SDE4' or 'AUTO' in file:
            with open(file) as fd:
                reader=csv.reader(fd)
                interestingrows=[row for idx, row in enumerate(reader) if idx ==2]
            T_str=interestingrows[0][1].replace("'", "")
            T_obj=datetime.strptime(T_str, '%y-%m-%d %H:%M:%S')
            #  Read xlsx into a DataFrame
            
            df = pd.read_csv(file, header=10)
            df = df.iloc[:,1:9]
            df_converted=df*5
            df_converted.columns=['1.1m ID1','1.1m ID2','1.1m ID3','1.1m ID4','0.6m ID1','0.6m ID2','0.6m ID3','0.6m ID4']
            df_cont=pd.concat([df, df_converted], axis=1)
            df_cont['Time'] = pd.date_range(start=T_obj, periods=len(df_cont), freq='1S')
            
            # df.columns = df.iloc[0]
            # df = df.iloc[1:].reset_index(drop=True)
            # Append df to frames
            frames1.append(df_cont)
    # Concatenate frames into dataframe
    data = pd.concat(frames1)
    data=data.drop_duplicates()
    data.to_excel(writer,sheet_name='combined_omni',index=False)
    writer.save()
    
  #%%
    #_______illuminance
    # grab excel files only
    pattern = 'F:\\nBOX\\semi research\\001phase 2 analysis\\env data\\*\\Light\\*.txt'
    writer=pd.ExcelWriter("combined_light.xlsx")
    
    # Save all file matches: xlsx_files
    xlsx_files = glob.glob(pattern, recursive=True)
    
  
    #indoor lux
    # Create an empty list: frames
    dfs=[]
    frames1 = []
    #  Iterate over csv_files
    for file in xlsx_files:
        if 'in' in file:
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
    data.to_excel(writer,sheet_name='lux_indoor',index=False)
    
    #outdoor lux
    # Create an empty list: frames
    frames2 = []
    #  Iterate over csv_files
    for file in xlsx_files:
        if 'out' in file:
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
       
            frames2.append(lux)
    # Concatenate frames into dataframe
    data = pd.concat(frames2)
    data=data.drop_duplicates()
    data.columns=['lux_outdoor', 'Time']
    dfs.append(data)
    data.to_excel(writer,sheet_name='lux_outdoor',index=False)
    

    df_final = reduce(lambda left,right: pd.merge(left,right,on='Time'), dfs)
    df_final.to_excel(writer,sheet_name='combined_lux',index=False)

    writer.save()
#%% 
  #_______ultrasonic wind speed
    # grab excel files only
    pattern = 'F:\\nBOX\\semi research\\001phase 2 analysis\\env data\\*\\SONIC\\*'
    
    
    # Save all file matches: xlsx_files
    xlsx_files = glob.glob(pattern, recursive=True)
    
  
    #1.4m wind speed
    # Create an empty list: frames
   
    frames1 = []
    #  Iterate over csv_files
    for file in xlsx_files:
        if 'csv' in file:
            None
        else:
            if 'com11' in file:
    
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
                # wind = wind.replace(r'û', '', regex=True)
                # wind = wind.replace(r'þ', '', regex=True)
                # wind.astype('float64').dtypes
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
    data.to_csv("combined_sonic_1_4m.csv",index=False)

    #1.1m wind speed
    # Create an empty list: frames
#%% 
  #_______ultrasonic wind speed for 1.1m
    # grab excel files only
    pattern = 'F:\\nBOX\\semi research\\001phase 2 analysis\\env data\\*\\SONIC\\*'
    # Save all file matches: xlsx_files
    xlsx_files = glob.glob(pattern, recursive=True)
    
    #1.1m wind speed
    frames2 = []
    #  Iterate over csv_files
    for file in xlsx_files:
        if 'csv' in file:
            None
        else:
            if 'com10' in file:
                print(file)
    
                df = open(file, "r")
                contents=df.read()
                df.close()
                contents_ = contents.split('\n',1)[-1]
                file_csv=file+'.csv'
                with open(file_csv,"w", encoding="utf-8") as f:
                    f.write(contents_ + "\n")
                
                csv=pd.read_csv(file_csv,engine='python', header=None, error_bad_lines=False)
                csv.dropna(inplace=True)
                csv.drop_duplicates(inplace=True)
                new=csv[0].str.split(expand = True)
                wind=new.iloc[:,2:6]
                wind.columns=['X','Y','Z','Direction']
                wind.dropna(inplace=True)
                # wind = wind.replace(r'û', '', regex=True)
                # wind = wind.replace(r'þ', '', regex=True)
                # wind.astype('float64').dtypes
                date=new[0].str.split('[',expand = True)[1]
                time=new[1].str.split(']',expand = True)[0]
                tt=pd.concat([date,time],axis=1)
                tt.columns=['date','hms']
                tt['Time_str']=tt['date']+' '+tt['hms']
                tt['Time']=pd.to_datetime(tt['Time_str'], format='%Y-%m-%d %H:%M:%S.%f')
                data1=pd.concat([tt['Time'],wind], axis=1)
                frames2.append(data1)
    data = pd.concat(frames2)
    data=data.drop_duplicates()
    data=data.dropna()
    data.to_csv("combined_sonic_1_1m.csv",index=False)

            

    
    

    
