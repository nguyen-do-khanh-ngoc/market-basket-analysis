#  Phân Tích Dữ Liệu Bán Hàng Quán Cafe & Đề Xuất Chiến Lược (Coffee Shop Sales Analysis)

Dự án này tập trung khai thác bộ dữ liệu giao dịch của hệ thống quán cafe gồm 3 chi nhánh trong 6 tháng đầu năm 2023. Thông qua việc làm sạch dữ liệu, trực quan hóa trên Power BI và áp dụng thuật toán học máy (Apriori), dự án nhằm mục đích hiểu rõ hành vi khách hàng và đưa ra các quyết định kinh doanh dựa trên dữ liệu (Data-driven decisions).

---

##  1. Phân Tích Tổng Quan Doanh Thu (Sales Performance)

**Phân bổ doanh thu theo chi nhánh (Donut Chart):**
Cả 3 chi nhánh đều có hiệu suất hoạt động cực kỳ đồng đều, không có sự chênh lệch quá lớn:
* **Astoria:** Dẫn đầu với tổng thu nhập **230K USD** (chiếm 33.51%).
* **Hell's Kitchen:** Theo sát với **229K USD** (chiếm 33.35%).
* **Lower Manhattan:** Đạt **228K USD** (chiếm 33.15%).

**Xu hướng doanh thu theo thời gian (Line Chart):**
* Trong giai đoạn từ tháng 1 đến tháng 6 năm 2023, đồ thị doanh thu cho thấy một xu hướng **tăng trưởng đều và bền vững**. 
* **Tháng 6 là tháng cao điểm nhất**, cho thấy nhu cầu tiêu dùng tại quán tăng mạnh vào thời điểm đầu hè.
* Dù có những nhịp điều chỉnh giảm cục bộ (như đầu tháng 4 và tháng 5), mức đáy doanh thu vẫn cao hơn hẳn so với các tháng trước đó (duy trì mức trên 2K USD/ngày).

---

##  2. Phân Tích Hành Vi Khách Hàng & Lưu Lượng (Customer Behavior)

**Khung giờ & Ngày cao điểm (Matrix):**
* **Theo ngày:** Lượng hóa đơn phân bổ khá đều đặn suốt tuần (dao động từ 16.000 - 17.000 đơn/ngày). Lượng khách có xu hướng nhỉnh hơn vào các ngày **Thứ Hai** và **Thứ Năm**.
* **Theo giờ:** Lưu lượng khách có sự chênh lệch rõ rệt giữa các khung giờ. Giờ cao điểm (Rush hour) tuyệt đối rơi vào buổi sáng từ **7:00 AM đến 10:00 AM** với khối lượng hóa đơn đột biến (10.000 - 13.000 đơn mỗi giờ).

**Sản phẩm chủ lực (Bar Chart):**
* Nhóm sản phẩm "Top-tier" (bán chạy nhất) đều ghi nhận khối lượng giao dịch trên 3.000 đơn cho mỗi loại.
* Các mặt hàng được ưa chuộng nhất bao gồm: **Chocolate Croissant, Earl Grey Tea, Dark Chocolate, Morning Sunrise Chai,...**

---

##  3. Đề Xuất Chiến Lược Kinh Doanh (Business Recommendations)

Từ những "Sự thật ngầm hiểu" (Insights) trên, nhóm đề xuất các chiến lược hành động sau để tối ưu hóa lợi nhuận:

1. **Chiến lược tối ưu khung giờ vàng (Rush-hour Strategy):**
   * Do lượng khách tập trung cực kỳ đông vào 7h-10h sáng, cần đẩy mạnh triển khai các gói **"Combo Bữa Sáng Nhanh"** (Ví dụ: Cà phê/Trà + Bánh Croissant).
   * Cần tăng cường nhân sự phục vụ vào khung giờ này để giảm thời gian chờ đợi của khách, tăng trải nghiệm dịch vụ.

2. **Chiến lược sản phẩm mồi (Product-led Promotion):**
   * Tận dụng sức hút của các sản phẩm Top đầu (Croissant, Earl Grey) để chạy các chiến dịch như **Mua 1 tặng 1 (BOGO)** hoặc giảm giá khi mua kèm sản phẩm mới. Điều này giúp kích cầu và tăng giá trị trung bình trên mỗi hóa đơn (AOV).

3. **Chiến lược phân bổ nguồn lực cơ sở vật chất:**
   * Cơ sở **Astoria** đang có đà dẫn đầu nhẹ về mặt doanh thu. Cần cân nhắc ưu tiên phân bổ ngân sách để nâng cấp không gian trang trí, cơ sở vật chất tại đây nhằm tạo sức bật, thu hút thêm lượng khách hàng mới và nới rộng khoảng cách doanh thu.

---

##  4. Phân Tích Giỏ Hàng & Luật Kết Hợp (Market Basket Analysis)

Bên cạnh các chỉ số tổng quan, dự án còn đi sâu vào việc tìm ra mối liên hệ ẩn giữa các sản phẩm khách hàng thường mua chung trong cùng một hóa đơn (Sử dụng thuật toán Apriori).

* Chi tiết về các chỉ số *Support, Confidence, Lift* và bảng quy luật Cross-Selling mạnh nhất được trình bày cụ thể tại file báo cáo mã nguồn: `02_association_rule.ipynb` và trang Dashboard Phân tích Combo.

---
