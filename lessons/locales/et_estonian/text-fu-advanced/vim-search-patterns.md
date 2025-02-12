# Vim'i otsingumustrid

## Tunni sisu

Et mõnda väljendit otsida, sisestada lihtsalt / ja siis otsitav sõna või sümbolid, kui vim sessioon juba käib. Kui oled vajutanud Enter, võid liikuda otsitulemuste seas edasi ja tagasi vastavalt klahvidega "n" ja "N".


<pre>
Minu kaunis fail on väga kaunis.

/kaunis

leiab tekstifailist sõnad kaunis.
</pre>

? otsingukäsk otsib failist tagurpidi järjekorras. Eelmise näite põhjal leitakse kõigepealt viimane sõna "kaunis".

<pre>
Minu kaunis fail on väga kaunis.

?kaunis

leiab tekstifailist sõnad kaunis tagurpidi järjekorras.
</pre>

## Harjutus

Mängi natuke otsinguga. Ava vim'iga tekstifail: vim [tekstifail] ja asu otsima!

## Küsimus

Millist sümbolit kasutab vim, et teostada ostingut?

## Vastus

/
