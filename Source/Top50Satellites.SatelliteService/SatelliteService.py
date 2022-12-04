from skyfield.api import load, wgs84, N, W
from numpy.polynomial import Chebyshev
from datetime import datetime, timedelta
from dateutil.parser import parse
from modules.initializeArgs import parse_arguments, check_args, get_datetime_format
from modules.satellite import load_satellites_tle, satellite_horizon_position

def main():
    args = parse_arguments()
    
    if check_args(args) == False:
        return
    
    ts = load.timescale()

    satellites = load_satellites_tle(args.load)
    satellite = satellites[0]

    lat, lon, el = args.observator
    observator = wgs84.latlon(lat * N, lon * W, el)
    start = parse(args.start)
    interval = args.interval
    degrees = args.degrees
    
    date = start
    altitudes = []
    azimuths = []
    seconds_axis = []
    for second in range(interval):
        time = ts.from_datetime(date)
        alt, az, mag = satellite_horizon_position(time, observator, satellite)
        altitudes.append(alt.degrees)
        azimuths.append(az.degrees)
        seconds_axis.append(second)
        date = date + timedelta(seconds=1)
        
    polyfit_alt = Chebyshev.fit(seconds_axis, altitudes, deg=degrees)
    polyfit_az = Chebyshev.fit(seconds_axis, azimuths, deg=degrees)
    
    print("Altitude polynomial")
    print(polyfit_alt)
    print("Azimuth polynomial")
    print(polyfit_az)

if __name__ == "__main__":
    main()
    pass