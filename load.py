import duckdb
import pandas as pd

def load_to_db():
    # Load the CSV we made
    df = pd.read_csv('cleaned_weather.csv')
    
    # Connect to DuckDB (it creates a file called weather.db)
    con = duckdb.connect('weather.db')
    
    # Create a table and insert the data
    con.execute("CREATE TABLE IF NOT EXISTS weather_table AS SELECT * FROM df")
    con.execute("INSERT INTO weather_table SELECT * FROM df")
    
    print("Step 3: Data loaded into the Database!")
    print(con.execute("SELECT * FROM weather_table").fetchall())

load_to_db()