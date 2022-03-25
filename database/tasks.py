"""Interactuamos con la base de datos"""

import sqlite3
from sqlite3 import Error
from .connection import create_connection

"""Inserta datos"""
def insert_task(data):
    conn = create_connection()
    
    sql = """ INSERT INTO tasks (title,created_date) 
              VALUES(?,?) 
          """
    
    try:
        cursor = conn.cursor()
        cursor.execute(sql, data)
        conn.commit()
        return cursor.lastrowid     # retorna el id del registro 
    except Error as e:
        print(f"Error at insert_task(): {str(e)}")
        return False
    finally:
        if conn:
            cursor.close()
            conn.close()

"""Mostrar datos del último registro"""
def select_task_by_id(_id):
    conn = create_connection()
    
    sql = f"SELECT * FROM tasks WHERE id = {_id}"
    
    try:
        conn.row_factory = sqlite3.Row  # Nos permite que sqlite retorne los datos en un formato parecido a los
                                        # diccionarios de python, de esta forma ya es más facil despues convertir
                                        # estos datos a un diccionario de python realmente.
        cursor = conn.cursor()
        cursor.execute(sql)
        resultado = dict(cursor.fetchone())

        return resultado
    except Error as e:
        print(f'Error at select_task_by_id: {str(e)}')
        return False
    finally:
        if conn:
            cursor.close()
            conn.close()

"""Mostrar todos datos de la base de datos"""
def select_all_tasks():
    conn = create_connection()
    
    sql = """ SELECT * FROM tasks"""

    try:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(sql)
        resultado = [ dict(i) for i in cursor.fetchall() ]
        
        return resultado
    except Error as e:
        print(f'Error at select_all_tasks: {str(e)}')
        return False
    finally:
        if conn:
            cursor.close()
            conn.close()

"""Actualizar datos"""
def update_task(_id,data):
    conn = create_connection()
    
    sql = f""" UPDATE tasks SET title=? 
              WHERE id={_id}
          """
    
    try:
        cursor = conn.cursor()
        cursor.execute(sql, data)
        conn.commit()
        return True
    except Error as e:
        print(f"Error at update_task(): {str(e)}")
        return False
    finally:
        if conn:
            cursor.close()
            conn.close()

"""Eliminar dato"""
def delete_task(_id):
    conn = create_connection()
    
    sql = f"""DELETE FROM tasks WHERE id={_id}"""

    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        return True
        
    except Error as e:
        print(f"Error at delete_task(): {str(e)}")
        return False
    finally:
        if conn:
            cursor.close()
            conn.close()

"""Completar Tareas """
def complete_task(_id, completed):
    conn = create_connection()
    
    sql = f"""UPDATE tasks SET completed = {completed}
              WHERE id = {_id}
           """
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        return True
    except Error as e:
        print(f"Error at completed_task(): {str(e)} ")
    finally:
        if conn:
            cursor.close()
            conn.close()
    
    
    
    