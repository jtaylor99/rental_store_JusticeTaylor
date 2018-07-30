import core
import disk


def rental_rates(rent_dictionary, item_name):
    '''(int,int) -> int
    Returns the rental rates 
    '''
    sales_tax = 0.07 + 1
    price = rent_dictionary[item_name][1] * sales_tax
    replacement_cost = rent_dictionary[item_name][2] * 0.10
    rental_rates = price + replacement_cost
    return rental_rates


def main():
    filename = 'inventory.txt'
    rent_info = disk.open_file()
    rent_dictionary = core.create_rent_dictionary(rent_info)
    print('Welcome to the Rental store!')
    name = input('What\'s your name?:')
    print(f'Hello {name.upper()}')
    user_response = input('Would you like to rent anything?')
    # this is a yes or no question
    if user_response == 'yes':
        print('These is what we have in stock')
        print(rent_dictionary)
    elif user_response == 'no':
        returning = input('What are you returning?:')
        print(f'Thank you for returning {returning} and have a great day')
        exit()
    else:
        print('Please choose a valid option!')
    while True:
        selection = input('Which one would you would like to rent?')
        if selection in rent_dictionary:
            print(f'you have selected {selection}')
            break
        if selection not in rent_dictionary:
            print('please choose a valid option!')
    total = rental_rates(rent_dictionary, selection)
    print('----------------')
    print('Here\'s your receipt')
    print('----------------')
    print(f'total: {total:.2f}')
    print('----------------')
    disk.write_the_history()
    file_string = core.create_file_string(rent_dictionary)
    disk.write_file(file_string)


if __name__ == '__main__':
    main()
