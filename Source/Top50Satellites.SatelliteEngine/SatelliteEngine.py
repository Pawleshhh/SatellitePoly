from skyfield.api import load
from skyfield.timelib import Time

def getTimescale():
    return load.timescale()

def getSatellites(tle_path):
    return load.tle_file(tle_path)

def howOldInDays(ts, year, month, day, hour, minute, second, satelliteEpoch):
    return abs(ts.utc(year, month, day, hour, minute, second) - satelliteEpoch)

def createSkyfieldTime(ts, epoch):
    return Time(ts, epoch)


ts = load.timescale()

print(howOldInDays(ts, 2022, 11, 24, 0, 0, 0, Time(ts, 2459888.0334955659)))