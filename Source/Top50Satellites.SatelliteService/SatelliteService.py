import argparse
import collections.abc
from skyfield.api import load, wgs84, N, W

# Parameters
displayOutput = True
output_path = ''
args = None

def check_if_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False
    
def get_month_days(year, monthIndex):
    leap = check_if_leap_year(year)
    months = [31, 29 if leap else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]

    return months[monthIndex - 1]

def load_satellites_tle(tle_path):
    """ Load satellites from given location
    """
    satellites = load.tle_file(tle_path)
    return satellites

def load_satellites_db(db_path):
    return 'No database'

def load_satellites_web(web_link):
    return 'No web'

def satellite_data_age(t, satellite):
    return t - satellite.epoch

def satellite_position(t, satellite):
    return [ satellite.at(time) for time in t ]

def satellite_geographic_position(t, satellite):
    geocentric = [ satellite.at(time) for time in t ]
    return [ wgs84.geographic_position_of(g) for g in geocentric ]
            
def satellite_horizon_position(t, geo_position, satellite):
    coords = wgs84.latlon(geo_position[0] * N, geo_position[1] * W)
    difference = satellite - coords
    return [ difference.at(time).altaz() for time in t ]

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

def load_satellites(args):
    if args.source == 'database':
        return load_satellites_db(args.load)
    elif args.source == 'website':
        return load_satellites_web(args.load)
    else:
        return load_satellites_tle(args.load)

def get_satellite_position(args):
    if args.position == 'geo':
        return satellite_geographic_position()

def parse_arguments():
    parser = argparse.ArgumentParser(
        prog = 'Top50Satellites service.',
        description='Service to process data related to Earth satellites.')
    
    parser.add_argument('--load', '-l', dest='load', action='store',
                        help='loads satellite data from specified location e.g., database, TLE file')
    parser.add_argument('--output', '-o', dest='output', action='store',
                        help='localisation of program\'s output')
    parser.add_argument('--source', '-s', dest='source', action='store',
                        choices=['database', 'file', 'website'],
                        help='specifies source of satellite data')
    
    parser.add_argument('--position', '-p', dest='position', action='store',
                        choices=['geo', 'hor'],
                        help='calculates position of loaded satellites')
    parser.add_argument('--observator', dest='observator', action='store',
                        type=float, nargs=2, default=[0.0, 0.0],
                        help='specifies coordinates of the observator')
    parser.add_argument('--time', dest='time', action='store',
                        type=int, nargs=8,
                        help='specifies time interval of calculations (year, month, day, hour, minute, second, interval in s, count)')

    parser.add_argument('--update', '-u', dest='update', action='store',
                        choices=['all', 'visual', 'weather'],
                        help='specifies to update database')

    parser.add_argument('--show', dest='show', action='store_false',
                        help='disables showing output')

    return parser.parse_args()

def print_horizon_result(result):

    def print_single_horizon(hor):
        alt, az, dist = hor
        print('Alt = ', alt, ' Az = ', az)
        
    for r in result:
        for hor in r:
            print_single_horizon(hor)

def main():
    args = parse_arguments()
    
    ts = load.timescale()

    result = None
    satellites = None
    if args.load is not None:
        satellites = load_satellites_tle(args.load)

    if args.position is not None:
        
        if satellites is None:
            print('Specify location of satellite data')
        elif args.observator is None:
            print('Specify location of observator')
        else:
            result = []
            print('LENGTH', len(satellites))
            i = 0
            for sat in satellites:
                print(i)
                i = i + 1
                if args.position == 'geo':
                    result.append(satellite_geographic_position(get_time_interval(args.time, ts), sat))
                else:
                    result.append(satellite_horizon_position(get_time_interval(args.time, ts), args.observator, sat))
            if args.show and result is not None:
                print_horizon_result(result)
    



if __name__ == "__main__":
    main()
    pass