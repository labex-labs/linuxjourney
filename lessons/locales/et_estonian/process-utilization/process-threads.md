# Protsessi lõimed

## Tunni sisu

Vahest on kuuldud väljendeid ühelõimeline ja mitmelõimeline protsess? Lõimed on protsessidele väga sarnased selle poolest, et neid kasutatakse sama programmi käivitamiseks. Neid nimetatakse vahel lihtsustatud protsessideks. Kui protsessil on ainult üks lõim on ta ühelõimeline ja kui lõimi on rohkem kui üks on see mitmelõimeline. Kõikidel protsessidel on vähemalt üks lõim.

Protsessid opereerivad isiklike isoleeritud süsteemi ressurssidega kuid lõimed võivad neid ressursse omavahel jagada kerge vaevaga. See teeb omavahelise suhtlemise lihtsamaks. Samuti on mitmelõimeline rakendus mõnikord otstarbekam ja tõhusam kui mitmeprotsessiline rakendus.

Kui avada LibreOffice Writer ja Chrome, on need mõlemad eraldi protsessid. Kui aga kasutada Writerit ja hakata teksti töötlema, salvestatakse muudatused automaatselt. Need kaks paralleelset salvestamise ja muudatuste "lihtustatud protsessi" ongi lõimed.

Protsessi lõimede kuvamiseks võib kasutada:

<pre>
pete@icebox:~$ ps m
  PID TTY      STAT   TIME COMMAND
 2207 pts/2    -      0:01 bash
    - -        Ss     0:01 -
 5252 pts/2    -      0:00 ps m
    - -        R+     0:00 -
</pre>

Protsesse tuvastab nende PID ja protsesside all kuvatakse nende lõimed (tuvastatavad  - - järgi). Seega võib näha, et üleval kuvatavad protsessid on mõlemad ühelõimelised.

## Harjutus

Käivitada <b>ps m</b> käsk ja selgitada välja, millised protsessid on mitmelõimelised.

## Küsimus

Õige või vale? Kõik protsessid on alguses ühelõimelised.

## Vastus

õige
