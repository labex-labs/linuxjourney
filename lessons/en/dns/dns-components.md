---
index: 2
lang: "en"
title: "DNS Components"
meta_title: "DNS Components - DNS"
meta_description: "Learn about DNS components: name servers, zone files, and resource records. Understand how DNS works for beginners. Start your Linux networking journey!"
meta_keywords: "DNS components, name server, zone file, resource records, DNS tutorial, Linux networking, beginner guide"
---

## Lesson Content

The DNS database of the Internet relies on sites and organizations providing part of that database. To do that, they need:

### Name Server

We set up DNS via "name servers." Name servers load our DNS settings and configurations and answer any questions from clients or other servers that want to know things like "Who is google.com?". If the name server doesn't know the answer to that query, it will redirect the request to other name servers. Name servers can be "authoritative," meaning they hold the actual DNS records you're looking for, or "recursive," meaning they would ask other servers, and those servers would ask other servers until they found an authoritative server that contained the DNS records. Recursive servers can also have the information we want cached instead of reaching an authoritative server.

### Zone File

Inside a name server lives something called zone files. Zone files are how the name server stores information about the domain or how to get to the domain if it doesn't know.

### Resource Records

A zone file is comprised of entries of resource records. Each line is a record and contains information about hosts, name servers, other resources, etc. The fields consist of the following:

- Record name
- TTL - The time after which we discard the record and obtain a new one. In DNS, TTL is denoted by time, so records could have a TTL of one hour. The reason we do this is because the Internet is constantly changing; one minute a host can be mapped to X IP address, then next it can be at Y IP address.
- Class - Namespace of the record information. Most commonly, IN is used for Internet.
- Type - Type of information stored in the record data. We won't get into record types, but you've probably seen common ones like A for address, MX for mail exchanger, etc.
- Data - This field can contain an IP address if it's an A record or something else depending on the record type.

```plaintext
patty    IN  A      192.168.0.4
```

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of DNS and hostname resolution:

1. **[Set Up a Local Authoritative DNS Server on Linux](https://labex.io/labs/linux-set-up-a-local-authoritative-dns-server-on-linux-592803)** - Practice installing and configuring a local DNS server (`bind9`), defining zones, and validating your setup.
2. **[Query DNS Records in Linux with dig and nslookup](https://labex.io/labs/linux-query-dns-records-in-linux-with-dig-and-nslookup-592796)** - Learn to use essential command-line tools (`dig`, `nslookup`) to query various DNS record types and troubleshoot DNS issues.
3. **[Manage Local Hostname Resolution in Linux](https://labex.io/labs/linux-manage-local-hostname-resolution-in-linux-592792)** - Understand how to manage local hostname resolution by editing the `/etc/hosts` file, a key skill for development and testing.

These labs will help you apply the concepts of DNS and hostname resolution in real scenarios and build confidence with network services.

## Quiz Question

What resource record type is used for mail exchangers?

## Quiz Answer

MX
