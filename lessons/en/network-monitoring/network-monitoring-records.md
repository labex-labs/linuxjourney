---
lesson_id: "network-monitoring-records"
course_id: "network-monitoring"
lang: "en"
order_index: 1
title: "Network Records"
description: "Learn to choose a network record that answers a particular monitoring question."
meta_title: "Network Records - Network Monitoring"
meta_description: "Learn to choose a network record that answers a particular monitoring question."
meta_keywords: "network records, network monitoring, cybersecurity, Linux Journey"
---

A network observation describes what one tool could see from one place. Start by asking what you need to learn. Different sources make different parts of the same activity visible.

## Choosing a Record Type

A **flow record** summarizes communication between network endpoints. A **DNS log** reports name lookups seen by a resolver. A **packet capture** saves copies of individual packets seen at its capture point. An endpoint is one side of communication, often identified with an address and port.

:::single-choice{#network-monitoring-records-choose-dns} You want to learn which answer a resolver returned for site.example. Which source fits best?

::option[A count of running web workers.]{#network-monitoring-records-choose-dns-b explanation="The worker count is unrelated to the lookup."}
::option[A DNS log from that resolver.]{#network-monitoring-records-choose-dns-a .correct explanation="The resolver can record the question and answer it handled."}
::option[A flow summary showing traffic volume only.]{#network-monitoring-records-choose-dns-c explanation="A flow summary may omit the DNS question and answer."}
:::

## Finding the Observation Point

A laptop capture includes packets visible to that laptop's selected interface. A server log records what arrived at the server or what the server recorded. For example, a user's request can fail before it reaches the server. Use the source whose position matches the question.

:::single-choice{#network-monitoring-records-capture-scope} You find no request in a capture on a different computer. What should you check before drawing a conclusion?

::option[Whether the capture interface could see the relevant path and time.]{#network-monitoring-records-capture-scope-b .correct explanation="A missing packet can reflect the visibility of that observation point."}
::option[Whether the capture contains some unrelated packets.]{#network-monitoring-records-capture-scope-a explanation="Seeing unrelated traffic shows that collection occurred. It leaves visibility of the relevant path and time open."}
::option[Whether another host was capturing at the same time.]{#network-monitoring-records-capture-scope-c explanation="Concurrent capture on another host does not establish what this capture interface could observe."}
:::

## Keeping the Sample Small

Packet captures can contain content people did not intend to share. Use a prepared capture with harmless practice traffic when learning to read packets. Include the viewing time and the filter when sharing a small excerpt so another person can understand its limits.

:::single-choice{#network-monitoring-records-choosing-evidence} Which sample would best teach how to identify a DNS response?

::option[A long capture of unrelated employee traffic.]{#network-monitoring-records-choosing-evidence-a explanation="It adds unnecessary data and may expose private information."}
::option[A summary with no fields describing the lookup.]{#network-monitoring-records-choosing-evidence-b explanation="That would leave the learner without the evidence to read."}
::option[A small prepared capture containing the practice query and response.]{#network-monitoring-records-choosing-evidence-c .correct explanation="It supplies just the exchange needed for the question."}
:::

## Summary

You can now choose a network record and explain what it could observe.

1. Distinguish flow summaries, DNS logs, and packet captures.
2. Match the observation point to the network path.
3. Use a focused, appropriate sample for review.
