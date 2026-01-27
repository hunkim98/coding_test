# Part 1: Parse GeoJSON and extract first N coordinates
# Task: Read ride_data.json, extract the first 5 coordinates
# Note: GeoJSON uses [longitude, latitude] order!
#
# Expected output:
# [
#     {"lat": 47.55126, "lon": -122.2851},
#     {"lat": 47.55126, "lon": -122.28531},
#     {"lat": 47.55126, "lon": -122.28565},
#     {"lat": 47.55126, "lon": -122.28631},
#     {"lat": 47.55127, "lon": -122.28767}
# ]

part = 1
ride_file = "ride_data.json"
num_coordinates = 5
