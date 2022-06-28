import json
from src.flowerbouquet.owner.owner import Owner
from src.flowerbouquet.constants import ROOT_DIR



class Customer:

    def __init__(self):
        pass

    def customer_choice(self):
        owner = Owner()
        print("======= Welcome to the User view ====")
        while (1):
            print("1)Display Flowers")
            print("2)Buy bouquet")
            print("3)Exit")
            print("Enter Your Choice :- ")
            n = int(input())
            if (n == 1):
                owner.display_data()
            elif (n == 2):
                self.buy_bouquet()
            elif (n == 3):
                break
            else:
                print("Invalid Choice...!!!")

    def buy_bouquet(self):
        fd = open(ROOT_DIR, 'r')
        txt = fd.read()
        data = json.loads(txt)
        fd.close()

        price = []
        names = []
        purchase_no = []
        quantity_all = []
        print("Enter Number of different types of flower you want to add :- ")
        n = int(input())
        for i in range(n):
            print("Enter Flower Name " +
                  str(i + 1) + " that you want to buy")
            name = input()
            if name and name in data.keys():
                if (float(data[str(name)]['quantity']) == 0.0):
                    print("Item You Want is Currenty Out Of Stock...!!!")
                    continue
                purchase_no.append(i + 1)
                names.append(data[str(name)])
                print("For Item " + name +
                      " Available Quantity is :- " + str(data[name]['quantity']))
                print("\nEnter Quantity that you want to buy")
                quantity = input()
                if quantity and (float(quantity) <= float(data[name]['quantity'])):
                    data[name]['quantity'] = str(
                        float(data[name]['quantity']) - float(quantity))
                    quantity_all.append(quantity)
                    price.append(data[name]['price'])
                else:
                    print(
                        "The Quantity You Have Asked is Quite High Than That is Available")
                    print(
                        "Did you Want To buy According to The Quantity Available then Enter '0' Else '1'\
                        to skip This Item")
                    key = int(input())
                    if (key == 0):
                        print("Enter Quantity of Item " +
                              str(i + 1) + " that you want to buy")
                        quantity = input()
                        if (float(quantity) <= float(data[name]['quantity'])):
                            data[name]['quantity'] = str(
                                float(data[name]['quantity']) - float(quantity))
                            quantity_all.append(quantity)
                            price.append(data[name]['price'])
                        else:
                            print("Invalid Operation Got Repeated...!!!")
                    elif (key == 1):
                        continue
                    else:
                        print("Invalid Choice...!!!")
            else:
                print("Invalid Item ID...!!!")
        if (len(purchase_no) != 0):
            self.generate_bill(price, purchase_no,quantity_all)
        js = json.dumps(data)
        fd = open(ROOT_DIR, 'w')
        fd.write(js)
        fd.close()

    def generate_bill(self,price, purchase_no,quantity_all):
        print("========= Bill ========")
        amount = 0
        n = len(purchase_no)

        for i in range(n):
            print("-----------------------------------------")
            amount = amount + float(price[i]) * float(quantity_all[i])
            print("Purchase number", purchase_no[i],
                  "\nPrice of per flower :-", price[i],
                  "\nPurchase Quantity :-", quantity_all[i])
        print(" Total Payable Bill :-",
              amount)
        print("***************************************")