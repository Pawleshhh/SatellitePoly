import numpy as np
from satelliteutil import satellite_horizon_position, satellite_equatorial_position
from numpy.polynomial import Chebyshev
from datetime import timedelta

def poly_horizon_position(ts, start, interval, observer, satellite, degrees):
    date = start
    altitudes = []
    azimuths = []
    elevations = []
    seconds_axis = []
    for second in range(interval):
        time = ts.from_datetime(date)
        alt, az, mag = satellite_horizon_position(time, observer, satellite)
        altitudes.append(alt.degrees)
        azimuths.append(az.degrees)
        elevations.append(mag.m)
        seconds_axis.append(second)
        date = date + timedelta(seconds=1)
        
    polyfit_alt = Chebyshev.fit(seconds_axis, altitudes, deg=degrees)
    polyfit_az = Chebyshev.fit(seconds_axis, azimuths, deg=degrees)
    polyfit_el = Chebyshev.fit(seconds_axis, elevations, deg=degrees)

    return polyfit_alt, polyfit_az, polyfit_el

def poly_equatorial_position(ts, start, interval, observer, satellite, degrees):
    date = start
    right_ascensions = []
    declinations = []
    elevations = []
    seconds_axis = []
    for second in range(interval):
        time = ts.from_datetime(date)
        ra, dec, mag = satellite_equatorial_position(time, observer, satellite)
        right_ascensions.append(ra._degrees)
        declinations.append(dec.degrees)
        elevations.append(mag.m)
        seconds_axis.append(second)
        date = date + timedelta(seconds=1)
        
    polyfit_ra = Chebyshev.fit(seconds_axis, right_ascensions, deg=degrees)
    polyfit_dec = Chebyshev.fit(seconds_axis, declinations, deg=degrees)
    polyfit_el = Chebyshev.fit(seconds_axis, elevations, deg=degrees)

    return polyfit_ra, polyfit_dec, polyfit_el

def get_coefficients(cheb_poly):
    return np.polynomial.chebyshev.cheb2poly(cheb_poly.coef)