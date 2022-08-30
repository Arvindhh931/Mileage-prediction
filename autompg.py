import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import base64
import pickle
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

import os
# from deta import Deta
# from dotenv import load_dotenv
# from datetime import datetime

# load_dotenv(".env")

# DETA_KEY = os.getenv("DETA_KEY")

st.set_page_config(page_title='Car Mileage prediction',page_icon="")
st.header("Fuel Efficiency in miles per gallon")

selected = option_menu(menu_title=None,options=["Mileage Prediction","Project","Information"],
icons=["house","book","envelope"],menu_icon="cast",default_index=0,
orientation='horizontal',
styles={
            "container": {"padding": "0!important", "background-color": "#000"},
            "icon": {"color": "orange", "font-size": "20px"}, 
            "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#000"},
            "nav-link-selected": {"background-color": "green"},
            "position": 
        })
if selected == "Prediction":
    st.markdown("### Prediction of Fuel efficiency in Miles per gallon")
    st.markdown("#### Please enter the details") 
    
    def numeric():
        hp = st.numer_input('Horsepower',40,170,None,key='horsepower')
        wt = st.numer_input('weight in pounds',0,10000,None,key='weight')
        acc = st.numer_input('Acceleration (No seconds to reach 60mph speed)',0,50,None,key='acceleration')
        return hp,wt,acc
    
    horsepower,weight,acceleration = numeric()
    
    def category():
        col1,col2,col3 = st.columns(3)
        with col1:
            value1 = st.selectbox('Number of cylinders',('3', '4', '5', '6', '8'),key='cylinder')
        with col2:
            value2 = st.selectbox('Car model year',('1971','1972','1973','1974','1975',                                              '1976','1977','1978','1979','1980','1981','1982'),key='model_year')
        with col3:
            value3 = st.selectbox('Region',('USA', 'Europe', 'Asia'),key='Region')
        return value1,value2,value3
    
    cylinder,model_year,origin = category()
    
    # Exception
    
    if None in horsepower,weight,acceleration:
        for i in horsepower,weight,acceleration:
        st.write("please enter all the values horsepower,weight & Acceleration")
        horsepower,weight,acceleration = numeric()
    if None in cylinder,model_year,origin:
        st.write("please enter all the values No of cylinders, & Acceleration")
        cylinder,model_year,origin = category()
        
    with open('./serialization/category_encoder.pickle','rb') as f1:
        encoder = pickle.load(f1)
    with open('./serialization/final_model.pickle','rb') as f2:
        model = pickle.load(f2)
      
    # processing query point
    
    category_encoding = encoder.transform([[cylinder,model_year,origin]]).flatten()
    category_coded = pd.Series(category_encoding)
    
    values = list(numeric())+list(category())
    
    # Encoding & storing the query point for prediction ready format
    numerical_data = pd.Series(numeric())
    query = pd.concat([numerical_data,category_coded],axis=0).to_frame().T
    
    confirm = st.button("Submit")
    if confirm:
        # getting project key from .env file
        # db_class = Deta(DETA_KEY)
        # database = db_class.base('Autompg')
        
        # Prediction
        prediction = MLR_regression.predict(query)[0][0]
        
        col = ['horsepower','weight','acceleration','cylinder','model_year','country/origin','mpg_predicted']
        values = values.apped(prediction)
        final_data = dict(col,values)
        
        # Storing the results in Database
        # database.put(final_data,key=str(datetime.now()))
        st.success(f"Car mileage is {round(prediction,0)} miles per gallon")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)







