def new_password():
    while True:
        import random
        number1 = random.randint(1, 11)
        number = str(number1)
        letter = ["a", "b", "d", "e", "f", "g", "h", "i", "j"]
        capital_leter = ["A", "B", "D", "E", "F", "G", "H", "I", "J"]
        symb = ["!", "@", "#", "$"]
        random.shuffle(capital_leter)
        random.shuffle(letter)
        random.shuffle(symb)

        user = input("Do you want a new password?")
        if user == "yes" or user == "Yes":
        # if user == "no" or user == "No":
            question = input("Do you want a strong password?")

            if question == "yes" or question == "Yes":

                password = number, capital_leter[0], letter[0], symb[0], number, capital_leter[1], letter[1], symb[1]
                print(password)

                print("Your strong password:", password)
                question2 = input("Would you like to save password?")
                if question2 == "yes" or question2 == "Yes":
                    print("--Password Created--")

                    final_password = password
                    return final_password
                else:
                    continue

            elif question == "no" or question == "No":

                password = (number, capital_leter[0], letter[0], symb[0])
                print(password)

                question2 = input("Would you like to save password?")
                if question2 == "yes":
                    print("--Password Created--")
                    return password

                elif question2 == "no" or question2 == "No":
                    continue
            else:
                print("Not Recognized")
        if user == "no" or user == "No":
            print("Chosen to stop")
            break
        else:
            print("not recognized")
