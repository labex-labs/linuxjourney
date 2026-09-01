---
lesson_id: "systemd-overview"
course_id: "init"
lang: "de"
order_index: 5
title: "Überblick über systemd"
description: "Erfahre, wie systemd Units lädt, Abhängigkeiten auflöst, Targets aktiviert und System- sowie Benutzerressourcen verwaltet."
meta_title: "Überblick über systemd – Init"
meta_description: "Lerne die Grundlagen des init-Systems systemd kennen. Diese Anleitung zeigt, wie systemd Units und Targets verwendet, um den Linux-Bootvorgang und Systemdienste zu verwalten."
meta_keywords: "systemd, system d, init-System, systemd-Units, systemd-Targets, Linux-Bootvorgang, Linux-Dienste, Systemverwaltung, Einsteiger, Tutorial"
---

Systemd ist der von vielen aktuellen Linux-Distributionen verwendete init- und Dienstmanager mit PID 1. Das systemd-Projekt stellt außerdem Komponenten für Protokollierung, Geräte, Anmeldungen, Netzwerk, Zeit und weitere Bereiche bereit, doch Distributionen können auswählen, welche Teile sie einsetzen.

## Den laufenden Manager bestätigen

Untersuche den aktuellen Zustand statt nur das Vorhandensein installierter Verzeichnisse:

```bash
$ ps -p 1 -o pid,comm,args=
$ systemctl is-system-running
```

`/usr/lib/systemd/` kann auf einem System vorhanden sein, auf dem ein anderes Programm PID 1 ist, und ein Container kann seinen eigenen PID-Namensraum bereitstellen. `systemctl` besitzt außerdem Modi für Benutzermanager sowie entfernte Systeme und Container. Stelle deshalb fest, an welchen Manager sich eine Operation richtet.

:::single-choice{#systemd-overview-detection} Woran lässt sich systemd am unmittelbarsten als init-Manager des Systems erkennen?

::option[Ein Verzeichnis namens `/usr/lib/systemd` ist vorhanden.]{#systemd-overview-directory explanation="Bibliotheken und Unit-Dateien können installiert bleiben, ohne dass systemd als PID 1 arbeitet."}
::option[Ein Benutzer hat einen Befehl namens `systemctl` ausgeführt.]{#systemd-overview-command-executed explanation="Ein Clientprogramm kann vorhanden sein, obwohl kein systemweiter systemd-Manager verfügbar ist."}
::option[PID 1 des Hosts ist systemd.]{#systemd-overview-pid-one .correct explanation="Der laufende erste Prozess ist ein stärkerer Beleg als installierte Dateien oder Paketnamen."}
:::

## Units als verwaltete Objekte

Eine Unit ist das benannte Modell von systemd für eine Ressource oder Aktivität. Häufige Unit-Typen sind:

- `.service` für Prozesse und Daemons
- `.socket` für Socket-Aktivierung
- `.mount` und `.automount` für Dateisysteme
- `.timer` und `.path` für ereignisgesteuerte Aktivierung
- `.target` für Gruppierung und Synchronisierung
- `.device`, `.swap`, `.slice` und `.scope` für weitere verwaltete Ressourcen

Der Zustand einer Unit ist nicht immer „running“. Ein Mount kann eingehängt sein, ein Timer warten, ein Gerät vorhanden und ein Target aktiv sein, nachdem seine Abhängigkeiten erreicht wurden.

:::single-choice{#systemd-overview-group-unit} Welcher Unit-Typ gruppiert üblicherweise andere Units und stellt einen Synchronisierungspunkt bereit?

::option[`.socket`]{#systemd-overview-socket explanation="Socket-Units stellen IPC- oder Netzwerkendpunkte bereit und können Dienste aktivieren."}
::option[`.target`]{#systemd-overview-target .correct explanation="Target-Units fassen Abhängigkeiten zusammen und stellen Meilensteine des Bootvorgangs oder Betriebs dar."}
::option[`.timer`]{#systemd-overview-timer explanation="Timer-Units planen Aktivierungen nach Kalenderzeit oder monotoner Zeit."}
:::

## Ladepfade und Überschreibungen für Units

System-Units können aus Distributions- und Administratorpfaden geladen werden, zum Beispiel:

- `/usr/lib/systemd/system/` für von Paketen bereitgestellte Units auf vielen Distributionen
- `/run/systemd/system/` für zur Laufzeit erzeugte oder transiente Konfiguration
- `/etc/systemd/system/` für dauerhafte lokale Administratorkonfiguration und Überschreibungen

Die genauen Anbieterpfade können abweichen. Lokale Konfiguration mit höherer Priorität überschreibt Dateien gleichen Unit-Namens mit niedrigerer Priorität. Bevorzuge mit `systemctl edit UNIT` erstellte Drop-in-Überschreibungen, statt eine vollständige Anbieterdatei zu kopieren und zu verändern, damit Paketaktualisierungen sichtbar bleiben.

:::single-choice{#systemd-overview-local-override} Wo sollten dauerhafte lokale Überschreibungen für System-Units normalerweise liegen?

::option[Innerhalb von `/proc/systemd/`.]{#systemd-overview-proc-systemd explanation="Procfs ist eine Kernel-Laufzeitschnittstelle und kein Speicherort für dauerhafte Unit-Konfiguration."}
::option[Unter `/etc/systemd/system/`.]{#systemd-overview-etc-system .correct explanation="Die Administratorkonfiguration hat Vorrang vor den mit Paketen gelieferten Anbieter-Units."}
::option[In den Bootcode-Bytes des MBR auf dem Datenträger.]{#systemd-overview-mbr-units explanation="Dienst-Units sind Konfigurationsdateien im Userspace."}
:::

## Abhängigkeiten und Reihenfolge

Systemd erstellt aus Abhängigkeitsbeziehungen eine Transaktion. `Wants=` und `Requires=` nehmen andere Units mit unterschiedlicher Bindungsstärke in eine Transaktion auf. `Before=` und `After=` legen die Reihenfolge fest, wenn beide Units eingeplant sind; allein bewirken sie nicht, dass eine andere Unit startet.

Eine Zeile `After=network.target` beweist nicht, dass eine nutzbare Verbindung, DNS oder ein bestimmter entfernter Endpunkt bereit ist. Dienste müssen die geeignete Network-online-Integration verwenden oder eigene Wiederholungs- und Bereitschaftsmechanismen implementieren.

:::single-choice{#systemd-overview-after-semantics} Was legt `After=other.service` für sich allein fest?

::option[Eine Garantie, dass der Anwendungsendpunkt des anderen Dienstes fehlerfrei ist.]{#systemd-overview-after-health explanation="Abschluss der Reihenfolge und Anwendungsbereitschaft sind unterschiedliche Konzepte."}
::option[Die Reihenfolge, falls beide Units Teil der Transaktion sind.]{#systemd-overview-after-ordering .correct explanation="Eine separate Anforderung wie Wants oder Requires ist nötig, um die andere Unit in die Transaktion aufzunehmen."}
::option[Die automatische Aktivierung beider Units bei jedem künftigen Bootvorgang.]{#systemd-overview-after-enable explanation="Die Aktivierung ist Installationsmetadaten und wird nicht durch eine Reihenfolgebeziehung impliziert."}
:::

## Targets und die standardmäßige Boottransaktion

`default.target` ist gewöhnlich ein Alias auf ein Target wie `multi-user.target` oder `graphical.target`. Systemd startet eine Transaktion für dieses Target und seine Abhängigkeiten. Dabei kann nicht zusammenhängende Arbeit gleichzeitig fortschreiten, während ausdrückliche Reihenfolgen eingehalten werden.

Targets ähneln Runlevels nur auf einer groben Kompatibilitätsebene. Mehrere Targets können gleichzeitig aktiv sein, eigene Targets können erstellt werden, und die Aktivität eines Targets bedeutet nicht, dass jeder Dienst des Rechners fehlerfrei ist.

:::single-choice{#systemd-overview-default-target} Was wählt `default.target` normalerweise aus?

::option[Das Standardblockgerät, das `mkfs` löschen soll.]{#systemd-overview-default-disk explanation="Targets beschreiben Unit-Aktivierung und keine destruktive Auswahl von Datenträgern."}
::option[Das einzige Target, das jemals aktiv sein kann.]{#systemd-overview-only-target explanation="Targets sind Gruppierungen, und während eines Bootvorgangs können viele davon aktiv sein."}
::option[Die Target-Transaktion für einen normalen Systemstart.]{#systemd-overview-normal-boot .correct explanation="Es ist gewöhnlich ein Alias auf das vom Administrator ausgewählte Multiuser- oder grafische Boot-Target."}
:::

## Zusammenfassung

Du kannst systemd nun anhand von laufenden Managern, Units und Transaktionen beschreiben.

1. Bestätige systemd über die betreffende PID 1 und Managerverbindung.
2. Ordne Ressourcentypen den Unit-Endungen zu.
3. Platziere lokale Überschreibungen oberhalb der Anbieterkonfiguration.
4. Trenne Abhängigkeitsstärke, Reihenfolge und Anwendungsbereitschaft.
5. Behandle Targets als Gruppierungen und Meilensteine statt als exklusive Zustände.
