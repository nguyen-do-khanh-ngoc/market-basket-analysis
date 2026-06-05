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
---
# 🛒 Coffee Shop Sales Data Analysis & Product Bundle Recommendation Project

## 1. Project Overview

- **Project Title:** Customer Purchase Behavior Analysis and Cross-Selling Strategy Recommendation for a Coffee Shop.
- **Dataset:** `Coffee Shop Sales.csv` – Contains real transaction data from three coffee shop branches during the first six months of 2023.
- **Dataset Size:** Approximately 149,000 detailed transaction records, including invoices, products, timestamps, and revenue information.
- **Objectives:**
  1. Identify products that customers frequently purchase together using the Apriori algorithm.
  2. Recommend product bundles to help increase sales revenue.
  3. Build a dashboard and a lightweight web application to demonstrate the recommendation system.

---

## 2. Project Outcomes (Deliverables)

The project consists of two practical deliverables:

### 🌐 A. Cross-Selling Recommendation Web App

Developed using Streamlit, this application allows users to customize parameters such as Support, Confidence, and Lift to discover the most valuable product associations generated by the Apriori algorithm.

👉 **[[Try the Web App Here](https://market-basket-analysis-ez3n3wzqje8wuozunstt8o.streamlit.app/)]**

### 📊 B. Power BI Sales Dashboard

An interactive dashboard that provides insights into sales performance across different branches, time periods, and peak business hours.

👉 **[[View the Dashboard Report](https://github.com/nguyen-do-khanh-ngoc/market-basket-analysis/blob/main/dashboards/insight.md)]** *(Or download the `.pbix` file from the `dashboards/` directory to explore the full interactive report.)*

---

## 3. Project Workflow

### Step 1: Data Cleaning & Preprocessing

- Used Pandas to clean the dataset and handle missing or inconsistent values.
- Grouped products purchased within the same invoice (`Receipt_ID`) to create a basket format suitable for Market Basket Analysis.

### Step 2: Applying the Apriori Algorithm

- Utilized the `mlxtend` library to implement the Apriori algorithm.
- Calculated three key metrics:
  - **Support** – Frequency of occurrence.
  - **Confidence** – Reliability of an association rule.
  - **Lift** – Strength of the relationship between products.
- Generated association rules to identify products that are frequently purchased together.

### Step 3: Visualization & Deployment

- Built a Power BI dashboard to visualize sales performance and business trends.
- Developed a Streamlit web application to provide an interactive recommendation tool.

---

## 4. Key Findings & Insights

### A. Revenue & Customer Traffic

- Revenue was distributed fairly evenly among the three branches (**Astoria**, **Hell's Kitchen**, and **Lower Manhattan**), with each branch contributing approximately 33% of total revenue.
- The busiest period occurred between **7:00 AM and 10:00 AM**, during which transaction volumes exceeded **13,000 orders per hour**.

### B. Frequently Purchased Product Combinations

#### Coffee & Pastry Pairings

- The strongest association was identified between **Ouro Brasileiro Shot** and **Ginger Scone**.
- This pair achieved a **Lift score of 15.82**, meaning customers who purchased the coffee were nearly 16 times more likely to purchase the pastry compared to the average customer.

#### Syrup Add-On Preferences

Customers ordering milk-based coffee beverages frequently added flavored syrups:

- *Latte* was commonly paired with:
  - *Hazelnut Syrup*
  - *Chocolate Syrup*

- *Cappuccino* was commonly paired with:
  - *Sugar-Free Vanilla Syrup*

---

## 5. Business Recommendations

Based on the analysis, the following recommendations can help improve sales performance:

### 1. Create a Breakfast Combo

The morning period experiences the highest customer traffic, making it an ideal opportunity to offer an **"Ouro Brasileiro Shot + Ginger Scone"** combo with a small discount.

Displaying the pastry near the coffee preparation area may also encourage impulse purchases while customers wait for their drinks.

### 2. Encourage Upselling

When customers order a Latte or Cappuccino, cashiers should proactively recommend relevant syrup add-ons.

For example:

> "Would you like to add some Hazelnut Syrup to make your coffee even more flavorful?"

Since the data shows a strong association between these items, the acceptance rate is expected to be relatively high.

### 3. Optimize the Menu

Add small recommendations beneath coffee items on the menu to suggest the most suitable syrup options.

This can make decision-making easier for customers and increase the average order value.

---

## 6. Project Structure

- 📂 **`dashboards/`**: Contains Power BI reports (`.pbix`) and business insight summaries (`.md`).
- 📂 **`notebooks/`**: Includes Jupyter Notebooks (`.ipynb`) covering Exploratory Data Analysis (EDA), data preprocessing, and Apriori implementation.
- 🌐 **`app.py`**: Contains the Streamlit web application code.
- 📂 **`data/`**: Stores both the raw and processed datasets.

---
