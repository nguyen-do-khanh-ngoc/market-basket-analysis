# ☕ Coffee Shop Sales Analysis & Business Strategy Recommendations
*Extracted from the Power BI Dashboard Report*

## 1. Sales Performance Analysis

### Revenue Distribution by Branch (Donut Chart)

All three branches demonstrate remarkably balanced performance, with no significant differences in revenue contribution:

- **Astoria:** Leads with a total revenue of **$230K** (33.51%).
- **Hell's Kitchen:** Closely follows with **$229K** (33.35%).
- **Lower Manhattan:** Generates **$228K** (33.15%).

<img width="640" height="317" alt="image" src="https://github.com/user-attachments/assets/6c67448d-1b15-485b-8158-66b4211529e4" />

### Revenue Trend Over Time (Line Chart)

- From January to June 2023, revenue exhibited a **steady and sustainable growth trend**.
- **June recorded the highest revenue**, indicating a significant increase in customer demand during the early summer season.
- Although there were temporary declines during early April and May, the revenue floor remained substantially higher than previous months, consistently exceeding **$2,000 per day**.

<img width="682" height="415" alt="image" src="https://github.com/user-attachments/assets/eda5c594-0076-4c18-bf56-3de15a411b51" />

---

## 2. Customer Behavior & Traffic Analysis

### Peak Hours and Peak Days (Matrix)

#### By Day

- Transaction volume is relatively consistent throughout the week, ranging from **16,000 to 17,000 orders per day**.
- Customer traffic tends to be slightly higher on **Mondays** and **Thursdays**.

#### By Hour

- Customer traffic varies significantly across different time periods.
- The absolute peak hours occur between **7:00 AM and 10:00 AM**, when transaction volume surges to approximately **10,000–13,000 orders per hour**.

<img width="603" height="397" alt="image" src="https://github.com/user-attachments/assets/1374592f-eb65-4f9d-81b2-8c8fab657e51" />

### Best-Selling Products (Bar Chart)

- The top-performing products each recorded more than **3,000 transactions**.
- The most popular items include:
  - **Chocolate Croissant**
  - **Earl Grey Tea**
  - **Dark Chocolate**
  - **Morning Sunrise Chai**
  - And several other high-demand products.

<img width="625" height="362" alt="image" src="https://github.com/user-attachments/assets/d5bed75b-46dd-4bde-8454-9469c2913d58" />

---

## 3. Business Recommendations

Based on the insights above, the following strategies are recommended to optimize profitability:

### 1. Rush-Hour Optimization Strategy

- Since customer traffic is heavily concentrated between **7:00 AM and 10:00 AM**, the coffee shop should actively promote **"Quick Breakfast Combos"** (e.g., Coffee/Tea + Croissant).
- Additional staff should be scheduled during these peak hours to reduce waiting times and improve customer experience.

### 2. Product-Led Promotion Strategy

- Leverage the popularity of top-selling products such as **Chocolate Croissant** and **Earl Grey Tea** to launch promotional campaigns, including:
  - **Buy One Get One Free (BOGO)**
  - Discounts when bundled with newly introduced products
- This approach can stimulate demand and increase the average transaction value.

### 3. Resource Allocation Strategy

- The **Astoria** branch currently holds a slight revenue advantage over the other locations.
- Management should consider prioritizing investments in store upgrades, interior design, and customer facilities at this branch to strengthen its competitive advantage and attract additional customers.

---

## 4. Market Basket Analysis & Association Rules

In addition to overall business performance metrics, the project further explores hidden relationships between products that customers frequently purchase together within the same transaction using the **Apriori Algorithm**.

- Detailed explanations of **Support**, **Confidence**, and **Lift**, along with the strongest cross-selling association rules, are available in the source analysis notebook:

```text
02_association_rule.ipynb
```

<img width="1392" height="747" alt="image" src="https://github.com/user-attachments/assets/10bb1d08-b701-4672-a40b-0bfcd6adb9c6" />

---

## Key Takeaway

The analysis reveals that the coffee shop maintains stable revenue growth, experiences strong morning customer demand, and has several high-performing products that can be leveraged for cross-selling opportunities. By implementing targeted promotional campaigns, optimizing staffing during peak hours, and utilizing association rule insights, the business can further increase revenue and enhance customer satisfaction.
---
#  Phân Tích Dữ Liệu Bán Hàng Quán Cafe & Đề Xuất Chiến Lược (Coffee Shop Sales Analysis) Trích Từ file pbix (Power BI đã tạo)

##  1. Phân Tích Tổng Quan Doanh Thu (Sales Performance)

**Phân bổ doanh thu theo chi nhánh (Donut Chart):**
Cả 3 chi nhánh đều có hiệu suất hoạt động cực kỳ đồng đều, không có sự chênh lệch quá lớn:
* **Astoria:** Dẫn đầu với tổng thu nhập **230K USD** (chiếm 33.51%).
* **Hell's Kitchen:** Theo sát với **229K USD** (chiếm 33.35%).
* **Lower Manhattan:** Đạt **228K USD** (chiếm 33.15%).
<img width="640" height="317" alt="image" src="https://github.com/user-attachments/assets/6c67448d-1b15-485b-8158-66b4211529e4" />


**Xu hướng doanh thu theo thời gian (Line Chart):**
* Trong giai đoạn từ tháng 1 đến tháng 6 năm 2023, đồ thị doanh thu cho thấy một xu hướng **tăng trưởng đều và bền vững**. 
* **Tháng 6 là tháng cao điểm nhất**, cho thấy nhu cầu tiêu dùng tại quán tăng mạnh vào thời điểm đầu hè.
* Dù có những nhịp điều chỉnh giảm cục bộ (như đầu tháng 4 và tháng 5), mức đáy doanh thu vẫn cao hơn hẳn so với các tháng trước đó (duy trì mức trên 2K USD/ngày).
<img width="682" height="415" alt="image" src="https://github.com/user-attachments/assets/eda5c594-0076-4c18-bf56-3de15a411b51" />

---

##  2. Phân Tích Hành Vi Khách Hàng & Lưu Lượng (Customer Behavior)

**Khung giờ & Ngày cao điểm (Matrix):**
* **Theo ngày:** Lượng hóa đơn phân bổ khá đều đặn suốt tuần (dao động từ 16.000 - 17.000 đơn/ngày). Lượng khách có xu hướng nhỉnh hơn vào các ngày **Thứ Hai** và **Thứ Năm**.
* **Theo giờ:** Lưu lượng khách có sự chênh lệch rõ rệt giữa các khung giờ. Giờ cao điểm (Rush hour) tuyệt đối rơi vào buổi sáng từ **7:00 AM đến 10:00 AM** với khối lượng hóa đơn đột biến (10.000 - 13.000 đơn mỗi giờ).
<img width="603" height="397" alt="image" src="https://github.com/user-attachments/assets/1374592f-eb65-4f9d-81b2-8c8fab657e51" />

**Sản phẩm chủ lực (Bar Chart):**
* Nhóm sản phẩm bán chạy nhất đều ghi nhận khối lượng giao dịch trên 3.000 đơn cho mỗi loại.
* Các mặt hàng được ưa chuộng nhất bao gồm: **Chocolate Croissant, Earl Grey Tea, Dark Chocolate, Morning Sunrise Chai,...**
<img width="625" height="362" alt="image" src="https://github.com/user-attachments/assets/d5bed75b-46dd-4bde-8454-9469c2913d58" />


---

##  3. Đề Xuất Chiến Lược Kinh Doanh (Business Recommendations)

Từ những Insights trên, đề xuất các chiến lược hành động sau để tối ưu hóa lợi nhuận:

1. **Chiến lược tối ưu khung giờ vàng (Rush-hour Strategy):**
   * Do lượng khách tập trung cực kỳ đông vào 7h-10h sáng, cần đẩy mạnh triển khai các gói **"Combo Bữa Sáng Nhanh"** (Ví dụ: Cà phê/Trà + Bánh Croissant).
   * Cần tăng cường nhân sự phục vụ vào khung giờ này để giảm thời gian chờ đợi của khách, tăng trải nghiệm dịch vụ.

2. **Chiến lược sản phẩm mồi (Product-led Promotion):**
   * Tận dụng sức hút của các sản phẩm Top đầu (Croissant, Earl Grey) để chạy các chiến dịch như **Mua 1 tặng 1 (BOGO)** hoặc giảm giá khi mua kèm sản phẩm mới. Điều này giúp kích cầu và tăng giá trị trung bình trên mỗi hóa đơn.

3. **Chiến lược phân bổ nguồn lực cơ sở vật chất:**
   * Cơ sở **Astoria** đang có đà dẫn đầu nhẹ về mặt doanh thu. Cần cân nhắc ưu tiên phân bổ ngân sách để nâng cấp không gian trang trí, cơ sở vật chất tại đây nhằm tạo sức bật, thu hút thêm lượng khách hàng mới và nới rộng khoảng cách doanh thu.

---

##  4. Phân Tích Giỏ Hàng & Luật Kết Hợp (Market Basket Analysis)

Bên cạnh các chỉ số tổng quan, dự án còn đi sâu vào việc tìm ra mối liên hệ ẩn giữa các sản phẩm khách hàng thường mua chung trong cùng một hóa đơn (Sử dụng thuật toán Apriori).

* Chi tiết về các chỉ số *Support, Confidence, Lift* và bảng quy luật Cross-Selling mạnh nhất được trình bày cụ thể tại file báo cáo mã nguồn: `02_association_rule.ipynb`.
<img width="1392" height="747" alt="image" src="https://github.com/user-attachments/assets/10bb1d08-b701-4672-a40b-0bfcd6adb9c6" />

---
