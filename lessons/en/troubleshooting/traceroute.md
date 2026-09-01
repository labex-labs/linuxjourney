---
lesson_id: "traceroute"
course_id: "troubleshooting"
lang: "en"
order_index: 3
title: "traceroute"
description: "Learn how traceroute discovers responding hops and how to interpret gaps, timing, and path variation."
meta_title: "traceroute - Troubleshooting"
meta_description: "Master the traceroute linux command to trace network routes and troubleshoot connectivity issues. This tutorial explains how traceroute uses TTL to map the path packets take to their destination."
meta_keywords: "traceroute, traceroute linux, Linux networking, network troubleshooting, TTL, packet routing, Linux commands, beginner, tutorial"
---

`traceroute` sends probes with increasing IPv4 TTL or IPv6 Hop Limit values. Routers where the value expires can return Time Exceeded messages, revealing some responding points along the forward path.

## How Hop Discovery Works

Probes begin with a hop limit of one and increase. The first router decrements one to zero and can return an ICMP error. A limit of two reaches the second router before expiring, and the process continues until the destination responds or the maximum is reached.

:::single-choice{#traceroute-expiring-field} Which field causes successive probes to expire at later routers?

::option[The DNS cache TTL for the destination name.]{#traceroute-dns-ttl explanation="DNS record lifetime does not control packet forwarding hops."}
::option[The Ethernet source MAC address.]{#traceroute-source-mac explanation="Link addresses do not carry an end-to-end hop counter."}
::option[IPv4 TTL or IPv6 Hop Limit.]{#traceroute-hop-field .correct explanation="Increasing this bounded forwarding count exposes responding routed hops."}
:::

## Probe Methods

Traditional Linux traceroute commonly sends UDP probes to high destination ports. The destination can signal completion with ICMP Port Unreachable. Options can instead use ICMP Echo or TCP SYN probes, which can traverse filtering differently:

```bash
$ traceroute -n example.com
$ traceroute -I -n example.com
$ traceroute -T -p 443 -n example.com
```

Privileges and supported options vary. Use methods authorized for the target, and record the method when comparing results.

:::single-choice{#traceroute-default-destination-response} What commonly ends a traditional Linux UDP traceroute?

::option[An ICMP Port Unreachable response from the destination.]{#traceroute-port-unreachable .correct explanation="High UDP ports are normally unused, allowing the destination to identify itself through the error."}
::option[A mandatory HTTP 200 response from every router.]{#traceroute-http-every-router explanation="Routers return network-control errors rather than HTTP responses."}
::option[An Ethernet broadcast from the destination across the Internet.]{#traceroute-ethernet-broadcast explanation="Link broadcasts do not cross routed paths."}
:::

## Interpreting Asterisks

An asterisk means no response was observed for that probe before timeout. The router may forward transit traffic while filtering or rate-limiting diagnostic responses. If later hops answer, the silent hop clearly forwarded at least some probes.

:::single-choice{#traceroute-asterisk-meaning} What does `*` at one hop prove?

::option[That the router dropped all transit packets permanently.]{#traceroute-star-all-drop explanation="Later replies can demonstrate continued forwarding."}
::option[Only that no matching response arrived before the probe timeout.]{#traceroute-star-no-response .correct explanation="Filtering, rate limiting, loss, and return-path issues can all produce silence."}
::option[That the destination has no IP address.]{#traceroute-star-no-address explanation="The probe already targets an address, and one silent hop does not erase it."}
:::

## Timing and Path Variation

Per-hop times measure round trips to control responses, not latency added by the link between adjacent printed lines. Routers can deprioritize control-plane replies. Load balancing can send probes through different paths, and name resolution can add display delay; `-n` avoids reverse lookups.

The return route for each ICMP response can differ from the forward route. Repeat tests and correlate with endpoint application timing before identifying a bottleneck.

:::single-choice{#traceroute-hop-rtt-limit} Why should adjacent hop RTT values not be subtracted as exact link latency?

::option[Traceroute reports all times in bytes rather than milliseconds.]{#traceroute-times-bytes explanation="The displayed probe timings are normally milliseconds."}
::option[Replies can use different return paths and control-plane processing.]{#traceroute-rtt-asymmetry .correct explanation="The measurements are separate end-to-hop round trips rather than synchronized one-way link samples."}
::option[Every router has the same clock as the source.]{#traceroute-router-clock explanation="The measurement does not rely on remote clock synchronization."}
:::

## Comparing with the Application

A traceroute can reach the destination while the service is blocked, and the service can work while intermediate routers hide their responses. Test the same address family, destination, transport protocol, and port as the application, then use traceroute as supporting path evidence.

:::single-choice{#traceroute-service-proof} Does a completed traceroute prove an HTTPS service is healthy?

::option[Yes, because every hop validates the server certificate.]{#traceroute-validates-cert explanation="Routers do not perform the client's TLS validation."}
::option[No; transport, TLS, and HTTP behavior need their own tests.]{#traceroute-not-app-proof .correct explanation="Path discovery and application health are different diagnostic layers."}
::option[Yes, but only if reverse DNS names are printed.]{#traceroute-rdns-proof explanation="Names do not establish application function."}
:::

## Summary

You can now interpret traceroute as a series of bounded-hop probes, not a complete path oracle.

1. Explain hop discovery through TTL or Hop Limit expiration.
2. Record whether UDP, ICMP, or TCP probes were used.
3. Treat asterisks as missing responses rather than proven outages.
4. Avoid deriving exact link latency from adjacent hop RTTs.
5. Correlate path evidence with the real application.
