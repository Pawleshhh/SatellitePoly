import argparse
from email.policy import default
from os import path
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
    parser.add_argument('--count', '-c', dest='count', action='store',
                        type=int, default=1,
                        help="number of satellites to download starting from the first one")

    parser.add_argument('--id', dest='id', action='store',
                        type=int, default=None,
                        help="id of concrete satellite")
    parser.add_argument('--separator', action='store',
                        type=str, default=',',
                        help="specifies separator for output csv file")
    parser.add_argument('--observator', '-b', dest='observator', action='store',
                        type=float, nargs=3, default=[0.0, 0.0, 0.0],
                        help='localisation of the observator {latitude[degrees], longitude[degrees], elevation[meters]}.')
    parser.add_argument('--start', '-s', dest='start', action='store',
                        type=str, default=datetime.now().astimezone().strftime(get_datetime_format()),
                        help='start date and time of predicting satellite position. Format - d/m/Y H:M:S z e.g 10/07/09 18:59:11 -0400')
    parser.add_argument('--interval', '-i', dest='interval', action='store',
                        type=int, default=60,
                        help='seconds since --start')
    parser.add_argument('--degrees', '-d', dest='degrees', action='store',
                        type=int, default=3,
                        help='specifies degrees of polynomials')

    return parser.parse_args()

def check_args(args):
    
    #if path.exists(args.output) == False:
    #    if path.isdir(args.output):
    #        print(args.output, ' directory does not exist')
    #    elif path.isfile(args.output):
    #        print(args.output, ' file does not exist')
    #    else:
    #        print(args.output, ' path does not exist')
    #    return False
    if args.count <= 0:
        print(args.count, ' is wrong. Count must be equal or bigger than 1')
        return False

    return True