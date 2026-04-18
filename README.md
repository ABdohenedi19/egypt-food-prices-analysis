# Egypt Food Prices Analysis 🇪🇬

## Project Goal
Analyze food price trends in Egypt and build a model to predict prices.

## Dataset
- Source: (add link here)

## Steps
1. Data Collection
  - In this initial phase, we established the foundation of our dataset by merging two primary sources:

Prices Dataset: Contains historical food price records in Egypt.

Markets Lookup Table: Contains geographical metadata (Governorates, Market names, and IDs).

Key Actions:

Data Integration: Performed a Left Join using market_id to provide geographical context for every price record.

Imputation: Handled missing values for "National Average" entries by assigning them to a "National" category instead of leaving them as nulls.

- Advanced Data Augmentation (Synthetic Data Generation)
To enhance the dataset's size and complexity for future Machine Learning tasks, we implemented a custom Data Augmentation script.

Realistic Simulation Logic:

Category-Based Behavior: Instead of a fixed increase, we modeled price fluctuations based on product categories (e.g., meat and dairy show higher volatility compared to stable cereals).

Stochastic Price Changes: Prices can increase, decrease, or remain stable, mimicking real market supply and demand dynamics.

Outlier Injection: We intentionally introduced a 2% noise factor (extreme price points) to simulate real-world anomalies like hyperinflation, promotions, or data entry errors. This ensures the model becomes robust and resistant to noise.

3. Data Cleaning
4. EDA
5. Modeling
6. Evaluation

## Team Members
- Abdelrahman Ali Henedi
- Osama Reda Teama
