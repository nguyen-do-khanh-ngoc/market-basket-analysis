# 🛒 F&B Product Affinity Analysis & Cross-Selling Strategy

## 1. Giới thiệu dự án
- **Tên dự án:** F&B Market Basket Analysis (Phân tích hành vi mua kèm và Đề xuất chiến lược bán chéo ngành F&B).
- **Bộ dữ liệu (coffee_sales_raw.csv):** Dữ liệu giao dịch thực tế (Transactions) của chuỗi cửa hàng F&B / nhà phân phối nguyên liệu pha chế. 
- **Quy mô dữ liệu:** Hơn 100,000 bản ghi chi tiết từng hạng mục sản phẩm trên các hóa đơn.
- **Đặc trưng dữ liệu:** Mã hóa đơn (Transaction ID), Ngày giờ mua hàng, Tên sản phẩm/nguyên liệu (Puree, Mứt, Trà, Topping, Syrup), Đơn giá, Số lượng, Loại khách hàng (B2C/B2B).
- **Mục tiêu:** 
  1. Khai phá các quy luật mua kèm (Association Rules) ẩn sâu trong lịch sử giao dịch.
  2. Đề xuất chiến lược Bán chéo (Cross-selling) và Đóng gói sản phẩm (Bundling) để tăng Giá trị trung bình trên mỗi đơn hàng (AOV - Average Order Value).
  3. Cung cấp Data Insights giúp phòng Commercial và Trade Marketing thiết kế các chương trình khuyến mãi chéo hiệu quả.

---

## 2. Các bước thực hiện dự án

**Bước 1: Tiền xử lý dữ liệu (Data Preprocessing)**
- **Công cụ:** Python, Pandas.
- Làm sạch dữ liệu: Loại bỏ các giao dịch bị lỗi (hủy đơn, số lượng âm), xử lý các giá trị thiếu (Missing values).
- Gom nhóm dữ liệu (Groupby): Chuyển đổi dữ liệu từ dạng danh sách liệt kê sang định dạng giỏ hàng (Basket format), trong đó mỗi dòng đại diện cho một mã hóa đơn duy nhất chứa tất cả các sản phẩm khách đã mua.

**Bước 2: Xây dựng Ma trận và Áp dụng Thuật toán Apriori**
- **Công cụ:** Python (`mlxtend`, `numpy`).
- **One-Hot Encoding:** Chuyển đổi dữ liệu giỏ hàng thành ma trận nhị phân (0-1), đánh dấu sự xuất hiện của từng sản phẩm trong mỗi hóa đơn.
- **Áp dụng Apriori:** Thiết lập ngưỡng `min_support` (Độ hỗ trợ tối thiểu) để lọc ra các nhóm sản phẩm có tần suất mua chung đủ lớn, loại bỏ các kết hợp mang tính ngẫu nhiên lẻ tẻ.
- Tính toán các chỉ số thương mại cốt lõi: **Confidence** (Độ tin cậy) và **Lift** (Độ nâng cao) để xác định sức mạnh của luật kết hợp.

**Bước 3: Trực quan hóa và Triển khai (Deployment)**
- **Công cụ:** Streamlit, Matplotlib.
- Đóng gói toàn bộ thuật toán vào một Web App nội bộ bằng **Streamlit**.
- Xây dựng bảng điều khiển cho phép người dùng (Marketing/Sales) tự do kéo thả các thanh trượt (slider) để điều chỉnh ngưỡng Support và Confidence, từ đó chủ động tìm kiếm các bộ đôi/bộ ba sản phẩm phù hợp với chiến dịch.
- Trực quan hóa mạng lưới liên kết sản phẩm (Network Graph) để thấy rõ sản phẩm nào là "trung tâm" kéo theo doanh số của các mặt hàng khác.

**Bước 4: Tổng hợp Báo cáo Thương mại**
- **Công cụ:** PowerPoint, Excel.
- Chắt lọc top 10 cặp sản phẩm có chỉ số Lift cao nhất ($Lift > 1.5$) để đưa ra các đề xuất hành động thực tế (Actionable Insights).

---

## 3. Hướng dẫn đọc dự án (Navigation Guide)
Để nắm bắt luồng phân tích từ tư duy kinh doanh đến triển khai kỹ thuật, vui lòng xem theo thứ tự sau:

1. 📂 **`reports/`**: Bắt đầu tại đây. Xem file `CrossSell_Strategy.pptx/pdf` để đọc báo cáo tóm tắt các phát hiện thương mại và đề xuất chiến lược gói combo.
2. 📂 **`app/`**: Chứa file `main.py`. Bạn có thể click vào [Link Streamlit App] đính kèm để trực tiếp thao tác trên Dashboard phân tích luật kết hợp.
3. 📂 **`notebooks/`**: Dành cho việc kiểm tra Source Code. Xem file `01_EDA_and_Apriori.ipynb` để hiểu chi tiết quá trình làm sạch dữ liệu và diễn giải thuật toán.
4. 📂 **`src/`**: Chứa các file Python (`preprocessing.py`, `market_basket.py`) được cấu trúc theo dạng module để dễ dàng tích hợp vào hệ thống lớn.

---

## 4. Kết luận & Insights cốt lõi

Từ việc chạy thuật toán trên hơn 100k giao dịch, bức tranh Cross-sell hiện ra với các điểm nhấn sau:

**A. Hiệu ứng "Chim mồi" (Hero Products)**
* **Phát hiện:** Các mặt hàng như *Trà Đen/Puree Trái cây nền* có chỉ số Support cực cao (xuất hiện trong >60% hóa đơn) nhưng biên lợi nhuận mỏng. 
* **Hành động:** Sử dụng các sản phẩm này làm "mỏ neo" để kéo doanh số cho nhóm sản phẩm ngách có biên lợi nhuận cao hơn (như *Sốt Caramel, Topping trân châu đặc biệt*).

**B. Khám phá các cặp sản phẩm "Hút nhau" (High Lift & Confidence)**
* **Phát hiện:** Khách hàng khi nhập sỉ *Mứt Dâu Chunky* có xác suất lên tới 75% (Confidence) sẽ mua kèm *Syrup Vani*. Chỉ số Lift = 2.4 chứng minh đây không phải sự ngẫu nhiên mà là nhu cầu thực tế của thị trường.
* **Hành động:** Ngừng việc giảm giá đại trà từng món. Thay vào đó, thiết kế **Combo Kích Cầu**: Mua số lượng lớn Mứt Dâu sẽ được chiết khấu 15% cho Syrup Vani. Cách này vừa tăng AOV, vừa bảo vệ được biên lợi nhuận tổng.

**C. Rationalization (Tối ưu hóa danh mục)**
* **Phát hiện:** Một số sản phẩm ngách có doanh số rất thấp và hoàn toàn không có mối liên kết mua kèm nào với các sản phẩm khác (Lift < 1). 
* **Hành động:** Đưa nhóm này vào danh sách theo dõi để cân nhắc loại bỏ (Delist) nhằm giảm chi phí tồn kho (Inventory holding cost).

---

## 5. Định hướng phát triển thực tế (Practical Future Directions)

Để tối ưu hóa ứng dụng của mô hình trong vận hành thực tế của Andros / Doanh nghiệp F&B, dự án có thể mở rộng theo các hướng:

* **Tích hợp vào Hệ thống bán hàng (POS / OMS Integration):**
  * Chuyển đổi mô hình thành API. Khi thu ngân (hoặc Sales B2B) nhập mã sản phẩm A vào hệ thống, màn hình sẽ **Real-time Recommend** (gợi ý theo thời gian thực) sản phẩm B với kịch bản chào hàng có sẵn.
* **Tự động hóa báo cáo Trade Marketing:**
  * Xây dựng Data Pipeline chạy hàng tháng để cập nhật sự thay đổi của các luật kết hợp theo mùa vụ (Ví dụ: mùa hè cặp Đào - Cam chanh lên ngôi, mùa đông cặp Cacao - Caramel chiếm ưu thế).
* **Triển khai A/B Testing cho Combo:**
  * Phối hợp với team Sales để thử nghiệm đẩy bán 2 combo do AI đề xuất tại 2 khu vực địa lý khác nhau (Region A & B). Thu thập dữ liệu sau 1 tháng để đo lường ROI thực tế của thuật toán so với việc tạo combo bằng cảm tính.
