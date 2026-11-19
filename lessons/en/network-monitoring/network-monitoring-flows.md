---
lesson_id: "network-monitoring-flows"
course_id: "network-monitoring"
lang: "en"
order_index: 2
title: "Network Flows"
description: "Learn to interpret addresses, ports, timing, and byte counts in a flow summary."
meta_title: "Network Flows - Network Monitoring"
meta_description: "Learn to interpret addresses, ports, timing, and byte counts in a flow summary."
meta_keywords: "network flows, network monitoring, cybersecurity, Linux Journey"
---

A **flow** groups traffic that shares properties such as network addresses, ports, and protocol. Monitoring systems can count the bytes or packets in a flow without keeping the full contents.

## Reading the Two Endpoints

In this simulated summary the collector records a direction from a source to a destination. Transport protocols such as TCP include port numbers, which can identify a listener on the receiving side.

```text
start=09:21:00Z protocol=TCP src=192.0.2.10:51600 dst=192.0.2.20:443 bytes=1800
start=09:21:00Z protocol=TCP src=192.0.2.20:443 dst=192.0.2.10:51600 bytes=8200
```

The first line goes toward port 443. The second shows the reverse direction. Some collectors group both directions together, so check the format you are reading.

:::single-choice{#network-monitoring-flows-endpoint-direction} In the first row, which address and port receive the recorded traffic?

::option[192.0.2.10:51600.]{#network-monitoring-flows-endpoint-direction-a explanation="That is the sending endpoint in the first direction."}
::option[Both listed endpoints as destinations.]{#network-monitoring-flows-endpoint-direction-c explanation="Each row in this sample has one recorded direction."}
::option[192.0.2.20:443.]{#network-monitoring-flows-endpoint-direction-b .correct explanation="The destination field tells you where the traffic was sent."}
:::

## Comparing the Counts

The sample shows more bytes in the direction from port 443. A larger response may be normal for a web page. The count alone gives no page content, account, or reason for the volume.

:::single-choice{#network-monitoring-flows-byte-count} What do 8,200 bytes in the second row describe?

::option[The response's exact message text.]{#network-monitoring-flows-byte-count-b explanation="The flow summary gives a volume and omits the message."}
::option[The recorded amount in that direction.]{#network-monitoring-flows-byte-count-a .correct explanation="The byte count summarizes traffic, while the source and destination identify its direction."}
::option[A guarantee that the page loaded successfully.]{#network-monitoring-flows-byte-count-c explanation="The volume does not give the HTTP outcome."}
:::

## Adding Context

Use known service information and time to decide which flows are relevant. If you need to know what the web server returned, compare with its access logs for the same time and connection where available.

:::single-choice{#network-monitoring-flows-next-source} You want the HTTP status for the web request. Which additional source would help?

::option[A corresponding web access record.]{#network-monitoring-flows-next-source-c .correct explanation="A server access record can report the HTTP result."}
::option[The flow byte count rounded to the nearest hundred.]{#network-monitoring-flows-next-source-a explanation="Rounding changes the precision and adds no response status."}
::option[A second flow summary for the same endpoints.]{#network-monitoring-flows-next-source-b explanation="A flow summary can confirm more traffic observations. It does not normally give the HTTP response status."}
:::

## Summary

You can now read the main fields of one flow summary.

1. Find endpoint addresses and ports.
2. Interpret byte counts in the reported direction.
3. Choose another source when application results matter.
