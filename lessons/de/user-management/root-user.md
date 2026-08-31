---
lesson_id: "root-user"
course_id: "user-management"
lang: "de"
order_index: 2
title: "root"
description: "Erfahre, wie su, sudo und sudoers-Richtlinien einen kontrollierten Zugriff auf privilegierte Identitäten ermöglichen."
meta_title: "root – Benutzerverwaltung"
meta_description: "Erkunde die Rolle des root-Benutzers unter Linux. Diese Lektion behandelt die Unterschiede zwischen su und sudo beim Erlangen von Superuser-Rechten und erklärt, wie die Datei /etc/sudoers den Zugriff verwaltet."
meta_keywords: "root-Benutzer unter Linux, Linux-root-Benutzer, su, sudo, sudoers, visudo, Superuser, Benutzerverwaltung, Linux-Berechtigungen"
---

Das traditionell `root` genannte Konto besitzt die UID 0 und weitreichende Befugnisse innerhalb seines Sicherheitskontexts. Verwende für die tägliche Arbeit ein unprivilegiertes Konto und erhöhe Rechte nur für einen bestimmten administrativen Zweck, den du verstehst.

## Mit su eine Shell als anderer Benutzer starten

`su`, kurz für substitute user, startet eine Shell oder einen Befehl mit der Identität eines anderen Kontos. Ohne Benutzernamen ist root das Standardziel:

```bash
$ su
```

Die Authentifizierung wird durch PAM und lokale Richtlinien gesteuert. Ein System kann nach dem Passwort des Zielkontos fragen, den Zugriff auf `su` einschränken oder das root-Passwort gesperrt lassen. Gehe nicht davon aus, dass die Kenntnis eines Passworts die einzige Voraussetzung ist.

Ein einfaches `su` wechselt die Identität und behält dabei einen größeren Teil der aktuellen Umgebung bei. `su - USER`, auch als `su --login USER` geschrieben, startet eine Shell im Anmeldestil und richtet eine Umgebung ein, die einer frischen Anmeldung am Zielkonto näherkommt:

```bash
$ su - operator
```

Beende die Subshell, sobald die Arbeit für das Zielkonto abgeschlossen ist.

:::single-choice{#root-su-login-shell}
Welcher Befehl fordert eine Shell im Anmeldestil als Benutzer `operator` an?

::option[`su - operator`]{#root-su-login-operator .correct explanation="Der Bindestrich fordert das Verhalten einer Anmelde-Shell und eine auf `operator` ausgerichtete Umgebung an."}
::option[`su operator`]{#root-su-preserve-environment explanation="Dies wechselt zur Zielidentität, fordert aber nicht die hier vorgestellte vollständige Initialisierung im Anmeldestil an."}
::option[`sudo -l operator`]{#root-sudo-list-operator explanation="`sudo -l` listet die gemäß Richtlinie erlaubten Befehle auf; es startet nicht die angeforderte Anmelde-Shell."}
:::

## Einen bestimmten Befehl mit sudo ausführen

`sudo COMMAND` fordert eine Autorisierung durch die Richtlinie an, um einen Befehl als Zielbenutzer auszuführen, standardmäßig gewöhnlich als root. Mit `-u USER` kannst du ein anderes Ziel anfordern:

```bash
$ sudo -u postgres id
```

Das bedeutet nicht, dass die Anfrage genehmigt wird. Die sudo-Richtlinie berücksichtigt den aufrufenden Benutzer, den Host, die Zielidentität, den Befehl und weitere Bedingungen. Je nach Konfiguration kann die Authentifizierung das Passwort des aufrufenden Benutzers, einen anderen Mechanismus oder überhaupt keine Abfrage verwenden.

Bevorzuge nach Möglichkeit einen einzelnen, eng begrenzten administrativen Befehl gegenüber einer langlebigen privilegierten Shell. Der kleinere Umfang verringert das Risiko, dass versehentliche Befehle mit erhöhten Rechten ausgeführt werden.

:::single-choice{#root-sudo-target-user}
Was fordert `sudo -u postgres id` an?

::option[Das aktuelle Konto dauerhaft in `postgres` umzubenennen.]{#root-sudo-rename explanation="`sudo` führt einen Befehl mit Zielzugangsdaten aus; es benennt keine Kontoeinträge um."}
::option[`id` mit `postgres` als Zielbenutzer auszuführen, sofern die Richtlinie dies erlaubt.]{#root-sudo-postgres-id .correct explanation="Die Option `-u` wählt die Zielidentität aus, während die sudoers-Richtlinie entscheidet, ob die Anfrage erlaubt wird."}
::option[Alle Benutzer aufzulisten, deren UID größer als die des aktuellen Benutzers ist.]{#root-sudo-list-uids explanation="Der Befehl `id` gibt Identitätsinformationen für seinen Prozess aus; diese Syntax listet keine Konto-UIDs auf."}
:::

## Dauerhafte privilegierte Shells vermeiden

Befehle wie `su -`, `sudo -s` oder `sudo -i` können eine privilegierte Shell erzeugen, wenn die Richtlinie dies erlaubt. Jeder spätere Befehl in dieser Shell kann bis zu ihrem Beenden erhöhte Auswirkungen haben. Fehlerhafte Pfade, ungeprüfte Skripte und Shell-Erweiterungen werden dadurch gefährlicher.

Das Auditverhalten hängt von der Konfiguration ab. `sudo` protokolliert Aufrufe häufig, doch ein einzelner protokollierter Shell-Start liefert nicht automatisch eine vollständige Aufzeichnung jedes in dieser Shell eingegebenen Befehls. Shell-Verlauf, System-Auditing und sudo-E/A-Protokollierung sind getrennte Mechanismen mit eigenen Richtlinien.

:::single-choice{#root-persistent-shell-risk}
Warum ist eine langlebige root-Shell riskanter, als jeweils nur einen verstandenen Befehl mit erhöhten Rechten auszuführen?

::option[root-Shells löschen automatisch jeden Befehl aus allen Audit-Systemen.]{#root-shell-no-audit explanation="Die Protokollierung hängt von der Konfiguration ab; die Behauptung, alle Audit-Aufzeichnungen würden automatisch gelöscht, ist falsch."}
::option[Die Shell deaktiviert Dateisystempfade, die aus mehr als einer Komponente bestehen.]{#root-shell-path-limit explanation="Privilegien führen nicht zu dieser Pfadeinschränkung; problematisch sind die auf gewöhnliche Vorgänge angewendeten Befugnisse."}
::option[Spätere Befehle können bis zum Beenden der Shell erhöhte Auswirkungen behalten.]{#root-shell-elevated-scope .correct explanation="Eine dauerhafte privilegierte Identität vergrößert das Zeitfenster, in dem ein Tippfehler oder ein nicht vertrauenswürdiger Befehl geschützte Ressourcen verändern kann."}
:::

## sudo-Autorisierung überprüfen

Führe `sudo -l` aus, um aufzulisten, was das aktuelle Konto gemäß der aktiven Richtlinie anfordern darf:

```bash
$ sudo -l
```

Prüfe Befehlspfade, erlaubte Zielbenutzer und Einschränkungen für Argumente. Eine weit gefasst wirkende Regel solltest du nicht als Erlaubnis für sachfremde Arbeiten behandeln.

:::single-choice{#root-list-sudo-rules}
Welcher Befehl listet die sudo-Berechtigungen auf, die dem aktuell aufrufenden Benutzer zur Verfügung stehen?

::option[`sudo -i`]{#root-sudo-login explanation="Dies fordert eine Ziel-Shell im Anmeldestil an und kann den Umfang der Privilegien erhöhen; es ist keine schreibgeschützte Richtlinienauflistung."}
::option[`sudo -l`]{#root-sudo-list .correct explanation="Die kleingeschriebene Option `-l` fordert sudo auf, die von seiner aktuellen Richtlinie erlaubten Befehle aufzulisten."}
::option[`su -l`]{#root-su-login-default explanation="Dies ruft das Verhalten einer Anmelde-Shell für `su` auf, statt sudo-Autorisierungen aufzulisten."}
:::

## sudoers-Richtlinien sicher bearbeiten

Die standardmäßige sudo-Richtlinie liest gewöhnlich `/etc/sudoers` und kann Dateien unter `/etc/sudoers.d/` einbinden. Andere Richtlinienquellen sind möglich. Die Syntax steuert weit mehr als eine einfache Liste von Benutzern und Gruppen.

Verwende für Richtlinienänderungen `visudo`, weil es die Datei sperrt und ihre Syntax vor der Installation überprüft:

```bash
$ sudo visudo
```

Gib für eine ergänzende Datei ihren genauen Pfad an:

```bash
$ sudo visudo -f /etc/sudoers.d/application-admins
```

Bearbeite sudoers nicht mit einer gewöhnlichen Umleitung oder einem Editor-Arbeitsablauf ohne Validierung. Ein Syntax- oder Berechtigungsfehler kann den administrativen Zugriff entfernen. Halte beim Ändern einer entfernten Autorisierung einen weiteren verifizierten Wiederherstellungsweg bereit.

:::single-choice{#root-edit-sudoers-safely}
Welches Werkzeug solltest du verwenden, um die sudoers-Hauptrichtlinie zu bearbeiten und ihre Syntax zu prüfen?

::option[`cat`]{#root-cat-sudoers explanation="`cat` kann lesbaren Text anzeigen, bearbeitet, sperrt oder validiert die sudoers-Syntax aber nicht sicher."}
::option[`visudo`]{#root-visudo .correct explanation="`visudo` bietet Sperrung und Syntaxvalidierung speziell für Änderungen an sudoers-Richtlinien."}
::option[`echo` mit `>`]{#root-echo-sudoers explanation="Eine Shell-Umleitung kann die Richtlinie sofort abschneiden und bietet keine Validierung der sudoers-Syntax."}
:::

Probiere dieses praktische Lab aus, um die delegierte Administration in einer kontrollierten Umgebung zu üben:

1. **[Benutzerkonten und sudo-Berechtigungen unter Linux konfigurieren](https://labex.io/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Übe das Durchsetzen von Passwortrichtlinien, das Sperren und Entsperren von Benutzerkonten, das Absichern des root-Kontos und das Gewähren administrativer Rechte – alles unmittelbar mit der Verwaltung des Superuser-Zugriffs verbunden.

## Zusammenfassung

Du kannst nun den Identitätswechsel von der richtliniengesteuerten Befehlsdelegation unterscheiden.

1. Verwende `su - USER` nur, wenn eine Ziel-Shell im Anmeldestil beabsichtigt ist.
2. Fordere mit `-u USER` ein bestimmtes sudo-Ziel an.
3. Verbringe möglichst wenig Zeit in einer privilegierten Shell.
4. Überprüfe wirksame sudo-Regeln mit `sudo -l`.
5. Bearbeite sudoers-Richtlinien ausschließlich mit `visudo`.
