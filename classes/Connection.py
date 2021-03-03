import mysql.connector


class Connection:

    HOST = 'localhost'
    USER = 'root'
    PASS = ''
    DATABASE = 'msc_database'

    def connect(self):
        con = mysql.connector.connect(
            host=self.HOST,
            user=self.USER, 
            password=self.PASS,
            database=self.DATABASE
            )
        return con

    def create_database(self, database_name):
        db = mysql.connector.connect(host=self.HOST, user=self.USER, password=self.PASS)
        cursor = db.cursor()
        query = f"CREATE DATABASE {database_name};"
        cursor.execute(query)
        db.close()

    def if_employee_table_not_exist(self):
        table_name = 'employee'

        db = self.connect()
        cursor = db.cursor()
        query = "SELECT * FROM information_schema.tables WHERE table_name=%s;"
        value = (table_name,)
        cursor.execute(query, value)
        result = cursor.fetchall()
        db.close()
            # raise Exception("Table does not exist.")
            # print("Table does not exist.")
        print(result)
        return len(result) == 0

    def create_employee_table(self, table_name):
        db = self.connect()
        cursor = db.cursor()
        query = f"""CREATE TABLE {table_name}(
            employee_id INT(11) AUTO_INCREMENT PRIMARY KEY,
            department_id INT(11) NULL,
            position_id INT(11) NULL,
            rfid_uid VARCHAR(10) NOT NULL,
            first_name VARCHAR(50) NOT NULL,
            middle_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50) NOT NULL,
            age INT(2) NOT NULL,
            gender VARCHAR(10) NOT NULL,
            email VARCHAR(20) NOT NULL,
            address VARCHAR(5) NOT NULL,
            contact_number VARCHAR(10) NOT NULL,
            employee_image VARCHAR(20) NOT NULL
        )"""
        cursor.execute(query)
        db.close()