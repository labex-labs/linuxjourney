---
index: 2
lang: "fr"
title: "Niveaux de privilège"
meta_title: "Niveaux de privilège - Kernel"
meta_description: "Découvrez les niveaux de privilège Linux, le mode noyau et le mode utilisateur. Comprenez les anneaux de protection et les appels système pour un accès sécurisé au matériel. Commencez votre parcours Linux !"
meta_keywords: "niveaux de privilège Linux, mode noyau, mode utilisateur, anneaux de protection, appels système, sécurité Linux, Linux pour débutants, tutoriel Linux"
---

## Lesson Content

Les prochaines leçons seront assez théoriques, donc si vous cherchez des choses pratiques, vous pouvez passer à la suite et revenir plus tard.

Pourquoi avons-nous différentes couches d'abstraction pour l'espace utilisateur et le noyau ? Pourquoi ne pouvez-vous pas combiner les deux pouvoirs en une seule couche ? Eh bien, il y a une très bonne raison pour laquelle ces deux couches existent séparément. Elles fonctionnent toutes deux dans des modes différents : le noyau fonctionne en mode noyau, et l'espace utilisateur fonctionne en mode utilisateur.

En mode noyau, le noyau a un accès complet au matériel ; il contrôle tout. En mode espace utilisateur, il y a une très petite quantité de mémoire et de CPU sûrs auxquels vous êtes autorisé à accéder. En gros, lorsque nous voulons faire quoi que ce soit qui implique le matériel — lire des données de nos disques, écrire des données sur nos disques, contrôler notre réseau, etc. — tout cela est fait en mode noyau. Pourquoi est-ce nécessaire ? Imaginez si votre machine était infectée par un logiciel espion ; vous ne voudriez pas qu'il ait un accès direct au matériel de votre système. Il pourrait accéder à toutes vos données, votre webcam, etc., et ce n'est pas bon.

Ces différents modes sont appelés niveaux de privilège (nommés à juste titre pour les niveaux de privilège que vous obtenez) et sont souvent décrits comme des anneaux de protection. Pour rendre cette image plus facile à peindre, disons que vous découvrez que Britney Spears est en ville dans votre club local. Elle est protégée par ses groupies, puis ses gardes du corps personnels, puis le videur à l'extérieur du club. Vous voulez obtenir son autographe (parce que pourquoi pas ?), mais vous ne pouvez pas l'atteindre car elle est fortement protégée. Les anneaux fonctionnent de la même manière : l'anneau le plus interne correspond au niveau de privilège le plus élevé. Il existe deux niveaux ou modes principaux dans une architecture informatique x86. L'anneau #3 est le privilège dans lequel les applications en mode utilisateur s'exécutent ; l'anneau #0 est le privilège dans lequel le noyau s'exécute. L'anneau #0 peut exécuter n'importe quelle instruction système et bénéficie d'une confiance totale. Alors maintenant que nous savons comment fonctionnent ces niveaux de privilège, comment pouvons-nous écrire quoi que ce soit sur notre matériel ? Ne serons-nous pas toujours dans un mode différent de celui du noyau ?

La réponse est avec les appels système. Les appels système nous permettent d'exécuter une instruction privilégiée en mode noyau, puis de revenir en mode utilisateur.

## Exercise

Pas d'exercices pour cette leçon.

## Quiz Question

Quel numéro d'anneau a les privilèges les plus élevés ?

## Quiz Answer

0
