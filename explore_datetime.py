from datetime import datetime, timedelta


def display_current_datetime():
    """
    Displays the current date and time in the format YYYY-MM-DD HH:MM:SS.
    Saves the current date inside the variable current_date.
    """
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date


def calculate_future_date(current_date):
    """
    Prompts the user for a number of days, calculates the future date,
    saves it inside the variable future_date, and prints it in YYYY-MM-DD format.
    """
    days_input = input("Enter the number of days to add to the current date: ")

    # Validate integer input
    if not days_input.lstrip("-").isdigit():
        raise ValueError("Invalid input. Please enter an integer value for days.")

    number_of_days = int(days_input)
    future_date = current_date + timedelta(days=number_of_days)

    formatted_future = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future}")

    return future_date


def main():
    current_date = display_current_datetime()
    calculate_future_date(current_date)


if __name__ == "__main__":
    main()
