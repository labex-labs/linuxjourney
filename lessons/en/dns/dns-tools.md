---
lesson_id: "dns-tools"
course_id: "dns"
lang: "en"
order_index: 6
title: "DNS Tools"
description: "Learn how to compare system resolution and direct DNS queries with getent, resolvectl, and dig."
meta_title: "DNS Tools - DNS"
meta_description: "Explore essential Linux DNS tools like nslookup and the powerful dig command. This beginner-friendly Linux tutorial covers DNS queries and DNS troubleshooting techniques."
meta_keywords: "nslookup, dig command, DNS tools, Linux DNS, DNS troubleshooting, name server lookup, Linux tutorial, beginner Linux"
---

DNS troubleshooting starts by identifying which layer is being tested. System resolver tools include local files and policy, while `dig` and `nslookup` send DNS queries and can target a specific server directly.

## Testing the System Resolver

Use the normal host name-service path with:

```bash
$ getent ahosts www.example.com
```

On a systemd-resolved host, inspect per-link servers, search domains, and protocol state with:

```bash
$ resolvectl status
$ resolvectl query www.example.com
```

An application can still use a private resolver library or proxy, so reproduce through the application when outputs differ.

:::single-choice{#dns-tools-system-resolver}
Which command exercises the configured system name-service path?

::option[`dig @SERVER NAME` only.]{#dns-tools-dig-direct explanation="Dig sends a DNS query and does not normally read hosts-file mappings."}
::option[`ip link set down`]{#dns-tools-link-down explanation="This disrupts the interface instead of testing resolution."}
::option[`getent ahosts NAME`]{#dns-tools-getent .correct explanation="It can reflect `/etc/hosts`, DNS, and other Name Service Switch sources."}
:::

## Querying with dig

Specify a name and record type:

```bash
$ dig www.example.com A
$ dig www.example.com AAAA
$ dig example.com MX
```

The output identifies the responding server, status, flags, question, answer, authority, additional data, query time, and transport metadata. `+short` is convenient for scripts but hides evidence needed for diagnosis.

:::single-choice{#dns-tools-record-type}
Which query requests IPv6 address records?

::option[`dig NAME AAAA`]{#dns-tools-aaaa .correct explanation="AAAA records contain IPv6 addresses."}
::option[`dig NAME MX`]{#dns-tools-mx explanation="MX requests mail-exchanger records."}
::option[`dig NAME PTR` on the forward name.]{#dns-tools-ptr-forward explanation="PTR is normally queried through a reverse-lookup name."}
:::

## Selecting a Server

Target a resolver or authoritative server explicitly:

```bash
$ dig @192.0.2.53 www.example.com A
```

Compare the configured recursive resolver, a second approved resolver, and each authoritative server when isolating cache versus authority. A `NOERROR` status can contain no requested answer; `NXDOMAIN` means the queried name does not exist, while `SERVFAIL` means the server could not complete the query.

:::single-choice{#dns-tools-noerror-empty}
Can `NOERROR` have an empty answer section?

::option[Yes, when the name exists but lacks the requested record data.]{#dns-tools-noerror-nodata .correct explanation="Status and answer count must be interpreted together."}
::option[No, it guarantees at least one address record.]{#dns-tools-noerror-always-answer explanation="The name can exist without data of the requested type."}
::option[No, empty answers are always Ethernet failures.]{#dns-tools-empty-ethernet explanation="DNS semantics, not link framing, explain a valid no-data response."}
:::

## Checking Recursion and Authority

`rd` in the query requests recursion; `ra` in a response says the server offers it. `aa` means the answer is authoritative. Query an authoritative server with `+norecurse` to avoid confusing recursive cache with served zone data.

`dig +trace NAME` performs its own iterative walk starting at the root hints. It can differ from a production resolver because it bypasses that resolver's cache, forwarding, policy, DNSSEC validation, and network location.

:::single-choice{#dns-tools-aa-flag}
What does the `aa` response flag mean?

::option[The query used two identical IPv4 addresses.]{#dns-tools-two-addresses explanation="The flag is unrelated to answer count or address family."}
::option[The response was encrypted with application credentials.]{#dns-tools-aa-encrypted explanation="DNS flags do not establish encrypted transport."}
::option[The answer is authoritative.]{#dns-tools-authoritative-answer .correct explanation="The responding server claims authority for the answer data."}
:::

## Testing Reverse and TCP Queries

Use `-x` to construct a reverse PTR query:

```bash
$ dig -x 192.0.2.25
```

Test DNS over TCP when investigating truncation, zone transfers, or firewall differences:

```bash
$ dig +tcp @192.0.2.53 example.com SOA
```

Modern DNS can use UDP or TCP port 53; both should be permitted where required. A UDP answer with the truncation flag prompts compliant clients to retry through an appropriate transport.

:::single-choice{#dns-tools-tcp-test}
What does `dig +tcp` change?

::option[It sends the DNS query using TCP instead of the default UDP attempt.]{#dns-tools-use-tcp .correct explanation="This helps isolate transport filtering and responses that require a larger reliable stream."}
::option[It requests only TCP service-name records.]{#dns-tools-tcp-records explanation="The requested DNS type remains separately specified."}
::option[It permanently changes the server's resolver configuration.]{#dns-tools-tcp-persistent explanation="A query does not edit server settings."}
:::

## Summary

You can now choose a DNS tool that matches the resolver layer under investigation.

1. Use `getent` for the configured system resolver path.
2. Use `dig` with explicit record types and servers.
3. Interpret status, flags, sections, and responding server together.
4. Separate recursive cache from authoritative data.
5. Test reverse queries and both required DNS transports.
