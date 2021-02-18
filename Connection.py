import mysql.connector

class Connection:

    # def __init__(self):
    #     HOST = "localhost"
    #     USER = "root"
    #     PASSWORD = ""
    #     DATABASE = "msc_database"

    HOST = "localhost"
    USER = "root"
    PASSWORD = ""
    DATABASE = "msc_database"

    def connect():
        con = mysql.connector.connect(
            host=self.HOST, 
            user=self.USER, 
            password=self.PASSWORD,
            database=self.DATABASE
            )
        return con

    def create_database():
        db = self.connect()
        cursor = db.cursor()
        query = "CREATE DATABASE %s"
        value = (self.DATABASE,)
        cursor.execute(query, value)
        cursor.commit()
        db.close()

    create_database()