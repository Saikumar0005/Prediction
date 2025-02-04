import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Streamlit Page Config
st.set_page_config(page_title="Disease Prediction", layout="wide")

# Get Absolute Path of the Script
working_dir = os.path.dirname(os.path.abspath(__file__))

# Function to Load Models Safely
def load_model(filename):
    model_path = os.path.join(working_dir, "saved-modules", filename)
    if not os.path.exists(model_path):
        st.error(f"⚠️ Model file not found: {model_path}. Please check deployment.")
        st.stop()
    with open(model_path, "rb") as file:
        return pickle.load(file)

# Load Models
diabetes_model = load_model("diabetes_model.sav")
heart_model = load_model("heart_disease_model.sav")
parkinsons_model = load_model("parkinsons_model.sav")

# Sidebar Menu
with st.sidebar:
    selected_model = option_menu("Disease Prediction",
                                 ["Diabetes Prediction", "Heart Disease Prediction", "Parkinsons Prediction"],
                                 menu_icon='hospital-fill',
                                 icons=['activity', 'heart', 'person'],
                                 default_index=0)

# ---- 🟢 Diabetes Prediction ----
if selected_model == "Diabetes Prediction":
    st.title("Diabetes Prediction using Machine Learning")
    
    # User Inputs
    col1, col2, col3 = st.columns(3)
    with col1: Pregnancies = st.number_input("Number of Pregnancies", min_value=0)
    with col2: Glucose = st.number_input("Glucose Level", min_value=0)
    with col3: BloodPressure = st.number_input("Blood Pressure", min_value=0)
    with col1: SkinThickness = st.number_input("Skin Thickness", min_value=0)
    with col2: Insulin = st.number_input("Insulin Level", min_value=0)
    with col3: BMI = st.number_input("BMI", min_value=0.0, format="%.2f")
    with col1: DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function", min_value=0.0, format="%.3f")
    with col2: Age = st.number_input("Age", min_value=0)

    # Prediction
    if st.button("Predict Diabetes"):
        user_input = [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]]
        diab_prediction = diabetes_model.predict(user_input)
        st.error("⚠️ You have Diabetes") if diab_prediction[0] == 1 else st.success("✅ You do not have Diabetes")

# ---- 🔴 Heart Disease Prediction ----
if selected_model == "Heart Disease Prediction":
    st.title("Heart Disease Prediction using Machine Learning")

    # User Inputs
    col1, col2, col3 = st.columns(3)
    with col1: age = st.number_input("Age", min_value=0)
    with col2: sex = st.radio("Sex", ["Male", "Female"])
    with col3: cp = st.number_input("Chest Pain Type", min_value=0, max_value=3)
    with col1: trestbps = st.number_input("Resting Blood Pressure", min_value=0)
    with col2: chol = st.number_input("Cholesterol Level", min_value=0)
    with col3: fbs = st.radio("Fasting Blood Sugar > 120 mg/dl", ["No", "Yes"])
    with col1: restecg = st.number_input("Resting ECG", min_value=0, max_value=2)
    with col2: thalach = st.number_input("Max Heart Rate", min_value=0)
    with col3: exang = st.radio("Exercise Induced Angina", ["No", "Yes"])
    with col1: oldpeak = st.number_input("ST Depression", min_value=0.0, format="%.2f")
    with col2: slope = st.number_input("Slope", min_value=0, max_value=2)
    with col3: ca = st.number_input("CA", min_value=0, max_value=4)
    with col1: thal = st.number_input("Thal (0: Normal, 1: Fixed Defect, 2: Reversible Defect)", min_value=0, max_value=2)

    # Mapping Categorical Inputs
    sex = 1 if sex == "Male" else 0
    fbs = 1 if fbs == "Yes" else 0
    exang = 1 if exang == "Yes" else 0

    # Prediction
    if st.button("Predict Heart Disease"):
        user_input = [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
        heart_prediction = heart_model.predict(user_input)
        st.error("⚠️ The person has heart disease") if heart_prediction[0] == 0 else st.success("✅ No heart disease detected")

# ---- 🟠 Parkinsons Prediction ----
if selected_model == "Parkinsons Prediction":
    st.title("Parkinson's Disease Prediction using Machine Learning")

    # User Inputs
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1: fo = st.number_input("MDVP:Fo(Hz)", min_value=0.0, format="%.2f")
    with col2: fhi = st.number_input("MDVP:Fhi(Hz)", min_value=0.0, format="%.2f")
    with col3: flo = st.number_input("MDVP:Flo(Hz)", min_value=0.0, format="%.2f")
    with col4: Jitter_percent = st.number_input("MDVP:Jitter(%)", min_value=0.0, format="%.3f")
    with col5: Jitter_Abs = st.number_input("MDVP:Jitter(Abs)", min_value=0.0, format="%.3f")
    with col1: RAP = st.number_input("MDVP:RAP", min_value=0.0, format="%.3f")
    with col2: PPQ = st.number_input("MDVP:PPQ", min_value=0.0, format="%.3f")
    with col3: DDP = st.number_input("Jitter:DDP", min_value=0.0, format="%.3f")
    with col4: Shimmer = st.number_input("MDVP:Shimmer", min_value=0.0, format="%.3f")
    with col5: Shimmer_dB = st.number_input("MDVP:Shimmer(dB)", min_value=0.0, format="%.3f")

    # Prediction
    if st.button("Predict Parkinson's Disease"):
        user_input = [[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB]]
        parkinsons_prediction = parkinsons_model.predict(user_input)
        st.error("⚠️ The person has Parkinson's Disease") if parkinsons_prediction[0] == 1 else st.success("✅ No Parkinson's detected")
