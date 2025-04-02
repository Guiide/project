
import streamlit as st
import joblib
import numpy as np

# โหลดโมเดล
model = joblib.load("waste_model.pkl")

# รับ input จากผู้ใช้
product_type = st.number_input("Product Type", min_value=0)
paper_weight = st.number_input("Paper Weight", min_value=0)

# สร้าง input array สำหรับทำนาย (คุณต้องกำหนดค่าฟีเจอร์ให้ครบตามที่โมเดลเทรนไว้)
# ตัวอย่าง: สมมุติใช้ค่าเฉลี่ยหรือค่าคงที่เติมช่องว่างให้ครบ
order = 1000  # ตัวอย่างค่าเฉลี่ย
color_front = 4
customer_name = 3

input_data = np.array([[order, product_type, paper_weight, color_front, customer_name]])

# ทำนาย
if st.button("Predict Waste %"):
    prediction = model.predict(input_data)
    st.success(f"Predicted Waste %: {prediction[0]:.2f}")
