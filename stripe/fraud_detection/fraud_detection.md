# Catch Me If You Can

## Background

Stripe processes billions of dollars worth of transactions every day. As guardians of the
Internet ecosystem, it is our duty to ensure that legitimate merchants can safely transact with
their customers, and that we quickly detect and block illegitimate or fraudulent activity.

To detect fraud, we employ various ML models at scale such as Radar to detect fraudulent
transactions as they come in. These models examine a variety of different variables about
incoming transactions to determine their authenticity. One input we can look at is the
outcome from the credit card networks like Visa and Mastercard. These networks communicate
with banks and provide different response codes to reflect the outcomes of credit card
transactions.

While they act as a safety net, if we have enough data to determine a merchant is fraudulent,
we should proactively block them to protect consumers from malicious activities like usage
of stolen cards.

Today, you will build a very simple fraud detection model to determine if a merchant is
fraudulent or not.

NOTE: Though the question is split into parts to guide your implementation, there are test
cases for all three parts, so your solution should work for all three parts.

---

## Inputs

There are 6 inputs.

Input 1:
A comma-separated list of codes that are NOT fraudulent.

Input 2:
A comma-separated list of codes that ARE fraudulent.

Input 3:
A table of MCCs and their corresponding fraud thresholds.
Each row is separated by a newline.
Each column is separated by a comma.

Input 4:
A table of merchants by account_id and their corresponding MCC.

Input 5:
The minimum number of transactions required before evaluating a merchant.

Input 6:
A table of events. Each row is one of:

CHARGE,charge_id,account_id,amount,code
DISPUTE,charge_id

---

## Output

Return a lexicographically sorted, comma-separated list of fraudulent merchants
(by account_id).

---

## Part 1: Count Threshold (Integers)

Each merchant has a Merchant Category Code (MCC).
Each MCC has a fraud threshold (integer > 1).

A merchant is marked as fraudulent if:
- total_charges_seen >= min_charges
- fraudulent_charge_count >= threshold_for_their_MCC

Once fraudulent, the merchant remains fraudulent.

---

## Part 2: Ratio Threshold (Fractions)

The threshold is now a fraction between 0 and 1 (inclusive).

A merchant is marked as fraudulent if:
- total_charges_seen >= min_charges
- fraudulent_charge_count / total_charges_seen >= threshold_for_their_MCC

Once fraudulent, the merchant remains fraudulent even if the ratio later drops.

---

## Part 3: Disputes

Merchants can dispute fraudulent charges.

DISPUTE,charge_id

Rules:
- A disputed charge is treated as NON-fraudulent.
- A dispute may restore a merchant from fraudulent to non-fraudulent.
- This is the ONLY way to restore status.
- A charge is disputed at most once.
- DISPUTE always appears after the corresponding CHARGE.

---

## Example 1 (Part 1)

INPUT

approved,invalid_pin,expired_card
do_not_honor,stolen_card,lost_card

retail,5
airline,2
restaurant,10
venue,3

acct_1,airline
acct_2,venue
acct_3,retail

0

CHARGE,ch_1,acct_1,100,do_not_honor
CHARGE,ch_2,acct_1,200,approved
CHARGE,ch_3,acct_1,300,do_not_honor
CHARGE,ch_4,acct_2,100,lost_card
CHARGE,ch_5,acct_2,200,lost_card
CHARGE,ch_6,acct_2,300,lost_card
CHARGE,ch_7,acct_3,100,lost_card
CHARGE,ch_8,acct_2,200,stolen_card
CHARGE,ch_9,acct_3,100,approved

OUTPUT

acct_1,acct_2

---

## Example 2 (Part 2)

INPUT

approved,invalid_pin,expired_card
do_not_honor,stolen_card,lost_card

retail,0.5
airline,0.25
restaurant,0.8
venue,0.25

acct_1,airline
acct_2,venue
acct_3,venue

3

CHARGE,ch_1,acct_1,100,do_not_honor
CHARGE,ch_2,acct_1,200,approved
CHARGE,ch_3,acct_1,300,do_not_honor
CHARGE,ch_4,acct_2,400,approved
CHARGE,ch_5,acct_2,500,approved
CHARGE,ch_6,acct_1,600,lost_card
CHARGE,ch_7,acct_2,700,approved
CHARGE,ch_8,acct_2,800,approved
CHARGE,ch_9,acct_3,800,approved
CHARGE,ch_10,acct_3,700,approved
CHARGE,ch_11,acct_3,600,approved
CHARGE,ch_12,acct_3,500,stolen_card
CHARGE,ch_13,acct_3,500,stolen_card
CHARGE,ch_14,acct_2,400,stolen_card

OUTPUT

acct_1,acct_3

---

## Example 3 (Part 3)

INPUT

approved,invalid_pin,expired_card
do_not_honor,stolen_card,lost_card

retail,0.8
venue,0.25

acct_1,retail
acct_2,retail

2

CHARGE,ch_1,acct_1,100,do_not_honor
CHARGE,ch_2,acct_1,200,lost_card
CHARGE,ch_3,acct_1,300,do_not_honor
DISPUTE,ch_2
CHARGE,ch_4,acct_2,400,lost_card
CHARGE,ch_5,acct_2,500,lost_card
CHARGE,ch_6,acct_1,600,lost_card
CHARGE,ch_7,acct_2,700,lost_card
CHARGE,ch_8,acct_2,800,do_not_honor

OUTPUT

acct_2

---

## Function Signature (Python)

from typing import List

def find_fraudulent_merchants(
    non_fraud_codes: str,
    fraud_codes: str,
    mcc_thresholds: List[str],
    merchant_mcc_map: List[str],
    min_charges: str,
    charges: List[str],
) -> str:
    pass