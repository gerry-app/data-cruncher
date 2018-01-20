import GeoJsonCountryGridCreater as i

c = i.GeoJsonCountryGridCreater('^', 'districts/cds/2016/')
i.image_string(c.get_country_grid())
