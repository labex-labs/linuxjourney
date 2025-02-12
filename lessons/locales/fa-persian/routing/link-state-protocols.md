# Link State Protocols

## Lesson Content

Link state protocols are great for large scale networks, they are more complex than distance vector protocols, however a large upside is their ability to converge quickly, this is because instead of periodically sending out the whole routing table, they only send updates to neighboring routes. They use a different algorithm to calculate the shortest path first and construct their network topology in the form of a graph to show which routers are connected to other routers.

One of the common link state protocols is OSPF (Open Shortest Path First), it only updates the routing tables if there was a network change. It doesn't have a hop limit.

## Exercise

No exercises for this lesson.

## Quiz Question

What is one of the most common link state protocols?

## Quiz Answer

OSPF