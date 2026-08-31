---
lesson_id: "routing-protocols"
course_id: "routing"
lang: "en"
order_index: 4
title: "Routing Protocols"
description: "Learn how dynamic routing protocols exchange reachability and converge on usable forwarding paths."
meta_title: "Routing Protocols - Routing"
meta_description: "Explore the fundamentals of routing protocols in Linux networking. This guide covers distance vector and link state protocols, network convergence, and how routers build and maintain routing tables. A perfect tutorial for beginners."
meta_keywords: "routing protocols, network convergence, distance vector, link state, linux networking, routing table, network tutorial, beginner guide, router communication"
---

Static routes are configured directly, while dynamic routing protocols exchange reachability and topology information so routers can adapt. Dynamic learning reduces manual work but introduces protocol state, trust boundaries, timers, and failure modes that must be monitored.

## Control Plane and Forwarding Plane

A routing protocol learns candidates in its own database. The router selects routes into a routing information base and installs usable next hops into a forwarding table. Hardware or the kernel then forwards packets from that table.

A protocol adjacency being established does not prove that the desired prefix was learned, selected, installed, or permitted by forwarding policy.

:::single-choice{#routing-protocols-adjacency-limit}
What does an established routing adjacency fail to prove?

::option[That every desired route is installed and forwarding successfully.]{#routing-protocols-not-full-proof .correct explanation="Route advertisement, selection, installation, filtering, and data-plane operation are separate stages."}
::option[That two protocol speakers exchanged any control messages.]{#routing-protocols-no-messages explanation="Establishing adjacency normally requires protocol communication."}
::option[That a control plane exists.]{#routing-protocols-no-control explanation="The adjacency is itself control-plane state."}
:::

## Interior and Exterior Routing

Interior gateway protocols operate within an administrative routing domain. Examples include RIP, OSPF, and IS-IS. BGP exchanges policy-controlled reachability within and between autonomous systems and is the Internet's exterior routing protocol.

Metrics have protocol-specific meaning. An OSPF cost, RIP hop count, and BGP attribute set cannot be compared as if they shared one universal numerical scale. Implementations use route preference or administrative distance to choose between sources before or alongside protocol-specific selection.

:::single-choice{#routing-protocols-metric-comparison}
Can a RIP hop count be directly compared with an OSPF cost?

::option[Yes, because all routing metrics use the same units.]{#routing-protocols-universal-metric explanation="Each protocol defines its own metric and selection process."}
::option[Yes, but only when both values are zero.]{#routing-protocols-zero-metric explanation="Their semantics remain different regardless of a displayed number."}
::option[No; they have protocol-specific meanings.]{#routing-protocols-specific-metric .correct explanation="Cross-source selection uses implementation policy rather than treating unlike metrics as one scale."}
:::

## Distance Vector and Link State

Distance-vector protocols advertise reachability and distance through neighbors, deriving paths from neighbor reports. Link-state protocols form adjacencies, flood link-state information through a scope, build a topology database, and calculate shortest-path trees. Modern protocols include refinements that make simple category summaries incomplete.

:::single-choice{#routing-protocols-link-state-input}
What does a link-state router use for its path calculation?

::option[Only the hostname of its default gateway.]{#routing-protocols-hostname-only explanation="A topology calculation requires link and prefix information."}
::option[A synchronized database describing links in the routing scope.]{#routing-protocols-link-database .correct explanation="The router runs a shortest-path algorithm over the learned topology."}
::option[Application-layer passwords from every host.]{#routing-protocols-passwords explanation="Routing topology exchange does not require end-user credentials."}
:::

## Convergence

After a topology or policy change, routers detect it, propagate control information, calculate paths, and update forwarding state. Convergence is the period and outcome in which the network reaches stable, mutually usable routing for the affected destinations. It does not require every router to have an identical full table; roles and policies can intentionally differ.

During convergence, transient loss, loops, or black holes can occur. Measure detection, propagation, calculation, and installation separately and verify with data-plane probes.

:::single-choice{#routing-protocols-convergence}
What is routing convergence?

::option[The process of reaching stable usable routing after a change.]{#routing-protocols-stable-routing .correct explanation="It includes control propagation and the resulting forwarding updates."}
::option[A requirement that every router store an identical global table.]{#routing-protocols-identical-table explanation="Policy, area, and role can create intentional differences."}
::option[Permanent prevention of every possible routing failure.]{#routing-protocols-no-failure explanation="A converged network can still have policy or capacity problems."}
:::

## Summary

You can now place dynamic routing information in the path from protocol exchange to forwarding.

1. Separate learned candidates, selected routes, and forwarding entries.
2. Distinguish interior routing from BGP policy exchange.
3. Compare metrics only within their protocol semantics.
4. Verify convergence in both control and data planes.
