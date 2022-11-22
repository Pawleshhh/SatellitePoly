from skyfield.api import load

def getSatellites(tle_path):
    return load.tle_file(tle_path)

def howOldInDays(year, month, day, hour, minute, second, satelliteEpoch):
    ts = load.timescale()
    return abs(ts.utc(year, month, day, hour, minute, second) - satelliteEpoch)