# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 13:42:16 2021

@author: CHEN SHISHENG
"""
import glob
import os 
import numpy as np
import pandas as pd
import csv
from datetime import datetime,timedelta
from functools import reduce
from dateutil import parser
import re
def run():
    
    #%%
    #_______sound data
    # grab excel files only
    df1=pd.read_excel('phase 2 start end time.xlsx', sheet_name='ID')
    df2=pd.read_excel('phase 2 start end time.xlsx', sheet_name='Skin cond')
    df30=df2.merge(df1, how='right')
    df3=df30.loc[df30['MMDD']>=622]
    df3.reset_index(inplace=True)
    # df3=df2.merge(df1, how='right')
    df4=[]
    
    
    for i in range(0,len(df3)):
        
        
        pattern = 'F:\\nBOX\\semi research\\001phase 2 analysis\\env data\\0'+str(df3['MMDD'][i])+'\\GSR\\*\\*\\*.csv'
        xlsx_files = glob.glob(pattern, recursive=True)
        
        end_n=df3['Series number'][i]
        
        # xlsx_files2=[]
        # for file in xlsx_files:
        #     if '.xlsx' in file:
        #         xlsx_files2.append(file)
        
        # if '.xlsx' in xlsx_files:
        #     for file in xlsx_files:
                
        #         if str(end_n) in file:
        #             print('xlsx', str(end_n), df3['Identification code'][i], df3['MMDD'][i])
        #             df = pd.read_excel(file, header=2)
        #             if not 'uS' in df: 
        #                 df = pd.read_excel(file, header=1)
        #             df_new=df[['yyyy/mm/dd hh:mm:ss.000','uS']]
        #             df_new.columns=['Time', 'Skin conductance']
        #             df_new['Time']=pd.to_datetime(df_new['Time'], format='%Y/%m/%d %H:%M:%S.%f')
        #             df_new['Series number']=str(df3['Series number'][i])
        #             df_new['ID']=df3['ID'][i]
        #             df_new['Identification code']=df3['Identification code'][i]
        #             df4.append(df_new)
        #     break
     
        # else:
        for file in xlsx_files:
            
            if str(end_n) in file:
                
                print('csv', str(end_n), df3['Identification code'][i], df3['MMDD'][i])
                df = pd.read_csv(file, skip_blank_lines=False,engine='python',sep=',', header=1, dtype = {'yyyy/mm/dd hh:mm:ss.000': str})
                if not 'uS' in df: 
                    df = pd.read_csv(file,  skip_blank_lines=False,engine='python',sep='\t', header=2)
                    if not 'uS' in df: 
                        df = pd.read_csv(file, skip_blank_lines=False,engine='python',sep=',', header=2, dtype = {'yyyy/mm/dd hh:mm:ss.000': str})
                df_new=df[['yyyy/mm/dd hh:mm:ss.000','uS']]
                df_new.columns=['Time', 'Skin conductance']
                if len(str(df_new['Time'][0]))==7:
                    
                    file=file.replace('csv','xlsx')
                    
                    if os.path.isfile(file)==False:
                        df_new['Time']='N/A'
                    else:
                        df = pd.read_excel(file, header=2)
                      
                        if not 'uS' in df: 
                            df = pd.read_excel(file, header=1)
                        df_new=df[['yyyy/mm/dd hh:mm:ss.000','uS']]
                        df_new.columns=['Time', 'Skin conductance']
                        if len(str(df_new['Time'][0]))<=15:
    
                            df_new['Time']='N/A'
                        else:
                            df_new['Time']=pd.to_datetime(df_new['Time'], format='%Y/%m/%d %H:%M:%S.%f')
                            df_new['Series number']=str(df3['Series number'][i])
                            df_new['ID']=df3['ID'][i]
                            df_new['Identification code']=df3['Identification code'][i]
                            df4.append(df_new)
                       
                            print('replaced by xlsx', str(end_n), df3['Identification code'][i], df3['MMDD'][i])
                    
                    
                    
                    
                    # df = pd.read_excel(file, header=2)
                    # if not 'uS' in df: 
                    #     df = pd.read_excel(file, header=1)
                    # df_new=df[['yyyy/mm/dd hh:mm:ss.000','uS']]
                    # df_new.columns=['Time', 'Skin conductance']
                    # ts=[]
                    # for i in range (0, len(df_new)):
                    #     ts.append(parser.parse(str(df_new['Time'][i])))
                    
                    # ts=pd.DataFrame(ts)
                    # df_new['Time']=ts.values
                    # df_new['Hour']=df_new['Time'].dt.hour
                    # df_new['Minute']=df_new['Time'].dt.minute
                    # df_new['Second']=df_new['Time'].dt.second
                    # df_new['Fraction']=df_new['Time'].dt.microsecond
                    
                    # hours=[12,13,14,15,16]
                    
                    # dffs=[]
                    # for i in range (0, len(df_new)):
                        
                    #     for mm in range (1,61):
                    #         dff=df_new.loc[(df_new['Minute']==59)&(df_new['Second']==59)]
                    #         dffs.append(dff)
                            
                    
                elif len(str(df_new['Time'][0]))==9:
                    dftime=df_new[['Time']]
                    dftime['Date']=df3['MMDD'][i]
                    dftime['Year']='2021'
                    df_new['Time']=dftime['Year'].map(str)+'/0'+dftime['Date'].map(str)+' '+dftime['Time'].map(str)
                    df_new['Time']=pd.to_datetime(df_new['Time'], format='%Y/%m%d %H:%M:%S.%f')
                else:
                    df_new['Time']=pd.to_datetime(df_new['Time'], format='%Y/%m/%d %H:%M:%S.%f')
            
                df_new['Series number']=str(df3['Series number'][i])
                df_new['ID']=df3['ID'][i]
                df_new['Identification code']=df3['Identification code'][i]
                df4.append(df_new)
    df5=pd.concat(df4)
    df5=df5.drop_duplicates()
    df5.to_csv("combined_skin conductance.csv",index=False)
    #%%
def forEachCog():
    #%%
    dfsc0=pd.read_csv("combined_skin conductance.csv")
    dfsc=dfsc0.loc[dfsc0['Time'] != 'N/A']
    dfsc['Time']=pd.to_datetime(dfsc['Time'], format='%Y/%m/%d %H:%M:%S.%f')
   
    
    df7=pd.read_excel('phase 2 start end time.xlsx', sheet_name='cog timing')
    t0=df7['Cognitive start time']
    t1=df7['Cognitive end time']

    
    datas=[]
    for i in range(0, len(t1)):

        data=dfsc.loc[ (parser.parse(str(t0[i])) <= dfsc['Time']) &  (dfsc['Time'] <= parser.parse(str(t1[i]))) ]
        data2=data.loc[data['Identification code']==df7['Identification code'][i]]
        data2=data2.drop(['Time','Identification code', 'Series number', 'ID'], axis=1)
        avg=pd.DataFrame(data2.mean()).T
        avg=avg.add_suffix('_avg')
        std=pd.DataFrame(data2.std()).T
        std=std.add_suffix('_std')
        score=pd.concat([avg,std],axis=1)
    
        
        datas.append(score)

    datass=pd.concat(datas)
    datass.reset_index(inplace=True, drop=True)
    datasss=pd.concat([df7,datass], axis=1)
    datasss.to_excel('results_each cognitive test_skin conductance.xlsx')
    #%%
def forwholecog():
    #%%
    dfsc0=pd.read_csv("combined_skin conductance.csv")
    dfsc=dfsc0.loc[dfsc0['Time'] != 'N/A']
    dfsc['Time']=pd.to_datetime(dfsc['Time'], format='%Y/%m/%d %H:%M:%S.%f')
   
    
    df7=pd.read_excel('phase 2 start end time.xlsx', sheet_name='cog timing start end')
    t0=df7['Cognitive start time']
    t1=df7['Cognitive end time']

    
    datas=[]
    for i in range(0, len(t1)):

        data=dfsc.loc[ (parser.parse(str(t0[i])) <= dfsc['Time']) &  (dfsc['Time'] <= parser.parse(str(t1[i]))) ]
        data2=data.loc[data['Identification code']==df7['Identification code'][i]]
        data2=data2.drop(['Time','Identification code', 'Series number', 'ID'], axis=1)
        avg=pd.DataFrame(data2.mean()).T
        avg=avg.add_suffix('_avg')
        std=pd.DataFrame(data2.std()).T
        std=std.add_suffix('_std')
        score=pd.concat([avg,std],axis=1)
    
        
        datas.append(score)

    datass=pd.concat(datas)
    datass.reset_index(inplace=True, drop=True)
    datasss=pd.concat([df7,datass], axis=1)
    datasss.to_excel('results_whole cognitive test_skin conductance.xlsx')
    #%%
def forquestion():
    #%%
    dfsc0=pd.read_csv("combined_skin conductance.csv")
    dfsc=dfsc0.loc[dfsc0['Time'] != 'N/A']
    dfsc['Time']=pd.to_datetime(dfsc['Time'], format='%Y/%m/%d %H:%M:%S.%f')
   
    
    df7=pd.read_excel('phase 2 start end time.xlsx', sheet_name='q timing')
    time_change = timedelta(seconds=60)
    t1=df7['Time']
    t1=t1.squeeze()
    t0=t1-time_change
    t0=t0.squeeze()

    
    datas=[]
    for i in range(0, len(t1)):

        data=dfsc.loc[ (parser.parse(str(t0[i])) <= dfsc['Time']) &  (dfsc['Time'] <= parser.parse(str(t1[i]))) ]
        data2=data.loc[data['Identification code']==df7['Identification code'][i]]
        data2=data2.drop(['Time','Identification code', 'Series number', 'ID'], axis=1)
        avg=pd.DataFrame(data2.mean()).T
        avg=avg.add_suffix('_avg')
        std=pd.DataFrame(data2.std()).T
        std=std.add_suffix('_std')
        score=pd.concat([avg,std],axis=1)
    
        
        datas.append(score)

    datass=pd.concat(datas)
    datass.reset_index(inplace=True, drop=True)
    datasss=pd.concat([df7,datass], axis=1)
    datasss.to_excel('results_questionnaire test_skin conductance.xlsx')
#%%
def split():
#%%
    dfc=pd.read_csv("combined_skin conductance.csv")
    dfc['Time']=pd.to_datetime(dfc['Time'], format='%Y-%m-%d %H:%M:%S.%f')
    dfc['Date']=dfc['Time'].dt.date
    
    ids=pd.unique(dfc['Identification code'])
    
    writer=pd.ExcelWriter('split_skin conductance.xlsx')
    
    for i in ids:
        df=dfc.loc[dfc['Identification code']==i]
        df.to_excel(writer, sheet_name=i)
    writer.save()
    