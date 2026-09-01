---
lesson_id: "samba"
course_id: "network-sharing"
lang: "de"
order_index: 5
title: "Samba"
description: "Lerne, eine grundlegende Samba-Dateifreigabe zu konfigurieren, zu validieren, aufzurufen und abzusichern."
meta_title: "Samba – Netzwerkfreigaben"
meta_description: "Lerne, eine Samba-Netzwerkfreigabe unter Linux einzurichten. Diese Anleitung behandelt SMB-Protokoll, Installation, Konfiguration und den Zugriff mit Linux-SMB-Clients."
meta_keywords: "Samba, SMB Linux, Linux SMB, Samba-Netzwerk, Samba-Protokoll, SMB Samba, Dateifreigabe, smb.conf, cifs, smbclient, Linux-Tutorial"
---

Samba implementiert das Server Message Block Protocol auf Unix-artigen Systemen und ermöglicht Linux-, Windows-, macOS- und anderen Clients die gemeinsame Nutzung von Dateien und Druckern. Moderne Installationen verwenden aktuelle SMB-Dialekte. Der ältere Begriff CIFS ist weiterhin in Linux-Clientwerkzeugen sichtbar, sollte aber nicht als Grund verstanden werden, das veraltete SMB1 zu aktivieren.

## Die Freigabe planen

Lege vor der Installation oder Änderung von Samba die autorisierten Clients, Identitäten, Lese-/Schreibanforderungen, Netzwerkzone, Dateneigentümer, Sicherungsrichtlinie und den erforderlichen SMB-Dialekt fest. Verwende ein eigenes Verzeichnis, statt unbeabsichtigt einen Home- oder Systembaum offenzulegen.

Der Zugriff wird sowohl durch die Samba-Richtlinie als auch die zugrunde liegenden Dateisystemberechtigungen gesteuert. Schreibzugriff in `smb.conf` kann einem Konto keinen Dateisystemzugriff gewähren, den es nicht besitzt.

:::single-choice{#samba-two-permission-layers} Was muss einem Benutzer das Schreiben über eine Samba-Freigabe erlauben?

::option[Nur der angezeigte Kommentar der Freigabe.]{#samba-comment-permission explanation="Ein Kommentar ist beschreibender Text und gewährt keinen Zugriff."}
::option[Sowohl Samba-Regeln als auch Dateisystemberechtigungen.]{#samba-policy-and-filesystem .correct explanation="Die Anfrage muss die Regeln auf Protokollebene und die lokale Dateisystemautorisierung bestehen."}
::option[Nur die Einstellung des Desktophintergrunds auf dem Client.]{#samba-wallpaper explanation="Darstellungseinstellungen des Clients steuern keine Serverdateien."}
:::

## Eine grundlegende Freigabe definieren

Die Hauptkonfiguration ist gewöhnlich `/etc/samba/smb.conf`. Ein eingeschränktes Beispiel lautet:

```ini
[team]
    path = /srv/samba/team
    browseable = yes
    read only = no
    valid users = @teamshare
```

Erstelle das Verzeichnis und wende geprüfte Eigentums- und Berechtigungseinstellungen für die Unix-Gruppe an:

```bash
$ sudo install -d -o root -g teamshare -m 2770 /srv/samba/team
```

Das Set-Group-ID-Bit hilft neuen Einträgen, die Verzeichnisgruppe zu übernehmen. Gemeinsamer Zugriff kann jedoch zusätzlich eine ACL oder eine sorgfältig gewählte Erstellungsmaske erfordern. Teste die tatsächlichen Datei- und Verzeichnisergebnisse, statt anzunehmen, dass die Vererbung ausreicht.

:::single-choice{#samba-valid-users} Was drückt `valid users = @teamshare` aus?

::option[Jeder anonyme Netzwerkbenutzer erhält Schreibzugriff.]{#samba-every-anonymous explanation="Die Regel schränkt den Zugriff ein, statt Gastschreibzugriff zu aktivieren."}
::option[Der Server muss die Freigabe in `teamshare` umbenennen.]{#samba-rename-share explanation="Der sichtbare Freigabename bleibt der Abschnittsname `[team]`."}
::option[Nur Mitglieder der benannten Gruppe werden von dieser Freigaberegel zugelassen.]{#samba-valid-group .correct explanation="Die Form mit `@` bezeichnet in Sambas Benutzerlistensyntax eine Gruppe."}
:::

## Identität konfigurieren

In einer eigenständigen Samba-Konfiguration benötigt ein Konto gewöhnlich eine entsprechende Unix-Identität und aktivierte Samba-Anmeldedaten:

```bash
$ sudo smbpasswd -a alice
```

Installationen mit Verzeichnisdomäne verwenden einen anderen Identitätsentwurf. Lege Passwörter weder im Shellverlauf noch in einer für unabhängige Benutzer lesbaren Konfiguration ab und nimm nicht an, dass ein Samba-Passwort automatisch mit dem Passwort des Unix-Kontos identisch ist.

:::single-choice{#samba-password-database} Was bewirkt `smbpasswd -a alice` gewöhnlich auf einem eigenständigen Server?

::option[Es löscht das Home-Verzeichnis des Unix-Benutzers.]{#samba-delete-home explanation="Der Befehl verwaltet Samba-Anmeldedaten und entfernt keine Home-Verzeichnisse."}
::option[Es fügt Samba-Anmeldedaten für das Konto hinzu oder initialisiert sie.]{#samba-add-credential .correct explanation="Die SMB-Authentifizierungsdatenbank wird getrennt vom bloßen Erstellen eines Unix-Benutzers verwaltet."}
::option[Es hängt jede sichtbare SMB-Freigabe als Alice ein.]{#samba-mount-all explanation="Das Eintragen von Serveranmeldedaten ist vom Einhängen auf einem Client getrennt."}
:::

## Konfiguration validieren und anwenden

Prüfe die geparste Konfiguration, bevor du Dienste neu lädst:

```bash
$ testparm -s
```

Prüfe unerwartete Standardwerte und Fehler und lade den Samba-Dienst der Distribution anschließend über seinen Dienstmanager neu. Dienstnamen unterscheiden sich und umfassen häufig `smbd.service` oder `smb.service`. Ein Neuladen ist, sofern unterstützt, weniger unterbrechend als ein Neustart. Überprüfe dennoch Zustand, lauschende Sockets, Firewallbereich und Protokolle.

Teste von einem Client mit einem ausdrücklich angegebenen Benutzer:

```bash
$ smbclient //server.example.net/team -U alice
```

:::single-choice{#samba-testparm-purpose} Warum solltest du `testparm -s` vor dem Anwenden einer Samba-Änderung ausführen?

::option[Der Befehl kopiert jede freigegebene Datei auf einen Sicherungsserver.]{#samba-testparm-backup explanation="Das Werkzeug parst und meldet Konfiguration, statt Freigabedaten zu kopieren."}
::option[Er validiert die wirksame Samba-Konfiguration und zeigt sie an.]{#samba-testparm-validate .correct explanation="Die Parserausgabe erkennt Konfigurationsfehler und zeigt interpretierte Einstellungen vor Auswirkungen auf den Dienst."}
::option[Er gewährt allen Clients Administratorrechte.]{#samba-testparm-admin explanation="Die Validierung verändert keine Clientautorisierung."}
:::

## Unter Linux einhängen

Linux-Clients verwenden gewöhnlich den Dateisystemtreiber `cifs` und Mount-Hilfsprogramme. Vermeide Passwörter in der Befehlszeile, weil Argumente über Verlauf oder Prozessuntersuchung offengelegt werden können. Verwende eine nur für root lesbare Anmeldedatendatei oder einen genehmigten Anmeldedatenmechanismus:

```bash
$ sudo mount -t cifs //server.example.net/team /mnt/team \
    -o credentials=/root/.smb-team,vers=3.1.1
```

Schütze die Anmeldedatendatei, bestätige den von beiden Seiten unterstützten Dialekt und lege Anforderungen an UID, GID, Berechtigungen und Verschlüsselung bewusst fest. Überprüfe nach dem Einhängen mit `findmnt`, führe autorisierte Lese-/Schreibtests aus und hänge nach Koordination aktiver Benutzer aus.

:::single-choice{#samba-command-line-password} Warum solltest du `password=...` nicht direkt in einem mount-Befehl verwenden?

::option[Das Geheimnis kann über den Verlauf oder Prozessargumente offengelegt werden.]{#samba-password-exposure .correct explanation="Eine geschützte Anmeldedatenquelle verringert unbeabsichtigte Offenlegung, erfordert aber weiterhin sorgfältige Berechtigungen."}
::option[SMB unterstützt keinerlei Passwortauthentifizierung.]{#samba-no-passwords explanation="Passwortbasierte SMB-Authentifizierung ist verbreitet, obwohl auch andere Identitätssysteme existieren."}
::option[Die Option macht die Freigabe dauerhaft schreibgeschützt.]{#samba-password-readonly explanation="Der Speicherort des Geheimnisses bestimmt nicht die Schreibrichtlinie."}
:::

## Zusammenfassung

Du kannst eine Samba-Freigabe nun unter Berücksichtigung von Protokoll- und Dateisystemsicherheit konfigurieren.

1. Lege zuerst Clients, Identitäten, Netzwerkbereich und Datenrichtlinie fest.
2. Beschränke die Freigabe und gleiche die zugrunde liegenden Berechtigungen ab.
3. Verwalte Samba-Anmeldedaten über das richtige Identitätsmodell.
4. Validiere mit `testparm` und führe einen Ende-zu-Ende-Clienttest aus.
5. Schütze Clientanmeldedaten und überprüfe den eingehängten Zugriff.
