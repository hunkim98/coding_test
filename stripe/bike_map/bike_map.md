# Bike Map Challenge

## Background

You are building a tool for a bike-sharing company that needs to visualize bicycle rides on a map. The ride data is stored in GeoJSON format, and you need to transform it into a format that can be sent to a map rendering API.

The challenge has three parts:

1. **Parse Coordinates**: Extract coordinates from GeoJSON data
2. **Build Map Request**: Construct an API request payload with a path
3. **Add Markers**: Include landmark markers on the map

---

## Input Data Formats

### GeoJSON Ride Data (`ride_data.json`)

Bicycle ride coordinates are stored in GeoJSON format. The coordinates are in `[longitude, latitude]` order (this is the GeoJSON standard).

```json
{
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "geometry": {
                "type": "LineString",
                "coordinates": [
                    [-122.2851, 47.55126],
                    [-122.28531, 47.55126],
                    ...
                ]
            }
        }
    ]
}
```

### Landmarks Data (`landmarks.json`)

Landmark locations with names and coordinates:

```json
{
    "landmarks": [
        {
            "place": "Dearborn Park",
            "latitude": 47.552376,
            "longitude": -122.294496
        },
        ...
    ]
}
```

### Map API Request Format

The map API expects coordinates in `{lat, lon}` object format:

```json
{
    "center": {"lat": 47.58, "lon": -122.31},
    "width": 600,
    "height": 400,
    "zoom": 13,
    "paths": [
        {
            "color": "blue",
            "positions": [
                {"lat": 47.55126, "lon": -122.2851},
                ...
            ]
        }
    ],
    "markers": [
        {
            "label": "Dearborn Park",
            "color": "blue",
            "coord": {"lat": 47.552376, "lon": -122.294496}
        }
    ]
}
```

**Important**: GeoJSON uses `[longitude, latitude]` but the API uses `{lat, lon}`. You must convert!

---

## Part 1: Parse Coordinates

### Goal

Write a function `parse_coordinates(ride_file, n)` that:
1. Reads the GeoJSON file
2. Extracts the first `n` coordinates
3. Converts from `[lon, lat]` to `{"lat": ..., "lon": ...}` format

### Example

Input:
```python
ride_file = "ride_data.json"
n = 5
```

Output:
```python
[
    {"lat": 47.55126, "lon": -122.2851},
    {"lat": 47.55126, "lon": -122.28531},
    {"lat": 47.55126, "lon": -122.28565},
    {"lat": 47.55126, "lon": -122.28631},
    {"lat": 47.55127, "lon": -122.28767}
]
```

### Requirements

- Read and parse JSON file
- Navigate to `features[0].geometry.coordinates`
- Take the first `n` coordinates
- Convert `[lon, lat]` → `{"lat": lat, "lon": lon}`

---

## Part 2: Build Map Request

### Goal

Write a function `build_map_request(ride_file, num_coordinates, path_color, width, height, zoom)` that builds a complete API request payload.

### Example

Input:
```python
ride_file = "ride_data.json"
num_coordinates = 10
path_color = "blue"
width = 600
height = 400
zoom = 13
```

Output:
```python
{
    "center": {"lat": 47.55106, "lon": -122.28996},  # average of coordinates
    "width": 600,
    "height": 400,
    "zoom": 13,
    "paths": [
        {
            "color": "blue",
            "positions": [
                {"lat": 47.55126, "lon": -122.2851},
                {"lat": 47.55126, "lon": -122.28531},
                # ... 10 positions total
            ]
        }
    ]
}
```

### Requirements

- Use `parse_coordinates` from Part 1 to get positions
- Calculate `center` as the average lat/lon of all positions
- Build the complete request structure with paths array

---

## Part 3: Add Markers

### Goal

Write a function `build_map_with_markers(ride_file, landmarks_file, path_color, marker_color, width, height, zoom)` that includes both the path AND landmark markers.

### Example

Input:
```python
ride_file = "ride_data.json"
landmarks_file = "landmarks.json"
path_color = "red"
marker_color = "blue"
width = 800
height = 600
zoom = 12
```

Output:
```python
{
    "center": {"lat": 47.58, "lon": -122.31},
    "width": 800,
    "height": 600,
    "zoom": 12,
    "paths": [
        {
            "color": "red",
            "positions": [...]  # ALL coordinates from ride
        }
    ],
    "markers": [
        {
            "label": "Dearborn Park",
            "color": "blue",
            "coord": {"lat": 47.552376, "lon": -122.294496}
        },
        {
            "label": "The Flora Bakehouse",
            "color": "blue",
            "coord": {"lat": 47.553513, "lon": -122.311713}
        },
        # ... all landmarks
    ]
}
```

### Requirements

- Use ALL coordinates from the ride (not just first N)
- Read landmarks from the landmarks file
- Convert landmark format to marker format with `label`, `color`, `coord`
- Include both `paths` and `markers` arrays in output

---

## Function Signatures

```python
from typing import List, Dict, Any

def parse_coordinates(ride_file: str, n: int) -> List[Dict[str, float]]:
    """Parse GeoJSON and return first n coordinates as {lat, lon} dicts."""
    pass

def build_map_request(
    ride_file: str,
    num_coordinates: int,
    path_color: str,
    width: int,
    height: int,
    zoom: int
) -> Dict[str, Any]:
    """Build map API request with a path."""
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
    """Build map API request with path and markers."""
    pass
```

---

## Tips

1. **Coordinate order matters**: GeoJSON is `[longitude, latitude]`, but the API wants `{lat, lon}`
2. **JSON parsing**: Use your language's JSON library to parse files
3. **Calculate center**: Average all latitudes for center lat, average all longitudes for center lon
4. **Build incrementally**: Part 2 builds on Part 1, Part 3 builds on Part 2
