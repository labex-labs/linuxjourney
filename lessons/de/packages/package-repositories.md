---
index: 2
lang: "de"
title: "Paket-Repositories"
meta_title: "Paket-Repositories - Pakete"
meta_description: "Erfahren Sie mehr über Linux-Paket-Repositories und wie sie Software verwalten. Entdecken Sie, wie Sie Paketquellen wie /etc/apt/sources.list finden und hinzufügen, um eine einfache Installation zu ermöglichen."
meta_keywords: "Linux-Paket-Repositories, apt sources list, /etc/apt/sources.list, Linux-Pakete, Linux für Anfänger, Linux-Tutorial, Paketverwaltung"
---

## Lesson Content

Wie gelangen Pakete, die ins Internet hochgeladen wurden, auf unsere Computer? Gehen Sie auf die Download-Seite jedes gewünschten Pakets und klicken Sie auf Herunterladen und Installieren? Obwohl das möglich ist, gibt es eine bessere Lösung: Paket-Repositories. Repositories sind zentrale Speicherorte für Pakete. Es gibt unzählige Repositories, die viele Pakete enthalten, und das Beste daran ist, dass sie alle im Internet zu finden sind – keine albernen Installationsdisketten. Ihr Rechner weiß nicht, wo er nach diesen Repositories suchen soll, es sei denn, Sie weisen ihn explizit an, wo er suchen soll.

Nehmen wir zum Beispiel an, ich möchte die Docker Software auf meinem Rechner haben. Docker verwaltet seine eigenen Repositories für seine Container-Pakete. In diesem Repository befinden sich mehrere Pakete, wie das docker-ce-Paket, das docker-ce-cli-Paket, das containerd.io-Paket usw. Docker hostet dieses Repository unter einem Quell-Link namens: `https://download.docker.com/linux/ubuntu`

Anstatt nun auf deren Website zu gehen, um das Paket direkt herunterzuladen, können Sie Ihrem Rechner mitteilen, dass er die Docker Software über den Quell-Link finden soll.

Ihre Distribution wird bereits mit vorab genehmigten Quellen geliefert, aus denen Pakete bezogen werden können, und so werden alle Basispakete, die Sie auf Ihrem System sehen, installiert. Auf einem Debian-System ist diese Quelldatei die Datei `/etc/apt/sources.list`. Ihr Rechner weiß, dass er dort nachsehen und nach allen von Ihnen hinzugefügten Quell-Repositories suchen muss.

## Exercise

No exercises for this lesson.

## Quiz Question

Wo befindet sich die Quelldatei in einem Debian-System?

## Quiz Answer

/etc/apt/sources.list
