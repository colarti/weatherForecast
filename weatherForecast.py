import streamlit as st
import pandas as pd
import plotly.express as px

st.title('Weather Forecast for the Next Days')

place = st.text_input(label='Place', key='place')

days = st.slider(label='Days', min_value=1, max_value=5, step=1, key='slider', help='Select the number of days')

option = st.selectbox(label='Select data to view', options=['Temperature', 'Sky'], key='selectbox')

st.header(f'{option} for the next {days} days in {place.title()}')


def get_data(days):
    dates = ['2022-10-25', '2022-10-26', '2022-10-27', '2022-10-28', '2022-10-29']
    # temp = [(-4, 8), (0, 10), (1,11), (3,15), (-2, 7)]
    temp = [5, 7, 9, 12, 11]
    return dates[0:days], temp[0:days]

dates, temp = get_data(days)

fig = px.line(x=dates, y=temp, labels={'x':'Dates', 'y':'Temp (C)'})
st.plotly_chart(fig)