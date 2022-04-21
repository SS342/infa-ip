import sqlite3
from static.modules.DevPost import Post
from static.modules.Camp import Camp


class DataBase(object):
    def __init__(self, path):
        self.connect = sqlite3.connect(path)
        self.cursor = self.connect.cursor()


    def CreateTableEmailPredReg(self):
        sql = """
                    CREATE TABLE IF NOT EXISTS EmailPredReg (
                    email STRING UNIQUE);
                """


        self.cursor.execute(sql)
        self.connect.commit()

    
    def CreateTableDevBlog(self):
        sql = '''CREATE TABLE IF NOT EXISTS DevBlog (
                    name        STRING UNIQUE
                                    NOT NULL,
                    description STRING NOT NULL,
                    author      STRING NOT NULL,
                    date        STRING NOT NULL
                );'''
    
        self.cursor.execute(sql)
        self.connect.commit()


    def CreateTableBugs(self):
        sql = """
                    CREATE TABLE IF NOT EXISTS Bugs (
                    bug STRING,
                    status STRING);
                """

        self.cursor.execute(sql)
        self.connect.commit()


    def CreateTableCampSearch(self):
        sql = '''CREATE TABLE IF NOT EXISTS CampSearch (
                    name        STRING UNIQUE
                                    NOT NULL,
                    server STRING NOT NULL,
                    type STRING NOT NULL,
                    description STRING NOT NULL,
                    author      STRING NOT NULL,
                    date        STRING NOT NULL
                );'''
    
        self.cursor.execute(sql)
        self.connect.commit()


    def OriginPredRegEmail(self, email):
        sql = f"SELECT * FROM EmailPredReg WHERE email = '{email}'"


        for row in self.cursor.execute(sql).fetchall():
            return False
        else:
            return True


    def NewPredRegUser(self, email):
        if self.OriginPredRegEmail(email):
            sql = f"INSERT INTO EmailPredReg values ('{email}')"
            self.cursor.execute(sql)
            self.connect.commit()
        else:
            return False


    def GetDevBlog(self):
        posts = []
        for row in self.cursor.execute("SELECT *, rowid FROM DevBlog").fetchall():
            posts.append(Post(title=row[0], description=row[1], author=row[2], date=row[3], id = row[4]))

        return posts


    def NewBug(self, text):
        sql = f"INSERT INTO Bugs values('{text}', 'new')"
        self.cursor.execute(sql)
        self.connect.commit()


    def SelectCamp(self, server, _type_):
        camps =[]
        if server != "all" and _type_ != "all":
            sql = f"SELECT * FROM CampSearch WHERE server='{server}' AND type = '{_type_}'"
        elif server != "all" and _type_ == "all":
            sql = f"SELECT * FROM CampSearch WHERE server='{server}'"
        elif server == "all" and _type_ != "all":
            sql = f"SELECT * FROM CampSearch WHERE type = '{_type_}'"
        else:
            sql = f"SELECT * FROM CampSearch"

        for row in self.cursor.execute(sql).fetchall():
            camps.append(Camp(name=row[0], server=row[1], _type =row[2], description=row[3], author=row[4], date=row[5]))
        return camps

        
    def close(self):
        self.connect.close()

