# Currency Exchange System

## Problem Description

You are building a currency conversion tool that converts money between currencies using exchange rates. The rates are provided as a comma-separated string where each entry specifies that 1 unit of the FROM currency equals RATE units of the TO currency.

**Format:** `"FROM:TO:RATE,FROM:TO:RATE,..."`

**Example:** `"USD:EUR:0.85,EUR:GBP:0.88,USD:JPY:110"`

Implement a `CurrencyConverter` class that handles increasingly complex conversion scenarios across 4 phases.

---

## Class Signature

```python
class CurrencyConverter:
    def __init__(self, rate_string: str):
        """Initialize with a comma-separated rate string."""
        pass

    def getRate(self, from_curr: str, to_curr: str) -> float:
        """
        Get the exchange rate from one currency to another.
        Returns None if conversion is not possible.
        """
        pass
```

---

## Phase 1: Direct Rates

### Description

Implement basic rate lookup with forward and reverse rates.

- **Forward:** Rate is explicitly listed (USD→EUR)
- **Reverse:** Only opposite is listed (EUR→USD) — calculate as `1/rate`
- **Same currency:** Return 1.0
- **No connection:** Return None

### Sample Input

```python
rates = "USD:EUR:0.85,EUR:GBP:0.88,USD:JPY:110"
converter = CurrencyConverter(rates)
```

### Sample Output

```python
converter.getRate("USD", "EUR")  # Returns 0.85
converter.getRate("EUR", "USD")  # Returns 1.176... (1/0.85)
converter.getRate("USD", "USD")  # Returns 1.0
converter.getRate("USD", "GBP")  # Returns None (no direct link)
```

### Constraints

- O(1) lookup time after initialization
- Handle reverse rates automatically

---

## Phase 2: One-Step Connection

### Description

Allow conversion through exactly **one intermediate currency**.

If USD→EUR and EUR→GBP exist, then USD→GBP = rate(USD→EUR) × rate(EUR→GBP).

### Sample Input

```python
rates = "USD:EUR:0.85,EUR:GBP:0.88,USD:JPY:110"
converter = CurrencyConverter(rates)
```

### Sample Output

```python
converter.getRate("USD", "GBP")  # Returns 0.748 (0.85 × 0.88)
converter.getRate("JPY", "GBP")  # Returns 0.0068 (1/110 × 0.748)
converter.getRate("GBP", "JPY")  # Returns None (needs 2 intermediate steps)
```

### Rules

- Check direct rate first (Phase 1)
- If not found, try all possible single intermediate currencies
- Return the first valid rate found, or None

---

## Phase 3: Best Possible Rate

### Description

When multiple paths exist between currencies, find the path that gives the **maximum exchange rate** (best value for the user).

### Sample Input

```python
rates = "USD:EUR:0.85,USD:GBP:0.75,EUR:GBP:0.88,GBP:CAD:1.7,EUR:CAD:1.45"
converter = CurrencyConverter(rates)
```

### Sample Output

```python
converter.getRate("USD", "CAD")
# Path 1: USD→GBP→CAD = 0.75 × 1.7 = 1.275
# Path 2: USD→EUR→CAD = 0.85 × 1.45 = 1.2325
# Path 3: USD→EUR→GBP→CAD = 0.85 × 0.88 × 1.7 = 1.2716
# Returns: 1.275 (best rate)
```

### Rules

- Find ALL valid paths
- Calculate total rate for each path (multiply rates along the way)
- Return the maximum rate
- Consider both forward and reverse rates on each edge

---

## Phase 4: Any Path Length

### Description

Allow conversions through **any number of intermediate currencies** using graph traversal (BFS or DFS).

### Sample Input

```python
rates = "USD:EUR:0.85,EUR:GBP:0.88,GBP:JPY:150,JPY:AUD:0.012"
converter = CurrencyConverter(rates)
```

### Sample Output

```python
converter.getRate("USD", "AUD")
# Path: USD→EUR→GBP→JPY→AUD
# Rate: 0.85 × 0.88 × 150 × 0.012 = 1.3464
# Returns: 1.3464

converter.getRate("AUD", "USD")
# Returns: 0.7427... (1/1.3464)
```

### Rules

- Use graph traversal (BFS or DFS)
- Handle cycles (don't visit same currency twice in a path)
- Find the best rate among all possible paths
- Return None if currencies are not connected

---

## Input Format

The rate string follows this format:
- Entries separated by commas
- Each entry: `FROM:TO:RATE`
- FROM and TO are 3-letter currency codes
- RATE is a positive decimal number

```
USD:EUR:0.85,EUR:GBP:0.88,USD:JPY:110
```

---

## Constraints

- 1 ≤ number of rate entries ≤ 1000
- Currency codes are 3 uppercase letters
- Rates are positive floating-point numbers
- No duplicate entries (same FROM:TO pair won't appear twice)
- Input is well-formed

---

## Notes

- Build incrementally: Phase 1 → 2 → 3 → 4
- Phase 4 subsumes all previous phases
- For Phase 3 and 4, think of currencies as a graph where rates are edge weights
- Multiplying rates along a path gives the total conversion rate
- Reverse rate is always 1/forward_rate
