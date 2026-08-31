---
lesson_id: "bgp-border-gateway-protocol"
course_id: "routing"
lang: "en"
order_index: 7
title: "Border Gateway Protocol"
description: "Learn how BGP exchanges policy-controlled IP reachability between and within autonomous systems."
meta_title: "Border Gateway Protocol - Routing"
meta_description: "Explore the fundamentals of Border Gateway Protocol (BGP), the core protocol that enables internet routing. Learn how BGP facilitates communication between autonomous systems and the principles of border gateway protocol routing."
meta_keywords: "BGP, Border Gateway Protocol, border gateway protocol routing, internet routing, autonomous systems, Linux networking, BGP tutorial, network protocols"
---

Border Gateway Protocol is the Internet's path-vector routing protocol. It exchanges IP prefix reachability and path attributes so networks can apply administrative policy rather than choosing routes only by physical distance.

## Autonomous Systems and Sessions

An autonomous system is a set of networks under a common routing administration, identified for BGP by an autonomous system number. External BGP exchanges routes between autonomous systems; internal BGP distributes BGP reachability within one AS.

BGP peers establish a session over TCP port 179. A working TCP session is only the transport foundation; BGP capabilities, policies, and route exchange must also succeed.

:::single-choice{#bgp-external-session}
What does external BGP exchange?

::option[Ethernet frame checksums within one switch.]{#bgp-ethernet-fcs explanation="BGP operates above TCP and exchanges network-layer reachability."}
::option[User passwords between web browsers.]{#bgp-browser-passwords explanation="Application credentials are not routing attributes."}
::option[Reachability and path information between autonomous systems.]{#bgp-between-as .correct explanation="eBGP connects separate routing administrations and applies interdomain policy."}
:::

## Path-Vector Information

An advertisement includes a prefix and attributes. `AS_PATH` lists autonomous systems traversed and helps detect loops. Other common attributes include `LOCAL_PREF`, `MED`, origin, next hop, and communities. Their effect depends on direction, implementation, and policy.

:::single-choice{#bgp-as-path-loop}
How does `AS_PATH` help prevent inter-AS loops?

::option[An AS can reject a path that already contains its own number.]{#bgp-own-as-reject .correct explanation="The path vector exposes the AS sequence used to reach the advertised prefix."}
::option[It encrypts every packet crossing those systems.]{#bgp-aspath-encryption explanation="The attribute describes routing path and provides no payload encryption."}
::option[It assigns a MAC address to every AS.]{#bgp-aspath-mac explanation="Autonomous system numbers and link addresses are separate namespaces."}
:::

## Policy-Based Selection

BGP's “best” path is the path that wins a configured decision process. Operators can prefer customer routes, alter local preference, filter prefixes, use communities, and apply traffic-engineering policy. A shorter `AS_PATH` can matter at one step but does not universally override higher-priority attributes.

After BGP selects candidates, normal IP forwarding still applies longest-prefix matching. A selected `/24` is used for its destinations instead of a selected covering `/16`.

:::single-choice{#bgp-best-path-meaning}
What does a BGP best path represent?

::option[The route that wins the local attribute and policy decision process.]{#bgp-policy-winner .correct explanation="Administrative intent is central to interdomain path selection."}
::option[The physically shortest cable route in every case.]{#bgp-shortest-cable explanation="BGP has no complete physical-distance map."}
::option[A guarantee of the lowest current application latency.]{#bgp-lowest-latency explanation="BGP selection does not continuously optimize end-user latency by default."}
:::

## Advertisement and Reachability

Advertising a prefix asserts reachability under policy; it does not create the underlying route or ensure the return path. Before originating a prefix, ensure valid forwarding, aggregation behavior, filters, failover, and ownership authorization.

:::single-choice{#bgp-advertisement-limit}
What does advertising a prefix fail to guarantee?

::option[That peers can receive a control-plane route.]{#bgp-peers-control explanation="Successful advertisement and acceptance can establish that limited control-plane fact."}
::option[That the prefix contains address bits.]{#bgp-prefix-bits explanation="An IP prefix is defined by address bits and length."}
::option[That it can deliver packets for the whole prefix.]{#bgp-data-plane-not-guaranteed .correct explanation="Underlying routes, next hops, filtering, and service health still need verification."}
:::

## Routing Security and Change Control

Route leaks and hijacks can affect traffic far beyond one router. Operators use strict import and export filters, maximum-prefix limits, peer policy, monitoring, and Resource Public Key Infrastructure origin validation where appropriate. RPKI origin validation checks whether an AS is authorized to originate a prefix; it does not validate the complete AS path.

BGP changes require staged rollout, route-diff review, out-of-band access, rollback, and both control- and data-plane verification.

:::single-choice{#bgp-rpki-limit}
What does RPKI origin validation check?

::option[Whether every packet payload is malware-free.]{#bgp-payload-malware explanation="RPKI does not inspect application content."}
::option[Whether the complete AS path has the lowest latency.]{#bgp-path-latency explanation="Origin validation is not performance selection or full path validation."}
::option[Whether the origin AS is authorized.]{#bgp-origin-authorized .correct explanation="It validates origin authorization, not every transit relationship in the AS path."}
:::

## Summary

You can now describe BGP as policy-controlled path-vector routing.

1. Distinguish external from internal BGP sessions.
2. Use `AS_PATH` as path and loop information.
3. Interpret best path through local attributes and policy.
4. Verify forwarding behind every advertised prefix.
5. Apply filtering, origin validation, monitoring, and rollback.
