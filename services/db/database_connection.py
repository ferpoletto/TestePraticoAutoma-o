import pymysql
import os
from dotenv import load_dotenv
 
load_dotenv()  # Carrega variáveis do .env
 
class DatabaseHandler:
    def __init__(self):
        self.connection = None
 
    def connect(self):
        if not self.connection or not self.connection.open:
            self.connection = pymysql.connect(
                host=os.getenv("DB_HOST"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                db=os.getenv("DB_NAME"),
                port=int(os.getenv("DB_PORT", 3306)),
                cursorclass=pymysql.cursors.DictCursor,
                autocommit=True
            )
 
    def disconnect(self):
        if self.connection and self.connection.open:
            self.connection.close()
 
    def execute_query(self, query: str, params: tuple = None):
        """
        Executa INSERT, UPDATE ou DELETE.
        Retorna o número de linhas afetadas.
        """
        self.connect()
        with self.connection.cursor() as cursor:
            affected_rows = cursor.execute(query, params)
            return affected_rows
 
    def fetch_all(self, query: str, params: tuple = None):
        """
        Executa SELECT e retorna todos os resultados.
        """
        self.connect()
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchall()
 
    def fetch_one(self, query: str, params: tuple = None):
        """
        Executa SELECT e retorna um único resultado.
        """
        self.connect()
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchone()