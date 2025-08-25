---
index: 3
lang: "en"
title: "Simple HTTP Server"
meta_title: "Simple HTTP Server - Network Sharing"
meta_description: "Learn to create a simple HTTP server using Python's http.server module. Quickly share files on your network with this beginner-friendly Linux tutorial."
meta_keywords: "http.server, SimpleHTTPServer, Python web server, file sharing, Linux tutorial, beginner guide"
---

## Lesson Content

Python has a super useful tool for serving files over HTTP. This is great if you just want to create a quick network share that other machines on your network can access. To do that, just go to the directory you want to share and run:

```bash
python -m http.server
```

Or, if you are still on Python 2:

```bash
python -m SimpleHTTPServer
```

This sets up a basic web server that you can access via the localhost address. So, grab the IP address of the machine you ran this on, and then on another machine, access it in the browser with: `http://IP_ADDRESS:8000`. On your own machine, you can view the files available by typing: `http://localhost:8000` in your web browser.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of network connectivity and IP addressing, which are essential for sharing files over a network:

1. **[Explore IP Address Types and Reachability in Linux](https://labex.io/labs/linux-explore-ip-address-types-and-reachability-in-linux-592780)** - Practice identifying different IP address types and testing network reachability, crucial for ensuring your Python HTTP server is accessible.
2. **[Identify MAC and IP Addresses in Linux](https://labex.io/labs/linux-identify-mac-and-ip-addresses-in-linux-592731)** - Learn to use the `ip a` command to find your machine's IP address, a necessary step before accessing your shared files from another device.
3. **[Manage Local Hostname Resolution in Linux](https://labex.io/labs/linux-manage-local-hostname-resolution-in-linux-592792)** - Learn to manage local hostname resolution in Linux by editing the /etc/hosts file, a key skill for web development and network testing.

These labs will help you apply the concepts in real scenarios and build confidence with basic network operations in Linux.

## Quiz Question

What tool can you use to create a simple HTTP server with Python?

## Quiz Answer

http.server
