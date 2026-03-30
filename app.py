import os
import pickle
import streamlit as st
import numpy as np
from streamlit_option_menu import option_menu
# Function to set background image
import base64
# Importing database functions
from database import init_db, save_prediction 

#recomendation function to provide lifestyle recommendations based on risk level
def get_recommendations(disease, risk_level):
     if disease == "Diabetes":

        if risk_level == "High":
            return [
                "Consult a physician immediately",
                "Reduce sugar and carbohydrate intake",
                "Exercise at least 30 minutes daily",
                "Monitor blood glucose regularly"
            ]

        elif risk_level == "Medium":
            return [
                "Maintain a balanced diet",
                "Increase physical activity",
                "Monitor blood sugar periodically"
            ]

        else:
            return [
                "Maintain healthy lifestyle",
                "Regular health checkups",
                "Continue balanced nutrition"
            ]

     elif disease == "Heart Disease":

        if risk_level == "High":
            return [
                "Seek cardiologist consultation",
                "Reduce salt and fatty foods",
                "Avoid smoking and alcohol",
                "Monitor blood pressure regularly"
            ]

        elif risk_level == "Medium":
            return [
                "Adopt heart-healthy diet",
                "Exercise regularly",
                "Manage stress levels"
            ]

        else:
            return [
                "Maintain healthy weight",
                "Regular cardiovascular exercise",
                "Annual heart screening"
            ]

     elif disease == "Parkinsons":

        if risk_level == "High":
            return [
                "Consult neurologist",
                "Start physiotherapy exercises",
                "Maintain medication schedule",
                "Ensure fall safety measures"
            ]

        elif risk_level == "Medium":
            return [
                "Practice balance exercises",
                "Maintain regular sleep routine",
                "Monitor motor symptoms"
            ]

        else:
            return [
                "Stay physically active",
                "Maintain healthy diet",
                "Routine neurological checkups"
            ]

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(image_file):
    bin_str = get_base64(image_file)
    page_bg_img = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

working_dir = os.path.dirname(os.path.abspath(__file__))

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

# Initialize the database
init_db()


if "page" not in st.session_state:
    st.session_state.page = "landing"

if st.session_state.page == "landing":
    # st.title("🧠 Welcome to Health Assistant")
    # st.markdown("""
    #     This app helps clinicians predict Diabetes, Heart Disease, and Parkinson’s using machine learning.
    #     Please proceed to enter patient data and get diagnostic insights.
    # """)
    
    set_background(f'{working_dir}/images/landingimg.png')

    st.markdown("""
    <style>
    @media (max-width: 480px){ .landing-spacer{height:65vh;} }
    @media (min-width: 481px) and (max-width: 1024px){ .landing-spacer{height:45vh;} }
    @media (min-width: 1025px){ .landing-spacer{height:28vh;} }
    /* make button more visible on image */
    .stButton>button {
        background-color: rgba(255,255,255,0.9) !important;
        color: #000 !important;
        border-radius: 8px;
        padding: 8px 18px;
    }
    </style>
    <div class="landing-spacer"></div>
    """, unsafe_allow_html=True)  # landing page adjusted for mobile view

    if st.button("Next"):
        st.session_state.page = "predict"

    st.stop()

elif st.session_state.page == "predict":
    
    
    # getting the working directory of the main.py

    # loading the saved models

    diabetes_model = pickle.load(open(f'{working_dir}/saved_models/diabetes_model.sav', 'rb'))

    heart_disease_model = pickle.load(open(f'{working_dir}/saved_models/heart_disease_model.sav', 'rb'))

    parkinsons_model = pickle.load(open(f'{working_dir}/saved_models/parkinsons_model.sav', 'rb'))

    # sidebar for navigation
    with st.sidebar:
        selected = option_menu('Multiple Disease Prediction System',

                            ['Diabetes Prediction',
                                'Heart Disease Prediction',
                                'Parkinsons Prediction'],
                            menu_icon='hospital-fill',
                            icons=['activity', 'heart', 'person'],
                            default_index=0)


    # Diabetes Prediction Page
    if selected == 'Diabetes Prediction':

        # page title
        st.title('Diabetes Prediction using ML')
        set_background(f'{working_dir}/images/diabetesimg.png')
        #patient information
        st.subheader("Patient Information")
        patient_name = st.text_input("Patient Name",key="diabetes_patient_name")
        # getting the input data from the user
        col1, col2, col3 = st.columns(3)

        with col1:
            Pregnancies = st.text_input('Number of Pregnancies')

        with col2:
            Glucose = st.text_input('Glucose Level')

        with col3:
            BloodPressure = st.text_input('Blood Pressure value')

        with col1:
            SkinThickness = st.text_input('Skin Thickness value')

        with col2:
            Insulin = st.text_input('Insulin Level')

        with col3:
            BMI = st.text_input('BMI value')

        with col1:
            DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

        with col2:
            Age = st.text_input('Age of the Person')


        # code for Prediction
        diab_diagnosis = ''

        # creating a button for Prediction

        if st.button('Diabetes Test Result'):

            user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                        BMI, DiabetesPedigreeFunction, Age]

            user_input = [float(x) for x in user_input]

            diab_prediction = diabetes_model.predict([user_input])
            #get probability of prediction
            diab_prediction_proba = diabetes_model.decision_function([user_input])
            risk_percentage = 1 / (1 + np.exp(-diab_prediction_proba[0])) * 100  # Convert to percentage using sigmoid function

            #determine risk level based on probability
            if risk_percentage < 40:
                risk_level = 'Low'
            elif risk_percentage < 70:
                risk_level = 'Medium'
            else:
                risk_level = 'High'

#diagnosis message with risk percentage and level       

            if diab_prediction[0] == 1:
                diab_diagnosis = 'The person is diabetic'
            else:
                diab_diagnosis = 'The person is not diabetic'

            st.success(diab_diagnosis)
            #show risk information  
            st.info(f'Risk Percentage: {risk_percentage:.2f}%')
            st.warning(f'Risk Level: {risk_level}')
 #save prediction result to database
            save_prediction(patient_name, "Diabetes", diab_diagnosis, risk_percentage, risk_level)
#get recommendations based on risk level
            recommendations = get_recommendations("Diabetes", risk_level)
            st.subheader("Recommendations")
            for rec in recommendations:
                st.write(f"- {rec}")



    # Heart Disease Prediction Page
    if selected == 'Heart Disease Prediction':

        # page title
        st.title('Heart Disease Prediction using ML')
        set_background(f'{working_dir}/images/heartimg.png')

        # patient information
        st.subheader("Patient Information")
        patient_name = st.text_input("Patient Name", key="heart_patient_name")

        col1, col2, col3 = st.columns(3)

        with col1:
            age = st.text_input('Age')

        with col2:
            sex = st.text_input('Sex')

        with col3:
            cp = st.text_input('Chest Pain types')

        with col1:
            trestbps = st.text_input('Resting Blood Pressure')

        with col2:
            chol = st.text_input('Serum Cholestoral in mg/dl')

        with col3:
            fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

        with col1:
            restecg = st.text_input('Resting Electrocardiographic results')

        with col2:
            thalach = st.text_input('Maximum Heart Rate achieved')

        with col3:
            exang = st.text_input('Exercise Induced Angina')

        with col1:
            oldpeak = st.text_input('ST depression induced by exercise')

        with col2:
            slope = st.text_input('Slope of the peak exercise ST segment')

        with col3:
            ca = st.text_input('Major vessels colored by flourosopy')

        with col1:
            thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

        # code for Prediction
        heart_diagnosis = ''

        # creating a button for Prediction

        if st.button('Heart Disease Test Result'):

            user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

            user_input = [float(x) for x in user_input]

            heart_prediction = heart_disease_model.predict([user_input])
            #get probability of prediction
            heart_prediction_proba = heart_disease_model.predict_proba([user_input])
            risk_percentage = heart_prediction_proba[0][1] * 100

            #determine risk level based on probability
            if risk_percentage < 40:
                risk_level = 'Low'
            elif risk_percentage < 70:
                risk_level = 'Medium'
            else:
                risk_level = 'High'
#diagnosis message with risk percentage and level
            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person is having heart disease'
            else:
                heart_diagnosis = 'The person does not have any heart disease'

            st.success(heart_diagnosis)
#show risk information
            st.info(f'Risk Percentage: {risk_percentage:.2f}%') 
            st.warning(f'Risk Level: {risk_level}')
#save prediction result to database
            save_prediction(patient_name, "Heart Disease", heart_diagnosis, risk_percentage, risk_level)
#get recommendations based on risk level
            recommendations = get_recommendations("Heart Disease", risk_level)
            st.subheader("Recommendations")
            for rec in recommendations:
                st.write(f"- {rec}")


    # Parkinson's Prediction Page
    if selected == "Parkinsons Prediction":

        # page title
        st.title("Parkinson's Disease Prediction using ML")
        set_background(f'{working_dir}/images/parkinsonimg.png')
        # patient information
        st.subheader("Patient Information")
        patient_name = st.text_input("Patient Name", key="parkinsons_patient_name")

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            fo = st.text_input('MDVP:Fo(Hz)')

        with col2:
            fhi = st.text_input('MDVP:Fhi(Hz)')

        with col3:
            flo = st.text_input('MDVP:Flo(Hz)')

        with col4:
            Jitter_percent = st.text_input('MDVP:Jitter(%)')

        with col5:
            Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

        with col1:
            RAP = st.text_input('MDVP:RAP')

        with col2:
            PPQ = st.text_input('MDVP:PPQ')

        with col3:
            DDP = st.text_input('Jitter:DDP')

        with col4:
            Shimmer = st.text_input('MDVP:Shimmer')

        with col5:
            Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

        with col1:
            APQ3 = st.text_input('Shimmer:APQ3')

        with col2:
            APQ5 = st.text_input('Shimmer:APQ5')

        with col3:
            APQ = st.text_input('MDVP:APQ')

        with col4:
            DDA = st.text_input('Shimmer:DDA')

        with col5:
            NHR = st.text_input('NHR')

        with col1:
            HNR = st.text_input('HNR')

        with col2:
            RPDE = st.text_input('RPDE')

        with col3:
            DFA = st.text_input('DFA')

        with col4:
            spread1 = st.text_input('spread1')

        with col5:
            spread2 = st.text_input('spread2')

        with col1:
            D2 = st.text_input('D2')

        with col2:
            PPE = st.text_input('PPE')

        # code for Prediction
        parkinsons_diagnosis = ''

        # creating a button for Prediction    
        if st.button("Parkinson's Test Result"):

            user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                        RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                        APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

            user_input = [float(x) for x in user_input]

            parkinsons_prediction = parkinsons_model.predict([user_input])
            #get probability of prediction
            parkinsons_prediction_proba = parkinsons_model.decision_function([user_input])
            risk_percentage = 1 / (1 + np.exp(-parkinsons_prediction_proba[0])) * 100  # Convert to percentage using sigmoid function

            #determine risk level based on probability
            if risk_percentage < 40:
                risk_level = 'Low'
            elif risk_percentage < 70:
                risk_level = 'Medium'
            else:
                risk_level = 'High'
 #diagnosis message with risk percentage and level
            if parkinsons_prediction[0] == 1:
                parkinsons_diagnosis = "The person has Parkinson's disease"
            else:
                parkinsons_diagnosis = "The person does not have Parkinson's disease"

            st.success(parkinsons_diagnosis)
#show risk information  
            st.info(f'Risk Percentage: {risk_percentage:.2f}%')
            st.warning(f'Risk Level: {risk_level}')
#save prediction result to database
            save_prediction(patient_name, "Parkinsons", parkinsons_diagnosis, risk_percentage, risk_level)
#get recommendations based on risk level
            recommendations = get_recommendations("Parkinsons", risk_level)
            st.subheader("Recommendations")
            for rec in recommendations:
                st.write(f"- {rec}")

    st.markdown("""
        <hr style='margin-top: 50px;'>
        <div style='text-align: center; font-size: 14px; color: white;'>
            Built by Subhankar | Powered by Streamlit & Machine Learning<br>
            © 2025 Health Assistant App
        </div>
    """, unsafe_allow_html=True)
