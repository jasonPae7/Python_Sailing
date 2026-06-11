# requested_toppings = []
# if requested_toppings:
#     for topping in requested_toppings:
#         print(f"Adding {topping}")
#     print("\nFinished making your pizza!")
# else:
#     print("Are you sure you want plain pizza?")
from zoneinfo import available_timezones

available_toppings = ['mushrooms','olives','green_peppers','pepperoin','pineapple','extra cheese']
requested_toppings = ['mushrooms','french fries','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry We don't have {requested_topping}.")
print("\nFinished making your pizza!")