import datetime

def change_timestamp(timestamp):
    date_time = datetime.datetime.fromtimestamp(timestamp)
    formatted_date = date_time.strftime('%B %d')

    return formatted_date

def round_timestamp(timestamp, round_time=86400):
    timestamp = int(timestamp)
    timestamp_unit_day = timestamp / round_time
    recover_to_unit_second = int(timestamp_unit_day) * round_time
    return recover_to_unit_second