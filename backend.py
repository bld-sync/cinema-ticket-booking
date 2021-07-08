import sqlite3


class Buy:
    def __init__(self, seat, card_type, card_number, card_cvc, card_holder):
        self.seat = seat
        self.card_type = card_type
        self.card_number = card_number
        self.card_cvc = card_cvc
        self.card_holder = card_holder

    def seat_taken(self):
        """Check if seat is taken or not"""
        connection = sqlite3.connect('cinema.db')
        cursor = connection.cursor()
        cursor.execute("""
                SELECT "seat_id", "taken" FROM "Seat" WHERE "seat_id" = ?
                """, [self.seat])
        result = cursor.fetchall()
        connection.close()

        if result == [(self.seat, 0)]:
            return False
        elif result == [(self.seat, 1)]:
            return True

    def seat_cost(self):
        """Get the cost of the seat"""
        connection = sqlite3.connect('cinema.db')
        cursor = connection.cursor()
        cursor.execute("""
            SELECT "price" FROM "Seat" WHERE "seat_id" == ?
            """, [self.seat])
        result = cursor.fetchall()[0][0]
        connection.close()

        return result

    def seat_update(self):
        """Set seat to taken"""
        connection = sqlite3.connect('cinema.db')
        connection.execute("""
            UPDATE "Seat" SET "taken"=1 WHERE "seat_id" = ?
            """, [self.seat])
        connection.commit()
        connection.close()

    def valid_card(self):
        """Check if the card is valid in database"""
        result = self._read_card_db()
        for i in result:
            if self.card_type in i:
                if self.card_number in i:
                    if self.card_cvc in i:
                        if self.card_holder in i:
                            return True

        return False

    def _read_card_db(self):
        """Read entire card database"""
        connection = sqlite3.connect('banking.db')
        cursor = connection.cursor()
        cursor.execute("""
                SELECT * FROM "Card"
                """)
        result = cursor.fetchall()
        connection.close()

        return result

    def card_balance(self, number):
        """Check card balance"""
        connection = sqlite3.connect('banking.db')
        cursor = connection.cursor()
        cursor.execute("""
            SELECT "balance" FROM "Card" WHERE "number" == ?
            """, [number])
        result = cursor.fetchall()[0][0]
        connection.close()

        return result

    def charge_the_card(self):
        """Charge the card of the seat cost"""
        balance = self.card_balance(self.card_number)
        cost = self.seat_cost()
        updated_balance = balance - cost

        connection = sqlite3.connect('banking.db')
        connection.execute("""
        UPDATE "Card" SET "balance"=? WHERE "number"=?
        """, [updated_balance, self.card_number])
        connection.commit()
        connection.close()
