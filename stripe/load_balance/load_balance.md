# Stripe OA — Jupyter Server Connection Management (5-Part Question)

Reference: https://programhelp.net/en/oa/stripe-26-new-grad-oa/

This problem simulates a **stateful connection router / load balancer**.  
You are not asked to design a large distributed system, but to implement a **precise state machine** that processes requests and produces a **connection assignment log**.

A single connection (`connId`) may appear **multiple times** in the output due to reassignment (e.g., after shutdown).

---

## Global Definitions

- **numTargets**: number of backend targets (servers), indexed from `1` to `numTargets`
- **maxConnectionsPerTarget**: maximum number of concurrent connections allowed per target
- **requests**: list of request strings

### Request Types

- `CONNECT connId`
- `DISCONNECT connId`
- `SHUTDOWN targetId`

---

## Output

Return a **list of connection logs**.

Each log entry represents a **successful assignment event** and is formatted as: (connId, targetId)

### Logging Rules

- Log **every successful assignment**, including:
  - initial CONNECT
  - duplicate CONNECT (returns original assignment)
  - reassignment due to SHUTDOWN
- Do **not** log:
  - DISCONNECT
  - rejected CONNECT (no available capacity / no online target)

---

## Routing Policy (Used in All Parts)

- Maintain a pointer `nextTarget`, initially set to `1`
- When assigning a connection:
  1. Starting from `nextTarget`, scan targets in circular order
  2. Select the first target that is:
     - online (not shutdown)
     - not full (`activeConnections < maxConnectionsPerTarget`)
  3. Assign the connection to that target
  4. Update `nextTarget = selectedTarget + 1` (wrap around if needed)

If no target satisfies these conditions, the assignment fails.

---

## Part 1 — Basic CONNECT Logic

**Difficulty:** ★☆☆☆☆

### Requirements

- Process `CONNECT connId` requests
- Assign each new connection using the routing policy
- Append `(connId, targetId)` to the log for each successful assignment

### Notes

- No duplicate CONNECTs
- No DISCONNECT
- No capacity limit
- All targets are always online

---

## Part 2 — Duplicate CONNECT Handling

**Difficulty:** ★☆☆☆☆

### Requirements

- If a `CONNECT` request arrives with a `connId` that already exists:
  - Do **not** reassign the connection
  - Do **not** modify any internal state
  - Append the **original assignment** `(connId, targetId)` to the log again

### Key Data Structure

connId → targetId

---

## Part 3 — DISCONNECT Support

**Difficulty:** ★☆☆☆☆

### Requirements

- Support `DISCONNECT connId`
- If `connId` exists:
  - Remove it from its assigned target
  - Free one capacity slot
- If `connId` does not exist, ignore the request
- `DISCONNECT` does **not** produce a log entry

---

## Part 4 — Target Capacity Limit

**Difficulty:** ★★☆☆☆

### Requirements

- Each target has a capacity limit
- When assigning a connection:
  - Skip targets that are full
  - Skip targets that are offline
  - Continue scanning circularly
- If all targets are full or offline:
  - Ignore the CONNECT request
  - Do **not** append to the log

---

## Part 5 — SHUTDOWN and Reassignment

**Difficulty:** ★★★☆☆

### SHUTDOWN targetId

- Mark the target as **offline**
- The target cannot receive future assignments
- All existing connections on this target must be **evicted**

### Eviction and Reassignment Rules

- Evict connections in the **order they were originally assigned** to the target
- For each evicted connection:
  1. Attempt to reassign it using the routing policy
  2. If reassignment succeeds:
     - Append `(connId, newTargetId)` to the log
  3. If no target is available:
     - Drop the connection silently

### Notes

- The SHUTDOWN operation itself does **not** generate a log entry
- Only successful reassignment events are logged
- A connection may appear **multiple times** in the log

---

## Example

### Input

numTargets = 2
maxConnectionsPerTarget = 2

requests = [
“CONNECT c1”,
“CONNECT c2”,
“SHUTDOWN 1”
]

### Output

(c1, 1)
(c2, 2)
(c1, 2)

### Explanation

1. `c1` is assigned to target 1
2. `c2` is assigned to target 2
3. Target 1 shuts down, evicting `c1`, which is reassigned to target 2

---

## Summary

| Part | Feature |
|------|---------|
| 1 | Basic CONNECT routing |
| 2 | Duplicate CONNECT handling |
| 3 | DISCONNECT support |
| 4 | Capacity limits |
| 5 | SHUTDOWN with eviction and reassignment |

---

## Key Insight

This problem is best approached as a **stateful simulation**:
- Maintain explicit state
- Reuse the same routing logic everywhere
- Log **assignment events**, not final state

This is closer to a **backend state machine + resource management** problem than a traditional system design question.