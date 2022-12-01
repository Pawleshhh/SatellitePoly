import argparse

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