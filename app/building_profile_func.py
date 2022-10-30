from password_func import new_password


def get_string2(message):
    while True:
        temp = (input(message))
        if len(temp) <= 2:
            print("Error in input")
            continue
        else:
            return temp


def get_string3(message):
    while True:
        temp = (input(message))
        if temp == "no" or temp == "No" or temp == "yes" or temp == "Yes":

            return temp
        else:
            print("Error in input")
            continue


def building_profile():
    question = get_string3("Are you a new user?")
    if question == "yes" or question == "Yes":
        user_name = get_string2("First Name?")
        email = get_string2("Email address?")
        user_password = new_password()
        str_pass = str(user_password)
        if str_pass == "None":
            print("Error")
        else:
            file1 = open("Passwords and accounts.txt", "a")
            file1.write(user_name + "," + email + "," + str_pass + "\n")
            file1.close()
            print("Your new account:", email, user_password)
            return email, user_password, user_name
        if question == "no" or question == "No":
            pass
