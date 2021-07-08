from backend import *
from create_pdf import *

# name = input("Your full name: ").title()
# seat = input('Preferred seat number: ').upper()
# card_type = input('Your card type: ').capitalize()
# card_number = input('Your card number: ')
# card_cvc = input('Your card cvc: ')
# card_holder = input('Card holder name: ').title()

name = "John smith".title()
card_type = "visa".capitalize()
card_number = "12345678"
card_cvc = "123"
card_holder = "John Smith".title()
seat = "b3".upper()


if not seat_taken(seat):
    if valid_card(card_type, card_number, card_cvc, card_holder):
        charge_the_card(card_number, seat)
        seat_update(seat)
        create_pdf(name, seat, seat_cost(seat))
        print("Purchase successful!")
    else:
        print("There was a problem with your card!")
else:
    print("Seat is taken!")
