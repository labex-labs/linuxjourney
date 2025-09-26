---
index: 2
lang: "de"
title: "syslog"
meta_title: "syslog - Protokollierung"
meta_description: "Erfahren Sie mehr über syslog und rsyslog unter Linux, wie Sie Systemprotokolle verwalten und den logger-Befehl verwenden. Beginnen Sie mit diesem anfängerfreundlichen Tutorial!"
meta_keywords: "syslog, rsyslog, Linux-Protokolle, logger-Befehl, /var/log/syslog, Linux-Tutorial, Anfänger-Linux, Systemprotokollierung"
---

## Lesson Content

Der syslog-Dienst verwaltet und sendet Protokolle an den System-Logger. Rsyslog ist eine erweiterte Version von syslog; die meisten Linux-Distributionen sollten diese neue Version verwenden. Die Ausgabe aller Protokolle, die der syslog-Dienst sammelt, finden Sie unter `/var/log/syslog` (jede Nachricht außer Authentifizierungsnachrichten).

Um herauszufinden, welche Dateien von unserem System-Logger verwaltet werden, sehen Sie sich die Konfigurationsdateien in `/etc/rsyslog.d` an:

```plaintext
pete@icebox:~$ less /etc/rsyslog.d/50-default.conf
# First some standard log files.  Log by facility.
#
auth,authpriv.*                 /var/log/auth.log
*.*;auth,authpriv.none          -/var/log/syslog
#cron.*                         /var/log/cron.log
#daemon.*                       -/var/log/daemon.log
kern.*                          -/var/log/kern.log
#lpr.*                          -/var/log/lpr.log
mail.*                          -/var/log/mail.log
#user.*                         -/var/log/user.log
```

Diese Regeln für Protokolldateien werden durch den Selektor in der linken Spalte und die Aktion in der rechten Spalte gekennzeichnet. Die Aktion teilt uns mit, wohin die Protokollinformationen gesendet werden sollen: in eine Datei, auf die Konsole usw. Denken Sie daran, dass nicht jede Anwendung und jeder Dienst rsyslog zur Verwaltung seiner Protokolle verwendet. Wenn Sie also genau wissen möchten, was protokolliert wird, müssen Sie in dieses Verzeichnis schauen.

Sehen wir uns die Protokollierung in Aktion an; Sie können manuell ein Protokoll mit dem Befehl `logger` senden:

```bash
logger -s Hello
```

Schauen Sie nun in Ihre `/var/log/syslog`, und Sie sollten diesen Eintrag in Ihren Protokollen sehen.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis der Linux-Protokollierung und der Dateiansicht zu festigen:

1. **[Anzeigen von Protokoll- und Konfigurationsdateien unter Linux](https://labex.io/de/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - Üben Sie wesentliche Linux-Befehlszeilenfähigkeiten für die effiziente Anzeige und Navigation von Textdateien, einschließlich Systemprotokollen und Konfigurationsdateien.
2. **[Linux tail Befehl: Anzeige des Dateiende](https://labex.io/de/labs/linux-linux-tail-command-file-end-display-214303)** - Lernen Sie den Linux-Befehl `tail` kennen, um das Ende von Textdateien anzuzeigen und zu überwachen, was besonders nützlich für die Echtzeit-Protokollanalyse ist.
3. **[Text mit grep unter Linux suchen](https://labex.io/de/labs/comptia-search-text-with-grep-in-linux-590841)** - Lernen Sie, nach bestimmten Textmustern in Dateien zu suchen, eine unschätzbare Fähigkeit, um Protokolleinträge nach wichtigen Informationen zu durchsuchen.

Diese Labs helfen Ihnen, die Konzepte des Protokollmanagements und der Dateiinspektion in realen Szenarien anzuwenden und Vertrauen in die Linux-Systemadministration aufzubauen.

## Quiz Question

Welchen Befehl können Sie verwenden, um manuell eine Nachricht zu protokollieren?

## Quiz Answer

logger
