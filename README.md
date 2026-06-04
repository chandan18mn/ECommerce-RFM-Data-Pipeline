# End-to-End E-Commerce Data Pipeline & RFM Customer Segmentation

##  Project Overview
This project builds a complete data pipeline that takes raw e-commerce transactional data, processes it via an enterprise database and predictive scripts, and exposes interactive business intelligence insights. By migrating data through SQL and Python, I calculated Recency, Frequency, and Monetary (RFM) metrics to segment **4,338 unique customers** into actionable marketing cohorts.

##  Tech Stack
* **Data Ingestion & Storage:** MySQL (Local Database Instance)
* **Data Processing & Modeling:** Python 3.13 (Pandas, SQLAlchemy)
* **Business Intelligence:** Power BI Desktop, DAX (Data Analysis Expressions)

## Pipeline Architecture
1. **Database Engineering (`upload_data.py`):** Cleaned raw e-commerce records and ingested them efficiently into a local MySQL instance.
2. **Analytics Engineering (`rfm_scoring.py`):** Queried the database via Python, engineered mathematical metrics for Recency, Frequency, and Monetary values, and assigned an algorithmic score (1-5) to each attribute.
3. **Data Modeling & Visualization (Power BI):** Developed a relative data model, constructed explicit DAX measures, and styled an executive-level dashboard.

##  Key Insights Found
* **The VIP Whale Effect:** The "Champions (VIP)" cohort represents 1,128 customers but generates **$5.89M (66%)** of the total $8.91M revenue.
* **Retention Risk:** 1,071 customers are currently classified as "Lost / Hibernating," signaling an immediate opportunity for a win-back email campaign.
* **High Engagement:** VIP customers maintain an outstanding average recency rate of just **12.6 days** between purchases.
