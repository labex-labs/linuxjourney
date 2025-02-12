# lsof ja fuser

## Tunni sisu

Ütleme, et kasutaja ühendab aruvisse USB pulga ja alustab tööd sealsete failidega. Kui aga töö on tehtud ja hakatakse pulka lahti ühendama ilmub veateade "Seade või ressurss on hõivatud". Kuidas saada teada, millised failid USB pulgal on endiselt kasutuses? Selle jaoks on isegi kaks tööriista:

<b>lsof</b>

Meenutame, et failid ei ole ainult tekstifailid, pildid ja muu selline vaid kõik, mis süsteemis asub: kettad, torud, võrgusoklid, seadmed jne. Et kuvada, mida protsessid parasjagu kasutavad, võib kasutada *lsof* (*list open files*) käsku. Kuvatakse nimekiri avatud failidest ja seotud protsessidest.

<pre>
pete@icebox:~$ lsof .
COMMAND    PID  USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
lxsession 1491 pete  cwd    DIR    8,6     4096  131 .
update-no 1796 pete  cwd    DIR    8,6     4096  131 .
nm-applet 1804 pete  cwd    DIR    8,6     4096  131 .
indicator 1809 pete  cwd    DIR    8,6     4096  131 .
xterm     2205 pete  cwd    DIR    8,6     4096  131 .
bash      2207 pete  cwd    DIR    8,6     4096  131 .
lsof      5914 pete  cwd    DIR    8,6     4096  131 .
lsof      5915 pete  cwd    DIR    8,6     4096  131 .
</pre>

Selliselt saab teada, mis protsessid hoiavad seadet, faili avatuna.  Meie USB näite kohaselt võib need protsessid pulga eemaldamiseks peatada.

<b>fuser</b>

*fuser* (*file user*) on veel üks võimalus kuidas protsessi jälgida. Käsk kuvab informatsiooni protesside kohta, mis mingit faili kasutavad.

<pre>
pete@icebox:~$ fuser -v .
                     USER        PID ACCESS COMMAND
/home/pete:         pete  1491 ..c.. lxsession
                     pete  1796 ..c.. update-notifier
                     pete  1804 ..c.. nm-applet
                     pete  1809 ..c.. indicator-power
                     pete  2205 ..c.. xterm
                     pete  2207 ..c.. bash
</pre>

Võime näiteks kuvada, millised protsessid kasutavad hetkel meie kodukataloogi. *lsof* ja *fuser* tööriistad on väga sarnased. Kasutaja võiks nendega tuttavaks saada ja proovida neid kasutada järgmine kord kui on tarvis mõnda faili või protsessi jälgida.

## Harjutus

Lugeda *lsof* ja *fuser* man-lehekülgi. Sealt võib leida hulgaliselt informatsiooni, mida selles peatükis ei avaldatud kuid võimaldavad nende tööriistade kasutamisel suuremat paindlikust.

## Küsimus

Millise käsuga kuvatakse avatud failid ja nende protsessi informatsioon?

## Vastus

*lsof*
