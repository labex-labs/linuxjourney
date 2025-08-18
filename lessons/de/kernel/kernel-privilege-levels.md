---
index: 2
lang: "de"
title: "Privilegien-Ebenen"
meta_title: "Privilegien-Ebenen - Kernel"
meta_description: "Erfahren Sie mehr über Linux-Privilegien-Ebenen, Kernel-Modus und Benutzer-Modus. Verstehen Sie Schutzringe und Systemaufrufe für sicheren Hardware-Zugriff. Beginnen Sie Ihre Linux-Reise!"
meta_keywords: "Linux-Privilegien-Ebenen, Kernel-Modus, Benutzer-Modus, Schutzringe, Systemaufrufe, Linux-Sicherheit, Linux für Anfänger, Linux-Tutorial"
---

## Lesson Content

Die nächsten paar Lektionen werden ziemlich theoretisch. Wenn Sie also nach praktischen Inhalten suchen, können Sie diese überspringen und später darauf zurückkommen.

Warum haben wir verschiedene Abstraktionsebenen für den Benutzerbereich und den Kernel? Warum kann man nicht beide Kräfte in einer Ebene vereinen? Nun, es gibt einen sehr guten Grund, warum diese beiden Ebenen getrennt existieren. Sie arbeiten beide in verschiedenen Modi: Der Kernel arbeitet im Kernel-Modus, und der Benutzerbereich arbeitet im Benutzer-Modus.

Im Kernel-Modus hat der Kernel vollständigen Zugriff auf die Hardware; er steuert alles. Im Benutzerbereichs-Modus gibt es eine sehr geringe Menge an sicherem Speicher und CPU, auf die Sie zugreifen dürfen. Grundsätzlich wird alles, was Hardware betrifft – Daten von unseren Festplatten lesen, Daten auf unsere Festplatten schreiben, unser Netzwerk steuern usw. – im Kernel-Modus ausgeführt. Warum ist das notwendig? Stellen Sie sich vor, Ihr Computer wäre mit Spyware infiziert; Sie würden nicht wollen, dass diese direkten Zugriff auf die Hardware Ihres Systems hat. Sie könnte auf all Ihre Daten, Ihre Webcam usw. zugreifen, und das ist nicht gut.

Diese verschiedenen Modi werden Privilegien-Ebenen genannt (passend benannt nach den Privilegien, die man erhält) und werden oft als Schutzringe beschrieben. Um dieses Bild einfacher zu gestalten, stellen wir uns vor, Sie erfahren, dass Britney Spears in Ihrer Stadt in Ihrem lokalen Club ist. Sie wird von ihren Groupies, dann von ihren persönlichen Bodyguards, dann vom Türsteher vor dem Club geschützt. Sie möchten ihr Autogramm bekommen (warum auch nicht?), aber Sie können nicht zu ihr gelangen, weil sie stark geschützt ist. Die Ringe funktionieren auf die gleiche Weise: Der innerste Ring entspricht der höchsten Privilegien-Ebene. Es gibt zwei Haupt-Ebenen oder Modi in einer x86-Computerarchitektur. Ring #3 ist das Privileg, in dem Benutzeranwendungen ausgeführt werden; Ring #0 ist das Privileg, in dem der Kernel ausgeführt wird. Ring #0 kann jede Systemanweisung ausführen und genießt volles Vertrauen. Da wir nun wissen, wie diese Privilegien-Ebenen funktionieren, wie können wir dann überhaupt etwas auf unsere Hardware schreiben? Werden wir nicht immer in einem anderen Modus als der Kernel sein?

Die Antwort liegt in System Calls. System Calls ermöglichen es uns, eine privilegierte Anweisung im Kernel-Modus auszuführen und dann in den Benutzer-Modus zurückzukehren.

## Exercise

No exercises for this lesson.

## Quiz Question

Welche Ringnummer hat die höchsten Privilegien?

## Quiz Answer

0
