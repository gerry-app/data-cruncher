import GeoJsonCountryGridCreater as i

c = i.GeoJsonCountryGridCreater('^', 'districts/cds/2016/')
# print i.image_string(c.get_country_grid_with_more_info())
s = c.get_country_grid_with_more_info()

print s.copy_array()
