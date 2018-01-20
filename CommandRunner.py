import os

def command_runner(filename):
    print 'Processing district {}... '.format(os.path.dirname(filename)),
    import GeoJsonPreProcessor
    preprocessor = GeoJsonPreProcessor.GeoJsonPreProcessor(filename)
    preprocessor.run()

    import GeoJsonGridCreater
    grid_creater = GeoJsonGridCreater.GeoJsonGridCreater(os.path.join(os.path.dirname(filename), 'preprocessed.txt'), debug=False)
    district_image = GeoJsonGridCreater.create_image(grid_creater.get_district_grid())

    with open(os.path.join(os.path.dirname(filename), 'district_image.txt'), 'w') as file_handler:
        file_handler.write(district_image)

    print 'Done!'
