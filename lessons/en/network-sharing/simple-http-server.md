---
index: 3
lang: "en"
title: "Simple HTTP Server"
meta_title: "Simple HTTP Server - Network Sharing"
meta_description: "Learn how to quickly set up a simple HTTP server in Linux using Python's http.server module. This guide explains how to create a simple Linux web server for easy file sharing across your network."
meta_keywords: "linux simple http server, simple http server linux, simple linux web server, python http.server, what is python simplehttpserver, file sharing, network server"
---

## Lesson Content

Python includes a built-in module that allows you to instantly create a web server, which is incredibly useful for sharing files over a network. Setting up a **linux simple http server** is a straightforward process that requires just a single command.

### Starting a Simple HTTP Server in Linux

To get started, navigate to the directory you wish to share using your terminal. Once you are in the desired directory, you can start a **simple http server linux** environment with the following command if you are using Python 3:

```bash
python -m http.server
```

This command launches a basic web server, making the contents of your current directory accessible over HTTP.

### Legacy Method for Python 2

For older systems that still use Python 2, the command is slightly different. The module was previously named `SimpleHTTPServer`. If you've ever wondered **what is python simplehttpserver**, it is simply the Python 2 equivalent of the `http.server` module. You can run it with:

```bash
python -m SimpleHTTPServer
```

### Accessing Your Simple Linux Web Server

After running the command, your **simple linux web server** will be active. You can access the shared files from another machine on the same network by opening a web browser and navigating to `http://IP_ADDRESS:8000`, replacing `IP_ADDRESS` with the local IP of the machine running the server.

To view the files on the same machine, you can use the localhost address: `http://localhost:8000`.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of network connectivity and IP addressing, which are essential for sharing files over a network:

1. **[Explore IP Address Types and Reachability in Linux](https://labex.io/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Practice identifying different IP address types and testing network reachability, crucial for ensuring your Python HTTP server is accessible.
2. **[Identify MAC and IP Addresses in Linux](https://labex.io/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - Learn to use the `ip a` command to find your machine's IP address, a necessary step before accessing your shared files from another device.
3. **[Manage Local Hostname Resolution in Linux](https://labex.io/labs/comptia-manage-local-hostname-resolution-in-linux-592792)** - Learn to manage local hostname resolution in Linux by editing the /etc/hosts file, a key skill for web development and network testing.

These labs will help you apply the concepts in real scenarios and build confidence with basic network operations in Linux.

## Quiz Question

For Python 3, what is the name of the module used to create a simple HTTP server? (Please answer in English, paying attention to case sensitivity).

## Quiz Answer

http.server
