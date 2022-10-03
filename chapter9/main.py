from restaurant import Restaurant
from users import User
from ice_cream_stand import IceCreamStand
from admin import Admin
from electric_car import ElectricCar


"""
9.1 Restaurant: Make an instance called restaurant from your class.
Print the two attributes individually, and then call both methods.
"""

restaurant = Restaurant("Pé de Fava", "Inedible Food")
print(restaurant.restaurant_name, "\n"+restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

"""
9.2 Three Restaurants: Start with your class from Exercise 9.1.
Create three different instances from the class, and call describe_restaurant()
for each instance.
"""
restaurant1 = Restaurant("Pé de Fava", "Inedible Food")
restaurant2 = Restaurant("Bar do Cuscuz", "Gourmetized Food")
restaurant3 = Restaurant("Coco Bamboo", "Expensive Food")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

"""
9.3 Users: Create several instances representing different users, and call both
methods for each user.
"""
user1 = User(
    first_name="Carl",
    last_name="Sagan",
    email="carl@sagan.com",
    age=62)
user2 = User(
    first_name="Neil",
    last_name="Tyson",
    email="neil@tyson.com",
    age=63)
user3 = User(
    first_name="Galileu",
    last_name="Galilei",
    email="galileu@galilei.com",
    age=77)

user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
user3.describe_user()
user3.greet_user()


"""
9.4 Create an instance called restaurant from this class. Print the
number of customers the restaurant has served, and then change this
value and print it again.
"""
restaurant = Restaurant("Pé de Fava", "Inedible Food")
print(restaurant.number_served)
restaurant.number_served = 5
print(restaurant.number_served)

"""
9.4 Call set_number_served() method with a new number and print the value
again.
"""
restaurant.set_number_served(10)
print(restaurant.number_served)

"""
9.4 Call increment_number_served() method with any number you like that could
represent how many customers were served in, say, a day of business.
"""
restaurant.increment_number_served(5)
print(restaurant.number_served)

"""
9.5 Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts(). Print login_attempts
again to make sure it was reset to 0.
"""
user1 = User(
    first_name="Carl",
    last_name="Sagan",
    email="carl@sagan.com",
    age=62)
print(user1.login_attempts)
user1.increment_login_attempts()
user1.increment_login_attempts()
print(user1.login_attempts)

"""
9.6 Create an instance of IceCreamStand, and call the
show_flavors() method.
"""

stand_of_ice_cream = IceCreamStand(
    "Kibon",
    "gelatteria",
    ["pistache", "cocconuts", "chocolate"]
    )

stand_of_ice_cream.show_flavors()

"""
9.7 Create an instance of Admin, and call show_privileges() method.
"""
admin_user = Admin(
    first_name="Carl",
    last_name="Sagan",
    email="carl@sagan.com",
    age=62
    )

# admin_user.show_privileges()

"""
9.8 Create a new instance of Admin and use your method to show its
privileges.
"""
admin_user.privileges.show_privileges()


"""
Make an electric car with default battery size, call get_range() once,
and then call get_range() a second time after upgrading the battery.
You should see an increase in the car's range.
"""


my_tesla = ElectricCar("Tesla", "Model S", 2021)
my_tesla.battery_size.get_range()
my_tesla.battery_size.describe_battery()
my_tesla.battery_size.upgrade_battery()
my_tesla.battery_size.describe_battery()
my_tesla.battery_size.get_range()
