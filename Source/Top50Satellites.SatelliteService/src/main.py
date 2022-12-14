from skyfield.api import load, wgs84, N, E
from dateutil.parser import parse
from initializeargs import parse_arguments, check_args
from satelliteutil import load_satellites_tle, find_satellite_by_id
from polynomials import get_polynomials_of_horizon_position
from os import path
from progress.bar import Bar
from progress.spinner import Spinner

def create_coords_row(name, coords):
    row = name
    for x in coords:
        row = row + ', ' + str(x)
    return row

def write_rows(rows, f):
    for row in rows:
        f.write(row)
        f.write('\n')

def write_polynomials(output, polynomials, satellites, observator, start, interval):
    
    with open(output, 'w') as f:
        observator_row = 'Observator coords, ' + str(observator)
        time_row = 'Start date time, ' + str(start) + ', Interval in seconds, ' + str(interval)

        write_rows([observator_row, time_row], f)

        f.write('\n')

        write_bar = Bar("Generating output", max=len(polynomials))

        for (satellite, poly_of_altaz) in zip(satellites, polynomials):
            alt, az, el = poly_of_altaz
            maxLength = max(len(el), max(len(alt), len(az)))

            sat_name_row = 'Satellite, ' + str(satellite.name)

            headers_row = 'Coordinates'
            for i in range(maxLength):
                headers_row = headers_row + ', x' + str(i)

            alt_row = create_coords_row("Altitude", alt)
            az_row = create_coords_row("Azimuth", az)
            el_row = create_coords_row("Elevation", el)

            write_rows([sat_name_row, 
                        headers_row, 
                        alt_row, 
                        az_row, 
                        el_row], f)

            f.write('\n')
            write_bar.next()

        write_bar.finish()

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
    observator = wgs84.latlon(lat * N, lon * E, el)
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

    write_polynomials(output, poly_of_altaz, selected_satellites, observator, start, interval)
        
if __name__ == "__main__":
    main()