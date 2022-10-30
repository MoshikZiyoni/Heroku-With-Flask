from building_profile_func import building_profile


def get_string2(message):
    while True:
        temp = (input(message))
        if len(temp) <= 2:
            print("Error in input")
            continue
        else:
            return temp


def entrance():
    building_profile()
    import time
    file1 = open("passwords and accounts.txt", "r")
    file = file1.readlines()
    my_list = []
    for i in file:
        i = i.split(",")
        str1 = "".join(i[2:])
        str2 = str1.replace("'", "")
        str3 = str2.replace("(", "")
        str4 = str3.replace(")", "")
        str5 = str4.replace(",", "")
        str6 = str5.replace(" ", "")
        str7 = str(str6)
        i = (i[0], i[1], str7[:-1])
        my_list.append(i)

    time.sleep(1)
    print("Loading...")
    time.sleep(1.5)
    print("--LOGIN--")

    email = get_string2("What is the email address ?")
    password = get_string2("What is the password?")

    for i in my_list:
        if email == i[1] and password == i[2]:
            time.sleep(2)
            print(" --- ACCESS GRANTED --- ")
            time.sleep(1)
            print("Uploading Data...")
            time.sleep(2)
            print("Hello", i[0], "!")
            time.sleep(1)
            print("Welcome Back")
            return True
        if email not in i and password not in i:
            continue
        else:
            print("ACCESS DENIED")
            return False
