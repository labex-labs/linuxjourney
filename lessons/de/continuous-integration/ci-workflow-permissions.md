---
lesson_id: "ci-workflow-permissions"
course_id: "continuous-integration"
lang: "de"
order_index: 7
title: "Workflow-Berechtigungen"
description: "Lerne, einer gewöhnlichen CI-Prüfung nur den Repository-Zugriff zu geben, den sie braucht."
meta_title: "Workflow-Berechtigungen - Kontinuierliche Integration"
meta_description: "Lerne, einer gewöhnlichen CI-Prüfung nur den Repository-Zugriff zu geben, den sie braucht."
meta_keywords: "Workflow-Berechtigungen, Lesezugriff, kontinuierliche Integration, DevOps, Linux Journey"
---

Ein CI-Job kann Befehle ausführen und dafür Zugangsdaten erhalten. Eine **Berechtigung** legt fest, was der Job damit lesen oder ändern darf. Ein Job, der nur die Seite prüft, braucht in der Regel Lesezugriff auf die Quelldateien.

## Einer Prüfung Lesezugriff geben

Der folgende Ausschnitt für GitHub Actions beschränkt das eingebaute Token des Workflows auf den Lesezugriff auf Repository-Inhalte.

```yaml
permissions:
  contents: read
```

Beim Checkout und beim lokalen Test lassen sich die Repository-Inhalte lesen. Ein Job, der ein Paket veröffentlicht, braucht eine andere Berechtigung für eine andere Ressource. Gib den Veröffentlichungszugriff gezielt dem Job, der ihn braucht.

:::single-choice{#ci-workflow-permissions-choose-permission} Ein Job liest die Seite und führt grep aus. Welche Berechtigung für Repository-Inhalte reicht aus?

::option[Schreibzugriff, weil die Testausgabe im Terminal erscheint.]{#ci-workflow-permissions-choose-permission-a explanation="Ausgabe im Terminal erfordert keinen Schreibzugriff auf die Repository-Inhalte."}
::option[Lesezugriff.]{#ci-workflow-permissions-choose-permission-c .correct explanation="Der Job muss Inhalte abrufen und ändert dabei nichts im Repository."}
::option[Schreibzugriff, weil die Quelle in einem Git-Repository liegt.]{#ci-workflow-permissions-choose-permission-b explanation="Für diese Prüfung reicht es, die Quelldateien zu lesen."}
:::

## Mit vertraulichen Werten umgehen

Ein **Secret** ist ein vertraulicher Wert, etwa ein privates Token. Wenn ein dafür vorgesehener Job ein Secret braucht, verwende den Geheimnisspeicher der Plattform. Bewahre gewöhnliche Seiteneinstellungen getrennt von vertraulichen Werten auf. Routinetests mit einer lokalen Beispieldatei sollten ohne Zugangsdaten zur Veröffentlichung funktionieren.

:::single-choice{#ci-workflow-permissions-secret-needed} Welcher Wert gehört in einen geschützten Geheimnisspeicher?

::option[Private Zugangsdaten zum Hochladen eines Pakets.]{#ci-workflow-permissions-secret-needed-a .correct explanation="Zugangsdaten können Zugriff auf ein anderes System gewähren."}
::option[Der im Test verwendete Text Welcome.]{#ci-workflow-permissions-secret-needed-b explanation="Das ist öffentlicher Beispieltext."}
::option[Der Name des Ausgabeordners dist.]{#ci-workflow-permissions-secret-needed-c explanation="Der Verzeichnisname ist eine gewöhnliche Einstellung."}
:::

## Nützliche Protokolle schreiben

Workflow-Protokolle können mit anderen Personen geteilt werden. Gib die Aktion und ihr Ergebnis an, ohne vertrauliche Werte auszugeben. Eine Fehlermeldung kann zum Beispiel sagen, dass benötigte Zugangsdaten fehlen oder der Zugriff verweigert wurde. Nenne den Namen des Jobs und die Revision, damit die zuständige Person den Fehler untersuchen kann. Der vertrauliche Wert selbst gehört nicht in die Meldung.

:::single-choice{#ci-workflow-permissions-safe-diagnostic} Ein Veröffentlichungsjob kann sich nicht authentifizieren. Welche Meldung hilft bei der Prüfung und schützt zugleich die Zugangsdaten?

::option[Gib die vollständigen Zugangsdaten aus, damit man sie kopieren kann.]{#ci-workflow-permissions-safe-diagnostic-a explanation="Jede Person mit Zugriff auf das Protokoll könnte die ausgegebenen Zugangsdaten sehen."}
::option[Gib alle Umgebungswerte aus, um den Zustand des Jobs zu zeigen.]{#ci-workflow-permissions-safe-diagnostic-c explanation="Eine vollständige Ausgabe der Umgebung kann vertrauliche Werte enthalten."}
::option[Melde, welcher Veröffentlichungsschritt scheiterte und was beim Zugriff passiert ist.]{#ci-workflow-permissions-safe-diagnostic-b .correct explanation="Damit lässt sich die Fehlerstelle finden und der konfigurierte Zugriff separat prüfen."}
:::

## Einen neuen Job prüfen

Ein vorgeschlagener Workflow prüft Seiten bei Pull Requests und fügt einen Job zur Paketveröffentlichung hinzu. Beide Jobs brauchen unterschiedliche Berechtigungen. Beschränke die Prüfung auf den nötigen Lesezugriff und erteile genehmigte Veröffentlichungsrechte nur dort, wo der Workflow tatsächlich veröffentlicht.

:::single-choice{#ci-workflow-permissions-final-application} Welche Anpassung passt am besten zu den Aufgaben der beiden Jobs?

::option[Gib beiden Jobs Schreibzugriff auf das Repository.]{#ci-workflow-permissions-final-application-b explanation="Die Prüfung liest nur die Quelle. Zum Veröffentlichen des Pakets kann eine andere Berechtigung erforderlich sein."}
::option[Verwende dieselben Zugangsdaten zum Hochladen für alle Schritte, damit sich Wiederholungen gleich verhalten.]{#ci-workflow-permissions-final-application-c explanation="Zugangsdaten zum Hochladen werden nur im Veröffentlichungsjob gebraucht."}
::option[Belasse die Prüfung beim Lesezugriff und gib dem Veröffentlichungsjob nur die nötigen Paketberechtigungen.]{#ci-workflow-permissions-final-application-a .correct explanation="So hat jeder Job den Zugriff, den er braucht, und die übrigen Berechtigungen bleiben begrenzt."}
:::

## Zusammenfassung

Du kannst jetzt einschätzen, welche Zugriffe eine kleine CI-Pipeline braucht.

1. Stimme die Repository-Berechtigungen auf die Aufgabe des Jobs ab.
2. Lege private Zugangsdaten in einem geschützten Geheimnisspeicher ab.
3. Protokolliere hilfreiche Fehlermeldungen, ohne vertrauliche Zugangsdaten auszugeben.
