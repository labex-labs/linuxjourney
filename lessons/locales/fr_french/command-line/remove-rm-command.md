# rm (Remove)

## Lesson Content

Maintenant, je crois que nous avons beaucoup de fichiers, supprimons en quelques-uns. La commande 'rm' (remove - supprimer) est utilisé pour supprimer les fichiers et répertoires. 

<pre>$ rm fichier1</pre>

Faites attention en utilisant la commande rm, il y a pas de corbeille magique où vous pouvez récupérer les fichiers supprimés. Une fois supprimés, ils sont supprimés pour de bon, donc attention. 

Heureusement il existe des mesures de sécurité mises en place, donc un utilisateur normal ne peut pas supprimer un ensemble de fichiers importants. Une confirmation vous sera demandée avant la suppression. Si le répertoire est protégé en écriture, il sera aussi difficile à supprimer. 

Maintenant si vous n'avez que faire de ça, vous pouvez bien sûr supprimer un ensemble de fichiers. 

<pre>$ rm -f fichier1</pre>

L'option -f ou force dit à rm de supprimer tous les fichiers, qu'ils soient protégés en écriture ou pas, sans demande de confirmation (tant que vous avez les droits d'accès nécessaires).

<pre>$ rm -i fichier</pre>

L'ajout du paramètre -i vous demandera confirmation avant la suppression des fichiers ou répertoires. 

<pre>$ rm -r répertoire</pre>

Normalement, vous ne pouvez pas supprimer un répertoire avec juste rm, vous devez ajouter le paramètre -r (récursif) pour aussi supprimer les fichiers et sous-répertoires qu'il pourrait contenir.

Vous pouvez supprimer un répertoire avec la commande rmdir

<pre>$ rmdir répertoire</pre>

## Exercise

<ol>
<li>Créez un fichier appelé "-fichier" (n'oubliez pas le tiret)</li>
<li>Supprimez ce fichier.</li>
</ol>

## Quiz Question

Comment supprimer un fichier appelé monfichier?

## Quiz Answer

rm monfichier