---
lesson_id: "upstart-jobs"
course_id: "init"
lang: "de"
order_index: 4
title: "Upstart-Jobs"
description: "Erfahre, wie du Jobs auf einem bestätigten älteren Upstart-System mit `initctl` untersuchst und steuerst."
meta_title: "Upstart-Jobs – Init"
meta_description: "Eine Anleitung zur Verwaltung von Diensten mit Upstart-Jobs in einer Linux-Umgebung. Lerne, mit initctl Jobs auf einem Upstart-Linux-System aufzulisten, zu starten, zu stoppen und neu zu starten."
meta_keywords: "Upstart-Jobs, initctl, Upstart Linux, Linux-Dienste, Systemadministration, init-System, Linux-Tutorial"
---

`initctl` kommuniziert mit einem laufenden Upstart-init-Daemon. Verwende es erst, nachdem du bestätigt hast, dass im betreffenden PID-Namensraum tatsächlich Upstart läuft; nutze auf einem aktuellen systemd-Host stattdessen die nativen Werkzeuge von systemd.

## Jobstatus auflisten und lesen

Liste bekannte Jobs und Instanzen auf:

```bash
$ initctl list
```

Untersuche einen einzelnen Job:

```bash
$ initctl status networking
networking start/running
```

Upstart meldet sowohl ein **Ziel** wie `start` oder `stop` als auch einen aktuellen **Zustand** wie `running` oder `waiting`. `stop/waiting` bedeutet, dass der Job nicht läuft und auf eine Startbedingung oder eine manuelle Anforderung wartet; dies weist nicht unbedingt auf einen Fehler hin.

:::single-choice{#upstart-jobs-stop-waiting} Was bedeutet `stop/waiting` normalerweise in der Statusausgabe von Upstart?

::option[Der Job läuft, verbraucht aber keine CPU-Zeit.]{#upstart-jobs-running-idle explanation="Ein laufender Job würde normalerweise das Ziel start und den Zustand running anzeigen."}
::option[Das Ziel des Jobs ist Stopp, und es läuft keine Prozessinstanz.]{#upstart-jobs-stopped-waiting .correct explanation="Die Definition bleibt bekannt, während Upstart auf eine spätere Bedingung oder einen Befehl wartet."}
::option[Das gesamte Betriebssystem wartet auf das Ausschalten.]{#upstart-jobs-system-poweroff explanation="Das Paar beschreibt diese Jobinstanz und nicht unbedingt den globalen Systemzustand."}
:::

## Einen Job starten und stoppen

Nachdem du Abhängigkeiten und Auswirkungen geprüft hast:

```bash
$ sudo initctl start JOB_NAME
$ sudo initctl stop JOB_NAME
```

Jobs können mehrere Instanzen definieren, die durch Umgebungsvariablen unterschieden werden. Gib in diesem Fall genau die von der Konfiguration verlangten Variablen an und verwende sie auch beim Abfragen oder Stoppen einer Instanz. Das Starten von Jobs für Netzwerk, Speicher, Authentifizierung oder Fernzugriff kann die Sitzung unterbrechen; halte deshalb einen Konsolenzugang zur Wiederherstellung bereit.

:::single-choice{#upstart-jobs-start-command} Welcher Befehl fordert den manuellen Start des Jobs `peanuts` an?

::option[`sudo initctl start peanuts`]{#upstart-jobs-start-peanuts .correct explanation="Auf den Unterbefehl start folgen der konfigurierte Jobname und alle erforderlichen Instanzvariablen."}
::option[`sudo initctl peanuts start`]{#upstart-jobs-name-first explanation="Bei der initctl-Syntax steht der Unterbefehl vor dem Jobnamen."}
::option[`sudo systemctl initctl peanuts`]{#upstart-jobs-systemctl-mixed explanation="Dies vermischt fälschlich die Schnittstellen zweier unterschiedlicher Dienstmanager."}
:::

## Neustart und Konfigurationsänderungen

Fordere einen Neustart eines bereits laufenden Jobs an mit:

```bash
$ sudo initctl restart peanuts
```

Bei Upstart entspricht `restart` nach der Bearbeitung einer Jobdatei nicht immer einem frischen `stop` gefolgt von `start`: Die bestehende Konfiguration des laufenden Jobs kann maßgeblich bleiben. Validiere die geänderte `.conf`-Datei, weise Upstart entsprechend der installierten Version an, die Konfiguration neu zu laden, und befolge das dokumentierte Stopp-/Startverfahren, wenn die neue Konfiguration wirksam werden muss.

Ein Neustart verursacht eine Unterbrechung und kann den Dienst möglicherweise nicht wieder in Betrieb bringen. Prüfe anschließend den tatsächlichen Endpunkt und die Protokolle.

:::single-choice{#upstart-jobs-restart-peanuts} Welcher Befehl fordert einen Neustart des laufenden Upstart-Jobs `peanuts` an?

::option[`sudo initctl restart peanuts`]{#upstart-jobs-restart-command .correct explanation="Der Unterbefehl restart wirkt über die Upstart-Steuerungsschnittstelle auf den benannten Job."}
::option[`sudo initctl emit peanuts`]{#upstart-jobs-emit-not-restart explanation="Das Ausgeben eines Ereignisses beeinflusst passende Jobbedingungen und ist keine direkte Neustartanforderung."}
::option[`sudo service --status-all peanuts`]{#upstart-jobs-status-all explanation="Eine Statusauflistung fordert keinen Neustart an."}
:::

## Jobkonfiguration validieren

Bevor du eine geänderte Jobdatei installierst, verwende das von der älteren Distribution bereitgestellte Validierungswerkzeug, häufig `init-checkconf`, und prüfe eingebundene Skripte, Umgebung, Benutzer-/Gruppeneinstellungen, Respawn-Richtlinie und Ereignisausdrücke. Lade die Definitionen danach mit dem zur Version passenden Arbeitsablauf `initctl reload-configuration` neu.

Eine Syntaxvalidierung kann nicht beweisen, dass Pfade existieren, Anmeldedaten die Ausführung erlauben, Ereignisse eintreffen oder der Prozess betriebsbereit wird. Teste in einer Umgebung mit Wiederherstellungsmöglichkeit.

:::single-choice{#upstart-jobs-syntax-validation-limit} Was kann die Syntaxvalidierung eines Jobs nicht beweisen?

::option[Dass der Dienst erfolgreich startet und betriebsbereit wird.]{#upstart-jobs-runtime-not-proven .correct explanation="Laufzeitpfade, Berechtigungen, Abhängigkeiten und Ereignisfluss erfordern einen tatsächlichen kontrollierten Test."}
::option[Dass der Konfigurationstext überhaupt geparst werden kann.]{#upstart-jobs-parse-purpose explanation="Das Parsen ist genau der Hauptzweck der Syntaxvalidierung."}
::option[Dass dem Validator eine Datei übergeben wurde.]{#upstart-jobs-file-supplied explanation="Das Werkzeug kann fehlende Eingaben sofort melden."}
:::

## Ereignisse mit Bedacht ausgeben

Upstart kann ein benanntes Ereignis ausgeben:

```bash
$ sudo initctl emit EVENT_NAME
```

Jeder Job, dessen Start- oder Stopp-Ausdruck passt, kann reagieren. Ein Ereignis ist nicht an einen einzelnen Job adressiert, und seine Auswirkungen können sich durch weitere Ereignisse fortsetzen. Untersuche alle passenden Konfigurationen, bevor du ein benutzerdefiniertes oder Systemereignis ausgibst; spiele zentrale Boot-Ereignisse auf einem Produktionshost nicht leichtfertig erneut ab.

:::single-choice{#upstart-jobs-emit-scope} Was kann geschehen, wenn `initctl emit EVENT_NAME` ausgeführt wird?

::option[Alle Jobausdrücke, die zu diesem Ereignis passen, können ihren Zustand wechseln.]{#upstart-jobs-event-matches .correct explanation="Ereignisse werden in Upstarts Abhängigkeitsmodell ausgestrahlt und nicht nur an einen benannten Dienst gesendet."}
::option[Nur ein Job, dessen Name genau dem Ereignis entspricht, kann reagieren.]{#upstart-jobs-event-name-only explanation="Die Übereinstimmung wird durch Ausdrücke mit `start on` und `stop on` definiert, nicht durch die Gleichheit von Job- und Ereignisname."}
::option[Das Ereignis wird für immer als Nachricht in einer dauerhaften Warteschlange gespeichert.]{#upstart-jobs-event-durable explanation="Upstart-Ereignisse sind Lebenszyklusbenachrichtigungen und keine allgemeine dauerhafte Nachrichtenwarteschlange."}
:::

## Zusammenfassung

Du kannst Upstart-Jobs nun mit eindeutigem Zustandsverständnis und klarem Ereignisumfang bedienen.

1. Lies Ziel und Zustand in der `initctl`-Ausgabe getrennt.
2. Starte und stoppe nach Prüfung der Auswirkungen genau die beabsichtigte Jobinstanz.
3. Behandle Neustart und geänderte Jobkonfiguration als getrennte Belange.
4. Validiere die Syntax und teste anschließend die Betriebsbereitschaft.
5. Prüfe jeden passenden Ausdruck, bevor du ein Ereignis ausgibst.
