---
index: 4
lang: "de"
title: "/etc/hosts"
meta_title: "/etc/hosts - DNS"
meta_description: "Erkunden Sie den Zweck der Datei /etc/hosts unter Linux. Erfahren Sie, wie diese Datei Hostnamen IP-Adressen zuordnet, ihre Rolle bei der lokalen DNS-Auflösung und wie man sie auf Systemen wie Debian konfiguriert. Ein Leitfaden zur etc hosts Linux-Konfiguration."
meta_keywords: "/etc/hosts, etc hosts linux, debian hosts, etc host linux, etc hosts, Linux-Netzwerk, Hostname-Zuordnung, DNS-Auflösung"
---

## Lesson Content

Bevor Ihr Linux-System einen DNS-Server abfragt, um einen Hostnamen aufzulösen, sucht es zuerst auf dem lokalen Rechner nach einer Zuordnung. Diese anfängliche Überprüfung ist ein grundlegender Bestandteil des Namensauflösungsprozesses.

### Die Rolle von /etc/hosts

Die primäre Datei für diese lokale Suche ist `/etc/hosts`. Diese einfache Textdatei enthält statische Zuordnungen von Hostnamen zu IP-Adressen. Die Struktur der `etc hosts`-Datei ist unkompliziert: Jede Zeile enthält drei Felder: die IP-Adresse, den kanonischen Hostnamen und optionale Aliase für diesen Host.

Hier ist ein typisches Beispiel für eine `etc host linux`-Datei:

```plaintext
pete@icebox:~$ cat /etc/hosts
127.0.0.1       localhost
127.0.1.1       icebox
```

Sie werden fast immer die `localhost`-Adresse standardmäßig zugeordnet finden. Diese Datei ist ein Standardmerkmal der meisten Linux-Distributionen, einschließlich der `Debian hosts`.

### Bearbeiten der etc hosts linux Datei

You können die Datei `/etc/hosts` manuell bearbeiten, um eigene Zuordnungen zu erstellen. Versuchen wir ein lustiges Beispiel. Fügen Sie die folgende Zeile zu Ihrer Datei hinzu:

```plaintext
123.45.6.7  www.google.com
```

Nach dem Speichern der Datei versuchen Sie, in Ihrem Webbrowser zu `www.google.com` zu navigieren. Sie werden feststellen, dass dies nicht funktioniert. Das liegt daran, dass wir `www.google.com` einer falschen IP-Adresse zugeordnet haben. Da Ihr System zuerst die lokale Datei `/etc/hosts` überprüft, verwendet es unsere fehlerhafte Zuordnung und fährt nicht fort, einen DNS-Server abzufragen, um die korrekte Adresse zu finden. Um dies zu beheben, entfernen Sie einfach die hinzugefügte Zeile.

Während ältere Systeme `/etc/hosts.deny` und `/etc/hosts.allow` für die Zugriffskontrolle verwendeten, ist diese Methode weitgehend veraltet. Moderne Sicherheitspraktiken verlassen sich stattdessen auf die Konfiguration von Firewall-Regeln für robusten Schutz.

### Lokale DNS-Server-Konfiguration

Traditionell wurde die Datei `/etc/resolv.conf` verwendet, um die DNS-Namenserver für Lookups anzugeben. Aufgrund von Fortschritten in der Systemverwaltung wird diese Datei jedoch oft nicht mehr manuell verwaltet. Wie Sie im folgenden Beispiel sehen können, wird die Datei automatisch von einem anderen Dienst generiert. Für die Verwaltung von DNS-Namenserver-Zuordnungen sollten Sie die Dokumentation Ihrer spezifischen Distribution konsultieren, da Tools wie `systemd-resolved` oder `resolvconf` dies heute oft übernehmen.

```plaintext
# Dynamische resolv.conf(5) Datei für glibc resolver(3), generiert durch resolvconf(8)
#     BEARBEITEN SIE DIESE DATEI NICHT VON HAND -- IHRE ÄNDERUNGEN WERDEN ÜBERSCHRIEBEN
nameserver 127.0.1.1
search localdomain
```

## Exercise

Übung macht den Meister! Hier sind einige praktische Labs, um Ihr Verständnis der lokalen Hostnamensauflösung und DNS-Abfragen zu festigen:

1. **[Lokale Hostnamensauflösung in Linux verwalten](https://labex.io/de/labs/comptia-manage-local-hostname-resolution-in-linux-592792)** - Üben Sie die Bearbeitung der Datei `/etc/hosts` zur Verwaltung der lokalen Hostnamensauflösung, ein wichtiger Schritt vor DNS-Abfragen.
2. **[DNS-Einträge in Linux mit dig und nslookup abfragen](https://labex.io/de/labs/comptia-query-dns-records-in-linux-with-dig-and-nslookup-592796)** - Lernen Sie, DNS-Einträge mit essentiellen Linux-Tools wie `dig` und `nslookup` abzufragen, um zu verstehen, wie Ihr Rechner externe Namen auflöst.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Selbstvertrauen bei der Hostnamensauflösung und DNS zu gewinnen.

## Quiz Question

Welche Datei wird verwendet, um Hostnamen auf unseren Maschinen IP-Adressen zuzuordnen? (Bitte antworten Sie auf Englisch und achten Sie auf die Groß-/Kleinschreibung).

## Quiz Answer

/etc/hosts
