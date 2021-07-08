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
seat = "b1".upper()


info = Buy(seat=seat, card_type=card_type, card_number=card_number,
           card_cvc=card_cvc, card_holder=card_holder)
export = Pdf(name=name, seat=seat, seat_cost=Buy.seat_cost(info))


if not Buy.seat_taken(info):
    if Buy.valid_card(info):
        Buy.charge_the_card(info)
        Buy.seat_update(info)
        Pdf.create_pdf(export)
        print("Purchase successful!")
    else:
        print("There was a problem with your card!")
else:
    print("Seat is taken!")
