import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()
DB_URI = os.getenv("DB_URL")
CSV_FILE = "test_etl.csv"
print("Reading CSV from:", CSV_FILE)

def extract(csv_path):    
    if not os.path.exists(csv_path):
        print(f"Error: File '{csv_path}' not found.")
        raise FileNotFoundError(f"File '{csv_path}' does not exist.")
    
    data = pd.read_csv(csv_path)
    print(f"Extracted {len(data)} rows.")
    return data

def transform(df):
    df.dropna(inplace=True)
    if 'year' in df.columns and 'variable' in df.columns:
        df['full_detail'] = df['year'].astype(str) + '-' + df['variable']
    if 'year' in df.columns:
        df = df[df['year'] > 2015]
    return df

def load(df, table_name='files'):
    engine = create_engine(DB_URI)
    try:
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        print("Data loaded successfully.")
    except Exception as e:
        print("Failed to load data:", e)

def run_etl():
    try:
        df = extract(CSV_FILE)
        df = transform(df)
        load(df)
        print("ETL process completed successfully.")
    except Exception as e:
        print("ETL process failed:", e)

if __name__ == "__main__":
    run_etl()
