

def print_horizon_result(result):

    def print_single_horizon(hor):
        alt, az, dist = hor
        print('Alt = ', alt, ' Az = ', az)
        
    for r in result:
        for hor in r:
            print_single_horizon(hor)
