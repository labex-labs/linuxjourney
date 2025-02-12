# pwd (Print Working Directory)

## Lesson Content

Tout dans Linux est un fichier, vous comprendrez cela dans votre voyage dans Linux, mais retenez ça pour le moment. Chaque fichier est organisé selon une arborescence hiérarchique. Le premier répertoire dans le système de fichiers est appelé le répertoire racine. Le répertoire racine contient beaucoup de dossiers et fichiers dont vous pouvez stocker plus de répertoires et fichiers, etc. Ceci est un exemple d'arborescence: 

<pre>/
|-- bin
|   |-- fichier1
|   |-- fichier2
|-- etc
|   |-- fichier3
|   `-- répertoire1
|       |-- fichier4
|       `-- fichier5
|-- home
|-- var
</pre>

L'emplacement de ces fichiers et répertoires est indiqué par des chemins. Si vous avez un répertoire nommé "home" avec un dossier à l'intérieur appelé "pete" et lui même possédant un dossier nommé "Movies", le chemin serait comme ceci: /home/pete/Movies, très simple hein?

La navigation dans le système de fichiers, un peu comme dans la vraie vie, est utile si vous savez où vous êtes et où vous allez. Pour voir où vous êtes, vous pouvez utiliser la commande pwd, elle signifie "print working directory" (affiche le répertoire de travail) et il vous montre le répertoire dans lequel vous êtes. Notez que le chemin commence au répertoire racine.

<pre>$ pwd</pre>

Où êtes-vous? Où suis-je? Essayez.

## Exercise

Pas d'exercices dans cette leçon.

## Quiz Question

Comment trouve t-on le répertoire dans lequel on se trouve actuellement?

## Quiz Answer

pwd
