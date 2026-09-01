---
lesson_id: "etc-hosts"
course_id: "dns"
lang: "en"
order_index: 4
title: "/etc/hosts"
description: "Learn how local hosts-file mappings participate in Linux name resolution and how to test them safely."
meta_title: "/etc/hosts - DNS"
meta_description: "Explore the purpose of the /etc/hosts file in Linux. Learn how this file maps hostnames to IP addresses, its role in local DNS resolution, and how to configure it on systems like Debian. A guide to the etc hosts linux configuration."
meta_keywords: "/etc/hosts, etc hosts linux, debian hosts, etc host linux, etc hosts, Linux networking, hostname mapping, DNS resolution"
---

`/etc/hosts` provides static address-to-name entries to the local system name-service stack. It is useful for loopback names, bootstrap dependencies, and narrowly scoped tests, but it does not publish records to other hosts or update DNS.

## Reading the File

A line begins with an IPv4 or IPv6 address followed by one or more names:

```text
127.0.0.1       localhost
192.0.2.25      app-test.example.net app-test
2001:db8::25    app-test-v6.example.net app-test-v6
```

Comments begin with `#`. The first name is conventionally treated as canonical by some tools, while later names are aliases, but application behavior and resolver APIs vary. Avoid duplicate or conflicting entries for the same name.

:::single-choice{#hosts-file-entry-order} What appears first on a normal `/etc/hosts` mapping line?

::option[An IP address.]{#hosts-file-address-first .correct explanation="One or more names follow the address on the same line."}
::option[A DNS record TTL.]{#hosts-file-ttl-first explanation="Hosts-file entries do not use DNS TTL fields."}
::option[A transport port number.]{#hosts-file-port-first explanation="The file maps names and addresses, not application ports."}
:::

## Resolver Order

The Name Service Switch configuration, commonly `/etc/nsswitch.conf`, determines how system resolver functions combine `files`, DNS, multicast systems, and other sources. A common line is:

```text
hosts: files dns
```

Do not assume files always come first without inspecting policy. Applications can also use their own DNS libraries, caches, proxies, or encrypted resolvers and may not follow the system path.

:::single-choice{#hosts-file-nss-order} What determines whether `/etc/hosts` is consulted before DNS by the system resolver?

::option[The alphabetical order of filenames in `/etc`.]{#hosts-file-alphabetical explanation="Filesystem listing order does not define name-service policy."}
::option[The order of sources in Name Service Switch policy.]{#hosts-file-nss-policy .correct explanation="The `hosts:` database line controls normal libc resolver source order."}
::option[The destination's TCP window size.]{#hosts-file-tcp-window explanation="Transport flow control is unrelated to local name lookup."}
:::

## Testing Through the System Resolver

Use `getent` to exercise the configured system name-service path:

```bash
$ getent ahosts app-test.example.net
```

`dig` queries DNS directly and normally does not report `/etc/hosts` mappings. This difference is useful: `getent` succeeding while `dig` does not can indicate a local source or resolver policy difference.

:::single-choice{#hosts-file-getent-versus-dig} Which tool is better for checking whether normal system resolution sees a hosts-file entry?

::option[`dig`, because it always reads `/etc/hosts` first.]{#hosts-file-dig-first explanation="Dig sends DNS queries and bypasses the hosts-file lookup path."}
::option[`getent ahosts`, because it uses configured name-service sources.]{#hosts-file-getent .correct explanation="It reflects the resolver path used by many native applications."}
::option[`ip route flush`, because it rebuilds all names.]{#hosts-file-flush-route explanation="Flushing routes is destructive and unrelated to hosts-file lookup."}
:::

## Editing Safely

Preserve required localhost and host-identity entries, validate the intended address, and make a recoverable change with privileged editor tooling. Avoid overriding a real public domain as a casual test; it can redirect credentials or application traffic unexpectedly. Use a dedicated test name and remove the entry after the experiment.

After editing, test the exact application because it may retain a cache or use a different resolver. Document persistent overrides so they do not silently outlive their purpose.

:::single-choice{#hosts-file-test-name} Why use a dedicated test name instead of overriding a public service name?

::option[Public names cannot contain dots.]{#hosts-file-public-no-dots explanation="Domain names commonly contain several labels separated by dots."}
::option[Dedicated names automatically create authoritative DNS zones.]{#hosts-file-auto-zone explanation="A hosts-file entry remains local and does not publish a zone."}
::option[It reduces the risk of redirecting real traffic or credentials.]{#hosts-file-reduce-redirection .correct explanation="A local override can affect any system-resolver client using that public name."}
:::

## Resolver Server Configuration

`/etc/resolv.conf` traditionally lists DNS resolver settings, but it is often generated by NetworkManager, systemd-resolved, DHCP, or another manager. Inspect symlinks and file comments, then change the owning configuration source rather than editing generated output that will be overwritten.

:::single-choice{#hosts-file-resolv-owner} What should you do before editing `/etc/resolv.conf`?

::option[Delete `/etc/hosts` and all network routes.]{#hosts-file-delete-state explanation="Those destructive changes are unrelated and can remove connectivity."}
::option[Assume every distribution stores permanent settings there directly.]{#hosts-file-assume-direct explanation="Many systems generate the file dynamically or link it to a managed stub."}
::option[Identify whether another service generates and owns it.]{#hosts-file-identify-resolver-owner .correct explanation="Persistent DNS server changes belong in the active manager's configuration."}
:::

## Summary

You can now use `/etc/hosts` as a controlled local resolver input.

1. Write address-first mappings with deliberate names and aliases.
2. Inspect Name Service Switch ordering instead of assuming it.
3. Test system resolution with `getent` and DNS separately with `dig`.
4. Use dedicated temporary names and verify the real application.
5. Change resolver servers through the configuration owner.
