---
index: 2
lang: "de"
title: "Root"
meta_title: "Root – Benutzerverwaltung"
meta_description: "Erkunden Sie die Rolle des Root-Benutzers in Linux. Diese Lektion behandelt die Unterschiede zwischen su und sudo für den Erhalt von Superuser-Rechten und erklärt, wie die Datei /etc/sudoers den Zugriff verwaltet."
meta_keywords: "root benutzer in linux, linux root benutzer, su, sudo, sudoers, visudo, superuser, benutzerverwaltung, linux berechtigungen"
---

## Lesson Content

Unter Linux erfordern bestimmte Verwaltungsaufgaben erweiterte Berechtigungen. Diese Berechtigungen gehören zu einem speziellen Konto, das als **root-Benutzer in Linux** bekannt ist. Obwohl Sie sich direkt als Root anmelden können, ist es oft sicherer und besser zu verwalten, temporär auf Superuser-Zugriff zuzugreifen.

### Der Befehl `su`

Neben dem Befehl `sudo` können Sie `su` (Substitute User) verwenden, um Superuser-Berechtigungen zu erlangen. Wenn `su` ohne Benutzernamen ausgeführt wird, versucht es, eine neue Shell-Sitzung für den **Linux-Root-Benutzer** zu öffnen, und fordert Sie zur Eingabe des Root-Passworts auf.

```bash
su
```

Sie können diesen Befehl auch verwenden, um zu jedem anderen Benutzer auf dem System zu wechseln, vorausgesetzt, Sie kennen dessen Passwort.

### Risiken einer dauerhaften Root-Shell

Die Verwendung von `su` zum Öffnen einer Root-Shell hat erhebliche Nachteile. Das kontinuierliche Arbeiten als Root-Benutzer erhöht das Risiko, einen kritischen, systemverändernden Fehler zu machen. Darüber hinaus werden Aktionen, die in einer Root-Shell ausgeführt werden, nicht unter Ihrem persönlichen Benutzerkonto protokolliert, was die Überprüfung von Systemänderungen erschwert. Aus diesen Gründen ist es bewährte Praxis, `sudo` für einzelne Befehle zu verwenden, die Superuser-Zugriff erfordern.

### Die Datei `sudoers`

Wie entscheidet das System also, wer `sudo` verwenden darf? Der Zugriff wird durch eine Konfigurationsdatei unter `/etc/sudoers` gesteuert. Diese Datei listet die Benutzer und Gruppen auf, denen die Berechtigung erteilt wurde, Befehle als Superuser auszuführen.

Um diese Datei sicher zu bearbeiten, sollten Sie immer den Befehl `visudo` verwenden. Dieses Dienstprogramm öffnet die `sudoers`-Datei in einem Texteditor und führt vor dem Speichern eine Syntaxprüfung durch, was hilft, Konfigurationsfehler zu vermeiden, die Sie vom administrativen Zugriff ausschließen könnten.

## Exercise

Bringen Sie Ihr Wissen in die Praxis. Das folgende praktische Labor hilft Ihnen, Ihr Verständnis von Superuser-Zugriff und -Berechtigungen zu festigen:

1. **[Benutzerkonten und Sudo-Berechtigungen in Linux konfigurieren](https://labex.io/de/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Üben Sie die Durchsetzung von Passwortrichtlinien, das Sperren und Entsperren von Benutzerkonten, die Sicherung des Root-Kontos und die Gewährung administrativer Berechtigungen, was direkt mit der Verwaltung des Superuser-Zugriffs zusammenhängt.

Dieses Labor hilft Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in die Verwaltung von Benutzerberechtigungen und Superuser-Zugriff aufzubauen.

## Quiz Question

Welche Datei listet die Benutzer und Gruppen mit `sudo`-Berechtigungen auf? Bitte geben Sie den vollständigen Pfad an. (Hinweis: Ihre Antwort muss auf Englisch und case-sensitiv sein).

## Quiz Answer

/etc/sudoers
