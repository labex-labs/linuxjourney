---
index: 5
lang: "de"
title: "Paketanalyse"
meta_title: "Paketanalyse - Fehlerbehebung"
meta_description: "Lernen Sie die Grundlagen der Paketanalyse mit tcpdump. Verstehen Sie Netzwerkverkehr, erfassen Sie Daten und interpretieren Sie die Ausgabe mit diesem anfängerfreundlichen Linux-Leitfaden."
meta_keywords: "tcpdump, Paketanalyse, Netzwerkanalyse, Linux-Netzwerk, Anfänger-Tutorial, Wireshark, Linux-Befehle, Netzwerkverkehr"
---

## Lesson Content

Das Thema Paketanalyse könnte einen eigenen Kurs füllen, und es gibt viele Bücher, die sich nur mit Paketanalyse befassen. Heute werden wir jedoch nur die Grundlagen lernen. Es gibt zwei äußerst beliebte Paketanalysatoren: Wireshark und tcpdump. Diese Tools scannen Ihre Netzwerkschnittstellen, erfassen die Paketaktivität, parsen die Pakete und geben die Informationen für uns aus. Sie ermöglichen es uns, in die Details der Netzwerkanalyse einzusteigen und uns mit den Low-Level-Aspekten zu befassen. Wir werden tcpdump verwenden, da es eine einfachere Schnittstelle hat; wenn Sie jedoch Paketanalyse in Ihr Repertoire aufnehmen möchten, würde ich Ihnen empfehlen, sich Wireshark anzusehen.

### tcpdump installieren

```bash
sudo apt install tcpdump
```

### Paketdaten auf einer Schnittstelle erfassen

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

Sie werden feststellen, dass viel passiert, wenn Sie eine Paketerfassung durchführen. Nun, das ist zu erwarten; im Hintergrund findet viel Netzwerkaktivität statt. In meinem obigen Beispiel habe ich nur einen Ausschnitt meiner Erfassung genommen, speziell die Zeit, als ich beschloss, `www.google.com` anzupingen.

### Die Ausgabe verstehen

```plaintext
11:28:23.958840 IP icebox.lan > nuq04s29-in-f4.1e100.net: ICMP echo request, id 1901, seq 2, length 64
11:28:23.970928 IP nuq04s29-in-f4.1e100.net > icebox.lan: ICMP echo reply, id 1901, seq 2, length 64
```

- Das erste Feld ist ein Zeitstempel der Netzwerkaktivität.
- IP: Dies enthält die Protokollinformationen.
- Als Nächstes sehen Sie die Quell- und Zieladresse: `icebox.lan > nuq04s29-in-f4.1e100.net`.
- `seq`: Dies ist die Start- und Endsequenznummer des TCP-Pakets.
- `length`: Länge in Bytes.

Wie Sie aus unserer tcpdump-Ausgabe ersehen können, senden wir ein ICMP-Echo-Anfragepaket an `www.google.com` und erhalten im Gegenzug ein ICMP-Echo-Antwortpaket! Beachten Sie auch, dass verschiedene Pakete unterschiedliche Informationen ausgeben; schlagen Sie in der Manpage nach, um zu sehen, welche das sind.

### tcpdump-Ausgabe in eine Datei schreiben

```bash
sudo tcpdump -w /some/file
```

Einige abschließende Gedanken: Wir haben das Thema Paketanalyse nur oberflächlich behandelt. Es gibt so viel, was man sich ansehen kann, und wir haben noch nicht einmal die Möglichkeit angesprochen, noch tiefer mit Hex- und ASCII-Ausgabe zu gehen. Es gibt viele Online-Ressourcen, die Ihnen helfen, mehr über Paketanalysatoren zu erfahren, und ich fordere Sie dringend auf, diese zu finden!

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis der Paketanalyse zu vertiefen:

1. **[Ethernet-Frames mit tcpdump in Linux analysieren](https://labex.io/de/labs/linux-analyze-ethernet-frames-with-tcpdump-in-linux-592765)** – Üben Sie das Erfassen und Überprüfen von Ethernet-Frames, das Generieren von Datenverkehr und das Analysieren von Frame-Headern und MAC-Adressen mit `tcpdump`.

Dieses Lab hilft Ihnen, die Konzepte der Paketanalyse in einem realen Szenario anzuwenden und Vertrauen in die Netzwerk-Fehlerbehebung aufzubauen.

## Quiz Question

Was ist das Flag, um eine bestimmte Schnittstelle mit tcpdump zu erfassen?

## Quiz Answer

-i
