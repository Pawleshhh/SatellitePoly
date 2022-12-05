from modules.satelliteutil import satellite_horizon_position
from numpy.polynomial import Chebyshev
import numpy as np
from datetime import timedelta

def get_polynomials_of_horizon_position(ts, start, interval, observator, satellite, degrees):
    date = start
    altitudes = []
    azimuths = []
    elevations = []
    seconds_axis = []
    for second in range(interval):
        time = ts.from_datetime(date)
        alt, az, mag = satellite_horizon_position(time, observator, satellite)
        altitudes.append(alt.degrees)
        azimuths.append(az.degrees)
        elevations.append(mag.m)
        seconds_axis.append(second)
        date = date + timedelta(seconds=1)
        
    polyfit_alt = Chebyshev.fit(seconds_axis, altitudes, deg=degrees)
    polyfit_az = Chebyshev.fit(seconds_axis, azimuths, deg=degrees)
    polyfit_el = Chebyshev.fit(seconds_axis, elevations, deg=degrees)

    return polyfit_alt, polyfit_az, polyfit_el

def get_coefficients(cheb_poly):
    return np.polynomial.chebyshev.cheb2poly(cheb_poly.coef)