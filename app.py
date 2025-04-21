import streamlit as st
import pickle
import numpy as np
import pandas as pd

with open("w_model.pkl", "rb") as f:
    model = pickle.load(f)
st.write("🧠 ฟีเจอร์ที่โมเดลต้องการ:", model.feature_names_in_)

st.title("📦 Print Waste Prediction App")

order = st.number_input("📝 Order Number", min_value=0)
product_type = st.selectbox("📦 Product Type", [0, 1, 2])
paper_weight = st.number_input("🧻 Paper Weight", min_value=0)
color_front = st.number_input("🎨 Colors (Front)", min_value=0)
customer_type = st.selectbox("👤 Customer Code", [0, 1, 2])

# ดูชื่อฟีเจอร์ที่ต้องการ
expected_cols = model.feature_names_in_
input_dict = {col: 0 for col in expected_cols}

# อัปเดตค่าที่ป้อน
input_dict["Order"] = order
input_dict["Paper_Weight"] = paper_weight
input_dict["color_front"] = color_front
input_dict[f"ProductType_{product_type}"] = 1
input_dict[f"CustType_{customer_type}"] = 1

# แปลงเป็น DataFrame พร้อมชื่อคอลัมน์ตรงกัน
input_df = pd.DataFrame([input_dict])

# ทำนาย
if st.button("🔍 Predict Waste %"):
    pred = model.predict(input_df)
    st.success(f"📈 Predicted Waste Percentage: {pred[0]:.2f}%")
