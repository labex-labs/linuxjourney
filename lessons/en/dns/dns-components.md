---
lesson_id: "dns-components"
course_id: "dns"
lang: "en"
order_index: 2
title: "DNS Components"
description: "Learn how recursive resolvers, authoritative servers, zones, and resource records divide DNS responsibilities."
meta_title: "DNS Components - DNS"
meta_description: "Learn about DNS components: name servers, zone files, and resource records. Understand how DNS works for beginners. Start your Linux networking journey!"
meta_keywords: "DNS components, name server, zone file, resource records, DNS tutorial, Linux networking, beginner guide"
---

DNS separates the client-facing recursion role from authoritative publication. Understanding that boundary prevents a cached answer from being mistaken for the owner of a zone.

## Stub and Recursive Resolvers

A stub resolver in an application or operating system sends queries to a configured recursive resolver. The recursive resolver returns a final answer, error, or referral outcome after using cache and, when necessary, performing iterative queries. Its reply can carry the authoritative-answer flag only when the answering server is authoritative for the data; recursion alone does not make it authoritative.

:::single-choice{#dns-components-recursive-role}
What does a recursive resolver do for a stub client?

::option[Obtains a final DNS result using cache and other name servers.]{#dns-components-recursive-result .correct explanation="The client delegates the multi-step lookup work to the recursive service."}
::option[Replaces every network router on the packet path.]{#dns-components-replaces-router explanation="Name resolution and IP forwarding are separate."}
::option[Becomes authoritative for every record it caches.]{#dns-components-cache-authority explanation="Cached data retains authority from its source; the resolver is not the zone owner."}
:::

## Authoritative Name Servers

An authoritative server answers from zone data for which it has authority. A zone should have multiple authoritative servers with synchronized data and independent failure considerations. An authoritative-only server need not perform recursion for arbitrary clients.

:::single-choice{#dns-components-authoritative-role}
What makes a server authoritative for a zone?

::option[It once queried the zone through a public resolver.]{#dns-components-once-queried explanation="Querying or caching does not confer authority."}
::option[It serves the zone data under the relevant delegation and configuration.]{#dns-components-serves-zone .correct explanation="Authority comes from the DNS delegation and the server's loaded zone, not from having a cached copy."}
::option[It responds fastest to one ping.]{#dns-components-fastest-ping explanation="ICMP timing does not define DNS authority."}
:::

## Zones and Zone Storage

A zone is an administratively served portion of the DNS namespace. It begins at a zone apex and can delegate child zones. Zone data may be stored in a text zone file, generated from a database, loaded through an API, or synthesized by software; “zone file” is not a mandatory physical implementation.

The zone apex normally has an SOA record and an NS set. Delegation data at a parent identifies child authoritative servers, sometimes accompanied by glue address records needed to reach in-bailiwick server names.

:::single-choice{#dns-components-zone-meaning}
What is a DNS zone?

::option[An administratively served portion of the namespace.]{#dns-components-admin-portion .correct explanation="It can contain records and delegations regardless of the storage backend."}
::option[A mandatory single text file on every client.]{#dns-components-client-file explanation="Authoritative implementations can use several storage forms, and clients do not hold every zone."}
::option[An Ethernet broadcast domain identified by a VLAN.]{#dns-components-vlan explanation="DNS zones and link-layer segments are independent concepts."}
:::

## Resource Record Fields

A resource record has an owner name, TTL, class, type, and type-specific RDATA. For example:

```text
www.example.com.  300  IN  A  192.0.2.25
```

The owner is `www.example.com.`, TTL is 300 seconds, class is Internet, type is IPv4 address, and RDATA is the address. Field omission and relative-name rules in zone-file syntax require careful origin handling.

:::single-choice{#dns-components-mx-type}
Which record type publishes mail-exchanger preference and hostnames?

::option[`A`]{#dns-components-a explanation="An A record stores an IPv4 address."}
::option[`NS`]{#dns-components-ns explanation="NS records identify authoritative name servers."}
::option[`MX`]{#dns-components-mx .correct explanation="MX RDATA includes preference and a mail exchanger name."}
:::

## TTL and Negative Caching

Positive records use TTLs to limit cache reuse. Negative answers such as a proven nonexistent name can also be cached according to SOA-derived rules. Lowering a TTL shortly before a planned change affects only records fetched after caches observe the lower value; previously cached longer TTLs remain until expiry.

:::single-choice{#dns-components-lower-ttl-timing}
Why lower a DNS TTL well before a planned address change?

::option[The TTL modifies the server's Ethernet MTU.]{#dns-components-ttl-mtu explanation="Caching lifetime and link packet size are unrelated."}
::option[A lower TTL guarantees the new application is healthy.]{#dns-components-ttl-health explanation="It affects caching behavior, not service correctness."}
::option[Existing caches need time to expire records learned with the old longer TTL.]{#dns-components-old-cache-expiry .correct explanation="Changing authoritative data cannot retroactively shorten an already cached record's remaining lifetime."}
:::

## Summary

You can now separate DNS recursion, authority, namespace management, and cached records.

1. Identify stub and recursive resolver roles.
2. Define authority through delegated zone service.
3. Treat a zone as namespace responsibility, not one required file.
4. Read owner, TTL, class, type, and RDATA fields.
5. Plan cache lifetimes before DNS changes.
