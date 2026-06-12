# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program."
#
# message = ""
# while message != "quit":
#     message = input(prompt)
#     if message != "quit":
#         print(message)

# unconfirmed_users = ['alice','brian','candance']
# confirmed_users = []
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop();
#     print(f"Verifying user: {current_user.title()}")
#     confirmed_users.append(current_user)
#
# print("\nThe following users have been confirmed:")
# for currentConfirmed_user in confirmed_users:
#     print(f"{currentConfirmed_user.title()}")

# pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
# print(pets)
#
# while 'cat' in pets:
#     pets.remove('cat')
# print(pets)

responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name?")
    response = input("Which mountain would you like to climb someday?")
    responses[name] = response
    repeat = input("Would you like to let another person respond?(yes/no)")

    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")

for name,response in responses.items():
    print(f"{name} would like to climb {response}.")
