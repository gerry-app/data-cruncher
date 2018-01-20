import re

import draw
import Screen

def print_matrix(matrix):
    for row in matrix:
        print row

def print_image(matrix):
    for row in matrix:
        print (''.join(map(str, row))).replace('0', ' ')

def create_image(matrix):
    string = ''
    for row in matrix:
        string += (''.join(map(str, row))).replace('0', ' ')
    return string

class GeoJsonGridCreater(object):

    def __init__(self, filename, matrix_border_offset=5, debug=True):
        self.content = self.get_content(filename)
        self.total_polygons = self.get_total_polygons()
        self.debug = debug
        self.matrix_border_offset = matrix_border_offset

    def get_content(self, filename):
        with open(filename) as file_handler:
            file_content = file_handler.read()
        return file_content

    def get_total_polygons(self):
        pattern = re.compile('\n\n\n')
        count = 1
        match = pattern.search(self.content)
        while match:
            count += 1
            match = pattern.search(self.content, match.end())
        return count

    def print_if_debug(self, message):
        if self.debug:
            print message

    def process_coordinates_pair(self, pair_string):
        return map(lambda x: float(x[:x.find('.') + 3]), pair_string.split(','))

    def get_screen_info(self, coordinates_list):
        xcor_temp_list = [pair[0] for pair in coordinates_list]
        ycor_temp_list = [pair[1] for pair in coordinates_list]

        min_xcor = min(xcor_temp_list)
        max_xcor = max(xcor_temp_list)
        min_ycor = min(ycor_temp_list)
        max_ycor = max(ycor_temp_list)

        x_range = int((max_xcor - min_xcor) * 100) + 1
        y_range = int((max_ycor - min_ycor) * 100) + 1
        return min_xcor, min_ycor, x_range, y_range

    def getNthPolygonEdgeCoordinates(self, num):
        start = 0
        pattern = re.compile('\n\n\n')

        while num > 0:
            match = pattern.search(self.content, start)
            assert match is not None, 'Could not find polygon {}'.format(num)
            start = match.end()
            num -= 1
        match = pattern.search(self.content, start)
        end = match.start() if match else len(self.content)

        polygon_string = self.content[start:end]
        polygon_edge_coordinate_pairs = polygon_string.split('\n')
        polygon_edge_coordinates = map(self.process_coordinates_pair, polygon_edge_coordinate_pairs)
        return polygon_edge_coordinates

    def getNthPolygonGrid(self, num):
        polygon_edge_coordinates = self.getNthPolygonEdgeCoordinates(num)
        min_xcor, min_ycor, x_range, y_range = self.get_screen_info(polygon_edge_coordinates)

        grid = Screen.Screen(x_range + 2 * self.matrix_border_offset, y_range + 2 * self.matrix_border_offset)
        for index in xrange(len(polygon_edge_coordinates) - 1):
            coordinate_pair1, coordinate_pair2 = polygon_edge_coordinates[index:index+2]
            grid_x1 = int((coordinate_pair1[0] - min_xcor) * 100) + self.matrix_border_offset
            grid_y1 = int((coordinate_pair1[1] - min_ycor) * 100) + self.matrix_border_offset
            grid_x2 = int((coordinate_pair2[0] - min_xcor) * 100) + self.matrix_border_offset
            grid_y2 = int((coordinate_pair2[1] - min_ycor) * 100) + self.matrix_border_offset

            draw.draw_line(grid, grid_x1, grid_y1, grid_x2, grid_y2)
        draw.flood_fill(grid, 0, 0, 2, 0)
        first_interior_coordinate_match = re.search(' ', create_image(grid))
        while first_interior_coordinate_match is not None:
            num_of_elems_in_row = x_range + 2 * self.matrix_border_offset
            draw.flood_fill(grid,
                            first_interior_coordinate_match.start() % num_of_elems_in_row,
                            first_interior_coordinate_match.start() / num_of_elems_in_row, 1, 0)
            first_interior_coordinate_match = re.search(' ', create_image(grid))
        # draw.flood_fill(grid, 0, 0, 0, 2)
        return grid

    def getNthPolygonGridCoordinates(self, num):
        polygon_edge_coordinates = self.getNthPolygonEdgeCoordinates(num)
        grid = self.getNthPolygonGrid(num)

        grid_coordinates = []
        min_xcor, min_ycor, x_range, y_range = self.get_screen_info(polygon_edge_coordinates)
        for x in xrange(x_range + 2 * self.matrix_border_offset):
            for y in xrange(y_range + 2 * self.matrix_border_offset):
                if grid.get(x, y) == 1:
                    grid_coordinates.append(((x / 100.0) + min_xcor, (y / 100.0) + min_ycor))
        return grid_coordinates

    def getDistrictGrid(self):
        district_grid_coordinates = self.getDistrictGridCoordinates()
        min_xcor, min_ycor, x_range, y_range = self.get_screen_info(district_grid_coordinates)

        grid = Screen.Screen(x_range + 2 * self.matrix_border_offset, y_range + 2 * self.matrix_border_offset)
        self.print_if_debug('Building district screen...')
        for coordinate in district_grid_coordinates:
            xcor = int((coordinate[0] - min_xcor) * 100) + self.matrix_border_offset
            ycor = int((coordinate[1] - min_ycor) * 100) + self.matrix_border_offset
            grid.plot(xcor, ycor)
        return grid

    def getDistrictGridCoordinates(self):
        district_grid_coordinates = []
        for i in xrange(self.total_polygons):
            self.print_if_debug('Processing polygon {}/{}'.format(i, self.total_polygons))
            polygon_grid_coordinates = self.getNthPolygonGridCoordinates(i)
            district_grid_coordinates.extend(polygon_grid_coordinates)
        return district_grid_coordinates
