import requests
import random

# Lists to identify what belongs to cuisines and offers
known_cuisines = [
    'Pizza', 'Burger', 'Chicken', 'Sandwich', 'Kebab', 'Turkish', 
    'Italian', 'American', 'Fast Food', 'Pasta', 'Hungarian', 'Italian', 
    'Breakfast', 'Café', 'British', 'Sushi', 'Asian', 'Caribbean', 'Greek', 
    'Mediterranean', 'African'
]
dietary_preferences = ['Halal', 'Kosher', 'Vegan', 'Vegetarian']
meal_times = ['Breakfast', 'Lunch', 'Dinner', 'Dessert', 'Snacks']
offer_keywords = ['collect stamps', 'deals', 'low delivery fee', 'delivery', 'offer', 'discount']

def fetch_restaurants(postcode):
    """
    Fetches restaurant data from the Just Eat API based on the provided postcode.

    Args:
        postcode (str): The postcode to search for.

    Returns:
        dict: JSON response containing restaurant data.
    """
    postcode = postcode.replace(' ', '')
    url = f"https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/{postcode}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    return response.json() if response.ok else None

def process_address(address):
    """
    Processes the address dictionary to generate a formatted address string.

    Args:
        address (dict): Address information dictionary.

    Returns:
        str: Formatted address string.
    """
    address_parts = [part for part in address.values() if isinstance(part, str)]
    cleaned_address = ' '.join(address_parts)
    if 'Point' in cleaned_address:
        cleaned_address = cleaned_address.rsplit(' ', 3)[0]
    return cleaned_address.strip()

def truncate_string(string, max_length, is_address=False):
    """
    Truncates a string if it exceeds a certain length.

    Args:
        string (str): The string to truncate.
        max_length (int): The maximum length allowed for the string.
        is_address (bool): Whether the string is an address.

    Returns:
        str: Truncated string if it exceeds the maximum length, otherwise the original string.
    """
    return string[:max_length] if len(string) > max_length and not is_address else string

def extract_cuisines_and_offers(restaurant):
    """
    Extracts cuisines and offers from the restaurant data.

    Args:
        restaurant (dict): Restaurant information dictionary.

    Returns:
        tuple: A tuple containing cuisines string and offers string.
    """
    items = restaurant.get('cuisines', [])
    cuisines = []
    offers = []

    for item in items:
        item_name = item['name'] if isinstance(item, dict) and 'name' in item else item
        if any(cuisine.lower() in item_name.lower() for cuisine in known_cuisines + dietary_preferences + meal_times):
            cuisines.append(item_name)
        elif any(offer.lower() in item_name.lower() for offer in offer_keywords):
            offers.append(item_name)

    cuisines_str = ', '.join(cuisines) if cuisines else 'Various'
    offers_str = ', '.join(offers) if offers else 'no offers available'
    return cuisines_str, offers_str

def custom_sort(restaurant):
    rating = -restaurant.get('rating', {}).get('starRating', 0)  # Multiply by -1 to sort in descending order
    name = restaurant.get('name', '').lower()
    if ',' in name:
        name_address = name.split(',', 1)
        address = name_address[1].strip()
        name = name_address[0].strip()
    else:
        address = ''
    return (rating, name, address)



def display_restaurants(data, postcode, display_option):
    """
    Displays restaurant information based on the chosen display option.

    Args:
        data (dict): Restaurant data dictionary.
        postcode (str): The postcode used for the search.
        display_option (str): The chosen display option.

    Returns:
        None
    """
    if not data or "restaurants" not in data:
        print("No restaurant data found.")
        return

    restaurants = data["restaurants"]
    if display_option == '1':
        sorted_restaurants = sorted(restaurants, key=custom_sort)
    elif display_option == '2':
        sorted_restaurants = sorted(restaurants, key=custom_sort, reverse=True)
    elif display_option == '3':
        sorted_restaurants = random.sample(restaurants, min(len(restaurants), 10))
    else:
        print("Invalid option. Displaying default sorted by highest rating.")
        sorted_restaurants = sorted(restaurants, key=custom_sort)

    header_format = f"{'Name':<30} {'Cuisines':<30} {'Rating':>6} {'Offers':<20} {'Address':<60}"
    print(f"\nRestaurants in {postcode}:\n")
    print(header_format)
    print("-" * len(header_format))
    
    for restaurant in sorted_restaurants[:10]:
        name = truncate_string(restaurant.get('name', 'N/A').split(',')[0], 30)
        cuisines, offers = extract_cuisines_and_offers(restaurant)
        rating = restaurant.get('rating', {}).get('starRating', 'N/A')
        address = truncate_string(process_address(restaurant.get('address', {})), 60, is_address=True)
        print(f"{name:<30} | {cuisines:<30} | {rating:>6} | {offers:<20} | {address:<60}")
        print("-" * len(header_format))  # Add a dashed line separator
        print()  # Add an empty line after each restaurant's information

def main():
    """
    Main function to run the Restaurant Finder application.
    """
    print("Welcome to the Restaurant Finder!")
    while True:
        print("\nPlease choose an option for listing restaurants by entering the number:")
        print("1: Highest to Lowest Rating")
        print("2: Lowest to Highest Rating")
        print("3: Random Order")
        print("4: Quit")
        display_option = input("Enter option (1, 2, 3, or 4): ").strip()
        if display_option == '4':
            break
        postcode = input("Enter a UK postcode: ").strip()
        data = fetch_restaurants(postcode)
        display_restaurants(data, postcode, display_option)

if __name__ == "__main__":
    main()
