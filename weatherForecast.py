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



if len(place) != 0:
    dates, info = get_data(place, days, option)
    # print(f'dates: {dates}    info:{info}')

    if dates == None:
        st.write(f'{place} does not exist')

    elif option == 'Temperature':
        fig = px.line(x=dates, y=info, labels={'x':'Dates', 'y':'Temp (C)'})
        st.plotly_chart(fig)
            
    elif option == 'Sky':
        # for d, x in zip(dates, info):
        #     st.image(image=f'.\\sky_images\\{x.lower()}.png', caption=d, width=115)
        image_paths = [f'.\\sky_images\\{x.lower()}.png' for x in info]
        print(f'image_paths: {image_paths}')
        st.image(image_paths, width=115)