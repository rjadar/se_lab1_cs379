import re


_SEAT_PATTERN = re.compile(r"[A-Za-z][1-9][0-9]*")
_PRICES_PATTERN = re.compile(r"[0-9]+(?:,[0-9]+)*")
_RATINGS_PATTERN = re.compile(r"[0-9]+(?:\s+[0-9]+)*")


def parse_seat(seat):
    if not isinstance(seat, str):
        raise TypeError("seat must be a string")
    if _SEAT_PATTERN.fullmatch(seat) is None:
        raise ValueError("seat must contain a row letter and a positive seat number")
    return seat[0].upper(), int(seat[1:])


def total_price(prices_csv):
    if not isinstance(prices_csv, str):
        raise TypeError("prices_csv must be a string")
    if _PRICES_PATTERN.fullmatch(prices_csv) is None:
        raise ValueError("prices_csv must contain non-negative integer prices separated by commas")
    prices = [int(price) for price in prices_csv.split(",")]
    try:
        return round(sum(prices) * 1.18, 2)
    except OverflowError as error:
        raise ValueError("ticket prices are too large to calculate") from error


def average_rating(ratings):
    if not isinstance(ratings, str):
        raise TypeError("ratings must be a string")
    if _RATINGS_PATTERN.fullmatch(ratings) is None:
        raise ValueError("ratings must contain one or more integer values")
    values = [int(rating) for rating in ratings.split()]
    if any(rating < 1 or rating > 5 for rating in values):
        raise ValueError("ratings must be between 1 and 5")
    return round(sum(values) / len(values), 1)


def main():
    print("==== Running parse_seat ====")
    user_input = input("Enter a seat number (e.g. H12): ")
    result = parse_seat(user_input)
    print("Row and Seat:", result)

    print("\n==== Running total_price ====")
    user_input = input("Enter ticket prices as CSV (e.g. 150,250,400): ")
    result = total_price(user_input)
    print("Total with GST:", result)

    print("\n==== Running average_rating ====")
    user_input = input("Enter ratings separated by spaces (e.g. 4 5 3): ")
    result = average_rating(user_input)
    print("Average Rating:", result)


if __name__ == "__main__":
    main()
