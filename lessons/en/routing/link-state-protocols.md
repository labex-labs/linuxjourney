---
lesson_id: "link-state-protocols"
course_id: "routing"
lang: "en"
order_index: 6
title: "Link State Protocols"
description: "Learn how link-state protocols form adjacencies, flood topology information, and calculate paths."
meta_title: "Link State Protocols - Routing"
meta_description: "Learn about link state protocols like OSPF for large networks. Understand their fast convergence and how they update routing tables. Start your Linux networking journey!"
meta_keywords: "link state protocols, OSPF, Linux networking, routing protocols, network topology, beginner"
---

Link-state protocols describe local links and prefixes, distribute those descriptions through a routing scope, and let each router calculate paths from a topology database. OSPF and IS-IS are common examples.

## Forming Adjacencies

Routers discover compatible neighbors and form protocol adjacencies according to interface type, area, timers, authentication, and other parameters. Seeing hello packets does not guarantee a full adjacency; mismatched configuration can stop the state machine earlier.

:::single-choice{#link-state-hello-limit} What does receiving an OSPF hello fail to prove?

::option[That the routers formed a full synchronized adjacency.]{#link-state-not-full .correct explanation="Area, timers, authentication, MTU, and other state can prevent full database exchange."}
::option[That the neighbor sent at least one protocol message.]{#link-state-hello-sent explanation="Receiving the hello directly proves that limited fact."}
::option[That an interface can receive a frame.]{#link-state-frame-received explanation="The received packet proves some local receive path worked."}
:::

## Flooding Link-State Information

Each router originates advertisements about its relevant state. Neighbors reliably flood newer information through the defined area or domain, rather than keeping updates only between the original neighboring pair. Sequence and aging mechanisms distinguish current information and remove stale state.

:::single-choice{#link-state-flooding-scope} Why is link-state information flooded beyond one neighbor?

::option[Every application needs a copy of all router passwords.]{#link-state-password-copy explanation="Application credentials are not topology advertisements."}
::option[Ethernet cannot send unicast frames.]{#link-state-no-unicast explanation="Ethernet supports unicast; flooding here is a routing-protocol distribution mechanism."}
::option[Routers in the routing scope need a consistent topology database.]{#link-state-consistent-database .correct explanation="Each router calculates paths from the shared set of current link-state advertisements."}
:::

## Calculating Shortest Paths

After building a link-state database, a router runs a shortest-path-first algorithm, commonly Dijkstra's algorithm, from itself as the root. OSPF sums interface costs; policy and equal-cost rules influence which results are installed.

“Shortest” means lowest protocol cost, not necessarily fewest routers or lowest measured application latency. Cost design must reflect operational intent.

:::single-choice{#link-state-shortest-meaning} What does “shortest” mean in a link-state path calculation?

::option[The route whose prefix has the fewest written characters.]{#link-state-shortest-text explanation="Text length is unrelated to topology cost."}
::option[The path with the smallest sum of protocol costs.]{#link-state-lowest-cost .correct explanation="The cost model may or may not correspond directly to hop count or current latency."}
::option[The path that always has zero packet loss.]{#link-state-zero-loss explanation="A calculated route does not guarantee application performance."}
:::

## Areas and Convergence

OSPF areas limit topology flooding and calculation scope, with Area 0 serving as the backbone for normal inter-area design. Summarization and area types can intentionally give different routers different database detail.

After a link change, detection, advertisement flooding, SPF calculation, route installation, and forwarding recovery each take time. Faster convergence than a simple distance-vector design is possible, but not automatic under every failure or configuration.

:::single-choice{#link-state-convergence-stages} What should be measured during an OSPF convergence investigation?

::option[Only the time at which an administrator opened a terminal.]{#link-state-terminal-time explanation="That does not isolate protocol or forwarding stages."}
::option[Only the alphabetical order of router names.]{#link-state-router-names explanation="Names do not determine convergence timing."}
::option[Detection, flooding, calculation, installation, and forwarding recovery.]{#link-state-all-stages .correct explanation="Separating stages reveals where convergence delay or failure occurs."}
:::

## Summary

You can now follow link-state routing from neighbor discovery to installed paths.

1. Distinguish hello reception from a full adjacency.
2. Explain reliable flooding through a routing scope.
3. Interpret shortest path as lowest configured protocol cost.
4. Measure every control- and data-plane convergence stage.
