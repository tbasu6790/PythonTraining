'''
Create a base class Flight with basic flight information. Create a derived class ScheduledFlight that adds scheduling information.
Requirements:
-Flight should have attributes: flight number, airline.
-ScheduledFlight should add departure time and arrival time.
-Include methods to display complete flight information.
 
Create a base class Person, derived class CrewMember, and a further derived class Pilot.
-Person contains name and ID.
-CrewMember adds role (e.g., "Cabin Crew", "Pilot").
-Pilot adds license number and rank (e.g., "Captain").
 
Create a base class Service, and derive two classes: SecurityService and BaggageService.
Requirements:
-Service class has a method service_info().
-Derived classes override or extend this to describe their own service.
 
Create one class PassengerDetails and another class TicketDetails. Create a new class Booking that inherits from both.
Requirements:
- PassengerDetails has name, age.
- TicketDetails has ticket number, seat number.
- Booking shows all information.
'''

class Flight:
    def __init__(self, flight_no, airline):
        self.flight_no = flight_no
        self.airline = airline
 
    def display_info(self):
        print(f"Flight Number: {self.flight_no}, Airline: {self.airline}")
 
class ScheduledFlight(Flight):
    def __init__(self, flight_no, airline, departure, arrival):
        super().__init__(flight_no, airline)  # Call base constructor
        self.departure = departure
        self.arrival = arrival
 
    def display_info(self):
        super().display_info()  # Call parent method
        print(f"Departure: {self.departure}, Arrival: {self.arrival}")
 
sf = ScheduledFlight("AI101", "Air India", "10:00 AM", "1:30 PM")
sf.display_info()
class Person:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
 
    def display(self):
        print(f"Name: {self.name}, ID: {self.ID}")
 
class CrewMember(Person):
    def __init__(self, name, ID, role):
        super().__init__(name, ID)
        self.role = role
 
    def display(self):
        super().display()
        print(f"Role: {self.role}")
 
 
class Pilot(CrewMember):
    def __init__(self, name, ID, role, license_no, rank):
        super().__init__(name, ID, role)
        self.license_no = license_no
        self.rank = rank
 
    def display(self):
        super().display()
        print(f"License: {self.license_no}, Rank: {self.rank}")
 
 
# Example
p = Pilot("Ajay Koley", "C123", "Pilot", "LN567", "Captain")
p.display()
class PassengerDetails:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
 
class TicketDetails:
    def __init__(self, ticket_no, seat_no, price):
        self.ticket_no = ticket_no
        self.seat_no = seat_no
        self.price = price
 
 
class Booking(PassengerDetails, TicketDetails):
    def __init__(self, name, age, ticket_no, seat_no, price):
        PassengerDetails.__init__(self, name, age)
        TicketDetails.__init__(self, ticket_no, seat_no, price)
 
    def show_booking(self):
        print(f"Passenger: {self.name}, Age: {self.age}")
        print(f"Ticket No: {self.ticket_no}, Seat: {self.seat_no}, Price: {self.price}")
 
 
# Example
b = Booking("Titli", 22, "T567", "12A", 5500)
b.show_booking()