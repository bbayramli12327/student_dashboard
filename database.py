# database.py
import pyodbc
from config import DB_CONFIG

def create_connection():
    """SQL Server ilə əlaqə yaradır."""
    conn_str = (
        f"DRIVER={DB_CONFIG['driver']};"
        f"SERVER={DB_CONFIG['server']};"
        f"DATABASE={DB_CONFIG['database']};"
        f"Trusted_Connection={DB_CONFIG['trusted_connection']};"
    )
    return pyodbc.connect(conn_str)

def add_student(student_name: str, score: float) -> bool:
    """Yeni tələbəni database-ə əlavə edir."""
    try:
        with create_connection() as conn:
            cursor = conn.cursor()
            query = "INSERT INTO Students (StudentName, Score) VALUES (?, ?)"
            cursor.execute(query, (student_name, score))
            conn.commit()
            return True
    except Exception as e:
        print(f"Database xətası (add_student): {e}")
        return False

def get_students():
    """Bütün tələbələrin siyahısını çəkir."""
    try:
        with create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("EXEC GetStudentResult")
            rows = cursor.fetchall()
            return [{"id": row[0], "name": row[1], "score": float(row[2])} for row in rows]
    except Exception as e:
        print(f"Database xətası (get_students): {e}")
        return []

def get_student(search_name: str):
    """Ada görə tələbə axtarışı aparır (Stored Procedure istifadə edərək)."""
    try:
        with create_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("EXEC GetStudentResult @SearchName = ?", (search_name,))
            rows = cursor.fetchall()
            return [{"id": row[0], "name": row[1], "score": float(row[2])} for row in rows]
    except Exception as e:
        print(f"Database xətası (get_student): {e}")
        return []