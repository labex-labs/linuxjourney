---
lesson_id: "dns-process"
course_id: "dns"
lang: "en"
order_index: 3
title: "DNS Process"
description: "Learn how a stub and recursive resolver use cache, referrals, glue, and authority to answer a DNS query."
meta_title: "DNS Process - DNS"
meta_description: "Explore the step-by-step DNS resolution process, from root servers to the authoritative DNS server. Understand how a Linux server finds a domain, a crucial concept for production environments and domain hosting."
meta_keywords: "DNS process, DNS lookup, domain resolution, linux dns, production server, domain hosting, dns server, TLD, root servers, authoritative dns"
---

A normal application asks the operating system's stub resolver, which consults local name-service policy and sends a recursive query to a configured resolver. The recursive resolver performs the hierarchy walk only when valid cache does not already answer the question.

## Starting with Local Policy and Cache

The system resolver can consult `/etc/hosts`, DNS, and other sources in the configured order. Search suffixes can transform a short name into several candidate names. A recursive resolver then checks positive and negative cache entries before sending upstream traffic.

:::single-choice{#dns-process-cache-first} Why might a recursive resolver not contact any authoritative server for a query?

::option[DNS requires every query to fail locally first.]{#dns-process-requires-failure explanation="A resolver can answer immediately from cache."}
::option[It has a still-valid cached answer.]{#dns-process-valid-cache .correct explanation="Caching avoids repeating the hierarchy walk until the record's lifetime expires."}
::option[Authoritative servers accept only Ethernet frames from clients.]{#dns-process-authoritative-ethernet explanation="DNS operates over IP transports across routed networks."}
:::

## Querying a Root Server

On a cache miss, a recursive resolver can ask a root server. The DNS root has 13 named server identities, A through M, served by many physical instances using anycast and other resilient deployment techniques. The response normally refers the resolver to authoritative servers for the relevant top-level domain rather than returning the final host address.

:::single-choice{#dns-process-root-response} What does a root server normally return for an uncached `www.example.com` lookup?

::option[A referral toward the `com` top-level-domain servers.]{#dns-process-root-referral .correct explanation="The hierarchy delegates responsibility rather than storing every final host record at the root."}
::option[The web page hosted at `www.example.com`.]{#dns-process-root-webpage explanation="DNS returns resource-record data, not application content."}
::option[The destination's Ethernet MAC address.]{#dns-process-root-mac explanation="MAC addresses are resolved on local links, not through the DNS hierarchy."}
:::

## Following TLD and Authoritative Referrals

The resolver asks a `com` authoritative server, which returns the delegated authoritative name servers for `example.com`. The referral can include glue address records when needed to reach a server whose name lies inside the delegated child. The resolver then queries an authoritative server for the requested record.

:::single-choice{#dns-process-glue-purpose} What problem does DNS glue help solve?

::option[Encrypting HTTP payloads after DNS resolution.]{#dns-process-glue-http explanation="TLS or other application security handles payload encryption."}
::option[Choosing the fastest Ethernet switch port.]{#dns-process-glue-switch explanation="Glue is delegation address data, not link forwarding policy."}
::option[Reaching an in-bailiwick server without circular resolution.]{#dns-process-glue-reachability .correct explanation="The parent supplies address data needed to contact a server named inside the child zone."}
:::

## Following Aliases and Record Types

An answer can contain a CNAME alias requiring another name lookup, or application-specific records that lead to more queries. Asking for `A` returns only IPv4-address records and related chain data; a separate `AAAA` query retrieves IPv6 addresses. The final response carries a status such as `NOERROR`, `NXDOMAIN`, or `SERVFAIL`, each with different meaning.

:::single-choice{#dns-process-nxdomain-meaning} What does `NXDOMAIN` report?

::option[The queried domain name does not exist according to an authoritative result.]{#dns-process-name-does-not-exist .correct explanation="This differs from an existing name that simply lacks the requested record type."}
::option[The name exists and always has an empty A record.]{#dns-process-empty-a explanation="An existing name with no requested data normally produces a no-data response, not NXDOMAIN."}
::option[The resolver reached its maximum Ethernet frame size.]{#dns-process-frame-size explanation="The status concerns name existence."}
:::

## Validation, Caching, and Application Use

A validating recursive resolver can use DNSSEC signatures and the chain of trust to verify authenticated denial or record integrity. DNSSEC does not encrypt queries or prove that the application at the returned address is trustworthy.

The resolver caches results within TTL rules and returns them to the stub. The application then chooses an address and attempts its own network and security protocols.

:::single-choice{#dns-process-dnssec-limit} What does DNSSEC validation not provide?

::option[Integrity and origin authentication for signed DNS data.]{#dns-process-dnssec-does-integrity explanation="Those are core DNSSEC goals."}
::option[Authenticated denial for signed nonexistent data.]{#dns-process-authenticated-denial explanation="Signed denial mechanisms can provide that validation."}
::option[Confidentiality for the DNS query and response.]{#dns-process-no-confidentiality .correct explanation="Encryption requires a separate protected DNS transport such as DoT or DoH."}
:::

## Summary

You can now trace a recursive DNS lookup from local policy to a cached final response.

1. Check local sources and resolver cache first.
2. Follow root and top-level-domain referrals.
3. Use glue to reach appropriate delegated servers.
4. Distinguish aliases, no-data answers, and nonexistent names.
5. Separate DNSSEC integrity from transport confidentiality.
