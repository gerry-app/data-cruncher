def command_runner(filename):
    import GeoJsonPreProcessor
    preprocessor = GeoJsonPreProcessor.GeoJsonPreProcessor(filename)
    preprocessor.run()

    import GeoJsonGridCreater
    grid_creater = GeoJsonGridCreater.GeoJsonGridCreater(filename, debug=False)
    district_image = GeoJsonGridCreater.create_image(grid_creater.getDistrictGrid())

    import os
    with open(os.path.join(os.path.dirname(filename), 'district_image.txt'), 'w') as file_handler:
        file_handler.write(district_image)
