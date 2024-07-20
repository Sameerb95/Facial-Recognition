import os
import sqlite3
import datetime 

class Database:

    def __init__(self,database_name) -> None:
        self.DATABASE_PATH = f"database/{database_name}.db"


    def create_database(self):

        if not os.path.isfile(self.DATABASE_PATH):
            try:
                conn = sqlite3.connect(self.DATABASE_PATH)

                conn.close()
            
            except:
                print("Database is not created there is some error. Please Verify!!!")

            
    def create_table(self):
        conn = sqlite3.connect(self.DATABASE_PATH)
        cursor = conn.cursor()
        
        with open('sql/create_table.sql', 'r') as sql_file:
            sql_script = sql_file.read()

        cursor.executescript(sql_script)

        conn.commit()
        conn.close()


    def add_visitor(self,first_name,relation,Last_Name):
        conn = sqlite3.connect(self.DATABASE_PATH)
        cursor = conn.cursor()

        cursor.execute("INSERT INTO Frequent_Visitor VALUES (?,?,?,?,?,?,?)",(4,first_name,Last_Name,relation,datetime.datetime.now(),1,None))
        
        conn.commit()
        conn.close()

    def update_visits(self,id):
        conn = sqlite3.connect(self.DATABASE_PATH)
        cursor = conn.cursor()

        cursor.execute("UPDATE Frequent_Visitor SET No_of_Visits = No_of_Visits + 1 , Last_Visited =datetime('now') WHERE Id = ?",(id,))

        conn.commit()
        conn.close()


    def get_visitor_frequency(self,id):
        conn = sqlite3.connect(self.DATABASE_PATH)
        cursor = conn.cursor()
        frequency =cursor.execute("SELECT No_of_Visits FROM Frequent_Visitor WHERE Id = ?",(id,)).fetchone()
        conn.commit()
        conn.close()
        return frequency



if __name__ =='__main__':
    db = Database()
    db.create_database('Dementia')