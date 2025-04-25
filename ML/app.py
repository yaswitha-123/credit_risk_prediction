import streamlit as st
import pickle
import numpy as np
from datetime import datetime

with open('ensemble_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.set_page_config(
    page_title="Risk Classification Tool",
    page_icon="🔍",
    layout="wide"
)

st.markdown("""
    <style>
        .main {
            background-color: #f8f9fa;
            padding: 20px;
        }
        
        .header-container {
            background: linear-gradient(90deg, #4b6cb7 0%, #182848 100%);
            padding: 2rem;
            border-radius: 10px;
            margin-bottom: 2rem;
            text-align: center;
        }
        
        .app-title {
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
            color: black;
        }
        
        .app-subtitle {
            font-size: 1.2rem;
            opacity: 0.9;
            color: black;
        }
        
        .form-card {
            background-color: white;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
        }
        
        .section-title {
            font-size: 1.3rem;
            font-weight: 600;
            color: black;
            margin-bottom: 1rem;
            border-bottom: 2px solid #4b6cb7;
            padding-bottom: 0.5rem;
        }
        
        .results-card {
            text-align: center;
            padding: 2rem;
            border-radius: 10px;
        }
        
        .result-risk {
            background: linear-gradient(90deg, #FF416C 0%, #FF4B2B 100%);
        }
        
        .result-safe {
            background: linear-gradient(90deg, #56ab2f 0%, #a8e063 100%);
        }
        
        .prediction-text {
            font-size: 2rem;
            font-weight: 700;
            margin-bottom: 1rem;
            color: black;
        }
        
        .prediction-description {
            font-size: 1.2rem;
            opacity: 0.9;
            color: black;
        }
        
        .stButton>button {
            background: linear-gradient(90deg, #4b6cb7 0%, #182848 100%);
            color: black;
            border: none;
            border-radius: 5px;
            font-size: 1.1rem;
            font-weight: 600;
            padding: 0.75rem 2rem;
            width: 100%;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 12px rgba(75, 108, 183, 0.3);
        }
        
        .stSelectbox>div>div>div {
            background-color: #f8f9fa;
            border-radius: 5px;
            border: 1px solid #e0e0e0;
            color: black;
        }
        
        .stNumberInput>div>div>input {
            background-color: #f8f9fa;
            border-radius: 5px;
            border: 1px solid #e0e0e0;
            padding: 0.5rem;
            color: black;
        }
        
        body {
            color: black !important;
        }
        
        p, span, label, .stMarkdown, .stText, .stExpander, .stInfo, h1, h2, h3, h4, h5, h6 {
            color: black !important;
        }
        
        .stAlert > div {
            color: black !important;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="header-container">
        <div class="app-title">Risk Classification Tool</div>
        <div class="app-subtitle">Advanced analysis for financial risk assessment</div>
    </div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown('<div class="form-card">', unsafe_allow_html=True)
    
    st.markdown('<div class="section-title">Personal Information</div>', unsafe_allow_html=True)
    pcol1, pcol2 = st.columns(2)
    
    with pcol1:
        age = st.number_input('Age', min_value=18, max_value=100, value=30, step=1)
        sex = st.selectbox('Gender', ['Male', 'Female'])
    
    with pcol2:
        job = st.selectbox('Employment Status', ['Skilled', 'Unskilled', 'Other'])
        housing = st.selectbox('Housing Situation', ['Own', 'Rent', 'Free'])
    
    st.markdown('<div class="section-title">Financial Information</div>', unsafe_allow_html=True)
    fcol1, fcol2 = st.columns(2)
    
    with fcol1:
        saving_accounts = st.selectbox('Savings Account Status', 
                                      ['None', 'Basic', 'Moderate', 'Good'],
                                      help="Level of savings you currently maintain")
        
        checking_account = st.selectbox('Checking Account Status', 
                                       ['None', 'Basic', 'Moderate', 'Good'],
                                       help="Level of funds in your checking account")
    
    with fcol2:
        credit_amount = st.number_input('Credit Amount ($)', 
                                       min_value=0, max_value=100000, value=5000, step=100,
                                       help="Amount of credit requested")
        
        duration = st.slider('Loan Duration (months)', 
                            min_value=1, max_value=60, value=12,
                            help="Period over which the loan will be repaid")
    
    st.markdown('<div class="section-title">Loan Purpose</div>', unsafe_allow_html=True)
    
    purpose = st.selectbox('Purpose of Loan', 
                         ['New car', 'Used car', 'Furniture/equipment', 'Radio/tv', 'Education', 'Re-training'],
                         help="What the loan will be used for")
    
    if purpose == 'New car':
        st.info("Financing for a brand new vehicle purchase.")
    elif purpose == 'Used car':
        st.info("Financing for a pre-owned vehicle purchase.")
    elif purpose == 'Furniture/equipment':
        st.info("Purchase of household items or equipment.")
    elif purpose == 'Radio/tv':
        st.info("Purchase of electronic entertainment devices.")
    elif purpose == 'Education':
        st.info("Funding for formal education expenses.")
    elif purpose == 'Re-training':
        st.info("Funding for professional development or skill acquisition.")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    predict_btn = st.button('Analyze Risk Profile')

with col2:
    st.markdown('<div class="form-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Quick Tips</div>', unsafe_allow_html=True)
    
    st.markdown("""
    - **Higher savings** typically indicate lower risk
    - **Longer loan duration** may increase risk assessment
    - **Home ownership** is usually viewed favorably
    - **Employment status** affects risk evaluation
    """)
    
    st.info("This tool uses machine learning to predict risk categories based on your inputs. The prediction is based on historical data patterns.")
    
    st.markdown(f"<div style='text-align: center; margin-top: 20px; color: black;'>Today: {datetime.now().strftime('%B %d, %Y')}</div>", unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

if predict_btn:
    with st.spinner("Analyzing risk profile..."):
        sex_encoded = 0 if sex == 'Male' else 1
        job_encoded = 0 if job == 'Unskilled' else 1 if job == 'Skilled' else 2
        housing_encoded = 0 if housing == 'Own' else 1 if housing == 'Rent' else 2
        saving_accounts_encoded = 0 if saving_accounts == 'None' else 1 if saving_accounts == 'Basic' else 2 if saving_accounts == 'Moderate' else 3
        checking_account_encoded = 0 if checking_account == 'None' else 1 if checking_account == 'Basic' else 2 if checking_account == 'Moderate' else 3
        purpose_encoded = 0 if purpose == 'New car' else 1 if purpose == 'Used car' else 2 if purpose == 'Furniture/equipment' else 3 if purpose == 'Radio/tv' else 4 if purpose == 'Education' else 5

        features = np.array([
            age, sex_encoded, job_encoded, housing_encoded, 
            saving_accounts_encoded, checking_account_encoded, 
            credit_amount, duration, purpose_encoded
        ]).reshape(1, -1)

        prediction = model.predict(features)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if prediction[0] == 1:
        st.markdown("""
            <div class="results-card result-risk">
                <div class="prediction-text">⚠️ High Risk Profile</div>
                <div class="prediction-description">
                    Based on the provided information, this profile is classified as higher risk.
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        with st.expander("Risk Assessment Details"):
            st.markdown("""
                ### Risk Factors That May Be Contributing:
                
                - **Credit amount** in relation to income
                - **Loan duration** and repayment timeline
                - **Account status** and financial history
                - **Housing situation** and stability
                
                *This assessment is based on statistical patterns and may not reflect individual circumstances.*
            """)
            
    else:
        st.markdown("""
            <div class="results-card result-safe">
                <div class="prediction-text">✅ Low Risk Profile</div>
                <div class="prediction-description">
                    Based on the provided information, this profile is classified as lower risk.
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        with st.expander("Risk Assessment Details"):
            st.markdown("""
                ### Positive Factors Contributing:
                
                - **Financial stability** indicators
                - **Credit amount** appears appropriate
                - **Loan purpose** and duration alignment
                - **Account status** shows good management
                
                *This assessment is based on statistical patterns and does not guarantee loan approval.*
            """)