import json
import os

class GeoJsonPreProcessor(object):

    def __init__(self, filename):
        self.filename = filename
        self.coordinates_string = None

    def get_content(self):
        with open(self.filename) as _file:
            json_content = json.load(_file)
        return json_content

    def preprocess(self):
        json_content = self.get_content()
        raw_coordinates_list = json_content['geometry']['coordinates']

        coordinates_string = ''
        for shape_coordinates in raw_coordinates_list:
            for polygon_coordinates in shape_coordinates:
                for coordinate_pair in polygon_coordinates:
                    coordinates_string += '{}, {}\n'.format(*coordinate_pair)
                coordinates_string += '\n'
            coordinates_string += '\n'
        self.coordinates_string = coordinates_string.strip()
        return self.coordinates_string

    def save(self):
        assert self.coordinates_string is not None, 'Data has not been preprocessed!'
        file_parent_directory = os.path.dirname(self.filename)
        with open(os.path.join('preprocessed.txt'), 'w') as outstream:
            outstream.write(self.coordinates_string)
        return True

    def run(self):
        self.preprocess()
        self.save()
