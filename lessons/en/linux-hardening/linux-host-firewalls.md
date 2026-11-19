---
lesson_id: "linux-host-firewalls"
course_id: "linux-hardening"
lang: "en"
order_index: 5
title: "Host Firewalls"
description: "Learn to read a simple host firewall policy and plan checks from the relevant locations."
meta_title: "Host Firewalls - Linux Hardening"
meta_description: "Learn to read a simple host firewall policy and plan checks from the relevant locations."
meta_keywords: "host firewalls, linux hardening, cybersecurity, Linux Journey"
---

A **host firewall** can allow or block incoming network traffic by properties such as source address, protocol, and destination port. Start by deciding what traffic the service needs.

## Reading an Example Policy

The following simplified policy describes one host. The slash in `192.0.2.0/24` describes a range of IPv4 addresses. In this sample, `192.0.2.44` is inside that range and `198.51.100.8` is outside it.

```text
Allow TCP port 443 from any source.
Allow TCP port 22 from 192.0.2.0/24.
Deny other new inbound connections.
```

Port 443 serves the public site. Port 22 is reserved for the maintenance network. The default describes connections outside the two allowed rules.

:::single-choice{#linux-host-firewalls-match-trusted-network} Which new connection matches the maintenance rule?

::option[TCP port 22 from 198.51.100.8.]{#linux-host-firewalls-match-trusted-network-b explanation="The port matches, but this source is outside the management network."}
::option[TCP port 443 from 192.0.2.44.]{#linux-host-firewalls-match-trusted-network-c explanation="That connection matches the public web rule."}
::option[TCP port 22 from 192.0.2.44.]{#linux-host-firewalls-match-trusted-network-a .correct explanation="Both the destination port and source range match."}
:::

![Simulated host firewall policy showing public HTTPS and restricted maintenance access](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/linux-hardening/linux-host-firewalls/sample-policy.png)

## Checking Both Policy and Listener

A permitted connection can still fail if no program is listening. Likewise, a healthy listener can be unreachable through a path the firewall denies. Read the policy and verify the listener separately.

:::single-choice{#linux-host-firewalls-allowed-but-failed} The rule allows port 443, but the host has no listener there. What should you check?

::option[Whether the client should use maintenance SSH.]{#linux-host-firewalls-allowed-but-failed-a explanation="That is a different service."}
::option[Whether the public web service is listening on the expected port.]{#linux-host-firewalls-allowed-but-failed-b .correct explanation="A firewall allowance does not create a listener."}
::option[Whether the request came from the maintenance network.]{#linux-host-firewalls-allowed-but-failed-c explanation="The public rule accepts any source in this example."}
:::

## Planning a Safe Verification

When reviewing a controlled change, keep a legitimate maintenance path available. Test the allowed path from the maintenance network. Test that an approved location outside that network does not get through. Record the source, target and expected result for each test.

:::single-choice{#linux-host-firewalls-verification-pair} Which pair tests the intended SSH restriction?

::option[An approved port 22 check from inside and outside the maintenance network.]{#linux-host-firewalls-verification-pair-c .correct explanation="These requests exercise both sides of the policy."}
::option[Two SSH requests from the same allowed machine.]{#linux-host-firewalls-verification-pair-a explanation="This would check the allowed case twice."}
::option[Two browser requests to the public homepage.]{#linux-host-firewalls-verification-pair-b explanation="These exercise the public port rather than maintenance access."}
:::

## Summary

You can now reason about host firewall rules alongside service state.

1. Match a rule to the protocol, destination, and source.
2. Check that the allowed service is listening.
3. Verify both expected access and expected restriction.
