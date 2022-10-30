class Property:
    def __init__(self, size_room, floor, house_type, square_meter, location, price, street, street_number):
        self.size_room = int(size_room)
        self.floor = int(floor)
        self.house_type = house_type
        self.square_meter = int(square_meter)
        self.location = location
        self.price = int(price)
        self.street = street
        self.street_number = int(street_number)

    def __str__(self):
        return f"{self.size_room} {self.floor} {self.house_type} {self.square_meter} {self.location} {self.price}" \
               f" {self.street}  {self.street_number}"


    def __repr__(self):
        return self.__str__()


class Property_list:

    def __init__(self):

        self.inventory = []

    def add_property(self, property1):
        self.inventory.append(property1)

    def __str__(self):
        return [self.size_room, self.floor, self.house_type, self.square_meter, self.location ,self.street,self.street_number,self.price]
