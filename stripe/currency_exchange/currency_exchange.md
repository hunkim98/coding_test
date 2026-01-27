Currency Exchange System

Problem Summary

You need to build a tool that converts money from one currency to another. The system uses specific exchange rates to do the math.

The rates come as a text string separated by commas. Each entry tells you that 1 unit of the "FROM" currency is equal to a specific amount of the "TO" currency.

Format: "FROM:TO:RATE,FROM:TO:RATE..."

Example: "USD:EUR:0.85,EUR:GBP:0.88,USD:JPY:110"

The interview problem has four parts, starting easy and getting harder:

1. Direct Rates: Check if there is a direct rate between two currencies (A to B).
2. One-Step Connection: Convert money using exactly one middle currency (A to B to C).
3. Best Possible Rate: If there are many ways to convert, find the one that gives the most money.
4. Any Path Length: Connect currencies through a chain of any size (A to... to Z).

Phase 1: Direct Rates

Problem Requirements

Write a CurrencyConverter class. It parses the rate string. Then, create a function called `getRate(from, to)`.

This function must handle:

- Forward check: The rate is explicitly listed (e.g., A to B).
- Reverse check: Only the opposite rate is listed (e.g., B to A). You must calculate 1 / rate.
- If there is no direct connection, return None or -1.

Example

Input:

```python
rates = "USD:EUR:0.85,EUR:GBP:0.88,USD:JPY:110"
converter = CurrencyConverter(rates)

converter.getRate("USD", "EUR")  # Returns 0.85 (It is in the string)
converter.getRate("EUR", "USD")  # Returns 1.176... (Math: 1 / 0.85)
converter.getRate("USD", "GBP")  # Returns None (No direct link)
```

Key Goals

- Read the input string quickly.
- Store the data so you can find it in O(1) time.
- Handle reverse math using the reciprocal.
- Return a specific value for failure (like None).

Questions You Might Ask

- How precise should the decimal numbers be?
- Are there duplicate rates in the string?
- Is the input format always correct?
- What happens if I convert USD to USD?

Phase 2: One-Step Connection

Problem Requirements

Update your solution to handle a "middleman" currency.

For example, if you have USD→EUR and EUR→GBP, you can calculate USD→GBP. The math is: Rate(USD→EUR) * Rate(EUR→GBP).

Example

Input:

```python
rates = "USD:EUR:0.85,EUR:GBP:0.88,USD:JPY:110"
converter = CurrencyConverter(rates)

converter.getRate("USD", "GBP")
# Returns 0.748 (Math: 0.85 * 0.88)

converter.getRate("GBP", "JPY")
# Returns None (This needs 2 middle steps, which is not allowed yet)
```

Key Goals

- Check for a direct rate first (Phase 1).
- If that fails, look for a single currency that connects the start and end.
- Multiply the two rates together.
- Return None if no single-step path exists.

Phase 3: Best Possible Rate

Problem Requirements

Sometimes, there are multiple paths between two currencies. You must find the path that gives the maximum exchange rate.

This ensures the user gets the best deal.

Example

Input:

```python
rates = "USD:EUR:0.85,USD:GBP:0.75,EUR:GBP:0.88,GBP:CAD:1.7,EUR:CAD:1.45"
converter = CurrencyConverter(rates)

converter.getRate("USD", "CAD")
# Path 1: USD→GBP→CAD = 0.75 * 1.7 = 1.275
# Path 2: USD→EUR→CAD = 0.85 * 1.45 = 1.2325
# Path 3: USD→EUR→GBP→CAD = 0.85 * 0.88 * 1.7 = 1.2716
# Result: 1.275 is the winner.
```

Key Goals

- Find every valid path between the currencies.
- Calculate the total rate for each path.
- Compare them and return the highest number.
- Remember to use both forward and reverse rates.

Phase 4: Any Path Length

Problem Requirements

Now, allow conversions through any number of middle currencies. You will need to use graph traversal algorithms like BFS (Breadth-First Search) or DFS (Depth-First Search).

Example

Input:

```python
rates = "USD:EUR:0.85,EUR:GBP:0.88,GBP:JPY:150,JPY:AUD:0.012"
converter = CurrencyConverter(rates)

converter.getRate("USD", "AUD")
# Math: 0.85 * 0.88 * 150 * 0.012 = 1.3464

converter.getRate("AUD", "USD")
# Reverse path returns 1 / 1.3464
```

Key Goals

- Use a graph algorithm to find paths of any length.
- Handle cycles (loops) so the program doesn't run forever.
- Keep track of visited nodes.
- Return the best rate found across all paths.
- Return None if the currencies are not connected.

Advanced Tip: Using Logarithms

To solve this efficiently, you can use math tricks. Instead of multiplying rates, you can add their logarithms.

log(a * b) = log(a) + log(b)

This turns the problem into a "Shortest Path" problem (or Longest Path). You can then use standard algorithms like Bellman-Ford.

Bonus Interview Questions

Note: These are extra questions the interviewer might ask to test your depth of knowledge.

Arbitrage (Free Money Loops)

Question: What if a cycle of trades results in a rate greater than 1? (e.g., you start with $1 and end up with $1.05).

Precision Issues

Question: Floating point numbers (like 0.1 + 0.2) are not always exact. How do you fix this?

Rate Updates

Question: What if the rates change every second?

Scaling Up

Question: How does this handle millions of requests?
