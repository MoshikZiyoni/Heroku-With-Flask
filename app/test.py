import sqlite3
from webbrowser import get
con = sqlite3.connect("tutorial.db", check_same_thread=False)
cur = con.cursor()

def testfunc():
    MMM=cur.execute(f"SELECT * from Property").fetchall()
    return MMM

