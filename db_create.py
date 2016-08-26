
import sqlite3
from _config import DATABASE_PATH

with sqlite3.connect(DATABASE_PATH) as connection:
    
    #cursor
    c=connection.cursor()
    
    #criar tabela
    c.execute("""CREATE TABLE tasks(task_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, due_date TEXT NOT NULL, priority INTEGER NOT NULL, status INTEGER NOT NULL, user TEXT NOT NULL)""")
    
    #dummy DAta
    c.execute('INSERT INTO  tasks (name, due_date, priority, status, user) VALUES("finish real python course", "24/08/2016", 10, 1,"Nuno")')