# HomeLoans-IFRS9-Engine
End-to-end Mortgage PD &amp; ECL model with Streamlit deployment.

# Mortgage Macro Stress Engine

An end-to-end IFRS 9 Stress-Testing Engine built on a 60-month panel (50,000 loans) spanning the 2007–2009 Global Financial Crisis. This project demonstrates longitudinal PD modeling, IFRS 9 Staging, Lifetime PD, a Business Cost Matrix, and macro-economic stress testing.

![Python](https://img.shields.io/badge/Python-3.13-blue.svg)
![XGBoost](https://img.shields.io/badge/XGBoost-1.7-orange.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30-red.svg)

## Overview
This repository contains a production-grade stress-testing engine designed to calculate IFRS 9 Expected Credit Loss (ECL) under varying macroeconomic scenarios. The engine models the GFC shock to demonstrate how banks dynamically provision capital across Stage 1, Stage 2, and Stage 3 based on a 60-month performance window.

## Model Performance & Validation
This project was developed to strict **SR 11-7 / PRA SS1/23 standards**. The model was validated for discrimination, calibration, stability, and conceptual soundness.

> **Validation Rating: 9.0 / 10 (FIT FOR USE)** 
> 
> *   **Out-of-Time Gini:** **0.5370** (Benchmark-grade for mortgages)
> *   **Calibration:** 1.1 basis point deviation post-Platt scaling (Excellent)
> *   **Sub-population:** AUC 0.7349 (Benign) vs. ~0.799 (Crisis) — Higher discrimination under stress.

📄 **[Click here to read the full Model Validation Report](mortgage_validation_v1.md)**

## Interactive Dashboard
The Streamlit app allows users to input an applicant's profile and dynamically adjust macroeconomic scenarios to watch the IFRS 9 Stage and Expected Credit Loss (ECL) update in real-time. 

*(Note: Update the image name below to match your exact screenshot filename)*
<img src="streamlit_dashboard.png" width="100%">

## Key Analytical Steps

### 1. Exploratory Data Analysis
We analyzed the distribution of key risk drivers (FICO, LTV, DTI) across the Good and Bad populations. The boxplots clearly show the separation between performing and defaulted loans.

<img src="1_boxplots_financial_variables.png" width="100%">
*Figure 1: Distribution of key financial variables by default status.*

### 2. Empirical Lifetime PD Curves
To prove the model captures macro-sensitivity, we plotted the empirical Lifetime PD curves. The 2008 vintage shows a steep, multi-year rise in cumulative defaults, perfectly capturing the GFC economic shock.

<img src="2_lifetime_pd_curves.png" width="100%">
*Figure 2: Empirical Lifetime PD Curves.*

### 3. Business Cost Matrix (Elbow Method)
A model is useless without a business strategy. We did not use a purely statistical cutoff. Instead, we applied a Business Cost Matrix (False Positive vs. False Negative cost) and used the Elbow Method across 59 candidate thresholds to find the business-optimal cutoff.

*(Note: Update the image name below to match your exact cost matrix filename)*
<img src="cost_matrix_elbow.png" width="100%">
*Figure 3: The Elbow Method for Business Cost Optimization.*

### 4. IFRS 9 Stress Testing Engine
The engine applies a Dynamic Loss Given Default (LGD) and calculates the ECL. The chart below shows how the engine provisions capital across the GFC period.

*(Note: Update the image name below to match your exact ECL chart filename)*
<img src="ifrs9_ecl_provision_trend.png" width="100%">
*Figure 4: IFRS 9 ECL Provision trend across the GFC.*

## Technical Architecture
1. **Data ETL:** Processed 50,000 loans over a 60-month panel.
2. **Feature Engineering:** Selected 11 key features (FICO, LTV, DTI, Macro). Handled missing data and outliers.
3. **Modeling:** Champion (XGBoost) calibrated via Platt Scaling, benchmarked against Logistic Regression.
4. **IFRS 9 Engine:** Implemented 3-stage logic with a Business Cost Matrix.

---
**Author:** Raymond Sibanda | [LinkedIn](https://www.linkedin.com/in/raymond-sibanda-91850613b) |
FRM | BSc Mathematics | BCom Honors Accounting
