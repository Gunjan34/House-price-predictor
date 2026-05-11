# 🏠 Smart House Price Predictor

A machine learning web application that predicts house prices based on area (sq ft) and number of bedrooms.

## 🚀 Features
- Predict house price instantly
- Clean and modern UI using Streamlit
- Trained using Linear Regression
- Real-time user input prediction

## 🧠 Tech Stack
- Python
- Pandas
- Scikit-learn
- Streamlit

## 📊 How it Works
1. Load dataset (`data.csv`)
2. Train model using Linear Regression
3. Save model using pickle (`model.pkl`)
4. Take user input (area & bedrooms)
5. Predict price and display result

## 💻 Run Locally

```bash
pip install -r requirement.txt
streamlit run app.py
