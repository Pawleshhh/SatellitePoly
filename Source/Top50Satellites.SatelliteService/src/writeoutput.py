from progress.bar import Bar

def create_row(values, separator = ','):
    row = ''
    length = len(values)
    for i, v in enumerate(values):
        row = row + str(v)
        if i < length - 1:
            row = row + separator

    return row

def create_coords_row(name, coords, separator = ','):
    row = name
    for x in coords:
        row = row + separator + str(x)
    return row

def write_rows(rows, f):
    for row in rows:
        f.write(row)
        f.write('\n')

def write_polynomials(output, polynomials, satellites, observator, start, interval, separator = ','):
    
    with open(output, 'w') as f:
        observator_row = create_row(['Observator coords', observator], separator)
        time_row = create_row(['Start date time', start, 'Interval in seconds', interval], separator)

        write_rows([observator_row, time_row], f)

        f.write('\n')

        write_bar = Bar("Generating output", max=len(polynomials))

        for (satellite, poly_of_altaz) in zip(satellites, polynomials):
            alt, az, el = poly_of_altaz
            max_length = max(len(el), max(len(alt), len(az)))

            sat_name_row = create_row(['Satellite', satellite.name], separator)
            
            headers_row = create_row(['Coordinates'] + ['x^' + str(i) for i in range(max_length)], separator)

            alt_row = create_coords_row("Altitude", alt, separator)
            az_row = create_coords_row("Azimuth", az, separator)
            el_row = create_coords_row("Elevation", el, separator)

            write_rows([sat_name_row, 
                        headers_row, 
                        alt_row, 
                        az_row, 
                        el_row], f)

            f.write('\n')
            write_bar.next()

        write_bar.finish()
