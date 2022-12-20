import sqlite3

class Database:

    def __init__(self,db):
        self.con = sqlite3.connect(db,check_same_thread=False)
        self.cur = self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS info (id INTEGER PRIMARY KEY,email string,height integer)")
        self.con.commit()
        

    def insert(self,email,height):
        # conn = sqlite3.connect("infos.db")
        # curr = conn.cursor()
        self.cur.execute("INSERT INTO info VALUES (NULL,?,?)",(email,height))
        self.con.commit()
        

    def viwe(self):
        # conn = sqlite3.connect("infos.db")
        # curr = conn.cursor()
        self.cur.execute("SELECT * FROM info")
        row = self.cur.fetchall()
       
        return row

    def search(self,email="",height=""):
        # conn = sqlite3.connect("infos.db")
        # curr = conn.cursor()
        self.cur.execute("SELECT * FROM info WHERE email=? OR (height=?)",(email,height))   
        row = self.cur.fetchall()
        
        return row

    def delete(self,id):
        # conn = sqlite3.connect("infos.db")
        # curr = conn.cursor()
        self.cur.execute("DELETE FROM info WHERE id=?",(id,))
        self.con.commit()
        

    def update(self,id,email,height):
        # conn = sqlite3.connect("infos.db")
        # curr = conn.cursor()
        self.cur.execute("UPDATE info SET email=?,height=? WHERE id=?",(email,height,id))
        self.con.commit()
        

# connect()
# insert("v","v",2,1)
# delete(5)
# update(1,"vk","k",32,23)
# print(viwe())
# print(search("v","v"))