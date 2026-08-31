---
lesson_id: "users-and-groups"
course_id: "user-management"
lang: "de"
order_index: 1
title: "Benutzer und Gruppen"
description: "Erfahre, wie Linux Benutzer und Gruppen identifiziert und wie Prozesszugangsdaten Zugriffsentscheidungen beeinflussen."
meta_title: "Benutzer und Gruppen – Benutzerverwaltung"
meta_description: "Ein wichtiger Teil der Linux-Grundlagen ist das Verständnis der Benutzer- und Gruppenverwaltung. Dieser Leitfaden behandelt Linux-Benutzer und -Gruppen, den Superuser root und den Befehl sudo für erhöhte Berechtigungen. Eine der besten Linux-Tutorial-Lektionen für Einsteiger."
meta_keywords: "Linux-Benutzer und -Gruppen, Linux-Grundlagen, sudo, root-Benutzer, UID, GID, Benutzerverwaltung, bestes Linux-Tutorial, schnellster Weg zu fortgeschrittenem Linux"
---

Linux verwendet Benutzer- und Gruppenidentitäten, um Prozesse zu kennzeichnen, Eigentümer von Dateisystemobjekten festzulegen und Entscheidungen zur Zugriffskontrolle zu treffen. Menschenlesbare Namen helfen Administratoren, während der Kernel hauptsächlich mit numerischen Kennungen und Prozesszugangsdaten arbeitet.

## Benutzer anhand von UIDs identifizieren

Jedes Konto besitzt eine numerische Benutzerkennung oder **UID**. Benutzernamen werden über die Kontodatenbanken des Systems UIDs zugeordnet. Dateien speichern numerische Eigentümerangaben, die Werkzeuge gewöhnlich als den zugehörigen Namen anzeigen.

Führe `id` aus, um Informationen zur Identität des aktuellen Prozesses anzuzeigen:

```bash
$ id
uid=1000(alice) gid=1000(alice) groups=1000(alice),27(sudo)
```

Die Werte unterscheiden sich je nach System. Menschliche Anmeldekonten besitzen häufig Home-Verzeichnisse wie `/home/alice`, doch Konten können einen anderen Pfad oder überhaupt kein gewöhnliches Home-Verzeichnis verwenden. Dienstkonten dienen oft dazu, Software unter einer eingeschränkten Identität auszuführen, und nicht der interaktiven Anmeldung.

:::single-choice{#users-uid-purpose}
Welche Kennung verwendet der Kernel hauptsächlich, um eine Benutzeridentität darzustellen?

::option[Den Pfad eines Home-Verzeichnisses]{#users-home-path explanation="Ein Home-Pfad gehört zur Kontokonfiguration und kann variieren oder fehlen; er ist nicht die Benutzerkennung des Kernels."}
::option[Eine numerische UID]{#users-numeric-uid .correct explanation="Kontodatenbanken ordnen Namen numerischen UIDs zu, die in Prozesszugangsdaten und Eigentumsangaben verwendet werden."}
::option[Die Nummer eines Terminalfensters]{#users-terminal-number explanation="Terminalgeräte und Sitzungen sind von numerischen Benutzeridentitäten getrennt."}
:::

## Zugriff mit Gruppen organisieren

Eine Gruppe besitzt eine numerische Gruppenkennung oder **GID**. Ein Konto hat gewöhnlich eine primäre Gruppe und kann zusätzlichen Gruppen angehören. Mit Gruppenmitgliedschaften können Administratoren einer Gruppe von Benutzern Zugriff gewähren, ohne Berechtigungen für jedes Konto einzeln zuzuweisen.

Überprüfe Mitgliedschaften mit:

```bash
$ id alice
$ groups alice
```

Diese Befehle geben konfigurierte oder aufgelöste Identitätsinformationen aus. Verzeichnisdienste und Zwischenspeicher können daran beteiligt sein, weshalb das direkte Lesen von `/etc/group` nicht immer die vollständigen wirksamen Mitgliedschaften zeigt.

:::single-choice{#users-primary-supplementary-groups}
Wie kann ein Linux-Konto gewöhnlich an Gruppen beteiligt sein?

::option[Es kann während seiner gesamten Lebensdauer genau einer Gruppe angehören.]{#users-single-group explanation="Linux-Prozesse können eine primäre Gruppe und zusätzlich eine Liste ergänzender Gruppen besitzen."}
::option[Es gehört jeder Gruppe an, deren Dateien es lesen kann.]{#users-readable-groups explanation="Die Lesbarkeit von Dateien ergibt sich aus Berechtigungen und Zugangsdaten; sie erzeugt nicht automatisch eine Gruppenmitgliedschaft."}
::option[Es besitzt eine primäre Gruppe und kann ergänzenden Gruppen angehören.]{#users-group-memberships .correct explanation="Die primäre GID ist Teil des Kontoeintrags, während ergänzende Mitgliedschaften zusätzliche Gruppenidentitäten bereitstellen."}
:::

## Prozesszugangsdaten verstehen

Ein Prozess besitzt Zugangsdaten wie reale und effektive UIDs und GIDs sowie ergänzende Gruppen. Die effektiven Zugangsdaten spielen bei vielen Berechtigungsprüfungen eine zentrale Rolle. Ein von einem Benutzer gestarteter Prozess übernimmt gewöhnlich die Zugangsdaten seines Elternprozesses, doch kontrollierte Mechanismen können sie ändern.

Das ist genauer als die Aussage, ein Prozess laufe immer nur „als der Benutzer, der ihn gestartet hat“. Ausführbare Dateien mit Set-User-ID, Dienstmanager, Container, Namensräume und Systemaufrufe zur Änderung von Privilegien können beeinflussen, welche Identitäten in einem bestimmten Kontext sichtbar oder wirksam sind.

:::single-choice{#users-process-access-identity}
Welche Informationen werden gewöhnlich berücksichtigt, wenn der Kernel einen Prozess anhand von Dateiberechtigungen prüft?

::option[Die effektive UID, die effektive GID und die ergänzenden Gruppen des Prozesses.]{#users-effective-credentials .correct explanation="Diese Zugangsdaten werden bei gewöhnlichen Prüfungen der frei bestimmbaren Zugriffskontrolle mit Eigentums- und Berechtigungsangaben verglichen."}
::option[Das Farbschema des Terminals, das den Prozess gestartet hat.]{#users-terminal-theme explanation="Anzeigeeinstellungen spielen bei der Prüfung von Dateisystemberechtigungen keine Rolle."}
::option[Die Länge des Benutzernamens des Kontos.]{#users-username-length explanation="Der Kernel arbeitet mit numerischen Zugangsdaten; die Länge eines Benutzernamens gewährt keinen Zugriff."}
:::

## Die root-Identität erkennen

Das traditionell `root` genannte Konto besitzt die UID 0. Viele Linux-Berechtigungsmechanismen behandeln die UID 0 besonders und verleihen ihr weitreichende administrative Macht. Modernes Linux kann Privilegien außerdem mithilfe von Capabilities, Namensräumen, verbindlicher Zugriffskontrolle und der Einschränkung von Diensten aufteilen. „Unbegrenzte Macht in jedem Kontext“ wäre daher eine zu starke Vereinfachung.

Für die tägliche Arbeit solltest du ein unprivilegiertes Konto verwenden. Administrative Rechte vergrößern die Auswirkungen von Fehlern bei Pfadangaben, nicht vertrauenswürdigen Befehlen und kompromittierter Software.

:::single-choice{#users-root-uid}
Welche numerische UID kennzeichnet traditionell das root-Konto?

::option[`0`]{#users-uid-zero .correct explanation="Linux und Unix-ähnliche Systeme reservieren die UID 0 traditionell für die Superuser-Identität."}
::option[`1000`]{#users-uid-thousand explanation="Viele Distributionen weisen dem ersten gewöhnlichen menschlichen Konto einen Wert nahe 1000 zu, doch dies ist nicht die UID von root."}
::option[`1`]{#users-uid-one explanation="Die UID 1 kann zu einem Systemkonto gehören und ist nicht die traditionelle Superuser-Identität."}
:::

## sudo unter einer Richtlinie verwenden

`sudo` fragt seine konfigurierte Richtlinie, ob der aufrufende Benutzer einen Befehl als Zielbenutzer ausführen darf. Das Standardziel ist häufig root, doch eine Richtlinie oder `-u USER` kann ein anderes Konto auswählen. Auch Authentifizierungsabfragen und Protokollierung hängen von der Konfiguration ab.

Liste die Befehle auf, die das aktuelle Konto ausführen darf:

```bash
$ sudo -l
```

Verwende einen erlaubten administrativen Befehl nur, wenn die Aufgabe ihn erfordert und du seine Auswirkungen verstehst. Nutze `sudo` nicht bloß, um eine Berechtigungsfehlermeldung zu unterdrücken, und zeige Datenbanken mit Passwort-Hashes wie `/etc/shadow` nicht als beiläufige Übung an.

:::single-choice{#users-sudo-policy}
Was tut `sudo`, bevor es einen angeforderten Befehl ausführt?

::option[Es prüft anhand der konfigurierten Richtlinie, ob die angeforderte Zielidentität verwendet werden darf.]{#users-sudo-policy-check .correct explanation="`sudo` autorisiert gemäß einer Richtlinie und richtet bei erteilter Erlaubnis anschließend die konfigurierten Zielzugangsdaten ein."}
::option[Es gewährt jedem lokalen Benutzer immer uneingeschränkten root-Zugriff.]{#users-sudo-always-root explanation="Die Autorisierung wird durch Richtlinien gesteuert, und abgelehnte Benutzer oder Befehle erhalten keinen pauschalen root-Zugriff."}
::option[Es ändert die UID des aufrufenden Kontos dauerhaft auf 0.]{#users-sudo-permanent-uid explanation="`sudo` führt einen Befehl mit Zielzugangsdaten aus; es schreibt die Kontoidentität des Aufrufers nicht dauerhaft um."}
:::

Probiere diese praktischen Labs aus, um die Verwaltung von Konten und Gruppen in einer kontrollierten Umgebung zu üben:

1. **[Linux-Benutzerkonten mit useradd, usermod und userdel verwalten](https://labex.io/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - Übe den vollständigen Lebenszyklus der Benutzerverwaltung, vom Erstellen und Absichern neuer Konten bis zu deren Änderung und Löschung.
2. **[Linux-Gruppen mit groupadd, usermod und groupdel verwalten](https://labex.io/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - Sammle praktische Erfahrung mit den zentralen Befehlszeilenwerkzeugen zur Gruppenverwaltung, einschließlich des Erstellens neuer Gruppen, der Änderung von Benutzermitgliedschaften und des Entfernens von Gruppen.
3. **[Benutzerkonten und sudo-Berechtigungen unter Linux konfigurieren](https://labex.io/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Lerne grundlegende Techniken zum Verwalten von Benutzerkonten und `sudo`-Berechtigungen, um die Sicherheit eines Linux-Systems zu erhöhen, darunter das Gewähren administrativer Rechte.

## Zusammenfassung

Du kannst nun beschreiben, wie Linux Identitäten darstellt und administrative Befehle delegiert.

1. Identifiziere Konten anhand ihrer UID und Gruppen anhand ihrer GID.
2. Unterscheide primäre und ergänzende Gruppenmitgliedschaften.
3. Setze Prozesszugangsdaten mit Zugriffsprüfungen in Beziehung.
4. Erkenne die UID 0 als traditionelle root-Identität.
5. Behandle `sudo` als richtliniengesteuertes Delegationswerkzeug.
