---
lesson_id: "wireshark-display-filters"
course_id: "network-monitoring"
lang: "de"
order_index: 4
title: "Wireshark-Anzeigefilter"
description: "Lerne, die Ansicht eines vorbereiteten Paketmitschnitts mit einem Wireshark-Anzeigefilter einzugrenzen."
meta_title: "Wireshark-Anzeigefilter - Netzwerküberwachung"
meta_description: "Lerne, die Ansicht eines vorbereiteten Paketmitschnitts mit einem Wireshark-Anzeigefilter einzugrenzen."
meta_keywords: "Wireshark, Anzeigefilter, Netzwerküberwachung, Cybersicherheit, Linux Journey"
---

Ein Paketmitschnitt kann viele Protokolle enthalten. Ein **Anzeigefilter** legt in Wireshark fest, welche gespeicherten Pakete du siehst. Er ändert die Ansicht und lässt die Mitschnittdatei unverändert.

## Ein Protokoll auswählen

Speichere den [Beispielmitschnitt](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/examples/network-monitoring/sample.pcap) als `sample.pcap`. Öffne ihn in Wireshark und gib `dns` in das Feld für den Anzeigefilter ein. Ist TShark installiert, kannst du denselben Filter mit diesem Befehl im Linux-Terminal auf die gespeicherte Datei anwenden. Die Datei enthält eine harmlose Namensabfrage und weiteren Beispielverkehr.

```bash
$ tshark -r sample.pcap -Y dns
```

Die Option `-r` liest eine Datei und `-Y` wendet einen Anzeigefilter an. Suche nach einer Abfrage und ihrer Antwort.

:::single-choice{#wireshark-display-filters-display-effect} Die gefilterte Liste zeigt zwei Zeilen weniger als die ursprüngliche Ansicht. Was ist mit den anderen Paketen passiert?

::option[Sie wurden aus der Mitschnittdatei gelöscht.]{#wireshark-display-filters-display-effect-a explanation="Ein Anzeigefilter ändert die sichtbaren Ergebnisse."}
::option[Sie bleiben gespeichert und haben dem Filter nicht entsprochen.]{#wireshark-display-filters-display-effect-b .correct explanation="Entferne den Filter, um wieder alle Pakete zu sehen."}
::option[Sie wurden erneut über das Netz gesendet.]{#wireshark-display-filters-display-effect-c explanation="Das Lesen eines gespeicherten Mitschnitts sendet keine Pakete."}
:::

## Nach einer Adresse filtern

Ein Filter kann sich auch auf ein Paketfeld beziehen. Mit `ip.addr` kannst du nach der IPv4-Quell- oder Zieladresse filtern. Die beiden Gleichheitszeichen vergleichen das Feld mit dem Beispielwert.

```bash
$ tshark -r sample.pcap -Y 'ip.addr == 192.0.2.10'
```

Die Anführungszeichen sorgen dafür, dass die Shell den Ausdruck als ein einziges Argument übergibt. In den angezeigten Zeilen kannst du die Endpunkte erkennen.

:::single-choice{#wireshark-display-filters-address-scope} Ein Paket geht von einer anderen Adresse an 192.0.2.10. Entspricht es dem Filter?

::option[Ja, weil die Bedingung beide Endpunkte berücksichtigt.]{#wireshark-display-filters-address-scope-a .correct explanation="Das Feld ip.addr kann auf die Quelle oder auf das Ziel passen."}
::option[Nein, weil die Bedingung nur die Quelle prüft.]{#wireshark-display-filters-address-scope-b explanation="Dieses Feld berücksichtigt beide Richtungen."}
::option[Nur wenn das Paket DNS-Daten enthält.]{#wireshark-display-filters-address-scope-c explanation="Dieser Ausdruck prüft nur die IPv4-Adresse."}
:::

![Aufgezeichnete TShark-Ausgabe mit der DNS-Ansicht und der Ansicht beider Protokolle im Übungsmitschnitt](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/network-monitoring/wireshark-display-filters/saved-dns-exchange.png)

## Eine leere Ansicht erklären

Ein leeres Ergebnis bedeutet, dass der Filter in der untersuchten Datei keine passenden gespeicherten Pakete gefunden hat. Prüfe Filterausdruck, Zeitraum und Erfassungspunkt, bevor du eine weitergehende Aussage triffst. Entferne zunächst den Filter, um zu sehen, ob der Mitschnitt Verkehr enthält.

:::single-choice{#wireshark-display-filters-empty-capture-view} Du wendest dns auf einen gespeicherten Mitschnitt an und siehst keine Zeilen. Was kannst du berichten?

::option[Niemand im gesamten Netz hat DNS verwendet.]{#wireshark-display-filters-empty-capture-view-a explanation="Eine Datei deckt nur einen bestimmten Erfassungspunkt und Zeitraum ab."}
::option[Wireshark hat die DNS-Pakete gelöscht.]{#wireshark-display-filters-empty-capture-view-b explanation="Der Anzeigefilter löscht keine gespeicherten Pakete."}
::option[Dieser Filter hat in diesem Mitschnitt keine DNS-Pakete angezeigt.]{#wireshark-display-filters-empty-capture-view-c .correct explanation="Diese Aussage bleibt innerhalb dessen, was du geprüft hast."}
:::

Um einen weiteren Mitschnitt in einer Browserübung zu untersuchen, probiere die Übung zu Anzeigefiltern in [Wireshark für Einsteiger](https://labex.io/courses/quick-start-with-wireshark) aus.

## Zusammenfassung

Du kannst jetzt einen gespeicherten Paketmitschnitt filtern und erklären, wie weit das Ergebnis reicht.

1. Wähle ein Protokoll mit einem Anzeigefilter aus.
2. Filtere mit ip.addr nach einer Paketadresse.
3. Berücksichtige bei der Auswertung, was die Datei am Erfassungspunkt sichtbar macht.
