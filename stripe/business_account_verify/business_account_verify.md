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

---

## Part 2: Check Description Length

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

---

## Part 3: Block Generic Names

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

---

## Part 4: Match Business Names

At least **50% of words** in the Business Name (col2) must appear in either the Short Description (col4) or Full Description (col5).

- Split by whitespace
- Remove "LLC" and "Inc" before comparison (case-insensitive)
- Case-insensitive word comparison

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

---

## Part 5: Specific Error Codes

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
    pass
```

---

## Constraints

- 1 ≤ number of business rows ≤ 10^4
- Each field length ≤ 1000 characters
- CSV is well-formed (no escaped commas within fields)
