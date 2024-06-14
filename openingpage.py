

import streamlit as st
import base64
st.header("WELCOME TO GREENXPLORE")

from streamlit_extras.switch_page_button import switch_page
want_to_contribute = st.button("hotels in delhi")
want_to_contribute1=st.button("hotels in mumbai")
want_to_contribute2=st.button("hotels in bangalore")
want_to_contribute3=st.button("hotels in kolkata")
want_to_contribute4=st.button("hotels in hyderabad")
want_to_contribute5=st.button("hotels in chennai")

if want_to_contribute:
    switch_page("app")
if want_to_contribute1:
    switch_page("app1")
if want_to_contribute2:
    switch_page("app2")
if want_to_contribute3:
    switch_page("app3")
if want_to_contribute4:
    switch_page("app4")
if want_to_contribute5:
    switch_page("app5")


from PIL import Image
image=Image.open('Screenshot 2023-09-21 171349.png')
image1=Image.open('Screenshot 2023-09-21 171428.png')
st.image([image,image1])

