---
lesson_id: "security-event-correlation"
course_id: "security-logs"
lang: "de"
order_index: 5
title: "Ereigniskorrelation"
description: "Lerne, Sicherheitseinträge anhand von Zeit, Host, Konto und Sitzung miteinander zu verknüpfen."
meta_title: "Ereigniskorrelation – Sicherheitsprotokolle"
meta_description: "Vergleiche kurze SSH- und sudo-Einträge, bringe Zeitstempel auf eine gemeinsame Basis und prüfe, welche Belege für einen Zusammenhang sprechen."
meta_keywords: "Ereigniskorrelation, Sicherheitsprotokolle, SSH-Anmeldungen, sudo-Ereignisse, Zeitstempel, Sitzungs-IDs"
---

Ein Eintrag meldet eine Anmeldung an einem Rechner. Ein anderer zeigt, dass ein Befehl erlaubt wurde. Hängen die beiden zusammen? Bei der **Ereigniskorrelation** vergleichst du Protokolleinträge, um herauszufinden, ob sie zusammengehörige Aktivitäten beschreiben.

## Zwei Einträge lesen

Über SSH kannst du dich an einem anderen Rechner anmelden. Danach kann eine Person mit `sudo` anfragen, ob sie einen Befehl unter einem anderen Konto ausführen darf. Die beiden simulierten Einträge stammen vom selben Tag und verwenden einheitliche Feldnamen. Echte Protokolle können andere Namen verwenden oder Felder auslassen.

```text
t=09:14:02Z      source=ssh   host=web-01 account=alex session=42 login=accepted
t=11:15:10+02:00 source=sudo  host=web-01 account=alex session=42 decision=allowed
```

Das Feld `source` nennt das Werkzeug, das das Ereignis meldet. `host` bezeichnet den Rechner, auf dem es stattfand. Beide Einträge melden Aktivitäten unter dem Konto `alex`. Um festzustellen, wer das Konto verwendet hat, brauchst du weitere Belege.

:::single-choice{#security-event-correlation-account-evidence} Jemand im Team sagt, Alex habe die sudo-Anfrage persönlich gestellt. Was belegen die Einträge bisher?

::option[Alex hat die sudo-Anfrage persönlich gestellt.]{#security-event-correlation-account-person explanation="Aus einem Kontonamen allein geht nicht hervor, wer das Konto benutzt hat."}
::option[Die Einträge melden Aktivitäten zweier Konten.]{#security-event-correlation-account-different explanation="In beiden account-Feldern steht alex. Die unterschiedlichen source-Werte bezeichnen die meldenden Werkzeuge."}
::option[Beide Ereignisse nennen dasselbe Konto.]{#security-event-correlation-account-shared .correct explanation="Beide Einträge nennen alex. Wer das Konto benutzt hat, lässt sich erst mit weiteren Belegen bestimmen."}
:::

## Ereigniszeiten vergleichen

Das Feld `t` enthält die erfasste Uhrzeit. Im ersten Eintrag kennzeichnet `Z` die UTC, eine gemeinsame Grundlage für den Vergleich. Der zweite Eintrag verwendet `+02:00`. Die dort angezeigte Uhrzeit ist UTC um zwei Stunden voraus. Ziehe von `11:15:10` zwei Stunden ab, um `09:15:10` UTC zu erhalten.

Vergleiche jetzt `09:14:02` mit `09:15:10`. Die Anmeldung wurde früher erfasst. Zeitlich nahe Ereignisse können dennoch zu verschiedenen Anmeldungen gehören.

:::single-choice{#security-event-correlation-time-order} An einem anderen Tag wird eine Anmeldung um `09:14Z` und eine Anfrage um `11:13+02:00` protokolliert. In welcher Reihenfolge geschahen sie?

::option[Die Anfrage kommt eine Minute früher.]{#security-event-correlation-time-request-first .correct explanation="Ziehst du bei der Anfrage zwei Stunden ab, erhältst du 09:13 UTC. Die Anmeldung war um 09:14 UTC."}
::option[Die Anmeldung kommt eine Minute früher.]{#security-event-correlation-time-login-first explanation="Die Anfrage entspricht 09:13 UTC und liegt eine Minute vor der Anmeldung um 09:14 UTC."}
::option[Die Anmeldung kommt fast zwei Stunden früher.]{#security-event-correlation-time-unadjusted explanation="Diese Antwort vergleicht die angezeigten Uhrzeiten direkt. Rechne beide Zeiten zuerst in UTC um."}
:::

## Host und Sitzung prüfen

Eine **Sitzung** reicht von der Anmeldung bis zur Abmeldung oder zum Verbindungsabbruch. In diesen Übungseinträgen enthält der SSH-Eintrag die Sitzungs-ID der akzeptierten Anmeldung. Beide Quellen verwenden für dieselbe Anmeldung auf demselben Host dieselbe Sitzungs-ID. In den ersten beiden Zeilen stehen `host=web-01` und `session=42`. Das verbindet die Anmeldung und die Anfrage mit einer Sitzung.

In diesen Beispielen gilt eine Sitzungsnummer nur auf ihrem jeweiligen Host. Der folgende Eintrag nennt dasselbe Konto und dieselbe Sitzungsnummer und erscheint nur wenige Sekunden später.

```text
t=09:15:18Z source=sudo host=web-02 account=alex session=42 decision=allowed
```

![LabEx-Terminal mit simulierten Einträgen von web-01 und web-02 sowie der Umrechnung auf 09:15:10 UTC](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/security-logs/security-event-correlation/utc-correlation.png)

Das Terminal zeigt die drei simulierten Einträge. Der Ubuntu-Befehl `date` bestätigt die Umrechnung in UTC.

:::single-choice{#security-event-correlation-host-scope} In welchem Verhältnis steht der dritte Eintrag zur ursprünglichen SSH-Sitzung?

::option[Er gehört wegen desselben Kontos und der zeitlichen Nähe zu dieser Sitzung.]{#security-event-correlation-host-scope-account explanation="Zwei Hosts können innerhalb weniger Sekunden Aktivitäten unter demselben Kontonamen melden."}
::option[Er gehört zu einer anderen Sitzung, weil der Host ein anderer ist.]{#security-event-correlation-host-scope-machine .correct explanation="Sitzung 42 auf web-02 gilt für diesen Host. Die ursprüngliche Anmeldung fand auf web-01 statt."}
::option[Er gehört wegen derselben Sitzungsnummer zu dieser Sitzung.]{#security-event-correlation-host-scope-session explanation="Die Nummer ist in diesem Beispiel nur auf dem jeweiligen Host aussagekräftig. Hier sind die Hostnamen verschieden."}
:::

## Die Aussage auf die Belege stützen

Auf `web-01` wurde die Anmeldung akzeptiert und `sudo` erlaubte während der Sitzung einen Befehl. Das belegen die verfügbaren Einträge. Um zu erfahren, wie der Befehl endete, suche nach einem Ergebniseintrag. Eine Sitzung kann mehrere Befehle umfassen. Ordne das Ergebnis deshalb der konkreten Anfrage zu. Bis du einen passenden Eintrag findest, bleibt das Ergebnis offen.

:::single-choice{#security-event-correlation-completion-evidence} Welcher neue Eintrag könnte zeigen, ob der Befehl erfolgreich war?

::option[Das Ergebnis eines anderen Befehls in derselben Sitzung.]{#security-event-correlation-completion-other-command explanation="In einer Sitzung können mehrere Befehle laufen. Das Ergebnis muss zur geprüften Anfrage passen."}
::option[Ein zweiter Eintrag, der die Erlaubnis der Anfrage meldet.]{#security-event-correlation-completion-permission explanation="Das bestätigt die Berechtigung. Für den Ausgang brauchst du weiterhin einen Ergebniseintrag."}
::option[Ein Ergebniseintrag für den Befehl aus genau dieser Anfrage.]{#security-event-correlation-completion-result .correct explanation="Ein passender Eintrag kann zeigen, wie der Befehl endete."}
:::

Um weitere Authentifizierungs- und sudo-Einträge zu filtern und zu vergleichen, probiere die [Analyse von Systemprotokollen](https://labex.io/tutorials/linux-system-log-analysis-656124) aus.

## Zusammenfassung

Du kannst jetzt mehrere Sicherheitseinträge auswerten und feststellen, welche Fragen offenbleiben.

1. Das Konto erkennen, das in einem Ereignis genannt wird.
2. Zeitstempel vor dem Vergleich in eine gemeinsame Zeitzone umrechnen.
3. Host und Sitzung gemeinsam nutzen, um Aktivitäten zuzuordnen.
4. Festhalten, was die Einträge belegen, und passende Belege für die offene Frage suchen.
