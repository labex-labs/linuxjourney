---
index: 6
lang: "fr"
title: "Outils de Gestion des Utilisateurs"
meta_title: "Outils de Gestion des Utilisateurs - Gestion des Comptes"
meta_description: "Maîtrisez la gestion des utilisateurs Linux avec des outils essentiels en ligne de commande. Ce guide couvre l'utilisation de useradd, userdel et passwd pour gérer les comptes sous Linux, idéal pour les débutants."
meta_keywords: "gestion utilisateurs linux, outil ligne de commande gestion comptes linux, useradd, userdel, passwd, comptes linux, gérer utilisateurs linux"
---

## Lesson Content

Bien que de nombreux environnements d'entreprise s'appuient sur des systèmes dédiés pour la gestion des identités, comprendre les fondamentaux de la **gestion des utilisateurs Linux** directement sur une seule machine est une compétence cruciale. Plusieurs utilitaires servent de **l'outil en ligne de commande pour gérer les comptes sous Linux**, permettant une administration efficace depuis le terminal.

### Ajout d'utilisateurs

Pour créer un nouvel utilisateur, vous pouvez utiliser la commande `useradd`. C'est un utilitaire de bas niveau qui crée un nouveau compte utilisateur basé sur les valeurs par défaut trouvées dans `/etc/default/useradd`. Bien que certains systèmes proposent également `adduser`, un script plus interactif et convivial, `useradd` est la norme universelle.

```bash
sudo useradd bob
```

L'exécution de cette commande ajoute une entrée pour l'utilisateur "bob" dans le fichier `/etc/passwd`, configure les appartenances aux groupes par défaut et crée une entrée correspondante dans le fichier `/etc/shadow` pour stocker le mot de passe en toute sécurité.

### Suppression d'utilisateurs

Pour supprimer un compte utilisateur, vous pouvez utiliser la commande `userdel`. Cette commande inverse efficacement les modifications apportées par `useradd` en supprimant les entrées de l'utilisateur des fichiers de compte système.

```bash
sudo userdel bob
```

Par défaut, cette commande peut ne pas supprimer le répertoire personnel de l'utilisateur. Vous pouvez utiliser l'indicateur `-r` (`userdel -r bob`) pour vous assurer que le répertoire personnel et la boîte aux lettres sont également supprimés.

### Modification des mots de passe

La commande `passwd` est utilisée pour définir ou modifier le mot de passe d'un utilisateur. Un utilisateur normal peut exécuter cette commande pour changer son propre mot de passe. L'utilisateur root peut l'exécuter pour changer le mot de passe de n'importe quel utilisateur.

```bash
passwd bob
```

Lorsqu'elle est exécutée par un administrateur, le système demandera un nouveau mot de passe pour l'utilisateur spécifié sans demander l'ancien. C'est une tâche fondamentale dans la **gestion des utilisateurs Linux**.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la gestion des utilisateurs et des comptes sous Linux :

1. **[Gérer les comptes utilisateurs Linux avec useradd, usermod et userdel](https://labex.io/fr/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - Entraînez-vous au cycle de vie complet de l'administration des utilisateurs, de la création et de la sécurisation des nouveaux comptes à leur modification et suppression.
2. **[Gérer les groupes Linux avec groupadd, usermod et groupdel](https://labex.io/fr/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - Acquérir une expérience pratique avec les utilitaires en ligne de commande essentiels pour l'administration des groupes, y compris l'ajout, la modification et la suppression de groupes.
3. **[Configurer les comptes utilisateurs et les privilèges Sudo sous Linux](https://labex.io/fr/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Apprenez les techniques essentielles pour gérer les comptes utilisateurs et les privilèges sudo afin d'améliorer la sécurité d'un système Linux.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à gagner en confiance dans la gestion des utilisateurs et des groupes sous Linux.

## Quiz Question

Quelle commande est utilisée pour changer un mot de passe ? Veuillez répondre avec le nom de la commande en lettres minuscules anglaises uniquement.

## Quiz Answer

passwd
