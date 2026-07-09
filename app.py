import streamlit as st
import pandas as pd

# Cấu hình giao diện rộng rãi dễ nhìn
st.set_page_config(layout="wide", page_title="Quản lý tiền phòng")

st.title("ỨNG DỤNG QUẢN LÝ TIỀN PHÒNG")
st.markdown("---")

# ----------------- PHẦN 1: USER NHẬP -----------------
st.header("✏️ User nhập (Dữ liệu đầu vào)")

# Giả định dữ liệu cũ để tính toán tiền (Số điện cũ, Số nước cũ)
# Trong thực tế, dữ liệu này có thể lấy từ Database
du_lieu_cu = {
    i: {"dien_cu": 100 + i * 15, "nuoc_cu": 20 + i * 2} for i in range(1, 11)
}

# Đơn giá cố định giả định (có thể tùy chỉnh)
GIA_DIEN_KWH = 3500
GIA_NUOC_M3 = 15000

# Danh sách lưu trữ thông tin sau khi nhập
danh_sach_phong = []

# Tạo các cột nhập liệu hoặc dùng Tabs cho gọn gàng (ở đây dùng selectbox/form để user tiện nhập)
st.subheader("Nhập thông tin chi tiết từng phòng (Từ phòng 1 đến 10):")

for i in range(1, 11):
    with st.expander(f"🏠 Cấu hình Phòng {i}", expanded=(i==1)):
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            so_dien_moi = st.number_input(
                f"Số điện mới (Phòng {i})", 
                min_value=du_lieu_cu[i]["dien_cu"], 
                value=du_lieu_cu[i]["dien_cu"] + 50, 
                key=f"dien_moi_{i}"
            )
        with col2:
            so_nuoc_moi = st.number_input(
                f"Số nước mới (Phòng {i})", 
                min_value=du_lieu_cu[i]["nuoc_cu"], 
                value=du_lieu_cu[i]["nuoc_cu"] + 8, 
                key=f"nuoc_moi_{i}"
            )
        with col3:
            gia_phong = st.number_input(
                f"Giá phòng (Phòng {i})", 
                min_value=0, 
                value=2500000, 
                step=100000, 
                key=f"gia_phong_{i}"
            )
        with col4:
            phi_khac = st.number_input(
                f"Phí khác / Phí dịch vụ (Phòng {i})", 
                min_value=0, 
                value=50000, 
                step=10000, 
                key=f"phi_khac_{i}"
            )
            
        # Lấy số cũ ra để tính toán
        so_dien_cu = du_lieu_cu
