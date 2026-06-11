# requested_toppings = []
# if requested_toppings:
#     for topping in requested_toppings:
#         print(f"Adding {topping}")
#     print("\nFinished making your pizza!")
# else:
#     print("Are you sure you want plain pizza?")
from zoneinfo import available_timezones

# available_toppings = ['mushrooms','olives','green_peppers','pepperoin','pineapple','extra cheese']
# requested_toppings = ['mushrooms','french fries','extra cheese']
# for requested_topping in requested_toppings:
#     if requested_topping in available_toppings:
#         print(f"Adding {requested_topping}.")
#     else:
#         print(f"Sorry We don't have {requested_topping}.")
# print("\nFinished making your pizza!")

user_list = ['Joy','Mike','Admin','Peter']
del user_list[:len(user_list)]
if user_list:
    for user in user_list:
        if user == 'Admin':
            print("Would you like to see a status report?")
        else:
            print(f"Hello,{user} happy to login.")
else:
    print("We need to find some users.")
