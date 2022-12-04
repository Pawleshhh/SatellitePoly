import argparse
from datetime import datetime
from dateutil.tz import tzoffset

def get_datetime_format():
    return "%d/%m/%Y %H:%M:%S %z"

def parse_arguments():
    parser = argparse.ArgumentParser(
        prog = 'Top50Satellites service.',
        description='Service to process data related to Earth satellites.')
    
    parser.add_argument('--load', '-l', dest='load', action='store',
                        help='loads satellite data from specified location e.g., database, TLE file')
    parser.add_argument('--output', '-o', dest='output', action='store',
                        default='./',
                        help='localisation of program\'s output')
    
    parser.add_argument('--observator', '-b', dest='observator', action='store',
                        type=float, nargs=3, default=[0.0, 0.0, 0.0],
                        help='localisation of the observator {latitude[degrees], longitude[degrees], elevation[meters]}.')
    parser.add_argument('--start', '-s', dest='start', action='store',
                        type=str, default=datetime.now(tz=tzoffset(None, 0)).strftime(get_datetime_format()),
                        help='start date and time of predicting satellite position. Format - d/m/Y H:M:S z e.g 10/07/09 18:59:11 -0400')
    parser.add_argument('--interval', '-i', dest='interval', action='store',
                        type=int, default=60,
                        help='seconds since --start')
    parser.add_argument('--degrees', '-d', dest='degrees', action='store',
                        type=int, default=3,
                        help='specifys degrees of polynomials')

    return parser.parse_args()

def check_args(args):

    if args.load is None:
        print('Need to supply location of data')
        return False

    return True