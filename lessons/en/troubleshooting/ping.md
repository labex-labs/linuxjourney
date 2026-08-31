---
lesson_id: "ping"
course_id: "troubleshooting"
lang: "en"
order_index: 2
title: "ping"
description: "Learn how to run bounded ping tests and interpret replies, loss, RTT, TTL, and limitations."
meta_title: "ping - Troubleshooting"
meta_description: "Learn to use the Linux ping command to test network connectivity. This guide explains the ping output, including the meaning of icmp_seq, TTL, and roundtrip time. Understand how to interpret the ping seq to diagnose network issues."
meta_keywords: "Linux ping, network connectivity, ICMP, TTL, ping command, icmp_seq, ping seq, icmp seq, icmp_seq meaning, ping icmp_seq, Linux networking"
---

`ping` sends ICMP Echo Requests and reports observed replies. It tests one control-message path to an address; it does not prove that TCP, UDP, DNS, authentication, or an application works.

## Running a Bounded Test

Send three IPv4 requests with a two-second per-packet timeout on common iputils implementations:

```bash
$ ping -4 -c 3 -W 2 example.com
```

Use `-6` to select IPv6. Record the resolved address because a hostname can return several addresses and repeated runs can choose differently.

:::single-choice{#ping-count-option}
What does `-c 3` request?

::option[A packet payload of exactly three megabytes.]{#ping-three-megabytes explanation="Packet size uses a different option."}
::option[Three permanent routes to the destination.]{#ping-three-routes explanation="Ping probes traffic and does not install routes."}
::option[Three Echo Requests before the command stops normally.]{#ping-three-requests .correct explanation="A finite count makes the diagnostic bounded and repeatable."}
:::

## Sequence and Loss

`icmp_seq` identifies requests within the run. Missing replies contribute to observed loss, while out-of-order replies can reflect varying delay. Small samples are noisy; compare multiple bounded intervals and the application's own error rate.

Loss can occur in either direction, and ICMP rate limiting can make ping loss differ from application loss.

:::single-choice{#ping-sequence-gap}
What can a missing `icmp_seq` reply indicate?

::option[The destination permanently changed its MAC address.]{#ping-sequence-mac explanation="A sequence gap alone provides no such link-layer conclusion."}
::option[The request or reply was lost, filtered, delayed past the wait, or rate-limited.]{#ping-sequence-possibilities .correct explanation="The sequence gap identifies an absent observed reply but not the exact direction or cause."}
::option[The source disk has no free inodes.]{#ping-sequence-inodes explanation="Filesystem inode state is unrelated to an ICMP sequence response."}
:::

## Round-Trip Time

The `time` field is round-trip time in milliseconds from sending the request to receiving its reply. It combines outbound delay, remote processing, and return delay. It cannot reveal one-way latency without synchronized endpoint measurements.

:::single-choice{#ping-rtt-meaning}
What does a reported `time=23.7 ms` measure?

::option[Only the one-way outbound path latency.]{#ping-outbound-only explanation="Ping measures the complete request-and-reply interval."}
::option[The target's system uptime.]{#ping-target-uptime explanation="The value is timing for the probe, not boot duration."}
::option[The round-trip time for that echo.]{#ping-round-trip .correct explanation="It includes both directions and endpoint handling."}
:::

## TTL or Hop Limit

The displayed IPv4 TTL or IPv6 Hop Limit is the value remaining in the received reply. Without knowing the sender's initial value and return route, subtracting it does not yield an exact hop count. A change can reflect a different responder, initial value, or return path.

:::single-choice{#ping-received-ttl}
What is the TTL printed on an IPv4 Echo Reply?

::option[The remaining value when the reply reached the local host.]{#ping-remaining-ttl .correct explanation="Each router on the return path decremented the sender's initial value."}
::option[An exact count of routers in both directions.]{#ping-exact-hop-count explanation="The initial TTL and directional path are not established by this field alone."}
::option[The DNS record's cache lifetime.]{#ping-dns-ttl explanation="DNS TTL and IP packet TTL are different fields."}
:::

## Testing the Right Layer

If ping succeeds but a service fails, test the actual port, TLS, protocol, and request. If ping fails, inspect name resolution, `ip route get`, neighbor state, firewall policy, and captures before declaring the host down.

:::single-choice{#ping-success-limit}
What does a successful ping fail to prove?

::option[That some ICMP request and reply path worked.]{#ping-icmp-worked explanation="That is the direct evidence supplied by replies."}
::option[That the reply contained a sequence number.]{#ping-sequence-present explanation="Normal output directly reports the reply sequence."}
::option[That the intended application accepts and completes requests.]{#ping-app-not-proven .correct explanation="Application and transport behavior require an application-appropriate test."}
:::

## Summary

You can now use ping as a bounded ICMP measurement with explicit limits.

1. Select the address family and record the resolved address.
2. Bound count and wait time for repeatable tests.
3. Interpret loss without assuming its direction or cause.
4. Treat RTT as two-way and TTL as a remaining value.
5. Test the real application separately.
