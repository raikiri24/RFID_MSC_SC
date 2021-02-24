from Connection import Connection


class Department:

    def __init__(self):
        self._department_id = 0
        self._department_name = ''

    # Encapsulation
    @property
    def department_id(self):
        return self._department_id
    
    @department_id.setter
    def department_id(self, id):
        self._department_id = id

    @property
    def department_name(self):
        return self._department_name

    @department_name.setter
    def department_name(self, name):
        self._department_name = name

    # Database methods
    # Inserting Department name
    def insert_department_name(self):
        # Create a connection
        con = Connection()
        db = con.connect()
        cursor = db.cursor()
        query = "INSERT INTO departments(department_name) VALUES(%s)"
        value = (self._department_name,)
        cursor.execute(query, value)
        db.commit()
        db.close()

    # Updating Department name
    def update_department_name(self):
        # Create a connection
        con = Connection()
        db = con.connect()
        cursor = db.cursor()
        query = "UPDATE departments SET department_name=%s WHERE department_id=%s"
        values = (self._department_name, self._department_id)
        cursor.execute(query, values)
        db.commit()
        db.close()

    # Deleting Department name
    def delete_department_name(self):
        # Create a connection
        con = Connection()
        db = con.connect()
        cursor = db.cursor()
        query = "DELETE FROM departments WHERE department_id=%s"
        value = (self._department_id,)
        cursor.execute(query, value)
        db.commit()
        db.close()