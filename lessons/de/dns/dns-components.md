---
title: "DNS-Komponenten"
description: "Erfahren Sie mehr über DNS-Komponenten: Name Server, Zone Files und Resource Records. Verstehen Sie, wie DNS für Anfänger funktioniert. Beginnen Sie Ihre Linux-Netzwerkreise!"
keywords: "DNS-Komponenten, Name Server, Zone File, Resource Records, DNS-Tutorial, Linux-Netzwerk, Anfängerleitfaden"
---

## Lesson Content

Die DNS-Datenbank des Internets basiert darauf, dass Websites und Organisationen einen Teil dieser Datenbank bereitstellen. Dazu benötigen sie:

### Name Server

Wir richten DNS über "Name Server" ein. Name Server laden unsere DNS-Einstellungen und -Konfigurationen und beantworten alle Anfragen von Clients oder anderen Servern, die Dinge wissen möchten wie "Wer ist google.com?". Wenn der Name Server die Antwort auf diese Abfrage nicht kennt, leitet er die Anfrage an andere Name Server weiter. Name Server können "autoritativ" sein, was bedeutet, dass sie die tatsächlichen DNS-Einträge enthalten, nach denen Sie suchen, oder "rekursiv", was bedeutet, dass sie andere Server fragen würden, und diese Server würden andere Server fragen, bis sie einen autoritativen Server finden, der die DNS-Einträge enthält. Rekursive Server können die gewünschten Informationen auch zwischengespeichert haben, anstatt einen autoritativen Server zu erreichen.

### Zone File

Innerhalb eines Name Servers befinden sich sogenannte Zone Files. Zone Files sind die Art und Weise, wie der Name Server Informationen über die Domain speichert oder wie er zur Domain gelangt, wenn er sie nicht kennt.

### Resource Records

Eine Zone File besteht aus Einträgen von Resource Records. Jede Zeile ist ein Record und enthält Informationen über Hosts, Name Server, andere Ressourcen usw. Die Felder bestehen aus den folgenden:

- Record name
- TTL - Die Zeit, nach der wir den Record verwerfen und einen neuen erhalten. Im DNS wird TTL durch Zeit angegeben, so dass Records eine TTL von einer Stunde haben könnten. Der Grund, warum wir dies tun, ist, dass sich das Internet ständig ändert; in einer Minute kann ein Host einer X IP-Adresse zugeordnet sein, dann in der nächsten einer Y IP-Adresse.
- Class - Namespace der Record-Informationen. Am häufigsten wird IN für Internet verwendet.
- Type - Art der im Record-Daten gespeicherten Informationen. Wir werden nicht auf Record Types eingehen, aber Sie haben wahrscheinlich gängige wie A für address, MX für mail exchanger usw. gesehen.
- Data - Dieses Feld kann eine IP-Adresse enthalten, wenn es sich um einen A record handelt, oder etwas anderes, je nach Record Type.

```plaintext
patty    IN  A      192.168.0.4
```

## Exercise

No exercises for this lesson.

## Quiz Question

Welcher Resource Record Type wird für Mail Exchanger verwendet?

## Quiz Answer

MX
