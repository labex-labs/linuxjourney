---
lesson_id: "dhclient"
course_id: "network-config"
lang: "en"
order_index: 3
title: "dhclient"
description: "Learn when and how to use dhclient without conflicting with the system's network manager."
meta_title: "dhclient - Network Config"
meta_description: "Learn about dhclient, how it obtains IP addresses using DHCP, and manages network leases. Understand dhclient.conf and dhclient.leases files. Linux beginner guide."
meta_keywords: "dhclient, DHCP, Linux networking, IP address, network configuration, Linux tutorial, beginner guide"
---

`dhclient` is an ISC DHCP client found on some Linux systems. Many current installations instead let NetworkManager, systemd-networkd, or another service run its own DHCP client. Starting a second client on a managed interface can create competing addresses, routes, DNS settings, and lease state.

## Identifying the Active Client

Before invoking `dhclient`, inspect the configuration owner and processes:

```bash
$ nmcli device status
$ networkctl status
$ ps -ef | grep '[d]hclient'
```

Use the tools that exist on the host. If a manager owns the interface, request DHCP through that manager rather than launching a separate client.

:::single-choice{#dhclient-second-client-risk} Why avoid starting `dhclient` on an already managed interface?

::option[DHCP can assign only loopback addresses.]{#dhclient-loopback-only explanation="DHCP commonly assigns non-loopback network configuration."}
::option[Two clients can compete over addresses, routes, DNS, and leases.]{#dhclient-competing-state .correct explanation="Only the identified configuration owner should normally reconcile the interface."}
::option[Every DHCP request reformats the local disk.]{#dhclient-reformats explanation="The protocol changes network state, not disk format."}
:::

## Requesting a Lease Explicitly

On an unmanaged test interface where `dhclient` is the intended owner, specify the interface and use verbose output:

```bash
$ sudo dhclient -v enp1s0
```

Running without an interface can act on multiple eligible interfaces. Configuration and lease paths vary by package and invocation; common names include `dhclient.conf` and `dhclient.leases`, but do not assume one fixed location.

:::single-choice{#dhclient-interface-operand} Why specify `enp1s0` in a manual request?

::option[To target only the intended network interface.]{#dhclient-scope-interface .correct explanation="An unqualified client invocation can consider more interfaces than intended."}
::option[To select TCP port 1 for DHCP.]{#dhclient-tcp-port explanation="DHCP uses UDP and the interface name is not a port."}
::option[To make the lease permanent.]{#dhclient-permanent explanation="DHCP configuration remains time-limited lease state."}
:::

## Releasing a Lease

`dhclient -r INTERFACE` requests release and can remove usable configuration. It is disruptive and does not guarantee the server is reachable to receive the release. Do not release a lease merely to inspect it, especially on a remote-management path.

:::single-choice{#dhclient-release-effect} What is the operational risk of `dhclient -r enp1s0`?

::option[It only prints the current lease without changes.]{#dhclient-release-readonly explanation="Release is a state-changing action."}
::option[It renews every lease for an unlimited period.]{#dhclient-release-renews explanation="Releasing and renewing are opposite operations."}
::option[It can remove current DHCP connectivity.]{#dhclient-release-connectivity .correct explanation="The release workflow relinquishes lease state and can terminate remote access."}
:::

## Verifying the Applied Lease

After a controlled request, verify more than the address:

```bash
$ ip address show dev enp1s0
$ ip route show
$ resolvectl status
```

Inspect the manager or client logs and lease lifetime, then test the intended name resolution and application. A DHCPACK can carry incorrect options, and successfully assigning an address does not prove gateway or DNS reachability.

:::single-choice{#dhclient-verify-state} What should be verified after obtaining a lease?

::option[Address, routes, DNS, lease, and application behavior.]{#dhclient-complete-verify .correct explanation="The lease configures several related components that must work together."}
::option[Only that an address string appears.]{#dhclient-address-only explanation="Routes, DNS, lifetime, and end-to-end function can still be wrong."}
::option[Only the desktop background.]{#dhclient-wallpaper explanation="Desktop appearance is unrelated to DHCP state."}
:::

## Summary

You can now use `dhclient` only when it is the intended owner of an interface.

1. Discover the active network manager and DHCP client.
2. Avoid competing clients on one interface.
3. Scope a manual request to a named test interface.
4. Treat release as disruptive and verify the complete lease result.
