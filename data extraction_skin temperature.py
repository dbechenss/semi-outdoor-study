# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 17:05:19 2021

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
    df2=pd.read_excel('phase 2 start end time.xlsx', sheet_name='ibutton')
    df3=df2.merge(df1, how='right')
    df4=[]
    

    for i in range(0,len(df3)):
        
        pattern = 'F:\\nBOX\\semi research\\001phase 2 analysis\\env data\\0'+str(df3['MMDD'][i])+'\\IBUTTON\\'+df3['ID'][i]+'\\*.csv'
        xlsx_files = glob.glob(pattern, recursive=True)
        
        end_n=df3['Device'][i][-5:]
        # end_n=pd.DataFrame(end_n)
        for file in xlsx_files:
            
            # if not end_n.empty:
            if end_n in file:

                df = pd.read_csv(file, header=19, skip_blank_lines=False)
                df['Time']=df.index+df['Date/Time']
                # ts=[]
                # for j in range(0,len(df)):
                #     t=parser.parse(df['Time'][j])
                #     t=pd.Series(t)
                #     ts.append(t)
                # ts=pd.concat(ts, ignore_index=True)
                ts=[]
                for j in range(0,len(df)):
                    t=datetime.strptime(df['Time'][j], '%d/%m/%y %I:%M:%S %p')
                    t=pd.Series(t)
                    ts.append(t)
                ts=pd.concat(ts, ignore_index=True)
               
                value=pd.Series(df['Value'].values)
                df_new=pd.concat([ts, value],axis=1)
                df_new.columns=['Time','Tskin']
                df_new['Device']=df3['Device'][i]
                df_new['ID']=df3['ID'][i]
                df_new['Location']=df3['Location'][i]
                df_new['Identification code']=df3['Identification code'][i]
                df4.append(df_new)
    df5=pd.concat(df4)
    writer=pd.ExcelWriter("combined_skin tem.xlsx")    
    df5.to_excel(writer,index=False)
    writer.save()
    #%%
def forcog():
    #%%
    df5=pd.read_excel("combined_skin tem.xlsx")
    locations=pd.unique(df5['Location'])
    df6s=[]
    for i in locations:
        df6=df5.loc[df5['Location']==i]
        df6=df6.drop(['Location','Device','ID'], axis=1)
        df6.rename(columns={'Tskin':i},inplace=True)
        df6s.append(df6)
    
    df7=pd.read_excel('phase 2 start end time.xlsx', sheet_name='cog timing')
    t0=df7['Cognitive start time']
    t1=df7['Cognitive end time']
    
    df8s=[]
    for df in df6s:
        
        datas=[]
        for i in range(0, len(t1)):

            data=df.loc[ (parser.parse(str(t0[i])) <= df['Time']) &  (df['Time'] <= parser.parse(str(t1[i]))) ]
            data2=data.loc[data['Identification code']==df7['Identification code'][i]]
            data2=data2.drop(['Time','Identification code'], axis=1)
            avg=pd.DataFrame(data2.mean()).T
            avg=avg.add_suffix('_avg')
            std=pd.DataFrame(data2.std()).T
            std=std.add_suffix('_std')
            score=pd.concat([avg,std],axis=1)
        
            
            datas.append(score)
            
            
        dat=pd.concat(datas)
      
        df8s.append(dat)
    df9=pd.concat(df8s, axis=1)
#%%    
def duringwholecog():
    #%%
    df5=pd.read_excel("combined_skin tem.xlsx")
    locations=pd.unique(df5['Location'])
    df6s=[]
    for i in locations:
        df6=df5.loc[df5['Location']==i]
        df6=df6.drop(['Location','Device','ID'], axis=1)
        df6.rename(columns={'Tskin':i},inplace=True)
        df6s.append(df6)
    #adding cog time
    cog=pd.read_excel('F:\\nBOX\\semi research\\001phase 2 analysis\\cog test\\cog data phase2.xlsx', sheet_name='combined cleared')
    cog['Cognitive start time']='N/A'
    cog['Cognitive end time']='N/A'
    
    names=['digit', 'mindmap', 'typing', 'stroop']
    for name in names:
           
            cog['start_'+name]=pd.to_datetime(cog['start_'+name], format='%Y-%m-%d %H:%M:%S')
            cog['end_'+name]=pd.to_datetime(cog['end_'+name], format='%Y-%m-%d %H:%M:%S')
    for i in range(0, len(cog)):
        ts=[]
        for name in names:
           
            t1=cog['start_'+name][i]
            t2=cog['end_'+name][i]
            ts.append(t1)
            ts.append(t2)
        cog['Cognitive start time'][i]=min(ts)
        cog['Cognitive end time'][i]=max(ts)
    
    cog1=cog[['Date','Identification code','Cognitive start time','Cognitive end time','Case']]
    
    
    #create extract timing
    df70=pd.read_excel('phase 2 start end time.xlsx', sheet_name='cog timing')
    df71=df70[['Date','Identification code','Case','cog test type']]
    df7=df71.merge(cog1, how='left', sort=False)
    #extracting
    t0=df7['Cognitive start time']
    t1=df7['Cognitive end time']
    
    df8s=[]
    for df in df6s:
        
        datas=[]
        for i in range(0, len(t1)):

            data=df.loc[ (parser.parse(str(t0[i])) <= df['Time']) &  (df['Time'] <= parser.parse(str(t1[i]))) ]
            data2=data.loc[data['Identification code']==df7['Identification code'][i]]
            data2=data2.drop(['Time','Identification code'], axis=1)
            avg=pd.DataFrame(data2.mean()).T
            avg=avg.add_suffix('_avg')
            std=pd.DataFrame(data2.std()).T
            std=std.add_suffix('_std')
            score=pd.concat([avg,std],axis=1)
        
            
            datas.append(score)
            
            
        dat=pd.concat(datas)
      
        df8s.append(dat)
    df9=pd.concat(df8s, axis=1)
    #%%
def forques():
    #%%
    df5=pd.read_excel("combined_skin tem.xlsx")
    locations=pd.unique(df5['Location'])
    df6s=[]
    for i in locations:
        df6=df5.loc[df5['Location']==i]
        df6=df6.drop(['Location','Device','ID'], axis=1)
        df6.rename(columns={'Tskin':i},inplace=True)
        df6s.append(df6)
    
    df7=pd.read_excel('phase 2 start end time.xlsx', sheet_name='q timing')
    time_change = timedelta(seconds=60)
    t1=df7['Time']
    t1=t1.squeeze()
    t0=t1-time_change
    t0=t0.squeeze()

    
    df8s=[]
    for df in df6s:
        
        datas=[]
        for i in range(0, len(t1)):

            data=df.loc[ (parser.parse(str(t0[i])) <= df['Time']) &  (df['Time'] <= parser.parse(str(t1[i]))) ]
            data2=data.loc[data['Identification code']==df7['Identification code'][i]]
            data2=data2.drop(['Time','Identification code'], axis=1)
            avg=pd.DataFrame(data2.mean()).T
           
        
            
            datas.append(avg)
            
            
        dat=pd.concat(datas)
      
        df8s.append(dat)
    df9=pd.concat(df8s, axis=1)
#%%
def split():
    df1=pd.read_excel("combined_skin tem.xlsx")
    loc=pd.unique(df1['Location'])
    df2s=[]
    for i in loc:
        df2=df1.loc[df1['Location'] == i]
        df2.drop(labels=['Location','Device', 'ID'],inplace=True,axis=1)
        
        df2.rename(columns={'Tskin': i}, inplace=True)
        # df2.rename(columns={'Location': i}, inplace=True)
        df2s.append(df2)
        
#%%       
    df3 = reduce(lambda left,right: pd.merge(left,right,how='outer'), df2s)
    df3.to_excel('combined_skin tem&location.xlsx', index=False)
    #import time
    exptime=pd.read_excel('phase 2 start end time.xlsx', sheet_name='q timing')
   
    writer1=pd.ExcelWriter('split_skin tem.xlsx')
    writer2=pd.ExcelWriter('split_skin tem_with Tskinavg.xlsx')
    ids=pd.unique(df3['Identification code'])
    ids.sort()
   
    cases=['C1','C2','C3','C4']
    for j in ids:
        df4=df3.loc[df3['Identification code'] == j]
        
        df5=df4[['Time', 'Identification code']]
        df6=df4.drop(['Time', 'Identification code'],axis=1)
        df7=pd.concat([df5,df6],axis=1)
        df7.sort_values(by=['Time'], inplace=True)
        df7.to_excel(writer1, sheet_name=j,index=False)
        
        alls=[]
        
        for case in cases:
            if case == 'C4' and j =='N936':
                pass
            else:
                case1=exptime.loc[(exptime['Case']==case) & (exptime['Identification code']==j)]
                # time_change = timedelta(minutes=80)
                # t0=case1.loc[case1['Qn Order']== '0th']['Time']
                # t1=t0+time_change
                if case == 'C4':
                    t0=case1.loc[case1['Qn Order']== '0th']['Time']
                    t1=case1.loc[case1['Qn Order']== '50th']['Time']
                else:
                    t0=case1.loc[case1['Qn Order']== '0th']['Time']
                    t1=case1.loc[case1['Qn Order']== '70th']['Time']
                t0=t0.reset_index(drop=True)
                t1=t1.reset_index(drop=True)
                
                data=df7.loc[ (parser.parse(str(t0[0])) <= df7['Time']) &  
                         (df7['Time'] <= parser.parse(str(t1[0]))) ]
                
         
                data['Case']=case
                data['Group']=pd.unique(case1['Group'])[0]
                data['Start time']=str(t0[0])
                data['End time']=str(t1[0])
                alls.append(data)
        allss=pd.concat(alls)
        allss['Time']=allss['Time'].dt.round(freq='1s')
        allss.to_excel(writer1, sheet_name=j,index=False)
        allss2=allss[['Time', 'Identification code','Case', 'Group', 'Start time', 'End time']]
        
        df8=allss.resample(on='Time',rule='10S').mean()
        df8['Tskin_avg']=df8.mean(axis=1,skipna=False)
        df8.reset_index(inplace=True) 
        
        allss2['Time']=allss2['Time'].dt.round(freq='10s')
        allss2.drop_duplicates(inplace=True)
        
        df9=df8.merge(allss2, how='left')     
        labels=list(df9.columns)
        labels.remove('Time')
        df9.dropna(subset=labels, how='all', inplace=True)            
        df9.to_excel(writer2, sheet_name=j,index=False)
        
    writer1.save()
    writer2.save()
    
    
                                