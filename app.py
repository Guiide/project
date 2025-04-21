import streamlit as st
import joblib
import numpy as np
import gdown
import pickle

output = 'a_model.pkl'
#gdown.download(url, output, quiet=False)

# 📦 โหลดโมเดลด้วย pickle
with open(output, 'rb') as f:
    model = pickle.load(f)

st.title("📦 Print Waste Prediction App")
st.write("กรอกข้อมูลด้านล่างเพื่อทำนาย Waste_Percentage")

# สร้างคอลัมน์ dummy ทั้งหมดที่ตรงกับตอนเทรน
all_columns = [
    "Order", "color_front", "Paper_Weight",
    "ProductType_0", "ProductType_1", "ProductType_2",  # 👈 ปรับตามของคุณ
    "CustType_0", "CustType_1", "CustType_2"            # 👈 ปรับตามของคุณ
]

# สร้าง dictionary ใส่ค่า default เป็น 0 หมด
input_dict = {col: 0 for col in all_columns}

# รับค่าจาก user
order = st.number_input("📝 Order Number", min_value=0)
paper_weight = st.number_input("🧻 Paper Weight", min_value=0)
color_front = st.number_input("🎨 Colors (จำนวนสี)", min_value=0)
product_type = st.selectbox("📦 Product Type", [0, 1, 2])
customer_type = st.selectbox("👤 Customer Code", [0, 1, 2])

# อัปเดตค่าจริง
input_dict["Order"] = order
input_dict["Paper_Weight"] = paper_weight
input_dict["color_front"] = color_front
input_dict[f"ProductType_{product_type}"] = 1
input_dict[f"CustType_{customer_type}"] = 1

# แปลงเป็น DataFrame แบบ 1 แถว
input_df = pd.DataFrame([input_dict])

# ทำนาย
if st.button("🔍 Predict Waste %"):
    prediction = model.predict(input_df)
    st.success(f"📈 Predicted Waste Percentage: {prediction[0]:.2f}%")
