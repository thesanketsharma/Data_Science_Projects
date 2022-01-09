#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import numpy as np
import pickle
import streamlit as st
from PIL import Image


path = 'PKL/classifier.pkl'
classifier = pickle.load(open(path, 'rb'))


def predict_wine_quality(fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide,density,pH,sulphates,alcohol):

    prediction=classifier.predict([[fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,
                         free_sulfur_dioxide,total_sulfur_dioxide,density,pH,sulphates,alcohol]])
    if prediction==0:
        return "Your Wine is of Poor Quality"
    elif prediction==1:
        return "Your Wine is of Average Quality"
    else:
        return "Your wine is of Good Quality"
    
    
def main():
    st.title("Wine Quality Prediction")
    st.subheader("By: Sanket Sharma, Email: ur.sanketsharma@gmail.com")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Lets Check Your Wine Quality</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    fixed_acidity = st.text_input("fixed_acidity","Type Here")
    volatile_acidity = st.text_input("volatile_acidity","Type Here")
    citric_acid = st.text_input("citric_acid","Type Here")
    residual_sugar = st.text_input("residual_sugar","Type Here")
    chlorides= st.text_input("chlorides","Type Here")
    free_sulfur_dioxide = st.text_input("free_sulfur_dioxide","Type Here")
    total_sulfur_dioxide = st.text_input("total_sulfur_dioxide","Type Here")
    density = st.text_input("density","Type Here")
    pH = st.text_input("pH","Type Here")
    sulphates = st.text_input("sulphates","Type Here")
    alcohol = st.text_input("alcohol","Type Here")
    result="Result"
    if st.button("Predict"):
        result=predict_wine_quality(fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide,density,pH,sulphates,alcohol)
    st.success(result)
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")



if __name__ =='__main__':
    main()






