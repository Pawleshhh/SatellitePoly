import argparse
from skyfield.api import load, wgs84

# Parameters
displayOutput = True
output_path = ''
args = None

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
    difference = satellite - geo_position
    return [ difference.at(time).altaz() for time in t ]

def get_time_interval(time, ts):
    [year, month, day, hour, minute, second, interval, count] = time
    t_start = ts.utc(year, month, day, hour, minute, second)
    t = t_start
    result = []

    #for t in range(count):
    #    result.append(t)
    #    t = t.

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
                        help='specifies time interval of calculations (year, month, day, hour, minute, second, interval in ms, count)')

    parser.add_argument('--update', '-u', dest='update', action='store',
                        choices=['all', 'visual', 'weather'],
                        help='specifies to update database')

    parser.add_argument('--show', dest='show', action='store_false',
                        help='disables showing output')

    return parser.parse_args()

def main():
    args = parse_arguments()
    
    ts = load.timescale()

    result = None
    if args.load is not None:
        result = load_satellites()
    elif args.position is not None:
        result = None

if __name__ == "__main__":
    main()
    pass