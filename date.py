import datetime as dt


if __name__ == "__main__":
    now = dt.datetime.now()

    year = now.year
    time_methods = {
        "weekday_short": now.strftime('%a'),
        "weekday_full": now.strftime('%A'),
        "weekday_number": now.strftime('%w'),
        "day_of_month": now.strftime('%d'),
        "month_short": now.strftime('%b'),
        "month_name": now.strftime('%B'),
        "month_number": now.strftime('%m'),
        "year_short": now.strftime('%y'),
        "year_full": now.strftime('%Y'),
        "hour_military": now.strftime('%H'),
        "hour_std": now.strftime('%I'),
        "am_pm": now.strftime('%p'),
        "minute": now.strftime('%M'),
        "second": now.strftime('%S'),
        "microsecond": now.strftime('%f'),
        "utc_offset": now.strftime('%z'),
        "timezone": now.strftime('%Z'),
        "day_number": now.strftime('%j'),
        "week_number_sun": now.strftime('%U'),
        "week_number_mon": now.strftime('%W'),
        "local_datetime": now.strftime('%c'),
        "local_date": now.strftime('%x'),
        "local_time": now.strftime('%X'),
        "character": now.strftime('%%'),
        "iso_year": now.strftime('%G'),
        "iso_weekday": now.strftime('%u'),
        "iso_week_number": now.strftime('%V')
    }

    the_ones_i_need = {
        "weekday_short": now.strftime('%a'),
        "weekday_full": now.strftime('%A'),
        "weekday_number": now.strftime('%w'),
        "day_of_month": now.strftime('%d'),
        "month_short": now.strftime('%b'),
        "month_name": now.strftime('%B'),
        "month_number": now.strftime('%m'),
        "year_short": now.strftime('%y'),
        "year_full": now.strftime('%Y'),
        "hour_military": now.strftime('%H'),
        "hour_std": now.strftime('%I'),
        "am_pm": now.strftime('%p'),
        "minute": now.strftime('%M'),
        "second": now.strftime('%S'),
        "day_number": now.strftime('%j'),
        "week_number_sun": now.strftime('%U'),
        "local_datetime": now.strftime('%c'),
        "local_date": now.strftime('%x'),
        "local_time": now.strftime('%X'),
        "character": now.strftime('%%')

    }

    for method_name, method_output in the_ones_i_need.items():
        print(f"{method_name}: {method_output}")

    build_custom = '[%b %d %Y]: %a %X %p'
    custom = dt.datetime.now()
    custom = custom.strftime(build_custom)
    print("\nCustom:")
    print(custom)
    print()

    # Create a date time object
    user_year = 2020
    user_month = 2
    user_day = 17
    new_date = dt.datetime(user_year, user_month, user_day)
    print(f"New Date: {new_date.strftime('%x')}")
    print(new_date)
