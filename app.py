import streamlit as st
import joblib
import numpy as np

# โหลดโมเดล
model = joblib.load("waste_model.pkl")

st.title("📦 Print Waste Prediction App")
st.write("กรอกข้อมูลด้านล่างเพื่อทำนาย Waste_Percentage")

# รับข้อมูลจากผู้ใช้
order = st.number_input("📝 Order Number", min_value=0)
product_type = st.number_input("📦 Product Type (เช่น 0, 1, 2...)", min_value=0)
paper_weight = st.number_input("🧻 Paper Weight (gsm)", min_value=0)
color_front = st.number_input("🎨 Colors on Front (จำนวนสี)", min_value=0)
customer_name = st.number_input("👤 Customer Code (ตัวเลขที่ใช้แทนชื่อลูกค้า)", min_value=0)

# สร้าง input array สำหรับทำนาย
input_data = np.array([[order, product_type, paper_weight, color_front, customer_name]])

# ทำนาย
if st.button("🔍 Predict Waste %"):
    prediction = model.predict(input_data)
    st.success(f"📈 Predicted Waste Percentage: {prediction[0]:.2f}%")
