import streamlit as st
import streamlit.components.v1 
import streamlit as st


from streamlit_extras.switch_page_button import switch_page
import streamlit as st

st.set_page_config(initial_sidebar_state="collapsed",layout="wide")


b=st.button('EXPLORE HOTELS')
c=st.button('CHECK WEATHER')
d=st.button("MAP")
e=st.button("AUDIOBOOKS")
if b:
    switch_page('openingpage')
if c:
    switch_page('weather')
if d:
    switch_page('map')
if e:
    switch_page('audiobook')