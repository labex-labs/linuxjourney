---
lesson_id: "netstat"
course_id: "troubleshooting"
lang: "en"
order_index: 4
title: "netstat"
description: "Learn how to inspect Linux sockets, listeners, queues, and TCP states with ss."
meta_title: "netstat - Troubleshooting"
meta_description: "Master the linux netstat command to analyze network connections, ports, and sockets. This guide covers common states like SYN_SENT and netstat close_wait for effective troubleshooting."
meta_keywords: "linux netstat, netstat, netstat command, syn_sent netstat, netstat close_wait, network connections, linux networking, network analysis, linux tutorial"
---

The legacy `netstat` tool displays sockets, routes, and interface statistics. On modern Linux, `ss` is the preferred socket-inspection tool because it exposes kernel socket state efficiently and is maintained with iproute2.

## Listing Listening Sockets

Show listening TCP and UDP sockets numerically, including owning processes when permitted:

```bash
$ sudo ss -lntup
```

`-l` selects listeners, `-n` avoids name lookup, `-t` and `-u` select TCP and UDP, and `-p` requests process data. UDP is connectionless, so its unconnected bound sockets do not have TCP-style `LISTEN` handshakes.

:::single-choice{#netstat-ss-numeric} Why use `-n` during socket troubleshooting?

::option[It creates a new network namespace.]{#netstat-new-namespace explanation="The option controls name resolution in output."}
::option[It prevents address and port name lookups.]{#netstat-numeric-output .correct explanation="Numeric output avoids confusing a service-name mapping with observed protocol identity."}
::option[It closes every non-listening socket.]{#netstat-close-sockets explanation="Inspection does not terminate sockets."}
:::

## Ports, Endpoints, and Services

A local socket endpoint combines an address, transport protocol, and port. A TCP connection is distinguished by protocol plus source and destination addresses and ports. `/etc/services` maps conventional names to numbers, but it does not prove which process currently owns a port or which application protocol it speaks.

:::single-choice{#netstat-services-file-limit} What does an `/etc/services` entry such as `https 443/tcp` establish?

::option[That a healthy HTTPS server is currently listening.]{#netstat-healthy-listener explanation="A static name database does not prove runtime state."}
::option[The conventional service-name mapping for that port.]{#netstat-conventional-name .correct explanation="Socket ownership and actual protocol behavior require runtime inspection and testing."}
::option[That all port 443 traffic is encrypted correctly.]{#netstat-all-encrypted explanation="A port number cannot validate TLS behavior."}
:::

## Reading TCP States

Common states include:

- `SYN-SENT`: the local endpoint sent a connection request and awaits progress.
- `ESTAB`: the TCP connection is established.
- `CLOSE-WAIT`: the peer closed its sending side, but the local application has not closed its socket.
- `TIME-WAIT`: the endpoint that actively closed waits so delayed segments expire and the final exchange can be handled safely.

Large or growing `CLOSE-WAIT` populations often point to local application cleanup behavior. `TIME-WAIT` is a normal protocol state; quantity and resource impact determine whether it is operationally concerning.

:::single-choice{#netstat-close-wait-owner} Which side still needs to close a socket in `CLOSE-WAIT`?

::option[Every router on the Internet.]{#netstat-all-routers-close explanation="Routers do not own the endpoint socket."}
::option[The DNS authoritative server.]{#netstat-dns-close explanation="Name service is unrelated to local TCP close handling."}
::option[The local application.]{#netstat-local-close .correct explanation="TCP has received the peer's FIN and waits for the local process to close its side."}
:::

## Interpreting Queues

`Recv-Q` and `Send-Q` meanings depend on state and protocol. On established TCP sockets they can indicate data queued for application receipt or transmission acknowledgement. On listening sockets, queue fields describe connection backlog state rather than application payload bytes in the same way.

One snapshot cannot establish a leak or bottleneck. Sample over time and correlate with process behavior, application latency, retransmissions, and resource limits.

:::single-choice{#netstat-queue-snapshot} Why is one large socket queue snapshot insufficient for diagnosis?

::option[Linux never stores data in socket queues.]{#netstat-no-queues explanation="Kernel networking relies on send and receive queues."}
::option[Every queue value is a filesystem permission.]{#netstat-queue-permission explanation="The fields describe networking state."}
::option[Queue impact needs state, trends, and workload context.]{#netstat-queue-context .correct explanation="A transient burst differs from a sustained application or network bottleneck."}
:::

## Filtering an Investigation

Limit output to the protocol, state, endpoint, or process in question:

```bash
$ ss -tn state established
$ ss -ltn 'sport = :443'
```

A listener proves local transport readiness, not remote reachability or application health. Follow with route, firewall, packet, TLS, and application tests appropriate to the symptom.

:::single-choice{#netstat-listener-limit} What does a TCP listener on port 443 fail to prove?

::option[That a local socket accepted a bind and listen operation.]{#netstat-listen-local explanation="That is precisely the local state shown."}
::option[That remote clients can complete a valid HTTPS request.]{#netstat-not-remote-proof .correct explanation="Path policy, TLS, and application behavior remain untested."}
::option[That TCP has a numeric port field.]{#netstat-port-field explanation="The listener output directly includes one."}
:::

## Summary

You can now use `ss` to inspect socket state without confusing ports with applications.

1. List listeners numerically with process context.
2. Distinguish conventional service names from runtime ownership.
3. Interpret TCP close states from the local endpoint's perspective.
4. Sample queues over time with workload context.
5. Verify remote application behavior beyond a local listener.
