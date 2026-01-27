# Part 2: Prefix Matching
# Generic codes (without region) match all variants

part = 2

test_cases = [
    {
        "accept_header": "en",
        "supported": ["en-US", "fr-CA", "fr-FR"],
        "expected": ["en-US"]
    },
    {
        "accept_header": "fr",
        "supported": ["en-US", "fr-CA", "fr-FR"],
        "expected": ["fr-CA", "fr-FR"]
    },
    {
        "accept_header": "fr-FR, fr",
        "supported": ["en-US", "fr-CA", "fr-FR"],
        "expected": ["fr-FR", "fr-CA"]  # fr-FR exact first, then fr matches fr-CA
    },
    {
        "accept_header": "en, en-US",
        "supported": ["en-US", "en-GB"],
        "expected": ["en-US", "en-GB"]  # en matches both, en-US already matched
    },
]
