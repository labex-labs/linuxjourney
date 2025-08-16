---
lang: "de"
title: "Paketanalyse"
description: "Lernen Sie die Grundlagen der Paketanalyse mit tcpdump. Verstehen Sie den Netzwerkverkehr, erfassen Sie Daten und interpretieren Sie die Ausgabe mit diesem anfängerfreundlichen Linux-Leitfaden."
keywords: "tcpdump, Paketanalyse, Netzwerkanalyse, Linux-Netzwerk, Anfänger-Tutorial, Wireshark, Linux-Befehle, Netzwerkverkehr"
---

## Lesson Content

Das Thema Paketanalyse könnte einen ganzen Kurs für sich füllen, und es gibt viele Bücher, die sich nur mit Paketanalyse befassen. Heute werden wir jedoch nur die Grundlagen lernen. Es gibt zwei äußerst beliebte Paketanalysatoren: Wireshark und tcpdump. Diese Tools scannen Ihre Netzwerkschnittstellen, erfassen die Paketaktivität, analysieren die Pakete und geben die Informationen zur Ansicht aus. Sie ermöglichen es uns, tief in die Netzwerkanalyse einzusteigen und uns mit den Low-Level-Details zu befassen. Wir werden tcpdump verwenden, da es eine einfachere Schnittstelle hat; wenn Sie jedoch Paketanalyse in Ihr Repertoire aufnehmen möchten, würde ich Ihnen empfehlen, sich Wireshark anzusehen.

### Install tcpdump

```bash
sudo apt install tcpdump
```

### Capture packet data on an interface

```plaintext
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
```

Sie werden feststellen, dass viel passiert, wenn Sie eine Paketerfassung durchführen. Nun, das ist zu erwarten; im Hintergrund findet viel Netzwerkaktivität statt. In meinem obigen Beispiel habe ich nur einen Ausschnitt meiner Erfassung genommen, speziell die Zeit, als ich mich entschied, <www.google.com> anzupingen.

### Understanding the output

```plaintext
11:28:23.958840 IP icebox.lan > nuq04s29-in-f4.1e100.net: ICMP echo request, id 1901, seq 2, length 64
11:28:23.970928 IP nuq04s29-in-f4.1e100.net > icebox.lan: ICMP echo reply, id 1901, seq 2, length 64
```

- Das erste Feld ist ein Zeitstempel der Netzwerkaktivität.
- IP: Dies enthält die Protokollinformationen.
- Als Nächstes sehen Sie die Quell- und Zieladresse: `icebox.lan > nuq04s29-in-f4.1e100.net`.
- `seq`: Dies ist die Start- und Endsequenznummer des TCP-Pakets.
- `length`: Länge in Bytes.

Wie Sie aus unserer tcpdump-Ausgabe ersehen können, senden wir ein ICMP echo request-Paket an <www.google.com> und erhalten im Gegenzug ein ICMP echo reply-Paket! Beachten Sie auch, dass verschiedene Pakete unterschiedliche Informationen ausgeben; schlagen Sie in der Manpage nach, um zu sehen, welche das sind.

### Writing tcpdump output to a file

```bash
sudo tcpdump -w /some/file
```

Einige abschließende Gedanken: Wir haben das Thema Paketanalyse nur oberflächlich behandelt. Es gibt so viel zu sehen, und wir haben noch nicht einmal die Möglichkeit angesprochen, mit Hex- und ASCII-Ausgabe noch tiefer zu gehen. Es gibt viele Online-Ressourcen, die Ihnen helfen, mehr über Paketanalysatoren zu erfahren, und ich fordere Sie dringend auf, diese zu finden!

## Exercise

Laden Sie das Wireshark-Tool herunter, installieren Sie es und spielen Sie mit der Oberfläche herum.

## Quiz Question

Was ist das Flag, um eine bestimmte Schnittstelle mit tcpdump zu erfassen?

## Quiz Answer

-i
