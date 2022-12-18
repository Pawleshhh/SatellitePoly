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

def coord_name(eq, index):

    names = None
    if eq == True:
        names = ['Right ascension', 'Declination']
    else:
        names = ['Altitude', 'Azimuth']

    names.append('Elevation')
    
    return names[index]

def write_polynomials(output, polynomials, satellites, observer, start, interval, eq, separator = ','):
    
    with open(output, 'w') as f:
        observer_row = create_row(['Observer coords', observer], separator)
        time_row = create_row(['Start date time', start, 'Interval in seconds', interval], separator)

        write_rows([observer_row, time_row], f)

        f.write('\n')

        write_bar = Bar("Generating output", max=len(polynomials))

        for (satellite, poly_of_altaz) in zip(satellites, polynomials):
            coord_x, coord_y, el = poly_of_altaz
            max_length = max(len(el), max(len(coord_x), len(coord_y)))

            sat_name_row = create_row(['Satellite', satellite.name], separator)
            
            headers_row = create_row(['Coordinates'] + ['x^' + str(i) for i in range(max_length)], separator)

            alt_row = create_coords_row(coord_name(eq, 0), coord_x, separator)
            az_row = create_coords_row(coord_name(eq, 1), coord_y, separator)
            el_row = create_coords_row(coord_name(eq, 2), el, separator)

            write_rows([sat_name_row, 
                        headers_row, 
                        alt_row, 
                        az_row, 
                        el_row], f)

            f.write('\n')
            write_bar.next()

        write_bar.finish()
