def shopping_list():
     return
print(f'Welcome to shopping list system!')
print(f'Please Pick A Operation \n1.View List \n2.Add item \n3.Remove item \n4.Exit \n5.Entire List')
operation = input("Pick a operation Number: ")

while True:
    list = ["hat","shoes","jeans","shirt","socks"]
    if operation == "1":
         print(list[0:5])
         break
    elif operation == "2":
        added_item = input("Add Item For List: ")
        list.append(added_item)
        print(f"Your {added_item} is now in the list!")
    elif operation == "3":
        removed_item = input("What item should be removed?: ")
        list.remove(removed_item)
        for removed_item in list:
            if removed_item not in list:
                print(f'Item not in list, Cannot Be Removed!')
    elif operation == "4":
            print(f'exiting system now.................................. \n Just Playing Seriously Exiting!')
            break
    elif operation == "5":
         print(list)
    else:
        (f'I do not understand function! TRY AGAIN!')

shopping_list()
