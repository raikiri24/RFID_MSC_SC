from Connection import Connection


class Position:

    def __init__(self):
        self._position_id = 0
        self._position_name = ''

    # Encapsulation
    @property
    def position_id(self):
        return self._position_id

    @position_id.setter
    def position_id(self, id):
        self._position_id = id

    @property
    def position_name(self):
        return self._position_name

    @position_name.setter
    def position_name(self, name):
        self._position_name = name

    # Database methods
    # Inserting Position name
    def insert_position_name(self):
        # Create a connection
        con = Connection()
        db = con.connect()
        cursor = db.cursor()
        query = "INSERT INTO positions(position_name) VALUES(%s)"
        value = (self._position_name,)
        cursor.execute(query, value)
        db.commit()
        db.close()

    # Updating Position name
    def update_position_name(self):
        # Create a connection
        con = Connection()
        db = con.connect()
        cursor = db.cursor()
        query = "UPDATE positions SET position_name=%s WHERE position_id=%s"
        values = (self._position_name, self._position_id)
        cursor.execute(query, values)
        db.commit()
        db.close()

    # Deleting Position name
    def delete_position_name(self):
        # Create a connection
        con = Connection()
        db = con.connect()
        cursor = db.cursor()
        query = "DELETE FROM positions WHERE position_id=%s"
        value = (self._position_id,)
        cursor.execute(query, value)
        db.commit()
        db.close()