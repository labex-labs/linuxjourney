---
index: 1
lang: "de"
title: "Benutzer und Gruppen"
meta_title: "Benutzer und Gruppen - Benutzerverwaltung"
meta_description: "Ein Schlüsselaspekt der Linux-Grundlagen ist das Verständnis der Benutzer- und Gruppenverwaltung. Dieser Leitfaden behandelt Linux-Benutzer und -Gruppen, den Root-Superuser und die Verwendung des sudo-Befehls für erweiterte Berechtigungen. Eine der besten Linux-Tutorial-Lektionen für Anfänger."
meta_keywords: "linux benutzer und gruppen, linux grundlagen, sudo, root benutzer, UID, GID, benutzerverwaltung, bestes linux tutorial, schnellster weg zu linux fortgeschritten"
---

## Lesson Content

In jedem Multi-User-Betriebssystem ist die Verwaltung von Benutzern und Gruppen ein fundamentales Konzept. Dies ist ein Kernbestandteil der **Grundlagen von Linux** und dient der Zugriffskontrolle und Berechtigungsverwaltung. Wenn ein Prozess ausgeführt wird, läuft er unter dem Benutzer, der ihn gestartet hat. Ebenso hängen Dateizugriff und Eigentümerschaft von Berechtigungen ab, was verhindert, dass ein Benutzer auf die privaten Dokumente eines anderen zugreift.

### Die Grundlagen von Linux-Benutzern und -Gruppen

Jeder Benutzer auf einem Linux-System erhält ein persönliches Home-Verzeichnis, das sich typischerweise unter `/home/benutzername` befindet. Dieses Verzeichnis speichert die benutzerspezifischen Dateien und Konfigurationen, obwohl der genaue Pfad zwischen verschiedenen Linux-Distributionen variieren kann.

Das System identifiziert Benutzer anhand einer Benutzer-ID (UID) und Gruppen anhand einer Gruppen-ID (GID). Während wir für Menschen lesbare Benutzernamen verwenden, verlässt sich das Betriebssystem bei allen berechtigungsbezogenen Aufgaben auf diese eindeutigen numerischen IDs. Gruppen sind im Grunde Sammlungen von Benutzern, was die Verwaltung von Berechtigungen für mehrere Konten gleichzeitig vereinfacht.

### Der Superuser und der Sudo-Befehl

Innerhalb der Hierarchie der **Linux-Benutzer und -Gruppen** steht ein Benutzer über allen anderen: `root`, auch bekannt als der Superuser. Der `root`-Benutzer verfügt über unbegrenzte Macht und kann auf jede Datei zugreifen und jeden Prozess verwalten. Die kontinuierliche Arbeit als `root` ist riskant, da ein einfacher Fehler das System beschädigen könnte.

Um dieses Risiko zu mindern, können autorisierte Benutzer Befehle mit Root-Rechten mithilfe des Befehls `sudo` (superuser do) ausführen. Dies ermöglicht administrative Aufgaben, ohne sich als `root`-Benutzer anmelden zu müssen. Das Verständnis, wie man `sudo` korrekt verwendet, ist unerlässlich für jeden, der die `schnellste Methode für fortgeschrittene Linux`-Kenntnisse anstrebt.

Versuchen wir, eine geschützte Datei wie `/etc/shadow` anzuzeigen, die die verschlüsselten Benutzerpasswörter speichert.

```bash
cat /etc/shadow
```

Sie erhalten eine Fehlermeldung „Permission denied“ (Zugriff verweigert). Untersuchen wir nun die Berechtigungen der Datei:

```bash
$ ls -la /etc/shadow

-rw-r----- 1 root shadow 1134 Dec 1 11:45 /etc/shadow
```

Obwohl wir Berechtigungen später im Detail behandeln werden, zeigt diese Ausgabe, dass nur der `root`-Benutzer und Mitglieder der Gruppe `shadow` diese Datei lesen dürfen. Führen Sie den Befehl nun erneut mit `sudo` aus:

```bash
sudo cat /etc/shadow
```

Dieses Mal werden Sie zur Eingabe Ihres Passworts aufgefordert, und nach erfolgreicher Authentifizierung wird der Inhalt der Datei angezeigt.

## Exercise

Während es viele Apps zum Erlernen von Linux gibt, ist praktische Übung unerlässlich. Hier sind einige Labs, um Ihr Verständnis von Linux-Benutzern, Gruppen und `sudo` zu festigen:

1. **[Linux-Benutzerkonten mit useradd, usermod und userdel verwalten](https://labex.io/de/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - Üben Sie den gesamten Lebenszyklus der Benutzeradministration, vom Erstellen und Sichern neuer Konten bis hin zum Ändern und Löschen dieser.
2. **[Linux-Gruppen mit groupadd, usermod und groupdel verwalten](https://labex.io/de/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - Sammeln Sie praktische Erfahrungen mit den zentralen Befehlszeilenprogrammen für die Gruppenadministration, einschließlich der Erstellung neuer Gruppen, der Änderung von Benutzerzuordnungen und der Entfernung von Gruppen.
3. **[Benutzerkonten und Sudo-Berechtigungen in Linux konfigurieren](https://labex.io/de/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Lernen Sie wesentliche Techniken zur Verwaltung von Benutzerkonten und `sudo`-Berechtigungen kennen, um die Sicherheit eines Linux-Systems zu erhöhen, einschließlich der Gewährung administrativer Berechtigungen.

Diese Labs helfen Ihnen, die Konzepte der Benutzer- und Gruppenverwaltung sowie die Verwendung von `sudo` in realen Szenarien anzuwenden und Vertrauen in die Linux-Systemadministration aufzubauen.

## Quiz Question

Welcher Befehl ermöglicht es Ihnen, einen einzelnen Befehl mit `root`-Berechtigungen auszuführen? (Bitte antworten Sie auf Englisch, nur in Kleinbuchstaben)

## Quiz Answer

sudo
