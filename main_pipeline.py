import requests
import pandas as pd
import duckdb
import os

# --- 1. EXTRACT ---
def extract():
    print("Inhaling data from the clouds...")
    URL = "https://api.open-meteo.com/v1/forecast?latitude=51.5074&longitude=-0.1278&current_weather=true"
    response = requests.get(URL)
    return response.json()['current_weather']

# --- 2. TRANSFORM ---
def transform(raw_data):
    print("Cleaning the messy bits...")
    df = pd.DataFrame([raw_data])
    df = df[['time', 'temperature', 'windspeed']]
    df.columns = ['timestamp', 'temp_celsius', 'wind_kmh']
    return df

# --- 3. LOAD ---
def load(df):
    print("Storing in the vault (Database)...")
    con = duckdb.connect('weather_analytics.db') # New clean DB name
    con.execute("CREATE TABLE IF NOT EXISTS weather_report AS SELECT * FROM df")
    con.execute("INSERT INTO weather_report SELECT * FROM df")
    
    # Check our work immediately!
    result = con.execute("SELECT * FROM weather_report").df()
    print("\n--- SUCCESS! CURRENT DATABASE CONTENT ---")
    print(result)

# --- 4. ANALYZE (GOLD LAYER) ---
def create_report():
    print("\n--- FINAL WEATHER REPORT (GOLD) ---")
    con = duckdb.connect('weather_analytics.db')
    
    # We use SQL to calculate the average temperature
    query = """
    SELECT 
        count(*) as total_readings,
        avg(temp_celsius) as avg_temp,
        max(wind_kmh) as max_wind
    FROM weather_report
    """
    report = con.execute(query).df()
    print(report)

import matplotlib.pyplot as plt

def create_visual():
    print("Generating the weather chart...")
    con = duckdb.connect('weather_analytics.db')
    
    # Get all the history from our database
    df = con.execute("SELECT timestamp, temp_celsius FROM weather_report").df()
    
    # Create the chart
    plt.figure(figsize=(10, 5))
    plt.plot(df['timestamp'], df['temp_celsius'], marker='o', color='tab:blue', linestyle='-')
    
    # Add labels so people know what they are looking at
    plt.title('Temperature Trend Over Time')
    plt.xlabel('Time of Reading')
    plt.ylabel('Temperature (°C)')
    plt.xticks(rotation=45) # Tilt the dates so they don't overlap
    plt.grid(True)
    plt.tight_layout()
    
    # Save the chart as an image
    plt.savefig('weather_chart.png')
    print("Success! Your chart is saved as 'weather_chart.png'")

# --- THE ORCHESTRATOR ---
if __name__ == "__main__":
    data = extract()
    clean_df = transform(data)
    load(clean_df)
    create_report()
    create_visual()