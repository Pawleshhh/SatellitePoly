from skyfield.api import load
from modules.initializeArgs import parse_arguments
from modules.printResult import print_horizon_result
from modules.satellite import load_satellites_tle, satellite_geographic_position, satellite_horizon_position, get_time_interval

def main():
    args = parse_arguments()
    
    ts = load.timescale()

    result = None
    satellites = None
    if args.load is not None:
        satellites = load_satellites_tle(args.load)

    if args.position is not None:
        
        if satellites is None:
            print('Specify location of satellite data')
        elif args.observator is None:
            print('Specify location of observator')
        else:
            result = []
            for sat in satellites:
                if args.position == 'geo':
                    result.append(satellite_geographic_position(get_time_interval(args.time, ts), sat))
                else:
                    result.append(satellite_horizon_position(get_time_interval(args.time, ts), args.observator, sat))
            
            if args.show and result is not None:
                print_horizon_result(result)

if __name__ == "__main__":
    main()
    pass