class Customers:
    greeting = "Welcome to Coffee Palace"
    def __init__(self, first, beverage, food, total):
        self.first = first
        self.beverage = beverage
        self.food = food
        self.total = total

c_1 = Customers("Nate", "Espresso", "Pastrami on rye", 220)
c_2 = Customers("Elaine", "Strawberry frappucino", "Tuna wrap", 270)
c_3 = Customers("Samirah", "Iced caffe latte", "Cinnamon roll", 225)
c_4 = Customers("Jerry", "Carmel macchiato", "Glazed doughnut", 230)
c_5 = Customers("Paz", "Iced tea", "Blueberry pancakes", 315)

print(Customers.greeting)
print(c_2.first)
print(c_2.beverage)
print(c_2.food)
print(c_2.total)
print(c_4.first)
print(c_4.beverage)
print(c_4.food)
print(c_4.total)
