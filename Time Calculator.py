def add_time(start_time,duration,day = ""):
    weekdays = ["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"]
    # Splitting the hours and (AM/PM) for first parameter
    hour_meridian = start_time.split()
    hours_1 = int(hour_meridian[0].split(":")[0])
    meridian = hour_meridian[1]
    # Splitting duration hour
    hour_2 = int(duration.split(":")[0])
    # Dividing hour_2 by 24 to get remainder
    newhour_2 = hour_2 % 24
    # Adding to hour 1 to get total hours
    cleanhour = hours_1 + newhour_2
    total_hour = cleanhour % 12 # Therefore final hour can now be adjusted by minutes if min > 60
    # Computing minutes
    time_minutes = int(hour_meridian[0].split(":")[1])
    duration_minutes = int(duration.split(":")[1])
    total_minutes = time_minutes + duration_minutes
    # Integer division of time to check if its greater than 60 minutes and adding to final hour
    int_minutes_divide = total_minutes // 60
    time_24_sys = cleanhour + int_minutes_divide # Used to compute meridian
    t = time_24_sys//12 # Int division of 24 hour system
    final_hour = str(total_hour + int_minutes_divide)
    if total_minutes < 60:
        final_minutes = str(total_minutes)
    else:
        final_minutes = str(total_minutes % 60)
    # Adding Zero's to fnal minutes < 10
    if int(final_minutes) < 10:
            final_minutes = "0" + final_minutes
    # Determine AM/PM
    # Also initializing number of days
    num_days = 0
    if meridian == "AM":
        if t % 2 != 0:
            meridian = "PM"
        else:
            pass
    elif meridian == "PM":
        if t % 2 != 0:
            meridian = "AM"
            num_days += 1
        else:
            pass
    # Determining Number of days
    num_days += hour_2//24
    # Determining day of the week
    if day != "":
        index = weekdays.index(day.title())
        new_index = (index + (num_days % 7)) % 7
        final_day = weekdays[new_index]
    else:
        pass 
    # Answer format
    time_format = final_hour + ":" + final_minutes + " " + meridian
    if day != "" and num_days < 1:
        return time_format + ", " + final_day
    elif day != "" and num_days > 0:
        if num_days == 1:
            return time_format + ", " + final_day + " (next day)"
        else:
            return time_format + ", " + final_day + f" ({num_days} days later)"
    elif day == "":
        if num_days == 1:
            return time_format + " (next day)"
        elif num_days > 1:
            return time_format + f" ({num_days} days later)"
        else:
            return time_format
        # =====Continue from here=====. Check other conditions for answer
lst = ["8:16 PM", "466:02"]
print(add_time(lst[0],lst[1]))
