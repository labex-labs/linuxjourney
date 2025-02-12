# L'environnement de commandes (Le Shell)

## Lesson Content

Le monde est à votre portée, ou plus précisément l'environnement (ou interpréteur) de commandes (le shell) est à votre portée. C'est quoi l'environnement de commandes? L'environnement de commandes est simplement un programme qui récupère vos commandes du clavier et les envoie au système d'exploitation pour exécution. Si vous avez déjà utilisé une interface graphique, vous avez certainement vu des programmes comme "Terminal" ou "Console"; ce sont juste des programmes qui exécutent l'environnement de commandes pour vous. Tout au long de ce cours, nous allons apprendre les merveilles de l'environnement de commandes.

Dans ce cours, nous utiliserons l'environnement de commandes bash (Bourne Again shell), présent dans presque toutes les distributions Linux. Il existe d'autres environnements de commandes tels que ksh, zsh, tsch, mais nous n'en parlerons pas.

Commençons! En fonction de la distribution, votre invité de commandes peut différer, mais la plupart suivent le format suivant:
<pre>nom_utilisateur@nom_de_la_machine:repertoire_courant
pete@icebox:/home/pete $</pre>

Avez-vous remarquer le $ à la fin de la commande? La commande peut varier en fonction de l'environnement de commandes, dans notre cas, le $ est pour un utilisateur normal de l'environnement de commandes Bash, Bourne ou Kon. Vous ne précisez pas ce symbole lorsque vous tapez la commande, sachez juste qu'il est là.

Commençons avec une simple commande, echo. La commande echo affiche juste le texte en paramètre.

<pre>$ echo Hello World</pre>

## Exercise

Essayez d'autres commandes Linux et voyez ce qu'elles affichent:

<ol>
<li>$ date</li>
<li>$ whoami</li>
</ol>

## Quiz Question

Que devrait s'afficher quand vous saisissez la commande echo Hello World?

## Quiz Answer

Hello World
