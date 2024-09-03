# Adapted from CoastWatch Python tutorial https://github.com/coastwatch-training/CoastWatch-Tutorials/blob/main/extract-satellite-data-within-boundary/Python/extract-satellite-data-within-boundary.ipynb

# Given an xarray n dimensional dataset and a geopandas geodataframe, 
# the xarray dataset will mask all values outside of the desired shape with nans

# Note this only works for a single shape.
# If your geodataframe has multiple polygons you can loop through each one.

# data is an N dimensional xarray dataset
# longitude name is a string of the variable name for longitude in data
# latitude name is a string of the variable name for latitude in data
# shape is a geodataframe


import regionmask

def crop_nd(data, longitude_name, latitude_name, shape):
    
    # Get the region of interest
    region = regionmask.from_geopandas(shape)
    
    # Create the mask
    mask = region.mask(data[longitude_name].astype('f4'), data[latitude_name].astype('f4'))
    
    # Apply mask to the data
    masked_ds = data.where(mask == region.numbers[0])
    
    return masked_ds