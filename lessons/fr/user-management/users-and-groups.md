---
lesson_id: "users-and-groups"
course_id: "user-management"
lang: "fr"
order_index: 1
title: "Utilisateurs et groupes"
description: "Découvrez comment Linux identifie utilisateurs et groupes et comment les identifiants des processus influencent les accès."
meta_title: "Utilisateurs et groupes - Gestion des utilisateurs"
meta_description: "Comprenez utilisateurs et groupes Linux, UID, GID, root et la délégation de privilèges avec sudo."
meta_keywords: "utilisateurs Linux, groupes Linux, sudo, root, UID, GID, gestion utilisateurs"
---

Linux utilise les identités d'utilisateurs et de groupes pour étiqueter les processus, attribuer les objets du système de fichiers et décider des accès. Les noms aident les administrateurs ; le noyau travaille surtout avec des identifiants numériques et les attributs des processus.

## Identifier les utilisateurs avec les UID

Chaque compte possède un identifiant numérique, ou **UID**. Les bases de comptes associent les noms aux UID. Les fichiers stockent une propriété numérique que les outils affichent normalement comme un nom.

```bash
$ id
uid=1000(alice) gid=1000(alice) groups=1000(alice),27(sudo)
```

Les valeurs varient. Les comptes humains ont souvent un répertoire comme `/home/alice`, mais peuvent en avoir un autre ou aucun. Les comptes de service exécutent souvent un logiciel avec une identité limitée plutôt que d'autoriser une connexion interactive.

:::single-choice{#users-uid-purpose} Quel identifiant le noyau utilise-t-il principalement pour représenter un utilisateur ?

::option[Le chemin de son répertoire personnel]{#users-home-path explanation="Le chemin est une configuration variable ou absente, pas l'identifiant du noyau."}
::option[Un UID numérique]{#users-numeric-uid .correct explanation="Les bases associent les noms aux UID employés dans les attributs de processus et la propriété."}
::option[Le numéro d'une fenêtre de terminal]{#users-terminal-number explanation="Terminaux et sessions sont distincts des identités utilisateur."}
:::

## Organiser les accès avec les groupes

Un groupe possède un identifiant numérique, ou **GID**. Un compte a normalement un groupe principal et peut appartenir à des groupes supplémentaires. Cela permet d'accorder un accès collectif.

```bash
$ id alice
$ groups alice
```

Ces commandes donnent les identités configurées ou résolues. Des annuaires et caches peuvent participer ; lire seulement `/etc/group` ne montre donc pas toujours l'ensemble effectif.

:::single-choice{#users-primary-supplementary-groups} Comment un compte Linux participe-t-il normalement aux groupes ?

::option[Il appartient exactement à un groupe toute sa vie.]{#users-single-group explanation="Un processus peut porter un groupe principal et une liste de groupes supplémentaires."}
::option[Il appartient à tous les groupes dont il peut lire les fichiers.]{#users-readable-groups explanation="La lisibilité résulte des droits ; elle ne crée pas d'appartenance."}
::option[Il a un groupe principal et peut avoir des groupes supplémentaires.]{#users-group-memberships .correct explanation="Le GID principal figure dans le compte et les appartenances supplémentaires ajoutent d'autres identités."}
:::

## Comprendre les attributs des processus

Un processus possède notamment des UID et GID réels et effectifs, ainsi que des groupes supplémentaires. Les valeurs effectives interviennent dans de nombreux contrôles. Un processus hérite généralement de son parent, mais des mécanismes contrôlés peuvent changer ces identités.

Les exécutables set-user-ID, gestionnaires de services, conteneurs, espaces de noms et appels de changement de privilèges rendent cette description plus exacte que « le processus s'exécute uniquement comme son lanceur ».

:::single-choice{#users-process-access-identity} Quelles informations sont couramment comparées aux permissions d'un fichier ?

::option[L'UID effectif, le GID effectif et les groupes supplémentaires du processus.]{#users-effective-credentials .correct explanation="Ces attributs sont comparés à la propriété et aux permissions lors des contrôles discrétionnaires."}
::option[Le thème de couleurs du terminal.]{#users-terminal-theme explanation="Les préférences d'affichage n'interviennent pas dans les permissions."}
::option[La longueur du nom du compte.]{#users-username-length explanation="Le noyau emploie des identifiants numériques ; la longueur du nom n'accorde rien."}
:::

## Reconnaître l'identité root

Le compte traditionnellement nommé `root` possède l'UID 0, traité spécialement par de nombreux mécanismes et doté d'un large pouvoir. Capacités, espaces de noms, contrôles obligatoires et confinement peuvent toutefois diviser ce pouvoir.

Travaillez au quotidien avec un compte non privilégié : l'autorité administrative amplifie l'impact des erreurs de chemin, commandes non fiables et logiciels compromis.

:::single-choice{#users-root-uid} Quel UID numérique identifie traditionnellement root ?

::option[`0`]{#users-uid-zero .correct explanation="Les systèmes Unix et Linux réservent traditionnellement l'UID 0 au superutilisateur."}
::option[`1000`]{#users-uid-thousand explanation="De nombreuses distributions l'attribuent au premier compte humain, pas à root."}
::option[`1`]{#users-uid-one explanation="L'UID 1 peut appartenir à un compte système et n'est pas l'identité root."}
:::

## Utiliser sudo selon une politique

`sudo` consulte sa politique pour décider si l'appelant peut exécuter une commande comme utilisateur cible. La cible par défaut est souvent root, mais `-u USER` peut en choisir une autre. Authentification et journalisation dépendent aussi de la configuration.

```bash
$ sudo -l
```

N'utilisez une commande administrative autorisée que si la tâche l'exige et que vous en comprenez les effets. N'employez pas `sudo` pour faire taire une erreur de permission, ni pour afficher sans raison une base de hachages comme `/etc/shadow`.

:::single-choice{#users-sudo-policy} Que fait `sudo` avant d'exécuter la commande demandée ?

::option[Il consulte la politique pour autoriser l'identité cible demandée.]{#users-sudo-policy-check .correct explanation="`sudo` autorise selon la politique puis établit les attributs cibles si la demande est permise."}
::option[Il accorde toujours à tout utilisateur un accès root illimité.]{#users-sudo-always-root explanation="L'autorisation dépend de la politique et peut refuser utilisateur ou commande."}
::option[Il remplace définitivement l'UID du compte appelant par 0.]{#users-sudo-permanent-uid explanation="`sudo` lance une commande avec les attributs cibles sans réécrire le compte."}
:::

Pour vous exercer :

1. **[Gérer les comptes Linux avec useradd, usermod et userdel](https://labex.io/fr/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - Pratiquez tout le cycle de vie des comptes.
2. **[Gérer les groupes Linux avec groupadd, usermod et groupdel](https://labex.io/fr/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - Créez des groupes et modifiez les appartenances.
3. **[Configurer les comptes et privilèges sudo](https://labex.io/fr/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Accordez des droits administratifs de façon sûre.

## Résumé

Vous savez décrire les identités Linux et la délégation administrative.

1. Identifier les comptes par UID et les groupes par GID.
2. Distinguer groupe principal et groupes supplémentaires.
3. Relier les attributs des processus aux contrôles d'accès.
4. Reconnaître l'UID 0 comme identité root traditionnelle.
5. Traiter `sudo` comme une délégation régie par une politique.
