import sqlite3
from webbrowser import get
from flask import request
con = sqlite3.connect("tutorial.db", check_same_thread=False)
cur = con.cursor()

# def result():
#     roomnumber = request.form.get('roomnumber')
#     floor = request.form.get('floor')
#     house_type = request.form.get('house type')
#     square_meter = request.form.get('square meter')
#     city = request.form.get('city')
#     street = request.form.get('street')
#     price = request.form.get('price')
#     years = request.form.get('years')
    


#     # end_result=cur.execute(f"SELECT Property.streetID, Project.streetID FROM Property INNER JOIN Project ON Property.streetID = Project.streetID;")
#     return roomnumber,floor,house_type,square_meter,city,street,price,years


# def searching():
    # from read_file_property import read_properties
    # from read_file_project import read_project



    # from entrance_func import entrance

counter = 5

def get_int(message):
    while True:
        try:
            temp = int(message)
            return temp
        except:
            print("Error in input")

def get_string(message):
    while True:
        temp = str(message)
        if temp == "apartment" or temp == "house":
            return temp

        else:
            print("Error in input")

def get_string1(message):
    while True:
        temp = (message)
        if len(temp) <= 2:
            print("Error in input")
        else:
            return temp

# for i in range(5):
#     counter -= 1
    # if entrance() == True:





# def search():
   
#     new_list = []
#     size_room_input = get_int(request.form.get('roomnumber'))
#     floor_input = get_int(request.form.get('floor'))
#     house_type_input = get_string(request.form.get('house type'))
#     square_meter_input = get_int(request.form.get('square meter'))
#     location_input = get_string1(request.form.get('city'))
#     street_input = get_string1(request.form.get('street'))
#     price_input = get_int(request.form.get('price'))
#     years = get_int(request.form.get('years'))
    
#     # all_properties = cur.execute(f"SELECT * from Property").fetchall()
#     for x in all_properties:
        

#         if size_room_input >= x.size_room and floor_input >= x.floor and house_type_input == x.house_type \
#                 and square_meter_input >= x.square_meter \
#                 and location_input == x.location and price_input >= x.price and street_input == x.street:
#             new_list.append(x)
            
    
#         else:
#             continue
#     return new_list
        
# all_properites = cur.execute(f"SELECT * from Property").fetchall()
# search(all_properties)
# all_projects = cur.execute(f"SELECT * from Project").fetchall()

# def search_proj(new_list):
#     all_projects = cur.execute(f"SELECT * from Project").fetchall()
#     counter2 = 0
#     # result2=result()
#     years_input = get_int(request.form.get('years'))
#     print()
#     print("That's our result...")
#     for i in new_list:
#         new = i.price
#         counter2 += 1
#         print()
#         print("Apartment number:", "(", counter2, ")", "-->>", "Size room:", i.size_room, ",Floor:",
#                 i.floor,
#                 ",Property type:", i.house_type, ",Square meter:", i.square_meter, ",Location:", i.location,
#                 ",Street:",
#                 i.street, ",Street number:", i.street_number, ",Price:", i.price, )
#         print("The projects are:")
#         print()
#         for t in all_projects:

#             our_date = t.dates - 2022
#             if years_input >= our_date:
#                 if t.location == i.location and t.street == i.street and (
#                         i.street_number in range(t.street_number - 15,
#                                                     t.street_number + 1) or i.street_number in range(
#                     t.street_number, t.street_number + 16)):
#                     print("Type project:", t.type_project, ",Size of project:", t.size_project, ",Company:",
#                             t.company,
#                             ",Dates:", t.dates, ",Value:", t.value, ",Location:", t.location, ",Street:",
#                             t.street,
#                             ",Street number:", t.street_number)
#                     new1 = new * t.value
#                     new = (new + new1)
#                     print("Future price in", our_date, "years for apartment number", counter2, "will be:",
#                             new)
#                 else:
#                     continue

# search_proj(all_projects, new_list)

        # break
    # else:
    #     print("Error,you have:", counter, "attempts left to login")
    #     print("Try again with your correct details")


