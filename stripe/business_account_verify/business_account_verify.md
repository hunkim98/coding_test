# Business Account Verification

## Problem Description

You are building a Know Your Customer (KYC) system that verifies new business accounts. The system reads business data from a CSV string and determines if each account should be VERIFIED or NOT VERIFIED based on multiple validation rules.

Complete the function `validate_businesses(csv_data)` that applies validation rules incrementally across 5 parts.

---

## Input Format

A CSV string with the following structure:

```
col1,col2,col3,col4,col5,col6
BIZ001,Legal Name,website.com,Short Desc,Full Description,Product Details
```

**Columns:**
- `col1`: Business ID
- `col2`: Legal Name (used in output)
- `col3`: Website URL
- `col4`: Short Description
- `col5`: Full Description (main validation target)
- `col6`: Product Details

The first row is always the header and should be skipped.

---

## Output Format

For each business row (in order), output one line:

```
VERIFIED: <business_name>
```
or
```
NOT VERIFIED: <business_name>
```

For Part 5, use specific error codes instead of "NOT VERIFIED".

---

## Part 1: Check for Missing Fields

### Description

A business is VERIFIED only if **all 6 fields** contain non-empty data. Fields containing only whitespace are considered empty.

### Sample Input

```python
csv_data = """col1,col2,col3,col4,col5,col6
BIZ001,Pawsome Pets Inc.,pawsomepets.com,Pawsome,PAWSOME PETS INC,Premium pet supplies
BIZ002,Bean Bliss Coffee,beanbliss.com,,,Artisan coffee roasters
BIZ003,,,,,
BIZ004,Tech Solutions,techsol.io,Tech,TECH SOLUTIONS,Software consulting"""
```

### Sample Output

```
VERIFIED: Pawsome Pets Inc.
NOT VERIFIED: Bean Bliss Coffee
NOT VERIFIED:
VERIFIED: Tech Solutions
```

### Rules

- Strip whitespace before checking if field is empty
- All 6 columns must have non-empty values
- If business name (col2) is empty, output shows empty name

---

## Part 2: Check Description Length

### Description

The Full Description (col5) must be between **5 and 31 characters** (inclusive) after stripping whitespace.

### Sample Input

```python
csv_data = """col1,col2,col3,col4,col5,col6
BIZ001,Pawsome Pets Inc.,pawsomepets.com,Pawsome,PAWSOME PETS INC,Premium pet supplies
BIZ002,Bean Bliss Coffee,beanbliss.com,Bean,Bean,Artisan coffee roasters
BIZ003,Oakridge Furniture,oakridge.com,Oak,OAKRIDGE CUSTOM WOODWORKING AND FURNITURE EMPORIUM,Custom furniture
BIZ004,Tech Solutions,techsol.io,Tech,ITCS,Software consulting"""
```

### Sample Output

```
VERIFIED: Pawsome Pets Inc.
NOT VERIFIED: Bean Bliss Coffee
NOT VERIFIED: Oakridge Furniture
NOT VERIFIED: Tech Solutions
```

### Explanation

- BIZ001: "PAWSOME PETS INC" = 16 chars ✓
- BIZ002: "Bean" = 4 chars (too short) ✗
- BIZ003: 50 chars (too long) ✗
- BIZ004: "ITCS" = 4 chars (too short) ✗

### Rules

- Check length after Part 1 validation passes
- 5 ≤ length ≤ 31

---

## Part 3: Block Generic Names

### Description

Block businesses using generic terms in the Full Description (col5). The following terms are **blocked** (case-insensitive):

- ONLINE STORE
- ECOMMERCE
- RETAIL
- SHOP
- GENERAL MERCHANDISE

### Sample Input

```python
csv_data = """col1,col2,col3,col4,col5,col6
BIZ001,Pawsome Pets Inc.,pawsomepets.com,Pawsome,PAWSOME PETS INC,Premium pet supplies
BIZ002,Global Goods Market,globalgoods.com,Global,ONLINE STORE,Various products
BIZ003,Northwest Tech,nwtech.com,NW Tech,NORTHWEST INNOVATION TECH,Technology solutions
BIZ004,Sweet Dreams,sweetdreams.com,Sweet,SWEET DREAMS CREAMERY,Ice cream shop"""
```

### Sample Output

```
VERIFIED: Pawsome Pets Inc.
NOT VERIFIED: Global Goods Market
VERIFIED: Northwest Tech
VERIFIED: Sweet Dreams
```

### Rules

- Check col5 for blocked terms (substring match)
- Case-insensitive comparison
- Only check col5, not other columns

---

## Part 4: Match Business Names

### Description

At least **50% of words** in the Business Name (col2) must appear in either the Short Description (col4) or Full Description (col5).

**Word Processing:**
- Split by whitespace
- Remove "LLC" and "Inc" (case-insensitive)
- Case-insensitive comparison

### Sample Input

```python
csv_data = """col1,col2,col3,col4,col5,col6
BIZ001,land water,landwater.com,land,land water LLC,Environmental services
BIZ002,Acme Global Trading,acme.com,Acme,XYZ ENTERPRISES,Import export services
BIZ003,Maple Ridge Bakery,maplebakery.com,Maple,MAPLE RIDGE BAKERY LLC,Artisan baked goods
BIZ004,Innovation Labs Inc,innovlabs.com,Labs,INNOVATION RESEARCH,R&D services"""
```

### Sample Output

```
VERIFIED: land water
NOT VERIFIED: Acme Global Trading
VERIFIED: Maple Ridge Bakery
VERIFIED: Innovation Labs Inc
```

### Explanation

- BIZ001: "land", "water" → both found → 100% ✓
- BIZ002: "Acme", "Global", "Trading" → only "Acme" found → 33% ✗
- BIZ003: "Maple", "Ridge", "Bakery" → all found → 100% ✓
- BIZ004: "Innovation", "Labs" (Inc removed) → both found → 100% ✓

### Rules

- Combine words from col4 and col5 for matching
- Match percentage ≥ 50%

---

## Part 5: Specific Error Codes

### Description

Return specific error codes instead of "NOT VERIFIED". Check in this order and return the **first** error found:

| Check Order | Error Code |
|-------------|------------|
| 1. Missing fields | `ERROR_MISSING_FIELDS` |
| 2. Invalid length | `ERROR_INVALID_LENGTH` |
| 3. Generic name | `ERROR_GENERIC_NAME` |
| 4. Name mismatch | `ERROR_NAME_MISMATCH` |

### Sample Input

```python
csv_data = """col1,col2,col3,col4,col5,col6
BIZ001,Pawsome Pets Inc.,pawsomepets.com,Pawsome,PAWSOME PETS INC,Premium pet supplies
BIZ002,Bean Bliss Coffee,beanbliss.com,,,Artisan coffee roasters
BIZ003,Short Name,short.com,Short,SHRT,Products
BIZ004,Generic Store,generic.com,Store,RETAIL,Various items
BIZ005,Mismatched Corp,mismatch.com,Wrong,DIFFERENT BUSINESS,Services"""
```

### Sample Output

```
VERIFIED: Pawsome Pets Inc.
ERROR_MISSING_FIELDS: Bean Bliss Coffee
ERROR_INVALID_LENGTH: Short Name
ERROR_GENERIC_NAME: Generic Store
ERROR_NAME_MISMATCH: Mismatched Corp
```

---

## Function Signature

```python
def validate_businesses(csv_data: str) -> str:
    """
    Validate business accounts from CSV data.

    Args:
        csv_data: CSV string with header row and business data

    Returns:
        String with one line per business showing validation result
    """
    pass
```

---

## Constraints

- 1 ≤ number of business rows ≤ 10^4
- Each field length ≤ 1000 characters
- CSV is well-formed (no escaped commas within fields)
- Business names contain only alphanumeric characters, spaces, and common punctuation

---

## Notes

- Process rows in order, output in same order
- Apply validations in the order specified (Part 1 → 2 → 3 → 4)
- For Part 5, stop at first error found
- All string comparisons for blocked terms and name matching are case-insensitive
