---
lesson_id: "device-types"
course_id: "devices"
lang: "de"
order_index: 2
title: "Gerätetypen"
description: "Lerne, Zeichen- und Blockgeräteknoten von Pipes, Sockets und gewöhnlichen Dateisystemobjekten zu unterscheiden."
meta_title: "Gerätetypen – Geräte"
meta_description: "Erkunde Linux-Gerätetypen wie Zeichen- und Blockgeräte sowie FIFOs und Unix-Sockets. Lerne außerdem Major- und Minor-Gerätenummern kennen."
meta_keywords: "Linux Geräte, Linux Gerätetypen, Gerätedatei, Zeichengerät, Blockgerät, Major Minor Nummern, /dev Verzeichnis"
---

Das erste Zeichen eines von `ls -l` angezeigten Modus bezeichnet den Dateisystemtyp eines Objekts. Unter `/dev` sind besondere Zeichen- und Blockdateien Geräteknoten. Dort können auch Pipes und Knoten von Unix-Domain-Sockets erscheinen. Diese sind jedoch Objekte für die Interprozesskommunikation und keine Hardware-Geräteknoten.

```text
$ ls -l /dev/null /dev/sda /run/systemd/journal/dev-log /tmp/example-fifo
crw-rw-rw- 1 root root 1, 3 ... /dev/null
brw-rw---- 1 root disk 8, 0 ... /dev/sda
srw-rw-rw- 1 root root      ... /run/systemd/journal/dev-log
prw------- 1 user user      ... /tmp/example-fifo
```

Einträge und Berechtigungen unterscheiden sich je nach System; das Beispiel veranschaulicht nur die Typzeichen.

## Zeichengeräteknoten

Ein `c` bezeichnet ein Zeichengerät. Es stellt normalerweise eine stromorientierte oder gerätespezifische Schnittstelle bereit und keinen adressierbaren Speicher aus Blöcken fester Größe. Beispiele sind Terminals und Pseudogeräte wie `/dev/null`.

„Zeichen“ bedeutet nicht, dass jeder Systemaufruf genau ein Zeichen übertragen muss. Anwendungen können Puffer lesen oder schreiben, während der Treiber Blockierung, Rahmung und Steuerverhalten festlegt.

:::single-choice{#device-types-character-marker} Welches erste Moduszeichen bezeichnet einen Zeichengeräteknoten?

::option[`b`]{#device-types-marker-block explanation="Das Zeichen `b` bezeichnet einen Blockgeräteknoten."}
::option[`p`]{#device-types-marker-pipe explanation="Das Zeichen `p` bezeichnet eine FIFO, also eine benannte Pipe."}
::option[`c`]{#device-types-marker-character .correct explanation="Besondere Zeichendateien beginnen in einer langen Auflistung mit `c`."}
:::

## Blockgeräteknoten

Ein `b` bezeichnet ein Blockgerät. Blockgeräte stellen über die Blockschicht des Kernels adressierbaren Speicher in Blöcken bereit und können Operationen wie gepufferte Ein-/Ausgabe, Partitionierung und Dateisysteme unterstützen. Datenträger, Partitionen und logische Volumes besitzen häufig Blockgeräteknoten.

Ein Blockgeräteknoten ist kein eingehängtes Dateisystem. Er stellt ein Speichergerät oder einen logischen Bereich dar; darauf kann getrennt ein Dateisystem erstellt und eingehängt werden. Das Schreiben von Rohdaten auf den falschen Blockgeräteknoten kann Partitionstabellen, Dateisysteme oder Benutzerdaten zerstören.

:::single-choice{#device-types-block-marker} Was bedeutet das erste Moduszeichen `b`?

::option[Einen Hintergrundjob der Shell.]{#device-types-background-job explanation="Der Zustand eines Shelljobs ist nicht als Dateisystem-Typzeichen codiert."}
::option[Eine Blockgeräteschnittstelle.]{#device-types-block-device .correct explanation="Besondere Blockdateien stellen über das Blocksubsystem des Kernels adressierbaren Speicher bereit."}
::option[Einen beschädigten symbolischen Link.]{#device-types-broken-link explanation="Symbolische Links verwenden `l`, unabhängig davon, ob ihr Ziel aktuell existiert."}
:::

## FIFOs und Socket-Knoten

Ein `p` bezeichnet eine FIFO, auch benannte Pipe genannt. Sie stellt einen benannten Bytestrom zur Kommunikation zwischen Prozessen bereit. Nach dem Lesen bleiben die Daten nicht dauerhaft im FIFO-Knoten gespeichert.

Ein `s` bezeichnet den Knoten eines Unix-Domain-Sockets. Er benennt einen lokalen Socket-Endpunkt und kann verbindungsorientierte oder Datagramm-Kommunikation, die Übergabe von Dateideskriptoren und Funktionen für Peer-Anmeldedaten unterstützen. Netzwerk-Sockets mit Internetadressen besitzen nicht zwangsläufig Dateisystemknoten.

Weder eine FIFO noch ein Unix-Socket-Knoten verwendet Major- und Minor-Nummern zur Auswahl eines Hardwaretreibers.

:::single-choice{#device-types-pipe-socket-distinction} Welche Aussage unterscheidet diese IPC-Objekttypen richtig?

::option[`p` bezeichnet eine Datenträgerpartition, `s` einen Solid-State-Speicher.]{#device-types-storage-letters explanation="Partitionen sind normalerweise Blockgeräte; die Buchstaben codieren keine Speichertechnologie."}
::option[`p` bezeichnet eine FIFO, `s` den Knoten eines Unix-Domain-Sockets.]{#device-types-p-and-s .correct explanation="Dies sind getrennte Dateisystemobjekttypen für die lokale Interprozesskommunikation."}
::option[Beide Typen identifizieren Kernel-Blocktreiber über Major-Nummern.]{#device-types-ipc-major explanation="FIFO- und Socket-Knoten sind weder Zeichen- noch Blockgeräteknoten."}
:::

## Major- und Minor-Gerätenummern

Zeichen- und Blockgeräteknoten speichern eine Gerätenummer, die in Major- und Minor-Komponente aufgeteilt ist. In einer langen Auflistung ersetzen sie die gewöhnliche Spalte für die Dateigröße:

```text
brw-rw---- 1 root disk 8, 0 ... /dev/sda
```

Das Zahlenpaar teilt dem Kernel mit, welche registrierte Geräteschnittstelle und Instanz der Knoten anspricht. Eine Major-Nummer ist einem Treiber oder einer Geräteklasse zugeordnet; der Treiber interpretiert die Minor-Nummer. Codiere Annahmen wie „Minor null bedeutet immer das erste Laufwerk“ nicht fest ein, denn die Zuordnung hängt vom Subsystem und den Kernel-Schnittstellen ab.

Zeige Typ und Gerätenummern ausdrücklich an:

```bash
$ stat -c 'type=%F major=%t minor=%T path=%n' /dev/null
```

GNU `stat` gibt die Werte `%t` und `%T` hexadezimal aus.

:::single-choice{#device-types-major-minor-scope} Welche Objekte verwenden Major- und Minor-Nummern zur Identifikation einer Kernel-Geräteschnittstelle?

::option[Jede gewöhnliche Datei und jedes Verzeichnis.]{#device-types-all-files explanation="Gewöhnliche Dateien verwenden Größe und Dateisystemmetadaten statt eines Major-/Minor-Paars für Geräteknoten."}
::option[Nur symbolische Links, deren Ziel fehlt.]{#device-types-broken-symlinks explanation="Symbolische Links speichern Pfadtext und werden bei einem fehlenden Ziel nicht zu Geräteknoten."}
::option[Zeichen- und Blockgeräteknoten.]{#device-types-device-number-nodes .correct explanation="Ihre besonderen Inode-Metadaten enthalten die an eine Treiberschnittstelle weitergeleitete Gerätenummer."}
:::

## Zusammenfassung

Du kannst besondere Dateisystemtypen nun einordnen, ohne sie alle als Hardwaregeräte zu behandeln.

1. Lies `c` als Zeichen- und `b` als Blockgeräteknoten.
2. Lies `p` als FIFO und `s` als Knoten eines Unix-Domain-Sockets.
3. Ordne Major- und Minor-Nummern ausschließlich Geräteknoten zu.
4. Behandle rohen Zugriff auf Blockgeräte als potenziell zerstörerisch.
