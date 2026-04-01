import os
import pickle
import streamlit as st
import numpy as np
import pandas as pd
from streamlit_option_menu import option_menu
# Function to set background image
import base64
from utils import calculate_risk_percent, determine_risk_level
# Importing database functions
from database import init_db, save_prediction, get_all_records 

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
st.set_page_config(page_title="Health Assistant 2.0",
                   layout="wide",
                   page_icon="🧑‍⚕️")
st.markdown("""
<style>

/* Main background overlay */
.stApp {
    background-color: rgba(0, 0, 0, 0.4) !important;
}

/* Card styling */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Buttons */
.stButton > button {
    border-radius: 10px;
    height: 3em;
    font-size: 16px;
    font-weight: bold;
}

/* Metrics */
[data-testid="stMetric"] {
    background-color: rgba(255,255,255,0.09);
    padding: 15px;
    border-radius: 12px;
}

/* Dataframes */
.stDataFrame {
    border-radius: 10px;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: rgba(0, 0, 0, 0.5);
}

</style>
""", unsafe_allow_html=True)

# Initialize the database
init_db()


if "page" not in st.session_state:
    st.session_state.page = "landing"

if st.session_state.page == "landing":

    set_background(f'{working_dir}/images/landingimg.png')

    st.markdown("""
<style>

/* Smooth page fade */
.stApp {
    animation: fadeIn 1.2s ease-in-out;
}

/* Push button to bottom of screen */
.landing-bottom {
    position: fixed;
    bottom: 0px;
    margin-bottom: 10px;
    left: 50%;
    transform: translateX(-50%);
    width: auto;
    text-align: center;
}

/* Modern animated button */
.stButton > button {
    background-color: #00c6ff;
    color: black;
    font-size: 20px;
    padding: 12px 30px;
    border-radius: 12px;
    border: none;
    font-weight: bold;
    cursor: pointer;

    /* Strong pulse animation */
    animation: pulse 1.8s infinite;
}

/* Hover effect */
.stButton > button:hover {
    transform: scale(1.1);
}

/* Animations */

@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

@keyframes pulse {
    0% {
        box-shadow: 0 0 0 0 rgba(255,255,255,0.9);
    }
    70% {
        box-shadow: 0 0 0 18px rgba(255,255,255,0);
    }
    100% {
        box-shadow: 0 0 0 0 rgba(255,255,255,0);
    }
}

</style>
""", unsafe_allow_html=True)
    st.markdown('<div class="landing-bottom">', unsafe_allow_html=True)
    if st.button("Next →"):
        st.session_state.page = "predict"
    st.markdown('</div>', unsafe_allow_html=True)
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
                                'Parkinsons Prediction',
                                'Patient History',
                                'Analytics Dashboard',
                                'Batch Prediction'],
                            menu_icon='hospital-fill',
                            icons=['activity', 'heart', 'person', 'clock-history', 'bar-chart-line','upload'],
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

            st.markdown(f"""
<div style="
    background-color: rgba(27, 94, 32, 1);
    padding: 20px;
    border-radius: 12px;
    margin-top: 20px;
">

<h3>Prediction Result</h3>

<b>Patient:</b> {patient_name} <br>
<b>Disease:</b> Diabetes <br>
<b>Result:</b> {diab_diagnosis} <br>
<b>Risk Percentage:</b> {risk_percentage:.2f}% <br>
<b>Risk Level:</b> {risk_level}

</div>
""", unsafe_allow_html=True)
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

            st.markdown(f"""
<div style="
    background-color: rgba(27, 94, 32, 1);
    padding: 20px;
    border-radius: 12px;
    margin-top: 20px;
">

<h3>Prediction Result</h3>

<b>Patient:</b> {patient_name} <br>
<b>Disease:</b> Heart Disease <br>
<b>Result:</b> {heart_diagnosis} <br>
<b>Risk Percentage:</b> {risk_percentage:.2f}% <br>
<b>Risk Level:</b> {risk_level}

</div>
""", unsafe_allow_html=True)
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

            st.markdown(f"""
<div style="
    background-color: rgba(27, 94, 32, 1);
    padding: 20px;
    border-radius: 12px;
    margin-top: 20px;
">

<h3>Prediction Result</h3>

<b>Patient:</b> {patient_name} <br>
<b>Disease:</b> Parkinson's Disease <br>
<b>Result:</b> {parkinsons_diagnosis} <br>
<b>Risk Percentage:</b> {risk_percentage:.2f}% <br>
<b>Risk Level:</b> {risk_level}

</div>
""", unsafe_allow_html=True)
#save prediction result to database
            save_prediction(patient_name, "Parkinsons", parkinsons_diagnosis, risk_percentage, risk_level)
#get recommendations based on risk level
            recommendations = get_recommendations("Parkinsons", risk_level)
            st.subheader("Recommendations")
            for rec in recommendations:
                st.write(f"- {rec}")
    # Patient History Page
    if selected == "Patient History":
        st.title("Patient Prediction History")
        #set_background(f'{working_dir}/images/historyimg.png')
        records = get_all_records()
        #search box
        search_term = st.text_input("Search by Patient Name or Disease")

        if records:
            df = pd.DataFrame(
                records,
                columns=[
                    "Patient ID",
                    "Patient Name",
                    "Disease",
                    "Result",
                    "Risk %",
                    "Risk Level",
                    "Date & Time"
                ]
            )
            df["Date & Time"] = pd.to_datetime(df["Date & Time"]).dt.strftime("%Y-%m-%d %H:%M:%S")
            if search_term:
                df = df[df["Patient Name"].str.contains(search_term, case=False, na=False) | df["Disease"].str.contains(search_term, case=False, na=False)]
            st.dataframe(df, use_container_width=True)
            #download button for history
            csv = df.to_csv(index=False)
            st.download_button(
                label="Download History as CSV",
                data=csv,
                file_name='patient_history.csv',
                mime='text/csv',
            )
        else:
            st.warning("No records found.")
    # Analytics Dashboard Page
    if selected == "Analytics Dashboard":
        st.title("Analytics Dashboard")
        records = get_all_records()

        if records:
            df = pd.DataFrame(
                records,
                columns=[
                    "Patient ID",
                    "Patient Name",
                    "Disease",
                    "Result",
                    "Risk %",
                    "Risk Level",
                    "Date & Time"
                ]
            )

            # Convert datetime
            df["Date & Time"] = pd.to_datetime(df["Date & Time"])

            # -----------------------------
            # Metrics
            # -----------------------------

            total_records = len(df)

            unique_patients = df["Patient Name"].nunique()

            col1, col2 = st.columns(2)

            with col1:
                st.metric("Total Records", total_records)

            with col2:
                st.metric("Unique Patients", unique_patients)

            st.markdown("---")

            # -----------------------------
            # Disease Distribution
            # -----------------------------

            st.subheader("Disease Distribution")

            disease_visits = df["Disease"].value_counts()

            disease_unique = (
                df.groupby("Disease")["Patient Name"]
                .nunique()
            )

            st.write("Visits per Disease")

            st.bar_chart(disease_visits)

            st.write("Unique Patients per Disease")

            st.bar_chart(disease_unique)

            st.markdown("---")

            # -----------------------------
            # Risk Level Distribution
            # -----------------------------

            st.subheader("Risk Level Distribution")

            risk_counts = df["Risk Level"].value_counts()

            st.bar_chart(risk_counts)

            st.markdown("---")

            # -----------------------------
            # Monthly Visits Trend
            # -----------------------------

            st.subheader("Monthly Visits Trend")

            df["Month"] = df["Date & Time"].dt.to_period("M")

            monthly_visits = df.groupby("Month").size()

            monthly_visits.index = monthly_visits.index.astype(str)

            st.line_chart(monthly_visits)
        else:
            st.warning("No records available for analytics.")      
    # Batch Prediction Page
    if selected == "Batch Prediction":
        st.title("Batch Prediction")
        disease_type = st.selectbox("Select Disease Type for Batch Prediction", ["Diabetes", "Heart Disease", "Parkinsons"])
        uploaded_file = st.file_uploader("Upload CSV file with patient data", type=["csv"])
        if uploaded_file is not None:
            try:
                batch_df = pd.read_csv(uploaded_file)
                st.write("Preview of Uploaded Data")
                st.dataframe(batch_df.head())

                if st.button("Run Batch Prediction"):
                    success_count = 0
                    results = []
                    for _, row in batch_df.iterrows():
                        try:
                            if disease_type == "Diabetes":
                                user_input = [
                                    row['Pregnancies'], row['Glucose'], row['BloodPressure'], row['SkinThickness'],
                                    row['Insulin'], row['BMI'], row['DiabetesPedigreeFunction'], row['Age']
                                ]
                                user_input = [float(x) for x in user_input]
                                prediction = diabetes_model.predict([user_input])[0]
                                prediction_proba = diabetes_model.decision_function([user_input])
                                risk_percentage = calculate_risk_percent(prediction_proba)
                                risk_level = determine_risk_level(risk_percentage)
                                disease= "Diabetes"
                            elif disease_type == "Heart Disease":
                                user_input = [
                                    row['age'], row['sex'], row['cp'], row['trestbps'], row['chol'], row['fbs'], row['restecg'],
                                    row['thalach'], row['exang'], row['oldpeak'], row['slope'], row['ca'], row['thal']
                                ]
                                user_input = [float(x) for x in user_input]
                                prediction = heart_disease_model.predict([user_input])[0]
                                prediction_proba = heart_disease_model.decision_function([user_input])
                                risk_percentage = calculate_risk_percent(prediction_proba)
                                risk_level = determine_risk_level(risk_percentage)
                                disease= "Heart Disease"
                            else: # Parkinsons
                                user_input = [
                                    row['fo'], row['fhi'], row['flo'], row['Jitter_percent'], row['Jitter_Abs'],
                                    row['RAP'], row['PPQ'], row['DDP'], row['Shimmer'], row['Shimmer_dB'],
                                    row['APQ3'], row['APQ5'], row['APQ'], row['DDA'], row['NHR'],
                                    row['HNR'], row['RPDE'], row['DFA'], row['spread1'], row['spread2'],
                                    row['D2'], row['PPE']
                                ]
                                user_input = [float(x) for x in user_input]
                                prediction = parkinsons_model.predict([user_input])[0]
                                prediction_proba = parkinsons_model.decision_function([user_input])
                                risk_percentage = calculate_risk_percent(prediction_proba)
                                risk_level = determine_risk_level(risk_percentage)
                                disease= "Parkinsons"
                            #result
                            result = "Positive" if prediction == 1 else "Negative" 
                            #save to database
                            save_prediction(row['Patient Name'], disease, result, risk_percentage, risk_level)   
                            #store for display
                            results.append({
                                "Patient Name": row['Patient Name'],
                                "Disease": disease,
                                "Result": result,
                                "Risk %": risk_percentage,
                                "Risk Level": risk_level
                            })
                            success_count += 1
                        except Exception as e:
                            st.error(f"Error processing row for patient {row.get('patient_name', 'Unknown')}: {e}")
                            continue
                    
                    # display results
                    if results:
                        results_df = pd.DataFrame(results)
                        st.subheader("Batch Prediction Results")
                        st.dataframe(results_df)
                        st.success(f"Batch prediction completed with {success_count} successful predictions.")
            except Exception as e:
                st.error(f"Unexpected error occurred: {e}")

    st.markdown("""
        <hr style='margin-top: 50px;'>
        <div style='text-align: center; font-size: 14px; color: white;'>
            Built by Subhankar | Powered by Streamlit & Machine Learning<br>
            © 2026 Health Assistant App 2.0
        </div>
    """, unsafe_allow_html=True)
