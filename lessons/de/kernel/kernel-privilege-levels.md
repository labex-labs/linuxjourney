---
index: 2
lang: "de"
title: "Privilegien-Ebenen"
meta_title: "Privilegien-Ebenen - Kernel"
meta_description: "Erfahren Sie mehr über Linux-Privilegien-Ebenen, Kernel-Modus und Benutzer-Modus. Verstehen Sie Schutzringe und Systemaufrufe für sicheren Hardware-Zugriff. Beginnen Sie Ihre Linux-Reise!"
meta_keywords: "Linux-Privilegien-Ebenen, Kernel-Modus, Benutzer-Modus, Schutzringe, Systemaufrufe, Linux-Sicherheit, Linux für Anfänger, Linux-Tutorial"
---

## Lesson Content

Die nächsten paar Lektionen werden ziemlich theoretisch. Wenn Sie also etwas Praktisches suchen, können Sie diese überspringen und später darauf zurückkommen.

Warum haben wir verschiedene Abstraktionsschichten für den Benutzerbereich und den Kernel? Warum kann man nicht beide Kräfte in einer Schicht vereinen? Nun, es gibt einen sehr guten Grund, warum diese beiden Schichten getrennt existieren. Sie arbeiten beide in verschiedenen Modi: Der Kernel arbeitet im Kernel-Modus, und der Benutzerbereich arbeitet im Benutzer-Modus.

Im Kernel-Modus hat der Kernel vollständigen Zugriff auf die Hardware; er steuert alles. Im Benutzer-Modus gibt es eine sehr kleine Menge an sicherem Speicher und CPU, auf die Sie zugreifen dürfen. Grundsätzlich wird alles, was Hardware betrifft – das Lesen von Daten von unseren Festplatten, das Schreiben von Daten auf unsere Festplatten, die Steuerung unseres Netzwerks usw. – im Kernel-Modus durchgeführt. Warum ist das notwendig? Stellen Sie sich vor, Ihr Computer wäre mit Spyware infiziert; Sie würden nicht wollen, dass diese direkten Zugriff auf die Hardware Ihres Systems hat. Sie könnte auf all Ihre Daten, Ihre Webcam usw. zugreifen, und das ist nicht gut.

Diese verschiedenen Modi werden als Privilegien-Ebenen (passend benannt nach den Privilegien, die man erhält) bezeichnet und oft als Schutzringe beschrieben. Um dieses Bild leichter zu malen, stellen wir uns vor, Sie erfahren, dass Britney Spears in Ihrer örtlichen Diskothek ist. Sie wird von ihren Groupies, dann von ihren persönlichen Bodyguards, dann vom Türsteher vor dem Club geschützt. Sie möchten ihr Autogramm bekommen (warum auch nicht?), aber Sie können nicht zu ihr gelangen, weil sie stark geschützt ist. Die Ringe funktionieren auf die gleiche Weise: Der innerste Ring entspricht der höchsten Privilegien-Ebene. In einer x86-Computerarchitektur gibt es zwei Haupt-Ebenen oder Modi. Ring #3 ist das Privileg, in dem Benutzeranwendungen ausgeführt werden; Ring #0 ist das Privileg, in dem der Kernel ausgeführt wird. Ring #0 kann jede Systemanweisung ausführen und genießt volles Vertrauen. Da wir nun wissen, wie diese Privilegien-Ebenen funktionieren, wie können wir dann überhaupt etwas auf unsere Hardware schreiben? Werden wir nicht immer in einem anderen Modus als der Kernel sein?

Die Antwort liegt in Systemaufrufen. Systemaufrufe ermöglichen es uns, eine privilegierte Anweisung im Kernel-Modus auszuführen und dann in den Benutzer-Modus zurückzukehren.

## Exercise

Übung macht den Meister! Das Verständnis der theoretischen Konzepte von Benutzerbereich, Kernelbereich und Privilegien-Ebenen ist entscheidend, aber praktische Erfahrung hilft, zu festigen, wie sich diese Konzepte in der praktischen Linux-Administration manifestieren. Hier sind einige praktische Übungen, um Ihr Verständnis zu vertiefen, wie Benutzeraktionen mit dem zugrunde liegenden System interagieren:

1. **[Linux-Benutzerkonten mit useradd, usermod und userdel verwalten](https://labex.io/de/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - Üben Sie das Erstellen, Ändern und Löschen von Benutzerkonten, was direkt mit der Verwaltung von Entitäten zusammenhängt, die im Benutzerbereich arbeiten und Kernel-Interaktion für privilegierte Aktionen erfordern.
2. **[Datei- und Verzeichnisberechtigungen in Linux verwalten](https://labex.io/de/labs/comptia-manage-file-and-directory-permissions-in-linux-590844)** - Lernen Sie, den Zugriff auf Dateien und Verzeichnisse zu steuern, ein zentrales Sicherheitskonzept, das darauf beruht, dass der Kernel Berechtigungen basierend auf Benutzerprivilegien durchsetzt.
3. **[Linux-Prozesse verwalten und überwachen](https://labex.io/de/labs/comptia-manage-and-monitor-linux-processes-590864)** - Erforschen Sie, wie Sie mit Prozessen interagieren und diese überwachen können. Dies sind Benutzerbereichsanwendungen, die Systemaufrufe an den Kernel zur Ressourcenverwaltung und Ausführung tätigen.

Diese Übungen werden Ihnen helfen, die Konzepte der Benutzerinteraktion mit dem Linux-System anzuwenden, wobei die Rolle des Kernels bei der Ressourcenverwaltung und Durchsetzung von Privilegien von größter Bedeutung ist, und Vertrauen in grundlegende Linux-Administrationsaufgaben aufzubauen.

## Quiz Question

Welche Ringnummer hat die höchsten Privilegien?

## Quiz Answer

0
