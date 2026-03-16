# 🌦️ End-to-End Weather Data Pipeline

An automated ETL (Extract, Transform, Load) pipeline that fetches real-time weather data, processes it into a structured format, stores it in a SQL database, and generates analytical insights.

## 🚀 Project Overview
This project demonstrates a complete data engineering lifecycle using a **Medallion Architecture** approach:
* **Bronze Layer:** Raw JSON data fetched from the Open-Meteo API.
* **Silver Layer:** Cleaned and filtered data processed via Python (Pandas).
* **Gold Layer:** Aggregated business metrics and visualizations stored in DuckDB.

## 🛠️ Tech Stack
* **Language:** Python 3.10+
* **Storage:** DuckDB (OLAP Database)
* **Libraries:** Pandas (Transformation), Requests (API Ingestion), Matplotlib (Visualization)
* **Architecture:** Modular ETL / Orchestrated Pipeline

## 📊 Features
* **Automated Ingestion:** Fetches current temperature and wind speed.
* **SQL Analytics:** Automatically calculates average temperatures and max wind speeds using SQL queries inside the pipeline.
* **Data Visualization:** Generates a `weather_chart.png` trend report after every run.

## 📋 How to Run
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/weather-data-pipeline.git](https://github.com/YOUR_USERNAME/weather-data-pipeline.git)
