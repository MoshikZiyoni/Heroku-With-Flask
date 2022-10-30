from datetime import timedelta
import os
import sqlite3
from flask import Blueprint, Flask, current_app, render_template, request, redirect, session, url_for
from login import login_required
from webbrowser import get
app = Flask(__name__)

con = sqlite3.connect("tutorial.db", check_same_thread=False)
cur = con.cursor()




cur.execute("create table IF NOT EXISTS Property (room size,desiered floor,property type,square meter,city,price,streetID,street_number)")
cur.execute("create table IF NOT EXISTS Project (project_type,project_size,company,dates,value,city,streetID,street_number)")
cur.execute("CREATE TABLE IF NOT EXISTS user (id INTEGER  PRIMARY KEY AUTOINCREMENT , username UNIQUE, password,petname)")


with open("Property-file.csv") as property_file:
    property_file.readline()
    property_file1 = property_file.readlines()
    for i in property_file1:
        i = i.strip()
        temp = i.split(",")
        cur.execute (f"insert into Property values ('{temp[0]}', '{temp[1]}', '{temp[2]}', '{temp[3]}', '{temp[4]}', '{temp[5]}', '{temp[6]}', '{temp[7]}')")
        con.commit()

with open("Project-file.csv") as project_file:
    project_file.readline()
    project_file1 = project_file.readlines()
    for i in project_file1:
        i = i.strip()
        temp = i.split(",")
        cur.execute (f"insert into Project values ('{temp[0]}', '{temp[1]}', '{temp[2]}', '{temp[3]}', '{temp[4]}', '{temp[5]}', '{temp[6]}', '{temp[7]}')")
        con.commit()
app.secret_key = 'asfajkbasdpgou0-31r98t6dshvt'

@app.route("/")
def main():
    return redirect(url_for('home'))
if __name__ == "__main__":
    app.run(debug=True)


        # מה שאמור להיות בסוף
# cur.execute(f"SELECT Property.streetID, Project.streetID FROM Property INNER JOIN Project ON Property.streetID = Project.streetID;")
