
import pickle
import streamlit as st
import pandas as pd

# loading the saved model
loaded_model, loaded_scaler = pickle.load(open('C:/Users/sonug/Desktop/22136_Practicum/heartguard.sav', 'rb'))

# creatimg a function for taking input

def prediction(input_data):
        
    user_df = pd.DataFrame([input_data])
    user_df_scaled = loaded_scaler.fit_transform(user_df)
    prediction = loaded_model.predict(user_df_scaled)

    if prediction[0] == 1:
        return "You are predicted to have heart disease."
    else:
        return "You are predicted not to have heart disease."
    
    
def main():
    
    # giving a title to our web app
    st.title('HeartGuard')
    
    # getting the input from the user
    age = st.text_input('Age of the person')
    sex = st.text_input('Gender of the person(0-Female, 1-Male)')
    Cp = st.text_input('Chest Pain Level(0-3)')
    trestbps = st.text_input('syslotic Blood Pressure of the person')
    chol = st.text_input('Cholestrol Level')
    fbs = st.text_input('Fasting Blood Sugar Level(0- <120 , 1- >120')
    restecg = st.text_input('restecg Leevel')
    thalach = st.text_input('Thalach level')
    exang = st.text_input('Exang Level')
    oldpeak = st.text_input('Oldpeak Level')
    slope = st.text_input('Slope of the ecg')
    ca = st.text_input('CAA value')
    thal = st.text_input('Thal value')
    
    
    # Code for Prediction
    diagnosis = ""
        
    # Creating a Button
    if st.button('Predict the Result'):
        diagnosis = prediction([age, sex, Cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal])
        
    st.success(diagnosis)
    
if __name__ == '__main__':
    main()
        
        
        
        
        
        
        
        
        
        
        
        
        
        