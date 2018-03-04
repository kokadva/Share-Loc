
import geoalchemy2


def to_geometry_point(coordinates):
    return "SRID=4326;POINT({longitude} {latitude})".\
        format(longitude=coordinates[0], latitude=coordinates[1])