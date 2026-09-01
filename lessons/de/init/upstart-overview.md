---
lesson_id: "upstart-overview"
course_id: "init"
lang: "de"
order_index: 3
title: "Überblick über Upstart"
description: "Erfahre, wie das ältere init-System Upstart Ereignisausdrücke mit Zielen des Joblebenszyklus verbindet."
meta_title: "Überblick über Upstart – Init"
meta_description: "Lerne Upstart, sein ereignisgesteuertes Modell und seine Verwaltung von Diensten unter Linux kennen. Verstehe Upstart-Jobkonfigurationen und seine Rolle als init-System."
meta_keywords: "Upstart, init-System, Linux-Dienste, Ubuntu, SysV, Tutorial für Einsteiger, Linux-Leitfaden"
---

Upstart ist ein älteres ereignisbasiertes init- und Dienstverwaltungssystem, das von Canonical entwickelt wurde. Ältere Ubuntu-Versionen und mehrere andere Distributionen verwendeten es, doch aktuelle Ubuntu-Veröffentlichungen verwenden systemd. Beschäftige dich mit Upstart zur Pflege eines bestätigten älteren Hosts und nicht als Standardannahme für eine moderne Installation.

## Einen älteren Upstart-Host bestätigen

Prüfe PID 1 und die aktive Steuerungsschnittstelle:

```bash
$ ps -p 1 -o pid,comm,args=
$ readlink /proc/1/exe
$ initctl version
```

Der letzte Befehl ist nur dort aussagekräftig erfolgreich, wo Upstarts Steuerungsdienst und Client vorhanden sind. Ein Verzeichnis wie `/usr/share/upstart` oder übrig gebliebene Dateien unter `/etc/init` sind schwache Belege, da Pakete und Migrationsreste bestehen bleiben können, nachdem ein anderes init-System übernommen hat.

:::single-choice{#upstart-overview-active-evidence} Was ist der stärkste Beleg dafür, dass ein Host tatsächlich Upstart verwendet?

::option[Ein Verzeichnisname enthält das Wort `upstart`.]{#upstart-overview-directory-only explanation="Installierte Dokumentation oder Überreste können auf einem System verbleiben, das ein anderes init verwendet."}
::option[Das System besitzt mindestens ein Shell-Skript.]{#upstart-overview-shell-script explanation="Shell-Skripte sind in allen init-Umgebungen verbreitet."}
::option[PID 1 und die aktive `initctl`-Schnittstelle weisen Upstart aus.]{#upstart-overview-live-interface .correct explanation="Laufzeitbelege aus Prozess und Steuerung sind stärker als das Vorhandensein älterer Dateien."}
:::

## Jobs und Ereignisse

Ein Upstart-**Job** beschreibt einen Dienst oder eine Aufgabe einschließlich seiner Prozessbefehle und Lebenszyklusbedingungen. Ein **Ereignis** ist eine benannte Benachrichtigung mit optionalen Umgebungsvariablen. Die Jobkonfiguration kann ausdrücken, wann ihr Ziel auf Start oder Stopp wechseln soll.

Systemweite Jobdateien befinden sich gewöhnlich mit der Endung `.conf` unter `/etc/init/`. Zum Beispiel:

```text
description "Example worker"
start on runlevel [2345]
stop on runlevel [016]
exec /usr/local/sbin/example-worker
```

Dies verwendet Runlevel-Ereignisse als Kompatibilitätseingaben. Upstart kann abhängig davon, welche Ereignisse das System ausgibt, außerdem auf Dateisystem-, Geräte-, Netzwerk- oder anwendungsdefinierte Ereignisse reagieren.

:::single-choice{#upstart-overview-start-on} Was definiert ein Upstart-Abschnitt `start on`?

::option[Die Kernelversion, die als Nächstes kompiliert werden muss.]{#upstart-overview-kernel-version explanation="Ereignisbedingungen eines Jobs wählen keinen Kernel-Build aus."}
::option[Den Ereignisausdruck, der das Ziel des Jobs in Richtung Start ändert.]{#upstart-overview-start-condition .correct explanation="Wenn der Ausdruck erfüllt ist, versucht Upstart den konfigurierten Startübergang des Jobs."}
::option[Die Datenträgerpartition, auf der jeder Job Daten speichert.]{#upstart-overview-partition explanation="Der Speicherort hat nichts mit der Upstart-Ereignissyntax zu tun."}
:::

## Ereignisgesteuerter Start

Während des Systemstarts lädt Upstart Jobdefinitionen und empfängt Ereignisse. Zutreffende Ausdrücke `start on` oder `stop on` aktualisieren Jobziele; Jobübergänge können zusätzliche Ereignisse ausgeben, die weitere Arbeit freigeben. Unabhängige Jobs können gleichzeitig fortschreiten.

Dieses Modell vermeidet eine einzige fest codierte globale Skriptreihenfolge, kann aber schwer zu diagnostizieren sein, wenn Ereignisnamen, Reihenfolge und Bedingungen implizit sind. Ereignisse sind standardmäßig keine dauerhafte Nachrichtenwarteschlange. Ein später hinzugefügter Job oder eine nachträglich geänderte Bedingung sollte daher nicht annehmen, dass jedes frühere Ereignis wiederholt wird.

:::single-choice{#upstart-overview-event-chain} Wie kann ein Upstart-Job dazu führen, dass ein anderer Job startet?

::option[Er schreibt die ausführbare Binärdatei des anderen Jobs im Speicher um.]{#upstart-overview-rewrite-binary explanation="Die Koordination erfolgt über Ereignisse und nicht durch Codeänderung."}
::option[Jeder Job startet immer streng in Dateinamenreihenfolge.]{#upstart-overview-filename-order explanation="Upstart verwendet Ereignisausdrücke statt einer einzigen nach Dateinamen sortierten Startliste."}
::option[Sein Übergang kann ein Ereignis ausgeben, auf das ein anderer Job passt.]{#upstart-overview-emitted-event .correct explanation="Ereignisausdrücke verbinden ansonsten unabhängige Übergänge im Joblebenszyklus."}
:::

## Migration und Kompatibilität

Systemd kann eine begrenzte Kompatibilität für einige ältere Dienstskripte bereitstellen, führt die Upstart-Jobsyntax aber nicht als native systemd-Units aus. Übertrage bei einer Migration Lebenszyklusbedingungen, Umgebung, Respawn-Richtlinie, Protokollierung, Abhängigkeiten und Bereitschaftssemantik, statt Dateien mechanisch umzubenennen.

:::single-choice{#upstart-overview-current-ubuntu} Welches init-System verwenden aktuelle Ubuntu-Standardveröffentlichungen?

::option[Ausschließlich Upstart auf jeder Installation.]{#upstart-overview-current-upstart explanation="Dies galt nur für historische Veröffentlichungszeiträume und Konfigurationen."}
::option[systemd.]{#upstart-overview-current-systemd .correct explanation="Upstart gehört zu älteren Ubuntu-Generationen; aktuelle Veröffentlichungen verwenden systemd als PID 1."}
::option[Überhaupt keinen init-Prozess.]{#upstart-overview-no-init explanation="Ein vollständiges Ubuntu-System benötigt weiterhin einen Dienstmanager als PID 1."}
:::

## Zusammenfassung

Du kannst Upstart nun als älteres Ereignis- und Jobmodell lesen.

1. Bestätige die aktive PID 1 und Steuerungsschnittstelle.
2. Unterscheide Jobdefinitionen von Ereignisbenachrichtigungen.
3. Interpretiere `start on` und `stop on` als Lebenszyklusausdrücke.
4. Migriere Semantik ausdrücklich, statt Konfigurationsdateien umzubenennen.
