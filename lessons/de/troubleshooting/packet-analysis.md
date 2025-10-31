---
index: 5
lang: "de"
title: "Paketanalyse"
meta_title: "Paketanalyse - Fehlerbehebung"
meta_description: "Lernen Sie die Grundlagen der Netzwerk-Paketanalyse unter Linux. Diese Anleitung stellt tcpdump vor, einen leistungsstarken Paketanalysator, um Netzwerkverkehr zu erfassen und zu interpretieren."
meta_keywords: "tcpdump, Paketanalyse, Netzwerk-Paketanalyse, Netzwerk-Paketanalysator, Netzwerkanalyse, Netzwerk-Paketanalyse-Tools, Linux-Netzwerk, Wireshark, Linux-Befehle, Netzwerkverkehr"
---

## Lesson Content

Das Gebiet der Netzwerkanalyse ist riesig und kann Gegenstand ganzer Kurse und Bücher sein. Diese Lektion führt in die Grundlagen ein. Die Paket-Analyse umfasst das Erfassen und Untersuchen der Daten, die über ein Netzwerk gesendet werden. Es ist eine wesentliche Fähigkeit für die Fehlerbehebung im Netzwerk, die Leistungsoptimierung und die Sicherheitsanalyse. Durch die Untersuchung einzelner Pakete erhalten Sie tiefe Einblicke in das, was auf einer niedrigen Ebene in Ihrem Netzwerk geschieht.

### Beliebte Tools zur Netzwerkanalyse

Es gibt zwei extrem beliebte Tools zur Netzwerkanalyse: Wireshark und tcpdump. Beide sind leistungsstarke Paketanalysatoren, die Ihre Netzwerkschnittstellen scannen, Paketaktivitäten erfassen und die Daten zur Inspektion analysieren. Sie ermöglichen es uns, ins Detail der Netzwerkanalyse einzutauchen. Wir verwenden tcpdump wegen seiner Einfachheit über die Kommandozeile, aber wenn Sie planen, tiefer in die Netzwerkanalyse einzutauchen, wird die Erkundung der grafischen Oberfläche von Wireshark dringend empfohlen.

### Installation von tcpdump

Auf Debian-basierten Systemen wie Ubuntu können Sie tcpdump mit dem folgenden Befehl installieren:

```bash
sudo apt install tcpdump
```

### Erfassen von Live-Paketdaten

Um die Datenerfassung auf einer bestimmten Schnittstelle zu starten, verwenden Sie das Flag `-i`, gefolgt vom Schnittstellennamen.

```plaintext
pete@icebox:~$ sudo tcpdump -i wlan0
tcpdump: ausführliche Ausgabe unterdrückt, verwenden Sie -v oder -vv für vollständige Protokolldekodierung
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

Sie werden viele Aktivitäten bemerken, wenn Sie eine Paketerfassung starten, was angesichts des konstanten Hintergrundnetzwerkverkehrs zu erwarten ist. Das obige Beispiel zeigt einen Ausschnitt einer Erfassung, die während des Pings von `www.google.com` gemacht wurde.

### Interpretation der tcpdump-Ausgabe

Lassen Sie uns eine Zeile aus der Erfassung aufschlüsseln:

```plaintext
11:28:23.958840 IP icebox.lan > nuq04s29-in-f4.1e100.net: ICMP echo request, id 1901, seq 2, length 64
```

- **Zeitstempel**: Das erste Feld (`11:28:23.958840`) zeigt an, wann das Paket erfasst wurde.
- **Protokoll**: `IP` zeigt das Protokoll der Netzwerkschicht an.
- **Quelle und Ziel**: `icebox.lan > nuq04s29-in-f4.1e100.net` zeigt den Ursprung und das Ziel des Pakets an.
- **Protokollspezifische Informationen**: Der Rest der Zeile enthält Details, die für das Protokoll spezifisch sind. Für dieses ICMP-Paket:
  - `seq`: Die Sequenznummer des Pakets.
  - `length`: Die Paketlänge in Bytes.

Wie Sie sehen, hat unsere Maschine eine ICMP-Echo-Anforderung gesendet und eine ICMP-Echo-Antwort erhalten. Verschiedene Protokolle zeigen unterschiedliche Informationen an. Konsultieren Sie die Manpage für weitere Details.

### Speichern von Erfassungen für die spätere Analyse

Anstatt den Live-Verkehr anzuzeigen, können Sie die Erfassung mit dem Flag `-w` in einer Datei speichern. Dies ist nützlich für eine tiefere, Offline-Paketanalyse.

```bash
sudo tcpdump -w /some/file.pcap
```

Wir haben bisher nur an der Oberfläche der Paket-Analyse gekratzt. Es gibt noch viel mehr zu entdecken, einschließlich erweiterter Filterung und der Inspektion von Paket-Inhalten in Hex und ASCII. Unzählige Online-Ressourcen können Ihnen helfen, die Tools zur Netzwerkanalyse zu meistern, und wir ermutigen Sie, Ihre Lernreise fortzusetzen.

## Exercise

Um Ihr Verständnis der Paket-Analyse zu festigen, versuchen Sie dieses praktische Labor. Übung macht den Meister!

1. **[Ethernet-Frames mit tcpdump unter Linux analysieren](https://labex.io/de/labs/comptia-analyze-ethernet-frames-with-tcpdump-in-linux-592765)** - Üben Sie das Erfassen und Untersuchen von Ethernet-Frames, das Generieren von Verkehr und die Analyse von Frame-Headern und MAC-Adressen mit `tcpdump`.

Dieses Labor hilft Ihnen, die Konzepte der Paket-Analyse in einem realen Szenario anzuwenden und Vertrauen in die Netzwerk-Fehlerbehebung aufzubauen.

## Quiz Question

Was ist das Flag, um eine bestimmte Schnittstelle mit tcpdump zu erfassen? Bitte antworten Sie nur mit dem erforderlichen Flag in Englisch. Die Antwort ist groß-/kleinschreibungsempfindlich.

## Quiz Answer

-i
