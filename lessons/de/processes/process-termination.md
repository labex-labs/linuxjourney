---
lang: "de"
title: "Prozessbeendigung"
description: "Erfahren Sie mehr über die Prozessbeendigung unter Linux, einschließlich verwaister und Zombie-Prozesse. Verstehen Sie die Systemaufrufe _exit und wait für ein effektives Prozessmanagement."
keywords: "Linux Prozessbeendigung, Zombie-Prozesse, verwaiste Prozesse, wait Systemaufruf, _exit, Linux Tutorial, Linux für Anfänger"
---

## Lesson Content

Nachdem wir nun wissen, was passiert, wenn ein Prozess erstellt wird, was geschieht, wenn wir ihn nicht mehr benötigen? Seien Sie gewarnt, manchmal kann Linux ein wenig düster werden...

Ein Prozess kann den `_exit`-Systemaufruf verwenden, um zu beenden. Dadurch werden die vom Prozess verwendeten Ressourcen zur Neuverteilung freigegeben. Wenn ein Prozess also bereit ist, zu beenden, teilt er dem Kernel mit, warum er beendet wird, und zwar mit einem sogenannten Beendigungsstatus. Am häufigsten bedeutet ein Status von 0, dass der Prozess erfolgreich war. Das reicht jedoch nicht aus, um einen Prozess vollständig zu beenden. Der Elternprozess muss die Beendigung des Kindprozesses durch den `wait`-Systemaufruf bestätigen, und dieser prüft den Beendigungsstatus des Kindprozesses. Ich weiß, es ist grausam, darüber nachzudenken, aber der `wait`-Aufruf ist eine Notwendigkeit; schließlich, welche Eltern würden nicht wissen wollen, wie ihr Kind gestorben ist?

Es gibt eine weitere Möglichkeit, einen Prozess zu beenden, und das beinhaltet die Verwendung von Signalen, die wir bald besprechen werden.

### Orphan Processes

Wenn ein Elternprozess vor einem Kindprozess stirbt, weiß der Kernel, dass er keinen `wait`-Aufruf erhalten wird, also macht er diese Prozesse stattdessen zu "Waisen" und stellt sie unter die Obhut von `init` (erinnern Sie sich, Mutter aller Prozesse). `init` wird schließlich den `wait`-Systemaufruf für diese Waisen ausführen, damit sie sterben können.

### Zombie Processes

Was passiert, wenn ein Kind beendet wird und der Elternprozess noch nicht `wait` aufgerufen hat? Wir möchten immer noch sehen können, wie ein Kindprozess beendet wurde, also obwohl der Kindprozess beendet ist, verwandelt der Kernel den Kindprozess in einen Zombie-Prozess. Die Ressourcen, die der Kindprozess verwendet hat, werden immer noch für andere Prozesse freigegeben; es gibt jedoch immer noch einen Eintrag in der Prozesstabelle für diesen Zombie. Zombie-Prozesse können auch nicht getötet werden, da sie technisch "tot" sind, sodass Sie keine Signale verwenden können, um sie zu töten. Schließlich, wenn der Elternprozess den `wait`-Systemaufruf aufruft, verschwindet der Zombie; dies wird als "reaping" bezeichnet. Wenn der Elternteil keinen `wait`-Aufruf durchführt, wird `init` den Zombie adoptieren und automatisch `wait` ausführen und den Zombie entfernen. Es kann schlecht sein, zu viele Zombie-Prozesse zu haben, da sie Platz in der Prozesstabelle beanspruchen; wenn sie sich füllt, verhindert dies, dass andere Prozesse ausgeführt werden.

## Exercise

Keine Übungen für diese Lektion.

## Quiz Question

Was ist der häufigste Beendigungsstatus für einen erfolgreich beendeten Prozess?

## Quiz Answer

0
