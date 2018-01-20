import os
import re

import GeoJsonDistrictGridCreater
import Screen

def print_matrix(matrix):
    for row in matrix:
        print row

def print_image(image):
    print image_string(image, add_newline=True)

def image_string(image, add_newline=False):
    string = ''
    for row in image:
        string += (''.join(map(str, row))).replace('0', ' ')
        if add_newline:
            string += '\n'
    return string.rstrip()

class GeoJsonStateGridCreater(object):

    def __init__(self, directory_pattern, start_directory='.', matrix_border_offset=3, debug=True):
        self.directories = self.get_directories(start_directory, directory_pattern)
        self.matrix_border_offset = matrix_border_offset
        self.debug = debug

    def get_directories(self, start_directory, directory_pattern):
        all_directories = os.listdir(start_directory)
        relevant_directories = [os.path.join(start_directory, directory) for directory in all_directories if re.match(directory_pattern, os.path.basename(directory.strip('/')))]
        return relevant_directories

    def print_if_debug(self, message):
        if self.debug:
            print message

    def get_screen_info(self, coordinates_list):
        xcor_temp_list = [pair[0] for pair in coordinates_list]
        ycor_temp_list = [pair[1] for pair in coordinates_list]

        min_xcor = min(xcor_temp_list)
        max_xcor = max(xcor_temp_list)
        min_ycor = min(ycor_temp_list)
        max_ycor = max(ycor_temp_list)

        x_range = int((max_xcor - min_xcor) * 10) + 1
        y_range = int((max_ycor - min_ycor) * 10) + 1
        return min_xcor, min_ycor, x_range, y_range

    def get_state_grid(self):
        state_grid_coordinates = self.get_state_grid_coordinates()
        min_xcor, min_ycor, x_range, y_range = self.get_screen_info(state_grid_coordinates)

        grid = Screen.Screen(x_range + 2 * self.matrix_border_offset, y_range + 2 * self.matrix_border_offset)
        self.print_if_debug('Building state screen...')
        for coordinate in state_grid_coordinates:
            xcor = int((coordinate[0] - min_xcor) * 10) + self.matrix_border_offset
            ycor = y_range + self.matrix_border_offset - int((coordinate[1] - min_ycor) * 10)
            grid.plot(xcor, ycor)
        return grid

    def get_state_grid_coordinates(self):
        state_grid_coordinates = []
        for index, directory in enumerate(self.directories):
            file_path = os.path.join(directory, 'preprocessed.txt')
            self.print_if_debug('Processing district {}/{}'.format(index + 1, len(self.directories)))
            district_grid_creater = GeoJsonDistrictGridCreater.GeoJsonDistrictGridCreater(file_path)
            state_grid_coordinates.extend(district_grid_creater.get_district_grid_coordinates())
        return state_grid_coordinates

    def get_state_array_more_info(self):
        state_grid_coordinates = self.get_state_grid_coordinates()
        min_xcor, min_ycor, x_range, y_range = self.get_screen_info(state_grid_coordinates)

        state_grid = self.get_state_grid()
        state_array_more_info = state_grid.copy_array()

        state_grid_coordinates_dict = {}
        for index, directory in enumerate(self.directories):
            file_path = os.path.join(directory, 'preprocessed.txt')
            self.print_if_debug('Processing district {}/{}'.format(index + 1, len(self.directories)))
            district_grid_creater = GeoJsonDistrictGridCreater.GeoJsonDistrictGridCreater(file_path)
            state_grid_coordinates_dict[os.path.basename(directory.strip('/'))] = district_grid_creater.get_district_grid_coordinates()

        for name, coordinates_list in state_grid_coordinates_dict.items():
            for coordinate in coordinates_list:
                xcor = int((coordinate[0] - min_xcor) * 10) + self.matrix_border_offset
                ycor = y_range + self.matrix_border_offset - int((coordinate[1] - min_ycor) * 10)
                state_array_more_info[ycor][xcor] = name
        return state_array_more_info
