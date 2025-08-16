---
lang: "de"
title: "/etc/passwd"
description: "Erfahren Sie mehr über die Datei /etc/passwd in Linux, verstehen Sie die Felder der Benutzerinformationen und wie UIDs funktionieren. Erkunden Sie diese essentielle Konfigurationsdatei."
keywords: "/etc/passwd, Linux-Benutzer, Benutzer-ID, UID, Linux-Tutorial, Anfänger, Anleitung, Linux-Befehle"
---

## Lesson Content

Denken Sie daran, dass Benutzernamen nicht wirklich Identifikationen für Benutzer sind. Das System verwendet eine Benutzer-ID (UID), um einen Benutzer zu identifizieren. Um herauszufinden, welche Benutzer welcher ID zugeordnet sind, sehen Sie sich die Datei `/etc/passwd` an.

```bash
cat /etc/passwd
```

Diese Datei zeigt Ihnen eine Liste von Benutzern und detaillierte Informationen über sie. Zum Beispiel sieht die erste Zeile in dieser Datei höchstwahrscheinlich so aus:

```plaintext
root:x:0:0:root:/root:/bin/bash
```

Jede Zeile zeigt Benutzerinformationen für einen Benutzer an; am häufigsten sehen Sie den root-Benutzer als erste Zeile. Es gibt viele Felder, die durch Doppelpunkte getrennt sind und Ihnen zusätzliche Informationen über den Benutzer geben. Schauen wir sie uns alle an:

1. **Benutzername**
2. **Benutzerpasswort** - Das Passwort wird nicht wirklich in dieser Datei gespeichert; es wird normalerweise in der Datei `/etc/shadow` gespeichert. Wir werden in der nächsten Lektion mehr über `/etc/shadow` besprechen, aber vorerst sollten Sie wissen, dass es verschlüsselte Benutzerpasswörter enthält. Sie können viele verschiedene Symbole in diesem Feld sehen: Wenn Sie ein "x" sehen, bedeutet das, dass das Passwort in der Datei `/etc/shadow` gespeichert ist; ein "\*" bedeutet, dass der Benutzer keinen Anmeldezugriff hat; und wenn ein leeres Feld vorhanden ist, bedeutet das, dass der Benutzer kein Passwort hat.
3. **Die Benutzer-ID** - Wie Sie sehen können, hat root die UID 0.
4. **Die Gruppen-ID**
5. **GECOS field** - Dies wird verwendet, um allgemeine Kommentare über den Benutzer oder das Konto zu hinterlassen, wie z.B. den richtigen Namen oder die Telefonnummer. Es ist durch Kommas getrennt.
6. **Home-Verzeichnis des Benutzers**
7. **Shell des Benutzers** - Sie werden wahrscheinlich sehen, dass viele Benutzer standardmäßig bash als Shell verwenden.

Normalerweise würden Sie auf der Einstellungsseite eines Benutzers nur menschliche Benutzer erwarten. Sie werden jedoch feststellen, dass `/etc/passwd` andere Benutzer enthält. Denken Sie daran, dass Benutzer wirklich nur auf dem System sind, um Prozesse mit unterschiedlichen Berechtigungen auszuführen. Manchmal möchten wir Prozesse mit vorbestimmten Berechtigungen ausführen. Zum Beispiel wird der `daemon`-Benutzer für Daemon-Prozesse verwendet.

Es sollte auch beachtet werden, dass Sie die Datei `/etc/passwd` manuell bearbeiten können, wenn Sie Benutzer hinzufügen und Informationen mit dem `vipw`-Tool ändern möchten. Solche Dinge überlässt man jedoch am besten den Tools, die wir in einer späteren Lektion besprechen werden, wie `useradd` und `userdel`.

## Exercise

Schauen Sie sich Ihre `/etc/passwd`-Datei an, sehen Sie sich einige der Benutzer an und notieren Sie den Zugriff, den sie haben.

## Quiz Question

Wenn ein Benutzer keinen Anmeldezugriff hat, wie wird das in `/etc/passwd` gekennzeichnet?

## Quiz Answer

-
