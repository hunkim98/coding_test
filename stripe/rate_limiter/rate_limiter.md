# Rate Limiter

## Problem Description

Build a rate limiter that tracks API access for multiple clients and decides if requests are allowed based on a sliding time window.

Your rate limiter must support two operations:
- `hit(key, timestamp)`: Record a request event for a specific user at a specific time
- `allowed(key, timestamp)`: Check if the user is allowed to make a request

The limit is defined as a maximum number of requests within a time window. For example, with a limit of 3 requests per 10 seconds, a user is allowed only if they made fewer than 3 requests in the last 10 seconds.

---

## Part 1: Basic Rate Limiter

Implement a basic `RateLimiter` class that counts hits for each key using a sliding window.

### Class Signature

```python
class RateLimiter:
    def __init__(self, max_requests: int, window_seconds: int):
        pass

    def hit(self, key: str, timestamp: int) -> None:
        pass

    def allowed(self, key: str, timestamp: int) -> bool:
        pass
```

### Example

```
RateLimiter(max_requests=3, window_seconds=10)

hit("user_1", 1)
hit("user_1", 2)
allowed("user_1", 3)  -> True (2 hits in window)
hit("user_1", 3)
allowed("user_1", 4)  -> False (3 hits = limit reached)
allowed("user_1", 12) -> True (hits at t=1,2 are outside window)
allowed("user_2", 5)  -> True (new key, no past hits)
```

---

## Part 2: Memory Optimization

In real systems, users may stop sending requests for extended periods. Your rate limiter needs to efficiently remove old timestamps to prevent memory from filling up with stale data.

### Requirements

- Remove timestamps older than the current window
- Memory usage should scale with active requests, not all historical requests
- Cleanup must not significantly slow down operations

---

## Part 3: Edge Cases

Handle difficult real-world scenarios:

1. **Burst Traffic**: Many requests arrive at the exact same timestamp
2. **New Keys**: First request from an unknown user
3. **Out-of-Order Timestamps**: Request arrives with timestamp older than previous requests
4. **Time Gaps**: User inactive for long period, then becomes active

### Example - Burst Traffic

```
RateLimiter(max_requests=3, window_seconds=10)

hit("user_1", 5)
hit("user_1", 5)      # Same timestamp
allowed("user_1", 5)  -> True (2 hits)
hit("user_1", 5)      # Third hit at same time
allowed("user_1", 5)  -> False (3 hits = limit)
```

### Example - Out-of-Order Timestamps

```
hit("user_2", 10)
hit("user_2", 8)       # Older timestamp arrives late
allowed("user_2", 10)  -> Should count both hits
```

### Example - Time Gap

```
hit("user_3", 1)
hit("user_3", 2)
allowed("user_3", 1000)  -> True (old hits outside window)
```

---

## Part 4: Thread Safety

In production, multiple threads may call `hit()` and `allowed()` simultaneously. Your code must handle concurrent access without data corruption.

### Race Condition Example

```
# Without protection:
# Start: count = 2 (Limit is 3)
# Thread A: allowed() -> sees count 2 -> returns True
# Thread B: allowed() -> sees count 2 -> returns True
# Thread A: hit() -> count becomes 3
# Thread B: hit() -> count becomes 4 (OVER LIMIT!)
# Both were allowed, but only one should have been.
```

### Requirements

1. Concurrent calls for the same key must work correctly
2. Prevent data corruption
3. Consider implementing an atomic `check_and_hit` operation:

```python
def check_and_hit(self, key: str, timestamp: int) -> bool:
    """
    Atomically check limit and record hit.
    Returns True if allowed (and hit recorded), False otherwise.
    """
    pass
```

---

## Constraints

- Timestamps are positive integers (seconds)
- Keys are non-empty strings
- `hit()` records requests even if over the limit
- `allowed()` checks past hits, not including the current request
- 1 ≤ max_requests ≤ 10^6
- 1 ≤ window_seconds ≤ 10^6
