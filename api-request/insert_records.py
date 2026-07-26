from api_request import mock_fetch_data,fetch_data 
import psycopg2 




def connect_to_db():
    print("Connecting to the database...")

    try:
        conn = psycopg2.connect(
            host="db",
            port=5432,
            database="db",
            user="db_user",
            password="db_password"
        )
        return conn
        
    except psycopg2.Error as e:
        print(f"An error occurred while connecting to the database: {e}")
        raise

    return "Database connection established"


def create_table(conn):
    print("Creating the weather_data table if it doesn't exist...")

    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE SCHEMA IF NOT EXISTS dev;
            CREATE TABLE IF NOT EXISTS dev.raw_weather_data (
                id SERIAL PRIMARY KEY,
                city Text,
                temperature Float,
                weather_description Text,
                wind_speed Float,
                pressure Float,
                humidity Float,
                time TIMESTAMP,
                inserted_at TIMESTAMP DEFAULT NOW(),
                utc_offset TEXT

            );
        ''')
        conn.commit()
        cursor.close()
        print("Table created successfully.")
    except psycopg2.Error as e:
        print(f"An error occurred while creating the table: {e}")
        raise



def insert_records(conn, data):
    print("Inserting records into the database...")

    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO dev.raw_weather_data (city, temperature, weather_description, wind_speed, pressure, humidity, time, inserted_at, utc_offset)
            VALUES (%s, %s, %s, %s, %s, %s, %s, NOW(), %s)
        ''', (
            data['location']['name'],
            data['current']['temperature'],
            data['current']['weather_descriptions'][0],
            data['current']['wind_speed'],
            data['current']['pressure'],
            data['current']['humidity'],
            data['location']['localtime'],
            data['location']['utc_offset']
        ))                          
        conn.commit()
        print("Records inserted successfully.")
    except psycopg2.Error as e:
        print(f"An error occurred while inserting records: {e}")
        raise

def main():
    try:
        #data = mock_fetch_data()
        data = fetch_data()
        conn = connect_to_db()
        create_table(conn)
        insert_records(conn, data)
    except Exception as e:
        print(f"An error occurred in the main function: {e}")
    finally:
        if 'conn' in locals():
            conn.close()
            print("Database connection closed.")

