import arcpy

# Set environment settings
arcpy.env.workspace = r"C:\Users\roypr\OneDrive\Documents\ArcGIS\Projects\MyProject11"  # Replace with the path to your workspace

# Define paths to input .jpg layers
topography_jpg = r"C:\Users\roypr\OneDrive\Documents\ArcGIS\Projects\MyProject11\topography.jpg"
geology_jpg = r"C:\Users\roypr\OneDrive\Documents\ArcGIS\Projects\MyProject11\geology.jpg"
water_ice_jpg = r"C:\Users\roypr\OneDrive\Documents\ArcGIS\Projects\MyProject11\water ice.jpg"
minerals_jpg = r"C:\Users\roypr\OneDrive\Documents\ArcGIS\Projects\MyProject11\minerals.jpg"
elevation_jpg = r"C:\Users\roypr\OneDrive\Documents\ArcGIS\Projects\MyProject11\elevation.jpg"

# Load .jpg layers into ArcGIS Pro
arcpy.management.MakeRasterLayer(topography_jpg, "topography")
arcpy.management.MakeRasterLayer(geology_jpg, "geology")
arcpy.management.MakeRasterLayer(water_ice_jpg, "water_ice")
arcpy.management.MakeRasterLayer(minerals_jpg, "minerals")
arcpy.management.MakeRasterLayer(elevation_jpg, "elevation")

import arcpy

# Set environment settings
arcpy.env.workspace = r"C:\Users\roypr\OneDrive\Documents\ArcGIS\Projects\MyProject11"  # Replace with the path to your workspace

# Define paths to input .jpg files and output rasters
input_jpgs = [
    r"C:\Users\roypr\OneDrive\Documents\ArcGIS\Projects\MyProject11\topography.jpg",
    r"C:\Users\roypr\OneDrive\Documents\ArcGIS\Projects\MyProject11\geology.jpg",
    r"C:\Users\roypr\OneDrive\Documents\ArcGIS\Projects\MyProject11\water ice.jpg",
    r"C:\Users\roypr\OneDrive\Documents\ArcGIS\Projects\MyProject11\minerals.jpg",
    r"C:\Users\roypr\OneDrive\Documents\ArcGIS\Projects\MyProject11\elevation.jpg"
]
output_rasters = [
    r"C:\Users\roypr\OneDrive\Documents\ArcGIS\Projects\MyProject11\topography.tif",
    r"C:\Users\roypr\OneDrive\Documents\ArcGIS\Projects\MyProject11\geology.tif",
    r"C:\Users\roypr\OneDrive\Documents\ArcGIS\Projects\MyProject11\water_ice.tif",
    r"C:\Users\roypr\OneDrive\Documents\ArcGIS\Projects\MyProject11\minerals.tif",
    r"C:\Users\roypr\OneDrive\Documents\ArcGIS\Projects\MyProject11\elevation.tif"
]

# Iterate through each .jpg file
for input_jpg, output_raster in zip(input_jpgs, output_rasters):
    # Convert .jpg to raster
    arcpy.management.CopyRaster(input_jpg, output_raster)

print("Conversion from .jpg to raster complete for all files.")

import arcpy

# Set environment settings
arcpy.env.workspace = r"C:\Users\roypr\OneDrive\Documents\ArcGIS\Projects\MyProject11"  # Replace with the path to your workspace

# Define paths to input raster layers
input_rasters = [
    r"C:\Users\roypr\OneDrive\Documents\ArcGIS\Projects\MyProject11\topography.tif",
    r"C:\Users\roypr\OneDrive\Documents\ArcGIS\Projects\MyProject11\geology.tif",
    r"C:\Users\roypr\OneDrive\Documents\ArcGIS\Projects\MyProject11\water_ice.tif",
    r"C:\Users\roypr\OneDrive\Documents\ArcGIS\Projects\MyProject11\minerals.tif",
    r"C:\Users\roypr\OneDrive\Documents\ArcGIS\Projects\MyProject11\elevation.tif"
]

# List to store shapes of all layers
shapes = []

# Iterate through each raster layer and retrieve its shape
for input_raster in input_rasters:
    # Convert raster to NumPy array
    raster_array = arcpy.RasterToNumPyArray(input_raster)
    # Get shape of the array
    shape = raster_array.shape
    # Add shape to the list
    shapes.append(shape)

# Print shapes of all layers
for i, shape in enumerate(shapes, start=1):
    print(f"Shape of layer {i}: {shape}")

import numpy as np

# Shapes of arrays
shapes = [
    (3, 1048, 2378),
    (3, 1086, 2396),
    (3, 1084, 2392),
    (3, 1084, 2396),
    (3, 1080, 2396)
]

# Find the maximum dimensions
max_shape = np.max(shapes, axis=0)

# Resize each array to the maximum dimensions
resized_arrays = []
for shape in shapes:
    resized_array = np.zeros(max_shape)
    resized_array[:, :shape[1], :shape[2]] = np.zeros(shape)

    resized_arrays.append(resized_array)

# Convert the list of resized arrays into a NumPy array
stacked_array = np.stack(resized_arrays)

# Print the shape of the resulting array
print("Shape of the stacked array:", stacked_array.shape)

import numpy as np

# Stacked array of resized arrays
stacked_array = np.zeros((5, 3, 1086, 2396))  # Example stacked array

# Define criteria for mineral exploration
# Example criteria: check if elevation is above a threshold, geology type matches, and presence of water ice and target mineral
elevation_threshold = 500
target_geology = "noachian volcanic unit"
target_mineral = "hydrated minerals"
water_ice_threshold = 0.5  # Example threshold for water ice presence

# Apply criteria to the stacked array
exploration_criteria = (
    (stacked_array[4] > elevation_threshold) &  # Elevation above threshold
    (stacked_array[1] == target_geology) &  # Geology type matches target
    (stacked_array[2] > water_ice_threshold) &  # Water ice presence
    (stacked_array[3] == target_mineral)  # Target mineral present
)

# Print the exploration criteria
print("Exploration criteria array shape:", exploration_criteria.shape)
print("Example exploration criteria array:", exploration_criteria)


