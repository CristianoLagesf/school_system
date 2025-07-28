import sqlite3

from model.database import DB_PATH


class Course:
    def __init__(self, name, id, qtd_hours):
        self._name = name
        self._id = id
        self._qtd_hours = qtd_hours
    
    @classmethod
    def create(cls,name,id,qtd_hours):
        conn= sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO course (id, name, qtd_hours) VALUES (?,?,?)",
                (id,name,qtd_hours)
            )
            conn.commit()
            print("Course added successfully!")
        except sqlite3.IntegrityError:
            print("Error: Student ID already exist.")
        finally:
            conn.close()
        
        @classmethod
        def get_by_id(cls,id):
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, name, qtd_hours FROM  course WHERE id=?",(id,)
            )
            row = cursor.fetchone()
            conn.close()
            if row:
                return cls(row[1], row[2], row[0])
            else:
                print("course not found")
                return None
        
        @classmethod
        def get_all(cls):
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, qtd_hours FROM course")
            courses = []
            for row in cursor.fetchall():
                courses.append(cls(row[1], row[2], row[0]))
            conn.close()
            return courses
        
        @classmethod
        def update(cls,id, name=None, qtd_hours = None):
            conn= sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            if name:
                cursor.execute(
                    "UPDATE course SET name =? WHERE id = ?",(name,id)
                )
            if qtd_hours:
                cursor.execute(
                    "UPDATE course SET qtd_hours =? WHERE id = ?",(qtd_hours,id)
                )
            conn.commit()
            conn.close()
            print("Course updated successfully.")
        
        @classmethod
        def delete(cls, id):
            conn= sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM course WHERE id = ?", (id,))
            conn.commit()
        conn.close()
        print("Course deleted successfully.")