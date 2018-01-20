import os
import json
import GeoJsonStateGridCreater as g

def strip_zeroes(matrix):
    return [row for row in matrix if any(map(bool, row)) > 0]

states = {}
for state_code in os.listdir('./districts/states'):
    print state_code
    a = g.GeoJsonStateGridCreater('^' + state_code, start_directory='./districts/cds/2016')
    states[state_code] = strip_zeroes(a.get_state_array_more_info())

with open('states.json', 'w') as f:
    f.write(json.dumps(str(states)))
    
