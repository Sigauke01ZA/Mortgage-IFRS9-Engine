import streamlit as st
import pandas as pd
import numpy as np
import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "models"

# Load LGD Model
lgd_model = joblib.load(MODEL_DIR / "lgd_model.pkl")
lgd_features = joblib.load(MODEL_DIR / "lgd_features.pkl")

st.set_page_config(page_title="LGD Predictor", layout="wide")
st.title("📉 Loss Given Default (LGD) Predictor")
st.markdown("Predict the percentage of exposure the bank will lose if this loan defaults.")

# Sidebar Inputs
with st.sidebar:
    st.header("⚙️ Defaulted Loan Profile")
    ltv = st.slider("Current LTV (%)", 10.0, 120.0, 80.0)
    purpose = st.selectbox("Loan Purpose", [0, 1], format_func=lambda x: "Business Loan" if x==1 else "Personal/Other")

# Prepare inputs
lgd_dict = {'LTV': ltv / 100.0, 'purpose1': purpose}
lgd_df = pd.DataFrame([lgd_dict])[lgd_features]

# Predict (Logit) then convert to Probability
lgd_logit = lgd_model.predict(lgd_df)[0]
lgd_prob = 1 / (1 + np.exp(-lgd_logit)) # Sigmoid function to reverse logit

# Output
st.header("Model Output")
col1, col2 = st.columns(2)
col1.metric("Predicted Loss Given Default (LGD)", f"{lgd_prob:.2%}")
col2.metric("Predicted Recovery Rate", f"{1 - lgd_prob:.2%}")

st.warning(f"**Interpretation:** If this loan defaults, the bank expects to lose **{lgd_prob:.2%}** of the outstanding balance and recover **{1 - lgd_prob:.2%}**.")

# Cost Example
out_bal = st.number_input("Outstanding Balance at Default (R)", 10000, 5000000, 250000)
loss_amount = out_bal * lgd_prob
st.info(f"On an outstanding balance of R{out_bal:,.2f}, the expected loss is **R {loss_amount:,.2f}**.")