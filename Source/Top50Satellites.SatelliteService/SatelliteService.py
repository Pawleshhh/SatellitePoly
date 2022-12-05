from skyfield.api import load, wgs84, N, W
from dateutil.parser import parse
from modules.initializeArgs import parse_arguments, check_args
from modules.satelliteutil import load_satellites_tle, find_satellite_by_id
from modules.polynomials import get_polynomials_of_horizon_position

def main():
    args = parse_arguments()
    
    if check_args(args) == False:
        return
    
    ts = load.timescale()

    satellites = load_satellites_tle(args.load)
    sat_id = args.id
    satellite = None

    if sat_id is not None:
        satellite = find_satellite_by_id(satellites, sat_id)
    elif len(satellites) > 0:
        satellite = satellites[0]
    
    if satellite is None:
        print("Could not find satellite")
        return
    
    lat, lon, el = args.observator
    observator = wgs84.latlon(lat * N, lon * W, el)
    start = parse(args.start)
    interval = args.interval
    degrees = args.degrees
    
    alt, az, el = get_polynomials_of_horizon_position(ts, start, interval, observator, satellite, degrees)
    
    print(str(alt.coef))
    print(str(az.coef))
    print(str(el.coef))
        
if __name__ == "__main__":
    main()
    pass