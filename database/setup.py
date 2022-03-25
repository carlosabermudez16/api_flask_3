from os import path
import sqlite3
from sqlite3 import Error

from .connection import create_connection

def read_file(path):
    with open(path,"r") as sql_file:
        return sql_file.read()
    
def create_tables():
    conn = create_connection() # conectarnos a la base de datos
    
    path = "database/sql/tables.sql" # lugar para trabajar con las sentencias sql
    
    read_file(path)
    
    try:
        cursor = conn.cursor()
        cursor.execute(read_file(path))
        conn.commit()
        return True
    except Error as e:
        print(f"Error at create_tables(): {str(e)}" )
    finally:
        if conn:
            cursor.close()  # cerramos el cursoe
            conn.close()    # cerramos la conexión
            