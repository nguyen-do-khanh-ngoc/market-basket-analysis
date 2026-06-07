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


