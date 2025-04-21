import streamlit as st
import pickle
import numpy as np
import pandas as pd

# โหลดโมเดล
with open("a_model.pkl", "rb") as f:
    model = pickle.load(f)

st.header("📦 Print Waste Prediction App")
st.write("กรอกข้อมูลด้านล่างเพื่อทำนาย Waste_Percentage")

# ฟีเจอร์หลัก
order = st.number_input("📝 **Order Number**", min_value=0)
color_front = st.number_input("🎨 Color", min_value=0)
paper_weight = st.number_input("📄 Paper Weight (gsm)", min_value=0)

# 📦 เลือกประเภทสินค้า (Label → Code)
product_type_display = {
    "Box": 0,
    "Sticker": 1,
    "Booklet": 3,
    "Brochure": 4
}
product_choice = st.selectbox("📦 Product Type", list(product_type_display.keys()))
product_code = product_type_display[product_choice]

# 👤 เลือกประเภทลูกค้า (Label → One-hot suffix)
cust_type_display = {
    "High Waste": "High_Waste",
    "Medium Waste": "Medium_Waste",
    "Low Waste": "Low_Waste"
}
cust_choice = st.selectbox("👤 Customer Type", list(cust_type_display.keys()))
cust_code = cust_type_display[cust_choice]

# เตรียม dict ฟีเจอร์ทั้งหมด
input_dict = {
    "Order": order,
    "color_front": color_front,
    "Paper_Weight": paper_weight,
    "ProductType_0": 0,
    "ProductType_1": 0,
    "ProductType_3": 0,
    "ProductType_4": 0,
    "CustType_High_Waste": 0,
    "CustType_Low_Waste": 0,
    "CustType_Medium_Waste": 0
}

# แปลงให้เป็น one-hot
input_dict[f"ProductType_{product_code}"] = 1
input_dict[f"CustType_{cust_code}"] = 1

# สร้าง DataFrame
input_df = pd.DataFrame([input_dict])

# ทำนาย
if st.button("🔍 Predict Waste %"):
    pred = model.predict(input_df)
    st.success(f"📈 Predicted Waste Percentage: {pred[0]:.2f}%")
