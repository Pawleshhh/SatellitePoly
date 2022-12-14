from skyfield.api import load, wgs84, N, W

def check_if_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False
    
def get_month_days(year, monthIndex):
    leap = check_if_leap_year(year)
    months = [31, 29 if leap else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]

    return months[monthIndex - 1]

def find_satellite_by_id(satellites, sat_id):

    if satellites is None or len(satellites) <= 0:
        return None

    for satellite in satellites:
        if satellite.model.satnum == sat_id:
            return satellite

    return None

def load_satellites_tle(tle_path):
    satellites = load.tle_file(tle_path)
    return satellites

def satellite_data_age(t, satellite):
    return t - satellite.epoch

def satellite_position(t, satellite):
    return satellite.at(t)

def satellite_geographic_position(t, satellite):
    geocentric = satellite.at(t)
    return wgs84.geographic_position_of(geocentric) 
            
def satellite_horizon_position(t, observer, satellite):
    difference = satellite - observer
    return difference.at(t).altaz()

def satellite_equatorial_position(t, observer, satellite):
    difference = satellite - observer
    return difference.at(t).radec()

#def satellite_is_sunlit(t, satellite, start, interval):
#    time_range = t.utc(start.date.year,
#                       start.date.month,
#                       start.date.day,
#                       start.time.hour,
#                       start.time.minute,
#                       range(start.time.second, interval, step=1))
#    sunlit = satellite.at(time_range).is_sunlit()

def get_time_interval(time, ts):

    def check_time_part(time_parts, max_parts, result):
        length = len(time_parts)
        if length == 0:
            return result
        elif time_parts[0] < max_parts[0]:
            result.append(time_parts[0])
        else:
            if length > 1:
                time_parts[1] = time_parts[1] + 1
            result.append(time_parts[0] - max_parts[0])

        return check_time_part(time_parts[1:], max_parts[1:], result)

    [year, month, day, hour, minute, second, interval, count] = time
    t_start = ts.utc(year, month, day, hour, minute, second)
    t = t_start
    result = []

    for i in range(count):
        result.append(t)
        [second, minute, hour, day, month, year] = check_time_part([second + interval, minute, hour, day, month, year], [60, 60, 24, get_month_days(year, month), 12, 10000], [])
        t = ts.utc(year, month, day, hour, minute, second)

    return result