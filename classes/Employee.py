from classes.Connection import Connection

class Employee:

    def __init__(self):
        self._uid = ''
        self._full_name = ''
        self._age = 0
        self._address = ''
        self._email = ''
        self._employee_image = ''
        self._contact_number = ''


    # Setters and Getters for Encapsulation
    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, uid):
        self._uid = uid

    @property
    def full_name(self):
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        self._name = full_name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if 17 < age < 60:  # Validation for age
            self._age = age
        else:
            raise ValueError("Age is not valid. Try again.")

    @property
    def address(self):
        return self._address
    
    @address.setter
    def address(self, address):
        self._address = address

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def contact_number(self):
        return self._contact_number
    
    @contact_number.setter
    def contact_number(self, number):
        country_code = "+63"
        if not len(number) == 11:  # Contact number must in the format of '09XXXXXXXXX'
            raise ValueError("Contact number should be 11 characters.")
        number = number[1:]  # Slice the number to remove 0
        self._contact_number = country_code + number  # Concatenate country code with sliced number

    @property
    def employee_image(self):
        return self._employee_image

    @employee_image.setter
    def employee_image(self, image_path):
        self._employee_image = image_path

    # Database methods
    # Registering records of employee in database
    def insert_employee_record(self):
        # Create a connection
        con = Connection()
        db = con.connect()
        cursor = db.cursor()
        query = "INSERT INTO employees(uid, full_name, age, address, email, contact_number, employee_image) \
            VALUES(%s, %s, %s, %s, %s, %s, %s)"
        values = (self._uid, self._full_name, self._age, self._address, self._email, self._contact_number, self._employee_image)
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
        query = "UPDATE employees SET full_name=%s, age=%s, address=%s, email=%s, contact_number=%s,\
            employee_image=%s WHERE uid=%s"
        values = (self._name, self._age, self._address, self._email, self._contact_number,\
            self.employee_image, self._uid)
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