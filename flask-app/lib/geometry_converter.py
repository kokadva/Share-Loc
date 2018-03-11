def to_geometry_point(coordinates):
    return "SRID=4326;POINT({longitude} {latitude})".\
        format(longitude=coordinates[0], latitude=coordinates[1])


def to_geometry_polygon(coordinates):
    str_geometry = ""
    for k in range(len(coordinates)):
        str_geometry += str(coordinates[k][0]) + " " + str(coordinates[k][1])
        if k == len(coordinates) - 1:
            break
        str_geometry += ','
    return "SRID=4326;POLYGON(({}))".format(str_geometry)
