---
lesson_id: "power-states"
course_id: "init"
lang: "de"
order_index: 7
title: "Energiezustände"
description: "Erfahre, wie du das Herunterfahren und Neustarten von Linux planst, abbrichst und sicher überprüfst."
meta_title: "Energiezustände – Init"
meta_description: "Lerne, Energiezustände eines Linux-Systems zu verwalten. Diese Anleitung behandelt die wichtigen Befehle shutdown, reboot und halt zum sicheren Ausschalten oder Neustarten eines Linux-Systems."
meta_keywords: "Linux-Energiezustände, shutdown-Befehl, reboot-Befehl, halt-Befehl, Linux ausschalten, Linux neu starten, Linux-Systemadministration, Linux für Einsteiger, Linux-Befehle, systemd, init"
---

Das Herunterfahren oder Neustarten verändert die Verfügbarkeit des gesamten Systems. Bestätige vor dem Eingriff den Zielhost, hole eine Genehmigung ein, warne angemeldete Benutzer und stelle sicher, dass wichtige Schreibvorgänge, Sicherungen und Wartungsaufgaben abgeschlossen werden können. Bewahre auf einem entfernten System einen unabhängigen Konsolen- oder Wiederherstellungszugang, falls der Rechner nicht zurückkehrt.

## Sicher ausschalten

Fordere auf einer systemd-basierten Distribution ein geordnetes Ausschalten an mit:

```bash
$ sudo systemctl poweroff
```

Die herkömmliche `shutdown`-Schnittstelle ist ebenfalls weithin verfügbar:

```bash
$ sudo shutdown -h now
```

Ein geordnetes Herunterfahren fordert Dienste zum Stoppen auf, hängt Dateisysteme aus und ändert anschließend den Energiezustand des Rechners. Behandle einen erzwungenen Neustart oder den physischen Netzschalter nicht als gewöhnliche Abkürzung; beides kann Schreibvorgänge unterbrechen und Daten oder Dienste in einem inkonsistenten Zustand hinterlassen.

:::single-choice{#power-states-orderly-poweroff} Was solltest du tun, bevor du einen entfernten Produktionshost ausschaltest?

::option[Seine Verwaltungskonsole trennen, bevor du den Befehl ausführst.]{#power-states-remove-console explanation="Eine Verwaltungskonsole ist ein nützlicher Wiederherstellungszugang und sollte verfügbar bleiben."}
::option[Das Ausschalten erzwingen, damit Dienste den Vorgang nicht verzögern können.]{#power-states-force-first explanation="Ein erzwungener Vorgang kann Schreiboperationen unterbrechen und sollte nicht das normale Verfahren sein."}
::option[Den Host bestätigen und einen Wiederherstellungszugang bewahren.]{#power-states-confirm-and-recover .correct explanation="Die Bestätigung des Ziels verhindert Eingriffe am falschen Host; der Wiederherstellungszugang hilft, falls er nicht zurückkehrt."}
:::

## Herunterfahren planen und abbrechen

Gib Benutzern und Arbeitslasten Zeit zur Vorbereitung, indem du den Vorgang planst. Die Form `+m` bezeichnet eine Anzahl von Minuten ab jetzt:

```bash
$ sudo shutdown -h +4
```

Dies plant ein Anhalten oder Ausschalten in vier Minuten und sendet Warnungen an angemeldete Benutzer. Wird die Wartung verschoben, brich das anstehende Herunterfahren vor Ablauf der Frist ab:

```bash
$ sudo shutdown -c
```

Nimm nicht an, dass eine Warnung den Vorgang sicher macht. Prüfe aktive Sitzungen und systemspezifische Arbeitslasten und befolge das dokumentierte Verfahren zum Leeren des Dienstes oder Clusters, sofern eines existiert.

:::single-choice{#power-states-four-minute-schedule} Welcher Befehl plant das Herunterfahren in vier Minuten?

::option[`sudo shutdown -h +4`]{#power-states-relative-four .correct explanation="Die Aktion `-h` zusammen mit `+4` fordert das Herunterfahren in vier Minuten an."}
::option[`sudo shutdown -h 4`]{#power-states-absolute-four explanation="Ohne das Pluszeichen ist das Zeitargument nicht die dokumentierte Form für relative Minuten."}
::option[`sudo shutdown -c +4`]{#power-states-cancel-four explanation="Die Option `-c` bricht ein anstehendes Herunterfahren ab, statt eines zu planen."}
:::

## Das System neu starten

Verwende einen geordneten Neustart, wenn der Rechner stoppen und erneut starten muss:

```bash
$ sudo systemctl reboot
```

Gleichwertige Kompatibilitätsbefehle sind häufig:

```bash
$ sudo shutdown -r now
$ sudo reboot
```

Prüfe vor dem Neustart, ob verschlüsselte Datenträger, Bootkonfiguration, Netzwerk und erforderliche Dienste ohne die aktuelle interaktive Sitzung wiederhergestellt werden können. Koordiniere zuerst Failover oder die Verlagerung von Arbeitslasten, wenn andere Systeme vom Host abhängen.

:::single-choice{#power-states-reboot-action} Welcher Befehl fordert über `shutdown` einen sofortigen geordneten Neustart an?

::option[`sudo shutdown -c now`]{#power-states-cancel-now explanation="Die Option `-c` bricht ein anstehendes Herunterfahren ab."}
::option[`sudo shutdown -r now`]{#power-states-reboot-now .correct explanation="Die Option `-r` wählt den Neustart, und `now` plant ihn sofort."}
::option[`sudo shutdown -h now`]{#power-states-halt-now explanation="Die Aktion `-h` hält an oder schaltet aus, statt neu zu starten."}
:::

## Anhalten und Ausschalten unterscheiden

`halt`, `poweroff` und `reboot` können Kompatibilitäts-Frontends für das init-System sein, ihre angeforderten Endzustände unterscheiden sich jedoch. Anhalten beendet den normalen Systembetrieb; abhängig von Plattform und Implementierung kann die Stromversorgung bestehen bleiben. Ausschalten fordert zusätzlich an, dass unterstützte Hardware die Stromversorgung beendet. Bevorzuge den Befehl, der das beabsichtigte Ergebnis benennt, und lies das lokale Handbuch, da das Kompatibilitätsverhalten abweichen kann.

:::single-choice{#power-states-halt-versus-poweroff} Warum solltest du `halt` und `poweroff` unterscheiden?

::option[Power-off fordert das Abschalten der Stromversorgung an, während sie bei Halt bestehen bleiben kann.]{#power-states-power-distinction .correct explanation="Der angeforderte abschließende Hardwarezustand kann sich unterscheiden, obwohl beide den normalen Betrieb beenden."}
::option[Halt startet Dienste nach dem Stoppen immer neu.]{#power-states-halt-restarts explanation="Halt ist ein Stoppzustand und keine Anforderung zum Neustart von Diensten."}
::option[Power-off meldet nur den aktuellen Terminalbenutzer ab.]{#power-states-power-logout explanation="Power-off ist ein systemweiter Zustandsübergang und keine Shell-Abmeldung."}
:::

## Das Ergebnis überprüfen

Bestätige bei einem geplanten Vorgang, dass Benutzer benachrichtigt wurden und kritische Arbeit abgeschlossen ist. Prüfe nach einem Neustart den erwarteten Kernel- und Bootzustand, fehlgeschlagene Units, die Anwendungsfunktion, eingehängte Speicher, die Netzwerkerreichbarkeit und aktuelle Bootprotokolle. Eine erfolgreiche Anmeldung allein beweist nicht, dass der gesamte Dienst wiederhergestellt ist.

```bash
$ uptime
$ systemctl --failed
$ journalctl -b -p warning
```

Dies sind Ausgangspunkte; verwende für die tatsächliche Arbeitslast anwendungseigene Zustandsprüfungen.

:::single-choice{#power-states-post-reboot-check} Was liefert den stärksten Beleg dafür, dass eine neu gestartete Anwendung bereit ist?

::option[Dienstzustand, Protokolle und ihre Zustandsprüfung sind alle erfolgreich.]{#power-states-health-evidence .correct explanation="Mehrere System- und Anwendungsprüfungen bestätigen die Arbeitslast und nicht nur den Hostzugang."}
::option[Die Betriebsanzeige am Gehäuse leuchtet.]{#power-states-light-on explanation="Die Stromversorgung der Hardware belegt nicht den Zustand der Anwendung."}
::option[Ein Administrator kann sich an einer Shell anmelden.]{#power-states-shell-open explanation="Shellzugang belegt nur einen Teil der Systemverfügbarkeit."}
:::

## Zusammenfassung

Du kannst Linux-Energiezustände nun mit Vorbereitung, eindeutiger Absicht und Überprüfung ändern.

1. Bestätige Ziel, Auswirkungen, Genehmigung und Wiederherstellungszugang.
2. Verwende für den normalen Betrieb geordnete Befehle zum Ausschalten oder Neustarten.
3. Plane das Herunterfahren, wenn Benutzer und Arbeitslasten eine Warnung benötigen.
4. Brich ein anstehendes Herunterfahren ab, wenn sich der Wartungsplan ändert.
5. Prüfe den Zustand von System und Anwendung, nachdem der Rechner zurückgekehrt ist.
