import pandas as pd
import streamlit as st
import datetime
from datetime import date
data=pd.read_csv('mumbai.csv')
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
price_list=[3000,5000,6000,7000,9000,11000,13000,15000,17000]

prices=st.selectbox("Please enter price",price_list)
ratings=st.selectbox("Select star rating",star_list)
data=data.loc[(data['Star Rating']==ratings) & (data['Price']<=prices)]
st.write(data)
HOTEL_list=[]
for i in data['Hotel Name']:
    HOTEL_list.append(i)
Hotel=st.selectbox("SELECT HOTEL NAME YOU WANT TO BOOK",HOTEL_list)
data=data.loc[(data['Hotel Name']==Hotel)]
st.write(data)
mem_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
child_list=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
check_in_date=st.date_input("enter check in date:",datetime.date(2023,9,21))
check_out_date=st.date_input("enter check out date:",datetime.date(2023,9,21))
members=st.selectbox("No.of adult members staying",mem_list)
children=st.selectbox("child:",child_list)
room_list=['suite','connecting rooms','deluxe room']
room_list1=[1,2,3,4,5,6]
r=st.selectbox("type of rooms:",room_list)
r1=st.selectbox('No.of rooms:',room_list1)
data=data.loc[(data['Hotel Name']==Hotel)]
from datetime import date
from functools import reduce
 
st.header("AMOUNT TO BE PAID FOR BOOKING")
def numOfDays(date1, date2):
    return reduce(lambda x, y: (y-x).days, [date1, date2])

timedelta=numOfDays(check_in_date, check_out_date)
i=data['Price']
j=data['Tax']
if timedelta==0:
    st.write(i+j)
else:
    st.write((i*timedelta*r1)+j)
st.button("BOOK")
from streamlit_extras.switch_page_button import switch_page
c=st.button("GO BACK TO HOME")
if c:
    switch_page('openingpage1')

