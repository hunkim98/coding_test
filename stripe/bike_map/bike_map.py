"""
Bike Map Challenge

Build a tool that reads bicycle ride data (GeoJSON format) and constructs
a request payload for a map visualization API.

Part 1: Parse GeoJSON and extract coordinates
Part 2: Build a map request payload with a path
Part 3: Add markers from landmarks file

Key insight: GeoJSON coordinates are [longitude, latitude], but the
staticmap API expects {lat, lon} objects.
"""

import json
from typing import List, Dict, Any

# Change this import to test different parts
from inputs1 import *
# from inputs2 import *
# from inputs3 import *


def parse_coordinates(ride_file: str, n: int) -> List[Dict[str, float]]:
    """
    Part 1: Parse GeoJSON file and extract first N coordinates.

    GeoJSON format: coordinates are [longitude, latitude]
    Output format: [{"lat": float, "lon": float}, ...]

    Args:
        ride_file: Path to the GeoJSON file
        n: Number of coordinates to extract

    Returns:
        List of coordinate dicts with lat/lon keys
    """
    # -----------------------------
    # Your implementation here
    # -----------------------------
    pass


def build_map_request(
    ride_file: str,
    num_coordinates: int,
    path_color: str,
    width: int,
    height: int,
    zoom: int
) -> Dict[str, Any]:
    """
    Part 2: Build a staticmap API request payload with a path.

    The request should include:
    - center: average lat/lon of all path coordinates
    - width, height, zoom: as provided
    - paths: array with one path object containing color and positions

    Args:
        ride_file: Path to the GeoJSON file
        num_coordinates: Number of coordinates to use for the path
        path_color: Color for the path
        width, height: Map dimensions
        zoom: Map zoom level

    Returns:
        Dict representing the API request payload
    """
    # -----------------------------
    # Your implementation here
    # -----------------------------
    pass


def build_map_with_markers(
    ride_file: str,
    landmarks_file: str,
    path_color: str,
    marker_color: str,
    width: int,
    height: int,
    zoom: int
) -> Dict[str, Any]:
    """
    Part 3: Build a complete map request with path AND markers.

    The request should include:
    - center: average lat/lon of all path coordinates
    - width, height, zoom: as provided
    - paths: array with path from ALL coordinates in ride file
    - markers: array with all landmarks, each having label, color, coord

    Args:
        ride_file: Path to the GeoJSON file
        landmarks_file: Path to the landmarks JSON file
        path_color: Color for the path
        marker_color: Color for all markers
        width, height: Map dimensions
        zoom: Map zoom level

    Returns:
        Dict representing the API request payload
    """
    # -----------------------------
    # Your implementation here
    # -----------------------------
    pass


# Test runner
if __name__ == "__main__":
    if part == 1:
        result = parse_coordinates(ride_file, num_coordinates)
        print("Extracted coordinates:")
        print(json.dumps(result, indent=2))
        # Expected: 5 coordinate objects with lat/lon

    elif part == 2:
        result = build_map_request(
            ride_file, num_coordinates, path_color, width, height, zoom
        )
        print("Map request payload:")
        print(json.dumps(result, indent=2))
        # Expected: Complete map request with center, dimensions, and path

    elif part == 3:
        result = build_map_with_markers(
            ride_file, landmarks_file, path_color, marker_color, width, height, zoom
        )
        print("Map request with markers:")
        print(json.dumps(result, indent=2))
        # Expected: Complete map request with path and markers
