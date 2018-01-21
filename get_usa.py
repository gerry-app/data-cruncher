import GeoJsonCountryGridCreater as i

c = i.GeoJsonCountryGridCreater('^', 'districts/cds/2016/')
# print i.image_string(c.get_country_grid_with_more_info())
s = c.get_country_grid_with_more_info()

def strip_zeroes(matrix):
    return [row for row in matrix if any(map(bool, row)) > 0]

a = strip_zeroes(s.copy_array())
with open('usa.json', 'w') as f:
    json.dump(a, f)
