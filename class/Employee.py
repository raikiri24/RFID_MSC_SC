from connection import Connection


class Employee:

    def __init__(self):
        self._uid = ''
        self._name = ''
        self._age = 0
        self._address = ''

    # Setters and Getters for Encapsulation
    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, a):
        self._uid = a

    @property
    def name(self):
        return self._uid

    @name.setter
    def name(self, a):
        self._name = a

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, a):
        if age < 0:
            raise ValueError("You're under age.")
        self._age = a

    @property
    def address(self):
        return self._address
    
    @address.setter
    def address(self, a):
        self._address = a

    # Registering records of employee in database
    def insert_employee_record(self):
        # Create a connection
        con = Connection()
        db = con.connect()
        cursor = db.cursor()
        query = "INSERT INTO employees(uid, name, age, address) VALUES(%s, %s, %s, %s)"
        values = (self._uid, self._name, self._age, self._address)
        cursor.execute(query, values)
        db.commit()
        db.close()

    # Deleting records of employee in database
    def delete_employee_record(self):
        # Create a connection
        con = Connection()
        db = con.connect()
        cursor = db.cursor()
        query = "DELETE FROM employees WHERE uid=%s"
        value = (self._uid,)
        cursor.execute(query, value)
        db.commit()
        db.close()

    # Updating records of employee in database
    def update_employee_record(self):
        # Create a connection
        con = Connection()
        db = con.connect()
        cursor = db.cursor()
        query = "UPDATE employees SET name=%s, age=%s, address=%s WHERE uid=%s"
        values = (self._name, self._age, self._address, self._uid)
        cursor.execute(query, values)
        db.commit()
        db.close()

    # Check if uid already exists in database
    def check_if_uid_already_exist(self, uid_to_check):
        # Create a connection
        con = Connection()
        db = con.connect()
        cursor = db.cursor()
        query = "SELECT * FROM employees WHERE uid=%s"
        value = (uid_to_check,)
        cursor.execute(query, value)
        cursor.fetchall()
        db.close()
        return cursor.rowcount > 0

    # Extracting employee's information in database
    def extract_employee_info(self, uid_to_extract):
        # Create a connection
        con = Connection()
        db = con.connect()
        cursor = db.cursor()
        query = "SELECT * FROM employees WHERE uid=%s"
        value = (uid_to_extract,)
        cursor.execute(query, value)
        result = cursor.fetchone()
        db.close()
        return result
