---
lesson_id: "distance-vector-protocols"
course_id: "routing"
lang: "en"
order_index: 5
title: "Distance Vector Protocols"
description: "Learn how distance-vector protocols derive routes from neighbor advertisements and limit loops."
meta_title: "Distance Vector Protocols - Routing"
meta_description: "A beginner guide to distance vector protocols in network routing. This tutorial explains how protocols like RIP use hop count to determine routes and covers their limitations for modern Linux networking."
meta_keywords: "distance vector protocols, network routing, RIP, routing information protocol, hop count, Linux networking, beginner guide, tutorial"
---

Distance-vector routing tells neighbors which destinations are reachable and a metric describing the distance. A router combines a neighbor's advertisement with the cost to that neighbor to derive its own candidate path.

## Learning Through Neighbors

If Router A advertises a distance of three to a prefix and Router B reaches A with cost one, B can derive distance four through A. The information describes a direction and metric, not a complete topology map, which is why the approach is sometimes called routing by rumor.

:::single-choice{#distance-vector-derived-distance}
If a neighbor advertises metric 3 and the link cost is 1, what metric is derived through it?

::option[2]{#distance-vector-two explanation="The link cost is added rather than subtracted."}
::option[31]{#distance-vector-thirty-one explanation="The values are metrics, not decimal digits to concatenate."}
::option[4]{#distance-vector-four .correct explanation="The neighbor distance and local link cost combine for the candidate path."}
:::

## Loops and Count to Infinity

After a failure, neighbors can mistakenly advertise a route back to each other, gradually increasing its metric. Protocols mitigate this with finite infinity values, split horizon, route poisoning, poison reverse, triggered updates, and timers. These mechanisms reduce but do not turn every topology change into instantaneous convergence.

:::single-choice{#distance-vector-split-horizon}
What is split horizon intended to reduce?

::option[The number of bits in every IPv4 address.]{#distance-vector-ip-bits explanation="IPv4 address size is fixed independently of routing updates."}
::option[Encryption overhead in application payloads.]{#distance-vector-encryption explanation="The technique concerns route advertisement direction."}
::option[Advertising a learned route back toward the neighbor it came from.]{#distance-vector-no-return .correct explanation="Suppressing that direction helps prevent simple feedback loops."}
:::

## RIP Metrics and Limits

RIP uses hop count. A route with metric 16 is unreachable, so the largest usable metric is 15. That bounds loop escalation but also limits network diameter. Fewer hops do not necessarily mean lower latency or more bandwidth.

RIPv2 uses periodic and triggered updates and supports CIDR information. It commonly multicasts updates rather than broadcasting an entire table in every circumstance. Authentication and filtering still require deliberate configuration.

:::single-choice{#distance-vector-rip-infinity}
What does RIP metric 16 represent?

::option[The fastest path with sixteen parallel links.]{#distance-vector-fastest-16 explanation="RIP treats the value as unreachable."}
::option[Infinity, meaning the destination is unreachable.]{#distance-vector-unreachable .correct explanation="RIP caps usable paths at 15 hops."}
::option[A route learned from BGP.]{#distance-vector-bgp-route explanation="The number has a RIP-specific meaning."}
:::

## Evaluating a Learned Route

Check neighbor state, received and advertised prefixes, metric, next hop, route installation, and data-plane reachability. A route can be valid within RIP but lose to another route source under local preference policy.

:::single-choice{#distance-vector-fewest-hop-limit}
Why can RIP's lowest-hop route perform poorly?

::option[Hop count does not encode link bandwidth, latency, loss, or congestion.]{#distance-vector-hop-limited .correct explanation="A path with more hops can have better links and application performance."}
::option[RIP always chooses the route with the most hops.]{#distance-vector-most-hops explanation="Its metric prefers smaller usable hop counts."}
::option[Hop count is measured in bytes of disk space.]{#distance-vector-disk-bytes explanation="It counts routed transitions rather than storage."}
:::

## Summary

You can now explain both the simplicity and limitations of distance-vector routing.

1. Derive candidate distance from a neighbor's advertisement.
2. Recognize loop and count-to-infinity behavior.
3. Explain RIP's 15-hop usable limit and metric 16.
4. Verify route installation and data-plane outcome separately.
