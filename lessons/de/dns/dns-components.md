---
index: 2
lang: "de"
title: "DNS-Komponenten"
meta_title: "DNS-Komponenten - DNS"
meta_description: "Erfahren Sie mehr über DNS-Komponenten: Name Server, Zone-Dateien und Resource Records. Verstehen Sie, wie DNS für Anfänger funktioniert. Beginnen Sie Ihre Linux-Netzwerkreise!"
meta_keywords: "DNS-Komponenten, Name Server, Zone-Datei, Resource Records, DNS-Tutorial, Linux-Netzwerk, Anfängerleitfaden"
---

## Lesson Content

Die DNS-Datenbank des Internets basiert darauf, dass Websites und Organisationen einen Teil dieser Datenbank bereitstellen. Dazu benötigen sie:

### Name Server

Wir richten DNS über "Name Server" ein. Name Server laden unsere DNS-Einstellungen und -Konfigurationen und beantworten alle Anfragen von Clients oder anderen Servern, die wissen möchten, wie z.B. "Wer ist google.com?". Wenn der Name Server die Antwort auf diese Abfrage nicht kennt, leitet er die Anfrage an andere Name Server weiter. Name Server können "autoritativ" sein, was bedeutet, dass sie die tatsächlichen DNS-Einträge enthalten, nach denen Sie suchen, oder "rekursiv", was bedeutet, dass sie andere Server fragen würden, und diese Server würden andere Server fragen, bis sie einen autoritativen Server gefunden haben, der die DNS-Einträge enthält. Rekursive Server können die gewünschten Informationen auch zwischengespeichert haben, anstatt einen autoritativen Server zu erreichen.

### Zone-Datei

Innerhalb eines Name Servers befindet sich etwas, das als Zone-Dateien bezeichnet wird. Zone-Dateien sind die Art und Weise, wie der Name Server Informationen über die Domäne speichert oder wie er zur Domäne gelangt, wenn er sie nicht kennt.

### Resource Records

Eine Zone-Datei besteht aus Einträgen von Resource Records. Jede Zeile ist ein Eintrag und enthält Informationen über Hosts, Name Server, andere Ressourcen usw. Die Felder bestehen aus den folgenden:

- Record name
- TTL - Die Zeit, nach der wir den Eintrag verwerfen und einen neuen erhalten. Im DNS wird TTL durch Zeit angegeben, so dass Einträge eine TTL von einer Stunde haben könnten. Der Grund, warum wir dies tun, ist, dass sich das Internet ständig ändert; in einer Minute kann ein Host einer X-IP-Adresse zugeordnet sein, dann in der nächsten einer Y-IP-Adresse.
- Class - Namespace der Eintraginformationen. Am häufigsten wird IN für Internet verwendet.
- Type - Art der im Eintrag gespeicherten Informationen. Wir werden nicht auf Eintragstypen eingehen, aber Sie haben wahrscheinlich gängige wie A für Adresse, MX für Mail Exchanger usw. gesehen.
- Data - Dieses Feld kann eine IP-Adresse enthalten, wenn es sich um einen A-Eintrag handelt, oder etwas anderes, je nach Eintragstyp.

```plaintext
patty    IN  A      192.168.0.4
```

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis von DNS und Hostnamenauflösung zu vertiefen:

1. **[Einen lokalen autoritativen DNS-Server unter Linux einrichten](https://labex.io/de/labs/linux-set-up-a-local-authoritative-dns-server-on-linux-592803)** - Üben Sie die Installation und Konfiguration eines lokalen DNS-Servers (`bind9`), das Definieren von Zonen und das Validieren Ihrer Einrichtung.
2. **[DNS-Einträge unter Linux mit dig und nslookup abfragen](https://labex.io/de/labs/linux-query-dns-records-in-linux-with-dig-and-nslookup-592796)** - Lernen Sie, wichtige Befehlszeilentools (`dig`, `nslookup`) zu verwenden, um verschiedene DNS-Eintragstypen abzufragen und DNS-Probleme zu beheben.
3. **[Lokale Hostnamenauflösung unter Linux verwalten](https://labex.io/de/labs/linux-manage-local-hostname-resolution-in-linux-592792)** - Verstehen Sie, wie Sie die lokale Hostnamenauflösung durch Bearbeiten der Datei `/etc/hosts` verwalten, eine wichtige Fähigkeit für Entwicklung und Tests.

Diese Übungen helfen Ihnen, die Konzepte von DNS und Hostnamenauflösung in realen Szenarien anzuwenden und Vertrauen in Netzwerkdienste aufzubauen.

## Quiz Question

Welcher Ressourcendatensatztyp wird für Mail Exchanger verwendet?

## Quiz Answer

MX
