---
lesson_id: "dns-setup"
course_id: "dns"
lang: "en"
order_index: 5
title: "DNS Setup"
description: "Learn how to choose, secure, validate, and operate authoritative or recursive DNS services."
meta_title: "DNS Setup - DNS"
meta_description: "Learn about popular DNS servers for Linux like BIND, DNSmasq, and PowerDNS. Discover the best DNS server for your network setup with this beginner-friendly guide."
meta_keywords: "Linux DNS, BIND, DNSmasq, PowerDNS, DNS server setup, Linux networking, DNS tutorial, beginner"
---

DNS software should be selected by role and operational requirements, not by a universal “best server.” An authoritative service publishes zones; a recursive service answers clients by resolving and caching; a forwarding resolver sends queries to another resolver. Combining roles changes the attack surface.

## Choosing a Role and Implementation

- BIND can provide authoritative and recursive service with extensive standards support.
- Unbound is commonly deployed as a validating recursive resolver.
- dnsmasq provides lightweight forwarding, caching, and DHCP features for smaller controlled networks.
- PowerDNS offers separate authoritative and recursive products with several data backends.

Capabilities and packaging change, so consult the installed version's official documentation. Deploy only the role needed and disable unintended recursion or zone service.

:::single-choice{#dns-setup-authoritative-role}
Which role publishes definitive records for zones it serves?

::option[Authoritative DNS server.]{#dns-setup-authoritative .correct explanation="It answers from configured zone authority rather than recursively finding arbitrary names."}
::option[Ethernet switch.]{#dns-setup-switch explanation="A switch forwards link-layer frames and does not publish DNS zones."}
::option[A recursive resolver answering arbitrary client queries.]{#dns-setup-stub explanation="A stub sends queries to a recursive service and does not host authoritative zones."}
:::

## Designing Before Installing

Define zones, clients, query volume, update mechanism, DNSSEC needs, logging, monitoring, backups, and recovery. Authoritative zones need redundant servers and correctly registered delegations. Recursive service needs explicit client access control, cache policy, upstream or iterative reachability, and protection against abuse.

Never expose unrestricted recursion to the Internet. Open resolvers can be abused for reflection attacks and consume local resources.

:::single-choice{#dns-setup-open-recursion}
Why restrict recursive queries to authorized clients?

::option[Recursive DNS cannot cache any record.]{#dns-setup-no-cache explanation="Caching is a core recursive-resolver function."}
::option[Authoritative delegations require every user to be root.]{#dns-setup-all-root explanation="DNS delegation does not grant operating-system privilege."}
::option[Open recursion can be abused for amplification and resource consumption.]{#dns-setup-recursion-abuse .correct explanation="Access controls reduce use of the resolver as public attack infrastructure."}
:::

## Validating Configuration and Zone Data

Use the implementation's syntax and zone-checking tools before reload. For BIND, common examples are:

```bash
$ named-checkconf
$ named-checkzone example.com /etc/bind/zones/db.example.com
```

Run with appropriate permissions and paths for the host. A parser success does not prove delegation, serial propagation, DNSSEC chain, firewall reachability, or correct answers, so follow with controlled queries.

:::single-choice{#dns-setup-zone-validation-limit}
What does a successful zone syntax check fail to prove?

::option[That delegation and end-to-end authoritative answers work.]{#dns-setup-not-end-to-end .correct explanation="Parent data, service activation, network policy, and runtime loading remain separate."}
::option[That the zone text can be parsed by the checker.]{#dns-setup-parser-proves explanation="That is the checker's direct evidence."}
::option[That the file has a record owner field.]{#dns-setup-record-owner explanation="Parsing valid records already checks structural aspects."}
:::

## Applying and Testing Safely

Preserve current configuration and recovery access, validate, then reload rather than restart when supported. Query each authoritative server directly with recursion disabled and compare SOA serial, NS set, positive records, nonexistent names, and both UDP and TCP behavior:

```bash
$ dig @192.0.2.53 example.com SOA +norecurse
$ dig @192.0.2.53 missing.example.com A +norecurse
$ dig @192.0.2.53 example.com SOA +norecurse +tcp
```

For recursion, test allowed and denied client networks, DNSSEC validation, cache behavior, and failure of upstream dependencies.

:::single-choice{#dns-setup-norecurse-test}
Why query an authoritative server with `+norecurse`?

::option[Test authoritative answers without asking for recursion.]{#dns-setup-authority-only .correct explanation="This separates zone service from any recursive behavior."}
::option[To remove every record from its zone.]{#dns-setup-remove-records explanation="A query does not edit authoritative data."}
::option[To force all responses through HTTP.]{#dns-setup-force-http explanation="The option controls the DNS recursion-desired flag."}
:::

## Operating the Service

Monitor query failures, latency, cache behavior, resource use, zone transfers, serial consistency, DNSSEC expiry, and delegation health. Back up source configuration and signing material securely, but verify that a fresh instance can load zones and serve correct answers. Patch supported versions and limit control interfaces, dynamic updates, and transfer access.

:::single-choice{#dns-setup-redundancy-verification}
What should authoritative DNS redundancy testing include?

::option[Querying each server and testing operation when another is unavailable.]{#dns-setup-test-each-server .correct explanation="Listing several NS records is not proof that each independent service is reachable and current."}
::option[Checking only that all servers have similar hostnames.]{#dns-setup-hostname-similarity explanation="Names do not prove data synchronization or availability."}
::option[Using one shared process and disk for every advertised server.]{#dns-setup-shared-failure explanation="A shared failure domain weakens redundancy."}
:::

## Summary

You can now design a DNS deployment around explicit authority or recursion roles.

1. Choose software only after defining the required role.
2. Restrict recursion and administrative interfaces.
3. Validate configuration and zones before reload.
4. Test authority, denial, transport, and client policy directly.
5. Monitor redundancy, DNSSEC, data consistency, and recovery.
