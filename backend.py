import sqlite3


def seat_taken(seat):
    """Check if seat is taken or not"""
    connection = sqlite3.connect('cinema.db')
    cursor = connection.cursor()
    cursor.execute("""
            SELECT "seat_id", "taken" FROM "Seat" WHERE "seat_id" = ?
            """, [seat])
    result = cursor.fetchall()
    connection.close()

    if result == [(seat, 0)]:
        return False
    elif result == [(seat, 1)]:
        return True


def seat_cost(seat):
    """Get the cost of the seat"""
    connection = sqlite3.connect('cinema.db')
    cursor = connection.cursor()
    cursor.execute("""
        SELECT "price" FROM "Seat" WHERE "seat_id" == ?
        """, [seat])
    result = cursor.fetchall()[0][0]
    connection.close()

    return result


def seat_update(seat):
    """Set seat to taken"""
    connection = sqlite3.connect('cinema.db')
    connection.execute("""
        UPDATE "Seat" SET "taken"=1 WHERE "seat_id" = ?
        """, [seat])
    connection.commit()
    connection.close()


def valid_card(card_type, number, cvc, holder):
    """Check if the card is valid in database"""
    result = _read_card_db()
    for i in result:
        if card_type in i:
            if number in i:
                if cvc in i:
                    if holder in i:
                        return True

    return False


def _read_card_db():
    """Read entire card database"""
    connection = sqlite3.connect('banking.db')
    cursor = connection.cursor()
    cursor.execute("""
            SELECT * FROM "Card"
            """)
    result = cursor.fetchall()
    connection.close()

    return result


def card_balance(number):
    """Check card balance"""
    connection = sqlite3.connect('banking.db')
    cursor = connection.cursor()
    cursor.execute("""
        SELECT "balance" FROM "Card" WHERE "number" == ?
        """, [number])
    result = cursor.fetchall()[0][0]
    connection.close()

    return result


def charge_the_card(number, seat):
    """Charge the card of the seat cost"""
    balance = card_balance(number)
    cost = seat_cost(seat)
    updated_balance = balance - cost

    connection = sqlite3.connect('banking.db')
    connection.execute("""
    UPDATE "Card" SET "balance"=? WHERE "number"=?
    """, [updated_balance, number])
    connection.commit()
    connection.close()
