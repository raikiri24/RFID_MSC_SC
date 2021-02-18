import mysql.connector

class Connection:

    HOST = "localhost"
    USER = "root"
    PASSWORD = ""
    DATABASE = "msc_database"

    def __init__(self):

        self.create_database()

    def connect():
        con = mysql.connector.connect(
            host=self.HOST, 
            user=self.USER, 
            password=self.PASSWORD
            )
        return con

    def create_database(self):
        db = self.connect()
        cursor = db.cursor()
        query = f"CREATE DATABASE {self.DATABASE}"
        cursor.execute(query)
        db.close()