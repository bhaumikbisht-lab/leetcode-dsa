# Patterns I Have Learned So Far

Notes from my first 10 solved problems — the pattern behind each one,
in my own words. One pattern at a time, understood properly, beats
ten problems copied blindly.

## 1. HashMap / HashSet — "have I seen this before?"
- **Two Sum** — store each number's index; for `x`, look up `target - x`. O(n)
- **Contains Duplicate** — a set remembers what already appeared. O(n)
- **Group Anagrams** — sorted string (or letter count) as a dictionary key. O(n·k log k)

Rule: when a problem asks about pairs, duplicates or grouping,
reach for a hash structure first.

## 2. Two Pointers — "shrink from both ends"
- **Valid Palindrome** — left/right pointers skipping non-alphanumerics. O(n), O(1) space
- **Two Sum II (sorted)** — move the pointer on the side that is wrong. O(n)
- **Container With Most Water** — move the *shorter* line inward; moving the taller one can never help. O(n)
- **3Sum** — fix one number, then two-pointer the rest; skip duplicates carefully. O(n²)

Rule: sorted input (or a palindrome / pair-in-array shape) usually
means two pointers beat a nested loop.

## 3. Sliding Window — "a moving range with a promise"
- **Longest Substring Without Repeating Characters** — window + last-seen
  index; when a repeat enters, jump the left edge past it. O(n)
- **Best Time to Buy and Sell Stock** — one pass keeping the minimum
  price so far (the simplest window of all: buy low, track best profit). O(n)

Rule: "longest / smallest subarray or substring with a condition"
almost always means a window, not brute force.

## 4. Stack — "last in, first out matching"
- **Valid Parentheses** — push openers, pop and match closers;
  valid only if the stack ends empty. O(n)

Rule: matching pairs, nesting, or "most recent unfinished thing"
means a stack.

## Complexity habits
- Say the complexity out loud before coding — it catches O(n²)
  brute force early.
- After solving, ask: "which pattern was this?" and file the
  problem under it (this file is that habit, written down).

*Updated as new topics are covered — next: Binary Search, Linked List.*
