# Homework 1 & 2: Graph ADT & Traversals

Follow the instructions [here](https://make-school-courses.github.io/CS-2.2-Graphs-Recursion/#/Assignments/01-Graph-ADT) to complete this assignment.

## Discussion Questions for Homework 1

1. How is Breadth-first Search different in graphs than in trees? Describe the differences in your own words.

Breadth-first Search for Trees goes levels by levels. For graphs its similar, but graphs can cycle unlike trees. This means once a node is visited in a Tree it cannot be revisited.

2. What is one application of Breadth-first Search (besides social networks)? Describe how BFS is used for that application. If you need some ideas, check out [this article](https://www.geeksforgeeks.org/applications-of-breadth-first-traversal/?ref=rp).

One application would be to optimize routes for a GPS-based map application. Each waypoint would be a vertex and the route would be the shortest path from start waypoint to target waypoint.

## Discussion Questions for Homework 2

1. Compare and contrast Breadth-first Search and Depth-first Search by providing one similarity and one difference.



2. Explain why a Depth-first Search traversal does not necessarily find the shortest path between two vertices. What is one such example of a graph where a DFS search would not find the shortest path?



3. Explain why we cannot perform a topological sort on a graph containing a cycle.

