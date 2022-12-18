from skyfield.api import load, wgs84
from dateutil.parser import parse
from initializeargs import parse_arguments, check_args
from satelliteutil import load_satellites_tle, find_satellite_by_id
from polynomials import poly_horizon_position, poly_equatorial_position
from writeoutput import write_polynomials
from os import path
from progress.bar import Bar
from progress.spinner import Spinner
import signal
import sys

def poly_coords(eq, ts, start, interval, observer, satellite, degrees):
    if eq == True:
        return poly_equatorial_position(ts, start, interval, observer, satellite, degrees)
    else:
        return poly_horizon_position(ts, start, interval, observer, satellite, degrees)

def main():
    args = parse_arguments()
    
    if check_args(args) == False:
        return
    
    ts = load.timescale()

    count = args.count

    load_spinner = Spinner('Loading tle')
    load_spinner.next()
    loaded_satellites = load_satellites_tle(args.load)[0:count]
    loaded_sats_length = len(loaded_satellites)
    load_spinner.next()
    load_spinner.finish()

    sat_id = args.id
    selected_satellites = None

    if sat_id is not None and len(loaded_satellites) > 1:
        selected_satellites = [find_satellite_by_id(loaded_satellites, sat_id)]
    elif loaded_sats_length > 0:
        selected_satellites = loaded_satellites
    elif loaded_sats_length == 0:
        print('No satellites have been found')
    else:
        print("Could not find satellite of ", sat_id, " id")
        return
    
    lat, lon, el = args.observer
    observer = wgs84.latlon(lat, lon, el)
    start = parse(args.start)
    interval = args.interval
    degrees = args.degrees
    
    poly_of_coords = []

    poly_bar = Bar('Generating polynomials', max=len(selected_satellites))
    for satellite in selected_satellites:
        poly_of_coords.append(poly_coords(
            args.eq,
            ts, 
            start, 
            interval, 
            observer, 
            satellite, 
            degrees))
        poly_bar.next()
    poly_bar.finish()
    
    output = args.output

    if path.isdir(output):
        output = output + '/polynomials.csv'

    write_polynomials(
        output, 
        poly_of_coords,
        selected_satellites,
        observer,
        start, 
        interval,
        args.eq,
        args.separator)
    
def signal_handler(sig, frame):
    print('\n Program has been stopped \n')
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    main()