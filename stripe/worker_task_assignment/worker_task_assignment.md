# Worker Task Assignment

## Problem Description

Build a system to assign support tasks to workers. The assignment rules become more complex as features are added.

---

## Data Format

### Workers

```python
# Step 1: Simple list of names
workers = ["alice", "bob", "charlie"]

# Steps 2-4: Objects with details
workers = [
    {"name": "alice", "specialty": "billing"},
    {"name": "bob", "specialty": "technical"}
]
```

### Tasks

```python
tasks = [
    {"id": "task1", "duration": 5},                                    # Step 1
    {"id": "task2", "duration": 3, "requiredSpecialties": ["billing"]}, # Step 2
    {"id": "task3", "duration": 7, "requiredSpecialties": ["billing"], "accountId": "acme"}  # Steps 3-4
]
```

### Output Format

```python
[
    {"taskId": "task1", "worker": "alice"},
    {"taskId": "task2", "worker": "bob"}
]
```

---

## Step 1: Balancing Workload

### Task

Assign each task to the worker with the lowest total workload.

### Rules

1. Process tasks in order
2. Assign to worker with minimum total work time
3. **Tie-breaker**: Worker appearing earlier in list wins
4. Add task duration to worker's workload after assignment

### Example

**Input:**
```python
workers = ["alice", "bob", "charlie"]
tasks = [
    {"id": "task1", "duration": 5},
    {"id": "task2", "duration": 3},
    {"id": "task3", "duration": 7},
    {"id": "task4", "duration": 2},
    {"id": "task5", "duration": 4}
]
```

**Output:**
```python
[
    {"taskId": "task1", "worker": "alice"},    # all at 0, alice first
    {"taskId": "task2", "worker": "bob"},      # bob,charlie at 0
    {"taskId": "task3", "worker": "charlie"},  # charlie at 0 (lowest)
    {"taskId": "task4", "worker": "bob"},      # bob at 3 (lowest)
    {"taskId": "task5", "worker": "alice"}     # alice,bob tied at 5, alice first
]
```

**Workload progression:**
- Start: alice=0, bob=0, charlie=0
- After task1: alice=5, bob=0, charlie=0
- After task2: alice=5, bob=3, charlie=0
- After task3: alice=5, bob=3, charlie=7
- After task4: alice=5, bob=5, charlie=7
- After task5: alice=9, bob=5, charlie=7

---

## Step 2: Matching Skills

### Task

Only assign tasks to workers who have the required specialty.

### Rules

1. Filter workers by required specialty
2. Among eligible workers, pick one with lowest workload
3. If no worker matches, skip the task
4. Same tie-breaker: earlier in list wins

### Example

**Input:**
```python
workers = [
    {"name": "alice", "specialty": "billing"},
    {"name": "bob", "specialty": "technical"},
    {"name": "charlie", "specialty": "billing"},
    {"name": "diana", "specialty": "technical"}
]

tasks = [
    {"id": "task1", "duration": 5, "requiredSpecialties": ["billing"]},
    {"id": "task2", "duration": 3, "requiredSpecialties": ["technical"]},
    {"id": "task3", "duration": 7, "requiredSpecialties": ["billing", "technical"]},
    {"id": "task4", "duration": 2, "requiredSpecialties": ["billing"]},
    {"id": "task5", "duration": 4, "requiredSpecialties": ["technical"]}
]
```

**Output:**
```python
[
    {"taskId": "task1", "worker": "alice"},    # billing: alice(0), charlie(0) -> alice
    {"taskId": "task2", "worker": "bob"},      # technical: bob(0), diana(0) -> bob
    {"taskId": "task3", "worker": "charlie"},  # both groups: charlie(0), diana(0) -> charlie
    {"taskId": "task4", "worker": "alice"},    # billing: alice(5), charlie(7) -> alice
    {"taskId": "task5", "worker": "diana"}     # technical: bob(3), diana(0) -> diana
]
```

---

## Step 3: Client History (Affinity)

### Task

Prioritize workers who have previously helped the same client (account).

### Priority Order

1. Filter by required specialty
2. Among eligible, prefer workers with **affinity** (helped this accountId before)
3. If multiple have affinity, pick lowest workload
4. If none have affinity, pick lowest workload from all eligible
5. Same tie-breaker: earlier in list wins

### Example

**Input:**
```python
workers = [
    {"name": "alice", "specialty": "billing"},
    {"name": "bob", "specialty": "billing"},
    {"name": "charlie", "specialty": "billing"}
]

tasks = [
    {"id": "task1", "duration": 5, "requiredSpecialties": ["billing"], "accountId": "acme"},
    {"id": "task2", "duration": 3, "requiredSpecialties": ["billing"], "accountId": "globex"},
    {"id": "task3", "duration": 7, "requiredSpecialties": ["billing"], "accountId": "acme"},
    {"id": "task4", "duration": 2, "requiredSpecialties": ["billing"], "accountId": "acme"},
    {"id": "task5", "duration": 4, "requiredSpecialties": ["billing"], "accountId": "globex"}
]
```

**Output:**
```python
[
    {"taskId": "task1", "worker": "alice"},    # No history. alice first at 0.
    {"taskId": "task2", "worker": "bob"},      # No globex history. bob at 0.
    {"taskId": "task3", "worker": "alice"},    # alice has acme history -> priority
    {"taskId": "task4", "worker": "alice"},    # alice still has acme affinity
    {"taskId": "task5", "worker": "bob"}       # bob has globex history
]
```

---

## Step 4: Handling Offline Workers

### Task

Handle workers going offline during task processing.

### Additional Input

```python
offlineEvents = [
    {"worker": "alice", "afterTaskIndex": 2}  # alice offline after task index 2
]
```

### Rules

1. Workers go offline **after** the specified task index is assigned
2. Offline workers cannot receive new tasks
3. History is preserved (but won't matter since they're offline)
4. Continue with remaining available workers

### Example

**Input:**
```python
workers = [
    {"name": "alice", "specialty": "billing"},
    {"name": "bob", "specialty": "billing"},
    {"name": "charlie", "specialty": "billing"}
]

tasks = [
    {"id": "task1", "duration": 5, "requiredSpecialties": ["billing"], "accountId": "acme"},
    {"id": "task2", "duration": 3, "requiredSpecialties": ["billing"], "accountId": "globex"},
    {"id": "task3", "duration": 7, "requiredSpecialties": ["billing"], "accountId": "acme"},
    {"id": "task4", "duration": 2, "requiredSpecialties": ["billing"], "accountId": "acme"},
    {"id": "task5", "duration": 4, "requiredSpecialties": ["billing"], "accountId": "globex"}
]

offlineEvents = [
    {"worker": "alice", "afterTaskIndex": 2}
]
```

**Output:**
```python
[
    {"taskId": "task1", "worker": "alice"},    # index 0
    {"taskId": "task2", "worker": "bob"},      # index 1
    {"taskId": "task3", "worker": "alice"},    # index 2 - alice goes offline after this
    {"taskId": "task4", "worker": "charlie"},  # alice offline, charlie takes acme
    {"taskId": "task5", "worker": "bob"}       # bob has globex history
]
```

---

## Constraints

- Worker names are unique strings
- Task IDs are unique strings
- Durations are non-negative integers
- Specialties are non-empty strings
- Account IDs are non-empty strings
- Task indices in offlineEvents are 0-based

---

## Test Format

```python
# Step 1
def assign_tasks(workers: List[str], tasks: List[dict]) -> List[dict]:
    pass

# Steps 2-3
def assign_tasks(workers: List[dict], tasks: List[dict]) -> List[dict]:
    pass

# Step 4
def assign_tasks(workers: List[dict], tasks: List[dict], offlineEvents: List[dict]) -> List[dict]:
    pass
```
