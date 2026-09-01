---
lesson_id: "authentication-logging"
course_id: "logging"
lang: "de"
order_index: 5
title: "Authentifizierungsprotokollierung"
description: "Lerne, Linux-Authentifizierungsdatensätze aufzufinden, zu interpretieren und sicher miteinander zu verknüpfen."
meta_title: "Authentifizierungsprotokollierung – Protokollierung"
meta_description: "Erkunde die Linux-Authentifizierungsprotokollierung anhand von /var/log/auth.log. Diese Anleitung erklärt Benutzeranmeldungen, Authentifizierungsmethoden und die sichere Untersuchung von Zugriffsproblemen."
meta_keywords: "Linux-Authentifizierung, auth.log, Linux-Protokollierung, Benutzeranmeldung, Linux-Sicherheit, Systemautorisierung, Anmeldefehler untersuchen, Authentifizierungsmethoden, Einsteiger, Tutorial, secure log"
---

Authentifizierungsprotokolle helfen, Anmeldeversuche, Berechtigungsänderungen und Sitzungsaktivität zu erklären. Sie sind sicherheitssensible Belege, doch eine einzelne Zeile belegt selten die Absicht eines Benutzers oder die Kompromittierung eines Kontos.

## Authentifizierungsdatensätze auffinden

Syslog-Konfigurationen der Debian-Familie leiten Authentifizierungsereignisse gewöhnlich nach `/var/log/auth.log`, während Konfigurationen der Red-Hat-Familie häufig `/var/log/secure` verwenden. Ein systemd-Journal kann dieselben Ereignisse mit Unit- und Prozessmetadaten aufbewahren, und eine zentrale Protokollierung kann die maßgebliche Kopie enthalten.

Ermittle das lokale Ziel und frage den betreffenden Dienst ab, zum Beispiel:

```bash
$ sudo journalctl -u ssh.service --since '1 hour ago'
$ sudo less /var/log/auth.log
```

Die SSH-Unit kann `ssh.service` oder `sshd.service` heißen. Berechtigungen beschränken diese Datensätze gewöhnlich, weil sie Konto- und Zugriffsdetails offenlegen.

:::single-choice{#auth-logs-file-location} Wo müssen Linux-Authentifizierungsereignisse immer gespeichert sein?

::option[Am durch die lokale Protokollierungsrichtlinie ausgewählten Ziel.]{#auth-logs-local-policy .correct explanation="Dateien, Journal und zentrale Datensammler unterscheiden sich je nach Distribution und Konfiguration."}
::option[Auf jeder Distribution in `/var/log/auth.log`.]{#auth-logs-auth-only explanation="Dieser Pfad ist auf Systemen der Debian-Familie verbreitet, aber nicht allgemeingültig."}
::option[In der Shellverlaufsdatei jedes Benutzers.]{#auth-logs-shell-history explanation="Der Shellverlauf enthält den Befehlsverlauf eines Benutzers und ist kein Speicher für Systemauthentifizierungsereignisse."}
:::

## Ein Ereignis interpretieren

Ein herkömmlicher Datensatz könnte Folgendes enthalten:

```text
Jan 31 10:37:50 icebox pkexec: pam_unix(polkit-1:session): session opened for user root by (uid=1000)
```

Dies bezeichnet Zeit, Host, ausgebendes Programm, PAM-Modul und -Dienst, angeforderten Sitzungsbenutzer sowie ursprüngliche UID. Es identifiziert für sich allein weder den Menschen hinter UID 1000 noch beweist es eine böswillige Handlung. Löse die UID anhand der zum Zeitpunkt des Vorfalls gültigen Kontodatensätze auf und verknüpfe Terminal, entfernte Adresse, Sitzung und umgebende Ereignisse.

:::single-choice{#auth-logs-uid-inference} Was belegt `uid=1000` in diesem Datensatz?

::option[Dass das root-Passwort tausendmal falsch eingegeben wurde.]{#auth-logs-thousand-passwords explanation="Der Wert ist eine Identitätsnummer und keine Anzahl von Versuchen."}
::option[Die numerische Kontoidentität, die dem auslösenden Prozess zugeordnet ist.]{#auth-logs-numeric-identity .correct explanation="Zur Zuordnung der Handlung zu einer Person sind weitere Sitzungs- und Kontobelege erforderlich."}
::option[Dass das Ereignis von TCP-Port 1000 stammt.]{#auth-logs-port explanation="Eine UID ist kein Netzwerkportfeld."}
:::

## Erfolg und Fehlschlag untersuchen

Suche in einem begrenzten Zeitraum sowohl nach angenommenen als auch abgelehnten Versuchen. Untersuche bei SSH außerdem Verbindungsquelle, Authentifizierungsmethode, Zielkonto, Sitzungsbeginn und -ende sowie Dienstneustarts. Wiederholte Fehlschläge können Benutzerfehler, Automatisierung mit veralteten Anmeldedaten, Scans oder einen Angriff bedeuten; die Rate allein wählt keine dieser Erklärungen aus.

`last` und `lastb` können, sofern sie geführt werden, Datensätze aus `wtmp` und `btmp` zusammenfassen. Diese Binärdatenbanken besitzen jedoch eigene Aufbewahrungs- und Integritätsgrenzen. Vergleiche sie mit Journal- oder Syslog-Datensätzen und zentralen Quellen.

:::single-choice{#auth-logs-failed-attempts} Womit sollten wiederholte fehlgeschlagene Anmeldungen verknüpft werden?

::option[Nur mit dem gesamten freien Datenträgerspeicher.]{#auth-logs-disk-space explanation="Kapazität identifiziert weder Quelle, Ziel noch Methode eines Authentifizierungsversuchs."}
::option[Mit Quelle, Zielkonto, Methode, Zeitverlauf und erfolgreichen Sitzungen.]{#auth-logs-correlated-fields .correct explanation="Diese Angaben helfen, Fehlkonfiguration, Benutzerfehler, Scans und unbefugten Zugriff zu unterscheiden."}
::option[Mit der Schlussfolgerung, dass das Konto sicher kompromittiert ist.]{#auth-logs-certain-compromise explanation="Fehlschläge können mehrere harmlose oder feindliche Ursachen haben."}
:::

## Belege bewahren und reagieren

Falls ein Vorfall vermutet wird, erfasse Hostzeit und Zeitzone, bewahre ursprüngliche Protokolle samt Metadaten und sichere jede exportierte Kopie. Bearbeite Belege nicht an Ort und Stelle. Kontosperren, Firewalländerungen und das Beenden von Sitzungen können berechtigten Zugriff unterbrechen oder einen Angreifer warnen. Befolge deshalb den Prozess zur Vorfallsreaktion und erhalte einen Wiederherstellungszugang.

:::single-choice{#auth-logs-preservation} Wie sollten Authentifizierungsbelege während einer Untersuchung behandelt werden?

::option[Verdächtige Zeilen zur Verdeutlichung in der Originaldatei bearbeiten.]{#auth-logs-edit-original explanation="Das Ändern der Quelle beschädigt die Integrität der Belege."}
::option[Das vollständige Protokoll veröffentlichen, damit jeder Benutzer identifizieren kann.]{#auth-logs-publish explanation="Authentifizierungsdatensätze können vertrauliche Identitäten und Infrastrukturdetails offenlegen."}
::option[Originale bewahren und exportierte Kopien schützen.]{#auth-logs-preserve .correct explanation="Integrität und Vertraulichkeit sind für Sicherheitsprotokolle gleichermaßen wichtig."}
:::

## Zusammenfassung

Du kannst Authentifizierungsereignisse nun untersuchen, ohne die Aussagekraft eines einzelnen Datensatzes zu überschätzen.

1. Ermittle das lokal konfigurierte Ziel für Authentifizierungsprotokolle.
2. Interpretiere Identität, Dienst, Methode und Sitzungsfelder im Zusammenhang.
3. Verknüpfe fehlgeschlagene und erfolgreiche Aktivität über aufbewahrte Quellen hinweg.
4. Bewahre Belege und koordiniere unterbrechende Reaktionsmaßnahmen.
