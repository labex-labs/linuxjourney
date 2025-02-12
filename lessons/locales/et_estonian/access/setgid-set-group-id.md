# Setgid

## Tunni sisu

Sarnaselt kasutaja ID õiguste seadistamise bitile on olemas ka grupi õiguste ID seadistamise bitt (SGID - *Set Group ID*). See bitt võimaldab programmi käivitada justkui oleks kasutaja vastava grupi liige.

Vaatame näidet:

<pre>
$ ls -l /usr/bin/wall

-rwxr-sr-x 1 root tty 19024 Dec 14 11:45 /usr/bin/wall
</pre>

Võib näha, et õiguste bitt on grupi õiguste osas.

<b>SGID muutmine</b>

<pre>
$ sudo chmod g+s minufail

$ sudo chmod 2555 minufail
</pre>

SGID'd numbriline esitus on 2.

Õiguste arvutamiseks on loodud ka mitmeid veebipõhiseid vahendeid, üks näide on <a target="_blank" href="http://permissions-calculator.org/">http://permissions-calculator.org/</a>

## Harjutus

Harutust pole.

## Küsimus

Milline number esindab SGID'd?

## Vastus

2
