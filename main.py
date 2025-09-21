# main.py
from flight_search import search_flights, display_flights

try:
    print("Searching for flights...")
    flights = search_flights("BLR", "CCU", "2025-10-15")
    display_flights(flights, limit=10)
except Exception as e:
    print(f"Error: {e}")