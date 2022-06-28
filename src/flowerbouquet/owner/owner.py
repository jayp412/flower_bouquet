import json
from src.flowerbouquet.constants import ROOT_DIR


class Owner:

    def __init__(self):
        with open(ROOT_DIR) as f:
            self.current_available=json.load(f)
            print("\n\n self.current_available",self.current_available)

    def owner(self):
        print("========Welcome to the owner Dashboard==============")
        while (1):
            print("1)Display Flowers")
            print("2)Insert New Item")
            print("3)Update Item")
            print("4)Delete Item")
            print("5)Exit")
            print("Enter Your Choice :- ")
            n = int(input())
            if (n == 1):
                self.display_data()
            elif (n == 2):
                self.add_new()
            elif (n == 3):
                self.update_flower_data()
            elif (n == 4):
                self.delete_item()
            elif (n == 5):
                break
            else:
                print("Invalid Choice...!!!")


    def display_data(self):
        print(self.current_available)
        # fd = open("data.json", 'r')
        # txt = fd.read()
        # data = json.loads(txt)
        # print("\n\n data", data)
        # fd.close()


    def add_new(self):
        fd = open(ROOT_DIR, 'r')
        txt = fd.read()
        data = json.loads(txt)
        fd.close()
        print("Enter New Item Name :- ")
        name = input()

        if name not in data.keys():
            print("Enter Price of Item(price for flower quantity as 1) :- ")
            price = input()
            print("Enter Quantity of Item :- ")
            quantity = input()
            data[name] = {'price': price,
                          'quantity': quantity, }
        else:
            print("The Flower Name you Have Entered Is\
                Already Exist Please Check...!!!")
        js = json.dumps(data)
        fd = open(ROOT_DIR, 'w')
        fd.write(js)
        fd.close()


    def delete_item(self):
        fd = open(ROOT_DIR, 'r')
        txt = fd.read()
        data = json.loads(txt)
        fd.close()
        print("Enter The flower name To Delete :- ")
        temp = input()
        if temp in data.keys():
            data.pop(temp)  # here we are removing that particular data
            print("flower name " + str(temp) + " Deleted Successfully...!!!")
        else:
            print("Invalid flower name...!!!")
        js = json.dumps(data)
        fd = open(ROOT_DIR, 'w')
        fd.write(js)
        fd.close()


    def update_flower_data(self):
        fd = open(ROOT_DIR, 'r')
        txt = fd.read()
        data = json.loads(txt)
        fd.close()
        print("Enter The flower name Which You Want To Update :- ")
        temp = input()

        if temp in data.keys():
            print("Want to update whole item press '0' else '1' for specific data :- ")
            q = int(input(">>>>"))

            if (q == 0):
                print("Enter Flower Name :- ")
                name = input()
                print("Enter Price of flower(price for quantity as 1) :- ")
                price = input()
                print("Enter Quantity of Item :- ")
                quantity = input()
                data[temp] = {'price': price, 'quantity': quantity, }
                print("Please Press '1' to Continue :- ")

            elif (q == 1):
                print("Enter Which Attribute of Item You want to Update :- ")
                p = input()

                if p in data[temp].keys():
                    print("Enter " + str(p) + " of Flower :- ")
                    u = input()
                    data[temp][p] = u
                    print("Flower " + str(temp) + "'s attribute " +
                          str(p) + " is Updated Successfully...!!!")
                else:
                    print("Invalid Attribute...!!!")
            else:
                print("Invalid Choice...!!!")
        else:
            print("Invalid Name...!!!")
        js = json.dumps(data)
        fd = open(ROOT_DIR, 'w')
        fd.write(js)
        fd.close()