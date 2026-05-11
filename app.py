import streamlit as st
import pandas as pd
import pickle
import os
from sklearn.linear_model import LinearRegression

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Smart House Price Predictor",
    page_icon="🏠",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}

/* Title */
.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    background: linear-gradient(to right, #4facfe, #00f2fe);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: grey;
    font-size: 18px;
    margin-bottom: 20px;
}

/* Card */
.card {
    background: white;
    padding: 30px;
    border-radius: 18px;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.08);
    margin-top: -60px;
}

/* Button */
.stButton>button {
    width: 100%;
    border-radius: 12px;
    height: 50px;
    background: linear-gradient(to right, #667eea, #764ba2);
    color: white;
    font-size: 18px;
    font-weight: bold;
}

/* Footer */
.footer {
    text-align: center;
    color: grey;
    margin-top: 30px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown('<div class="title">🏠 Smart House Price Predictor</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Get instant AI-powered house price estimates</div>', unsafe_allow_html=True)

# ---------------- HERO IMAGE ----------------
st.image(
    "https://images.unsplash.com/photo-1568605114967-8130f3a36994",
    use_container_width=True
)

# ---------------- LOAD OR TRAIN MODEL ----------------
if not os.path.exists("model.pkl"):
    data = pd.read_csv("data.csv")
    X = data[['area', 'bedrooms']]
    y = data['price']

    model = LinearRegression()
    model.fit(X, y)

    with open("model.pkl", "wb") as f:
        pickle.dump(model, f)
else:
    model = pickle.load(open("model.pkl", "rb"))

# ---------------- CARD UI ----------------
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        area = st.number_input("📏 Area (sq ft)", min_value=100.0, step=50.0)

    with col2:
        bedrooms = st.number_input("🛏 Bedrooms", min_value=1, step=1)

    st.write("")

    # Predict Button
    if st.button("🚀 Predict Price"):
        if area > 0:
            sample = pd.DataFrame([[area, bedrooms]], columns=['area', 'bedrooms'])
            prediction = model.predict(sample)[0]

            st.markdown(f"""
            <div style='background:#e6f4ea; padding:20px; border-radius:12px;'>
            <h3 style='color:#1e7e34;'>💰 Estimated Price: ₹ {prediction:,.2f}</h3>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.error("Please enter valid area!")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown('<div class="footer">Built with ❤️ by Gunjan | AI Project</div>', unsafe_allow_html=True)