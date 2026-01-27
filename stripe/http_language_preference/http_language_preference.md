# HTTP Request Language Matching

## Problem Description

You are building a system that serves content to users in their preferred language. When a browser sends an HTTP request, it includes an `Accept-Language` header listing languages the user prefers, in order of preference.

Your server has a list of supported languages. You need to determine which of the user's requested languages you can provide, maintaining the user's preference order.

---

## Input Format

Your function takes two inputs:

1. **Accept-Language Header** (string): Comma-separated language tags
   - Example: `"en-US, fr-CA, fr-FR"`

2. **Supported Languages** (list): Languages your server provides
   - Example: `["en-US", "fr-FR", "es-ES"]`

## Output Format

Return a list of language tags that:
- Match the user's request (based on the rules for each part)
- Are supported by your server
- Maintain the user's preference order

---

## Part 1: Exact Matches

### Description

Match language tags exactly. `"en-US"` only matches `"en-US"`, not `"en"` or `"en-GB"`.

### Function Signature

```python
def parse_accept_language(accept_header: str, supported_languages: List[str]) -> List[str]:
```

### Sample Input/Output

```python
parse_accept_language("en-US, fr-CA, fr-FR", ["fr-FR", "en-US"])
# Returns: ["en-US", "fr-FR"]

parse_accept_language("fr-CA, fr-FR", ["en-US", "fr-FR"])
# Returns: ["fr-FR"]

parse_accept_language("en-US", ["en-US", "fr-CA"])
# Returns: ["en-US"]
```

### Rules

- Split header by commas, trim whitespace
- Return matches in header's preference order
- Return empty list if no matches

---

## Part 2: Prefix Matching

### Description

Allow generic language codes (without region) to match specific variants.

- `"en"` matches `"en-US"`, `"en-GB"`, etc.
- Exact matches take priority over prefix matches

### Sample Input/Output

```python
parse_accept_language("en", ["en-US", "fr-CA", "fr-FR"])
# Returns: ["en-US"]

parse_accept_language("fr", ["en-US", "fr-CA", "fr-FR"])
# Returns: ["fr-CA", "fr-FR"]

parse_accept_language("fr-FR, fr", ["en-US", "fr-CA", "fr-FR"])
# Returns: ["fr-FR", "fr-CA"]
# fr-FR is exact match (first), fr matches fr-CA (fr-FR already used)
```

### Rules

- Check exact match first
- If no exact match AND tag has no hyphen, match all `{tag}-*` variants
- No duplicates in result
- Maintain preference order

---

## Part 3: Wildcards

### Description

Handle the `*` wildcard, which means "any language not yet matched."

### Sample Input/Output

```python
parse_accept_language("en-US, *", ["en-US", "fr-CA", "fr-FR"])
# Returns: ["en-US", "fr-CA", "fr-FR"]

parse_accept_language("fr-FR, fr, *", ["en-US", "fr-CA", "fr-FR"])
# Returns: ["fr-FR", "fr-CA", "en-US"]

parse_accept_language("*", ["en-US", "fr-FR", "es-ES"])
# Returns: ["en-US", "fr-FR", "es-ES"]
```

### Rules

- When `*` is encountered, add all remaining unmatched supported languages
- Languages are added in the order they appear in the supported list
- `*` respects its position in the preference order

---

## Part 4: Quality Scores (q-factors)

### Description

Parse quality scores that indicate preference strength.

Format: `language;q=value` where value is 0.0 to 1.0

- Higher score = stronger preference
- No score = defaults to 1.0
- `q=0` = lowest priority (or excluded)

### Sample Input/Output

```python
parse_accept_language("fr-FR;q=1, fr-CA;q=0, fr;q=0.5", ["fr-FR", "fr-CA", "fr-BG"])
# Returns: ["fr-FR", "fr-BG", "fr-CA"]
# fr-FR: q=1.0, fr-BG (via "fr"): q=0.5, fr-CA: q=0

parse_accept_language("fr-FR;q=1, fr-CA;q=0, *;q=0.5", ["fr-FR", "fr-CA", "fr-BG", "en-US"])
# Returns: ["fr-FR", "fr-BG", "en-US", "fr-CA"]

parse_accept_language("en;q=0.8, fr;q=0.9, de;q=0.7", ["en-US", "fr-FR", "de-DE"])
# Returns: ["fr-FR", "en-US", "de-DE"]
# Sorted by q: 0.9, 0.8, 0.7
```

### Rules

- Parse `q=value` from each entry (default 1.0)
- Sort final results by q-value descending
- Use stable sort (equal scores maintain original order)
- Wildcards can also have q-values

---

## Constraints

- Header string length ≤ 1000 characters
- 1 ≤ supported languages ≤ 100
- Language tags follow standard format: `language` or `language-REGION`
- q-values are between 0.0 and 1.0

---

## Notes

- Each part builds on the previous
- Part 4 is the complete solution incorporating all rules
- Case sensitivity: assume case-sensitive matching (ask interviewer)
- Order matters: preference order is critical
