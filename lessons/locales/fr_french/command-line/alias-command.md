# alias

## Lesson Content

Des fois taper des commandes peut devenir répétitif, or si vous devez taper une longue commande à plusieurs reprises, il est mieux d'avoir un alias que vous pouvez utiliser pour. Pour créer un alias pour une commande, vous donnez simplement le nom de l'alias et y affectez la commande. 

<pre>$ alias foobar='ls -la'</pre>

Ainsi, au lieu de taper ls -la, vous pouvez taper foobar et il exécutera la commande, un outil super. Sachez que votre alias n'existera plus après un redémarrage. Vous aurez besoin d'ajouter un alias permanent dans le fichier:

<pre>~/.bashrc</pre>

ou fichiers similaires si vous voulez qu'il existe même après un redémarrage.

Vous pouvez supprimer les alias avec la commande unalias:

<pre>$ unalias foobar</pre>

## Exercise

Créez quelques alias puis supprimez-les.

## Quiz Question

Quelle commande utilise-t-on peut créer un alias?

## Quiz Answer

alias
