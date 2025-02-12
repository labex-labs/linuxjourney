# cp (Copy)

## Lesson Content

Commençons par faire des copies de ces fichiers. Tout comme le copier/coller dans d'autres systèmes, l'invite de commandes nous offre un moyen plus simple de le faire. 

<pre>$ cp monfichiercool /home/pete/Documents/docscool</pre>

monfichiercool est le fichier à copier et /home/pete/Documents/docscool est la destination.

Vous pouvez copier plusieurs fichiers et dossiers avec l'utilisation des métacaractères. Un métacaractère est un caractère qui peut être substitué par une sélection de motifs, vous donnant plus de flexibilité dans la recherche. Vous pouvez utiliser des métacaractères dans chaque commande pour plus de flexibilité.

<ul>
<li>* le métacaractère des métacaractères, il est utilisé pour représenter n'importe quel caractère ou n'importe quelle chaîne de caractères.</li>
<li>? utilisé pour représenter un caractère.</li>
<li>[] utilisé pour représenter n'importe caractère dans les crochets.</li>
</ul>

<pre>$ cp *.jpg /home/pete/Pictures</pre>

Ceci va copier tous les fichiers d'extension .jpg du répertoire courant vers le dossier Pictures.

Une commande utile est l'utilisation du paramètre -r, il va copier de façon récursive les fichiers et répertoires.

Essayez d'exécuter cp sur un répertoire contenant des fichiers vers le répertoire Documents. Ça ne marche pas. Si?
Bien c'est parce que vous devez copier tous les fichiers et répertoires dans le dossier avec le paramètre -r.

<pre>$ cp -r Pumpkin/ /home/pete/Documents</pre>

Une chose à savoir, si vous copier un fichier vers un répertoire qui possède un fichier avec le même nom, il va écraser ce dernier. C'est désagréable si vous ne le désiriez pas. Vous pouvez utiliser le paramètre -i (interactive) qui demande votre accord avant d'écraser le fichier. 

<pre>$ cp -i monfichiercool /home/pete/Pictures</pre>

## Exercise

Copiez des fichiers, faites attention à ne pas écraser quelque chose d'important. ;)

## Quiz Question

Quel paramètre dois-tu utiliser pour copier tout un répertoire?

## Quiz Answer

-r