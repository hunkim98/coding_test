# Part 2: Build a staticmap request payload with a path
# Task: Create a map request with a path from the first 10 coordinates
#
# Expected output structure:
# {
#     "center": {"lat": <center_lat>, "lon": <center_lon>},
#     "width": 600,
#     "height": 400,
#     "zoom": 13,
#     "paths": [
#         {
#             "color": "blue",
#             "positions": [
#                 {"lat": 47.55126, "lon": -122.2851},
#                 ... (10 positions total)
#             ]
#         }
#     ]
# }
#
# Center should be the average of all coordinates in the path

part = 2
ride_file = "ride_data.json"
num_coordinates = 10
path_color = "blue"
width = 600
height = 400
zoom = 13
