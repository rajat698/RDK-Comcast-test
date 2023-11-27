from datetime import datetime, timezone

#Function to convert UTC timestamp to HH:MM:SS AM/PM format
def time_formatter(timestamp):

    # Convert UTC timestamp to datetime object
    utc = datetime.utcfromtimestamp(timestamp).replace(tzinfo=timezone.utc)

    # Format the datetime object to HH:MM:SS AM/PM format
    result = utc.strftime("%I:%M:%S %p")

    #Return the final formatted string
    return result