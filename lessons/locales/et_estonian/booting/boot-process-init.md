# Alglaadimisprotsess: Init

## Tunni sisu

*Init* on eelmistes peatükkides juba vaatluse all olnud ja on teada, et see on esimene protsess, mis käivitatakse ja see omakorda käivitab teised esmatähtsad teenused. Aga kuidas?

Linuxis on *init*'il kolm peamist kehastust:

<b>System V init (sysv)</b>

See on traditsiooniline *init*, mis käivitab ja peatab protsesse alglaadimise skriptil põhinevas järjekorras.  Masina seisundit märgib *runlevel* (*töötasand*). Iga *runlevel* alustab või peatab masina erineval moel.

<b>Upstart</b>

Selle *init*'i leiab vanematelt Ubuntu paigaldustelt. Upstart kasutab teenuste ja sündmuste ideed käivitades teenuseid ja teostades teatud tegevusi reaktsioonina sündmustele.

<b>Systemd</b>

See on *init*'i uus eesmärgile orienteeritud standard. Põhimõtteliselt on olemas eesmärk ja *systemd* üritab lahendada eesmärgi sõltuvusi, et seda täita.

*Init*'i süsteemide kohta on tulemas terve kursus, kus süveneme neisse kolmesse palju detailsemalt.

## Harjutus

Selles peatükis harjutust ei ole.

## Küsimus

Milline on uusim *init*'i standard?

## Vastus

systemd
