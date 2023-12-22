import streamlit as st
import pandas as pd

st.title('Weather Forecast for the Next Days')

place = st.text_input(label='Place', key='place')

days = st.slider(label='Days', min_value=1, max_value=5, step=1, key='slider', help='Select the number of days')

option = st.selectbox(label='Select data to view', options=['Temperature', 'Sky'], key='selectbox')

st.header(f'{option} for the next {days} days in {place.title()}')