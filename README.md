# Medians and Order Statistics (Part 1)

This project demonstrates two approaches to the k-th smallest element selection problem
- **Deterministic Algorithm**: Using the Median of Medians method.
- **Randomized Algorithm**: Based on Quickselect.

It includes implementations, complexity analysis, and a summary of empirical performance based on different input distributions.

---

# 📊 Summary of Findings
- Deterministic Selection is excellent when you need guaranteed performance and are willing to accept a slight overhead.
- Randomized Selection is faster in most real-world cases and ideal when average-case performance is acceptable.
- For large datasets with unpredictable distributions, the deterministic method offers predictable latency.
- For general-purpose usage (e.g., median-finding, percentile estimation), randomized Quickselect is the preferred choice.

---

# Elementary Data Structures (Part 2)

This project implements core data structures from scratch using Python. It includes
- Array and Matrices
- Stacks and Queues
- Singly Linked Lists
- Rooted Trees

It includes implementations, complexity analysis, and a summary of empirical performance based on different input distributions.

---

# 📊 Summary of Findings
- Arrays are best for random access and small, static data sets.
- Stacks and queues are conceptually simple and important for control flows and task ordering.
- Linked lists and trees offer flexibility and dynamic behavior, but at the cost of speed and memory.
- Understanding these basic structures is essential for building more complex systems such as graphs, heaps, and hash tables.

---

## 📁 Files

- `assignment6_part1.py`: Contains source code for medians and order statistics implementation.
- `assignment6_part2.py`: Contains source code for elementary data structures implementation.
- `README.md`: Documentation and summary of results of both parts.

---

## ▶️ How to Run

1. **Clone or download** this repository.
2. Make sure you have **Python 3.6** installed or higher (no external libraries needed).
3. Run the script from the command line:

```bash
python assignment6_part1.py
python assignment6_part2.py