# Coin Combinations Problem

## Problem Statement

You have exactly **\(n\)** coins in total, and each coin can be one of three possible denominations: **10**, **30**, or **50**. You want these **\(n\)** coins to add up to a total value of **\(m\)**.

**Task**: Determine in how many distinct ways you can choose the number of 10-value, 30-value, and 50-value coins so that:

1. The total number of coins is **\(n\)**.
2. The sum of their values is **\(m\)**.

## Input Format

- A single line containing two space-separated integers, **\(n\)** and **\(m\)**.

## Output Format

- Print a single integer: the number of valid combinations of the coins.

## Example

**Input**

3, 90

**Explanation**

We have **3** coins to form a total of **90**. Each coin can be **10**, **30**, or **50**.

Some valid combinations:
- **10 + 30 + 50 = 90**
- **30 + 30 + 30 = 90**

(Your task is to count all such valid combinations.)

**Output**

2