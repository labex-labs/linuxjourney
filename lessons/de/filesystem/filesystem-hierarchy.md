---
lesson_id: "filesystem-hierarchy"
course_id: "filesystem"
lang: "de"
order_index: 1
title: "Dateisystemhierarchie"
description: "Lerne die vorgesehenen Aufgaben wichtiger Linux-Verzeichnisse kennen und erfahre, wie moderne zusammengeführte Strukturen abweichen können."
meta_title: "Dateisystemhierarchie – Das Dateisystem"
meta_description: "Erkunde die Linux-Dateisystemhierarchie und die Rollen wichtiger Verzeichnisse wie /etc, /usr, /home, /var, /dev, /proc und /sys."
meta_keywords: "Linux Dateisystemhierarchie, Dateisystemhierarchie Linux, Linux Verzeichnisstruktur, FHS, Linux Dateihierarchie"
---

Linux stellt eingehängte Dateisysteme als einen einzigen Verzeichnisbaum mit der Wurzel `/` dar. Der Filesystem Hierarchy Standard (FHS) weist vielen Verzeichnissen herkömmliche Aufgaben zu. Distributionen, Container, unveränderliche Systeme und lokale Richtlinien können jedoch abweichen. Prüfe den tatsächlichen Host, bevor du dich auf einen Pfad verlässt.

```bash
$ ls -ld /*
```

## Wurzel und grundlegende Systempfade

- `/` ist die Wurzel des sichtbaren Dateisystembaums.
- `/etc` enthält hostspezifische Systemkonfiguration. Dort können ausführbare Hilfs- oder Startskripte liegen; die Aussage, das Verzeichnis enthalte niemals ausführbare Inhalte, wäre daher falsch.
- `/boot` enthält bootbezogene Dateien wie Bootloader-Daten und auf vielen Systemen Kernel sowie Abbilder des initialen RAM-Dateisystems.
- `/bin` und `/sbin` enthalten traditionell grundlegende Benutzer- und Systemverwaltungsbefehle.
- `/lib` und architekturspezifische Varianten enthalten traditionell grundlegende gemeinsam genutzte Bibliotheken und Loader-Komponenten.

Viele aktuelle Distributionen verwenden eine zusammengeführte `/usr`-Struktur, in der `/bin`, `/sbin` und `/lib` symbolische Links auf entsprechende Verzeichnisse unter `/usr` sind. Nutze die Befehlssuche und Paketdaten, statt anzunehmen, ob ein Pfad ein physisches Verzeichnis oder ein Link ist.

:::single-choice{#filesystem-hierarchy-configuration-directory}
Welches Verzeichnis enthält herkömmlicherweise hostspezifische Systemkonfiguration?

::option[`/proc`]{#filesystem-hierarchy-proc-config explanation="Procfs stellt aktive Prozess- und Kernel-Schnittstellen statt dauerhafter Hostkonfigurationsdateien bereit."}
::option[`/etc`]{#filesystem-hierarchy-etc .correct explanation="System- und Dienstkonfiguration ist herkömmlicherweise unter `/etc` organisiert."}
::option[`/dev`]{#filesystem-hierarchy-dev-config explanation="`/dev` enthält laufzeitbezogene, geräteseitige Objekte und nicht die allgemeine Konfigurationshierarchie."}
:::

## Distributions- und lokale Software

- `/usr` enthält die hauptsächliche gemeinsam nutzbare, weitgehend schreibgeschützte Hierarchie des Betriebssystems und der Anwendungen einschließlich Befehlen, Bibliotheken und architekturunabhängigen Daten.
- `/usr/local` ist für Software und Daten reserviert, die der lokale Administrator außerhalb der normalen `/usr`-Verwaltung der Distribution installiert.
- `/opt` kann zusätzliche Anwendungspakete in eigenständigen Unterbäumen enthalten.

Trotz seines Namens ist `/usr` normalerweise nicht der Ort für persönliche Dateien einzelner Benutzer. Paketmanager der Distribution verwalten große Teile des Verzeichnisses. Das Kopieren lokal kompilierter Dateien nach `/usr/bin` kann daher mit verwalteten Paketen in Konflikt geraten.

:::single-choice{#filesystem-hierarchy-local-software}
Welches Präfix ist herkömmlicherweise für lokal installierte Software außerhalb des distributionsverwalteten `/usr`-Inhalts reserviert?

::option[`/usr/local`]{#filesystem-hierarchy-usr-local .correct explanation="Die lokale Hierarchie trennt vom Administrator installierte Software vom hauptsächlichen `/usr`-Baum der Distribution."}
::option[`/proc/local`]{#filesystem-hierarchy-proc-local explanation="Procfs ist eine virtuelle Kernel-Schnittstelle und kein dauerhafter Softwarepräfix."}
::option[`/dev/local`]{#filesystem-hierarchy-dev-local explanation="Der Speicherort für Geräteknoten ist nicht der herkömmliche Platz für lokale Anwendungen."}
:::

## Benutzer- und Dienstdaten

- `/home` enthält herkömmlicherweise die Home-Verzeichnisse nicht privilegierter Benutzer; Verzeichnisdienste und lokale Richtlinien können sie jedoch anderswo platzieren.
- `/root` ist das herkömmliche Home-Verzeichnis des Root-Kontos.
- `/srv` ist für standortspezifische Daten vorgesehen, die dieses System bereitstellt.

Ein Home-Pfad stammt aus Kontoinformationen und nicht nur aus der Verbindung von `/home` mit einem Benutzernamen. Verwende `getent passwd USER` oder das von der Shell aufgelöste Home-Verzeichnis, statt Annahmen fest einzucodieren.

:::single-choice{#filesystem-hierarchy-root-home}
Was ist das herkömmliche Home-Verzeichnis des Root-Kontos?

::option[`/home/root`]{#filesystem-hierarchy-home-root explanation="Gewöhnliche Home-Verzeichnisse liegen häufig unter `/home`, doch root besitzt einen eigenen herkömmlichen Pfad."}
::option[`/root`]{#filesystem-hierarchy-root .correct explanation="Das Home-Verzeichnis des privilegierten Kontos liegt herkömmlicherweise direkt unter der Dateisystemwurzel."}
::option[`/usr/root`]{#filesystem-hierarchy-usr-root explanation="`/usr` ist die Hierarchie für Software und gemeinsame Daten und nicht das Home-Verzeichnis von root."}
:::

## Veränderliche, Laufzeit- und temporäre Daten

- `/var` enthält veränderliche Daten wie Protokolle, Caches, Spools und Anwendungszustand. Systemprotokolle liegen häufig unter `/var/log`, auch wenn manche Systeme hauptsächlich eine Journal-Schnittstelle verwenden.
- `/run` enthält flüchtigen Laufzeitzustand des aktuellen Systemstarts, etwa Sockets, Dienstzustand und PID-Dateien. Es wird normalerweise beim Start neu erstellt.
- `/tmp` ist für temporäre Dateien vorgesehen und üblicherweise mit Sticky-Bit-Schutz für alle Benutzer beschreibbar.
- `/var/tmp` ist für temporäre Dateien gedacht, die länger als Dateien in `/tmp` bestehen bleiben sollen.

Die Bereinigungsrichtlinie für `/tmp` unterscheidet sich. Gehe weder davon aus, dass Dateien bis zum Neustart bestehen bleiben, noch dass sie beim Neustart immer gelöscht werden. Anwendungen sollten temporäre Dateien sicher erzeugen und keine vorhersehbaren Namen verwenden.

:::single-choice{#filesystem-hierarchy-log-path}
Welcher Pfad speichert herkömmlicherweise Systemprotokolldateien?

::option[`/etc/log`]{#filesystem-hierarchy-etc-log explanation="`/etc` ist für Konfiguration und nicht für gewöhnliche anwachsende Protokolldaten vorgesehen."}
::option[`/var/log`]{#filesystem-hierarchy-var-log .correct explanation="Protokolle gehören zu den sich verändernden Systemdaten unter der Hierarchie für variable Daten."}
::option[`/boot/log`]{#filesystem-hierarchy-boot-log explanation="`/boot` ist für bootbezogene Artefakte und nicht für allgemeine Dienstprotokolle reserviert."}
:::

## Geräte, Kernel-Schnittstellen und Einhängepunkte

- `/dev` enthält Geräteknoten und zugehörige Laufzeitlinks.
- `/proc` stellt über procfs Prozess- und Kernel-Schnittstellen bereit.
- `/sys` stellt über sysfs Kernel-Objekte, Geräte, Treiber und Attribute bereit.
- `/media` wird häufig für automatisch eingehängte Wechselmedien verwendet.
- `/mnt` ist ein herkömmlicher Ort für vorübergehende Einhängungen durch Administratoren.

Dies sind Konventionen und keine Berechtigungsgewährungen. Das Einhängen eines anderen Dateisystems auf einem nicht leeren Verzeichnis verbirgt dessen bisherigen Inhalt vorübergehend bis zum Aushängen.

:::single-choice{#filesystem-hierarchy-sysfs-path}
Welcher Pfad stellt normalerweise das Kernel-Gerätemodell über sysfs bereit?

::option[`/srv`]{#filesystem-hierarchy-srv explanation="`/srv` ist für vom System bereitgestellte Daten vorgesehen."}
::option[`/sys`]{#filesystem-hierarchy-sys .correct explanation="Sysfs wird herkömmlicherweise unter `/sys` eingehängt und stellt Geräte, Treiber, Busse und Attribute dar."}
::option[`/opt`]{#filesystem-hierarchy-opt explanation="`/opt` enthält optionale zusätzliche Anwendungsbäume."}
:::

Nutze das Lab [Im Linux-Dateisystem navigieren](https://labex.io/labs/comptia-navigate-the-filesystem-in-linux-590971), um diese Pfade zu untersuchen, und [Dateien und Befehle unter Linux finden](https://labex.io/labs/comptia-find-files-and-commands-in-linux-590834), damit du dich nicht auf geratene Speicherorte verlässt.

## Zusammenfassung

Du kannst wichtige Linux-Pfade nun ihren vorgesehenen Aufgaben zuordnen und dabei echte Systemunterschiede berücksichtigen.

1. Beginne beim einheitlichen Baum mit der Wurzel `/`.
2. Trenne Konfiguration, verwaltete Software, lokale Software und veränderliche Daten.
3. Unterscheide Home- und Dienstdaten von Laufzeitzustand.
4. Erkenne `/dev`, `/proc` und `/sys` als besondere Laufzeitschnittstellen.
5. Prüfe symbolische Links, Einhängungen, Kontodaten und Distributionsrichtlinien, bevor du eine Struktur voraussetzt.
