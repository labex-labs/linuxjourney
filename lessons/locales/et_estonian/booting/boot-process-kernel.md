# Alglaadimisprotsess: Tuum

## Tunni sisu

Nüüd kui alglaadur on vajalikud parameetrid edastanud, vaatame kuida see alustab:

<b>Initrd vs Initramfs</b>

Rääkides tuuma alglaadimisest, on tegu väikest viisi kana ja muna probleemiga. Tuum haldab süsteemi riistvara kuid kõik juhtprogrammid ei ole alglaadimise ajal kättesaadavad. Oluline on ajutine juurfailisüsteem, mis sisaldab tuumale ainult esmavajalikke mooduleid, et käivitada ülejäänud riistvara. Vanemates Linuxi versioonides oli see ülesanne *initrd* (*initial ram disk*) nimelisel protsessil. Tuum haakis *initrd* külge ja hankis vajalikud alglaadimise juhtprogrammid. Seejärel kui kõige vajaliku laadimine oli lõpetatud, vahetati algne *initrd* juurfailisüsteemi vastu välja. Tänapäeval on meil *initramfs*, ajutine juurfailisüsteem, mis on otse tuuma sisse ehitatud. Selle ülesanne on laadida päris juurfailisüsteemile vajalikud juhtprogrammid, seega enam *initrd*'d vaja ei ole.

<b>Juurfailisüsteemi külge ühendamine</b>

Selleks hetkeks on tuumal kõik vajalikud moodulid, et luua juurseade ja haakida külge juurpartitsioon. Juurpartitsioon haagitakse tegelikult külge kirjutuskaitstult ja seetõttu saab *fsck* turvaliselt teostada terviklikkuse kontrolle. Hiljem haagitakse juurfailisüsteem uuesti külge aga siis juba ka kirjutamisõigustega. Seejärel tuvastab tuum *init*'i asukoha ja käivitab selle.

## Harjutus

Harjutust pole.

## Küsimus

Mida kasutatakse tänapäeval ajutise failisüsteemi laadimiseks?

## Vastus

*initramfs*
