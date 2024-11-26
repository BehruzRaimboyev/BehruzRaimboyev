import os
import pandas as pd
import pyodbc
import logging
import json
import datetime
from dotenv import load_dotenv

load_dotenv()  

logging.basicConfig(filename='data_process.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

server = os.getenv('SQL_SERVER')
database = os.getenv('SQL_DATABASE')
folder_path = os.getenv('CSV_FOLDER_PATH')

def connect_to_sql():
    try:
        conn = pyodbc.connect(f'DRIVER={{ODBC Driver 17 for SQL Server}};'
                              f'SERVER={server};'
                              f'DATABASE={database};'
                              f'Trusted_Connection=yes')
        return conn
    except Exception as e:
        logging.error(f"Error connecting to SQL Server: {e}")
        raise

def create_table_from_df(df, table_name, conn):
    columns = ", ".join([f"{col} VARCHAR(255)" for col in df.columns])  
    create_table_sql = f"CREATE TABLE {table_name} ({columns});"
    
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
        conn.commit()
        logging.info(f"Table {table_name} created successfully.")
    except Exception as e:
        logging.error(f"Error creating table {table_name}: {e}")
        raise

def upload_data_to_sql(df, table_name, conn):
    try:
        cursor = conn.cursor()
        for index, row in df.iterrows():
            placeholders = ", ".join(["?"] * len(row))
            insert_sql = f"INSERT INTO {table_name} ({', '.join(df.columns)}) VALUES ({placeholders})"
            cursor.execute(insert_sql, tuple(row))
        conn.commit()
        logging.info(f"Data inserted into table {table_name}.")
    except Exception as e:
        logging.error(f"Error uploading data to table {table_name}: {e}")
        raise

def read_file(file_path):
  
    file_extension = os.path.splitext(file_path)[1].lower()
    
    if file_extension == '.csv':
        return pd.read_csv(file_path)
    elif file_extension == '.xlsx' or file_extension == '.xls':
        return pd.read_excel(file_path)
    elif file_extension == '.json':
        with open(file_path, 'r') as f:
            data = json.load(f)
        return pd.json_normalize(data) 
    else:
        logging.warning(f"Unsupported file type: {file_extension}. Skipping file.")
        return None

def process_files():
    conn = connect_to_sql()
    try:
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                table_name = f"engine_{filename.split('.')[0]}"
                df = read_file(file_path)
                if df is not None:
                    try:
                        create_table_from_df(df, table_name, conn)
                        upload_data_to_sql(df, table_name, conn)
                    except Exception as e:
                        logging.error(f"Failed to process {file_path}: {e}")
    finally:
        conn.close()

def run_etl():
    try:
        logging.info("ETL Process Started.")
        process_files()
        logging.info("ETL Process Completed.")
    except Exception as e:
        logging.error(f"ETL Process Failed: {e}")

if __name__ == '__main__':
    run_etl()
