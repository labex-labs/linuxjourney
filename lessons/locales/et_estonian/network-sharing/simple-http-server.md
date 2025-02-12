# Simple HTTP Server

## Tunni sisu

Python'i programmeerimiskeeles on olemas väga kasulik tööriist failide teenindamiseks üle HTTP. See on kasulik, kui eesmärgiks on jagada faile kiirelt teistele masinatele võrgus. Selleks peab minema vaid kataloogi, mida on soov jagada ning sisestada:

<pre>$ python -m SimpleHTTPServer</pre>

See käsk seab üles algelise võrguserveri, millele pääseb ligi kohaliku kasutaja IP-aadressiga. Seega ei jäägi muud üle, kui haarata enda masina IP-aadress ja mõnes teises masinas avada veebilehitseja aadressiga *http://IP_AADRESS:8000*. Enda masinas saab vaadata kättesaadavaid faile sisestades veebilehitsejasse *http://localhost:8000.*

Sama saab teha ka kasutades GNU/Linuxiga virtuaalarvutit või kui kasutajal on arvutis Python 3. Lausekuju on küll veidi erinev.

## Harjutus

Proovida üles seada *SimpleHTTPServer*.

## Küsimus

Millise tööriista abil saab üles seada algelise HTTP serveri kasutades *python*'it?

## Vastus

*SimpleHTTPServer*
