# Shortest Travel Time in a Directed Graph

## Problem Statement

You are given a collection of directed routes between nodes in a network. Each route has an associated travel time (cost). Given a **start node** and an **end node**, determine the **shortest travel time** from the start to the end. If there is no valid route from the start to the end, the result should be **0**.

## Details

- Each route is represented as a triple \([ \text{sourceNode}, \text{destinationNode}, \text{travelTime} ]\).
- The graph may have any number of nodes and routes.
- Travel times are non-negative integers.
- Return the minimum possible travel time between the **startNode** and the **endNode**, or **0** if no path exists.

## Input Format

- **startNode**: A string representing the starting node.
- **endNode**: A string representing the destination node.
- **paths**: A list (or array) of routes. Each route is given as a list of three strings:  
  \[
    \text{paths}[i] = [ \text{sourceNode}, \text{destinationNode}, \text{travelTime} ]
  \]

## Output Format

- A single integer (or long), which is the shortest travel time from **startNode** to **endNode**.
- If no path exists, output **0**.

## Example

Suppose you have the following input:

- **startNode** = `"A"`
- **endNode** = `"D"`
- **paths** =  
  \[
    ["A", "B", "2"],  
    ["B", "C", "3"],  
    ["A", "C", "5"],  
    ["C", "D", "4"]  
  \]

Here is one possible shortest path:

1. \( A \to B \) takes **2** units of time.
2. \( B \to C \) takes **3** units of time.
3. \( C \to D \) takes **4** units of time.

The total travel time would be **2 + 3 + 4 = 9**.

However, if you take \( A \to C \) (5 units) and then \( C \to D \) (4 units), you get **9** units as well. In this case, both routes yield the same shortest time: **9**.

If there were no route from **A** to **D**, your program should return **0**.

---

### What the Code Does

The provided function `get_shortest_time`:
1. Builds an adjacency list (`ma`) from the given paths (where each path is `source -> (destination, travelTime)`).
2. Initializes a distance map `d` with `LONG_MAX` (representing "infinity") for all nodes and sets the start node’s distance to 0.
3. Uses a **Dijkstra-like** approach with a `multiset` (acting as a priority queue) to determine the minimum cost to reach every other node.
4. Returns the distance to `endNode`, or **0** if `endNode` remains at `LONG_MAX` (meaning it is unreachable).

Use this function (or write your own) to compute the minimum travel time from **startNode** to **endNode** under the given constraints.
