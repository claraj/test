""" A program for looking up a country's name from a country code. """

import country_api 

def main():
    while True:

        code = input('Enter the 2-letter country code or press enter to quit ')

        if code == '':
            print('Bye!')
            break

        if len(code) != 2:
            print('The country code must be two letters')
            continue

        found, name, error = country_api.get_country_name(code)

        if found:
            print(f'{code} is the country code for {name}')
        elif not found and not error:
            print('No country found for that code')
        else:
            print('Error fetching data')
        

main()
