'''Problem Statement
You are asked to design a Flight Management System in Python using exception handling.
The system should:
- Read flight information from a file called flights.txt.
- Each line has: flight_number available_seats price_per_ticket
  Example: AI101 50 6000
 
Ask the user for:
- Flight number
- Number of tickets to book
Implement the following exception rules: (Questions below)
(a) Raise FlightNotFoundError (custom) if the entered flight number does not exist. 
(b) Raise SeatsUnavailableError (custom) if requested tickets exceed available seats.
(c) Handle ValueError if user enters invalid input (like string instead of integer).
(d) Handle ZeroDivisionError if user enters 0 tickets (while calculating discount per ticket).
(e) Always close the file using finally.
The program should print:
- Flight details
- Total booking cost
- Discount per ticket (total / tickets)

Note**:
Use nested try-except:
Inner block for booking operations.
Outer block for file handling & re-raised exceptions
'''

class FlightNotFoundError(Exception):
    pass

class SeatsUnavailableError(Exception):
    pass

def main():
    try:
        file = open(r"C:\Users\Titli.Basu\Documents\PythonTraining\Assignment\flight.txt", "r")
        
        # Read flight data into a dictionary
        flights = {}
        for line in file:
            parts = line.strip().split()
            if len(parts) == 3:
                flight_number, seats, price = parts
                flights[flight_number] = {
                    "seats": int(seats),
                    "price": float(price)
                }

        try:
            flight_no = input("Enter flight number: ").strip()
            tickets = int(input("Enter number of tickets to book: "))

            if flight_no not in flights:
                raise FlightNotFoundError(f"Flight {flight_no} not found!")

            flight = flights[flight_no]

            if tickets > flight["seats"]:
                raise SeatsUnavailableError("Not enough seats available!")

            total_cost = flight["price"] * tickets

            discount_per_ticket = total_cost / tickets  

            print("\n--- Booking Details ---")
            print(f"Flight: {flight_no}")
            print(f"Available Seats: {flight['seats']}")
            print(f"Price per Ticket: {flight['price']}")
            print(f"Tickets Booked: {tickets}")
            print(f"Total Cost: {total_cost}")
            print(f"Discount per Ticket: {discount_per_ticket}")

        except FlightNotFoundError as e:
            print("Error:", e)
        except SeatsUnavailableError as e:
            print("Error:", e)
        except ValueError:
            print("Error: Invalid input. Please enter numeric values for tickets.")
        except ZeroDivisionError:
            print("Error: Number of tickets cannot be zero.")
        finally:
            print("\nBooking attempt finished.")

    except FileNotFoundError:
        print("Error: flight.txt file not found!")
    finally:
        try:
            file.close()
        except:
            pass

if __name__ == "__main__":
     main()
