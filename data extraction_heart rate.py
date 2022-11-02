# -*- coding: utf-8 -*-
#Copyright@ CHEN SHISHENG
"""
@author: CHEN SHISHENG, chenshisheng@u.nus.edu

Codes for data extraction of heart rate data from Polar H10 device
"""

import numpy as np
import pandas as pd
import glob
import os 
import csv
import matplotlib
from datetime import datetime,timedelta
from functools import reduce
from dateutil import parser
import pyhrv
from sklearn.neighbors import LocalOutlierFactor

def extracthrv():    
    """extract heart rate sensor data"""
    df1=pd.read_excel('experiment info file', sheet_name='participant ID')
    df2=pd.read_excel('experiment info file', sheet_name='heart rate sensor series number')
    df3=df2.merge(df1, how='left')
    df3['Date']=df3['Date'].dt.date
    
    # grab excel files only
    pattern = 'filepath\\*.txt'
    
    # Save all file matches: xlsx_files
    xlsx_files = glob.glob(pattern, recursive=True)
    
    hr_files=[]
    for file in xlsx_files:
        if 'HR_' in file:
            hr_files.append(file)
    
    combineds=[]
    for file in hr_files:

        df = open(file, "r")
        contents=df.read()
        df.close()
        contents_ = contents.split('\n',3)[-1]
        contentss_=contents_.replace(" ", ",")
        file_csv=file.replace('txt', 'csv')
        with open(file_csv,"w") as file:
            file.write(contentss_ + "\n")
            
        tl=contents.find('TIME: ')+6
        st1=contents[tl:(tl+10)].replace(".", "-")
        st2=contents[(tl+10):(tl+16)].replace(".", ":")
        st3=st1+st2
        st4=datetime.strptime(st3, '%d-%m-%Y %H:%M')
        
        data=pd.read_csv(file_csv,engine='c', header=None)
        sn=data[1][0]
        data2=data[3:].iloc[:,0:4]
        data2.columns=['HR','RR','MS','SKINCONTACT']
        data2=data2.astype(int)
        data2.reset_index(inplace=True, drop=True)
        data2['Series number']=sn
        data2['Time']=st4
        for i in range(0, len(data2)):
            time_change = timedelta(seconds=data2['MS'][i]/1000)
            data2['Time'][i]=st4+time_change
        st5=st4.date()
        df4=df3.loc[(df3['Date'] == st5) &(df3['Series number'] == sn)]
        df4.reset_index(inplace=True, drop=True)
        data2['ID']=df4['ID'][0]
        data2['Identification code']=df4['Identification code'][0]
        combineds.append(data2)
    combinedss=pd.concat(combineds)
    combinedss.to_csv("combined_Heart Rate.csv", index=False)
    
def hrvforeachcogtest():
    """heart rate data extraction for each cognitive test"""
    matplotlib.use('Agg')
    cog=pd.read_excel('experiment info file', sheet_name='cognitive test experiment time')
    
    dfhrv=pd.read_csv('combined_Heart Rate.csv')
    dfhrv['Time']=pd.to_datetime(dfhrv['Time'], format='%Y-%m-%d %H:%M:%S.%f')
    dfhrv['Date']=dfhrv['Time'].dt.date
    
    df3s=[]
    resultss=[]
    for i in range (0, len(cog)):
        dateinfo=cog['Date'][i]
        idinfo=cog['Identification code'][i]
        t0=cog['Cognitive start time'][i]
        t1=cog['Cognitive end time'][i]
        cogtype=cog['cog test type'][i]
        
        dfhrvi=dfhrv.loc[(dfhrv['Date']== dateinfo) & (dfhrv['Identification code']== idinfo)]
        dfhrvii=dfhrvi.loc[ (t0<= dfhrvi['Time']) &  
                         (dfhrvi['Time'] <= t1) ]
        
        if dfhrvii.empty:
            dfna={'Time':['N/A'],'HR':['N/A'],'RR':['N/A']}
            df3=pd.DataFrame.from_dict(dfna) 
            df3['Identification code']=idinfo
            df3['cog test type']=cogtype
            df3s.append(df3)
            rd={'hr_mean':['N/A'], 'hr_std':['N/A'], 'rmssd':['N/A'], 'pnn50':['N/A'], 'fft_ratio':['N/A'],'ar_ratio':['N/A']}
            results_selected=pd.DataFrame.from_dict(rd)     
            results_selected['Identification code']=idinfo
            results_selected['cog test type']=cogtype
            resultss.append(results_selected)
        elif len(dfhrvii)<=20:
            dfna={'Time':['N/A'],'HR':['N/A'],'RR':['N/A']}
            df3=pd.DataFrame.from_dict(dfna) 
            df3['Identification code']=idinfo
            df3['Qn Order']=cogtype
            df3s.append(df3)
            rd={'hr_mean':['N/A'], 'hr_std':['N/A'], 'rmssd':['N/A'], 'pnn50':['N/A'], 'fft_ratio':['N/A'],'ar_ratio':['N/A']}
            results_selected=pd.DataFrame.from_dict(rd)     
            results_selected['Identification code']=idinfo
            results_selected['Qn Order']=cogtype
            resultss.append(results_selected)
        else:

            df1=dfhrvii[['Time','HR','RR']]
            df1.reset_index(inplace=True, drop=True)
            lof = LocalOutlierFactor()
            yhat = lof.fit_predict(df1[['HR','RR']])
            yhat =pd.DataFrame(yhat)
            yhat.columns=['outlier']
            df2=pd.concat([df1,yhat],axis=1)
            df3=df2.loc[df2['outlier'] != -1]
            df3.reset_index(inplace=True, drop=True)
            df3=df3.drop(columns=['outlier'])
            df3['Identification code']=idinfo
            df3['cog test type']=cogtype
            df3s.append(df3)
            
        
            results=pyhrv.hrv(df3['RR'], show=False,plot_ecg=False, plot_tachogram=False)
            hr_mean=results['hr_mean']
            hr_std=results['hr_std']
            rmssd=results['rmssd']
            pnn50=results['pnn50']
            lfhf_fftratio=results['fft_ratio']
            lfhf_arratio=results['ar_ratio']
            results_selected=pd.DataFrame([hr_mean, hr_std, rmssd, pnn50, lfhf_fftratio, lfhf_arratio]).T
            results_selected.columns=['hr_mean', 'hr_std', 'rmssd', 'pnn50', 'fft_ratio', 'ar_ratio']
            results_selected['Identification code']=idinfo
            results_selected['cog test type']=cogtype
            resultss.append(results_selected)
    df4=pd.concat(df3s)
   
    df4.to_csv('combined_Heart Rate_during cog test.csv', index=False)
    redf=pd.concat(resultss)
    redf.to_excel('processed data_Heart Rate during cog test.xlsx', index=False)

def split():
    """extract data for each participant"""

    dfc=pd.read_csv('combined_Heart Rate_during cog test.csv') 
    dfc['Time']=pd.to_datetime(dfc['Time'], format='%d/%m/%Y %H:%M:%S.%f')
    dfc['Date']=dfc['Time'].dt.date
    ids=pd.unique(dfc['Identification code'])
    writer=pd.ExcelWriter('split_Heart Rate_during cog test.xlsx')
    
    for i in ids:
        df=dfc.loc[dfc['Identification code']==i]
        df.to_excel(writer, sheet_name=i)
    writer.save()
    
def hrvforqtest():
    """heart rate data during subjective measurement timing"""
    matplotlib.use('Agg')
  
    cog=pd.read_excel('experiment info file', sheet_name='subjective measurement timing')

    dfhrv=pd.read_csv('combined_Heart Rate.csv')
    dfhrv['Time']=pd.to_datetime(dfhrv['Time'], format='%Y-%m-%d %H:%M:%S.%f')
    dfhrv['Date']=dfhrv['Time'].dt.date
    
    df3s=[]
    resultss=[]
    for i in range (0, len(cog)):
        dateinfo=cog['Date'][i]
        idinfo=cog['Identification code'][i]
        time_change = timedelta(seconds=60)
        t1=cog['Time'][i]
        t0=t1-time_change
        cogtype=cog['Qn Order'][i]

        dfhrvi=dfhrv.loc[(dfhrv['Date']== dateinfo) & (dfhrv['Identification code']== idinfo)]
        dfhrvii=dfhrvi.loc[ (t0<= dfhrvi['Time']) &  
                         (dfhrvi['Time'] <= t1) ]
        
        if dfhrvii.empty:
            dfna={'Time':['N/A'],'HR':['N/A'],'RR':['N/A']}
            df3=pd.DataFrame.from_dict(dfna) 
            df3['Identification code']=idinfo
            df3['Qn Order']=cogtype
            df3s.append(df3)
            rd={'hr_mean':['N/A'], 'hr_std':['N/A'], 'rmssd':['N/A'], 'pnn50':['N/A'], 'fft_ratio':['N/A'],'ar_ratio':['N/A']}
            results_selected=pd.DataFrame.from_dict(rd)     
            results_selected['Identification code']=idinfo
            results_selected['Qn Order']=cogtype
            resultss.append(results_selected)
        elif len(dfhrvii)<=20:
            dfna={'Time':['N/A'],'HR':['N/A'],'RR':['N/A']}
            df3=pd.DataFrame.from_dict(dfna) 
            df3['Identification code']=idinfo
            df3['Qn Order']=cogtype
            df3s.append(df3)
            rd={'hr_mean':['N/A'], 'hr_std':['N/A'], 'rmssd':['N/A'], 'pnn50':['N/A'], 'fft_ratio':['N/A'],'ar_ratio':['N/A']}
            results_selected=pd.DataFrame.from_dict(rd)     
            results_selected['Identification code']=idinfo
            results_selected['Qn Order']=cogtype
            resultss.append(results_selected)
        else:

            df1=dfhrvii[['Time','HR','RR']]
            df1.reset_index(inplace=True, drop=True)
            lof = LocalOutlierFactor()
            yhat = lof.fit_predict(df1[['HR','RR']])
            yhat =pd.DataFrame(yhat)
            yhat.columns=['outlier']
            df2=pd.concat([df1,yhat],axis=1)
            df3=df2.loc[df2['outlier'] != -1]
            df3.reset_index(inplace=True, drop=True)
            df3=df3.drop(columns=['outlier'])
            df3['Identification code']=idinfo
            df3['Qn Order']=cogtype
            df3s.append(df3)
            
        
            results=pyhrv.hrv(df3['RR'], show=False,plot_ecg=False, plot_tachogram=False)
            hr_mean=results['hr_mean']
            hr_std=results['hr_std']
            rmssd=results['rmssd']
            pnn50=results['pnn50']
            lfhf_fftratio=results['fft_ratio']
            lfhf_arratio=results['ar_ratio']
            results_selected=pd.DataFrame([hr_mean, hr_std, rmssd, pnn50, lfhf_fftratio, lfhf_arratio]).T
            results_selected.columns=['hr_mean', 'hr_std', 'rmssd', 'pnn50', 'fft_ratio', 'ar_ratio']
            results_selected['Identification code']=idinfo
            results_selected['Qn Order']=cogtype
            resultss.append(results_selected)
    df4=pd.concat(df3s)
   
    df4.to_csv('combined_Heart Rate_during subjective measurement.csv', index=False)
    redf=pd.concat(resultss)
    redf.to_excel('processed data_Heart Rate during subjective measurement.xlsx', index=False)
