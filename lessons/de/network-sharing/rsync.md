---
index: 2
lang: "de"
title: "rsync"
meta_title: "rsync - Netzwerkfreigabe"
meta_description: "Erfahren Sie, wie Sie den leistungsstarken rsync-Befehl unter Linux für effiziente Dateisynchronisierung, Remote-Datenübertragung und zuverlässige Backups verwenden. Diese Anleitung behandelt wichtige rsync-Befehle und Optionen."
meta_keywords: "rsync, linux rsync, dateisynchronisierung, datensicherung, remote sync, rsync befehl, linux dateitransfer, rsync tutorial"
---

## Lesson Content

### Was ist rsync?

Ein weiteres unverzichtbares Werkzeug zum Kopieren von Daten zwischen verschiedenen Hosts ist `rsync`, was für "remote synchronization" (Fernsynchronisation) steht. Obwohl es `scp` ähnelt, hat `rsync` einen wesentlichen Unterschied, der es unglaublich effizient macht. Es verwendet einen Delta-Transfer-Algorithmus, der intelligent das Ziel auf vorhandene Daten überprüft und nur die Teile von Dateien überträgt, die sich geändert haben.

Wenn beispielsweise eine große Dateiübertragung unterbrochen wird, kann `rsync` das Kopieren fortsetzen und nur die verbleibenden Teile der Datei übertragen, anstatt von vorne zu beginnen. Dies macht es zu einer robusten Wahl für instabile Netzwerkverbindungen.

### Hauptmerkmale von rsync

Die Effizienz von `rsync` ergibt sich aus seinen intelligenten Optimierungen. Es überprüft die Dateiintegrität mithilfe von Prüfsummen, um sicherzustellen, dass die kopierten Daten während der Übertragung nicht beschädigt werden. Diese Funktionen bieten erhebliche Flexibilität und machen `rsync` zu einem idealen Werkzeug für:

- Verzeichnissynchronisation (sowohl remote als auch lokal)
- Erstellung inkrementeller Datensicherungen
- Effiziente Handhabung großer Datenübertragungen

### Häufige rsync-Optionen

Sie können das Verhalten des `rsync`-Befehls mit verschiedenen Optionen modifizieren. Zu den am häufigsten verwendeten gehören:

- `-v`: Ausführliche Ausgabe (Verbose), zeigt an, welche Dateien übertragen werden.
- `-r`: Rekursiv, notwendig für das Kopieren ganzer Verzeichnisse.
- `-h`: Menschenlesbare Ausgabe (Human-readable), zeigt Zahlen in einem verständlicheren Format an (z. B. KB, MB).
- `-z`: Komprimiert die Dateiübertragung während der Übertragung, ideal für langsame Verbindungen.
- `-a`: Archivmodus, eine praktische Abkürzung, die mehrere Optionen (`-rlptgoD`) kombiniert, um Berechtigungen, Eigentümerschaft und Zeitstempel beizubehalten.

### rsync Anwendungsbeispiele

#### Dateien auf demselben Host synchronisieren

Sie können `rsync` verwenden, um zwei Verzeichnisse auf Ihrem lokalen Rechner zu synchronisieren. Dies ist nützlich für die Erstellung lokaler Backups.

```bash
rsync -avh /my/local/directory/one/ /my/local/directory/two/
```

#### Dateien von einem Remote-Host auf einen lokalen Host synchronisieren

Um Dateien von einem Remote-Server auf Ihren lokalen Rechner zu ziehen, geben Sie zuerst die Remote-Quelle an.

```bash
rsync -avh username@remotehost.com:/remote/directory/ /local/directory/
```

#### Dateien von einem lokalen Host auf einen Remote-Host synchronisieren

Um Dateien von Ihrem lokalen Rechner auf einen Remote-Server zu pushen, geben Sie zuerst die lokale Quelle an.

```bash
rsync -avh /local/directory/ username@remotehost.com:/remote/directory/
```

## Exercise

Obwohl es für dieses Thema keine spezifischen Übungen gibt, empfehlen wir Ihnen, den umfassenden [Linux Lernpfad](https://labex.io/de/learn/linux) zu erkunden, um verwandte Linux-Fähigkeiten und -Konzepte zu üben.

## Quiz Question

Welcher Befehl, bekannt für seinen Delta-Transfer-Algorithmus, ist besonders nützlich für die Erstellung effizienter Datensicherungen? Bitte antworten Sie auf Englisch und achten Sie auf die Groß- und Kleinschreibung.

## Quiz Answer

rsync
