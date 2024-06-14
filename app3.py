import pandas as pd
import streamlit as st
import datetime
from datetime import date
from streamlit_extras.switch_page_button import switch_page
data=pd.read_csv('kolkata.csv')
star_list=[2,3,4,5]
data['Star Rating']=data['Star Rating'].fillna('4')
data['Nearest Landmark']=data['Nearest Landmark'].fillna('Not Given')
data['Distance to Landmark']=data['Distance to Landmark'].fillna('0 km')
data['Tax']=data['Tax'].replace(',','',regex=True)
data['Price']=data['Price'].replace(',','',regex=True)
data=data.astype({'Price':'float'})
data=data.astype({'Star Rating':'int'})
data['Tax']=data['Tax'].fillna('843.02')
data=data.astype({'Tax':'float'})
st.write(data)
want_to_contribute=st.button("BOOK HOTEL")

if want_to_contribute:
    switch_page("BOOK3")