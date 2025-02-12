# history

## Lesson Content

Dans votre invité de commande, il y a l'historique des commandes que vous avez précédemment saisies, vous pouvez en fait consulter ces commandes. C'est bien utile quand vous voulez chercher et exécuter une commande précédemment utilisée sans la saisir à nouveau.

<pre>$ history</pre>

Envie de réexécuter une même commande, appuyez juste sur la flèche haut du clavier.

Envie de réexécuter une commande sans la saisir à nouveau? Taper juste "!!". Si vous avez exécuté la commande "cat fichier1" et voulez la réexécuter, vous pouvez juste faire !! et il exécutera votre dernière commande. 

Un autre raccourci de l'historique est ctrl+R, c'est une commande de recherche inversée, si faites ctrl+R et commencez à saisir des termes de la commande que vous désirez, il vous affichera toutes les commandes correspondantes et vous pouvez les voir en faisant les touches ctrl+R. Une fois que vous trouvez votre commande, tapez juste la touche Entrée.

Notre invité de commande devient un peu touffu. Non? Faisons un peu de nettoyage, utilisez la commande "clear" pour effacer le tableau.

<pre>$ clear</pre>

Là c'est mieux. N'est-ce pas? 

Parlant des choses utiles, une des fonctionnalités les plus importantes dans n'importe quel invité de commandes est la complétion à l'aide de la touche de tabulation. Si vous commencez à saisir le début d'une commande, d'un fichier, un répertoire, etc et appuyez la touche de tabulation, il va compléter automatiquement en se basant sur ce qu'il a trouvé dans le répertoire dans lequel vous êtes et si vous n'avez pas d'autres fichiers débutants par les mêmes caractères. Par exemple, si vous essayez d'exécuter la commande chrome, vous pouvez saisir chr et tapez la touche Tab et il complétera chrome.

## Exercise

Consultez l'historique de vos commandes avec les touches Haut et Bas. Amusez-vous avec le recherche inversée ctrl+R.

## Quiz Question

Quelle est la commande pour nettoyer la console?

## Quiz Answer

clear
