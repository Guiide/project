import streamlit as st
import gdown
import numpy as np
import joblib
import os

# ✅ URL จาก Google Drive (เปลี่ยน YOUR_FILE_ID ให้ตรงกับลิงก์ของคุณ)
url = "https://drive.google.com/uc?export=download&id=17xLLprqNYo9v2djw-Q9EkTVxHBfW7omg"
output = "best_random_forest_model.pkl"

# ✅ ดาวน์โหลดไฟล์ (ถ้ายังไม่มีไฟล์)
if not os.path.exists(output):
    gdown.download(url, output, quiet=False)

# ✅ โหลดโมเดลด้วย joblib
model = joblib.load(output)
# แปลง Paper Type
paper_type_mapping = {
    "Art": 0,
    "Glossy": 1,
    "Bond": 2,
    "Offset": 3,
    "อื่นๆ": 4
}

# UI
st.set_page_config(page_title="📄 Paper Usage Predictor", layout="centered")
st.title("📄 ทำนายจำนวนใบกระดาษที่ต้องใช้")
st.markdown("กรอกข้อมูลด้านล่างเพื่อให้โมเดลพยากรณ์")

order = st.number_input("📌 จำนวนออเดอร์ (Order)", min_value=1, step=1)
paper_type = st.selectbox("📦 ชนิดกระดาษ (Paper Type)", options=list(paper_type_mapping.keys()))
paper_weight = st.number_input("📏 แกรม (Paper Weight)", min_value=30, max_value=400, step=5)
color_front = st.slider("🎨 สีด้านหน้า (Color Front)", 0, 6, 4)
color_back = st.slider("🎨 สีด้านหลัง (Color Back)", 0, 6, 1)

if st.button("🔍 ทำนาย"):
    try:
        paper_type_encoded = paper_type_mapping[paper_type]
        X_input = np.array([[order, paper_type_encoded, paper_weight, color_front, color_back]])
        prediction = model.predict(X_input)
        st.success(f"📄 ต้องใช้ใบกระดาษประมาณ: {int(prediction[0])} ใบ")
    except Exception as e:
        st.error(f"❌ เกิดข้อผิดพลาด: {e}")

