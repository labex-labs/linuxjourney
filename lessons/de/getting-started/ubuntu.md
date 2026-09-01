---
lesson_id: "ubuntu"
course_id: "getting-started"
lang: "de"
order_index: 5
title: "Ubuntu"
description: "Erfahre, wie Ubuntu seine Debian-Grundlage mit zugänglichen Desktop-, Server- und Veröffentlichungsoptionen verbindet."
meta_title: "Ubuntu Linux"
meta_description: "Erfahre, was Ubuntu Linux ist, warum Ubuntu beliebt ist, wie sein Veröffentlichungsmodell und seine Paketverwaltung funktionieren und warum es auf Desktops, Laptops und Servern weitverbreitet ist."
meta_keywords: "Ubuntu Linux, Ubuntu-Distribution, was ist Ubuntu, Ubuntu-Veröffentlichungen, Ubuntu-Paketverwaltung, Ubuntu Debian-basiert, Linux-Distribution"
---

## Was ist Ubuntu?

Ubuntu ist eine der am weitesten verbreiteten Linux-Distributionen. Es wird von Canonical entwickelt, baut auf Debian auf und ist für seine zugängliche Gestaltung, seine große Nutzergemeinschaft sowie seine breite Hardware- und Softwareunterstützung bekannt.

Ubuntu ist zu einem verbreiteten Ausgangspunkt für Menschen geworden, die Linux kennenlernen möchten, ohne mit einer stärker manuellen oder fortgeschrittenen Einrichtung zu beginnen. Es wird auf privaten Computern, Entwicklungssystemen, Cloud-Plattformen und Servern eingesetzt und erreicht damit eine Verbreitung, mit der nur wenige andere Distributionen mithalten können.

:::single-choice{#identify-ubuntu-base} Welche Distribution bildet die Grundlage von Ubuntu?

::option[Die Debian-Distribution]{#debian-base .correct explanation="Ubuntu baut auf Debian auf und übernimmt einen großen Teil von Debians Ansatz zur Paketierung. Ubuntu ergänzt diesen um eigene Veröffentlichungen, Voreinstellungen und ein eigenes Supportmodell."}
::option[Die Fedora-Distribution]{#ubuntu-fedora-base explanation="Fedora gehört zum Red-Hat-Ökosystem und bildet nicht die Grundlage von Ubuntu. Ubuntu gehört zur Debian-Familie."}
::option[Die Arch-Distribution]{#ubuntu-arch-base explanation="Arch Linux ist eine eigenständige Distribution mit einem eigenen Paketsystem und Veröffentlichungsansatz. Ubuntu basiert auf Debian."}
:::

## Warum Ubuntu beliebt ist

Ubuntu ist beliebt, weil es Linux für den täglichen Einsatz praktisch machen möchte. Es bietet ein ausgefeiltes Installationsprogramm, eine gute Dokumentation, vorhersehbare Veröffentlichungen und ein großes Ökosystem aus Anleitungen und Unterstützung durch Drittanbieter. Für viele Nutzer macht diese Kombination Ubuntu zu einer der Linux-Distributionen, mit denen sich am einfachsten arbeiten lässt.

Ein weiterer Grund für Ubuntus hohe Sichtbarkeit ist sein Einsatz in vielen verschiedenen Umgebungen. Du findest es auf Laptops und Desktops, in virtuellen Maschinen, auf Servern und auf Cloud-Plattformen. Diese breite Verbreitung stärkt seinen Ruf als vielseitig einsetzbare Linux-Distribution.

:::single-choice{#recognize-beginner-support} Welche Eigenschaft von Ubuntu hilft einem Einsteiger am unmittelbarsten bei der Lösung von Problemen?

::option[Die vorgeschriebene manuelle Kompilierung jedes installierten Programms]{#manual-compilation explanation="Ubuntu stellt Software gewöhnlich als Pakete bereit, statt die manuelle Kompilierung jedes Programms zu verlangen. Zusätzlicher Aufwand beim Erstellen würde die Fehlersuche nicht vereinfachen."}
::option[Eine umfangreiche Dokumentation und eine große Nutzergemeinschaft]{#documentation-community .correct explanation="Dokumentation und Diskussionen in der Gemeinschaft bieten Einsteigern viele Anlaufstellen für Erklärungen und Hilfe bei der Fehlersuche. Das senkt die Einstiegshürde."}
::option[Begrenzte Anleitungen, die nur erfahrenen Administratoren zur Verfügung stehen]{#limited-guidance explanation="Ubuntus Bekanntheit beruht zum Teil auf den weitverbreiteten Hilfsangeboten für viele Erfahrungsstufen. Unterstützung auf Experten zu beschränken, würde der Zugänglichkeit für Einsteiger entgegenwirken."}
:::

## Ubuntu und Debian

Ubuntu ist eine Debian-basierte Distribution. Das bedeutet, dass es einen großen Teil seines Paketverwaltungsmodells und seines Ansatzes zur Softwarepaketierung von Debian übernimmt. Wenn du lernst, wie `apt` unter Ubuntu funktioniert, hilft dir dieses Wissen auch beim Verständnis anderer Debian-basierter Systeme.

Gleichzeitig ist Ubuntu nicht einfach nur „Debian mit einem Desktop“. Es besitzt einen eigenen Veröffentlichungsplan, eigene Voreinstellungen, ein eigenes Supportmodell und ein eigenes Ökosystem. Wenn du es mit anderen Optionen vergleichen möchtest, sieh dir [Eine Linux-Distribution auswählen](https://labex.io/lesson/choosing-a-linux-distribution) an oder erfahre mehr über [Debian](https://labex.io/lesson/debian).

## Ubuntu-Veröffentlichungen

Ubuntu verwendet zwei Hauptarten von Veröffentlichungen. Alle sechs Monate erscheint eine neue Version, und alle zwei Jahre wird eine davon zu einer Long-Term-Support- oder LTS-Version. LTS-Veröffentlichungen werden häufig für Desktops, Arbeitsstationen und Server gewählt, die eine beständigere Grundlage benötigen.

Dieses Veröffentlichungsmodell erklärt einen Teil von Ubuntus Attraktivität. Nutzer, die eine zuverlässige Grundlage möchten, wählen häufig LTS, während Nutzer mit Interesse an neueren Funktionen die in kürzeren Abständen erscheinenden Zwischenversionen verwenden können.

:::single-choice{#choose-ubuntu-lts} Welche Art von Ubuntu-Veröffentlichung eignet sich am besten für ein System, das eine langlebigere, vorhersehbare Grundlage benötigt?

::option[Eine Zwischenversion]{#interim-release explanation="Zwischenversionen erscheinen häufiger und stellen neuere Funktionen früher bereit. Ihr kürzerer Supportzeitraum entspricht nicht der genannten Priorität."}
::option[Eine LTS-Veröffentlichung]{#lts-release .correct explanation="LTS-Veröffentlichungen sind für längeren Support vorgesehen und werden häufig für Systeme ausgewählt, bei denen eine zuverlässige Grundlage im Vordergrund steht."}
::option[Eine Paketaktualisierung]{#package-update explanation="Eine Paketaktualisierung ändert Software innerhalb einer installierten Veröffentlichung. Sie gehört nicht zu den beiden Arten von Betriebssystemveröffentlichungen bei Ubuntu."}
:::

## Paketverwaltung

Als Debian-basiertes System verwendet Ubuntu das Paketformat `.deb` und die Paketverwaltung `apt`, um Software zu installieren, zu aktualisieren und zu entfernen. Dadurch erhalten Nutzer Zugriff auf ein sehr großes Software-Ökosystem und einen vertrauten Arbeitsablauf auf der Befehlszeile.

Die Paketverwaltung ist eine der praktischen Stärken von Ubuntu, weil sie ausgereifte Debian-Werkzeuge mit einer großen und ausführlich dokumentierten Softwareumgebung verbindet.

:::single-choice{#identify-ubuntu-package-tool} Welcher Eintrag bezeichnet das Paketverwaltungswerkzeug, mit dem Software unter Ubuntu installiert wird?

::option[`.deb`]{#deb-format explanation="`.deb` bezeichnet das Paketformat Debian-basierter Systeme. Es ist nicht das Werkzeug zur Paketverwaltung auf der Befehlszeile."}
::option[`LTS`]{#lts-label explanation="LTS kennzeichnet eine Long-Term-Support-Veröffentlichung. Es installiert oder verwaltet keine Softwarepakete."}
::option[`apt`]{#ubuntu-apt-tool .correct explanation="Ubuntu verwendet `apt`, um Pakete zu installieren, zu aktualisieren und zu entfernen. Das Werkzeug arbeitet mit Software, die im `.deb`-Format von Debian paketiert ist."}
:::

## Einsatz auf Desktop und Server

Ubuntu wird sowohl auf Desktop- als auch auf Serversystemen eingesetzt. Auf dem Desktop ist es für eine ausgefeilte, GNOME-basierte Oberfläche und vergleichsweise zugängliche Voreinstellungen bekannt. Auf Servern wird es häufig in der Entwicklung, für Web-Infrastruktur und in Cloud-Umgebungen eingesetzt.

Diese Bandbreite macht Ubuntu für Nutzer attraktiv, die eine einzige Linux-Distribution möchten, die vom Lernen auf einem Laptop bis zum Ausführen produktiver Arbeitslasten mitwachsen kann.

## Warum Einsteiger Ubuntu wählen

Ubuntu wird Einsteigern häufig empfohlen, weil es sich einfacher installieren und bei Problemen untersuchen lässt als viele andere Linux-Distributionen. Dank der großen Nutzerbasis stehen zahlreiche Anleitungen, Forenbeiträge und Leitfäden zur Verfügung, wenn etwas nicht funktioniert.

Für Nutzer, die eine einsteigerfreundliche Linux-Distribution suchen, ohne auf langfristige Flexibilität zu verzichten, bleibt Ubuntu ein verbreiteter Ausgangspunkt.

## Weiterführende Literatur

- [Ubuntu Desktop](https://ubuntu.com/desktop)
- [Ubuntu Server](https://ubuntu.com/server)
- [Ubuntu-Veröffentlichungszyklus](https://ubuntu.com/releaseendoflife)
- [Dokumentation zu Ubuntu-Veröffentlichungen](https://documentation.ubuntu.com/project/release-team/ubuntu-releases/)

Um nach dieser Einführung in Ubuntu weiterzulernen, empfehlen wir diese LabEx-Kurse:

1. **[Schnellstart mit Linux](https://labex.io/courses/quick-start-with-linux)** - Schaffe eine praktische Grundlage in Linux-Grundlagen und im Umgang mit der Befehlszeile.
2. **[Linux für Einsteiger](https://labex.io/courses/linux-for-noobs)** - Folge einem einsteigerfreundlichen Lernpfad, um die Linux-Grundlagen Schritt für Schritt zu verstehen.
3. **[Werde Junior-Systemadministrator](https://labex.io/courses/become-a-junior-system-administrator)** - Vertiefe deine praktischen Fähigkeiten in der Linux-Administration, sobald du mit den Grundlagen vertraut bist.

## Zusammenfassung

Du kannst nun erklären, wie Ubuntu auf Debian aufbaut und zugleich eigene Veröffentlichungen und eine eigene Nutzererfahrung bietet.

1. Bestimme Debian als Grundlage von Ubuntu.
2. Erkenne Unterstützungsangebote, die Einsteigern helfen.
3. Vergleiche LTS- und Zwischenveröffentlichungen von Ubuntu.
4. Verwende `apt` als Ubuntus Paketverwaltungswerkzeug.
