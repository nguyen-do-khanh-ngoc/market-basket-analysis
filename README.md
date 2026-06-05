# 🛒 Đồ Án Phân Tích Dữ Liệu Bán Hàng Quán Cafe & Gợi Ý Combo

## 1. Giới thiệu dự án
- **Tên dự án:** Phân tích hành vi mua kèm và đề xuất chiến lược bán chéo (Cross-selling) cho quán cafe.
- **Bộ dữ liệu:** `Coffee Shop Sales.csv` - Chứa dữ liệu giao dịch thực tế của 3 chi nhánh quán cafe trong 6 tháng đầu năm 2023.
- **Quy mô dữ liệu:** Khoảng 149,000 dòng dữ liệu chi tiết về hóa đơn, sản phẩm, thời gian, và doanh thu.
- **Mục tiêu:**
  1. Tìm ra các món đồ khách hàng hay mua chung với nhau bằng thuật toán Apriori.
  2. Đề xuất các combo sản phẩm giúp quán tăng doanh thu.
  3. Vẽ Dashboard báo cáo và làm một cái Web App nhỏ để minh họa công cụ gợi ý bán hàng.

---

## 2. Kết Quả Dự Án (Sản Phẩm Đầu Ra)

Dự án bao gồm 2 sản phẩm thực tế:

### 🌐 A. Web App: Công Cụ Gợi Ý Bán Chéo
Được viết bằng Streamlit, giúp người dùng tự chỉnh các thông số (Support, Confidence, Lift) để tìm ra các cặp sản phẩm bán chung tốt nhất theo thuật toán AI.
👉 **[[Trải nghiệm Web App tại đây](https://market-basket-analysis-ez3n3wzqje8wuozunstt8o.streamlit.app/)]**

### 📊 B. Dashboard Power BI: Báo Cáo Doanh Thu
Dashboard trực quan giúp theo dõi doanh thu theo thời gian, chi nhánh và các khung giờ đông khách.
👉 **[[Xem nhanh bản báo cáo PDF tại đây](https://github.com/nguyen-do-khanh-ngoc/market-basket-analysis/blob/main/dashboards/insight.md)]** *(Hoặc tải file `.pbix` trong thư mục `dashboards/` để xem bản đầy đủ).*

---

## 3. Các Bước Thực Hiện

**Bước 1: Tiền xử lý dữ liệu (Data Cleaning & Preprocessing)**
- Dùng Pandas để làm sạch dữ liệu, xử lý các giá trị bị thiếu hoặc lỗi.
- Gom nhóm các món đồ được mua trong cùng một hóa đơn (`Receipt_ID`) để tạo thành định dạng giỏ hàng (Basket).

**Bước 2: Chạy thuật toán Apriori**
- Dùng thư viện `mlxtend` để áp dụng thuật toán Apriori.
- Tính toán 3 chỉ số quan trọng: **Support** (Độ phủ), **Confidence** (Độ tin cậy) và **Lift** (Độ nâng) để tìm ra các quy luật kết hợp (Association Rules).

**Bước 3: Trực quan hóa và Triển khai**
- Dùng Power BI để vẽ biểu đồ phân tích thực trạng kinh doanh.
- Dùng Streamlit để đưa mô hình Apriori lên web cho trực quan.

---

## 4. Nhận Xét & Kết Luận Tổng Quan

Từ việc phân tích dữ liệu, nhóm rút ra được một số nhận xét sau:

**A. Về Doanh Thu & Lượng Khách:**
- Doanh thu của 3 chi nhánh (Astoria, Hell's Kitchen, Lower Manhattan) khá đều nhau, mỗi nơi chiếm khoảng 33% tổng doanh thu.
- Quán đông khách nhất vào buổi sáng từ **7h đến 10h**, với số lượng hóa đơn có thể lên tới hơn 13,000 đơn mỗi giờ.

**B. Về Các Cặp Sản Phẩm Thường Được Mua Chung:**
- **Cặp Cafe & Bánh ngọt:** Nổi bật nhất là cặp món **Ouro Brasileiro shot** (cafe) và **Ginger Scone** (bánh). Chỉ số Lift đạt **15.82**, tức là khi khách gọi cafe này thì xác suất mua thêm bánh kia tăng lên gần 16 lần so với bình thường.
- **Thói quen gọi thêm Syrup:** Khách hàng uống cafe sữa rất hay gọi thêm hương liệu.
  - *Latte* thường đi kèm *Hazelnut syrup* hoặc *Chocolate syrup*.
  - *Cappuccino* thường đi kèm với *Sugar Free Vanilla syrup*.

---

## 5. Đề Xuất Cho Quán Cafe

Từ các nhận xét trên, nhóm có một số đề xuất để giúp quán tăng doanh thu hiệu quả:

1. **Tạo Combo Bữa Sáng:** Khung giờ sáng cực kỳ đông khách, quán nên bán chung "Cà phê Ouro Brasileiro + Bánh Ginger Scone" thành một combo và giảm giá nhẹ. Trưng bày bánh này ngay cạnh máy pha cafe để khách dễ bốc thêm khi đang chờ lấy nước.
2. **Nhắc nhân viên gợi ý mua kèm (Upsell):** Khi khách gọi Latte hoặc Cappuccino, nhân viên thu ngân nên chủ động hỏi: *"Dạ mình có muốn thêm chút Hazelnut syrup cho ly cafe thơm hơn không ạ?"*. Vì dữ liệu cho thấy khách rất thích sự kết hợp này, tỷ lệ gật đầu sẽ rất cao.
3. **Tối ưu hóa Menu:** In thêm các dòng chữ nhỏ gợi ý các loại Syrup phù hợp nhất ngay dưới tên các món cafe chính trên Menu để khách hàng dễ lựa chọn.

---

## 6. Hướng Dẫn Đọc Thư Mục Dự Án

- 📂 **`dashboards/`**: Chứa file Power BI (`.pbix` và `.md`) báo cáo doanh thu tổng quan.
- 📂 **`notebooks/`**: Chứa 2 file Jupyter Notebook (`.ipynb`) thể hiện quá trình dọn dẹp dữ liệu (EDA) và code thuật toán.
- 🌐 **`app.py`**: Chứa code giao diện Streamlit của Web App.
- 📂 **`data/`**: Chứa dữ liệu gốc và dữ liệu đã qua xử lý.
