# For All Intents and Purposes

## Background

Stripe processes billions of dollars of payments to businesses every day through dozens of different payment methods like cards, bank debits, and even paper cheques.

We don't want merchants (the businesses who use Stripe to accept payments) to have to worry about the details for each specific payment method. For example, for many payment methods, payments are not completed instantly and can take a few days to process and be confirmed or fail, while others are processed much more quickly.

Stripe abstracts this payment flow with a simple state machine object called a **Payment Intent**.

NOTE: It is highly recommended to read all of the parts before coding. Parts may build on top of each other.

---

## What is a Payment Intent?

A Payment Intent tracks a payment through its flow from initialization to processing to confirmation. We model this flow as a state machine: an abstract object that can exist in one of a number of states and transition between states.

A Payment Intent stores information like the merchant receiving the payment and the monetary amount. It also should keep track of its state, which can be one of three values:

| State | Description |
|-------|-------------|
| `REQUIRES_ACTION` | The initial state of a Payment Intent upon creation. Can transition to `PROCESSING`. |
| `PROCESSING` | The customer has attempted to pay but the attempt has not yet succeeded or failed. Can transition to either `REQUIRES_ACTION` or `COMPLETED`. |
| `COMPLETED` | The attempt to pay succeeded and the Payment Intent amount was added to the merchant's balance. |

---

## Your Task

You will implement a function that executes a chronologically ordered list of commands to create and manage Payment Intents for different merchants and then returns the account balances for each merchant after executing all commands.

### Input
A chronologically ordered list of commands in the form `['INIT m1 0', 'CREATE p1 m1 100']` where each command is a single string. You will also receive the part number.

### Output
A list of merchant balances in the form `['m1 100', 'm2 200']` representing the balance for each merchant after executing all commands. The list should be sorted by merchant ID in ascending alphabetical order.

---

## Part 1: Good intentions

To build the initial version of our system, we will support a few basic commands for initializing a merchant, creating a Payment Intent, attempting a Payment Intent, and succeeding a Payment Intent.

### Commands

**INIT \<merchant_id\> \<starting_balance\>**
- Initializes a merchant with a unique identifier string and starting balance (the amount of money in their account).
- If a merchant with the given identifier has already been created, this command should do nothing.

**CREATE \<payment_intent_id\> \<merchant_id\> \<amount\>**
- Creates a Payment Intent for a merchant with a given amount.
- After creation, the state of the Payment Intent should be `REQUIRES_ACTION`.
- If a Payment Intent with the given identifier already exists, or if a merchant with the given identifier does not exist, or if the amount is negative, this command should do nothing.

**ATTEMPT \<payment_intent_id\>**
- Transitions a Payment Intent with a given identifier from the `REQUIRES_ACTION` state to the `PROCESSING` state.
- If no Payment Intent with the given identifier exists, or if the state of the Payment Intent is not `REQUIRES_ACTION`, this command should do nothing.

**SUCCEED \<payment_intent_id\>**
- Transitions a Payment Intent with a given identifier from the `PROCESSING` state to the `COMPLETED` state.
- If no Payment Intent with the given identifier exists, or if the state of the Payment Intent is not `PROCESSING`, this command should do nothing.

### Example 1

**Input:**
```
INIT m1 0
INIT m2 10
CREATE p1 m1 50
ATTEMPT p1
SUCCEED p1
CREATE p2 m2 100
ATTEMPT p2
```

**Output:**
```
m1 50
m2 10
```

---

## Part 2: Change is good

Merchants also need to be able to update the amount of initialized Payment Intents. This might happen if a customer begins to check out but then decides to change the items in their shopping cart.

### Commands

**UPDATE \<payment_intent_id\> \<new_amount\>**
- Updates the monetary amount of an existing Payment Intent in the `REQUIRES_ACTION` state. This does not transition the state of the Payment Intent.
- If no Payment Intent with the given identifier exists, or if the Payment Intent is not in the `REQUIRES_ACTION` state, or if the new amount is negative, this command should do nothing.

### Example 2

**Input:**
```
INIT m1 0
CREATE p1 m1 50
UPDATE p1 100
ATTEMPT p1
SUCCEED p1
```

**Output:**
```
m1 100
```

---

## Part 3: Accepting failure

Payments don't always succeed and can fail for a variety of reasons like a card network declining a transaction or a bank account not having sufficient funds. Also, even after payments have succeeded, customers need to be able to request refunds from merchants.

### Commands

**FAIL \<payment_intent_id\>**
- Fails a payment intent in the `PROCESSING` state, transitioning it from `PROCESSING` to `REQUIRES_ACTION`. This occurs when the customer's payment was declined.
- If no Payment Intent with the given identifier exists, or if the Payment Intent is not in the `PROCESSING` state, this command should do nothing.

**REFUND \<payment_intent_id\>**
- Processes a refund for a previously successful payment intent in the `COMPLETED` state. This should decrement the merchant's balance by the amount of the Payment Intent in order to return the funds to the customer.
- If no Payment Intent with the given identifier exists, or if the Payment Intent is not in the `COMPLETED` state, or if the Payment Intent has already been refunded, this command should do nothing.

### Example 3

**Input:**
```
INIT m1 0
CREATE p1 m1 50
ATTEMPT p1
FAIL p1
ATTEMPT p1
SUCCEED p1
CREATE p2 m1 100
ATTEMPT p2
SUCCEED p2
REFUND p2
```

**Output:**
```
m1 50
```

---

## Part 4: Timing matters

Merchants have requested that we augment our refund functionality by letting merchants specify a refund timeout policy: the amount of time after a payment succeeds that refunds are permitted.

### Timestamps

- All commands will now have an integer timestamp in front. For example, instead of `SUCCEED <pi_id>` you will now receive `<timestamp> SUCCEED <pi_id>`.
- Timestamps are strictly increasing integers.

### Merchant refund timeout limit

The `INIT` command now has an optional third argument:

**\<timestamp\> INIT \<merchant_id\> \<starting_balance\> \<refund_timeout_limit\>**

- If a merchant has a `refund_timeout_limit` of `n`, and succeeds a Payment Intent at timestamp `t`, then the timestamp of a `REFUND` command must be no greater than `t + n`, otherwise the refund should not succeed.
- If `refund_timeout_limit` is not specified, there is no refund time limit.
- A `refund_timeout_limit` of `0` means no refunds should be accepted ever.
- A negative `refund_timeout_limit` should be ignored (meaning all refunds should be accepted).

### Example 4

**Input:**
```
1 INIT m1 0 5
2 CREATE p1 m1 100
3 CREATE p2 m1 50
4 ATTEMPT p1
5 ATTEMPT p2
8 SUCCEED p1
10 SUCCEED p2
11 REFUND p1
16 REFUND p2
```

**Output:**
```
m1 50
```

**Explanation:**
- p1 succeeded at time 8, refunded at time 11 (11 - 8 = 3 <= 5) -> refund succeeds
- p2 succeeded at time 10, refunded at time 16 (16 - 10 = 6 > 5) -> refund fails
- Final balance: 0 + 100 - 100 + 50 = 50

---

## Function Signature

```python
from typing import List

def execute(commands: List[str], part: int) -> List[str]:
    pass
```
