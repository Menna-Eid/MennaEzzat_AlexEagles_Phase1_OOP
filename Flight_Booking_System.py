import tkinter as tk
from tkinter import messagebox

class Airport:
    def __init__(self,name,code):
        self.name = name
        self.code = code

class Meal_Selecting:
    def __init__(self, meal_options):
        self.meal_options = meal_options

class services:
    def __init__(self, price):
        self.price = price

class Flight(services):
    def __init__(self, flight_number, airline,departure_airport, arrival_airport, price, meal):
        super().__init__(price)
        self.flight_number = flight_number
        self.airline = airline
        self.departure_airport = departure_airport
        self.arrival_airport = arrival_airport
        self.meal = meal
    def get_details(self):
        return f"{self.flight_number} ,{self.airline} from {self.departure_airport.name} to {self.arrival_airport.name}, Time: {self.departure_time} - {self.arrival_time}, Price: {self.price}"
#Flight inherits from class services
class Airline:
    def __init__(self, name):
        self.name = name
        self.flights = []
    def add_flight(self, flight):
        self.flights.append(flight)

class Customer:
    def __init__(self, name, email, airport_1, airport_2):
        self.name = name
        self.email = email
        self.airport_1 = airport_1
        self.airport_2 = airport_2



class Booking:
    def __init__(self, flight, customer, selected_meal):
        self.flight = flight
        self.customer = customer
        self.selected_meal = selected_meal

class FlightBookingSystem:
    def __init__(self):
        self.airports = []
        self.flights = []
        self.airlines = []
    def add_airport(self, airport):
        self.airports.append(airport)

    def add_flight(self, flight):
        self.flights.append(flight)

    def add_airline(self, airline):
        self.airlines.append(airline)

    def book_flight(self, flight, customer, selected_meal):
        booking = Booking(flight, customer, selected_meal)
        return booking
    
class Booking_Application:
    def __init__(self, root):
        self.root = root
        self.system = FlightBookingSystem()
        self.setup_ui()
    def setup_ui(self):
        self.root.title("Flight Booking System") 
        #Adding UI elements to take inputs
        tk.Label(self.root, text="Customer Name").pack()
        self.customer_name = tk.Entry(self.root)
        self.customer_name.pack()

        tk.Label(self.root, text="Customer Email").pack()
        self.customer_email = tk.Entry(self.root)
        self.customer_email.pack()

        tk.Label(self.root, text="Departure Airport").pack()
        self.customer_airport_1 = tk.Entry(self.root)
        self.customer_airport_1.pack()  

        tk.Label(self.root, text="Arrival Airport").pack()
        self.customer_airport_2 = tk.Entry(self.root)
        self.customer_airport_2.pack()

        tk.Button(self.root, text= "Book a flight", command= self.make_booking).pack()

    def make_booking(self):
        name = self.customer_name.get()
        email = self.customer_email.get()
        airport_1 = self.customer_airport_1.get()
        airport_2 = self.customer_airport_2.get()

        if name and email and airport_1 and airport_2:
            customer = Customer(name, email, airport_1, airport_2)
            flight = self.system.flights[0]#choosing first flight
            selected_meal = Meal_Selecting("Steak")
            booking = self.system.book_flight(flight, customer, selected_meal)
            messagebox.showinfo(" Booking Successful",f"Booking made for {customer.name} on flight {flight.flight_number}")  
        else:
            messagebox.showwarning("Error", "Please enter all details")

if __name__ == "__main__":
    root = tk.Tk()
    app = Booking_Application(root)

    #sample data example
    airport_1 = Airport("CIA", "Cairo International Airport")
    airport_2 = Airport("AIA", "Athens International Airport")
    airline = Airline("Egypt Air")         
    flight1 = Flight("FL658", airline.name, airport_1, airport_2 , 500 ,[Meal_Selecting("Steak"),Meal_Selecting("Vegetarian")] )
    
    app.system.add_airport(airport_1)
    app.system.add_airport(airport_2)
    
    airline.add_flight(flight1)
    
    app.system.add_airline(airline)
    app.system.add_flight(flight1)
    root.mainloop()      

