import os

def command_runner(filename):
    print 'Processing district {}... '.format(os.path.dirname(filename)),
    import GeoJsonPreProcessor
    preprocessor = GeoJsonPreProcessor.GeoJsonPreProcessor(filename)
    preprocessor.run()

    import GeoJsonDistrictGridCreater
    grid_creater = GeoJsonDistrictGridCreater.GeoJsonDistrictGridCreater(os.path.join(os.path.dirname(filename), 'preprocessed.txt'), debug=False)
    district_image = GeoJsonDistrictGridCreater.image_string(grid_creater.get_district_grid())

    with open(os.path.join(os.path.dirname(filename), 'district_image.txt'), 'w') as file_handler:
        file_handler.write(district_image)

    print 'Done!'
