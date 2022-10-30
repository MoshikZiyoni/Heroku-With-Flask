from datetime import timedelta
from xml.sax.handler import all_properties
from flask import Flask, render_template, request, redirect,Blueprint,current_app,session
from app.login import login_required
import sqlite3
import os
from app.read_file_property import read_properties
from app.read_file_project import read_project
from webbrowser import get
from app.test import testfunc
from app.login import auth_bp
con = sqlite3.connect("tutorial.db", check_same_thread=False)
# from app.searchingpro import search, search_proj

# from app.searchingpro import searching
cur = con.cursor()
con.row_factory = sqlite3.Row


app = Flask(__name__)
app.register_blueprint(auth_bp)

app.secret_key = 'asfajkbasdpgou0-31r98t6dshvt'

@app.route("/")
@login_required
def home():
    print(session)
    session['ran'] = '1234'
    print(session.get('username'))
    session.permanent = True
    current_app.permanent_session_lifetime = timedelta(minutes=15)
    # session['username'] = 'admin'
    print(request.cookies)
    # session.pop('username', None)
    return render_template ("index.html")

@app.route("/searchproperty",methods=['POST','GET'])
@login_required
def searchproperty():
    list_of_properties1=search()
    list_of_projects1=search_proj(list_of_properties1)
    # result1=result()
    # test1=testfunc()
    # test1=searching()
    # print(f"filename is:{test1}")

    return render_template ("searchpropertytest.html",list_of_properties=list_of_properties1,list_of_projects=list_of_projects1)


@app.route("/searchpropertyform",methods=['POST','GET'])
@login_required
def searchpropertyform(): 
    
    return render_template ("searchproperty.html")

@app.route ("/login")
def login():
    return render_template("auth.login.html")

# @app.route ("/register")
# def register():
#     return render_template("register.html")
@app.route ("/password")
def password():
    return render_template("password.html")

def search():
    new_list = []
    all_properties=read_properties()
    size_room_input = int(request.form.get('roomnumber'))
    floor_input = int(request.form.get('floor'))
    house_type_input = (request.form.get('house type'))
    square_meter_input = int(request.form.get('square meter'))
    location_input = (request.form.get('city'))
    street_input = (request.form.get('street'))
    price_input = int(request.form.get('price'))
    years = int(request.form.get('years'))
    
    # all_properties = cur.execute(f"SELECT * from Property").fetchall()
    for x in all_properties:
        

        if size_room_input >= x.size_room and floor_input >= x.floor and house_type_input == x.house_type \
                and square_meter_input >= x.square_meter \
                and location_input == x.location and price_input >= x.price and street_input == x.street:
            new_list.append(x)
            
    
        else:
            continue
    return new_list


def search_proj(new_list):
    list_of_related_proj = []
    all_projects = read_project()
    # all_projects = cur.execute(f"SELECT * from Project").fetchall()
    counter2 = 0
    # result2=result()
    years_input = int(request.form.get('years'))
    print()
    print("That's our result...")
    for i in new_list:
        new = i.price
        counter2 += 1
        print()
        found_apt=( i.size_room, 
                i.floor,
                 i.house_type,  i.square_meter, i.location,
                i.street,  i.street_number, i.price, )
        
        print("The projects are:")
        print()
        list_of_related_proj.append({
            'size_room' : new_list[0],
            'floor' : new_list[1],
            'house_type': new_list[2],
            'square_meter': new_list[3],
            'location': new_list[4],
            'street' : new_list[5],
            'street_number': new_list[6],
            'price': new_list[7]

        })
        for t in all_projects:

            our_date = t.dates - 2022
            if years_input >= our_date:
                if t.location == i.location and t.street == i.street and (
                        i.street_number in range(t.street_number - 15,
                                                    t.street_number + 1) or i.street_number in range(
                    t.street_number, t.street_number + 16)):
                    print("Type project:", t.type_project, ",Size of project:", t.size_project, ",Company:",
                            t.company,
                            ",Dates:", t.dates, ",Value:", t.value, ",Location:", t.location, ",Street:",
                            t.street,
                            ",Street number:", t.street_number)
                    new1 = new * t.value
                    new = (new + new1)
                    print("Future price in", our_date, "years for apartment number", counter2, "will be:",
                            new)
                    found_proj="Type project:", t.type_project, ",Size of project:", t.size_project, ",Company:",t.company,",Dates:", t.dates, ",Value:", t.value, ",Location:", t.location, ",Street:",t.street,",Street number:", t.street_number,"Future price in", our_date, "years for apartment number", counter2, "will be:",new
                    
                    list_of_related_proj.append(found_proj)
                else:
                    continue
    return list_of_related_proj 

if __name__ == '__main__':
    app.run(debug=True)