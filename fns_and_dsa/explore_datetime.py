# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    """Display the current date and time in a readable format."""
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date

def calculate_future_date(current_date, days_to_add):
    """Calculate and display the future date after adding the specified number of days to the current date."""
    future_date = current_date + timedelta(days=days_to_add)
    print("Future date:", future_date.strftime("%Y-%m-%d"))
    return future_date

def main():
    # Display the current date and time
    current_date = display_current_datetime()
    
    # Prompt the user to enter a number of days to add
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    # Calculate and display the future date
    calculate_future_date(current_date, days_to_add)

if __name__ == "__main__":
    main()
