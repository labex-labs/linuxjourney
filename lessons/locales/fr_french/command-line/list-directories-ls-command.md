# ls (List Directories)

## Lesson Content

Maintenant que nous savons comment se déplacer dans le système, comment savoir ce qui nous est accessible? Actuellement, c'est comme si on progressait dans le noir. Bien, nous pouvons utiliser la formidable commande ls pour lister le contenu d'un répertoire. La commande ls va lister les dossiers et fichiers présents dans le répertoire où vous vous trouvez. Cependant, vous pouvez préciser le chemin du répertoire dont vous voulez lister le contenu.

<pre>$ ls
$ ls /home/pete</pre>

ls est un outil très utile, il vous montre aussi les informations sur les fichiers et dossiers que vous regardez.

Notez aussi que ce ne sont pas tous les fichiers dans le répertoire qui seront visibles. Les noms de fichiers commençant avec "." sont cachés, vous pouvez cependant les voir en ajoutant le paramètre "-a" (a pour dire "tout", all en anglais) à la commande ls.

<pre>$ ls -a</pre>

Il existe aussi un autre paramètre utile, "-l" pour "long", il donne une liste détaillée des fichiers dans un grand (long) format. Il vous affiche des informations détaillées, allant de la gauche: droit d'accès, nombre de liens, nom du propriétaire, groupe propriétaire, taille, date de la dernière modification, et le nom du fichier/répertoire. 

<pre>$ ls -l</pre>

<pre>pete@icebox:~$ ls -l
total 80
drwxr-x--- 7 pete penguingroup   4096 Nov 20 16:37 Desktop
drwxr-x--- 2 pete penguingroup   4096 Oct 19 10:46  Documents
drwxr-x--- 4 pete penguingroup   4096 Nov 20 09:30 Downloads
drwxr-x--- 2 pete penguingroup   4096 Oct  7 13:13   Music
drwxr-x--- 2 pete penguingroup   4096 Sep 21 14:02 Pictures
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41   Public
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41   Templates
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41   Videos</pre>

Les commandes ont ce qu'on appelle des paramètres (ou arguments ou options, peu importe comment vous les appelez) pour ajouter plus de fonctionnalités. Rappelez comment nous avons ajoutés -a et -l, bien vous pouvez les utiliser ensemble en faisant "-la". L'ordre des paramètres détermine quel ordre suit le résultat, bien des fois c'est pas problématique alors vous pouvez faire "ls -al" et ça fonctionnera aussi.

<pre>$ ls -la</pre>

## Exercise

Exécutez ls avec différents paramètres et regardez le résultat reçu.

## Quiz Question

Quelle commande devriez vous utiliser pour voir les fichiers cachés?

## Quiz Answer

ls -a
