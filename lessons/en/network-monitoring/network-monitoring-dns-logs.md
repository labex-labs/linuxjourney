---
lesson_id: "network-monitoring-dns-logs"
course_id: "network-monitoring"
lang: "en"
order_index: 3
title: "DNS Logs"
description: "Learn to distinguish a DNS question, its answer, and a later application connection."
meta_title: "DNS Logs - Network Monitoring"
meta_description: "Learn to distinguish a DNS question, its answer, and a later application connection."
meta_keywords: "dns logs, network monitoring, cybersecurity, Linux Journey"
---

Before connecting to a service by name, a client may ask DNS for an address. A resolver can record the question and its result. A **resolver** looks up names for clients.

## Identifying the Question

A DNS record can contain the time, client address, name, and requested record type. An `A` query asks for an IPv4 address.

```text
09:21:00Z client=192.0.2.10 query=site.example type=A result=NOERROR answer=192.0.2.20
09:21:03Z client=192.0.2.10 query=preview.example type=A result=NXDOMAIN
```

The first result contains an address for `site.example`. The second reports that DNS found no name matching `preview.example` in this lookup.

:::single-choice{#network-monitoring-dns-logs-lookup-name} Which row returned an IPv4 address for the requested name?

::option[The lookup for site.example.]{#network-monitoring-dns-logs-lookup-name-a .correct explanation="That row includes an answer containing an IPv4 address."}
::option[The lookup for preview.example.]{#network-monitoring-dns-logs-lookup-name-b explanation="NXDOMAIN reports that the queried name does not exist in the lookup view."}
::option[Both rows, because they have the same client.]{#network-monitoring-dns-logs-lookup-name-c explanation="The client is shared and the lookup results differ."}
:::

## Reading the Outcome

`NOERROR` means the DNS exchange did not report a protocol error. Check the answer field too. A response can use `NOERROR` and contain no address record of the type requested. A failed lookup may also appear as a different result, such as a timeout recorded by the client.

:::single-choice{#network-monitoring-dns-logs-no-answer} A DNS row says NOERROR but has no address answer. What should you report?

::option[The client necessarily received an IPv4 address.]{#network-monitoring-dns-logs-no-answer-a explanation="The answer field gives the addresses returned for the sample."}
::option[The site definitely refused a browser connection.]{#network-monitoring-dns-logs-no-answer-c explanation="This row records a DNS result, not a browser request."}
::option[The exchange returned without a protocol error, and this row gives no address.]{#network-monitoring-dns-logs-no-answer-b .correct explanation="The result and answer fields answer different questions."}
:::

## Following the Connection Separately

A client can look up a name and then choose to make a connection. To test whether that happened, find a matching flow or connection record. Compare the endpoint and time. DNS results may be cached, so some connections occur without a fresh lookup in the available logs.

:::single-choice{#network-monitoring-dns-logs-dns-vs-flow} What would best show that a client later connected to the returned address?

::option[Another view of the DNS answer alone.]{#network-monitoring-dns-logs-dns-vs-flow-a explanation="The answer lists an address for the client to use."}
::option[A corresponding connection or flow record showing the destination.]{#network-monitoring-dns-logs-dns-vs-flow-c .correct explanation="This tracks subsequent traffic separately from the lookup."}
::option[A second DNS lookup from the same client.]{#network-monitoring-dns-logs-dns-vs-flow-b explanation="Another lookup confirms repeated name resolution activity. It leaves the later application connection unverified."}
:::

## Summary

You can now read a DNS log without confusing it with later network activity.

1. Find the client, question, and requested record type.
2. Interpret the result and answer together.
3. Look for a separate record of a later connection.
