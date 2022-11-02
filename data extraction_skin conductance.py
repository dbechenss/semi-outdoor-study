# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
#Copyright@ CHEN SHISHENG
"""
@author: CHEN SHISHENG, chenshisheng@u.nus.edu

Codes for data extraction of skin conductance measured by Shimmer 3
"""
import glob
import os 
import pandas as pd
from dateutil import parser

def extract():
    """extract skin conductance sensor data"""
    df1=pd.read_excel('experiment info file', sheet_name='participant ID')
    df2=pd.read_excel('experiment info file', sheet_name='skin conductance sensor series number')
    df3=df2.merge(df1, how='right')
    df3.reset_index(inplace=True)
    df4=[]

    for i in range(0,len(df3)):
        pattern = 'filepath\\*.csv'
        xlsx_files = glob.glob(pattern, recursive=True)
        end_n=df3['Series number'][i]
        for file in xlsx_files:
            if str(end_n) in file:
                print('csv', str(end_n), df3['participant ID'][i], df3['MMDD'][i])
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
                            df_new['participant ID']=df3['participant ID'][i]
                            df4.append(df_new)
                            print('replaced by xlsx', str(end_n), df3['participant ID'][i], df3['MMDD'][i])
                    
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
                df_new['participant ID']=df3['participant ID'][i]
                df4.append(df_new)
    df5=pd.concat(df4)
    df5=df5.drop_duplicates()
    df5.to_csv("combined_skin conductance.csv",index=False)
    
def forEachCog():
    """skin conductance data extraction for each cognitive test"""
    dfsc0=pd.read_csv("combined_skin conductance.csv")
    dfsc=dfsc0.loc[dfsc0['Time'] != 'N/A']
    dfsc['Time']=pd.to_datetime(dfsc['Time'], format='%Y/%m/%d %H:%M:%S.%f')
   
    df7=pd.read_excel('experiment info file', sheet_name='cognitive test experiment time')
    t0=df7['Cognitive start time']
    t1=df7['Cognitive end time']
    
    datas=[]
    for i in range(0, len(t1)):
        data=dfsc.loc[ (parser.parse(str(t0[i])) <= dfsc['Time']) &  (dfsc['Time'] <= parser.parse(str(t1[i]))) ]
        data2=data.loc[data['participant ID']==df7['participant ID'][i]]
        data2=data2.drop(['Time','participant ID', 'Series number', 'table ID'], axis=1)
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
    

def forquestion():
    """skin conductance data during subjective measurement period"""
    dfsc0=pd.read_csv("combined_skin conductance.csv")
    dfsc=dfsc0.loc[dfsc0['Time'] != 'N/A']
    dfsc['Time']=pd.to_datetime(dfsc['Time'], format='%Y/%m/%d %H:%M:%S.%f')
   
    df7=pd.read_excel('experiment info file', sheet_name='subjective measurement period')
    time_change = timedelta(seconds=60)
    t1=df7['Time']
    t1=t1.squeeze()
    t0=t1-time_change
    t0=t0.squeeze()

    datas=[]
    for i in range(0, len(t1)):
        data=dfsc.loc[ (parser.parse(str(t0[i])) <= dfsc['Time']) &  (dfsc['Time'] <= parser.parse(str(t1[i]))) ]
        data2=data.loc[data['participant ID']==df7['participant ID'][i]]
        data2=data2.drop(['Time','participant ID', 'Series number', 'table ID'], axis=1)
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

def split():
    """extract data for each participant"""
    dfc=pd.read_csv("combined_skin conductance.csv")
    dfc['Time']=pd.to_datetime(dfc['Time'], format='%Y-%m-%d %H:%M:%S.%f')
    dfc['Date']=dfc['Time'].dt.date
    
    ids=pd.unique(dfc['participant ID'])
    writer=pd.ExcelWriter('split_skin conductance.xlsx')
    for i in ids:
        df=dfc.loc[dfc['participant ID']==i]
        df.to_excel(writer, sheet_name=i)
    writer.save()
    