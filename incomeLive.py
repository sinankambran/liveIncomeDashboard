import streamlit as st
import pandas as pd
import numpy as np
import time
import plotly.express as px
st.set_page_config(
    page_title='Live Income Dashboard',
    layout='wide'
)


st.title('Live Income Data Monitoring App')

df = pd.read_csv('test.csv')

job_filter = st.selectbox('Choose a job',df['occupation'].unique())

placeholder = st.empty()

df = df[df['occupation']==job_filter]

while True:
    df['new_age'] = df['age'] * np.random.choice(range(1,5))
    df['whpw_new'] = df['hours-per-week'] * np.random.choice(range(1,5))

    avg_age = np.mean(df['new_age'])
    count_married = int(df[df['marital-status']=='Married-civ-spouse']['marital-status'].count()+np.random.choice(range(1,30)))

    hpw = np.mean(df['whpw_new'])
    with placeholder.container():
        kpi1,kpi2,kpi3 = st.columns(3)
        kpi1.metric(label='Age',value=round(avg_age),delta=round(avg_age) - 10)
        kpi2.metric(label='Married Count',value=int(round(count_married)),delta=10+count_married)
        kpi3.metric(label='Working Hours/w', value=round(hpw), delta=round(count_married/hpw)/8)

        figCol1,figCol2 = st.columns(2)
        with figCol1:
            st.markdown('### Age vs Marital Status')
            fig = px.density_heatmap(data_frame=df,y='new_age',x='marital-status').update_layout(yaxis_title='Age',xaxis_title='Married')

            st.write(fig)
        with figCol2:
            st.markdown('### Age Count')
            fig2 = px.histogram(data_frame=df,x='new_age').update_layout(xaxis_title='Age')
            st.write(fig2)
        st.markdown('### Data View As Per Selection')
        st.dataframe(df)
        time.sleep(1)