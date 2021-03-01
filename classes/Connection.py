import mysql.connector


class Connection:

    HOST = 'localhost'
    USER = 'root'
    PASS = ''
    DATABASE = 'tkinter'

    # def __init__(self):
    #     HOST = "localhost"
    #     USER = "root"
    #     PASS = ""
    #     DATABASE = "msc_database"

    def connect(self):
        con = mysql.connector.connect(
            host=self.HOST,
            user=self.USER, 
            password=self.PASS,
            database=self.DATABASE
            )
        return con

    def create_database(self, database):
        db = mysql.connector.connect(host=self.HOST, user=self.USER, password=self.PASS)
        cursor = db.cursor()
        query = f"CREATE DATABASE {database}"
        cursor.execute(query)
        db.close()