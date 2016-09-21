# inventory tracker RPG

player = {"inventory": {"red potion": {'quantity': 20}}}

{
        "red potion": {
              "quantity": 1
         }
}

player_name = input("welcome traveler! what is your name? ")
player["name"] = player_name
print(player)
while True:
    choice = input("would you like to (i)nspect your inventory, or (a)dd to your inventory?\n>")

    if choice == "a":
        item_name = input('what is the item name? ')
        item_quantity = int(input("how many? "))
        player["inventory"][item_name] = {"quantity": item_quantity}
    elif choice == 'i':
        print("looking at inventory")
        for item in player["inventory"].keys():
            quantity = player["inventory"][item]["quantity"]
            print("name{} - {}".format(item, quantity))
