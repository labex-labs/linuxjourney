# Packet Analysis

## Lesson Content

The subject of packet analysis could fill an entire course of its own and there are many books written just on packet analysis. However, today we will just learn the basics. There are two extremely popular packet analyzers, Wireshark and tcpdump. These tools scan your network interfaces, capture the packet activity, parse the packages and output the information for us to see. They allows us to get into the nitty gritty of network analysis and get into the low level stuff. We'll be using tcpdump since it has a simpler interface, however if you were to pick up packet analysis for your toolbelt, I would recommend looking into Wireshark.

<b>Install tcpdump</b>

<pre>
$ sudo apt install tcpdump
</pre>

<b>Capture packet data on an interface</b>

<pre>
pete@icebox:~$ sudo tcpdump -i wlan0
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on wlan0, link-type EN10MB (Ethernet), capture size 65535 bytes
11:28:23.958840 IP icebox.lan > nuq04s29-in-f4.1e100.net: ICMP echo request, id 1901, seq 2, length 64
11:28:23.970928 IP nuq04s29-in-f4.1e100.net > icebox.lan: ICMP echo reply, id 1901, seq 2, length 64
11:28:24.960464 IP icebox.lan > nuq04s29-in-f4.1e100.net: ICMP echo request, id 1901, seq 3, length 64
11:28:24.979299 IP nuq04s29-in-f4.1e100.net > icebox.lan: ICMP echo reply, id 1901, seq 3, length 64
11:28:25.961869 IP icebox.lan > nuq04s29-in-f4.1e100.net: ICMP echo request, id 1901, seq 4, length 64
11:28:25.976176 IP nuq04s29-in-f4.1e100.net > icebox.lan: ICMP echo reply, id 1901, seq 4, length 64
11:28:26.963667 IP icebox.lan > nuq04s29-in-f4.1e100.net: ICMP echo request, id 1901, seq 5, length 64
11:28:26.976137 IP nuq04s29-in-f4.1e100.net > icebox.lan: ICMP echo reply, id 1901, seq 5, length 64
11:28:30.674953 ARP, Request who-has 172.254.1.0 tell ThePickleParty.lan, length 28
11:28:31.190665 IP ThePickleParty.lan.51056 > 192.168.86.255.rfe: UDP, length 306
</pre>

You'll notice a lot of stuff happening when you run a packet capture, well that's to be expected there's a lot of network activity happening in the background. In my above example, I've taken only a snippet of my capture specifically the time when I decided to ping www.google.com. 

<b>Understanding the output</b>

<pre>
11:28:23.958840 IP icebox.lan > nuq04s29-in-f4.1e100.net: ICMP echo request, id 1901, seq 2, length 64
11:28:23.970928 IP nuq04s29-in-f4.1e100.net > icebox.lan: ICMP echo reply, id 1901, seq 2, length 64
</pre>

<ul>
<li>The first field is a timestamp of the network activity</li>
<li>IP, this contains the protocol information</li>
<li>Next, you'll see the source and destination address: icebox.lan > nuq04s29-in-f4.1e100.net</li>
<li>seq, this is the TCP packets's starting and ending sequence number</li>
<li>length, length in bytes</li>
</ul>

As you can see from our tcpdump output, we are sending an ICMP echo request packet to www.google.com and getting an ICMP echo reply packet in return! Also note that different packets will output different information, refer to the manpage to see what those are.

<b>Writing tcpdump output to a file</b>

<pre>
$ sudo tcpdump -w /some/file
</pre>


Some final thoughts: we only scraped the surface of the subject of packet analysis. There is so much you can look at and we haven't even touched upon going even deeper with Hex and ASCII output. There are plenty of resources online to help you learn more about packet analyzers and I urge you to find them!

## Exercise

Download and install the Wireshark tool and play around with the interface.

## Quiz Question

What is the flag to capture a specific interface with tcpdump?

## Quiz Answer

-i
