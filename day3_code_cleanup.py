# inventory tracker RPG

player = {}
player_name = input("welcome traveler! what is your name? ")
player["name"] = player_name
print(player)
while True:
    choice = input("would you like to (i)nspect your inventory, or (a)dd to your inventory?\n>")

    if choice == "a":
        print("adding item to inventory")
    elif choice == 'i':
        print("looking at inventory")