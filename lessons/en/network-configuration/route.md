---
lang: "en"
title: "route"
meta_title: "route - Network Config"
meta_description: "Learn how to add and delete network routes using the Linux route and ip commands. Understand routing table management for beginners and intermediate users."
meta_keywords: "route command, ip route, add route, delete route, Linux networking, routing table, Linux tutorial, beginner guide"
---

## Lesson Content

We've already discussed viewing our routing tables with the `route` command. If you want to add or remove routes, you can do so manually.

### Add a new route

```bash
sudo route add -net 192.168.2.1/23 gw 10.11.12.3
```

### Delete a route

```bash
sudo route del -net 192.168.2.1/23
```

You can also perform these changes with the **ip** command:

### To add a route

```bash
ip route add 192.168.2.1/23 via 10.11.12.3
```

### To delete a route

```bash
$ ip route delete 192.168.2.1/23 via 10.11.12.3
or
$ ip route delete 192.168.2.1/23
```

## Exercise

There are no exercises for this lesson, but you can read more information on commands discussed here in the man pages.

```bash
man route
```

```bash
man ip-route
```

## Quiz Question

What is the command flag to delete a route?

## Quiz Answer

del
