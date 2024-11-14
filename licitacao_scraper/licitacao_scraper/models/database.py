# models/database.py

import mysql.connector
from mysql.connector import Error

def get_connection():
    try:
        conn = mysql.connector.connect(
            host='sh-pro110.hostgator.com.br',
            database='ecproj16_licitacoes',
            user='ecproj16_pythonScript',
            password='.[3epcnk=E**'
        )
        if conn.is_connected():
            print("Conectado ao MySQL!")
            return conn
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None
