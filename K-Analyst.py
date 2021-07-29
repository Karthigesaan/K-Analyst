import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np



#title of the app

st.title("**DATA VISUALIZATION APP**")

# Add a sidebar

st.sidebar.subheader("**Visualization Setting**")

# Setup file upload

uploaded_file = st.sidebar.file_uploader(label="Upload File.csv/xlsx. (200MB max)",
                         type=['csv','xlsx'])

global df
if uploaded_file is not None:
  print("hello")
  try:
    df = pd.read_csv(uploaded_file)
  except Exception as e:
    print(e)
    df = pd.read_excel(uploaded_file)

global numeric_columns
try:
  st.write(df)
  numeric_columns = list(df.select_dtypes(['float','int','object']).columns)
except Exception as e:
  print(e)
  st.write("Please upload a file to begin")

#add a select widget to the sidebar

chart_selection = st.sidebar.selectbox(
    label = "Select the chart type",
    options = ["Scatterplots", "Lineplots", "Histogram"]
)


if chart_selection == 'Scatterplots':
  st.sidebar.subheader("Scatterplots Settings")
  try:
    x_values = st.sidebar.selectbox('X axis', options = numeric_columns)
    y_values = st.sidebar.selectbox('Y axis', options = numeric_columns)
    plot = px.scatter(data_frame=df, x= x_values, y=y_values)
    # display the chart
    st.plotly_chart(plot)
  except Exception as e:
    print(e)

elif chart_selection == 'Lineplots':
  st.sidebar.subheader("Lineplots")
  try:
    x_values = st.sidebar.selectbox('X axis', options = numeric_columns)
    y_values = st.sidebar.selectbox('Y axis', options = numeric_columns)
    plot = px.line(data_frame=df, x= x_values, y=y_values)
    # display the chart
    st.plotly_chart(plot)
  except Exception as e:
    print(e)

else:
  st.sidebar.subheader("Histogram")
  try:
    x_values = st.sidebar.selectbox('X axis', options = numeric_columns)
    y_values = st.sidebar.selectbox('Y axis', options = numeric_columns)
    plot = px.histogram(data_frame=df, x= x_values, y=y_values)
    # display the chart
    st.plotly_chart(plot)
  except Exception as e:
    print(e)