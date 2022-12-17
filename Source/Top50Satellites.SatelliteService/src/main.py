from skyfield.api import load, wgs84
from dateutil.parser import parse
from initializeargs import parse_arguments, check_args
from satelliteutil import load_satellites_tle, find_satellite_by_id
from polynomials import get_polynomials_of_horizon_position
from writeoutput import write_polynomials
from os import path
from progress.bar import Bar
from progress.spinner import Spinner
import signal
import sys

def signal_handler(sig, frame):
    print('\n Program has been stopped \n')
    sys.exit(0)

def main():
    args = parse_arguments()
    
    if check_args(args) == False:
        return
    
    ts = load.timescale()

    count = args.count

    load_spinner = Spinner('Loading tle')
    load_spinner.next()
    loaded_satellites = load_satellites_tle(args.load)[0:count]
    load_spinner.next()
    load_spinner.finish()

    sat_id = args.id
    selected_satellites = None

    if sat_id is not None and len(loaded_satellites) > 1:
        selected_satellites = [find_satellite_by_id(loaded_satellites, sat_id)]
    elif len(loaded_satellites) > 0:
        selected_satellites = loaded_satellites
    else:
        print("Could not find satellite of ", sat_id, " id")
        return
    
    lat, lon, el = args.observator
    observator = wgs84.latlon(lat, lon, el)
    start = parse(args.start)
    interval = args.interval
    degrees = args.degrees
    
    poly_of_altaz = []

    poly_bar = Bar('Generating polynomials', max=len(selected_satellites))
    for satellite in selected_satellites:
        poly_of_altaz.append(get_polynomials_of_horizon_position(
            ts, 
            start, 
            interval, 
            observator, 
            satellite, 
            degrees))
        poly_bar.next()
    poly_bar.finish()
    
    output = args.output

    if path.isdir(output):
        output = output + '/polynomials.csv'

    write_polynomials(
        output, 
        poly_of_altaz,
        selected_satellites,
        observator,
        start, 
        interval,
        args.separator)
    
if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    main()