---
index: 5
lang: "de"
title: "I/O-Überwachung"
meta_title: "I/O-Überwachung - Prozessauslastung"
meta_description: "Erfahren Sie, wie Sie iostat für die Linux-I/O-Überwachung verwenden. Verstehen Sie CPU- und Festplattennutzungsmetriken mit diesem wichtigen Befehl. Verbessern Sie die Systemleistung!"
meta_keywords: "iostat, Linux I/O-Überwachung, CPU-Auslastung, Festplattennutzung, Linux-Befehle, Anfänger, Tutorial, Anleitung"
---

## Lesson Content

Wir können sowohl die CPU-Auslastung als auch die Festplattennutzung mit einem praktischen Tool namens **iostat** überwachen.

```bash
pete@icebox:~$ iostat
Linux 3.13.0-39-lowlatency (icebox)     01/28/2016      _i686_  (1 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           0.13    0.03    0.50    0.01    0.00   99.33

Device:            tps    kB_read/s    kB_wrtn/s    kB_read    kB_wrtn
sda               0.17         3.49         1.92     385106     212417
```

Der erste Teil sind die CPU-Informationen:

- **%user** – Zeigt den Prozentsatz der CPU-Auslastung an, der bei der Ausführung auf Benutzerebene (Anwendung) aufgetreten ist.
- **%nice** – Zeigt den Prozentsatz der CPU-Auslastung an, der bei der Ausführung auf Benutzerebene mit Nice-Priorität aufgetreten ist.
- **%system** – Zeigt den Prozentsatz der CPU-Auslastung an, der bei der Ausführung auf Systemebene (Kernel) aufgetreten ist.
- **%iowait** – Zeigt den Prozentsatz der Zeit an, in der die CPU oder CPUs im Leerlauf waren, während das System eine ausstehende Disk-I/O-Anforderung hatte.
- **%steal** – Zeigt den Prozentsatz der Zeit an, die die virtuelle CPU oder CPUs im unfreiwilligen Wartezustand verbracht haben, während der Hypervisor einen anderen virtuellen Prozessor bediente.
- **%idle** – Zeigt den Prozentsatz der Zeit an, in der die CPU oder CPUs im Leerlauf waren und das System keine ausstehende Disk-I/O-Anforderung hatte.

Der zweite Teil ist die Festplattenauslastung:

- **tps** – Zeigt die Anzahl der Übertragungen pro Sekunde an, die an das Gerät ausgegeben wurden. Eine Übertragung ist eine I/O-Anforderung an das Gerät. Mehrere logische Anforderungen können zu einer einzigen I/O-Anforderung an das Gerät kombiniert werden. Eine Übertragung hat eine unbestimmte Größe.
- **kB_read/s** – Zeigt die vom Gerät gelesene Datenmenge in Kilobyte pro Sekunde an.
- **kB_wrtn/s** – Zeigt die auf das Gerät geschriebene Datenmenge in Kilobyte pro Sekunde an.
- **kB_read** – Die Gesamtzahl der gelesenen Kilobyte.
- **kB_wrtn** – Die Gesamtzahl der geschriebenen Kilobyte.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis der Systemüberwachung und Festplattennutzung zu vertiefen:

1. **[Linux df Befehl: Festplattenspeicherberichte](https://labex.io/de/labs/linux-linux-df-command-disk-space-reporting-219188)** – Üben Sie das Berichten der Festplattenspeichernutzung auf gemounteten Dateisystemen, ein Schlüsselaspekt der Überwachung.
2. **[Linux du Befehl: Dateispeicher schätzen](https://labex.io/de/labs/linux-linux-du-command-file-space-estimating-219190)** – Lernen Sie, die Festplattenspeichernutzung für Verzeichnisse und Unterverzeichnisse zu schätzen, was die Disk-I/O-Informationen von `iostat` ergänzt.
3. **[Linux top Befehl: Echtzeit-Systemüberwachung](https://labex.io/de/labs/linux-linux-top-command-real-time-system-monitoring-388500)** – Erkunden Sie die Echtzeit-Systemüberwachung, einschließlich CPU- und Speichernutzung, die einen breiteren Kontext für die in `iostat` angezeigten CPU-Metriken bietet.

Diese Übungen helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in die Überwachung von Linux-Systemressourcen aufzubauen.

## Quiz Question

Welcher Befehl kann verwendet werden, um die I/O- und CPU-Auslastung anzuzeigen?

## Quiz Answer

iostat
