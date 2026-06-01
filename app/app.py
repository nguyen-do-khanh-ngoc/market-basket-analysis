import streamlit as st
import pandas as pd

# 1. Cài đặt giao diện trang web
st.set_page_config(page_title="F&B Cross-Selling Dashboard", layout="wide")
st.title("🛒 Dashboard Phân Tích Mua Kèm (Cross-Selling) - F&B")
st.markdown("Công cụ hỗ trợ team Commercial & Marketing ra quyết định tạo Combo Khuyến mãi.")

# 2. Tạo dữ liệu giả lập (Kết quả từ thuật toán Apriori)
data = {
    'Sản phẩm chính (Mua)': ['Mứt Dâu Chunky', 'Puree Đào', 'Trà Đen', 'Trà Lài', 'Cafe Pha Máy'],
    'Sản phẩm mua kèm': ['Syrup Vani', 'Sốt Caramel', 'Topping Trân Châu', 'Puree Vải', 'Sữa Đặc'],
    'Support (%)': [12.5, 8.2, 25.0, 15.4, 30.1],
    'Confidence (%)': [75.0, 60.5, 45.0, 55.2, 85.0],
    'Lift': [2.4, 1.8, 1.1, 1.9, 1.2]
}
df_rules = pd.DataFrame(data)

# 3. Tạo thanh điều hướng (Sidebar) để người dùng tương tác
st.sidebar.header("⚙️ Điều chỉnh thông số")
min_confidence = st.sidebar.slider("Độ tin cậy tối thiểu (Confidence %)", 10.0, 100.0, 50.0, step=5.0)
min_lift = st.sidebar.slider("Độ nâng cao tối thiểu (Lift)", 1.0, 3.0, 1.5, step=0.1)

# 4. Lọc dữ liệu dựa trên thao tác kéo thanh trượt của sếp/người dùng
filtered_df = df_rules[(df_rules['Confidence (%)'] >= min_confidence) & (df_rules['Lift'] >= min_lift)]

# 5. Hiển thị các chỉ số tổng quan (KPIs)
st.subheader("📊 Tổng quan chiến lược")
col1, col2, col3 = st.columns(3)
col1.metric("Tổng số quy luật tìm thấy", len(filtered_df))
col2.metric("Lift cao nhất", f"{filtered_df['Lift'].max() if not filtered_df.empty else 0}")
col3.metric("Khuyến nghị", "Nên tạo Combo" if not filtered_df.empty else "Cần hạ tiêu chuẩn")

# 6. Hiển thị bảng dữ liệu cuối cùng
st.markdown("### 🏆 Top các cặp sản phẩm sinh lời")
if not filtered_df.empty:
    st.dataframe(filtered_df.style.highlight_max(axis=0, color='#90EE90'), use_container_width=True)
else:
    st.warning("Không có cặp sản phẩm nào thỏa mãn điều kiện hiện tại. Hãy thử kéo thanh trượt xuống!")
