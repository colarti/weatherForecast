import streamlit as st
import pandas as pd
import plotly.express as px
from backend import get_data
from extractZip import extractAll

st.title('Weather Forecast for the Next Days')

place = st.text_input(label='Place', key='place')

days = st.slider(label='Days', min_value=1, max_value=5, step=1, key='slider', help='Select the number of days')

option = st.selectbox(label='Select data to view', options=['Temperature', 'Sky'], key='selectbox')

st.header(f'{option} for the next {days} days in {place.title()}')

extractAll()

if len(place, days, option) != 0:
    data = get_data(place)
    
    for x in data:
        content = pd.read_json(x)
        print(content)

# fig = px.line(x=dates, y=temp, labels={'x':'Dates', 'y':'Temp (C)'})
# st.plotly_chart(fig)