import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

st.title('talha yedho panra')

st.write("edho oru table")
st.write(pd.DataFrame({
    'pineapple': [1, 2, 3, 4],
    'pizza': [10, 20, 30, 40]
}))

text = "innum oru table using magic"

text

df = pd.DataFrame({
  'car peyar': ["talha", "tesla", "huracan", "namma ooru vandi"],
  'gethu': ["Infinite", 20, 30, 40]
})

df

text2 = "Tact Games"

text2

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['serkinti', 'espazimo', 'varun gaala game'])

st.line_chart(chart_data)

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

if st.checkbox('click pannu man'):
    chart_data = pd.DataFrame(
       np.random.randn(4, 3),
       columns=['onnum ille', 'b', 'c'])

    chart_data

option = st.selectbox(
    'Best Car Company Select pannu',
     df['car peyar'])

'You selected: ', option

option = st.sidebar.selectbox(
    'adhe dhaan but on the left',
     df['car peyar'])

left_column, right_column = st.beta_columns(2)


pressed = left_column.button('idhuvum click panlaam')

if pressed:
    right_column.write("avlo dhaan")

expander = st.sidebar.beta_expander("FAQ")
expander.write("Stream lit semmaya irukku")




