---
lesson_id: "network-manager"
course_id: "network-config"
lang: "en"
order_index: 4
title: "Network Manager"
description: "Learn how NetworkManager separates devices, persistent connection profiles, and active runtime state."
meta_title: "Network Manager - Network Config"
meta_description: "Discover the role of the NetworkManager daemon in modern Linux network management. Learn how this tool automates network configuration and how to interact with it using nm-tool and the powerful nmcli command-line utility."
meta_keywords: "NetworkManager, nm-tool, nmcli, network manager linux, networkmanager linux, linux network manager, linux network management, network configuration, Linux networking"
---

NetworkManager manages network devices and activates connection profiles on many Linux desktops and servers. It is not universal, so confirm that it owns the target interface before using `nmcli` to change configuration.

## Devices and Connections

A device is a kernel interface such as `enp1s0` or `wlan0`. A connection is a stored profile containing IPv4, IPv6, DNS, Wi-Fi, routing, and other settings. One device can have several profiles, but normally only an applicable profile is active at a time.

```bash
$ nmcli device status
$ nmcli connection show
$ nmcli connection show --active
```

:::single-choice{#networkmanager-device-profile}
What is a NetworkManager connection profile?

::option[A physical connector soldered to the network card.]{#networkmanager-physical-connector explanation="That is hardware, not a NetworkManager profile."}
::option[A stored set of settings that can be activated on a device.]{#networkmanager-stored-settings .correct explanation="Profiles persist configuration separately from the kernel interface object."}
::option[A packet captured from every active flow.]{#networkmanager-packet-capture explanation="Profiles describe configuration and do not contain all traffic."}
:::

## Inspecting Effective State

Show the active profile and device details:

```bash
$ nmcli -f GENERAL,IP4,IP6 device show enp1s0
$ nmcli connection show 'Wired connection 1'
```

Profile settings, runtime DHCP results, and kernel state can differ. Compare with `ip address`, `ip route`, and the resolver. The deprecated `nm-tool` should not be the basis of a current workflow.

:::single-choice{#networkmanager-active-command}
Which command lists active NetworkManager profiles?

::option[`nmcli device delete --all`]{#networkmanager-delete-all explanation="This is not an inspection command and suggests destructive intent."}
::option[`nmcli connection show --active`]{#networkmanager-show-active .correct explanation="It filters stored connections to those currently activated."}
::option[`ip route flush table all`]{#networkmanager-flush-routes explanation="This removes routing state instead of listing profiles."}
:::

## Modifying and Activating a Profile

Modify a named profile explicitly, then activate it in a maintenance window:

```bash
$ sudo nmcli connection modify 'Wired connection 1' ipv4.method auto
$ sudo nmcli connection up 'Wired connection 1'
```

Modification changes persistent profile data; activation can replace live addresses, routes, and DNS. A remote change needs console access, saved original settings, and an independent timed rollback. Never rely on the connection being changed to carry its own recovery command.

:::single-choice{#networkmanager-modify-versus-up}
What is the difference between `connection modify` and `connection up`?

::option[Modify reboots the host; up edits DNS source code.]{#networkmanager-reboot-source explanation="Neither description matches the commands."}
::option[Modify changes profile settings; up activates a profile.]{#networkmanager-change-activate .correct explanation="Persistence and runtime activation are related but separate operations."}
::option[They are read-only aliases that can never affect connectivity.]{#networkmanager-readonly explanation="Both can be state-changing in this workflow."}
:::

## Verifying and Protecting Secrets

After activation, verify profile state, kernel addresses and routes, DNS, both address families, and the intended application. Wi-Fi, VPN, 802.1X, and mobile profiles can contain secrets. Limit profile permissions and avoid printing secret fields into shared logs or shell transcripts.

:::single-choice{#networkmanager-verification}
What proves more than NetworkManager reporting “connected”?

::option[The profile name contains the word Wired.]{#networkmanager-name-proof explanation="A label does not establish path or service health."}
::option[The terminal window remains open.]{#networkmanager-terminal-open explanation="A terminal can survive some partial network failures."}
::option[The intended DNS and application tests succeed.]{#networkmanager-end-to-end .correct explanation="Manager state must be correlated with kernel and service behavior."}
:::

## Summary

You can now manage NetworkManager profiles without confusing them with interface objects.

1. Confirm NetworkManager owns the target device.
2. Distinguish stored profiles from active runtime state.
3. Inspect devices, all profiles, and active profiles separately.
4. Modify, activate, recover, and verify as distinct steps.
