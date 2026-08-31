---
lesson_id: "nat-network-address-translation"
course_id: "subnetting"
lang: "en"
order_index: 6
title: "NAT"
description: "Learn how source, destination, and port translation modify IPv4 flows and connection state."
meta_title: "NAT - Subnetting"
meta_description: "Learn about NAT (Network Address Translation) in Linux, how it works, and its role in network security. Understand private vs. public IPs. Linux networking guide."
meta_keywords: "NAT, Network Address Translation, Linux networking, private IP, public IP, Linux tutorial, beginner guide"
---

Network Address Translation rewrites address fields, and often transport ports, as packets cross a translating device. It is widely used to connect privately addressed IPv4 networks through a smaller set of externally routable addresses.

## Source Translation

Source NAT replaces a packet's source address as it leaves a network. Many-to-one deployments also translate source ports so several internal flows can share one external address. This port-aware form is often called NAPT, PAT, or masquerading when the external address can change.

The translator tracks mappings so reply packets can be rewritten back to the original internal endpoint. It normally forwards the same transport flow; it does not have to open a separate proxy connection as an application proxy would.

:::single-choice{#nat-source-translation}
What does source NAT change on an outbound packet?

::option[Only the destination application's file permissions.]{#nat-file-permissions explanation="NAT operates on network and transport headers, not remote filesystems."}
::option[The source address and, in many-to-one use, often the source port.]{#nat-source-fields .correct explanation="The mapping lets return traffic be associated with the original internal flow."}
::option[The DNS name permanently stored by the client.]{#nat-dns-name explanation="Translation does not rewrite the client's name-service database."}
:::

## Destination Translation

Destination NAT rewrites the destination address or port, commonly to publish an internal service through an external endpoint. A port-forward rule might map an external TCP port to a different internal address and port. Return traffic needs consistent reverse translation.

:::single-choice{#nat-port-forward}
Which NAT form commonly implements an inbound port forward?

::option[Source NAT only, before route lookup.]{#nat-snat-port-forward explanation="Publishing an internal destination requires destination-field translation."}
::option[No address or port translation at all.]{#nat-no-translation explanation="A port-forward rule is a translation policy by definition."}
::option[Destination NAT.]{#nat-dnat .correct explanation="DNAT maps the external destination to the selected internal service endpoint."}
:::

## NAT and Firewall Policy

NAT is not a firewall. A stateful translator may lack a mapping for unsolicited inbound traffic, but explicit forwarding, destination translation, filtering, and application exposure determine what is reachable. Security policy should be expressed and audited with firewall rules, least-privilege services, and end-to-end controls rather than inferred from address rewriting.

:::single-choice{#nat-not-firewall}
Why should NAT not be treated as a security policy by itself?

::option[NAT automatically encrypts every payload.]{#nat-encrypts explanation="Address translation provides no payload confidentiality."}
::option[Translation rules and traffic-filtering rules have different purposes.]{#nat-filter-separate .correct explanation="Reachability and authorization require explicit filtering and service policy even when translation is present."}
::option[NAT prevents administrators from defining firewall rules.]{#nat-prevents-firewall explanation="Translation and firewall policy commonly coexist."}
:::

## Operational Consequences

NAT can exhaust address-and-port mappings, complicate peer-to-peer protocols, obscure original sources from applications, and require special handling for protocols that embed addresses. Logs must preserve translation timestamps and mapping details if flows need to be traced.

On Linux, modern policy is commonly configured with nftables and connection tracking. Inspect the actual ruleset before changing it:

```bash
$ sudo nft list ruleset
$ sudo conntrack -L
```

The second command requires conntrack tooling and privileges. Ruleset changes can disconnect remote access, so use console recovery, atomic configuration, validation, and rollback.

:::single-choice{#nat-trace-flow}
What evidence is needed to trace a shared-address flow back to an internal client?

::option[Only the external address, with no time or port.]{#nat-address-only explanation="Many clients and flows can share that address."}
::option[Only the client's displayed hostname.]{#nat-hostname-only explanation="The translator maps packet tuples, not necessarily hostnames."}
::option[Time-correlated translation mapping including protocol and ports.]{#nat-correlated-mapping .correct explanation="The complete tuple and timestamp distinguish concurrent translated flows."}
:::

## Summary

You can now distinguish address translation from routing, proxying, and firewall policy.

1. Identify source translation on outbound flows.
2. Identify destination translation in published services.
3. Understand how port mappings allow address sharing.
4. Apply explicit filtering instead of treating NAT as security.
5. Preserve mapping evidence and recovery access during changes.
