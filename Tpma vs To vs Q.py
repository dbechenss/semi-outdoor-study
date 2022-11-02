# -*- coding: utf-8 -*-
#Copyright@ CHEN SHISHENG
"""
@author: CHEN SHISHENG, chenshisheng@u.nus.edu

Codes for Tpma To and subjective data
"""

import pandas as pd
from dateutil import parser
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)

fig, ax = plt.subplots(figsize=(10, 6))
writer2=pd.ExcelWriter('Tpma&To&Q.xlsx')
excels=['2020', '2021']
colors=['blue', 'orange']
counts=[]
for excel, color in zip(excels, colors):
    
    df1=pd.read_excel('scatter plot.xlsx', sheet_name=excel+' weather')
    times=[]
    for i in range(0,len(df1)):
        time=parser.parse(str(df1['Time_o'][i]))
        times.append(time)
    times=pd.DataFrame(times)
    df1['Time']=times
    
    df2=df1.resample(rule='1D', on='Time').mean()
    tra1=df2['Ta'][0:7].mean()
    toa=df2['Ta']
    df2['Tra']='N/A'
    df2['Tpma']='N/A'
    
    alpha=0.9
    for i in range(0, len(df2)):
        if i in range(0,7):
            pass
            
        elif i ==7:
            tpma=(1-alpha)*toa[i-1]+alpha*tra1
            df2['Tra'][i]=tra1
            df2['Tpma'][i]=tpma
            
        else:
            tra_n_1=df2['Tpma'][i-1]
            tpma=(1-alpha)*toa[i-1]+alpha*tra_n_1
            df2['Tra'][i]=tra_n_1
            df2['Tpma'][i]=tpma
    df2['Date']=df2.index.date
    
    df3=pd.read_excel('scatter plot.xlsx', sheet_name=excel)
    times=[]
    for i in range(0,len(df3)):
        time=parser.parse(str(df3['Time'][i]))
        times.append(time)
    times=pd.DataFrame(times)
    df3['Time']=times
    df3['Date']=df3['Time'].dt.date
    
    df4=df2[['Date','Ta','Tra','Tpma']]
    df4.reset_index(inplace=True, drop=True)
    df5=df4.merge(df3, on='Date')
    df5['Upper 80%']=df5['Tpma']*0.31+21.3
    df5['Lower 80%']=df5['Tpma']*0.31+14.3
    df5['Upper 90%']=df5['Tpma']*0.31+20.3
    df5['Lower 90%']=df5['Tpma']*0.31+15.3
    
    df2.to_excel(writer2, sheet_name=excel+' Tpma')
    
    #check acceptability
    df5['Acceptability']='N/A'
    for i in range(0, len(df5)):
        if (df5['To'][i]<=df5['Upper 80%'][i]) & (df5['To'][i]>=df5['Lower 80%'][i]):
            df5['Acceptability'][i]='Accepted'
        else:
            df5['Acceptability'][i]='Rejected'
    df5.to_excel(writer2, sheet_name=excel+' Tpma&To')        
            
    df6=df5.loc[df5['Q acceptability']=='Accepted']
    df7=df5.loc[df5['Q acceptability']=='Rejected']
    #How many percentage of subjects Q unacceptable within 80% acceptability limit?
    df10=df5.loc[df5['Acceptability']=='Accepted']
    if len(df10) == 0:
        pent1=0
        length1=0
    else:
        df11=df10.loc[df10['Q acceptability']=='Rejected']
        length1=len(df11)
        pent1=len(df11)/len(df10)
    #How many percentage of subjects Q acceptable without 80% acceptability limit?
    df12=df5.loc[df5['Acceptability']=='Rejected']
    if len(df12) == 0:
        pent2=0
        length2=0
    else:
        df13=df12.loc[df12['Q acceptability']=='Accepted']
        length2=len(df13)
        pent2=len(df13)/len(df12)
    
    counts.append({'Total 80% acceptable': len(df10), 'Q unacceptable within 80%': length1,
                   'Total 80% unacceptable': len(df12), 'Q acceptable outside 80%': length2,
                   'Q unacceptable within 80%/Total 80% acceptable': pent1, 'Q acceptable outside 80%/Total 80% unacceptable': pent2})
    print(round(pent2,2)*100, round(pent1,2)*100)

    plt.scatter(df6['Tpma'], df6['To'],  c=color, label=excel+' Q Acceptable', marker='o')
    plt.scatter(df7['Tpma'], df7['To'],  c=color, label=excel+' Q Unacceptable', marker='^',edgecolors='red')
    if excel=='2020':
        plt.plot(df5['Tpma'], df5['Upper 80%'], c='k',linestyle='solid', label='80% acceptability limits')
        plt.plot(df5['Tpma'],  df5['Lower 80%'],  c='k',linestyle='solid')
        
        plt.plot(df5['Tpma'], df5['Upper 90%'], c='k',linestyle='dashed', label='90% acceptability limits')
        plt.plot(df5['Tpma'],  df5['Lower 90%'],  c='k',linestyle='dashed')
    else:
        plt.plot(df5['Tpma'], df5['Upper 80%'], c='k',linestyle='solid')
        plt.plot(df5['Tpma'],  df5['Lower 80%'],  c='k',linestyle='solid')
        
        plt.plot(df5['Tpma'], df5['Upper 90%'], c='k',linestyle='dashed')
        plt.plot(df5['Tpma'],  df5['Lower 90%'],  c='k',linestyle='dashed')
    
ax.legend( ncol=1, bbox_to_anchor=(1.05, 1))
ax.set_ylabel('operative temperature(\xb0C)')
ax.set_xlabel('prevailing mean outdoor air temperature(\xb0C)')
ax.xaxis.set_major_locator(MultipleLocator(0.5))
ax.xaxis.set_minor_locator(MultipleLocator(0.1))
ax.yaxis.set_major_locator(MultipleLocator(1))
ax.yaxis.set_minor_locator(MultipleLocator(0.5))
ax.grid(True)   
fig.tight_layout()
plt.savefig('Tpma&To&Q.jpg', dpi=300)

counts=pd.DataFrame(counts).T
counts.columns=['2020','2021']
counts.to_excel(writer2, sheet_name='counts')
writer2.save()

    