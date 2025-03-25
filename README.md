📊 Strategic Data-Driven Media Campaign Evaluation Framework
A full-scale, end-to-end data science project simulating real-world media campaign analysis using predictive modeling, scenario simulations, and agent-based modeling—culminating in a dynamic Tableau dashboard for stakeholder insights and strategic decision-making.

📜 Table of Contents
🎯 Project Objective

📁 Dataset Overview

🧠 Methodology

📈 Machine Learning Models

🧪 Scenario Simulation

👥 Agent-Based Modeling (ABM)

📊 Tableau Dashboard

🛠️ Tech Stack

📂 Folder Structure

🚀 How to Use This Repo

📩 Contact

🎯 Project Objective
This project demonstrates how data science can drive media planning strategy by evaluating marketing campaigns and customer behavior through:

✅ Predictive modeling
✅ Scenario-based simulation
✅ Agent-based behavioral modeling
✅ Interactive visualization for business decision-making

📁 Dataset Overview
The dataset contains information about marketing campaign interactions for a financial services company, including:

Demographics (e.g., income, age, marital status)

Product purchases (e.g., wine, meat, gold products)

Channel interactions (web, catalog, store)

Campaign responses (Yes/No)

Data Size: 2,240 records × 29 columns
Source: Simulated / Mock Marketing Data

🧠 Methodology
Data Cleaning & Preprocessing

Missing values handled (e.g., income)

Feature engineering: total spending, engagement rate, customer tenure

Encoding categorical variables

BigQuery Storage

Data stored and queried using Google BigQuery

Cleaned datasets exported to Excel for Power BI/Tableau

📈 Machine Learning Models
1️⃣ Regression (XGBoost)
Goal: Predict total customer spend

Metrics: MAE = 3.57, R² = 1.00

Top Features: Total purchases, web visits, meat product spending

2️⃣ Classification (Random Forest)
Goal: Predict whether a customer will respond to a campaign

Accuracy: 87%

Key Insight: High-engagement customers are more likely to respond

🧪 Scenario Simulation
What-If Analysis:

Increase digital ad spend by 20%

Reduce spend on underperforming channels

Focus only on high-value customer segments

Scenario	Avg Predicted Spend
A - Increased Digital Spend	$575.67
B - Cut Low Channels	$576.01
C - Target High-Spenders	$1132.81
📌 Outcome: Focusing on high-spenders has 2× the ROI.

👥 Agent-Based Modeling (ABM)
Simulated long-term purchasing behavior using MESA framework:

Each customer = Agent with income, engagement & purchase probability

Agents react to campaign exposure over 12 months

Spending distribution shows most customers spend between $2,000–$3,500

📈 Insight: Personalized marketing boosts average spend and loyalty.

📊 Tableau Dashboard
✅ Live Dashboard Features:
Customer spending distribution

Income vs. spending segmentation

KPI cards: Avg spend, customer count

Filter by income, campaign response, and engagement

Scenario simulation summary

📌 Link to Dashboard: [https://public.tableau.com/app/profile/brian.balbuena/vizzes]

🛠️ Tech Stack
Category	Tools Used
Programming	Python (Pandas, Scikit-learn, SHAP, XGBoost), SQL
Data Storage	Google BigQuery
Modeling	XGBoost, RandomForest, MESA (ABM)
Visualization	Tableau
Project Mgmt	Git, GitHub, Excel
