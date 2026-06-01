import datetime 

print(datetime.MAXYEAR) # max year 
future_date = datetime.date(2025, 1, 1)
print(future_date) # date(year, month, day)

print(future_date.year) # year
print(future_date.month) # month
print(future_date.day) # day

somet_time = datetime.time(14, 30, 45) # time(hour, minute, second)
print(somet_time) # time(hour, minute, second)

## Format time 
print("Formated time:", somet_time.strftime("%H:%M:%S")) # Formatted time: 14:30:45

## now time 
now = datetime.datetime.now() # current date and time
now_time = datetime.time() # current time with default values for hour, minute, second
print(now) # current date and time
print("formatted: ", now.strftime("%Y-%m-%d %H:%M:%S")) # formatted: 2024-06-01 12:34:56
# %Y - year with century, %m - month as a zero-padded decimal, %d - day of the month as a zero-padded decimal, 
# %H - hour (24-hour clock) as a zero-padded decimal, %M - minute as a zero-padded decimal, %S - second as a zero-padded decimal   
# %A - weekday name, %B - month name, %p - AM or PM, %I - hour (12-hour clock) as a zero-padded decimal


formatted_date_str = "3000-01-01 00:00:00"
parsed_datetime = datetime.datetime.strptime(formatted_date_str, "%Y-%m-%d %H:%M:%S") # parse string to datetime object
print(parsed_datetime) # 3000-01-01 00:00:00


import time 
start_time = time.time() # start time
print('Start:',start_time)
time.sleep(3)

end_time = time.time()
print('Continue:',end_time)
print("Time Spent: ", end_time - start_time) # Time Spent: 3.000123456