# Homework 1: Graph ADT & Traversals

Follow the instructions [here](https://make-school-courses.github.io/CS-2.2-Graphs-Recursion/#/Assignments/01-Graph-ADT) to complete this assignment.

## Discussion Questions

1. How is Breadth-first Search different in graphs than in trees? Describe the differences in your own words.

Breadth-first Search for Trees goes levels by levels. For graphs its similar, but graphs can cycle unlike trees. This means once a node is visited in a Tree it cannot be revisited.

2. What is one application of Breadth-first Search (besides social networks)? Describe how BFS is used for that application. If you need some ideas, check out [this article](https://www.geeksforgeeks.org/applications-of-breadth-first-traversal/?ref=rp).

One application would be to optimize routes for a GPS-based map application. Each waypoint would be a vertex and the route would be the shortest path from start waypoint to target waypoint.