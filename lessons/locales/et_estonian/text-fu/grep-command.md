# grep

## Tunni sisu

Grep on kõige tavalisem tekstitöötlemise käsk. See võimaldab otsida failist tähemärke, mis vastavad teatud mustrile. Mis siis kui tahta teada, kas mingi fail eksisteerib mingis konkreetses kataloogis või kas mingis failis asub otsitav sõne? Kindlasti ei hakkaks keegi kogu teksti läbi otsima vaid kasutaks grep'i!

Kasutame näitena näide.txt faili:

<pre>$ grep rebane näide.txt</pre>

Peaks nägema, et *grep* leidis sõna *rebane* failist *näide.txt*

Saab otsida ka väike- ja suurtähedele mittetundlikku teksti, kui kasutada lippu *-i*.

<pre>$ grep -i mingimuster mingifail</pre>

Et veelgi paindlikkust lisada, võib *grep*'i kombineerida teiste käskudega | operaatoriga.

<pre>$ env | grep -i Kasutaja</pre>

Nagu näha, on grep väga mitmekülgne. Mustris võib kasutada ka regulaaravaldisi:

<pre>$ ls /mingikat | grep '.txt$'</pre>

Peaks kuvama kataloogist mingikat kõik TXT-tüüpi tekstifailid.

## Harjutus

Ehk ollakse kuulnud käskudest *egrep* ja *fgrep*, need on nüüd vananenud ning asendatud käskudega *grep -E* ja *grep -F*. Lugeda *grep*'i man lehekülge ja saab rohkem teada.

## Küsimus

Millist käsku kasutada, et mingit tähemärgi kombinatsiooni leida?

## Vastus

*grep*
