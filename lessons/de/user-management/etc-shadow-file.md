---
lesson_id: "etc-shadow-file"
course_id: "user-management"
lang: "de"
order_index: 4
title: "/etc/shadow"
description: "Erfahre, wie lokale shadow-Einträge Passwort-Hashes und Alterungsrichtlinien darstellen, ohne vertrauliche Daten offenzulegen."
meta_title: "/etc/shadow – Benutzerverwaltung"
meta_description: "Erkunde die Datei /etc/shadow unter Linux, einen wichtigen Bestandteil der Benutzerauthentifizierung. Erfahre, wie sie mit 'cat /etc/shadow' angezeigt wird, und verstehe die Struktur der etc-shadow-Datei, die Passwort-Hashes und Richtlinieninformationen speichert."
meta_keywords: "etc shadow, Datei etc/shadow unter Linux, cat /etc/shadow, etc shadow unter Linux, /etc/shadow, Benutzerauthentifizierung, Passwortsicherheit, Linux-Systemadministration"
---

`/etc/shadow` speichert geschützte lokale Passwort-Hashes und Felder zur Passwortalterung. Die Trennung dieser Werte von der allgemein lesbaren Datenbank `/etc/passwd` verringert das Risiko, sie für Offline-Angriffe zum Erraten von Passwörtern offenzulegen.

## Shadow-Daten schützen

Passwörter werden nicht umkehrbar „verschlüsselt“ gespeichert, um sie später wieder anzuzeigen. Ein lokaler Passworteintrag enthält gewöhnlich einen Einweg-Passwort-Hash, der mit einer Algorithmuskennung, einem Salt und Parametern codiert ist. Ein Angreifer, der solche Hashes erlangt, kann mögliche Passwörter offline ausprobieren. Die Datenbank muss daher geschützt bleiben.

Die genauen Eigentums- und Berechtigungsangaben unterscheiden sich, doch der Zugriff ist gewöhnlich auf root und eng begrenzte autorisierte Systemkomponenten beschränkt. Gib shadow-Inhalte nicht allein zur Prüfung eines Kontostatus aus, kopiere, protokolliere oder teile sie nicht.

:::single-choice{#shadow-restricted-reason} Warum sind lokale shadow-Daten gewöhnlich vor allgemeinem Lesezugriff geschützt?

::option[Die Datei enthält das aktuelle Passwort jedes Benutzers im Klartext.]{#shadow-plaintext-passwords explanation="Ordnungsgemäße shadow-Einträge speichern Einweg-Passwort-Hashes oder besondere Markierungen und keine abrufbaren Klartextpasswörter."}
::option[Offengelegte Passwort-Hashes können offline angegriffen werden.]{#shadow-offline-guessing .correct explanation="Ein Angreifer kann Passwortversuche gegen gestohlene Hashes prüfen, ohne mit dem Anmeldedienst zu interagieren."}
::option[Das Lesen ändert automatisch alle Ablaufdaten von Passwörtern.]{#shadow-read-changes explanation="Ein Lesezugriff aktualisiert nicht von sich aus Richtlinienfelder; das Problem ist die Offenlegung vertraulichen Authentifizierungsmaterials."}
:::

## Das Format mit neun Feldern lesen

Ein lokaler shadow-Eintrag enthält neun durch Doppelpunkte getrennte Felder. Ein schematischer Eintrag sieht so aus, wobei der Hash bewusst weggelassen wurde:

```text
alice:<password-field>:20000:0:90:7:14:20500:
```

Die Felder sind:

1. **Anmeldename**.
2. **Passwort-Hash oder besondere Passwortmarkierung**.
3. **Letzte Passwortänderung** in Tagen seit dem 01.01.1970; `0` fordert bei typischen Werkzeugen eine Änderung bei der nächsten mit einem Passwort authentifizierten Anmeldung an.
4. **Mindestalter des Passworts** in Tagen.
5. **Höchstalter des Passworts** in Tagen.
6. **Warnzeitraum** vor Ablauf des Passworts in Tagen.
7. **Inaktivitätszeitraum** nach Ablauf des Passworts in Tagen.
8. **Ablaufdatum des Kontos** in Tagen seit dem 01.01.1970.
9. **Reserviertes Feld**.

Leere Felder und besondere numerische Werte besitzen festgelegte Bedeutungen, die je nach Feld und Werkzeug variieren können. Verwende Werkzeuge zur Kontoverwaltung, statt Werte nach Augenmaß zu bearbeiten.

:::single-choice{#shadow-account-expiration-field} Welches shadow-Feld speichert das Ablaufdatum des Kontos als Tage seit dem 01.01.1970?

::option[Feld 3]{#shadow-field-three explanation="Feld 3 erfasst das Datum der letzten Passwortänderung und nicht den Ablauf des Kontos."}
::option[Feld 8]{#shadow-field-eight .correct explanation="Das achte Feld ist die absolute Tageszahl für den Ablauf des Kontos."}
::option[Feld 5]{#shadow-field-five explanation="Feld 5 erfasst das Höchstalter des Passworts."}
:::

## Das Passwortfeld sorgfältig interpretieren

Ein gültiger Hash in Feld 2 ermöglicht die lokale Prüfung eines Unix-Passworts. Ein mit `!` beginnender Wert sperrt gewöhnlich diesen Passwort-Hash, während `*` oder eine andere ungültige Hash-Markierung eine erfolgreiche Passwortprüfung über dieses Feld verhindert. Ein leerer Wert ist sicherheitskritisch und kann je nach PAM-Richtlinie ein Verhalten ohne Passwort ermöglichen.

Diese Markierungen beschreiben den lokalen Passwortweg und nicht jede mögliche Authentifizierungsmethode. Öffentliche SSH-Schlüssel, Zertifikate, Token und anwendungsspezifische Zugangsdaten können weiter nutzbar bleiben, sofern sie nicht gesondert eingeschränkt werden. Auch der Ablauf eines Kontos in Feld 8 unterscheidet sich von der Passwortsperre.

:::single-choice{#shadow-password-lock-scope} Was kannst du aus einem shadow-Passwortfeld, das mit `!` beginnt, sicher schließen?

::option[Der gespeicherte Unix-Passwort-Hash wurde für die normale Passwortprüfung unbrauchbar gemacht.]{#shadow-password-locked .correct explanation="Wird dem Hash `!` vorangestellt, kann er über den shadow-Passwortweg nicht mehr mit einem eingegebenen Passwort übereinstimmen."}
::option[Jede mögliche Anmeldemethode für das Konto wurde deaktiviert.]{#shadow-all-login-disabled explanation="Andere Authentifizierungsmethoden können unabhängig sein. Die Passwortmarkierung allein beweist daher keine vollständige Kontosperre."}
::option[Das Konto wurde aus allen Identitätsdatenbanken gelöscht.]{#shadow-account-deleted explanation="Ein shadow-Eintrag ist weiterhin vorhanden, und das Löschen ist ein gesonderter Vorgang der Kontoverwaltung."}
:::

## Passwort- und Kontodaten unterscheiden

Die Felder 3 bis 7 betreffen die Passwortalterung: wann das Passwort zuletzt geändert wurde, wann eine weitere Änderung erlaubt ist, wann es abläuft, wann Warnungen beginnen und wie lange eine Passwortanmeldung nach dem Ablauf noch möglich bleibt. Feld 8 lässt das Konto an einem absoluten Tag ablaufen, unabhängig vom Alter des Passworts.

Ein Höchstalter des Passworts von 90 Tagen ist beispielsweise nicht dasselbe wie ein Ablaufdatum des Kontos. Ersteres verschiebt sich relativ zur letzten Passwortänderung, letzteres bleibt ein festes Datum, bis ein Administrator es ändert.

:::single-choice{#shadow-max-age-versus-expire} Worin unterscheiden sich die shadow-Felder 5 und 8?

::option[Feld 5 speichert den Benutzernamen; Feld 8 speichert die Anmelde-Shell.]{#shadow-username-shell explanation="Der Benutzername steht in Feld 1, und die Anmelde-Shell wird in `/etc/passwd` und nicht im shadow-Eintrag erfasst."}
::option[Feld 5 speichert einen Passwort-Hash; Feld 8 speichert dessen Salt.]{#shadow-hash-salt explanation="Die Codierung des Passwort-Hashes gehört in Feld 2, und Alterungsfelder speichern dessen Salt nicht getrennt."}
::option[Feld 5 ist das Höchstalter des Passworts; Feld 8 ist ein absolutes Ablaufdatum des Kontos.]{#shadow-password-vs-account-expiry .correct explanation="Das Passwortalter ist relativ zur letzten Änderung, während der Kontoablauf als absolute Tageszahl gespeichert wird."}
:::

## Richtlinien mit Werkzeugen prüfen und ändern

Administratoren sollten nur die für eine Aufgabe erforderlichen Informationen abfragen:

```bash
$ sudo passwd -S alice
$ sudo chage -l alice
```

`passwd -S` fasst den lokalen Passwortstatus zusammen, während `chage -l` die Alterungsinformationen in lesbarer Form auflistet. Ausgabeformate und Autorisierungsanforderungen können sich je nach Distribution unterscheiden.

Verwende `passwd`, `chage`, `usermod` und verwandte Kontowerkzeuge für Änderungen. Wenn eine manuelle Reparatur der lokalen shadow-Datenbank unvermeidbar ist, bietet `vipw -s` eine Sperrung; validiere Kontodatenbanken mit `pwck`. Halte eine Wiederherstellungssitzung aufrecht, bevor du eine entfernte Authentifizierung änderst.

:::single-choice{#shadow-list-aging-policy} Welcher Befehl ist dafür vorgesehen, lesbare Informationen zur Passwortalterung des lokalen Kontos `alice` aufzulisten?

::option[`cat /etc/shadow`]{#shadow-cat-entire-file explanation="Dies legt jeden lokalen shadow-Eintrag und damit mehr vertrauliche Informationen offen, als die Aufgabe erfordert."}
::option[`passwd -d alice`]{#shadow-passwd-delete explanation="Die Operation `-d` entfernt den Passwort-Hash und ist eine zustandsverändernde, sicherheitskritische Aktion statt eines Auflistungsbefehls."}
::option[`chage -l alice`]{#shadow-chage-list .correct explanation="Die kleingeschriebene Option `-l` fordert `chage` auf, die Felder zur Passwortalterung des Kontos in lesbarer Form anzuzeigen."}
:::

PAM und NSS können Authentifizierungs- und Identitätsquellen außerhalb lokaler shadow-Dateien einbinden. Ein Systemkonto kann deshalb keinen lokalen shadow-Eintrag besitzen oder sich über zusätzliche Dienste authentifizieren.

Probiere diese praktischen Labs aus, um Kontostatus und Alterungsrichtlinien in einer kontrollierten Umgebung zu üben:

1. **[Linux-Benutzerkonten mit useradd, usermod und userdel verwalten](https://labex.io/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - Übe den vollständigen Lebenszyklus der Benutzerverwaltung, vom Erstellen und Absichern neuer Konten mit `useradd` und `passwd` bis zu deren Änderung und Löschung.
2. **[Benutzerkonten und sudo-Berechtigungen unter Linux konfigurieren](https://labex.io/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Lerne grundlegende Techniken zur Verwaltung von Benutzerkonten und sudo-Berechtigungen, einschließlich des Durchsetzens von Passwortrichtlinien und Absicherns von Konten.

## Zusammenfassung

Du kannst nun shadow-Richtlinien interpretieren, ohne die vollständige Passwortdatenbank offenzulegen.

1. Behandle Passwort-Hashes als geschütztes Authentifizierungsmaterial.
2. Lies die neun shadow-Felder nach ihrem Zweck.
3. Unterscheide eine Passwortsperre von der Deaktivierung jeder Anmeldemethode.
4. Trenne die Passwortalterung vom absoluten Ablauf eines Kontos.
5. Prüfe und ändere Richtlinien mit gezielten Kontowerkzeugen.
