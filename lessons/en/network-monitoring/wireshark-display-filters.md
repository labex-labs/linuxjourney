---
lesson_id: "wireshark-display-filters"
course_id: "network-monitoring"
lang: "en"
order_index: 4
title: "Wireshark Display Filters"
description: "Learn to limit the view of a prepared capture with a Wireshark display filter."
meta_title: "Wireshark Display Filters - Network Monitoring"
meta_description: "Learn to limit the view of a prepared capture with a Wireshark display filter."
meta_keywords: "wireshark display filters, network monitoring, cybersecurity, Linux Journey"
---

A packet capture can hold many protocols. A **display filter** tells Wireshark which saved packets to display. It changes what you see while leaving the capture file intact.

## Selecting a Protocol

Open the [sample capture](https://github.com/labex-labs/linuxjourney/blob/master/examples/network-monitoring/sample.pcap) on GitHub and save the file as `sample.pcap`. Open it in Wireshark and enter `dns` in the display filter box. On a Linux terminal with TShark installed, this command applies the same filter to the saved file. The file in this example contains a harmless lookup and separate sample traffic.

```bash
$ tshark -r sample.pcap -Y dns
```

The `-r` option reads a file and `-Y` applies a display filter. Look for a query and its response.

:::single-choice{#wireshark-display-filters-display-effect} The filtered list shows two fewer rows than the original view. What happened to the other packets?

::option[They were deleted from the capture file.]{#wireshark-display-filters-display-effect-a explanation="A display filter changes the visible results."}
::option[They are still saved and did not match this filter.]{#wireshark-display-filters-display-effect-b .correct explanation="Clear the filter to see the unfiltered view again."}
::option[They were sent out again on the network.]{#wireshark-display-filters-display-effect-c explanation="Reading a saved capture does not transmit its packets."}
:::

## Matching an Address

A filter can also refer to a packet field. `ip.addr` matches an IPv4 source or destination address. The two equals signs compare the field with the sample value.

```bash
$ tshark -r sample.pcap -Y 'ip.addr == 192.0.2.10'
```

The shell quotes keep the expression together as one argument. You can recognize the endpoints in the displayed rows.

:::single-choice{#wireshark-display-filters-address-scope} A packet goes to 192.0.2.10 from a different address. Will it match?

::option[Yes, because the condition checks either endpoint.]{#wireshark-display-filters-address-scope-a .correct explanation="Ip.addr can match the source or the destination."}
::option[No, because the condition checks the source only.]{#wireshark-display-filters-address-scope-b explanation="This field can match both directions."}
::option[Only if the packet contains DNS.]{#wireshark-display-filters-address-scope-c explanation="This expression only checks the IPv4 address."}
:::

![Recorded TShark output comparing the DNS-only display with both protocols in the practice capture](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/network-monitoring/wireshark-display-filters/saved-dns-exchange.png)

## Explaining an Empty View

An empty result means the filter found no matching saved packets in the file you examined. Check the expression, time, and capture point before making a broader claim. Start by clearing the filter to confirm the capture contains traffic.

:::single-choice{#wireshark-display-filters-empty-capture-view} You apply dns to a saved capture and see no rows. What can you report?

::option[No one used DNS anywhere on the network.]{#wireshark-display-filters-empty-capture-view-a explanation="A file covers a limited capture point and time."}
::option[Wireshark erased the DNS evidence.]{#wireshark-display-filters-empty-capture-view-b explanation="The display filter does not delete saved packets."}
::option[This filter displayed no DNS packets in this capture.]{#wireshark-display-filters-empty-capture-view-c .correct explanation="That statement stays within the evidence you examined."}
:::

To inspect another capture in a browser lab, try the display-filter exercise in [Wireshark for Beginners](https://labex.io/courses/quick-start-with-wireshark).

## Summary

You can now filter a saved packet capture and explain the result's scope.

1. Select a protocol with a display filter.
2. Match a packet address with ip.addr.
3. Interpret a filtered view using the file's visibility limits.
