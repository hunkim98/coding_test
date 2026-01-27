# Part 3: Wildcards
# * matches any remaining unmatched languages

part = 3

test_cases = [
    {
        "accept_header": "en-US, *",
        "supported": ["en-US", "fr-CA", "fr-FR"],
        "expected": ["en-US", "fr-CA", "fr-FR"]
    },
    {
        "accept_header": "fr-FR, fr, *",
        "supported": ["en-US", "fr-CA", "fr-FR"],
        "expected": ["fr-FR", "fr-CA", "en-US"]
    },
    {
        "accept_header": "*",
        "supported": ["en-US", "fr-FR", "es-ES"],
        "expected": ["en-US", "fr-FR", "es-ES"]
    },
    {
        "accept_header": "*, en-US",
        "supported": ["en-US", "fr-FR"],
        "expected": ["en-US", "fr-FR"]  # * comes first, gets everything
    },
]
