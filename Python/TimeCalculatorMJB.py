def get_seconds():
    seconds = int(input("Enter the total number of seconds: "))
    return seconds

def get_days(seconds):
    days = seconds // 86400
    seconds = seconds % 86400
    return days, seconds

def get_hours(seconds):
    hours = seconds // 3600
    seconds = seconds % 3600
    return hours, seconds

def get_minutes(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    return minutes, seconds

def main():
    seconds = get_seconds()
    days, remaining_seconds = get_days(seconds)
    hours, remaining_seconds = get_hours(remaining_seconds)
    minutes, remaining_seconds = get_minutes(remaining_seconds)
    seconds = remaining_seconds
    print("The number of days is: ", days, "\n",
    "The number of hours is: ", hours, "\n",
    "The number of minutes is: ", minutes, "\n",
    "The number of seconds is: ", seconds)

main()