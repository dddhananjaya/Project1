# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 11:34:34 2019

@author: sidhidatrinayak
"""

import pandas as pd
import numpy as np
from pandas import Series,DataFrame

data=Series(['one','two',np.nan,'four'])
data
#check if it has null values
data.isnull()
#how to handle missing values
data.dropna()
data.fillna('1')

#create a new dataframe

df=DataFrame([[1,2,3],[np.nan,5,6],[7,np.nan,9],[np.nan,np.nan,np.nan]])
df

df.isnull()
df.dropna()
#delete the rows that is having all missing value
df.dropna(how='all')
#if you want to check if the column has missing values or not?
df.dropna(axis=1)

#define a variable for np.nan
npn=np.nan

df2=DataFrame([[1,2,3,npn],[2,npn,5,6],[npn,7,npn,9],[1,npn,npn,npn]])
df2
#the row that is having at least 2 values will get printed
df2.dropna(thresh=2)
#the row that is having at least 3 values will get printed
df2.dropna(thresh=3)


df2
#how to fill the values 

df2.fillna(1)
df2.fillna(0)
df2
df2.fillna({0:1,1:2,2:3,3:4},inplace=True)
df2
df2.fillna(1,inplace=True)
df2
df2
df2.fillna()
dt=pd.read_csv('C:\\dataset\\loan_small.csv')
dt
dt.head(10)
dt.isnull()
dt.info()
dt.isnull().sum()
dt.isna()
data.isna().any()

#Get Missing Values
dt.isnull()
dt.isnull().sum(axis=0)

#handling Missing values
#drop the rows having missing values

cleandata=dt.dropna()
cleandata


#drop the rows having missing values in perticular column
dt
cleandata=dt.dropna(subset=['Loan_Status'])
cleandata

a=10
b=10
c=a
a==b
a==c
c==a

dt1=dt.copy() 
dt2=dt
 #copy of dataset in dt
dt1
cols=['Gender','Area','Loan_Status']
dt1[cols]
dt1[cols].isnull().sum(axis=0)
#replace the missing values in the above three columns with their corresponding mode values

dt1[cols]=dt1[cols].fillna(dt1.mode().iloc[0])
dt1[cols]

#Replace the missing values in the columns having numerical values

cols1=['ApplicantIncome','CoapplicantIncome','LoanAmount']
dt1[cols1]
dt1[cols1].isnull().sum()
dt1[cols1].mean()
dt1[cols1]=dt1[cols1].fillna(dt1.mean())
dt1[cols1]
dt1[cols1].isnull().sum(axis=0)


x=np.array([12,3,3,np.nan,np.nan,5,6,7])
d=pd.DataFrame(x)
d.ffill()
d.bfill()
#--------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------
