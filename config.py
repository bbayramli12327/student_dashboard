# config.py

# SQL Server Konfiqurasiyaları
# Öz SQL Server parametrlərinizə uyğun dəyişdirin
DB_CONFIG = {
    'server': 'localhost',        # Məsələn: 'localhost\\SQLEXPRESS' və ya 'localhost'
    'database': 'UniversityDB',
    'trusted_connection': 'yes',  # Windows Authentication üçün 'yes'
    'driver': '{ODBC Driver 17 for SQL Server}'
}

# Grade Konstantları (Magic Numbers qarşısını almaq üçün)
GRADE_A_THRESHOLD = 90
GRADE_B_THRESHOLD = 80
GRADE_C_THRESHOLD = 70
GRADE_D_THRESHOLD = 60

# Qiymət Hərfləri
GRADE_A = 'A'
GRADE_B = 'B'
GRADE_C = 'C'
GRADE_D = 'D'
GRADE_F = 'F'