
import pickle
import streamlit as st
import os
from streamlit_option_menu import option_menu

# Set Streamlit page configuration
st.set_page_config(page_title='Prediction of Disease Outbreaks', layout='wide')

# Load the trained model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))

# Sidebar Menu
with st.sidebar:
    selected = option_menu(
        "Disease Outbreak Prediction System",
        ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
        menu_icon='hospital-fill',
        icons=['activity', 'heart', 'person'],
        default_index=0
    )

# Diabetes Prediction
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction Using ML')

    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies', '')
    with col2:
        Glucose = st.text_input('Glucose Level', '')
    with col3:
        BloodPressure = st.text_input('Blood Pressure', '')
    with col1:
        SkinThickness = st.text_input('Skin Thickness', '')
    with col2:
        Insulin = st.text_input('Insulin Level', '')
    with col3:
        BMI = st.text_input('BMI', '')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function', '')
    with col2:
        Age = st.text_input('Age', '')

    if st.button('Diabetes Test Result'):
        if not all([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]):
            st.warning("Please fill in all fields before proceeding.")
        else:
            try:
                user_input = list(map(lambda x: float(x) if x else 0.0, 
                                    [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]))
                prediction = diabetes_model.predict([user_input])
                st.success('The person is diabetic.' if prediction[0] == 1 else 'The person is not diabetic.')
            except ValueError:
                st.error("Please enter valid numerical values.")
    # else:
    #     st.error("Diabetes prediction model is not available.")

# Heart Disease Prediction
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction Using ML')

    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input('Age', '')
    with col2:
        sex = st.text_input('Sex (0 = Female, 1 = Male)', '')
    with col3:
        cp = st.text_input('Chest Pain Type', '')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure', '')
    with col2:
        chol = st.text_input('Cholesterol Level', '')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar (1=True, 0=False)', '')
    with col1:
        restecg = st.text_input('Resting ECG Results', '')
    with col2:
        thalach = st.text_input('Max Heart Rate Achieved', '')
    with col3:
        exang = st.text_input('Exercise-Induced Angina (1=Yes, 0=No)', '')
    with col1:
        oldpeak = st.text_input('ST Depression Induced by Exercise', '')
    with col2:
        slope = st.text_input('Slope of Peak Exercise ST Segment', '')
    with col3:
        ca = st.text_input('Major Vessels Colored by Fluoroscopy', '')
    with col1:
        thal = st.text_input('Thalassemia (0-3)', '')

    if st.button('Heart Disease Test Result'):
        if not all([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]):
            st.warning("Please fill in all fields before proceeding.")
        else:
            try:
                user_input = list(map(lambda x: float(x) if x else 0.0, 
                                    [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]))
                prediction = heart_disease_model.predict([user_input])
                st.success('The person has heart disease.' if prediction[0] == 1 else 'The person does not have heart disease.')
            except ValueError:
                st.error("Please enter valid numerical values.")
    # else:
    #     st.error("heart disease prediction model is not available.")

# Parkinson’s Prediction
#MDVP:Fo(Hz),MDVP:Fhi(Hz),MDVP:Flo(Hz),MDVP:Jitter(%),MDVP:Jitter(Abs),MDVP:RAP,MDVP:PPQ,Jitter:DDP,MDVP:Shimmer,MDVP:Shimmer(dB),Shimmer:APQ3,Shimmer:APQ5,MDVP:APQ,Shimmer:DDA,NHR,HNR,status,RPDE,DFA,spread1,spread2,D2,PPE

if selected == 'Parkinsons Prediction':
    st.title('Parkinsons Prediction Using ML')

    col1, col2, col3 = st.columns(3)
    with col1:
        MDVP_Fo_Hz = st.text_input('MDVP:Fo(Hz)', '')
    with col2:
        MDVP_Fhi_Hz = st.text_input('MDVP:Fhi(Hz)', '')
    with col3:
        MDVP_Flo_Hz = st.text_input('MDVP:Flo(Hz)', '')
    with col1:
        MDVP_Jitter_percent = st.text_input('MDVP:Jitter(%)', '')
    with col2:
        MDVP_Jitter_Abs = st.text_input('MDVP:Jitter(Abs)', '')
    with col3:
        MDVP_RAP = st.text_input('MDVP:RAP', '')
    with col1:
        MDVP_PPQ = st.text_input('MDVP:PPQ', '')
    with col2:
        Jitter_DDP = st.text_input('Jitter:DDP', '')
    with col3:
        MDVP_Shimmer = st.text_input('MDVP:Shimmer', '')
    with col1:
        MDVP_Shimmer_dB = st.text_input('MDVP:Shimmer(dB)', '')
    with col2:
        Shimmer_APQ3 = st.text_input('Shimmer:APQ3', '')
    with col3:
        Shimmer_APQ5 = st.text_input('Shimmer:APQ5', '')
    with col1:
        MDVP_APQ = st.text_input('MDVP:APQ', '')
    with col2:
        Shimmer_DDA = st.text_input('Shimmer:DDA', '')
    with col3:
        NHR = st.text_input('NHR', '')
    with col1:
        HNR = st.text_input('HNR', '')
    with col2:
        RPDE = st.text_input('RPDE', '')
    with col3:
        DFA = st.text_input('DFA', '')
    with col1:
        spread1 = st.text_input('spread1', '')
    with col2:
        spread2 = st.text_input('spread2', '')
    with col3:
        D2 = st.text_input('D2', '')
    with col1:
        PPE = st.text_input('PPE', '')

    if st.button('Parkinsons Prediction Test Result'):
        if parkinsons_disease_model:
            if not all([MDVP_Fo_Hz, MDVP_Fhi_Hz, MDVP_Flo_Hz, MDVP_Jitter_percent, MDVP_Jitter_Abs, MDVP_RAP, MDVP_PPQ, 
                        Jitter_DDP, MDVP_Shimmer, MDVP_Shimmer_dB, Shimmer_APQ3, Shimmer_APQ5, MDVP_APQ, Shimmer_DDA, 
                        NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]):
                st.warning("Please fill in all fields before proceeding.")
            else:
                try:
                    user_input = list(map(lambda x: float(x) if x else 0.0, 
                                        [MDVP_Fo_Hz, MDVP_Fhi_Hz, MDVP_Flo_Hz, MDVP_Jitter_percent, 
                                        MDVP_Jitter_Abs, MDVP_RAP, MDVP_PPQ, Jitter_DDP, 
                                        MDVP_Shimmer, MDVP_Shimmer_dB, Shimmer_APQ3, Shimmer_APQ5, 
                                        MDVP_APQ, Shimmer_DDA, NHR, HNR, RPDE, DFA, 
                                        spread1, spread2, D2, PPE]))
                    prediction = parkinsons_disease_model.predict([user_input])
                    st.success('The person has Parkinsons disease.' if prediction[0] == 1 else 'The person does not have Parkinsons disease.')
                except ValueError:
                    st.error("Please enter valid numerical values.")
        # else:
        #     st.error("Parkinsons disease prediction model is not available.")
