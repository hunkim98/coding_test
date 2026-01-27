# Part 1: Exact Matches
# Only exact string matches count

part = 1

test_cases = [
    {
        "accept_header": "en-US, fr-CA, fr-FR",
        "supported": ["fr-FR", "en-US"],
        "expected": ["en-US", "fr-FR"]
    },
    {
        "accept_header": "fr-CA, fr-FR",
        "supported": ["en-US", "fr-FR"],
        "expected": ["fr-FR"]
    },
    {
        "accept_header": "en-US",
        "supported": ["en-US", "fr-CA"],
        "expected": ["en-US"]
    },
    {
        "accept_header": "de-DE, es-ES",
        "supported": ["en-US", "fr-FR"],
        "expected": []  # No matches
    },
]
