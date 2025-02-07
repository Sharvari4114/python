import numpy as np
import pandas as pd
import streamlit as st

st.title("Welcome everyone to learn python")
st.write("Python requires practice")
data=pd.DataFrame({'c1':[10,20,30,40],'c2':['A','B','C','D']})

st.write("Below is the table for data")
st.write(data)

chart_data=pd.DataFrame(np.random.randn(20,3),columns=["A","B","c"])
st.line_chart(chart_data)

st.bar_chart(chart_data)