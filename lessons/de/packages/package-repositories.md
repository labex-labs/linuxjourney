---
index: 2
lang: "de"
title: "Paket-Repositories"
meta_title: "Paket-Repositories - Pakete"
meta_description: "Erfahren Sie mehr über Linux-Paket-Repositories und wie sie Software verwalten. Entdecken Sie, wie Sie Paketquellen wie /etc/apt/sources.list für eine einfache Installation finden und hinzufügen."
meta_keywords: "Linux-Paket-Repositories, apt sources list, /etc/apt/sources.list, Linux-Pakete, Linux für Anfänger, Linux-Tutorial, Paketverwaltung"
---

## Lesson Content

Wie gelangen Pakete, die ins Internet hochgeladen wurden, auf unsere Computer? Gehen Sie auf die Download-Seite jedes gewünschten Pakets und klicken Sie auf Herunterladen und Installieren? Obwohl das möglich ist, gibt es eine bessere Lösung: Paket-Repositories. Repositories sind zentrale Speicherorte für Pakete. Es gibt unzählige Repositories, die viele Pakete enthalten, und das Beste daran ist, dass sie alle im Internet zu finden sind – keine lästigen Installationsdisketten. Ihr Computer weiß nicht, wo er nach diesen Repositories suchen soll, es sei denn, Sie teilen ihm explizit mit, wo er suchen soll.

Nehmen wir zum Beispiel an, ich möchte Docker Software auf meinem Computer haben. Docker verwaltet seine eigenen Repositories für seine Container-Pakete. In diesem Repository befinden sich mehrere Pakete, wie das docker-ce-Paket, das docker-ce-cli-Paket, das containerd.io-Paket usw. Docker hostet dieses Repository unter einem Quelllink namens: `https://download.docker.com/linux/ubuntu`

Anstatt nun auf deren Website zu gehen, um das Paket direkt herunterzuladen, können Sie Ihrem Computer mitteilen, Docker-Software über den Quelllink zu finden.

Ihre Distribution wird bereits mit vorab genehmigten Quellen geliefert, um Pakete zu beziehen, und so werden alle Basispakete installiert, die Sie auf Ihrem System sehen. Auf einem Debian-System ist diese Quelldatei die Datei `/etc/apt/sources.list`. Ihr Computer weiß, dass er dort nachsehen und nach allen von Ihnen hinzugefügten Quell-Repositories suchen muss.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis von Linux-Paketverwaltung und Repositories zu vertiefen:

1. **[Software-Installation unter Linux](https://labex.io/de/labs/linux-software-installation-on-linux-18005)** – Üben Sie verschiedene Methoden zur Installation und Verwaltung von Software auf Ubuntu-Systemen, einschließlich der Verwendung von apt und der Handhabung von .deb-Dateien, die direkt mit dem `sources.list`-Konzept zusammenhängen.
2. **[Pakete installieren und entfernen](https://labex.io/de/labs/linux-installing-and-removing-packages-385380)** – Lernen Sie, das System zu aktualisieren, Pakete auf einem Debian-basierten System zu installieren und zu entfernen, und festigen Sie so Ihr Verständnis, wie Paketmanager mit Repositories interagieren.
3. **[Pakete mit YUM in Linux abfragen und aktualisieren](https://labex.io/de/labs/rhel-query-and-update-packages-with-yum-in-linux-590869)** – Erfahren Sie, wie Sie Softwarepakete auf RHEL-basierten Linux-Systemen mit YUM verwalten, und erhalten Sie so eine breitere Perspektive auf die Paketverwaltung über verschiedene Distributionen hinweg.

Diese Übungen helfen Ihnen, die Konzepte von Paket-Repositories und Softwareverwaltung in realen Szenarien anzuwenden und Vertrauen in Systemadministrationsaufgaben aufzubauen.

## Quiz Question

Wo befindet sich die Quelldatei in einem Debian-System?

## Quiz Answer

/etc/apt/sources.list
