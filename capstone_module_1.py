############################################################# Database, Functions, Placeholders #############################################################

# Login credentials
credentials = [
    ['admin1','12345678'],
    ['admin2','87654321']
]

# Login function
def login(username, password):
    for cred in credentials:
        if cred[0] == username and cred[1] == password:
            return 1
    return 0

# Contact database
registries = [
    ['Abdul','Bandung','Jalan Kacapiring',6281312345678],
    ['Aziz','Jakarta','Jalan Sudirman',6282298765432],
    ['Purwa','Jakarta','Jalan Swadarma',6285643215678],
    ['Dhika','Yogyakarta','Jalan Diponegoro',6288834561237]
]

# Search contact function
def find_contact(var, user_input):
    for fcont in registries:
        if user_input in str(fcont[var]):
            return fcont
        else:
            print(f'Cannot find {user_input}. Please try again.')

        

    
# To show registries
def reg_header():
    print('Index\t |Name\t |City\t\t |Address\t\t |Phone Number')

def show_reg():
    for i in range(len(registries)):
        print('{}\t |{}\t |{}\t |{}\t |{}'.format(i,registries[i][0], registries[i][1], registries[i][2], registries[i][3]))

# Validation and error message in add/edit contact function
def validate(prompt, validation, error_message):
    while True:
        user_input = input(prompt)
        if validation(user_input):
            return user_input
        else:
            print (error_message)  

# Message if process is canceled
def cancel_msg():
    print('Process canceled.')

# Message if selecting outside of options
def error_msg(error_message):
    print(f'Sorry, {error_message} is not on the list. Please select one of the available options.')

############################################################# Login Page #############################################################

login_attempt = int()
print('Welcome to The Contact Book - Please login to your account.')

while True:
    username_input = validate('Username: ', lambda x: x !='', 'Username cannot be blank.')
    password_input = validate('Password: ', lambda x: x !='', 'Password cannot be blank.')
   
    login_result = login(username_input, password_input)
    
    if login_attempt == 3:
        print('You failed too many times. Please contact your Admin.')
        break

    if login_result == 0:
        login_attempt += 1 
        print(f'Username or Password is invalid. Please try again. (Remaining attempt: {4 - login_attempt})')
        continue

############################################################# Main Menu #############################################################

    elif login_result == 1:
        print(f'Login Successful. Welcome back, {username_input}!')
        reg_header()
        show_reg()

        while True :
            next_step = input('''
            What would you like to do?
            1. Add a New Contact
            2. Delete a Contact
            3. Edit a Contact
            4. Find contacts                  
            5. Log Out
            
            Please input the option you would like to choose: ''')

            if next_step == '5':
                print('You are logged out.')
                break

############################################################# Menu 1 - Add New Contact #############################################################

            elif next_step == '1':
                input_name = validate('Please enter the name (fill with x to cancel).: ', lambda x: x != '', 'Name cannot be blank.')
                if input_name == 'x':
                    cancel_msg()
                    reg_header()
                    show_reg()
                    continue
                input_city = validate('Please enter the city of residence (fill with x to cancel).: ', lambda x: x != '', 'City cannot be blank.')
                if input_city == 'x':
                    cancel_msg()
                    reg_header()
                    show_reg()
                    continue
                input_address = validate('Please enter the address (fill with x to cancel).: ', lambda x: x != '', 'Address cannot be blank.')
                if input_address == 'x':
                    cancel_msg()
                    reg_header()
                    show_reg()
                    continue
                input_number = validate('Please enter the number (fill with 0 to cancel).: ', lambda x: x.isdigit(), 'Please fill in with number.') 
                if input_number == '0':
                    cancel_msg()
                    reg_header()
                    show_reg()
                    continue 
                
                print('You are about to add the following contact:')
                reg_header()
                print('{}\t |{}\t |{}\t |{}\t |{}'.format(len(registries), input_name, input_city, input_address, input_number))
                
                add_confirmation = validate('Enter Y to proceed or X to cancel: ', lambda x: x != '', 'Please select an option.')
                if add_confirmation == 'x':
                    cancel_msg()
                    reg_header()
                    show_reg()
                    continue
                
                registries.append([input_name, input_city, input_address, input_number])
                print('Updated registries: ')
                reg_header()
                show_reg()

############################################################# Menu 2 - Removing Contact #############################################################
            
            elif next_step == '2':
                while True:
                    index_contact_str = input('Please select the index of the contact you would like to delete (fill with x to cancel): ')
                    if index_contact_str.isdigit():
                        index_contact = int(index_contact_str)
                        if 0 <= index_contact < len(registries):
                            print('You are about to delete the following contact: ')
                            reg_header()
                            print('{}\t |{}\t |{}\t |{}\t |{}'.format(index_contact, registries[index_contact][0], registries[index_contact][1], registries[index_contact][2], registries[index_contact][3]))
                            del_confirmation = validate('Enter Y to proceed or X to cancel: ', lambda x: x != '', 'Please select an option.')
                            break
                        else:
                            error_msg(index_contact)
                            reg_header()
                            show_reg()
                    elif index_contact_str == 'x':
                        del_confirmation = 'x'
                        break
                    elif index_contact_str == '':
                            print('You have not chosen any index. Please try again.')
                            continue
                    else:
                        error_msg(index_contact_str)
                        reg_header()
                        show_reg()

                if del_confirmation == 'x':
                    cancel_msg()
                    reg_header()
                    show_reg()
                    continue

                else: 
                    del registries[index_contact]
                    print('Updated Registries: ')
                    reg_header()
                    show_reg()

############################################################# Menu 3 - Edit Contact #############################################################

            elif next_step == '3':
                edit_name = ()
                edit_city = ()
                edit_address = ()
                edit_number = ()
                while True:
                    if (edit_name or edit_number or edit_address == 'x') or (edit_number == '0'):
                        break
                    else:
                        index_contact_str = input('Please select the index of the contact you would like to edit (fill with x to cancel): ')
                        if index_contact_str.isdigit():
                            index_contact = int(index_contact_str)
                            if 0 <= index_contact < len(registries):
                                reg_header()
                                print('{}\t |{}\t |{}\t |{}\t |{}'.format(index_contact, registries[index_contact][0], registries[index_contact][1], registries[index_contact][2], registries[index_contact][3]))
                                edit_menu = input('''
                                What would you like to edit:
                                1. All Values
                                2. Name
                                3. City
                                4. Address
                                5. Number
                                6. Cancel                                                       
                                                      
                                Please select one of the option: ''')

                                if edit_menu == '1':
                                    edit_name = validate('Please enter the new name (fill with x to cancel).: ', lambda x: x != '', 'Name cannot be blank.')
                                    if edit_name == 'x':
                                        cancel_msg()
                                        reg_header()
                                        show_reg()
                                        continue
                                    edit_city = validate('Please enter the new city (fill with x to cancel).: ', lambda x: x != '', 'City cannot be blank.')
                                    if edit_city == 'x':
                                        cancel_msg()
                                        reg_header()
                                        show_reg()
                                        continue
                                    edit_address = validate('Please enter the new address (fill with x to cancel).: ', lambda x: x != '', 'Address cannot be blank.')
                                    if edit_address == 'x':
                                        cancel_msg()
                                        reg_header()
                                        show_reg()
                                        continue
                                    edit_number = validate('Please enter the new number (fill with 0 to cancel).: ', lambda x: x.isdigit(), 'Please fill in with number.')
                                    if edit_number == '0':
                                        cancel_msg()
                                        reg_header()
                                        show_reg()
                                        continue
                        
                                    print('Please confirm the changes:')
                                    print('Old Values:')
                                    reg_header()
                                    print('{}\t |{}\t |{}\t |{}\t |{}'.format(index_contact, registries[index_contact][0], registries[index_contact][1], registries[index_contact][2], registries[index_contact][3]))
                                    print('New Values:')
                                    reg_header()
                                    print('{}\t |{}\t |{}\t |{}\t |{}'.format(index_contact, edit_name, edit_city, edit_address, edit_number))

                                    edit_confirmation = validate('Enter Y to proceed or X to cancel: ', lambda x: x != '', 'Please select an option.')
                                    if edit_confirmation == 'x':
                                        cancel_msg()
                                        reg_header()
                                        show_reg()
                                        continue

                                    else:
                                        registries[index_contact][0] = edit_name
                                        registries[index_contact][1] = edit_city
                                        registries[index_contact][2] = edit_address
                                        registries[index_contact][3] = edit_number 
                                        print('Updated registries: ')
                                        reg_header()
                                        show_reg()
                                
                                elif edit_menu == '2':
                                    edit_name = validate('Please enter the new name (fill with x to cancel).: ', lambda x: x != '', 'Name cannot be blank.')
                                    if edit_name == 'x':
                                        cancel_msg()
                                        reg_header()
                                        show_reg()
                                        continue
                                    print('Please confirm the changes:')
                                    print('Old Values:')
                                    reg_header()
                                    print('{}\t |{}\t |{}\t |{}\t |{}'.format(index_contact, registries[index_contact][0], registries[index_contact][1], registries[index_contact][2], registries[index_contact][3]))
                                    print('New Values:')
                                    reg_header()
                                    print('{}\t |{}\t |{}\t |{}\t |{}'.format(index_contact, edit_name, registries[index_contact][1], registries[index_contact][2], registries[index_contact][3]))

                                    edit_confirmation = validate('Enter Y to proceed or X to cancel: ', lambda x: x != '', 'Please select an option.')
                                    if edit_confirmation == 'x':
                                        cancel_msg()
                                        reg_header()
                                        show_reg()
                                        continue
                                    else:
                                        registries[index_contact][0] = edit_name
                                        print('Updated registries: ')
                                        reg_header()
                                        show_reg()
                                
                                elif edit_menu == '3':
                                    edit_city = validate('Please enter the new city (fill with x to cancel).: ', lambda x: x != '', 'City cannot be blank.')
                                    if edit_city == 'x':
                                        cancel_msg()
                                        reg_header()
                                        show_reg()
                                        continue
                                    print('Please confirm the changes:')
                                    print('Old Values:')
                                    reg_header()
                                    print('{}\t |{}\t |{}\t |{}\t |{}'.format(index_contact, registries[index_contact][0], registries[index_contact][1], registries[index_contact][2], registries[index_contact][3]))
                                    print('New Values:')
                                    reg_header()
                                    print('{}\t |{}\t |{}\t |{}\t |{}'.format(index_contact, registries[index_contact][0], edit_city, registries[index_contact][2], registries[index_contact][3]))

                                    edit_confirmation = validate('Enter Y to proceed or X to cancel: ', lambda x: x != '', 'Please select an option.')
                                    if edit_confirmation == 'x':
                                        cancel_msg()
                                        reg_header()
                                        show_reg()
                                        continue
                                    else:
                                        registries[index_contact][1] = edit_city
                                        print('Updated registries: ')
                                        reg_header()
                                        show_reg()
                                
                                elif edit_menu == '4':
                                    edit_address = validate('Please enter the new address (fill with x to cancel).: ', lambda x: x != '', 'address cannot be blank.')
                                    if edit_address == 'x':
                                        cancel_msg()
                                        reg_header()
                                        show_reg()
                                        continue
                                    print('Please confirm the changes:')
                                    print('Old Values:')
                                    reg_header()
                                    print('{}\t |{}\t |{}\t |{}\t |{}'.format(index_contact, registries[index_contact][0], registries[index_contact][1], registries[index_contact][2], registries[index_contact][3]))
                                    print('New Values:')
                                    reg_header()
                                    print('{}\t |{}\t |{}\t |{}\t |{}'.format(index_contact, registries[index_contact][0], registries[index_contact][1], edit_address, registries[index_contact][3]))

                                    edit_confirmation = validate('Enter Y to proceed or X to cancel: ', lambda x: x != '', 'Please select an option.')
                                    if edit_confirmation == 'x':
                                        cancel_msg()
                                        reg_header()
                                        show_reg()
                                        continue
                                    else:
                                        registries[index_contact][2] = edit_address
                                        print('Updated registries: ')
                                        reg_header()
                                        show_reg()

                                elif edit_menu == '5':
                                    edit_number = validate('Please enter the new number (fill with 0 to cancel).: ', lambda x: x.isdigit(), 'Please fill in with number.')
                                    if edit_number == '0':
                                        cancel_msg()
                                        reg_header()
                                        show_reg()
                                        continue
                                    print('Please confirm the changes:')
                                    print('Old Values:')
                                    reg_header()
                                    print('{}\t |{}\t |{}\t |{}\t |{}'.format(index_contact, registries[index_contact][0], registries[index_contact][1], registries[index_contact][2], registries[index_contact][3]))
                                    print('New Values:')
                                    reg_header()
                                    print('{}\t |{}\t |{}\t |{}\t |{}'.format(index_contact, registries[index_contact][0], registries[index_contact][1], edit_address, registries[index_contact][3]))

                                    edit_confirmation = validate('Enter Y to proceed or X to cancel: ', lambda x: x != '', 'Please select an option.')
                                    if edit_confirmation == 'x':
                                        cancel_msg()
                                        reg_header()
                                        show_reg()
                                        continue
                                    else:
                                        registries[index_contact][3] = edit_number
                                        print('Updated registries: ')
                                        reg_header()
                                        show_reg()
                                
                                elif edit_menu == '':
                                    print('You have not chosen any option. Please try again.')
                                    

                                else:
                                    error_msg(edit_menu)
                                    reg_header()
                                    show_reg()
                                    
                            else:
                                error_msg(index_contact)
                                reg_header()
                                show_reg()

                        elif index_contact_str == 'x':
                            cancel_msg()
                            reg_header()
                            show_reg()
                            break
                        
                        elif index_contact_str == '':
                            print('You have not chosen any index. Please try again.')
                            continue

                        else:
                            error_msg(index_contact_str)
                            reg_header()
                            show_reg()
############################################################# Menu 4 - Find Contacts #############################################################

            elif next_step == '4':
                while True:
                    index_contact_str = validate('Please enter the index you would like to find (fill with x to cancel).: ', lambda x: x != '', 'You have not choosen any index.')
                    if index_contact_str == 'x':
                        cancel_msg()
                        reg_header()
                        show_reg()
                        break
                    if index_contact_str.isdigit():
                        index_contact = int(index_contact_str)
                        if 0 <= index_contact < len(registries):
                            reg_header()
                            print('{}\t |{}\t |{}\t |{}\t |{}'.format(index_contact, registries[index_contact][0], registries[index_contact][1], registries[index_contact][2], registries[index_contact][3]))
                        else:
                            error_msg(index_contact)
                            print(f'(Available index is 0 until {len(registries)-1})')
                            continue
                    else:
                        error_msg(index_contact_str)
                        print(f'(Available index is 0 until {len(registries)-1})')
                        continue
                
############################################################# Main Menu Error #############################################################
            elif next_step == '':
                print('You have not chosen any option. Please try again.')
                reg_header()
                show_reg()
            else:
                error_msg(next_step)
                reg_header()
                show_reg()
            
            