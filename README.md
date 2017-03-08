# eve-nav-graph

A navigation resource which provides pre-computed shortest paths for travel in EVE Online.
Its purpose is to circumvent ceiling issues such as a limited number of waypoints. 

The graph is constructed by processing EVE SDE data in the networkx library for Python.

Shortest paths will be calculated using Dijkstra's algorithm.
Final data will be stored in a neo4j graph database.
