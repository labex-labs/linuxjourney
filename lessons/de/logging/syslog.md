---
index: 2
lang: "de"
title: "syslog"
meta_title: "syslog - Protokollierung"
meta_description: "Erfahren Sie mehr über syslog und rsyslog in Linux, wie Sie Systemprotokolle verwalten und den logger-Befehl verwenden. Starten Sie mit diesem anfängerfreundlichen Tutorial!"
meta_keywords: "syslog, rsyslog, Linux-Protokolle, logger-Befehl, /var/log/syslog, Linux-Tutorial, Linux für Anfänger, Systemprotokollierung"
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

Diese Regeln für Protokolldateien werden durch den Selektor in der linken Spalte und die Aktion in der rechten Spalte gekennzeichnet. Die Aktion sagt uns, wohin die Protokollinformationen gesendet werden sollen: an eine Datei, Konsole usw. Denken Sie daran, dass nicht jede Anwendung und jeder Dienst rsyslog zur Verwaltung ihrer Protokolle verwendet. Wenn Sie also genau wissen möchten, was protokolliert wird, müssen Sie in diesem Verzeichnis nachsehen.

Sehen wir uns die Protokollierung in Aktion an; Sie können ein Protokoll manuell mit dem Befehl `logger` senden:

```bash
logger -s Hello
```

Schauen Sie nun in Ihr `/var/log/syslog`, und Sie sollten diesen Eintrag in Ihren Protokollen sehen!

## Exercise

Sehen Sie sich Ihre Konfigurationsdatei `/etc/rsyslog.d` an und prüfen Sie, was sonst noch über den System-Logger protokolliert wird.

## Quiz Question

Welchen Befehl können Sie verwenden, um eine Nachricht manuell zu protokollieren?

## Quiz Answer

logger
