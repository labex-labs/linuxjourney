---
lesson_id: "linux-listening-services"
course_id: "linux-hardening"
lang: "en"
order_index: 4
title: "Listening Services"
description: "Learn to read a Linux listening address and decide where to test its reachability."
meta_title: "Listening Services - Linux Hardening"
meta_description: "Learn to read a Linux listening address and decide where to test its reachability."
meta_keywords: "listening services, linux hardening, cybersecurity, Linux Journey"
---

A service can wait for connections at a particular address and port. A **listener** is a socket ready to receive incoming connections. Its address is one clue about who may be able to reach it.

## Listing TCP Listeners

Run this read-only command on a Linux practice host. The options ask `ss` to show listening TCP sockets with numeric addresses and ports.

```bash
$ ss -lnt
```

Read the local address column. The example below uses `127.0.0.1:8091` for a web preview. The port is 8091. The address is **loopback**, which refers to the host itself.

:::single-choice{#linux-listening-services-local-listener} A browser on the same host needs the preview in this example. Which address should it try?

::option[0.0.0.0:8091.]{#linux-listening-services-local-listener-a explanation="That notation describes a listening choice rather than the local destination shown here."}
::option[127.0.0.1:8091.]{#linux-listening-services-local-listener-b .correct explanation="The service is listening on that loopback address and port."}
::option[Port 80 on an unrelated server.]{#linux-listening-services-local-listener-c explanation="The sample listener uses port 8091 on its own host."}
:::

![Recorded LabEx ss output for the practice listener on loopback port 8091](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/linux-hardening/linux-listening-services/loopback-listener.png)

## Interpreting All Interfaces

An IPv4 local address of `0.0.0.0:8091` means that the service listens on all IPv4 interfaces on the host. That can include an interface reached from another computer. The listener listing describes what the process accepts locally. Firewall rules and routes can limit what another computer can reach.

:::single-choice{#linux-listening-services-all-interfaces} A service changes from 127.0.0.1 to 0.0.0.0 on the same port. What changed?

::option[It can listen on more IPv4 interfaces.]{#linux-listening-services-all-interfaces-a .correct explanation="The setting broadens the local addresses on which incoming connections can be accepted."}
::option[It now listens on a different port.]{#linux-listening-services-all-interfaces-b explanation="The port number stayed the same."}
::option[It guarantees immediate access from every network.]{#linux-listening-services-all-interfaces-c explanation="Network rules and routes still determine which paths can reach it."}
:::

## Checking the Intended Path

An internal staff service might be intended for one network. Verify it from that network and check an approved test location outside it if you need evidence the restriction works. Confirm both the listener and the path. A local listing alone cannot tell you what a distant client experienced.

:::single-choice{#linux-listening-services-verify-from-client} You see a listener on all local interfaces. Which check shows whether a staff workstation can reach it?

::option[Read the hostname a second time.]{#linux-listening-services-verify-from-client-a explanation="The hostname does not test the network path."}
::option[Count how many listeners are present.]{#linux-listening-services-verify-from-client-b explanation="Counts do not show access from the workstation."}
::option[Make an approved request from the staff network.]{#linux-listening-services-verify-from-client-c .correct explanation="This tests the intended path."}
:::

To check which services listen on a Linux host, start with Audit Listening Services in [Linux Security for DevSecOps](https://labex.io/courses/linux-security-for-devsecops).

## Summary

You can now read a listening address before deciding where to test access.

1. List local TCP listeners safely.
2. Distinguish loopback from all IPv4 interfaces.
3. Verify the connection from the relevant client location.
