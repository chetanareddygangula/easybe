#from numpy import full
import streamlit as st
import plotly_express as px
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from streamlit_option_menu import option_menu

st.set_page_config(page_title='EasyBe-Analysis',page_icon="https://cdn3.vectorstock.com/i/thumb-large/93/97/analytics-growth-circle-icon-vector-27719397.jpg")

# configuration
st.set_option('deprecation.showfileUploaderEncoding', False)

# title of the app

uploaded_file = st.file_uploader(
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

# 1. as sidebar menu
with st.sidebar:
    selected2 = option_menu("Main Menu", ["Home","Analysis","Visualize", 'Settings'],
        icons=['house', "upload","list-task","phone",'gear'], menu_icon="cast", default_index=1)


if selected2=="Home":
    #st.title("EasyBe")
    image="logo.png"

    #st.image(image, width=200)
    #si=st.write('<p style="font-family:Math;font-weight: bold;text-transform:uppercase; color:#DC143C; font-size: 80px;">EasyBe</p>',unsafe_allow_html=True)
    #st.write("a logo and text next to eachother")

    st.image(image,width=1000)


if selected2=="Analysis":


            

    #show dataset  
    if st.checkbox("Show dataset"):
        st.write(df)
    #Shape of Our Dataset (Number of Rows And Number of Columns)
    if st.checkbox("Show number of rows and columns "):
        st.warning(f'Rows : {df.shape[0]}')
        st.warning(f'Columns : {df.shape[1]}')
        
     # get the list of columns
    if st.checkbox(" Show dataset with selected columns"):
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
        
        



    if st.checkbox("Show dataset with selected rows"):
        ade = st.selectbox(
            "Select to view ",
            ('Greater than values', 'Less than', 'Equal values'))
        if ade == "Greater than values":
            t = st.selectbox('Select the colum to view ', list(df.columns))
            fn = st.text_input("Enter value to view : ")
            fn = float(fn)
            df1 = df[df[t] > fn]
            st.write(df1)

        if ade == "Less than":
            y = st.selectbox('Select the colum to view ', list(df.columns))
            fn1 = st.text_input("Enter value to view : ")
            fn1 = float(fn1)
            df2 = df[df[y] < fn1]
            st.write(df2)

        if ade == "Equal values":
            z = st.selectbox('Select the colum to view ', list(df.columns))
            fn2 = st.text_input("Enter value to view : ")
            fn2 = float(fn2)
            df3 = df[df[z] == fn2]
            st.write(df3)
            
    #null values    
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
                df=df.dropna(inplace=True)
                st.write("Null Values are Removed")  
                if st.checkbox("View dataset"):
                    st.write(df)  
            if dup=="No":
                st.write("Ok No Problem!!!")
            if dup=="Replace Values":
                a=st.text_input("Enter the value to be replaced");
                df=df.fillna(a)
                if st.checkbox("View dataset"):
                    st.write(df)
                
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
                df=df.drop_duplicates(inplace=True)
                st.text("Duplicate Values are Removed")
            if dup=="No":
                st.text("Ok No Problem")
        else:
            st.warning("No Duplicate values...")
            #add rows
    #if st.checkbox("Add row"):
     #   x = st.selectbox('Select the colum to add a row',list(df.columns))
      #  y=st.text_input("Enter the value to add")
       # df4=df.append({x:y},ignore_index=True)
        #df4=float(df4)
        #st.write(df4)
        
     # 8. Get Overall Statistics

    if st.checkbox("Summary of The Dataset"):
        st.write(df.describe(include='all'))
        
if selected2=="Visualize":
    



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
        #st.subheader("Boxplot Settings")
        try:
            y = st.selectbox("Y axis", options=list(df.columns))
            x = st.selectbox("X axis", options=list(df.columns))
        #color_value = st.sidebar.selectbox("Color", options=non_numeric_columns)
            plot = px.box(data_frame=df, y=y, x=x)
            st.plotly_chart(plot)
        except Exception as e:
            print(e)
        
