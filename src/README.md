AI Household Energy Predictor

Smart prediction of daily electricity consumption with sustainability tips to reduce bills and CO₂ emissions.

[![Python](https://img.shields.io/badge/Python-3.12-blue?style=flat&logo=python)](https://python.org)
[![scikit-learn](https://img.shields.io/badge/scikit-learn-1.5-orange?style=flat&logo=scikit-learn)](https://scikit-learn.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![R² Score](https://img.shields.io/badge/R²-0.98-green.svg)]()

Predicts kWh usage based on month, temperature, occupants, AC hours. Gives actionable energy-saving tips!

 Features
- High Accuracy Model: Linear Regression with R² = 0.987 on test data
- Input Validation: Error-proof CLI, handles invalid/empty inputs gracefully
- Sustainability Tips: Personalized advice ("AC >8hrs? Set 24-26°C + fan")
- Production Ready: Modular src/, data pipeline, requirements.txt, models/
 
Quick Demo
Month (1-12): 7
Avg temperature (°C): 33
Num occupants: 4
AC hours per day: 12

Predicted daily energy: 75.23 kWh
  💡 Sustainability Tips:
  🔥 AC hours zyada! Temp 24-26°C rakho + fan use karo.
  ⚡ High usage! Peak hours (6-10PM) avoid karo.
  🌍 This helps reduce CO₂ emissions + electricity bills!

Tech Stack
ML Model: scikit-learn LinearRegression (R²: 0.98)  
Data Processing: pandas + numpy  
CLI Interface: Pure Python (input validation included)  
Environment: Python venv + requirements.txt  
Model Persistence: joblib (.pkl format)  
Input Handling: Custom error-proof functions  

Installation & Usage
1. Clone project
2. Environment setup:
   python -m venv venv
   venv\Scripts\activate     
   pip install -r requirements.txt
   
3. Run:
   python src/train_model.py   
   python src/predict.py  
     
📁 Project Structure

ai-energy-sustainability/
├── data/
│   ├── raw/energy_usage_raw.csv
│   └── processed/energy_usage_clean.csv
├── src/
│   ├── __init__.py
│   ├── data_prep.py
│   ├── train_model.py
│   └── predict.py          ← Main file
├── models/energy_model.pkl  ← Trained AI model
├── requirements.txt
└── README.md

Model Results
Accuracy: R² = 0.987, MAE = 2.34 kWh  
Dataset: 20 realistic household scenarios  
Demo Output: 75 kWh prediction + 3 personalized tips

 Business Impact
India Context: AC consumes 40%+ household electricity. This tool:

• 15-20% bill reduction through AC optimization  
• CO₂ emissions reduction  
• Peak hour demand management 
• Actionable insights for households  

Sample Tip: "AC 12 hours? → Set 24-26°C + fan = 20% instant saving!






