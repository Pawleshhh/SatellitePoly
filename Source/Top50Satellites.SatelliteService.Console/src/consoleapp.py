from skyfield.api import load, wgs84, N, W
from dateutil.parser import parse
import satelliteservice
from satelliteservice.initializeargs import parse_arguments, check_args
from satelliteservice.satelliteutil import load_satellites_tle, find_satellite_by_id
from satelliteservice.polynomials import get_polynomials_of_horizon_position

def create_coords_row(name, coords):
    row = name
    for x in coords:
        row = row + ', ' + str(x)
    return row

def write_polynomials(output, polynomials, satellite, observator, start, interval):
    alt, az, el = polynomials

    if output == './':
        output = output + 'polynomials.csv'

    maxLength = max(len(el), max(len(alt), len(az)))
    if maxLength == 0:
        return

    sat_name_row = 'Satellite, ' + str(satellite.name)
    observator_row = 'Observator coords, ' + str(observator)
    time_row = 'Start date time, ' + str(start) + ', Interval in seconds, ' + str(interval)

    headers_row = 'Coordinates'
    for i in range(maxLength):
        headers_row = headers_row + ', x' + str(i)

    alt_row = create_coords_row("Altitude", alt)
    az_row = create_coords_row("Azimuth", az)
    el_row = create_coords_row("Elevation", el)

    with open(output, 'w') as f:
        for row in [sat_name_row, 
                    observator_row, 
                    time_row, 
                    headers_row, 
                    alt_row, 
                    az_row, 
                    el_row]:
            f.write(row)
            f.write('\n')

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
    
    alt, az, el = get_polynomials_of_horizon_position(
        ts, 
        start, 
        interval, 
        observator, 
        satellite, 
        degrees)
    
    write_polynomials(args.output, [alt, az, el], satellite, observator, start, interval)
        
if __name__ == "__main__":
    main()
    pass