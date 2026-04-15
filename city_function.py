#Creates a function to format city state and country and list it
def city_country(city, state, country):
    formatted_name = f"{city}, {state}, {country}".title()
    return formatted_name