#5. Write a function which takes the input of a time in 24-hour format, and converts it to 12-hour
#format. Note: do not use a datetime library.

#Example:
#Input: 09:53
#Output: 9:53AM
#Input: 17:29
#Output: 5:29PM
def convert_to_12_hour(time_24):
    # Split the input into hours and minutes
    hours, minutes = map(int, time_24.split(':'))
    
    # Determine the period (AM/PM)
    period = 'AM' if hours < 12 else 'PM'
    
    # Adjust the hour for 12-hour format
    hours = hours % 12
    if hours == 0:
        hours = 12

    # Format the new time string
    time_12 = f'{hours}:{minutes:02d}{period}'
    return time_12

# Example usage:
print(convert_to_12_hour('09:53'))  # Output: 9:53AM
print(convert_to_12_hour('17:29'))  # Output: 5:29PM    
