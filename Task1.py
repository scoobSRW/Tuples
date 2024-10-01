#here we define what we got goin on
def format_flight_itineraries(itineraries):
    formatted_itineraries = []

    for index, (traveler_name, origin, destination) in enumerate(itineraries, start=1):
        itinerary = f"Itinerary {index}: {traveler_name} - From {origin} to {destination}"
        formatted_itineraries.append(itinerary)

    return "\n".join(formatted_itineraries)

#List of our tuples
itineraries = [
    ("Timothy", "London", "Dallas"),
    ("Bob", "Tokyo", "Houston"),
    ("Thomas", "Oklahoma City", "Seattle")
]

#run
result = format_flight_itineraries(itineraries)
print(result)