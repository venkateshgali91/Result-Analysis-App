import pandas as pd
import streamlit as st
#from streamlit_pandas_profiling import st_profile_report
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sweetviz as sv
import streamlit.components.v1 as components
import codecs
from sklearn.datasets import load_boston

st.set_page_config(page_title='Exploratory data analysis app',layout='wide')
m = st.markdown("""
<style>
div.stButton > button:first-child {

     background-color: white;
     color: black;
     border: 2px solid #4CAF50; /* Green */
    
}
div.stButton > button:hover {
     background-color: #4CAF50; /* Green */
     color: white;
}

[theme]
base="light"
primaryColor="#7d7878"
backgroundColor="#e0dddf"
secondaryBackgroundColor="#d2d0d1"
</style>""", unsafe_allow_html=True)
data = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
st.sidebar.markdown("""
[Example CSV input file](https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv)
""")
if data is not None:
    data = pd.read_csv(data)
    st.markdown('**1.1. Glimpse of dataset**')
    st.write(data)
    st.write('Numeric Columns :')
    numerics = ['int16', 'int32', 'int64']
    df = data.select_dtypes(include=numerics)
    st.info(df.columns)
    df1 = data.select_dtypes(exclude=["number","bool_","object_"])
    st.write('Categorical columns :')
    st.info(df1.columns)

else:

    boston = load_boston()
    data = pd.DataFrame(boston.data)
    data.columns = boston.feature_names

    st.markdown('The Boston housing dataset is used as the example.')
    st.write(data.head(5))
if st.button('Show Statistics'):
    st.write('The statisitical analysis of your data is shown below')
    st.write(data.describe().style.background_gradient(cmap='pink_r'))
if st.button('Visualize'):
    st.write('Data Visualization!')
    df1=data['Branch'].tolist()
    dfr=data['ROLL NUMBER'].tolist()
    dfs=[]
    for j in range(0,10):
        dfs.append(dfr[j])
    df2=[]
    for i in range (0,10):
        df2.append(df1[i])
    dff=dfs+df2
    st.line_chart(dff)