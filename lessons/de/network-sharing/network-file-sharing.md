---
lesson_id: "network-file-sharing"
course_id: "network-sharing"
lang: "de"
order_index: 1
title: "Überblick über Dateifreigaben"
description: "Lerne, eine SSH-basierte Dateiübertragung mit scp auszuwählen und sicher auszuführen."
meta_title: "Überblick über Dateifreigaben – Netzwerkfreigaben"
meta_description: "Erkunde die Linux-Dateifreigabe und lerne den Befehl scp für sichere Dateiübertragungen über das Netzwerk kennen."
meta_keywords: "Linux-Dateifreigabe, scp-Befehl, sichere Kopie, Linux-Befehle lernen, Linux-Onlinekurs, Linux programmieren, Netzwerkdateiübertragung, Linux-Ressourcen"
---

Das Verschieben von Dateien über ein Netzwerk reicht von einmaligen Kopien über dauerhaft eingehängte Freigaben bis zu synchronisierten Verzeichnisbäumen. Wähle eine Methode anhand von Richtung, Datenmenge, Aktualisierungshäufigkeit, Identitätsmodell, Netzwerkvertrauen, Metadatenanforderungen und der Frage, ob Clients gemeinsamen Live-Zugriff benötigen.

## Eine Übertragungsmethode auswählen

- `scp` oder SFTP bietet eine durch SSH authentifizierte Kopie beziehungsweise interaktive Übertragung.
- `rsync` gleicht Verzeichnisbäume lokal oder über einen Transport wie SSH effizient ab.
- NFS stellt Serverexporte als eingehängte Dateisysteme bereit, gewöhnlich zwischen Unix-artigen Hosts.
- SMB, unter Linux durch Samba implementiert, unterstützt gemeinsamen Zugriff über viele Betriebssysteme hinweg.
- HTTP kann einfache Downloads bereitstellen, ist aber kein allgemeines eingehängtes Dateisystem.

Eine Kopie ist nicht automatisch eine Sicherung. Ein Sicherungsentwurf benötigt außerdem unabhängige Aufbewahrung, Wiederherstellungstests, Integritätsprüfungen und Schutz vor derselben Löschung oder Kompromittierung.

:::single-choice{#file-sharing-one-time-ssh-copy} Welches Werkzeug eignet sich für eine einmalige Dateikopie über SSH?

::option[`scp`]{#file-sharing-scp .correct explanation="SCP verwendet SSH-Authentifizierung und -Transport für Dateikopien."}
::option[`uptime`]{#file-sharing-uptime explanation="Uptime meldet Betriebsdauer und Last eines Hosts, statt Dateien zu übertragen."}
::option[`logrotate`]{#file-sharing-logrotate explanation="Logrotate verwaltet Generationen von Dateiprotokollen auf einem Host."}
:::

## scp-Pfade verstehen

Die allgemeine Form lautet `scp SOURCE DESTINATION`. Ein entfernter Operand verwendet gewöhnlich `user@host:path`:

```bash
$ scp -- report.txt alice@example.net:/srv/incoming/
$ scp -- alice@example.net:/srv/outgoing/result.txt ./result.txt
```

Der erste Befehl überträgt eine lokale Datei zum entfernten Host; der zweite ruft eine entfernte Datei ab. Ein Doppelpunkt trennt den entfernten Host von seinem Pfad. Setze Pfade mit für die Shell bedeutsamen Zeichen in Anführungszeichen und vermeide mehrdeutige, nicht vertrauenswürdige Dateinamen.

:::single-choice{#file-sharing-scp-pull-source} Wo steht bei einem Abruf mit `scp` die entfernte Angabe?

::option[Als Quelle vor dem lokalen Ziel.]{#file-sharing-pull-source .correct explanation="Die Kopierrichtung folgt der Operandenreihenfolge von Quelle zu Ziel."}
::option[Als lokales Ziel hinter jeder Option.]{#file-sharing-pull-destination explanation="Das abgerufene entfernte Objekt ist der Quelloperand."}
::option[Nur innerhalb der SSH-Konfigurationsdatei des Benutzers.]{#file-sharing-pull-config explanation="Die SSH-Konfiguration kann Standardwerte bereitstellen, doch der kopierte entfernte Pfad bleibt ein Operand."}
:::

## Ein Verzeichnis kopieren

Verwende den rekursiven Modus für einen Verzeichnisbaum:

```bash
$ scp -r -- project/ alice@example.net:/srv/incoming/
```

Untersuche vor dem Kopieren Datenmenge, symbolische Links, Berechtigungen, Eigentumsanforderungen, freien Speicherplatz und Zielbenennung. SCP ist keine Synchronisierungsrichtlinie; wiederholte Verzeichniskopien können am Ziel Dateien zurücklassen, die an der Quelle nicht mehr existieren.

:::single-choice{#file-sharing-scp-recursive} Was fordert `scp -r` an?

::option[Das Entfernen des entfernten Ziels vor dem Kopieren.]{#file-sharing-scp-remove explanation="Der rekursive Modus durchläuft Verzeichnisse und definiert keine Bereinigungsrichtlinie."}
::option[Das rekursive Kopieren eines Verzeichnisbaums.]{#file-sharing-scp-tree .correct explanation="Das Kennzeichen ist erforderlich, wenn die ausgewählte Quelle ein Verzeichnis ist."}
::option[Schreibgeschützten Zugriff auf die SSH-Konfiguration.]{#file-sharing-scp-readonly explanation="Die Option betrifft das Durchlaufen von Verzeichnissen und nicht den Konfigurationszugriff."}
:::

## Identität und Ergebnisse überprüfen

Die Überprüfung des SSH-Hostschlüssels schützt vor einer Verbindung zum falschen Server. Behandle einen geänderten Hostschlüssel als Ereignis, das über einen vertrauenswürdigen Kanal geprüft werden muss, statt die Warnung zu umgehen. Verwende Konten mit geringstmöglichen Berechtigungen und eine zur Umgebung passende Schlüsselverwaltung.

Überprüfe nach der Übertragung Exit-Status, erwartete Dateien, Größen, Metadaten und – falls die Integritätsanforderungen es verlangen – unabhängig berechnete Hashes an beiden Enden. Bestätige, dass die Zielanwendung die Daten tatsächlich lesen kann.

:::single-choice{#file-sharing-host-key-change} Was solltest du tun, wenn SSH einen unerwartet geänderten Hostschlüssel meldet?

::option[Die Hostschlüsselprüfung für jede künftige Übertragung deaktivieren.]{#file-sharing-disable-checking explanation="Dies entfernt eine wichtige Kontrolle der Serveridentität."}
::option[Den neuen Schlüssel vor dem Fortfahren über eine vertrauenswürdige Quelle prüfen.]{#file-sharing-verify-key .correct explanation="Die Warnung kann auf einen neu aufgebauten Host, ein falsches Ziel oder einen Abfangversuch hindeuten und sollte untersucht werden."}
::option[Den privaten Authentifizierungsschlüssel in der Befehlsausgabe veröffentlichen.]{#file-sharing-publish-key explanation="Private Anmeldedaten dürfen nicht offengelegt werden."}
:::

## Zusammenfassung

Du kannst nun eine sichere einmalige Netzwerkdateikopie auswählen und überprüfen.

1. Stimme die Freigabemethode auf Zugriffs- und Aufbewahrungsanforderungen ab.
2. Lies lokale und entfernte `scp`-Operanden als Quelle und Ziel.
3. Verwende den rekursiven Modus bewusst für Verzeichnisbäume.
4. Überprüfe Serveridentität, Übertragungsergebnis und Nutzbarkeit am Ziel.
