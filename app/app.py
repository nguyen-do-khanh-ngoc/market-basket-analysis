import streamlit as st
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
import warnings
warnings.filterwarnings('ignore')

# 1. Cài đặt giao diện
st.set_page_config(page_title="F&B Cross-Selling Engine", layout="wide")
st.title("🛒 Hệ Thống Gợi Ý Bán Chéo (Cross-Selling Engine)")
st.markdown("Hệ thống AI tự động quét lịch sử giao dịch để tìm ra các combo sản phẩm sinh lời.")

# 2. HÀM TẢI VÀ TIỀN XỬ LÝ DATA (Chỉ chạy 1 lần duy nhất nhờ @st.cache_data)
@st.cache_data(show_spinner="Đang đọc và làm sạch dữ liệu gốc...")
def load_and_preprocess_data():
    # Đọc file CSV 
    df = pd.read_csv('app/Coffee Shop Sales.csv')
    
    # Tiền xử lý nhanh
    df.fillna(df.mean(numeric_only=True), inplace=True)
    df.drop_duplicates(inplace=True)
    
    # Tạo mã hóa đơn thực tế (Receipt_ID)
    df['Receipt_ID'] = (df['store_id'].astype(str) + "_" + 
                        df['transaction_date'].astype(str) + "_" + 
                        df['transaction_time'].astype(str))
    
    # Tạo ma trận giỏ hàng
    basket = (df.groupby(['Receipt_ID', 'product_detail'])['transaction_qty']
              .sum().unstack().reset_index().fillna(0).set_index('Receipt_ID'))
    
    basket_sets = (basket > 0)
    return basket_sets, len(df)

# 3. HÀM CHẠY THUẬT TOÁN APRIORI (Sẽ chạy lại nếu đổi min_support)
@st.cache_data(show_spinner="AI đang quét tìm quy luật, vui lòng đợi vài giây...")
def run_apriori_model(basket_sets, min_sup):
    frequent_itemsets = apriori(basket_sets, min_support=min_sup, use_colnames=True)
    if frequent_itemsets.empty:
        return pd.DataFrame() # Trả về bảng rỗng nếu không tìm thấy
        
    rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.0)
    if rules.empty:
        return pd.DataFrame()

    # Xử lý format
    rules['Sản phẩm chính (Mua)'] = rules['antecedents'].apply(lambda x: ', '.join(list(x)))
    rules['Sản phẩm mua kèm'] = rules['consequents'].apply(lambda x: ', '.join(list(x)))
    rules['Support (%)'] = round(rules['support'] * 100, 3)
    rules['Confidence (%)'] = round(rules['confidence'] * 100, 2)
    rules['Lift'] = round(rules['lift'], 2)
    
    rules_final = rules[['Sản phẩm chính (Mua)', 'Sản phẩm mua kèm', 'Support (%)', 'Confidence (%)', 'Lift']]
    return rules_final.sort_values(by='Lift', ascending=False).reset_index(drop=True)

# ==========================================
# GIAO DIỆN CHÍNH CỦA APP
# ==========================================
try:
    # Gọi hàm tải data
    basket_sets, total_rows = load_and_preprocess_data()
    
    st.sidebar.header("⚙️ 1. Cấu hình AI (Thuật toán)")
    st.sidebar.markdown("*(Lưu ý: Thay đổi thông số này AI sẽ tốn vài giây để tính toán lại toàn bộ)*")
    # Cho phép sếp tự chỉnh min_support từ 0.001 (0.1%) đến 0.05 (5%)
    min_sup_input = st.sidebar.slider("Độ phủ tối thiểu (Min Support)", 0.001, 0.050, 0.001, step=0.001, format="%.3f")
    
    # Chạy mô hình
    df_rules = run_apriori_model(basket_sets, min_sup_input)
    
    st.sidebar.divider()
    
    st.sidebar.header("🎯 2. Lọc Kết Quả (Hiển thị)")
    # Các thanh trượt này chỉ lọc bảng hiển thị nên sẽ chạy ngay lập tức (không tốn thời gian load)
    if not df_rules.empty:
        max_lift = float(df_rules['Lift'].max())
        min_confidence = st.sidebar.slider("Độ tin cậy (Confidence %)", 0.0, 100.0, 10.0, step=5.0)
        min_lift = st.sidebar.slider("Độ nâng cao (Lift)", 1.0, max_lift, 1.2, step=0.1)
        
        # Lọc dataframe
        filtered_df = df_rules[(df_rules['Confidence (%)'] >= min_confidence) & (df_rules['Lift'] >= min_lift)]
        
        # Hiển thị KPI
        st.subheader("📊 Tổng quan hệ thống")
        col1, col2, col3 = st.columns(3)
        col1.metric("Tổng dòng dữ liệu gốc", f"{total_rows:,}")
        col2.metric("Quy luật tìm thấy (Thỏa điều kiện)", len(filtered_df))
        col3.metric("Combo có sức hút cao nhất (Max Lift)", f"{filtered_df['Lift'].max() if not filtered_df.empty else 0}")

        st.markdown("### 🏆 Bảng Xếp Hạng Cặp Sản Phẩm Tiềm Năng")
        if not filtered_df.empty:
            st.dataframe(filtered_df.style.highlight_max(axis=0, color='#90EE90'), use_container_width=True)
        else:
            st.warning("Không có quy luật nào vượt qua bộ lọc hiển thị. Hãy thử hạ Confidence hoặc Lift xuống!")
    else:
        st.error(f"Thuật toán không tìm thấy quy luật nào với mức Min Support là {min_sup_input}. Vui lòng hạ mức này xuống.")

except FileNotFoundError:
    st.error("⚠️ Không tìm thấy file 'Coffee_Shop_Sales.csv'. Vui lòng kiểm tra lại!")
