# Part 3: Add markers from landmarks
# Task: Build a complete map request with path AND markers
#
# Expected output structure:
# {
#     "center": {"lat": <center_lat>, "lon": <center_lon>},
#     "width": 800,
#     "height": 600,
#     "zoom": 12,
#     "paths": [
#         {
#             "color": "red",
#             "positions": [...all coordinates from ride...]
#         }
#     ],
#     "markers": [
#         {"label": "Dearborn Park", "color": "blue", "coord": {"lat": 47.552376, "lon": -122.294496}},
#         {"label": "The Flora Bakehouse", "color": "blue", "coord": {"lat": 47.553513, "lon": -122.311713}},
#         ... (all landmarks)
#     ]
# }

part = 3
ride_file = "ride_data.json"
landmarks_file = "landmarks.json"
path_color = "red"
marker_color = "blue"
width = 800
height = 600
zoom = 12
