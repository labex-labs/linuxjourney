---
index: 3
lang: "de"
title: "DNS-Prozess"
meta_title: "DNS-Prozess - DNS"
meta_description: "Erfahren Sie Schritt für Schritt, wie DNS funktioniert, von Root-Servern bis hin zu autoritativem DNS. Verstehen Sie den DNS-Lookup-Prozess für Anfänger und fortgeschrittene Benutzer."
meta_keywords: "DNS-Prozess, DNS-Lookup, wie DNS funktioniert, DNS-Tutorial, DNS für Anfänger, Linux DNS, TLD, Root-Server"
---

## Lesson Content

Betrachten wir ein Beispiel, wie Ihr Host eine Domain (catzontheinterwebz.com) mit DNS findet. Im Wesentlichen arbeiten wir uns nach unten vor, bis wir den DNS-Server erreichen, der diese Domain kennt.

### Local DNS Server

Zuerst fragt unser Host: "Wo ist catzontheinterwebz.com?" Unser lokaler DNS-Server weiß es nicht, also beginnt er ganz oben im Trichter und fragt die Root-Server. Beachten Sie, dass unser Host diese Anfragen nicht direkt stellt, um catzontheinterwebz.com zu finden; die meisten Benutzer sprechen mit einem rekursiven DNS-Server, der von ihren ISPs bereitgestellt wird, und dieser Server ist dann damit beauftragt, den Standort von catzontheinterwebz.com zu finden.

### Root Servers

Es gibt 13 Root-Server für das Internet. Sie sind gespiegelt und weltweit verteilt, um DNS-Anfragen für das Internet zu bearbeiten, sodass tatsächlich Hunderte von Servern arbeiten. Sie werden von verschiedenen Organisationen kontrolliert und enthalten Informationen über Top-Level-Domains. Top-Level-Domains sind das, was Sie als .org-, .com-, .net- usw. Adressen kennen. Der Root-Server weiß also nicht, wo catzontheinterwebz.com ist, aber er sagt uns, wir sollen den .com Top-Level Domain DNS-Server unter einer IP-Adresse fragen, die er uns gibt.

### Top-Level Domain

Jetzt senden wir eine weitere Anfrage an den Nameserver, der über ".com"-Adressen Bescheid weiß, und fragen, ob er weiß, wo catzontheinterwebz.com ist. Die TLD hat catzontheinterwebz.com nicht in ihren Zonendateien, aber sie sieht einen Eintrag für den Nameserver für catzontheinterwebz.com. Also gibt sie uns die IP-Adresse dieses Nameservers und sagt uns, wir sollen dort nachsehen.

### Authoritative DNS Server

Jetzt senden wir eine letzte Anfrage an den DNS-Server, der tatsächlich den gewünschten Eintrag hat. Der Nameserver sieht, dass er eine Zonendatei für catzontheinterwebz.com hat und dass es einen Resource Record für 'www' für diesen Host gibt. Er gibt uns dann die IP-Adresse dieses Hosts, und wir können endlich einige Katzen im Internet sehen.

## Exercise

Keine Übungen für diese Lektion.

## Quiz Question

Was ist die Abkürzung für die Nameserver, bei denen .com-, .net-, .org- usw. Adressen gefunden werden?

## Quiz Answer

TLD
