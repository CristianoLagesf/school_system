import sqlite3

DB_PATH = 'shool.db'

class Person:
    table_name = None
    def __init__(self, name, age, id):
        self._name = name
        self._age = age
        self._id = id
    @classmethod
    def create(cls,name,age,id):
        conn = sqlite3.connect(DB_PATH)
        curso = conn.cursor()
        try:
            curso.execute(
                f"INSERT INTO {cls.table_name} (id,name,age) VALUES (?,?,?)",
                (id,name,age)
            )
            conn.commit()
            print(f"{cls.table_name.capitalize()} added successfully!")
        except sqlite3.IntegrityError:
            print("Error: Student ID already exist.")
        finally:
            conn.close()
    
    @classmethod
    def get_by_id(cls,id):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(
            f"SELECT id, name,age FROM {cls.table_name} WHERE id = ?",(id,)
            )
        row = cursor.fetchone()
        conn.close()
        if row:
            return cls(row[1],row[2],row[0])
        else:
            print(f"{cls.table_name.capitalize()} not found")
            return None
    
    @classmethod
    def get_all(cls):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(f"SELECT id, name, age FROM {cls.table_name}")
        students = []
        for row in cursor.fetchall():
            students.append(cls(row[1], row[2],row[0]))
        conn.close()
        return students
    
    @classmethod
    def update(cls, id, name= None, age = None):
        conn = sqlite3.connect(DB_PATH)
        curso = conn.cursor()
        
        if name:
            curso.execute(
                f"UPDATE {cls.table_name} SET name = ? WHERE id = ?",(name,id)
                )
        if age:
            curso.execute(
                f"UPDATE {cls.table_name} SET age = ? WHERE id =?",(age,id)
                )
        conn.commit()
        conn.close()
        print(f"{cls.table_name.capitalize()} updated successfully.")
    
    @classmethod
    def delete(cls,id):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM {cls.table_name} WHERE id = ?", (id,))
        conn.commit()
        conn.close()
        print(f"{cls.table_name.capitalize()} deleted successfully.")