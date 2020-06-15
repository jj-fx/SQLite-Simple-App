def command_line_input():
    name = ''
    address = ''
    phone_number = '999 999 999'

    try:
        name = str(input('Name: '))
    except ValueError:
        name = 'Jeffrey Epstein'

    try:
        address = str(input('Address: '))
    except ValueError:
        address = '666 Hells Pass Rd'

    try:
        phone_number = str(input('Phone Number: '))
    except ValueError:
        phone_number = '000 000 000'

    return [name, address, phone_number]


if __name__ == '__main__':
    command_line_input()
