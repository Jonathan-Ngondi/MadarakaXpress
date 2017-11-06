"Will store all information about Passenger object"

class Passenger(object):
    "Controls passenger object"

    def __init__(self, name):
        self.name = name
        self.passenger_data = {}

    def book_seat(self, bus_destination):
        "Helps Passenger book a bus"
        self.passenger_data['destination'] = bus_destination

    def cancel_booking(self, destination):
        "Helps Passenger cancel a booking"
        del self.passenger_data['destination']

    def update_booking(self, new_booking):
        "Helps Passenger update a booking"
        self.cancel_booking(new_booking)
        self.passenger_data['booking'] = new_booking
