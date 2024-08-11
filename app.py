import phonenumbers
from phonenumbers import geocoder

def get_location(phone_number: str) -> str:
    """Parse and get the location of the phone number."""
    parsed_number = phonenumbers.parse(phone_number)
    location = geocoder.description_for_number(parsed_number, "en")
    return location

def main():
    # List of phone numbers
    phone_numbers = [
        "+254769405130",
        "+918878586271",
        "+12136574429",
        "+201234567890",
        "+917294536271",
        "+255798954395"
    ]

    print("\nPhone Number Location")
    for i, number in enumerate(phone_numbers, start=1):
        location = get_location(number)
        print(f"{i}. {location}")

if __name__ == "__main__":
    main()
