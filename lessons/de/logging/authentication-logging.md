---
index: 5
lang: "de"
title: "Authentifizierungs-Protokollierung"
meta_title: "Authentifizierungs-Protokollierung - Protokollierung"
meta_description: "Erkunden Sie die Linux-Authentifizierungs-Protokollierung durch die Untersuchung der Datei /var/log/auth.log. Dieser Leitfaden hilft Anfängern, Benutzeranmeldeereignisse, Authentifizierungsmethoden und die Fehlerbehebung bei Zugriffsproblemen für eine bessere Linux-Sicherheit zu verstehen."
meta_keywords: "Linux-Authentifizierung, auth.log, Linux-Protokollierung, Benutzeranmeldung, Linux-Sicherheit, Systemautorisierung, Anmeldeprobleme beheben, Authentifizierungsmethoden, Anfänger, Tutorial, Leitfaden, sicheres Protokoll"
---

## Lesson Content

Unter Linux ist es für die Sicherheit und Fehlerbehebung von entscheidender Bedeutung, nachzuverfolgen, wer auf ein System zugreift und wie dies geschieht. Dieser Prozess wird durch die Authentifizierungsprotokollierung verwaltet, die alle autorisierungsbezogenen Ereignisse aufzeichnet, wie z. B. Benutzeranmeldungen und die verwendeten Methoden.

### Die auth.log-Datei

Auf Debian-basierten Systemen wie Ubuntu ist die primäre Datei zur Verfolgung dieser Aktivität `/var/log/auth.log`. Diese Protokolldatei enthält Systemautorisierungsinformationen, einschließlich erfolgreicher und fehlgeschlagener Benutzeranmeldeversuche und aller ausgelösten Authentifizierungsmechanismen. Die Überprüfung dieser Datei ist ein wichtiger Schritt bei der Diagnose von Anmeldeproblemen oder der Untersuchung von Sicherheitsvorfällen.

Hier ist ein Beispielausschnitt aus einer `auth.log`-Datei:

```plaintext
Jan 31 10:37:50 icebox pkexec: pam_unix(polkit-1:session): session opened for user root by (uid=1000)
```

### Protokolleinträge verstehen

Jede Zeile im Protokoll liefert wertvolle Details. Im obigen Beispiel:

- **`Jan 31 10:37:50`**: Der Zeitstempel des Ereignisses.
- **`icebox`**: Der Hostname des Computers, auf dem das Ereignis aufgetreten ist.
- **`pkexec`**: Das Programm, das das Ereignis initiiert hat.
- **`pam_unix(polkit-1:session)`**: Das verwendete Authentifizierungsmodul und der Dienst.
- **`session opened for user root by (uid=1000)`**: Die durchgeführte Aktion – eine Sitzung wurde für den Benutzer `root` von einem Benutzer mit der UID `1000` geöffnet.

### Alternative Protokolldateien

Es ist wichtig zu beachten, dass der Speicherort der Authentifizierungsprotokolle zwischen verschiedenen Linux-Distributionen variieren kann. Auf Red Hat-basierten Systemen wie CentOS und Fedora werden diese Ereignisse beispielsweise typischerweise in `/var/log/secure` anstelle von `/var/log/auth.log` aufgezeichnet.

## Exercise

Übung macht den Meister! Hier sind einige praktische Labs, um Ihr Verständnis von Benutzerauthentifizierung und Kontoverwaltung zu festigen:

1. **[Konfigurieren von Benutzerkonten und Sudo-Berechtigungen in Linux](https://labex.io/de/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** – Üben Sie die Durchsetzung von Passwortrichtlinien, das Sperren/Entsperren von Benutzerkonten, die Sicherung des Root-Kontos und die Gewährung administrativer Berechtigungen, was alles entscheidend für das Verständnis der Authentifizierungssicherheit ist.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in die Benutzer- und Sicherheitsverwaltung von Linux aufzubauen.

## Quiz Question

Unter Debian-basierten Systemen, wie lautet der Name der Protokolldatei, die für die Benutzerauthentifizierung verwendet wird? Bitte antworten Sie nur mit dem Dateinamen. Die Antwort ist groß- und kleingeschrieben.

## Quiz Answer

auth.log
