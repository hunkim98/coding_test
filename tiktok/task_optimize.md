# Processing Tasks Within Date Ranges

## Problem Statement

You are given several tasks, each with:
1. A **start day** (\(start\))
2. An **end day** (\(end\))
3. A **required number of processing units** (\(k\))  

For a task \(i\), it can **only** be processed on days from \(start\) to \(end\) (inclusive). Each time you pick a **single day** to process, **all tasks active on that day** (i.e., tasks for which the chosen day is between their start and end) each receive **1 unit of processing**—assuming they still need processing.

Your goal is to determine the **minimum number of days** you must select so that **all tasks** receive their required number of processing units. If a task still needs processing, it can be processed on any of its active days that you choose.

## Input Format

1. An integer \( \text{tasksRows} \): the number of tasks.  
2. An integer \( \text{tasksColumns} \): the number of columns in each task’s description (should be 3 in this setup: `start`, `end`, `requiredUnits`).  
3. A **2D integer array** \( \text{tasks} \) of size \(\text{tasksRows} \times \text{tasksColumns}\), where each row represents:
   \[
   \bigl[\, start, \ end, \ requiredUnits \bigr]
   \]
   - **`start`** and **`end`** are the (inclusive) day range within which the task can be processed.
   - **`requiredUnits`** indicates how many times total this task needs processing.

## Output Format

- Print **one integer**: the minimum number of day selections necessary to ensure every task is fully processed.

## Example

Suppose you have 3 tasks as follows:

1. \([1, 3, 2]\) — A task can be processed on days **1**, **2**, or **3**, and it needs **2** processing units.  
2. \([2, 2, 1]\) — A task can only be processed on day **2**, needing **1** processing unit.  
3. \([1, 2, 2]\) — A task can be processed on days **1** or **2**, needing **2** units.  

One possible strategy:
- Pick **day 2**: The 1st task (days 1–3) gets 1 unit, 2nd task (day 2) gets 1 unit (completing it), and 3rd task (days 1–2) gets 1 unit.  
  - Remaining needs: Task 1 → 1 unit, Task 2 → 0 units, Task 3 → 1 unit.  
- Pick **day 1**: The 1st task gets its final needed unit, and the 3rd task gets its final needed unit.  

Total days picked: **2**. In this example, we cannot do it in fewer than 2 selections because tasks 1 and 3 each need 2 units of processing.  

Hence, the output for this example is:

2