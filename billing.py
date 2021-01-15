class Food:
    def __init__(self, name, code, rate):
        self.name = name
        self.code = code
        self.rate = rate

    def calculate(self, quantity):
        return self.rate*quantity


hot_coffee = Food("Hot Coffee", 1, 70)
# hot_coffee.setData("Hot Coffee", 1, 70)

cold_coffee = Food("Cold Coffee", 2, 100)
# cold_coffee.setData("Cold Coffee", 2, 100)

cold_coffee_ice = Food("Ice Cold Coffee", 3, 120)
# cold_coffee_ice.setData("Ice Cold Coffee", 3, 120)

french_fries = Food("French Fries", 4, 60)
# french_fries.setData("French Fries", 4, 60)

# pizza = Food()
# sandwich = Food()
# capichino = Food()
# masala_fries= Food()
# ice_cream = Food()
# soda= Food()
print("Welcome To Our Restro")

print("Code         Item                Rate")
print("01           Hot Coffee          70")
print("02           Cold Coffee         100")
print("03           Ice Cold Coffee     120")
print("04           French Fries        60")
print("00           Exit                ")

t = 0
str = ""


run = True
while(run):
    n = int(input(("Please Enter The Code Of Item You will like to have: ")))

    if(n == 1):
        i = int(input(("Number of Items: ")))
        print()
        cost = hot_coffee.calculate(i)
        t = t+cost
        str = str +(f"Hot Coffee        {hot_coffee.rate}            x     {i}         =   {cost}\n")
        
        print(str)
        print(f"Total So far {t}")
        print()

    elif(n == 2):
        i = int(input(("Number of Items: ")))
        print()
        cost = cold_coffee.calculate(i)
        t = t+cost
        str = str+(f"Cold Coffee       {cold_coffee.rate}           x     {i}         =   {cost}\n")
        print(str)
        print(f"Total So far {t}")

        print()

    elif(n == 3):
        i=int(input(("Number of Items: ")))
        print()
        cost = cold_coffee_ice.calculate(i)
        t = t+cost
        str = str+(f"Ice Cold Coffee   {cold_coffee_ice.rate}           x     {i}         =   {cost}\n")
        print(str)
        print(f"Total So far {t}")
        print()

    elif(n == 4):
        i=int(input(("Number of Items: ")))
        print()
        cost = french_fries.calculate(i)
        t = t+cost
        str = str+(f"French Fries      {french_fries.rate}            x     {i}         =   {cost}\n")
        print(str)
        print(f"Total So far {t}")
        print()

    elif(n == 0):
        print(str)
        print(f"Your Toatal Bill Is {t}")
        print("Thank You")
        run = False
    else:
        print("Invalid Code")
