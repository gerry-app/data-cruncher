# data-cruncher

## Written by PChan

### What it does
Contains a variety of parsing function to view the shape.geojson files in the districts submodule in
different ways...

- View each state/district as a grid of 1s and 0s (where 1 marks the point as being part of the
  state/district)
- Generate a list of points for each state with the districts marked districtly
- Generate a list of points for the district

### Running it

Initialize/Update the submodule
```bash
$ git submodule init --recursive
$ git submodule update --recursive
```

In the root of the repo, you would find CommandMaster.py.  Some preprocessing work is needed before
running the parsing functions:
```bash
$ python CommandMaster.py
```

### Functions Available

#### GeoJsonDistrictGridCreater

Initialize an instance of the class:

```python
GeoJsonDistrictGridCreater.GeoJsonDistrictGridCreater(filename)
```

where filename is the name of the file you're interested in

```python
instance.get_district_grid()
```

return a grid where the district is plotted as a Screen class

```python
instance.get_district_array_more_info()
```

return an array where each point of the district is labeled by the district name

#### GeoJsonStateGridCreater

Initialize an instance of the class:

```python
GeoJsonStateGridCreater.GeoJsonStateGridCreater(filename)
```

where filename is the name of the file you're interested in

```python
instance.get_district_grid()
```

return a grid where the district is plotted as a Screen class

```python
instance.get_district_array_more_info()
```

return an array where each point of the district is labeled by the district name
