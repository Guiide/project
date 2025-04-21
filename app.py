import streamlit as st
import joblib
import numpy as np
import gdown

# ใส่ file_id จากลิงก์ Google Drive
#file_id = '1mY7GfZpDHfyv1fWNeEgBAtMX2dlB3ouI'
#url = f'https://drive.google.com/uc?id={file_id}'

output = 'waste_model.pkl'
#gdown.download(url, output, quiet=False)

# 📦 โหลดโมเดลด้วย pickle
with open(output, 'rb') as f:
    model = pickle.load(f)

st.title("📦 Print Waste Prediction App")
st.write("กรอกข้อมูลด้านล่างเพื่อทำนาย Waste_Percentage")

# รับข้อมูลจากผู้ใช้
order = st.number_input("📝 Order Number", min_value=0)
product_type = st.number_input("📦 Product Type (เช่น 0, 1, 2...)", min_value=0)
paper_weight = st.number_input("🧻 Paper Weight (gsm)", min_value=0)
color_front = st.number_input("🎨 Colors on Front (จำนวนสี)", min_value=0)
customer_name = st.number_input("👤 Customer Code (ตัวเลขที่ใช้แทนชื่อลูกค้า)", min_value=0)
produced_amount = st.number_input("🏭 Produced Amount", min_value=0.0)
good_amount = st.number_input("✅ Good Amount", min_value=0.0)
input_data = np.array([[order, product_type, paper_weight, color_front, customer_name,produced_amount,good_amount]])


# ทำนาย
if st.button("🔍 Predict Waste %"):
    prediction = model.predict(input_data)
    st.success(f"📈 Predicted Waste Percentage: {prediction[0]:.2f}%")
