---
index: 5
lang: "de"
title: "Prozessbeendigung"
meta_title: "Prozessbeendigung - Prozesse"
meta_description: "Erfahren Sie mehr über die Beendigung von Linux-Prozessen, einschließlich verwaister und Zombie-Prozesse. Verstehen Sie _exit- und wait-Systemaufrufe für ein effektives Prozessmanagement."
meta_keywords: "Linux-Prozessbeendigung, Zombie-Prozesse, verwaiste Prozesse, wait-Systemaufruf, _exit, Linux-Tutorial, Linux für Anfänger"
---

## Lesson Content

Nachdem wir nun wissen, was passiert, wenn ein Prozess erstellt wird, was geschieht, wenn wir ihn nicht mehr benötigen? Seien Sie gewarnt, manchmal kann Linux ein wenig düster werden...

Ein Prozess kann den `_exit`-Systemaufruf verwenden, um sich zu beenden. Dadurch werden die vom Prozess verwendeten Ressourcen zur Neuverteilung freigegeben. Wenn ein Prozess bereit ist, sich zu beenden, teilt er dem Kernel mit, warum er sich beendet, und zwar mit einem sogenannten Beendigungsstatus. Am häufigsten bedeutet ein Status von 0, dass der Prozess erfolgreich war. Das reicht jedoch nicht aus, um einen Prozess vollständig zu beenden. Der Elternprozess muss die Beendigung des Kindprozesses durch den `wait`-Systemaufruf bestätigen, und dieser überprüft den Beendigungsstatus des Kindprozesses. Ich weiß, es ist grausam, darüber nachzudenken, aber der `wait`-Aufruf ist eine Notwendigkeit; schließlich, welche Eltern würden nicht wissen wollen, wie ihr Kind gestorben ist?

Es gibt eine weitere Möglichkeit, einen Prozess zu beenden, und das beinhaltet die Verwendung von Signalen, die wir bald besprechen werden.

### Verwaiste Prozesse

Wenn ein Elternprozess vor einem Kindprozess stirbt, weiß der Kernel, dass er keinen `wait`-Aufruf erhalten wird, also macht er diese Prozesse stattdessen zu "Waisen" und stellt sie unter die Obhut von `init` (erinnern Sie sich, die Mutter aller Prozesse). `init` wird schließlich den `wait`-Systemaufruf für diese Waisen ausführen, damit sie sterben können.

### Zombie-Prozesse

Was passiert, wenn ein Kind sich beendet und der Elternprozess noch nicht `wait` aufgerufen hat? Wir möchten immer noch sehen können, wie ein Kindprozess beendet wurde, also obwohl der Kindprozess beendet ist, verwandelt der Kernel den Kindprozess in einen Zombie-Prozess. Die vom Kindprozess verwendeten Ressourcen werden immer noch für andere Prozesse freigegeben; es gibt jedoch immer noch einen Eintrag in der Prozesstabelle für diesen Zombie. Zombie-Prozesse können auch nicht getötet werden, da sie technisch "tot" sind, sodass Sie keine Signale verwenden können, um sie zu töten. Schließlich, wenn der Elternprozess den `wait`-Systemaufruf aufruft, verschwindet der Zombie; dies wird als "reaping" bezeichnet. Wenn der Elternteil keinen `wait`-Aufruf durchführt, adoptiert `init` den Zombie und führt automatisch `wait` aus und entfernt den Zombie. Es kann schlecht sein, zu viele Zombie-Prozesse zu haben, da sie Platz in der Prozesstabelle beanspruchen; wenn sie sich füllt, verhindert dies, dass andere Prozesse ausgeführt werden.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis von Linux-Prozessen und deren Verwaltung zu vertiefen:

1. **[Linux-Prozesse verwalten und überwachen](https://labex.io/de/labs/comptia-manage-and-monitor-linux-processes-590864)** – Üben Sie die Interaktion mit Vordergrund- und Hintergrundprozessen, deren Überprüfung mit `ps`, die Überwachung von Ressourcen mit `top`, die Anpassung der Priorität mit `renice` und deren Beendigung mit `kill`. Dieses Labor vermittelt Ihnen praktische Erfahrungen mit dem Lebenszyklus von Prozessen, einschließlich deren Beendigung.

Dieses Labor wird Ihnen helfen, die Konzepte der Prozessverwaltung und -beendigung in realen Szenarien anzuwenden und Vertrauen in die Linux-Systemadministration aufzubauen.

## Quiz Question

Was ist der häufigste Beendigungsstatus für einen erfolgreich beendeten Prozess?

## Quiz Answer

0
