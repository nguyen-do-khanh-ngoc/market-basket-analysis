import streamlit as st
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
import warnings
warnings.filterwarnings('ignore')

# 1. Page Configuration (Bắt buộc phải nằm trên cùng)
st.set_page_config(page_title="F&B Cross-Selling Engine", layout="wide")

# ==========================================
# CÀI ĐẶT FONT MONTSERRAT & FONT AWESOME
# ==========================================
st.markdown("""
    <style>
    /* Import Font Montserrat từ Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;700&display=swap');
    
    /* Import FontAwesome Icons */
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css');

    /* Ép toàn bộ web xài font Montserrat */
    html, body, [class*="css"]  {
        font-family: 'Montserrat', sans-serif !important;
    }
    </style>
""", unsafe_allow_html=True)

# 2. GIAO DIỆN HEADER (Dùng HTML để chèn icon FontAwesome)
st.markdown("<h1><i class='fa-solid fa-cart-arrow-down'></i> Cross-Selling Recommendation Engine</h1>", unsafe_allow_html=True)
st.markdown("<p><i class='fa-solid fa-microchip'></i> AI system automatically scans transaction history to find profitable product combos.</p>", unsafe_allow_html=True)

# 3. DATA LOADING & PREPROCESSING
@st.cache_data(show_spinner="Reading and cleaning raw data...")
def load_and_preprocess_data():
    import os 
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_name = 'Coffee Shop Sales.csv' 
    # Nhớ đổi lại đường dẫn nếu bà đã cho file này vô thư mục data/processed nha
    file_path = os.path.join(current_dir, file_name) 
    
    df = pd.read_csv(file_path, sep=';', decimal=',', encoding='latin1', on_bad_lines='skip')
    
    df.fillna(df.mean(numeric_only=True), inplace=True)
    df.drop_duplicates(inplace=True)
    
    df['Receipt_ID'] = (df['store_id'].astype(str) + "_" + 
                        df['transaction_date'].astype(str) + "_" + 
                        df['transaction_time'].astype(str))
    
    basket = (df.groupby(['Receipt_ID', 'product_detail'])['transaction_qty']
              .sum().unstack().reset_index().fillna(0).set_index('Receipt_ID'))
    
    basket_sets = (basket > 0)
    return basket_sets, len(df)
    
# 4. RUN APRIORI ALGORITHM
@st.cache_data(show_spinner="AI is scanning for patterns, please wait...")
def run_apriori_model(basket_sets, min_sup):
    frequent_itemsets = apriori(basket_sets, min_support=min_sup, use_colnames=True)
    if frequent_itemsets.empty:
        return pd.DataFrame() 
        
    rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.0)
    if rules.empty:
        return pd.DataFrame()

    # Dịch sang Tiếng Anh
    rules['Primary Product (Buy)'] = rules['antecedents'].apply(lambda x: ', '.join(list(x)))
    rules['Bought With'] = rules['consequents'].apply(lambda x: ', '.join(list(x)))
    rules['Support (%)'] = round(rules['support'] * 100, 3)
    rules['Confidence (%)'] = round(rules['confidence'] * 100, 2)
    rules['Lift'] = round(rules['lift'], 2)
    
    rules_final = rules[['Primary Product (Buy)', 'Bought With', 'Support (%)', 'Confidence (%)', 'Lift']]
    return rules_final.sort_values(by='Lift', ascending=False).reset_index(drop=True)

# ==========================================
# MAIN APP INTERFACE
# ==========================================
try:
    basket_sets, total_rows = load_and_preprocess_data()
    
    # Sidebar
    st.sidebar.markdown("### <i class='fa-solid fa-gears'></i> 1. AI Configuration", unsafe_allow_html=True)
    st.sidebar.markdown("*(Note: Changing this will cause the AI to recalculate)*")
    min_sup_input = st.sidebar.slider("Minimum Support", 0.001, 0.050, 0.001, step=0.001, format="%.3f")
    
    df_rules = run_apriori_model(basket_sets, min_sup_input)
    
    st.sidebar.divider()
    
    st.sidebar.markdown("### <i class='fa-solid fa-filter'></i> 2. Result Filters", unsafe_allow_html=True)
    
    if not df_rules.empty:
        max_lift = float(df_rules['Lift'].max())
        min_confidence = st.sidebar.slider("Minimum Confidence (%)", 0.0, 100.0, 10.0, step=5.0)
        min_lift = st.sidebar.slider("Minimum Lift", 1.0, max_lift, 1.2, step=0.1)
        
        filtered_df = df_rules[(df_rules['Confidence (%)'] >= min_confidence) & (df_rules['Lift'] >= min_lift)]
        
        # KPIs
        st.markdown("### <i class='fa-solid fa-chart-pie'></i> System Overview", unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Raw Transactions", f"{total_rows:,}")
        col2.metric("Rules Found (Filtered)", len(filtered_df))
        col3.metric("Max Lift (Highest Synergy)", f"{filtered_df['Lift'].max() if not filtered_df.empty else 0}")

        # Main Table
        st.markdown("### <i class='fa-solid fa-trophy'></i> Top Potential Product Combos", unsafe_allow_html=True)
        if not filtered_df.empty:
            # Highlight max values bằng màu xanh nhạt (#ADD8E6)
            st.dataframe(filtered_df.style.highlight_max(axis=0, color='#ADD8E6'), use_container_width=True)
        else:
            st.warning("No rules passed the display filters. Try lowering Confidence or Lift!")
    else:
        st.error(f"Algorithm found no rules with Min Support at {min_sup_input}. Please lower this value.")

except FileNotFoundError:
    # Báo lỗi chuyên nghiệp kèm icon
    st.markdown("<p style='color:red;'><i class='fa-solid fa-triangle-exclamation'></i> File 'Coffee Shop Sales.csv' not found. Please check your file path!</p>", unsafe_allow_html=True)
