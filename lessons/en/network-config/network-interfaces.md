---
lesson_id: "network-interfaces"
course_id: "network-config"
lang: "en"
order_index: 1
title: "Network Interfaces"
description: "Learn how to inspect Linux interface state, addresses, statistics, and persistent configuration ownership."
meta_title: "Network Interfaces - Network Config"
meta_description: "A comprehensive guide to the Linux network interface. Learn to use ifconfig and the modern ip command, and understand configuration files like /etc/network/interfaces, especially on Debian systems."
meta_keywords: "linux interface, linux network interface, etc network interfaces, debian network interfaces, ifconfig, ip command, network configuration, linux networking"
---

A Linux network interface connects a network namespace to a physical device, loopback path, bridge, tunnel, virtual device, or other link. Interface state, addresses, routes, DNS, and persistent configuration are related but distinct.

## Discovering Interfaces

Use the modern iproute2 tools:

```bash
$ ip -brief link show
$ ip -brief address show
```

Interface names can be predictable hardware-derived names such as `enp1s0`, traditional names such as `eth0`, or administrator-defined names. Never assume `eth0` exists or identifies a particular adapter.

:::single-choice{#interfaces-name-assumption} Why should a script discover rather than assume `eth0`?

::option[Every interface is required to be named `lo`.]{#interfaces-all-loopback explanation="Loopback is one special interface, not the name of every link."}
::option[Linux systems can use several interface naming schemes.]{#interfaces-naming-varies .correct explanation="Hardware-derived, virtual, and custom names make a fixed `eth0` assumption unreliable."}
::option[Interface names are always remote passwords.]{#interfaces-name-password explanation="Names identify kernel devices and are not credentials."}
:::

## Administrative and Operational State

`UP` means the interface is administratively enabled. `LOWER_UP` commonly indicates that the lower layer reports operational readiness, such as Ethernet carrier. Either flag alone does not prove an IP address, route, DNS, firewall, or application path works.

```bash
$ ip -details link show dev enp1s0
$ ip -s link show dev enp1s0
```

The statistics view can reveal errors, drops, and counters, but counters need a time interval and baseline to become meaningful.

:::single-choice{#interfaces-up-limit} What does administrative `UP` fail to prove?

::option[That end-to-end connectivity works.]{#interfaces-up-not-connectivity .correct explanation="Lower-layer, addressing, routing, filtering, naming, and service failures can remain."}
::option[That the administrator enabled the interface.]{#interfaces-up-does-prove explanation="That is the direct meaning of the state."}
::option[That the interface has a kernel object.]{#interfaces-up-kernel-object explanation="The displayed state belongs to an existing kernel interface."}
:::

## Changing Runtime State

Runtime commands include:

```bash
$ sudo ip link set dev enp1s0 up
$ sudo ip address add 192.0.2.10/24 dev enp1s0
```

These changes affect current kernel state and can conflict with a network manager that later reapplies its profile. Bringing down a remote-management interface can immediately end access. Before changing it, verify the exact device, preserve console access, record current state, and prepare a timed or tested rollback.

:::single-choice{#interfaces-ip-address-add-persistence} Does `ip address add` by itself guarantee persistence after reboot?

::option[No; the active configuration system must also store the setting.]{#interfaces-manager-persistence .correct explanation="NetworkManager, systemd-networkd, ifupdown, or another owner applies persistent policy."}
::option[Yes, because every kernel change edits all manager profiles.]{#interfaces-runtime-always-persistent explanation="Kernel runtime changes do not universally update persistent configuration."}
::option[Only when the address is private IPv4.]{#interfaces-private-persistent explanation="Address scope does not make a runtime command persistent."}
:::

## Identifying Configuration Ownership

Persistent paths differ across distributions and installations. Possibilities include NetworkManager profiles, systemd-networkd units, netplan input, `/etc/network/interfaces`, cloud-init, or orchestration. Determine which service manages the device before editing files:

```bash
$ systemctl --type=service --state=running | grep -E 'NetworkManager|networkd|networking'
$ networkctl status
$ nmcli device status
```

Use only commands present for the identified manager. Two managers controlling the same link can race and overwrite each other's state.

:::single-choice{#interfaces-config-owner} What should precede a persistent interface change?

::option[Edit every possible network configuration file.]{#interfaces-edit-all explanation="Competing definitions create conflicts and unpredictable reapplication."}
::option[Identify which network manager owns the interface.]{#interfaces-identify-owner .correct explanation="The correct configuration source and apply method depend on that ownership."}
::option[Delete all current routes before inspection.]{#interfaces-delete-routes explanation="That is destructive and can remove recovery access."}
:::

## Verifying a Change

Verify link state, assigned addresses and lifetimes, selected routes, resolver state, neighbor reachability, and the actual application. For a persistent change, test a controlled service restart or reboot only when a recovery path exists.

:::single-choice{#interfaces-change-verification} What provides better evidence than seeing the new address in `ip address`?

::option[The interface name contains a digit.]{#interfaces-digit explanation="Naming provides no end-to-end validation."}
::option[The shell prompt still has the same color.]{#interfaces-prompt-color explanation="Terminal appearance is unrelated to network operation."}
::option[Routes, resolver state, and the intended application also work.]{#interfaces-end-to-end .correct explanation="A usable configuration depends on the complete path and service behavior."}
:::

## Summary

You can now inspect and change an interface without confusing runtime state with persistent policy.

1. Discover real interface names and addresses.
2. Separate administrative state from operational connectivity.
3. Treat direct `ip` changes as current kernel state.
4. Identify the active configuration owner before persistence changes.
5. Verify routing, resolution, and application behavior afterward.
