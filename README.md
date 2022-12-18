# SatellitePoly

Python project that generates satellite polynomials as a CSV file using the skyfield package.
The input for the generated polynomials are the seconds since the start of predicting satellites position.

## Requirements
- Python 3.11 or higher
- Packages:
  - [skyfield](https://rhodesmill.org/skyfield/)
  - [numpy](https://numpy.org/)
  - [python-dateutil](https://dateutil.readthedocs.io/en/stable/)
  - [progress](https://pypi.org/project/progress/)

## Usage

SatellitePoly is used in console with given arguments.

### Required arguments
- --load, -l - Loads satellite TLE data from specified location e.g., local file, website

### Additional arguments
- --output, -o - Localisation of program's output. Default is working directory of the program and the name of the file will be 'polynomials.csv'.
- --count, -c - Number of satellites to download starting from the beginning. Default is 1.
- --id - Single id of satellite to be downloaded and processed.
- --separator - Specifies separator for the output csv file.
- --observator, -b - Specifies localisation of the observer {latitude(degrees), longitude(degrees), elevation(meters)}. Geographic coordiantes are east positive. E.g., 30.1 12.1 232. By default all values are set to 0.
- --eq - Specifies that polynomials of equatorial coordiantes have to be generated. If not used, polynomials of horizontal coordiantes will be generated instead.
- --start, -s - Specifies starting date and time of predicting satellite position. Format - d/m/Y H:M:S z e.g 10/07/09 18:59:11 -0400. By default local system time is used at the beginning of running the program.
- --interval, -i - Seconds since --start. Default is 60.
- --degrees, -d - Specifies degrees of polynomials. Default is 3.