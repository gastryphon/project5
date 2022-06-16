#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import streamlit as st

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

from sklearn import datasets

pd.set_option("display.max_columns", 50)

#layout

st.set_page_config(layout="wide")


#Set title

st.title("HR, Comapnies & Target Employees")

#Load data
df=pd.read_csv(r'/Users/davidpitoun/All_Ironhack/project5/HR_Data_target.xlsx - aug_test.csv')
df

#plot test

#charts

pivot1 = pd.pivot_table(
    data=df,
    index='education_level',
    columns='relevent_experience',
    values='training_hours',
    margins=True
)

gender_count=pd.crosstab(df.education_level, df.gender)
gender_count

# average training per discipline
pivot2 = pd.pivot_table(
    data=df,
    index='major_discipline',
    values='training_hours'
)

com_size3 = pd.pivot_table(
    data=df,
    index='company_size',
    values='city_development_index',
    aggfunc='sum'
)

tab4=pd.crosstab(df.major_discipline, df.target)

chart6=pd.pivot_table(data=df,index=df['company_size'], columns=df['target'],values='target',aggfunc='sum')


# know the education level based on their discipline

chart5=pd.crosstab(df.major_discipline, df.education_level, normalize = True).plot.bar(stacked=True)


#sidebar

    #show dataset in sidebar
                        
st.sidebar.write("Table1: Education Level, experience & training Hours")

st.sidebar.write(" Table2: Gender Count by education level")

st.sidebar.write( "Table3: Average training per discipline")

st.sidebar.write(" Table4: City Development per Company Size")

st.sidebar.write("Table5: Major Discipline in demand")

st.sidebar.write("Table6: Company size in demand")

st.sidebar.write(" Chart1: Education Level per discipline")

container1 = st.container()
col1, col2 = st.columns(2)

with container1:
    with col1:
        pivot1
        pivot2
    with col2:
       com_size3.head(4)
       tab4

container2 = st.container()
col3, col4 = st.columns(2)

with container2:
    with col3:
        chart6
    with col4:
        chart5
        