# Based in bookStore.py flowchart (./assets/bookStore_flowchart.pdf)

bookTitle = input('Insert book title: ')
bookISBN = input('Insert book ISBN: ')
bookPrice = input('Insert book price (in USD): ')
bookShip = input('Is shipment free of charge? ')
if bookShip == 'Y' or bookShip == 'y' or bookShip == 'Yes' or bookShip == 'yes' or bookShip == 'YES':
    bookShip = 'Free'
else:
    bookShip = 'Non free'

# Triple apostrophe is used to declare a multi-line string

print(f'''Book name: {bookTitle}
ISBN: {bookISBN}
Price: {bookPrice} USD
Shipment: {bookShip}
''')

# To be complemented
