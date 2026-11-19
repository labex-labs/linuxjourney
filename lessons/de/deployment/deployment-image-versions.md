---
lesson_id: "deployment-image-versions"
course_id: "deployment"
lang: "de"
order_index: 2
title: "Image-Versionen"
description: "Lerne, wie du Image-Tags von Digests unterscheidest und die exakten Images zweier Umgebungen vergleichst."
meta_title: "Image-Versionen - Bereitstellung"
meta_description: "Lerne, wie du Image-Tags von Digests unterscheidest und die exakten Images zweier Umgebungen vergleichst."
meta_keywords: "Image-Versionen, Image-Tags, Digest, Bereitstellung, DevOps, Linux Journey"
---

Ein Tag wie `site:2` macht eine Image-Referenz gut lesbar. Beim Hochladen eines neuen Images kann derselbe Tag einem anderen Image zugeordnet werden. Um den genauen Inhalt zu bestimmen, halte den **Digest** fest. Dieser Wert wird aus dem referenzierten Inhalt berechnet.

## Einen Tag lesen

Angenommen, eine Registry zeigt an zwei verschiedenen Tagen die folgenden Einträge. Die abgekürzten Digests sind Beispiele, mit denen sich kein Image abrufen lässt.

```text
Monday    site:2    sha256:a1b2…
Tuesday   site:2    sha256:c3d4…
```

Der Tag zeigt jetzt auf einen anderen Inhalt. Ein Rechner, der das Image am Montag abgerufen hat, kann weiterhin die ältere Version verwenden.

:::single-choice{#deployment-image-versions-moving-tag} Beide Umgebungen melden den Tag site:2. Woran erkennst du, welches Image sie tatsächlich abgerufen haben?

::option[Allein am gemeinsamen Tag.]{#deployment-image-versions-moving-tag-b explanation="Im Beispiel tragen beide unterschiedlichen Images denselben Tag."}
::option[An der Anzahl der Container auf einem der Rechner.]{#deployment-image-versions-moving-tag-c explanation="Diese Zahl identifiziert die verwendeten Images nicht."}
::option[An den aufgezeichneten Digests.]{#deployment-image-versions-moving-tag-a .correct explanation="Der Tag kann neu zugeordnet werden. Der Digest identifiziert den Inhalt, der beim Abruf ausgewählt wurde."}
:::

## Eine Digest-Referenz lesen

Eine Image-Referenz kann ein `@` mit anschließendem vollständigen Digest enthalten. Die Registry liefert dann genau das referenzierte Objekt. Verwende den vollständigen Digest aus der Registry oder dem Build-Eintrag. Verkürzte Werte eignen sich zur Anzeige in Beispielen. Für den Abruf brauchst du den vollständigen Wert.

:::single-choice{#deployment-image-versions-fixed-reference} Welche Angabe wählt ein bestimmtes Objekt aus der Registry aus?

::option[Der Image-Name ohne Tag.]{#deployment-image-versions-fixed-reference-a explanation="Docker verwendet dafür einen Standard-Tag, der auf einen anderen Inhalt verschoben werden kann."}
::option[Der Image-Name mit dem vollständigen Digest.]{#deployment-image-versions-fixed-reference-c .correct explanation="Der Digest verweist auf einen bestimmten Inhalt."}
::option[Ein Kommentar mit dem Datum des Builds.]{#deployment-image-versions-fixed-reference-b explanation="Die Registry kann kein Objekt anhand eines Kommentars abrufen."}
:::

## Images für dieselbe Plattform vergleichen

Ein Image-Name kann auf eine Liste mit Builds für verschiedene Rechnertypen oder auf ein Image für eine bestimmte Plattform verweisen. Halte beim Vergleich zweier Hosts fest, für welche Plattform sie ausgelegt sind, und vergleiche die passenden plattformspezifischen Image-Referenzen. Bewahre die vollständige Originalreferenz im Release-Eintrag auf.

:::single-choice{#deployment-image-versions-compare-platform} Ein Release unterstützt arm64 und amd64. Welcher Vergleich ist bei zwei amd64-Hosts hilfreich?

::option[Die amd64-Image-Referenzen, die beide Hosts ausgewählt haben.]{#deployment-image-versions-compare-platform-b .correct explanation="Du vergleichst die Inhalte für dieselbe Plattform."}
::option[Images für unterschiedliche Architekturen.]{#deployment-image-versions-compare-platform-a explanation="Diese Objekte sind für unterschiedliche Plattformen vorgesehen."}
::option[Die Hostnamen.]{#deployment-image-versions-compare-platform-c explanation="Die Namen identifizieren die Rechner, aber nicht die bereitgestellten Inhalte."}
:::

## Zusammenfassung

Du kannst jetzt genau feststellen, welches Image hinter einem Tag verwendet wurde.

1. Erkläre, warum derselbe Tag auf unterschiedliche Inhalte zeigen kann.
2. Erkenne eine vollständige Digest-Referenz.
3. Vergleiche die Image-Referenzen für die passende Plattform.
