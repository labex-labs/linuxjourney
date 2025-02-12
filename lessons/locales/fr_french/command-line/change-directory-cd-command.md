# cd (Change Directory)

## Lesson Content

Maintenant que vous savez où vous vous trouvez, voyons si nous pouvons un peu parcourir le système de fichiers. Souvenez-vous, nous nous déplacerons en utilisant des chemins. Il existe deux façons différentes de donner un chemin: chemins absolu et relatif. 

<ul>
<li>Chemin absolu: C'est le chemin ayant pour origine le répertoire racine. La racine est le grand patron. Le répertoire racine est généralement représenté à l'aide d'un slash (/). Chaque fois que votre chemin commence avec un /, cela signifie que vous venez du répertoire racine. Par exemple, /home/pete/Desktop.</li>

<li>Chemin relatif: C'est le chemin ayant pour origine le répertoire dans lequel vous vous trouvez. Si je me trouvais dans l'emplacement /home/pete/Documents et voudrais me rendre dans le répertoire "taxes" se trouvant dans Documents, j'ai pas besoin de préciser le chemin entier à partir de la racine comme ceci /home/pete/Documents/taxes, je peux juste faire ça à la place: taxes/</li>
</ul>

Maintenant que vous savez comment les chemins fonctionnent, nous avons besoin de quelque chose pour nous aider à nous rendre dans le répertoire que nous voulons. Heureusement, nous avons cd ou "change directory" (changer de répertoire) pour le faire. 

<pre>$ cd /home/pete/Pictures</pre> 

Alors j'ai changé mon emplacement en /home/pete/Pictures.

Maintenant dans ce répertoire j'ai un dossier à l'intérieur nommé Hawaï, je peux m'y rendre avec:

<pre>$ cd Hawaii</pre>

Remarquez vous comment j'ai juste utilisé le nom du dossier (Hawaï)? Parce que j'étais déjà dans /home/pete/Pictures.

Il peut être très fatiguant de se déplacer avec des chemins absolu et relatif, heureusement il existe des raccourcis pour vous aider. 

<ul>
<li>. (répertoire courant). C'est le répertoire dans lequel vous êtes actuellement.</li>
<li>.. (répertoire parent). Vous amène dans le répertoire au dessus de votre répertoire courant.</li>
<li>~ (répertoire home). Ce répertoire conduit à votre "répertoire maison" par défaut (on parle de "home"). Comme /home/pete.</li>
<li>- (répertoire précédent). Il vous conduira au répertoire précédent dont vous venez.</li>
</ul>

<pre>$ cd .
$ cd ..
$ cd ~
$ cd -
</pre>
Essayez!

## Exercise

<ol>
<li>Exécutez la commande cd sans paramètres, où vous conduit-il?</li>
</ol>

## Quiz Question

Si vous êtes dans /home/pete/pictures et voulez aller à /home/pete, quel est le bon raccourci à utiliser?

## Quiz Answer

cd ..
