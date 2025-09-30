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

### Der ifconfig-Befehl

Das Tool **ifconfig** ermöglicht es uns, unsere Netzwerkschnittstellen zu konfigurieren. Wenn wir keine Netzwerkschnittstellen eingerichtet haben, wissen die Gerätetreiber des Kernels und das Netzwerk nicht, wie sie miteinander kommunizieren sollen. Ifconfig wird beim Booten ausgeführt und konfiguriert unsere Schnittstellen über Konfigurationsdateien, aber wir können sie auch manuell ändern. Die Ausgabe von ifconfig zeigt den Schnittstellennamen auf der linken Seite, und die rechte Seite zeigt detaillierte Informationen. Am häufigsten sehen Sie Schnittstellen mit den Namen eth0 (erste Ethernet-Karte im Gerät), wlan0 (drahtlose Schnittstelle) und lo (Loopback-Schnittstelle). Die Loopback-Schnittstelle wird verwendet, um Ihren Computer darzustellen; sie leitet Sie einfach zu sich selbst zurück. Dies ist gut zum Debuggen oder zum Verbinden mit lokal laufenden Servern.

Der Status von Schnittstellen kann up oder down sein. Wie Sie sich denken können, können Sie eine Schnittstelle auf down setzen, wenn Sie sie "ausschalten" möchten. Die Felder, die Sie in der ifconfig-Ausgabe wahrscheinlich am häufigsten betrachten werden, sind die HWaddr (MAC-Adresse der Schnittstelle), inet address (IPv4-Adresse) und inet6 (IPv6-Adresse). Natürlich können Sie sehen, dass die Subnetzmaske und die Broadcast-Adresse ebenfalls vorhanden sind. Sie können Schnittstelleninformationen auch unter /etc/network/interfaces einsehen.

### Eine Schnittstelle erstellen und aktivieren

```bash
ifconfig eth0 192.168.2.1 netmask 255.255.255.0 up
```

Dies weist der eth0-Schnittstelle eine IP-Adresse und eine Netzmaske zu und aktiviert sie.

### Eine Schnittstelle aktivieren oder deaktivieren

```bash
ifup eth0
ifdown eth0
```

### Der ip-Befehl

Der Befehl **ip** ermöglicht es uns auch, den Netzwerk-Stack eines Systems zu manipulieren. Je nach verwendeter Distribution kann dies die bevorzugte Methode zur Manipulation Ihrer Netzwerkeinstellungen sein.

Hier sind einige Beispiele für seine Verwendung:

### Schnittstelleninformationen für alle Schnittstellen anzeigen

```bash
ip link show
```

### Statistiken einer Schnittstelle anzeigen

```bash
ip -s link show eth0
```

### Zugewiesene IP-Adressen für Schnittstellen anzeigen

```bash
ip address show
```

### Schnittstellen aktivieren und deaktivieren

```bash
ip link set eth0 up
ip link set eth0 down
```

### Eine IP-Adresse zu einer Schnittstelle hinzufügen

```bash
ip address add 192.168.1.1/24 dev eth0
```

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis von Netzwerkschnittstellen und IP-Adressierung zu vertiefen:

1. **[MAC- und IP-Adressen in Linux identifizieren](https://labex.io/de/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - Üben Sie die Verwendung des Befehls `ip a`, um Netzwerkinformationen, einschließlich MAC-, IPv4- und IPv6-Adressen auf einem Linux-System, zu identifizieren.
2. **[IP-Adressierung in Linux verwalten](https://labex.io/de/labs/comptia-manage-ip-addressing-in-linux-592736)** - Lernen Sie, statische und dynamische IP-Adressen zu konfigurieren, ein Standard-Gateway einzurichten und Netzwerkkonfigurationen mit dem Befehl `ip` zu überprüfen.
3. **[IP-Adresstypen und Erreichbarkeit in Linux erkunden](https://labex.io/de/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Erkunden Sie verschiedene IP-Adresstypen (privat, öffentlich, Multicast) und testen Sie die Netzwerk-Erreichbarkeit mit `ping` und `ip a`.

Diese Labs helfen Ihnen, die Konzepte der Netzwerkschnittstellenidentifikation und IP-Adressierung in realen Szenarien anzuwenden und Vertrauen in die Linux-Netzwerkverwaltung aufzubauen.

## Quiz Question

Wie lautet der Befehl zum Konfigurieren unserer Netzwerkschnittstellen?

## Quiz Answer

ifconfig
