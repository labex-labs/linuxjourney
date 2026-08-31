---
lesson_id: "packet-analysis"
course_id: "troubleshooting"
lang: "en"
order_index: 5
title: "Packet Analysis"
description: "Learn how to capture a bounded, filtered packet trace and analyze it safely with tcpdump."
meta_title: "Packet Analysis - Troubleshooting"
meta_description: "Learn the fundamentals of network packet analysis in Linux. This guide introduces tcpdump, a powerful packet analyzer, to capture and interpret network traffic."
meta_keywords: "tcpdump, packet analysis, network packet analysis, network packet analyzer, network analysis, network packet analysis tools, Linux networking, Wireshark, Linux commands, network traffic"
---

Packet capture records traffic visible at a chosen observation point. It can reveal protocol exchanges and timing, but it can also collect credentials, personal data, and unrelated users' traffic. Obtain authorization, minimize scope, protect files, and follow retention policy.

## Choosing the Observation Point

Capture on the interface and network namespace through which the affected flow actually passes. Bridges, containers, VPNs, bonds, VLANs, and offload can change what one interface shows. Use `ip route get` and `ip link` to identify candidates before capturing.

:::single-choice{#packet-analysis-interface-choice}
Why does capture-interface choice matter?

::option[Every interface automatically mirrors the entire Internet.]{#packet-analysis-mirrors-internet explanation="A host normally sees only traffic delivered through or mirrored to its interfaces."}
::option[Only traffic visible at that observation point can be recorded.]{#packet-analysis-visible-point .correct explanation="Namespaces, tunnels, bridges, and routing can place the relevant flow elsewhere."}
::option[The interface name decrypts TLS payloads.]{#packet-analysis-name-decrypts explanation="Naming has no decryption capability."}
:::

## Capturing a Bounded Flow

Capture up to 100 packets without name resolution, restricted to a host and TCP port:

```bash
$ sudo tcpdump -i enp1s0 -n -c 100 -w incident.pcap \
    'host 192.0.2.25 and tcp port 443'
```

`-i` selects the interface, `-n` keeps numeric names, `-c` bounds packet count, `-w` writes pcap data, and the final expression is a capture filter. Also set a time bound externally when traffic may be absent.

:::single-choice{#packet-analysis-count-bound}
What does `-c 100` do?

::option[Captures only TCP port 100.]{#packet-analysis-port-hundred explanation="Port selection belongs in the filter expression."}
::option[Compresses the file to 100 bytes.]{#packet-analysis-compress-hundred explanation="The option is a packet count, not a file-size limit."}
::option[Stops after capturing 100 packets.]{#packet-analysis-hundred .correct explanation="The count prevents an unattended capture from growing indefinitely by packet number."}
:::

## Reading Captured Packets

Analyze the saved file without changing it:

```bash
$ tcpdump -n -tttt -r incident.pcap
```

Read timestamps, protocol, source, destination, flags, sequence or acknowledgement data, and length according to the protocol. A capture timestamp marks observation at this host, not necessarily the exact transmit time elsewhere. Clock synchronization matters when correlating captures from several systems.

:::single-choice{#packet-analysis-read-file}
Which option reads packets from a saved pcap file?

::option[`-r`]{#packet-analysis-option-read .correct explanation="The read option processes an existing capture file."}
::option[`-i`]{#packet-analysis-option-interface explanation="This selects a live capture interface."}
::option[`-w`]{#packet-analysis-option-write explanation="This writes raw packets to a file."}
:::

## Interpreting Absence and Encryption

No captured packet can mean the wrong interface or namespace, capture loss, an overly narrow filter, offload effects, routing elsewhere, or no traffic. Check tcpdump's received and dropped counters and reproduce a known event.

TLS and other encryption normally hide application payloads while leaving useful metadata such as endpoints, timing, sizes, TCP behavior, and parts of handshakes. Do not attempt unauthorized decryption or collect private keys casually.

:::single-choice{#packet-analysis-no-packets}
What does an empty filtered capture prove?

::option[The remote application has been permanently deleted.]{#packet-analysis-empty-deleted explanation="Observation point and filter errors can produce the same result."}
::option[The entire network has zero traffic.]{#packet-analysis-empty-network explanation="A narrow filter can exclude unrelated traffic."}
::option[Only that no matching packets were recorded at that capture point.]{#packet-analysis-empty-limited .correct explanation="Validate interface, namespace, filter, capture drops, and test generation before concluding."}
:::

## Protecting and Sharing Evidence

Store pcaps with restrictive permissions, record command, host, interface, timezone, filter, and incident window, and hash evidence when integrity matters. Before sharing, minimize or sanitize data with tools and procedures that preserve needed fields; packet payloads and even metadata can identify users and systems.

:::single-choice{#packet-analysis-pcap-safety}
How should an incident pcap be handled?

::option[As sensitive evidence with restricted access and documented provenance.]{#packet-analysis-sensitive-evidence .correct explanation="Captures can contain confidential content and require integrity as well as confidentiality controls."}
::option[As harmless text suitable for public upload without review.]{#packet-analysis-public explanation="Binary captures can expose payloads, identities, and infrastructure."}
::option[By editing bytes in place without preserving the original.]{#packet-analysis-edit-original explanation="That damages provenance and can invalidate later analysis."}
:::

## Summary

You can now create a useful packet capture without making it unnecessarily broad or unsafe.

1. Choose the correct interface and network namespace.
2. Bound captures by filter, packet count, and time.
3. Save raw packets and analyze the file read-only.
4. Treat absence and encrypted payloads with proper limits.
5. Protect capture confidentiality, integrity, and provenance.
