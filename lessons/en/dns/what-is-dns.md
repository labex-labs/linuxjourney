---
lesson_id: "what-is-dns"
course_id: "dns"
lang: "en"
order_index: 1
title: "What is DNS?"
description: "Learn how DNS organizes and resolves distributed names and typed resource records."
meta_title: "What is DNS? - DNS"
meta_description: "If you want to learn Linux networking, understanding DNS is crucial. This guide explains what the Domain Name System (DNS) is, how it translates domain names to IP addresses, and why it's the internet's essential address book. A perfect starting point for anyone looking to learn Linux."
meta_keywords: "DNS, Domain Name System, IP address, learn linux, linux learn, hostname, Linux networking, beginner, tutorial, guide, labex linux"
---

The Domain Name System is a distributed, hierarchical database and query protocol. It lets clients retrieve typed information associated with names, including addresses, mail routing, authoritative servers, service data, and verification records.

## Names and Resource Records

DNS does more than translate one hostname into one IP address. An `A` record holds an IPv4 address, `AAAA` an IPv6 address, `MX` mail-routing data, `NS` authoritative server names, and many other types carry different data. One name can have several records or no address record at all.

:::single-choice{#dns-purpose-beyond-address} Why is DNS more than a hostname-to-address list?

::option[It permanently assigns MAC addresses to every Ethernet frame.]{#dns-mac-frames explanation="Link-layer neighbor discovery does not use DNS this way."}
::option[It stores typed records for several kinds of service and delegation data.]{#dns-typed-records .correct explanation="Address, mail, authority, alias, and policy-related records have distinct semantics."}
::option[It guarantees that every named application is healthy.]{#dns-health-guarantee explanation="DNS data can resolve even when the destination service is unavailable."}
:::

## Hierarchical Names

A fully qualified domain name identifies a path in the DNS tree. In `www.example.com.`, the final dot represents the root, `com` is below it, `example` is below `com`, and `www` is a name within that domain. The trailing dot is often omitted in user interfaces but matters when distinguishing absolute from locally relative names in configuration.

:::single-choice{#dns-trailing-dot} What does the final dot in `www.example.com.` represent?

::option[The DNS root and an absolute name.]{#dns-root-dot .correct explanation="The dot terminates the complete path from the named node to the root."}
::option[A wildcard for every top-level domain.]{#dns-dot-wildcard explanation="A wildcard uses a label such as `*`, not the root terminator."}
::option[An instruction to use only IPv4.]{#dns-dot-ipv4 explanation="Record type controls the requested address family."}
:::

## Distributed Authority

DNS authority is delegated down the hierarchy. Root servers direct resolvers toward top-level-domain servers, which direct them toward authoritative servers for delegated zones. Organizations manage their own authoritative data without storing the entire global namespace on one central server.

:::single-choice{#dns-authoritative-data} Who provides definitive data for a delegated DNS zone?

::option[Any browser that previously visited the site.]{#dns-browser-authority explanation="A browser cache is not authoritative for the zone."}
::option[The zone's configured authoritative name servers.]{#dns-authoritative-servers .correct explanation="Delegation identifies the servers responsible for answering authoritatively."}
::option[Every router carrying a packet to the address.]{#dns-router-authority explanation="Packet forwarding and DNS authority are separate roles."}
:::

## Resolution and Caching

A host's stub resolver usually sends a query to a recursive resolver. That resolver can answer from valid cache or query the hierarchy on the client's behalf. Record TTLs limit how long cache entries can normally be reused, improving scale but delaying visibility of changes until caches refresh.

DNS success does not prove route, transport, TLS, or application health. DNS failure can also arise before any external query because `/etc/hosts`, search suffixes, local caches, or name-service policy affect the system resolver.

:::single-choice{#dns-cache-ttl-role} What does a DNS record TTL primarily control?

::option[How many routers an IP packet may cross.]{#dns-ip-hop-limit explanation="IP TTL or Hop Limit is a different protocol field."}
::option[How long the application must remain healthy.]{#dns-app-health-time explanation="DNS caching provides no service-availability guarantee."}
::option[How long a resolver may cache the record under normal rules.]{#dns-cache-lifetime .correct explanation="Shorter or longer caching affects query load and change propagation."}
:::

## Summary

You can now describe DNS as a typed, cached, hierarchical data system.

1. Distinguish DNS resource-record types by purpose.
2. Read a fully qualified name from the root downward.
3. Identify delegation and authoritative responsibility.
4. Separate name resolution from application connectivity.
