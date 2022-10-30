from app.property import Property, Property_list

house_list = Property_list()


def read_properties():
    property_list = []

    with open("Property-file.csv") as property_file:
        property_file.readline()
        property_file1 = property_file.readlines()
        for i in property_file1:
            i = i.strip()
            temp = i.split(",")
            property = Property(temp[0], temp[1], temp[2], temp[3], temp[4], temp[5], temp[6], temp[7])
            property_list.append(property)
    for p in property_list:
        return property_list
