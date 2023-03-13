import streamlit as st
import pickle as pkl
from streamlit_option_menu import option_menu

# Loading the models
diabetes_model=pkl.load(open("C:/Users/91850/Desktop/Multiple Diseases/diabetes_predictor.sav","rb")) 
heart_model=pkl.load(open("C:/Users/91850/Desktop/Multiple Diseases/heart_disease_predictor.sav","rb")) 
parkinson_model=pkl.load(open("C:/Users/91850/Desktop/Multiple Diseases/parkinson_predictor.sav","rb")) 
# breast_cancer_model=pkl.load(open("C:/Users/91850/Desktop/Multiple Diseases/breast_cancer_predictor.sav","rb")) 


# Sidebar for Navigation

with st.sidebar:
    
    selected = option_menu("Multiple Diseases Prediction System",
                           
                           ["Check for Heart Disease",
                            "Check for Diabetes",
                            "Check for Parkinsons Infection"],
                           
                           default_index=0)
    
    

    
        
    # Heart Disease Page
if(selected == "Check for Heart Disease"):
    st.title("Heart Disease Predictor")
    
    col1,col2,col3=st.columns(3)
    
    with col1:
        age=st.text_input("Age")
        
    with col2:
        sex=st.text_input("Sex")
        
    with col3:
        cp=st.text_input("Chest Pain Type")
        
    with col1:
        trestbps=st.text_input("Resting Blood Pressure")
        
    with col2:
        chol=st.text_input("Serum Cholestrol in mg/dl")
        
    with col3:
        fbs=st.text_input("Fasting Blood Sugar > 120 mg/dl")
        
    with col1:
        restecg=st.text_input("Resting Electrocardiographic results")
        
    with col2:
        thalach=st.text_input("Maximum Heart Rate Achieved")
        
    with col3:
        exang=st.text_input("Exercise Induced Angina")
        
    with col1:
        oldpeak=st.text_input("ST Depression induced by Exercise")
        
    with col2:
        slope=st.text_input("Slope of the Peak Exercise ST Segment")
        
    with col3:
        ca=st.text_input("Major Vessels colored by flourosopy")
        
    with col1:
        thal=st.text_input("Thal: 0=Normal; 1=fixed defect; 2=reversible defect")
        
    # creating a button for prediction
    if st.button("Test Your Health"):
        heart_pred=heart_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        
        if heart_pred[0]==1:
            st.warning("You are suffering with a Heart Disease")
        else:
            st.success("You are Healthy")
        
    # Diabetes Page
if(selected == "Check for Diabetes"):
    st.title("Diabetes Predictor")
        
    # Parkinson Page
if(selected == "Check for Parkinsons Infection"):
    st.title("Parkinsons Infection Predictor")