---
lang: "de"
title: "Dateisystemreparatur"
meta_title: "Dateisystemreparatur - Das Dateisystem"
meta_description: "Lernen Sie, fsck für die Reparatur von Linux-Dateisystemen und die Datenwiederherstellung zu verwenden. Verstehen Sie, wie Sie Festplattenfehler mit diesem wichtigen Befehl überprüfen und beheben können. Beginnen Sie Ihre Linux-Reise!"
meta_keywords: "fsck, Dateisystemreparatur, Linux-Befehle, Festplattenfehler, Datenwiederherstellung, Linux-Tutorial, Anfängerleitfaden"
---

## Lesson Content

Manchmal ist unser Dateisystem nicht immer im besten Zustand. Wenn wir einen plötzlichen Shutdown haben, können unsere Daten beschädigt werden. Es liegt am System, zu versuchen, uns wieder in einen funktionierenden Zustand zu versetzen (obwohl wir es sicherlich selbst versuchen können).

Der Befehl **fsck** (filesystem check) wird verwendet, um die Konsistenz eines Dateisystems zu überprüfen und kann sogar versuchen, es für uns zu reparieren. Normalerweise, wenn Sie eine Festplatte booten, wird fsck ausgeführt, bevor Ihre Festplatte gemountet wird, um sicherzustellen, dass alles in Ordnung ist. Manchmal ist Ihre Festplatte jedoch so schlecht, dass Sie dies manuell tun müssen. Stellen Sie jedoch sicher, dass Sie dies tun, während Sie sich auf einer Rettungsdisk befinden oder an einem Ort, an dem Sie auf Ihr Dateisystem zugreifen können, ohne dass es gemountet ist.

```bash
sudo fsck /dev/sda
```

## Exercise

Schauen Sie sich die Manpage für fsck an, um zu sehen, was es sonst noch tun kann.

## Quiz Question

Welcher Befehl wird verwendet, um die Integrität eines Dateisystems zu überprüfen?

## Quiz Answer

fsck
