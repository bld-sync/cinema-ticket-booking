import webbrowser
from fpdf import FPDF
import string
import random


class Pdf:
    def __init__(self, name, seat, seat_cost):
        self.name = name
        self.seat = seat
        self.seat_cost = seat_cost

    def create_pdf(self):
        """Create digital_ticket.pdf file"""
        letters = string.ascii_letters
        ticket_id = (''.join(random.choice(letters) for _ in range(6)))
        the_cost = str(self.seat_cost)

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Insert Title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Digital Ticket', border=0, align='C', ln=1)

        # Insert Values
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=40, txt='Name:', border=1)
        pdf.cell(w=100, h=40, txt=self.name, border=1, ln=1)
        pdf.cell(w=100, h=40, txt='Ticket ID:', border=1)
        pdf.cell(w=100, h=40, txt=ticket_id, border=1, ln=1)
        pdf.cell(w=100, h=40, txt='Price:', border=1)
        pdf.cell(w=100, h=40, txt=the_cost, border=1, ln=1)
        pdf.cell(w=100, h=40, txt='Seat Number:', border=1)
        pdf.cell(w=100, h=40, txt=self.seat, border=1, ln=1)

        pdf.output('digital_ticket.pdf')
        webbrowser.open('digital_ticket.pdf')
