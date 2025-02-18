# Cup Exchange (Counting Swaps with Selection Sort)

## Problem Statement

You are given an array of labels (numbers) that represent cups placed in a row. Your task is to **sort these cups in ascending order**. However, instead of simply returning the sorted array, you need to **report how many swaps** occur in the process of sorting when using a **selection sort** algorithm.

## Details

1. **Input**:  
   - An integer \( n \) denoting the number of cups (size of the array).  
   - \( n \) subsequent lines, each containing a label (an integer).

2. **Output**:  
   - A single integer (or long integer), which is the **number of swaps** executed in the selection sort process.

### Selection Sort Overview

In selection sort, for each position \( i \) in the array:
1. Find the **index of the minimum value** from the subarray starting at \( i \) to the end.
2. If that minimum is not already at position \( i \), **swap** the values at indices \( i \) and the minimum index.
3. Move on to \( i+1 \) until the array is fully sorted.

Every time a swap occurs, increment a **counter**. The final value of that counter is your answer.

## Example

**Input**  

4 4 3 1 2


Here, \( n = 4 \) and the labels are \([4, 3, 1, 2]\).

- **Step-by-step**:
  1. **i = 0**: subarray is `[4, 3, 1, 2]`; min is `1` (index 2). Swap index 0 with index 2 → `[1, 3, 4, 2]`, swaps = 1
  2. **i = 1**: subarray is `[3, 4, 2]`; min is `2` (index 3 overall). Swap index 1 with index 3 → `[1, 2, 4, 3]`, swaps = 2
  3. **i = 2**: subarray is `[4, 3]`; min is `3` (index 3 overall). Swap index 2 with index 3 → `[1, 2, 3, 4]`, swaps = 3
  4. **i = 3**: nothing to do (already the last element).

**Output**  

3


So, the selection sort procedure on this array results in **3 swaps** in total.
