list = ['PreAssignedData', 1, True, 'Alpha123']
print("\n")

def access_list_item():
    while True:
        print("\nSelected Menu: 1. Access List")
        print("Old list: ", list)
        print("Choose an option: \n1. All Data\n2. Index Wise Data\n3. Range Wise Data\n4. Back")
        o = int(input("Option: "))

        if o == 1:
            print("All list data: ", list)
        elif o == 2:
            i = int(input("Enter the index number: "))
            r = list[i]
            print(i, "Index data is: ", r)
        elif o == 3:
            i1 = int(input("Enter the 1st index number: "))
            i2 = int(input("Enter the 1st index number: "))
            r = list[i1:i2]
            print(i1,":",i2, "Index data: ", r)
        elif o == 4:
            choose_an_option()
        
def change_data_of_list():
    while True: 
        print("\nSelected Menu: 2. Change/Replace List Velue")
        print("Old list: ", list)
        i = int(input("Enter index number: "))
        a = input("Please enter replace value: ")
        list[i] = a
        print("New list: ", list)
        print("\n")
        print("Go Back?\n1. Yes\n2. No")
        o = int(input("Option: "))
        if o == 1:
            choose_an_option()
        elif o ==2:
            change_data_of_list()

def add_list_items():
    while True:
        print("\nSelected Menu: 3. Add List Items")
        print("Old list: ", list)
        print("Choose an option: \n1. Append\n2. Insert\n3. Back")
        o = int(input("Option: "))

        if o == 1:
            ap = input("Enter a new value: ")
            list.append(ap)
            print("New list data: ", list)
        elif o == 2:
            i = int(input("Enter index number: "))
            a = input("Please enter new value: ")
            list.insert(i, a)
            print("New list data: ", list )
        elif o == 3:
            choose_an_option()
    
def remove_list_items():
    while True:
        global list
        print("\nSelected Menu: 4. Remove List Items")
        print("Old list: ", list)
        print("Choose an option: \n1. Remove\n2. Pop Without Index\n3. Pop With Index\n4. Clear List\n5. Delete Index\n6. Delete List\n7. Back")
        o = int(input("Option: "))

        if o == 1:
            ap = str(input("Enter a value you want to remove: "))
            list.remove(f'"{ap}"')
            print("New list data: ", list)
        elif o == 2:
            list.pop()
            print("New list data: ", list )
        elif o == 3:
            i = int(input("Enter index number: "))
            list.pop(i)
            print("New list data: ", list )
        elif o == 4:
            list.clear()
            print("New list data: ", list )
        elif o == 5:
            i = int(input("Enter index number: "))
            del list[i]
            print("New list data: ", list )
        elif o == 6:
            del list
            print("New list data: ", list )
        elif o == 7:
            choose_an_option()

def choose_an_option():
    print("\n==== Main Menu =====\nChoose a menu\n1. Access List\n2. Change/Replace List Velue\n3. Add List Items\n4. Remove List Items")
    mo = int(input("Option: "))

    if mo == 1:
        access_list_item()
    elif mo == 2:
        change_data_of_list()
    elif mo == 3:
        add_list_items()
    elif mo == 4:
        remove_list_items()

while True:
    try: 
        choose_an_option()
    except ValueError:
        print("The value you entered was not a number, please enter a integer number")
    
