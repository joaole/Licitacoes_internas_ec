from decouple import config
import mysql.connector
from mysql.connector import Error

def get_connection():
    try:
        conn = mysql.connector.connect(
            host=config('DB_HOST'),
            database=config('DB_NAME'),
            user=config('DB_USER'),
            password=config('DB_PASSWORD')
        )
        if conn.is_connected():
            print("Conectado ao MySQL!")
            return conn
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None
