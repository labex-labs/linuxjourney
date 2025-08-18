---
index: 1
lang: "de"
title: "Netzwerkschnittstellen"
meta_title: "Netzwerkschnittstellen - Netzwerkkonfiguration"
meta_description: "Erfahren Sie mehr über Linux-Netzwerkschnittstellen, ifconfig und ip-Befehle. Verstehen Sie, wie Netzwerkeinstellungen konfiguriert und verwaltet werden. Beginnen Sie Ihre Linux-Netzwerkreise!"
meta_keywords: "Linux-Netzwerkschnittstellen, ifconfig, ip-Befehl, Netzwerkkonfiguration, Linux-Netzwerk, Anfänger, Tutorial, Anleitung"
---

## Lesson Content

Eine Netzwerkschnittstelle ist die Art und Weise, wie der Kernel die Softwareseite der Vernetzung mit der Hardwareseite verbindet. Wir haben bereits ein Beispiel dafür gesehen:

```plaintext
pete@icebox:~$ ifconfig -a
eth0      Link encap:Ethernet  HWaddr 1d:3a:32:24:4d:ce
          inet addr:192.168.1.129  Bcast:192.168.1.255  Mask:255.255.255.0
          inet6 addr: fd60::21c:29ff:fe63:5cdc/64 Scope:Link
```

### The ifconfig command

Das **ifconfig**-Tool ermöglicht es uns, unsere Netzwerkschnittstellen zu konfigurieren. Wenn wir keine Netzwerkschnittstellen eingerichtet haben, wissen die Gerätetreiber des Kernels und das Netzwerk nicht, wie sie miteinander kommunizieren sollen. Ifconfig wird beim Booten ausgeführt und konfiguriert unsere Schnittstellen über Konfigurationsdateien, aber wir können sie auch manuell ändern. Die Ausgabe von ifconfig zeigt den Schnittstellennamen auf der linken Seite, und die rechte Seite zeigt detaillierte Informationen. Am häufigsten sehen Sie Schnittstellen mit den Namen eth0 (erste Ethernet-Karte im Gerät), wlan0 (drahtlose Schnittstelle) und lo (Loopback-Schnittstelle). Die Loopback-Schnittstelle wird verwendet, um Ihren Computer darzustellen; sie leitet Sie einfach zu sich selbst zurück. Dies ist gut zum Debuggen oder zum Verbinden mit lokal laufenden Servern.

Der Status von Schnittstellen kann up oder down sein. Wie Sie sich denken können, können Sie, wenn Sie eine Schnittstelle "ausschalten" möchten, sie auf down setzen. Die Felder, die Sie in der ifconfig-Ausgabe wahrscheinlich am häufigsten betrachten werden, sind die HWaddr (MAC-Adresse der Schnittstelle), inet address (IPv4-Adresse) und inet6 (IPv6-Adresse). Natürlich können Sie sehen, dass die Subnetzmaske und die Broadcast-Adresse ebenfalls vorhanden sind. Sie können Schnittstelleninformationen auch unter /etc/network/interfaces einsehen.

### To create an interface and bring it up

```bash
ifconfig eth0 192.168.2.1 netmask 255.255.255.0 up
```

Dies weist der eth0-Schnittstelle eine IP-Adresse und eine Netzmaske zu und bringt sie auch hoch.

### To bring up or down an interface

```bash
ifup eth0
ifdown eth0
```

### The ip command

Der **ip**-Befehl ermöglicht es uns auch, den Netzwerk-Stack eines Systems zu manipulieren. Abhängig von der verwendeten Distribution kann dies die bevorzugte Methode zur Manipulation Ihrer Netzwerkeinstellungen sein.

Hier sind einige Beispiele für seine Verwendung:

### To show interface information for all interfaces

```bash
ip link show
```

### To show the statistics of an interface

```bash
ip -s link show eth0
```

### To show IP addresses allocated to interfaces

```bash
ip address show
```

### To bring interfaces up and down

```bash
ip link set eth0 up
ip link set eth0 down
```

### To add an IP address to an interface

```bash
ip address add 192.168.1.1/24 dev eth0
```

## Exercise

Versuchen Sie, den Status Ihrer Netzwerkschnittstellen auf up oder down zu ändern und beobachten Sie, was passiert.

Können Sie Ihre Netzwerkschnittstellen sowohl mit den ifconfig- als auch mit den ip-Befehlen ändern?

## Quiz Question

Wie lautet der Befehl zum Konfigurieren unserer Netzwerkschnittstellen?

## Quiz Answer

ifconfig
