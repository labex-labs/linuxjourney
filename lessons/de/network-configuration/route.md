---
lang: "de"
title: "route"
meta_title: "route - Netzwerkkonfiguration"
meta_description: "Erfahren Sie, wie Sie Netzwerkrouten mit den Linux-Befehlen route und ip hinzufügen und löschen. Verstehen Sie die Verwaltung von Routing-Tabellen für Anfänger und fortgeschrittene Benutzer."
meta_keywords: "route Befehl, ip route, Route hinzufügen, Route löschen, Linux-Netzwerk, Routing-Tabelle, Linux-Tutorial, Anfängerleitfaden"
---

## Lesson Content

Wir haben bereits besprochen, wie man Routing-Tabellen mit dem Befehl `route` anzeigt. Wenn Sie Routen hinzufügen oder entfernen möchten, können Sie dies manuell tun.

### Eine neue Route hinzufügen

```bash
sudo route add -net 192.168.2.1/23 gw 10.11.12.3
```

### Eine Route löschen

```bash
sudo route del -net 192.168.2.1/23
```

Sie können diese Änderungen auch mit dem Befehl **ip** durchführen:

### Eine Route hinzufügen

```bash
ip route add 192.168.2.1/23 via 10.11.12.3
```

### Eine Route löschen

```bash
$ ip route delete 192.168.2.1/23 via 10.11.12.3
or
$ ip route delete 192.168.2.1/23
```

## Exercise

Für diese Lektion gibt es keine Übungen, aber Sie können weitere Informationen zu den hier besprochenen Befehlen in den Manpages nachlesen.

```bash
man route
```

```bash
man ip-route
```

## Quiz Question

Was ist das Befehls-Flag, um eine Route zu löschen?

## Quiz Answer

del
