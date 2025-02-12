# Join ja split

## Tunni sisu

Join käsk lubab ühise välja kaudu liita kokku mitu faili:

Näiteks kaks faili, mida on vaja kokku liita:

<pre>fail1.txt
1 John
2 Jane
3 Mary

fail2.txt
1 Doe
2 Doe
3 Sue

$ join fail1.txt fail2.txt
1 John Doe
2 Jane Doe
3 Mary Sue
</pre>

Failid ühendatakse vaikimisi esimese välja kaudu, mis peavad olema identsed. Kui nad seda ei ole, peaks neid korrastama, nii et praegusel juhul ühendatakse neid 1, 2, 3 abil.

Kuidas liita järgmisi faile?

<pre>fail1.txt
John 1
Jane 2
Mary 3

fail2.txt
1 Doe
2 Doe
3 Sue
</pre>

Et seda faili ühendada, peab täpsustama milliseid välju ühendada. Hetkel me tahame välja 2 fail1.txt'st ja välja 1 fail2.txt's, seega näeb käsk välja nii:

<pre>
$ join -1 2 -2 1 fail1.txt fail2.txt
1 John Doe
2 Jane Doe
3 Mary Sue
</pre>

*-1* viitab *fail1.txt*'le ja *-2* viitab *fail2.txt*'le. Päris uhke. Ühte faili on aga võimalik ka jagada mitme faili vahel, kui kasutad *split* käsku:

<pre>$ split mingifail</pre>

Nii jagatakse fail mitmeks failiks, vaikimisi eraldatakse nad, kui 1000 rea limiit täis saab. Failid nimetatakse vaikimisi x**.

## Harjutus

Liida kokku kaks faili, milles on erinev arv ridu. Mis juhtub?

## Küsimus

Millise käsuga liita kokku failid *kass, koer* ja *lehm*?

## Vastus

*join kass koer lehm*
