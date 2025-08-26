---
index: 3
lang: "de"
title: "/etc/passwd"
meta_title: "/etc/passwd - Benutzerverwaltung"
meta_description: "Erfahren Sie mehr über die Datei /etc/passwd in Linux, verstehen Sie die Felder der Benutzerinformationen und wie UIDs funktionieren. Erkunden Sie diese essentielle Konfigurationsdatei."
meta_keywords: "/etc/passwd, Linux-Benutzer, Benutzer-ID, UID, Linux-Tutorial, Anfänger, Leitfaden, Linux-Befehle"
---

## Lesson Content

Denken Sie daran, dass Benutzernamen nicht wirklich Identifikationen für Benutzer sind. Das System verwendet eine Benutzer-ID (UID), um einen Benutzer zu identifizieren. Um herauszufinden, welche Benutzer welcher ID zugeordnet sind, sehen Sie sich die Datei `/etc/passwd` an.

```bash
cat /etc/passwd
```

Diese Datei zeigt Ihnen eine Liste der Benutzer und detaillierte Informationen über sie. Zum Beispiel sieht die erste Zeile in dieser Datei höchstwahrscheinlich so aus:

```plaintext
root:x:0:0:root:/root:/bin/bash
```

Jede Zeile zeigt Benutzerinformationen für einen Benutzer an; am häufigsten sehen Sie den root-Benutzer als erste Zeile. Es gibt viele durch Doppelpunkte getrennte Felder, die Ihnen zusätzliche Informationen über den Benutzer geben. Schauen wir uns alle an:

1. **Benutzername**
2. **Benutzerpasswort** – Das Passwort wird nicht wirklich in dieser Datei gespeichert; es wird normalerweise in der Datei `/etc/shadow` gespeichert. Wir werden in der nächsten Lektion mehr über `/etc/shadow` besprechen, aber vorerst sollten Sie wissen, dass es verschlüsselte Benutzerpasswörter enthält. Sie können viele verschiedene Symbole in diesem Feld sehen: Wenn Sie ein „x“ sehen, bedeutet dies, dass das Passwort in der Datei `/etc/shadow` gespeichert ist; ein „*“ bedeutet, dass der Benutzer keinen Anmeldezugriff hat; und wenn das Feld leer ist, bedeutet dies, dass der Benutzer kein Passwort hat.
3. **Die Benutzer-ID** – Wie Sie sehen können, hat root die UID 0.
4. **Die Gruppen-ID**
5. **GECOS-Feld** – Dies wird verwendet, um allgemeine Kommentare über den Benutzer oder das Konto zu hinterlassen, wie z. B. den richtigen Namen oder die Telefonnummer. Es ist durch Kommas getrennt.
6. **Home-Verzeichnis des Benutzers**
7. **Shell des Benutzers** – Sie werden wahrscheinlich sehen, dass viele Benutzer standardmäßig bash als Shell verwenden.

Normalerweise würden Sie auf der Einstellungsseite eines Benutzers nur menschliche Benutzer erwarten. Sie werden jedoch feststellen, dass `/etc/passwd` andere Benutzer enthält. Denken Sie daran, dass Benutzer im System wirklich nur dazu da sind, Prozesse mit unterschiedlichen Berechtigungen auszuführen. Manchmal möchten wir Prozesse mit vorbestimmten Berechtigungen ausführen. Zum Beispiel wird der `daemon`-Benutzer für Daemon-Prozesse verwendet.

Es sollte auch beachtet werden, dass Sie die Datei `/etc/passwd` manuell bearbeiten können, wenn Sie Benutzer hinzufügen und Informationen mit dem Tool `vipw` ändern möchten. Solche Dinge überlässt man jedoch am besten den Tools, die wir in einer späteren Lektion besprechen werden, wie `useradd` und `userdel`.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis von Linux-Benutzerkonten und deren Verwaltung zu vertiefen:

1. **[Linux-Benutzerkonten mit useradd, usermod und userdel verwalten](https://labex.io/de/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** – Üben Sie den gesamten Lebenszyklus der Benutzerverwaltung, vom Erstellen und Sichern neuer Konten bis zum Ändern und Löschen.
2. **[Linux-Gruppen mit groupadd, usermod und groupdel verwalten](https://labex.io/de/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** – Sammeln Sie praktische Erfahrungen mit den wichtigsten Befehlszeilen-Dienstprogrammen für die Gruppenverwaltung, einschließlich des Erstellens neuer Gruppen und des Änderns von Benutzerzugehörigkeiten.
3. **[Benutzerkonten und Sudo-Berechtigungen in Linux konfigurieren](https://labex.io/de/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** – Lernen Sie wesentliche Techniken zur Verwaltung von Benutzerkonten und Sudo-Berechtigungen, um die Sicherheit eines Linux-Systems zu verbessern.

Diese Übungen helfen Ihnen, die Konzepte von Benutzer-IDs und Kontoverwaltung in realen Szenarien anzuwenden und Vertrauen in die Linux-Benutzerverwaltung aufzubauen.

## Quiz Question

Wenn ein Benutzer keinen Anmeldezugriff hat, wie wird das in `/etc/passwd` gekennzeichnet?

## Quiz Answer

*
