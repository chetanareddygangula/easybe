
from numpy import full
import streamlit as st
import plotly_express as px
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


st.set_page_config(page_title='EasyBe-Analysis',page_icon="https://png.pngtree.com/png-clipart/20210302/ourmid/pngtree-statistics-clip-art-rainbow-gradient-chart-png-image_2986825.jpg")

# configuration
st.set_option('deprecation.showfileUploaderEncoding', False)

# title of the app
original_title = '<p style="font-family:Math;text-align:center;font-weight: bold;text-transform:uppercase; color:#DC143C; font-size: 30px;background-color:#FFF8DC;">EasyBe</p>'
st.markdown(original_title, unsafe_allow_html=True)
# Add a sidebar
st.sidebar.subheader("Visualization Settings")

# Setup file upload
uploaded_file = st.sidebar.file_uploader(
                        label="Upload your CSV or Excel file. (200MB max)",
                         type=['csv', 'xlsx'])

global df
if uploaded_file is not None:
    print(uploaded_file)
    print("hello")

    try:
        df = pd.read_csv(uploaded_file)
    except Exception as e:
        print(e)
        df = pd.read_excel(uploaded_file)
#show dataset  
if st.checkbox("Show dataset"):
    st.write(df)

#Shape of Our Dataset (Number of Rows And Number of Columns)

if st.checkbox("Show number of rows and columns "):
    st.warning(f'Rows : {df.shape[0]}')
    st.warning(f'Columns : {df.shape[1]}')
    

#if st.checkbox("Show Dataset"):
 #   st.write("### Enter the number of rows to view")
  #  rows = st.number_input("", min_value=0,value=3)
   # if rows > 0:
    #    st.dataframe(df.head(rows))
            
if st.checkbox(" Show dataset with selected columns"):
    # get the list of columns
    columns = df.columns.tolist()
    st.write("#### Select the columns to display:")
    st.write("For ascending or decending order of column , click on the column name...")
    selected_cols = st.multiselect("", columns)
    if len(selected_cols) > 0:
        selected_df = df[selected_cols]
        st.dataframe(selected_df)
            
 #Show datatype

if st.checkbox("DataType of Each Column"):
    st.text("DataTypes")
    st.write(df.dtypes)
        
#Shape of Our Dataset (Number of Rows And Number of Columns)

#if st.checkbox("Show number of rows and columns "):
 #   st.warning(f'Rows : {df.shape[0]}')
  #  st.warning(f'Columns : {df.shape[1]}')
    
#Null values
#unique values


if uploaded_file is not None:
    test=df.isnull().values.any()
    
    if st.checkbox("Null Values in the dataset"):
        if test==True:
            st.write(df.isnull().any())
            sns.heatmap(df.isnull())
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot()
            dup=st.selectbox("Do You Want to Remove Null Values?", \
                     ("Select One","Yes","No","Replace Values"))
            if dup=="Yes":
                df=df.dropna()
                st.write("Null Values are Removed")    
            if dup=="No":
                st.write("Ok No Problem!!!")
        else:
            st.warning("No null values...")
            

        
        
if uploaded_file is not None:
    test1=df.duplicated().any()
    if st.checkbox("Duplicates in the dataset"):
        if test1==True:
            st.warning("This Dataset Contains Some Duplicate Values")
            dup=st.selectbox("Do You Want to Remove Duplicate Values?", \
                         ("Select One","Yes","No"))
            if dup=="Yes":
                df=df.drop_duplicates()
                st.text("Duplicate Values are Removed")
            if dup=="No":
                st.text("Ok No Problem")
        else:
            st.warning("No Duplicate values...")

   


    # 8. Get Overall Statistics

if st.checkbox("Summary of The Dataset"):
    st.write(df.describe(include='all'))
  #add rows  




# add a select widget to the side bar
st.write("### Visualize Dataset")
#st.checkbox("Visualize plots")
#chart_select = st.selectbox(label="select the chart type",
 #                           options=['Scatterplots', 'Lineplots', 'Histogram', 'Boxplot']
#)
if st.checkbox("Scatterplot"):
    
    st.subheader("Scatterplot Settings")
    try:
        x_values = st.selectbox('X axis',list(df.columns))
        y_values = st.selectbox('Y axis', list(df.columns))
        #color_value = st.sidebar.selectbox("Color", options=non_numeric_columns)
        plot = px.scatter(data_frame=df, x=x_values, y=y_values)
        # display the chart
        st.plotly_chart(plot)
    except Exception as e:
        print(e)

if st.checkbox("Line Plot"):
    st.subheader("Line Plot Settings")
    try:
        x_values = st.selectbox('X axis',list(df.columns))
        y_values = st.selectbox('Y axis', list(df.columns))
        #color_value = st.sidebar.selectbox("Color", options=non_numeric_columns)
        plot = px.line(data_frame=df, x=x_values, y=y_values)
        st.plotly_chart(plot)
    except Exception as e:
        print(e)

if st.checkbox("Histogram"):
    st.subheader("Histogram Settings")
    try:
        x = st.selectbox('Feature', options=list(df.columns))
        bin_size = st.slider("Number of Bins", min_value=10,
                                     max_value=100, value=40)
        #color_value = st.sidebar.selectbox("Color", options=non_numeric_columns)
        plot = px.histogram(x=x, data_frame=df)
        st.plotly_chart(plot)
    except Exception as e:
        print(e)

if st.checkbox("Box Plot"):
    st.subheader("Boxplot Settings")
    try:
        y = st.selectbox("Y axis", options=list(df.columns))
        x = st.selectbox("X axis", options=list(df.columns))
        #color_value = st.sidebar.selectbox("Color", options=non_numeric_columns)
        plot = px.box(data_frame=df, y=y, x=x)
        st.plotly_chart(plot)
    except Exception as e:
        print(e)
        