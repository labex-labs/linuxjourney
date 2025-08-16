---
lang: "de"
title: "Authentifizierungsprotokollierung"
description: "Erfahren Sie mehr über die Linux-Authentifizierungsprotokollierung mit /var/log/auth.log. Verstehen Sie Benutzeranmeldungen und beheben Sie Zugriffsprobleme mit diesem wichtigen Leitfaden."
keywords: "Linux-Authentifizierung, auth.log, Linux-Protokollierung, Benutzeranmeldung, Linux-Sicherheit, Anfänger, Tutorial, Leitfaden"
---

## Lesson Content

Die Authentifizierungsprotokollierung kann sehr nützlich sein, wenn Sie Probleme beim Anmelden haben.

### /var/log/auth.log

Diese Datei enthält Systemautorisierungsprotokolle, wie z. B. Benutzeranmeldungen und die verwendeten Authentifizierungsmethoden.

Beispielausschnitt:

```plaintext
Jan 31 10:37:50 icebox pkexec: pam_unix(polkit-1:session): session opened for user root by (uid=1000)
```

## Exercise

Führen Sie einige fehlgeschlagene Anmeldeversuche und anschließend einen erfolgreichen durch. Überprüfen Sie danach Ihre Datei `/var/log/auth.log`, um zu sehen, was passiert ist.

## Quiz Question

Welche Protokolldatei wird für die Benutzerauthentifizierung verwendet?

## Quiz Answer

auth.log
