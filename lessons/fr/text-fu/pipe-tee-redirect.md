---
index: 4
lang: "fr"
title: "Tuyau et T"
meta_title: "Tuyau et T - Text-Fu"
meta_description: "Explorez la puissante commande pipe et tee sous Linux. Apprenez à chaîner des commandes avec la combinaison pipe tee de Linux et à rediriger la sortie à la fois vers l'écran et un fichier. Ce guide explique comment utiliser pipe vers tee pour un flux de données en ligne de commande avancé."
meta_keywords: "commande pipe et tee sous linux, linux pipe tee, pipe vers tee, pipe Linux, commande tee, stdout, stdin, redirection ligne de commande, tutoriel Linux"
---

## Lesson Content

Sous Linux, la ligne de commande devient incroyablement puissante lorsque vous commencez à connecter des commandes. Au lieu d'exécuter une commande, de sauvegarder sa sortie, puis d'en exécuter une autre, vous pouvez créer un pipeline pour transmettre les données directement entre elles.

### Comprendre l'Opérateur Pipe

Commençons par une commande qui produit beaucoup de sortie :

```bash
ls -la /etc
```

La liste des éléments est probablement trop longue pour tenir sur votre écran, ce qui la rend difficile à lire. Bien que vous puissiez rediriger cette sortie vers un fichier, une méthode plus efficace consiste à l'envoyer directement à une autre commande, comme `less`, pour une visualisation aisée.

```bash
ls -la /etc | less
```

L'opérateur pipe `|`, représenté par une barre verticale, est la clé de ce processus. Il prend la sortie standard (`stdout`) de la commande à sa gauche et l'utilise comme entrée standard (`stdin`) pour la commande à sa droite. Dans ce cas, nous avons _pipé_ la sortie de `ls -la /etc` directement dans la commande `less`. Le pipe est un outil fondamental que vous utiliserez constamment.

### Diviser la Sortie avec la Commande Tee

Et si vous souhaitez voir la sortie sur votre écran _et_ l'enregistrer simultanément dans un fichier ? C'est là qu'intervient la commande `tee`. La combinaison de commandes `pipe and tee command in linux` est un classique pour la journalisation et la surveillance.

```bash
ls | tee peanuts.txt
```

Après avoir exécuté ceci, vous verrez la sortie de `ls` sur votre terminal. Si vous vérifiez également le contenu de `peanuts.txt`, vous trouverez exactement les mêmes informations. La commande `tee` divise efficacement le flux de sortie en deux directions : une vers la sortie standard et une autre vers un fichier spécifié.

### Combiner Pipe et Tee

Vous pouvez créer des flux de travail encore plus avancés en chaînant ces commandes. Un modèle courant consiste à `pipe to tee` au milieu d'une chaîne de commandes plus longue. Cela vous permet de sauvegarder un résultat intermédiaire tout en continuant à traiter les données.

Par exemple, vous pouvez utiliser la combinaison `linux pipe tee` pour visualiser et sauvegarder la sortie avant un filtrage ultérieur :

```bash
ls -la /etc | tee etc_listing.txt | grep "conf"
```

Cette commande fait trois choses :

1. Elle liste le contenu du répertoire `/etc`.
2. Elle transmet cette sortie à `tee`, qui en sauvegarde une copie dans `etc_listing.txt` et la transmet également.
3. La sortie de `tee` est ensuite transmise à `grep`, qui filtre les lignes contenant "conf".

Maîtriser ces commandes améliorera considérablement votre efficacité sur la ligne de commande.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la redirection d'entrée/sortie et des pipelines :

1. **[Redirection d'Entrée et de Sortie sous Linux](https://labex.io/fr/labs/comptia-redirecting-input-and-output-in-linux-590840)** - Entraînez-vous à contrôler le flux de données des commandes en manipulant la sortie standard (stdout), l'erreur standard (stderr) et l'entrée standard (stdin) à l'aide d'opérateurs tels que `>`, `>>`, `2>`, et la commande `tee`.
2. **[Contrôle de Séquence et Pipeline Linux](https://labex.io/fr/labs/linux-sequence-control-and-pipeline-17994)** - Apprenez à contrôler les séquences d'exécution des commandes, à utiliser les pipelines et à exploiter des outils de traitement de texte puissants comme `cut`, `grep`, `wc`, `sort` et `uniq`.
3. **[Redirection de Flux de Données](https://labex.io/fr/labs/linux-data-stream-redirection-17995)** - Apprenez l'art de la redirection de flux sous Linux, y compris la manipulation des flux d'entrée, de sortie et d'erreur standard, la combinaison des sorties et l'utilisation de `/dev/null`.

Ces laboratoires vous aideront à appliquer les concepts de piping et de redirection dans des scénarios réels et à gagner en confiance dans la manipulation des données en ligne de commande.

## Quiz Question

Quel caractère unique représente l'opérateur pipe dans une commande Linux ? Veuillez répondre uniquement avec le symbole.

## Quiz Answer

|
