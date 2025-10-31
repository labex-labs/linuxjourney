---
index: 9
lang: "de"
title: "Verlauf"
meta_title: "Verlauf - Kommandozeile"
meta_description: "Meistern Sie den history-Befehl in Linux, um Ihre Kommandozeilenaktivität effizient abzurufen und zu verwalten. Erfahren Sie, wie Sie den Verlauf anzeigen, Tastenkombinationen wie Strg-R verwenden und Ihren Verlauf mit Optionen wie history -c und history -d verwalten."
meta_keywords: "history in linux, history -c linux, history -d linux, history -w linux, history befehl unix, bash verlauf, kommandozeile, strg-r, verlauf löschen"
---

## Lesson Content

Ihre Shell speichert eine Aufzeichnung der Befehle, die Sie zuvor eingegeben haben. Sie können auf diese Liste zugreifen, was unglaublich nützlich ist, wenn Sie einen Befehl finden und wiederverwenden möchten, ohne ihn erneut einzutippen. Der Befehl `history` ist ein grundlegendes Werkzeug in den meisten Unix- und Linux-Umgebungen.

### Anzeigen Ihrer Befehlshistorie

Um die Liste der verwendeten Befehle anzuzeigen, geben Sie einfach den Befehl `history` ein. Diese Funktion bietet ein detailliertes Protokoll Ihrer Aktivitäten und erleichtert die Nachverfolgung Ihrer `history in linux`.

```bash
history
```

### Erneutes Ausführen früherer Befehle

Die Shell bietet mehrere Tastenkombinationen, um das erneute Ausführen von Befehlen zu vereinfachen.

- **Pfeil nach oben**: Möchten Sie denselben Befehl erneut ausführen, den Sie gerade verwendet haben? Drücken Sie einfach die Pfeil-nach-oben-Taste, um rückwärts durch Ihre Historie zu blättern.
- **Die `!!`-Tastenkombination**: Um den letzten Befehl erneut auszuführen, können Sie `!!` verwenden. Wenn Sie beispielsweise gerade `cat file1` ausgeführt haben, führt die Eingabe von `!!` und das Drücken der Eingabetaste dazu, dass `cat file1` erneut ausgeführt wird.

### Durchsuchen Ihrer Historie

Eine der leistungsstärksten History-Tastenkombinationen ist `Ctrl-R`. Dies startet eine umgekehrte Suche. Nachdem Sie `Ctrl-R` gedrückt haben, beginnen Sie mit der Eingabe eines Teils des gesuchten Befehls, und die Shell zeigt die zuletzt gefundene Übereinstimmung an. Sie können `Ctrl-R` wiederholt drücken, um ältere Übereinstimmungen zu durchlaufen. Sobald Sie den gewünschten Befehl gefunden haben, drücken Sie einfach die Eingabetaste, um ihn auszuführen.

### Verwalten der History-Liste

Über das einfache Anzeigen Ihrer Historie hinaus können Sie diese auch direkt verwalten.

- **Historie löschen**: Wenn Sie die Befehlshistorie für Ihre aktuelle Sitzung löschen möchten, können Sie den Befehl `history -c linux` verwenden. Dadurch werden alle Einträge aus der History-Liste im Speicher entfernt.
- **In Datei schreiben**: Um die Historie der aktuellen Sitzung in Ihre History-Datei (normalerweise `~/.bash_history`) zu speichern, können Sie `history -w linux` verwenden. Dies ist nützlich, um Befehle zu sichern, bevor Sie eine Sitzung beenden.
- **Einen bestimmten Eintrag löschen**: Sie können einen einzelnen Befehl aus Ihrer Historie entfernen, indem Sie `history -d <offset>` verwenden. Der Offset ist die Nummer, die neben dem Befehl in der `history`-Ausgabe angezeigt wird. Zum Beispiel würde `history -d 101` den 101. Eintrag löschen. Dies ist eine Schlüsselfunktion von `history -d linux`.

### Andere nützliche Terminal-Tools

Wenn sich Ihr Terminalfenster füllt, möchten Sie es möglicherweise bereinigen. Verwenden Sie den Befehl `clear`, um die Anzeige zu löschen und mit einem neuen Bildschirm zu beginnen.

```bash
clear
```

Eine weitere unverzichtbare Funktion ist die Tab-Vervollständigung. Wenn Sie beginnen, den Anfang eines Befehls, Dateinamens oder Verzeichnisses einzugeben und die Tab-Taste drücken, versucht die Shell, diesen zu vervollständigen. Wenn es mehrere Möglichkeiten gibt, werden Ihnen möglicherweise die Optionen angezeigt oder es passiert nichts. Das zweimalige Drücken der Tab-Taste listet oft alle möglichen Vervollständigungen auf.

## Exercise

Obwohl es für dieses Thema keine spezifischen Übungen gibt, empfehlen wir Ihnen, den umfassenden [Linux Lernpfad](https://labex.io/de/learn/linux) zu erkunden, um verwandte Linux-Fähigkeiten und -Konzepte zu üben.

## Quiz Question

Was ist der Befehl zum Löschen des Terminals? (Bitte antworten Sie nur in Kleinbuchstaben auf Englisch)

## Quiz Answer

clear
