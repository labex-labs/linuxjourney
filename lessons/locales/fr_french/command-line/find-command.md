# find

## Lesson Content

Avec tous ces fichiers que nous avons dans notre machine, il peut devenir fiévreux de trouver un fichier spécifique. Bien, il existe une commande pour nous aider, 'find'! 

<pre>$ find /home -name puppies.jpg</pre>

Avec find, vous devez précisez le dossier dans lequel vous allez faire la recherche et ce que vous voulez rechercher. Dans notre cas, on veut trouver un fichier à travers son nom puppies.jpg.

Vous pouvez préciser le type de fichier vous chercher. 

<pre>$ find /home -type d -name MonDossier</pre>

Vous pouvez voir que j'ai mis le type de fichier à chercher comme un dossier avec (d) et je cherche aussi par le nom MonDossier. 

Une chose géniale à savoir est que find ne s'arrête pas dans le répertoire où vous vous trouvez, il cherche aussi dans les sous-répertoires.

## Exercise

<ol>
<li>Cherchez un fichier dans le répertoire racine (root) qui contient le terme "net".</li>
</ol>

## Quiz Question

Quelle option devrais-je spécifier si je veux effectuer une recherche par nom?

## Quiz Answer

-name