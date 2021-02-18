import mysql.connector

class Connection:
    DATABASE = "MSC_Shit5"
    def __init__(self):
        print("Initialized")
        self.create_database()
        

    def connect(self):
        con = mysql.connector.connect(
            host = "localhost", 
            user = "root", 
            password = ""
            )
        return con
    def create_database(self):
        db = self.connect()
        cursor = db.cursor()
        query = f"CREATE DATABASE {self.DATABASE}"
        cursor.execute(query)
        db.close()



connectDB = Connection()
connectDB.create_database()