# DNS Process

## Lesson Content

Let's look at an example of how your host finds a domain (catzontheinterwebz.com) with DNS. Essentially, we funnel our way down until we reach the DNS server that knows of that domain.

**Local DNS Server**

First, our host asks, "Where is catzontheinterwebz.com?" Our local DNS server doesn't know, so it goes and starts from the top of the funnel to ask the Root Servers. Keep in mind that our host is not making these requests to find catzontheinterwebz.com directly; most users talk to a recursive DNS server provided by their ISPs, and that server is then tasked with finding the location of catzontheinterwebz.com.

**Root Servers**

There are 13 Root Servers for the Internet. They are mirrored and distributed around the world to handle DNS requests for the Internet, so there are really hundreds of servers that are working. They are controlled by different organizations and contain information about Top-Level Domains. Top-level domains are what you know as .org, .com, .net, etc., addresses. So the Root Server doesn't know where catzontheinterwebz.com is, but it tells us to ask the .com Top-Level Domain DNS Server at an IP address it gives us.

**Top-Level Domain**

So now we send another request to the name server that knows about ".com" addresses and ask if it knows where catzontheinterwebz.com is. The TLD doesn't have catzontheinterwebz.com in its zone files, but it does see a record for the name server for catzontheinterwebz.com. So it gives us the IP address of that name server and tells us to look there.

**Authoritative DNS Server**

Now we send a final request to the DNS server that actually has the record we want. The name server sees that it has a zone file for catzontheinterwebz.com, and there is a resource record for 'www' for this host. It then gives us the IP address of this host, and we can finally see some cats on the Internet.

## Exercise

No exercises for this lesson.

## Quiz Question

What is the abbreviation for the nameservers where .com, .net, .org, etc., addresses are found?

## Quiz Answer

TLD
