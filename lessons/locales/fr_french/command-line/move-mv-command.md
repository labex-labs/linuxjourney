# mv (Move)

## Lesson Content

Utilisée pour déplacer des fichiers et les renommer aussi. Identique à la commande cp avec les paramètres et fonctionnalités. 

Vous pouvez renommer un fichier comme ceci:

<pre>$ mv vieuxfichier nouveaufichier</pre>

Ou bien vous pouvez déplacer un fichier vers un répertoire différent: 

<pre>$ mv fichier2 /home/pete/Documents</pre>

Et déplacer plus d'un fichier:

<pre>$ mv fichier_1 fichier_2 /unrepertoire</pre>

Vous pouvez aussi renommer les dossiers:

<pre>$ mv repertoire1 repertoire2</pre>

Comme la commande cp, si vous déplacer un fichier ou répertoire, il va écraser le fichier/répertoire ayant le même nom. Donc vous pouvez utiliser le paramètre -i qui demande votre accord avant d'écraser.

<pre>mv -i repertoire1 repertoire2</pre>

Disons que vous avez voulu déplacer un fichier en écrasant l'existant. Vous pouvez faire une récupération du fichier écrasé et il sera nommé avec un ~. 

<pre>$ mv -b repertoire1 repertoire2</pre>

## Exercise

Renommez un fichier, puis déplacez dans un répertoire différent.

## Quiz Question

Comment renommer le fichier "cat" en "dog"?

## Quiz Answer

mv cat dog