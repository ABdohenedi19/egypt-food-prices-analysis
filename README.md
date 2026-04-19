# Egypt Food Prices Analysis 🇪🇬

## Project Goal
Analyze food price trends in Egypt and build a model to predict prices.

## Dataset
- Source: CAPMAS, Central Agency for Public Mobilization and Statistics, IDSC, Information Decision Support Center, Information Decision Support Center of the Cabinet, Information Decision Support Center of the Cabinet www.agriprice.idsc.net

- This dataset contains Food Prices data for Egypt, sourced from the World Food Programme Price Database. The World Food Programme Price Database covers foods such as maize, rice, beans, fish, and sugar for 98 countries and some 3000 markets. It is updated weekly but contains to a large extent monthly data. The data goes back as far as 1992 for a few countries, although many countries started reporting from 2003 or thereafter

- link : https://data.humdata.org/dataset/wfp-food-prices-for-egypt

## Steps
### 1️⃣ Data Collection & Integration
The foundation was established by merging primary data sources to create a unified geographical context.
* **Data Sources:** Merged historical price records with the `Markets Lookup` table.
* **Integration:** Performed a **Left Join** on `market_id` to map every price entry to its specific Governorate.
* **Imputation:** Resolved "National Average" entries by assigning them to a dedicated "National" category to maintain data continuity.

### 2️⃣ Advanced Data Augmentation (Synthetic Data)
To increase dataset volume and complexity for deep learning, we implemented a custom augmentation engine.
* **Category-Based Behavior:** Modeled price volatility based on food types (e.g., highly volatile Meat vs. stable Cereals).
* **Stochastic Dynamics:** Introduced random price fluctuations to mimic real-world supply and demand shifts.
* **Outlier Injection:** Injected a 2% noise factor to simulate economic anomalies (hyperinflation/shocks), making future models more **Robust**.

### 3️⃣ Data Preprocessing (The Engine) ⚙️
We transformed raw records into a structured, model-ready format using the following pipeline:

* 📍 **Spatial Disaggregation:**
    * *Definition:* Expanded "National" records into 27 unique governorate-level entries to increase geographical granularity.
* 🗑️ **Dimensionality Reduction:**
    * *Definition:* Removed the `Market` column to eliminate noise and focus the model on governorate-level patterns.
* 📅 **Temporal Sorting:**
    * *Definition:* Chronologically ordered data by Date and Governorate to ensure a valid time-series sequence.
* 🧹 **Handling Missing Values:**
    * *Definition:* Applied listwise deletion for records with missing geographical tags to maintain 100% data integrity.
* 📏 **Unit Standardization:**
    * *Definition:* Normalized all quantities to a standard unit (KG). Adjusted prices proportionally (e.g., scaling 800g prices to 1KG equivalents).
* 🕒 **Temporal Reformatting:**
    * *Definition:* Standardized dates into a `MMM-YYYY` format (e.g., Nov-2022) to reduce daily noise while preserving high-frequency data points.

### 4️⃣ Exploratory Data Analysis (EDA) 🔍
*(In Progress)* - Analyzing price distributions, calculating inflation rates per province, and visualizing price heatmaps across Egypt.

### 5️⃣ Modeling & Forecasting 🤖
*(Planned)* - Implementing time-series algorithms (LSTM, Prophet, or Random Forest) to predict future food commodity prices.


## 👨‍💻 Team Members
* **Abdelrahman Ali Henedi**
* **Osama Reda Teama**
