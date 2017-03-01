'''this program allows users to manage user names from dictionary'''

from sortedcontainers import SortedDict


def print_menu():
    print('1. Print a user')
    print('2. Add a user')
    print('3. Remove a user')
    print('4. Lookup a user')
    print('5. Quit')
    print()


# Create dictionary with key = Names, value = user_name
user_name = SortedDict()
user_name['Alpha'] = 'Superman'
user_name['Beta'] = 'Batman'
user_name['Gamma'] = 'Spiderman'
user_name['Delta'] = 'Captain America'
user_name['Echo'] = 'Hulk'

menu_choice = 0

print_menu()

while (menu_choice< 5):
    try:
        menu_choice = int(input("Type in a number (1-5); 1:Print the users.2:Add a user.3:Remove a user.4:Lookup a user.5: Quit: "))
    except:
        print("You did not select 1-5")
    else:
        if menu_choice == 1:
            print("Current Users:")
            for x, y in user_name.items():
                print("Name: {} \tUser Name: {} \n".format(x, y))

        # add an entry
        elif menu_choice == 2:
            print("Add User")
            name = input("Name: ")
            username = input("Username: ")
            user_name[name] = username

        # remove an entry
        elif menu_choice == 3:
            print("Remove User")
            input_name = input("Name: ")
            # check if input name in dictionary
            if input_name in user_name:
                del user_name[input_name]

        # view user name
        elif menu_choice == 4:
            print("Lookup User")
            name = input("Name or username: ")
            if name in user_name:
                print(user_name[name])
            else:
                print("User not found.")

        else:
            print_menu()
