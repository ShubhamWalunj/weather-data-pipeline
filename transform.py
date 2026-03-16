import pandas as pd
import json

def clean_data():
    # Load the raw file
    with open('raw_weather.json', 'r') as f:
        raw_data = json.load(f)
    
    # Extract just the 'current_weather' part
    current = raw_data['current_weather']
    
    # Convert to a Table (DataFrame)
    df = pd.DataFrame([current])
    
    # Rename columns to be more professional
    df = df[['time', 'temperature', 'windspeed']]
    df.columns = ['timestamp', 'temp_celsius', 'wind_kmh']
    
    # Save as "Silver" data
    df.to_csv('cleaned_weather.csv', index=False)
    print("Step 2: Data cleaned and transformed!")

clean_data()