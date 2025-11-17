import mysql.connector
from mysql.connector import Error
# from utils import log_info, log_error

# If you don’t have utils, you can temporarily define these:
def log_info(msg):
    print(f"[INFO] {msg}")

def log_error(msg):
    print(f"[ERROR] {msg}")


class DBConnection:
    """
    Handles MySQL database connection and queries.
    Uses credentials from local MySQL (docker-compose credentials).
    """

    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host="127.0.0.1",          # local MySQL
                port=3306,
                user="db_user",            # use the non-root user we created
                password="6equj5_db_user", # correct password
                database="home_db"
            )
            self.cursor = self.conn.cursor(dictionary=True)  # fetch as dict
            log_info("Connected to MySQL database successfully")

        except Error as e:
            log_error(f"Database connection failed: {e}")
            raise e

    # ---------------------------------------------
    # SIMPLE EXECUTE (no returned ID)
    # ---------------------------------------------
    def execute(self, query, params=None):
        try:
            self.cursor.execute(query, params)
            self.conn.commit()
        except Error as e:
            log_error(f"Query failed: {e}\nSQL: {query}")
            raise e

    # ---------------------------------------------
    # INSERT AND RETURN AUTO-INCREMENTED ID
    # ---------------------------------------------
    def execute_and_return_id(self, query, params=None):
        try:
            self.cursor.execute(query, params)
            self.conn.commit()
            return self.cursor.lastrowid
        except Error as e:
            log_error(f"Insert failed: {e}")
            raise e

    # ---------------------------------------------
    # SELECT (fetch all rows)
    # ---------------------------------------------
    def fetch_all(self, query, params=None):
        try:
            self.cursor.execute(query, params)
            return self.cursor.fetchall()
        except Error as e:
            log_error(f"Select failed: {e}")
            raise e

    # ---------------------------------------------
    # CLOSE CONNECTION
    # ---------------------------------------------
    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        log_info("MySQL connection closed")
