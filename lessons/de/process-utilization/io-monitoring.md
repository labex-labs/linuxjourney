---
index: 5
lang: "de"
title: "I/O-Überwachung"
meta_title: "I/O-Überwachung – Prozessauslastung"
meta_description: "Meistern Sie die Linux I/O-Überwachung mit dem iostat-Befehl. Diese Anleitung erklärt, wie Sie CPU- und Festplattenauslastungsmetriken analysieren, um die Systemleistung zu optimieren."
meta_keywords: "i/o überwachung, iostat, linux i/o überwachung, cpu auslastung, festplattenauslastung, systemleistung, iowait, linux befehle"
---

## Lesson Content

Effektives **I/O-Monitoring** ist entscheidend für die Aufrechterhaltung eines gesunden und reaktionsschnellen Linux-Systems. Ein leistungsstarkes Befehlszeilenwerkzeug für diese Aufgabe ist **iostat**, das detaillierte Berichte über CPU- und Festplattenaktivität liefert.

Die Ausführung des Befehls `iostat` generiert eine Momentaufnahme der Leistungsmetriken Ihres Systems.

```bash
pete@icebox:~$ iostat
Linux 3.13.0-39-lowlatency (icebox)     01/28/2016      _i686_  (1 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           0.13    0.03    0.50    0.01    0.00   99.33

Device:            tps    kB_read/s    kB_wrtn/s    kB_read    kB_wrtn
sda               0.17         3.49         1.92     385106     212417
```

Die Ausgabe ist in zwei Hauptabschnitte unterteilt. Lassen Sie uns diese aufschlüsseln.

### Verständnis der CPU-Metriken

Der erste Bericht beschreibt die CPU-Auslastung und gibt Aufschluss darüber, wie der Prozessor seine Zeit verbringt.

- **%user**: Prozentsatz der CPU-Zeit, die für die Ausführung von Prozessen auf Benutzerebene (Anwendungen) aufgewendet wird.
- **%nice**: Prozentsatz der CPU-Zeit, die für Prozesse auf Benutzerebene mit modifizierter (nice) Priorität aufgewendet wird.
- **%system**: Prozentsatz der CPU-Zeit, die für die Ausführung von Prozessen auf Systemebene (Kernel) aufgewendet wird.
- **%iowait**: Prozentsatz der Zeit, in der die CPU untätig war, während sie auf den Abschluss einer ausstehenden Festplatten-I/O-Anforderung wartete. Hohe Werte hier können auf einen Speicherengpass hinweisen.
- **%steal**: In einer virtualisierten Umgebung ist dies der Prozentsatz der Zeit, in der eine virtuelle CPU auf eine reale CPU wartet, während der Hypervisor einen anderen virtuellen Prozessor bedient.
- **%idle**: Prozentsatz der Zeit, in der die CPU untätig war und nicht auf I/O-Anforderungen der Festplatte wartete.

### Analyse der Festplattenauslastung

Der zweite Bericht konzentriert sich auf das **I/O-Monitoring** auf Geräteeebene und zeigt, wie Daten auf Ihre Speichergeräte übertragen werden und von diesen abgerufen werden.

- **tps**: Übertragungen pro Sekunde, die an das Gerät gesendet werden. Eine Übertragung ist eine I/O-Anforderung, und mehrere logische Anforderungen können zu einer einzigen zusammengefasst werden.
- **kB_read/s**: Die vom Gerät gelesene Datenmenge, ausgedrückt in Kilobyte pro Sekunde.
- **kB_wrtn/s**: Die auf das Gerät geschriebene Datenmenge, ausgedrückt in Kilobyte pro Sekunde.
- **kB_read**: Die insgesamt vom Gerät gelesenen Kilobytes seit dem letzten Neustart.
- **kB_wrtn**: Die insgesamt auf das Gerät geschriebenen Kilobytes seit dem letzten Neustart.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis der Systemüberwachung und Festplattennutzung zu festigen:

1. **[Linux df Befehl: Berichterstattung über den Speicherplatz](https://labex.io/de/labs/linux-linux-df-command-disk-space-reporting-219188)** - Üben Sie die Berichterstattung über die Festplattennutzung auf gemounteten Dateisystemen, ein wichtiger Aspekt der Überwachung.
2. **[Linux du Befehl: Schätzung des Speicherplatzes](https://labex.io/de/labs/linux-linux-du-command-file-space-estimating-219190)** - Lernen Sie, die Festplattennutzung für Verzeichnisse und Unterverzeichnisse abzuschätzen, was die von `iostat` bereitgestellten Festplatten-I/O-Informationen ergänzt.
3. **[Linux top Befehl: Echtzeit-Systemüberwachung](https://labex.io/de/labs/linux-linux-top-command-real-time-system-monitoring-388500)** - Erkunden Sie die Echtzeit-Systemüberwachung, einschließlich CPU- und Speichernutzung, was einen breiteren Kontext für die in `iostat` angezeigten CPU-Metriken bietet.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in die Überwachung von Linux-Systemressourcen aufzubauen.

## Quiz Question

Welcher Befehl kann verwendet werden, um I/O- und CPU-Auslastung anzuzeigen? (Bitte antworten Sie nur in Kleinbuchstaben auf Englisch)

## Quiz Answer

iostat
