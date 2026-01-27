# Part 4: Quality Scores (q-factors)
# Sort by q-value descending, use stable sort for ties

part = 4

test_cases = [
    {
        "accept_header": "fr-FR;q=1, fr-CA;q=0, fr;q=0.5",
        "supported": ["fr-FR", "fr-CA", "fr-BG"],
        "expected": ["fr-FR", "fr-BG", "fr-CA"]
        # fr-FR: 1.0, fr-BG (via fr): 0.5, fr-CA: 0
    },
    {
        "accept_header": "fr-FR;q=1, fr-CA;q=0, *;q=0.5",
        "supported": ["fr-FR", "fr-CA", "fr-BG", "en-US"],
        "expected": ["fr-FR", "fr-BG", "en-US", "fr-CA"]
    },
    {
        "accept_header": "en;q=0.8, fr;q=0.9, de;q=0.7",
        "supported": ["en-US", "fr-FR", "de-DE"],
        "expected": ["fr-FR", "en-US", "de-DE"]
        # Sorted: 0.9, 0.8, 0.7
    },
    {
        "accept_header": "en-US, fr-FR;q=0.8, es-ES;q=0.8",
        "supported": ["en-US", "fr-FR", "es-ES"],
        "expected": ["en-US", "fr-FR", "es-ES"]
        # en-US: 1.0, fr-FR and es-ES tie at 0.8 (stable sort)
    },
]
