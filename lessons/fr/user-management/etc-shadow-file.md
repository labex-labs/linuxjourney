---
index: 4
lang: "fr"
title: "/etc/shadow"
meta_title: "/etc/shadow - Gestion des utilisateurs"
meta_description: "Explorez le fichier /etc/shadow sous Linux, un composant essentiel de l'authentification des utilisateurs. Apprenez à le visualiser avec 'cat /etc/shadow' et comprenez la structure du fichier etc shadow, qui stocke les mots de passe chiffrés et les informations de politique."
meta_keywords: "etc shadow, fichier etc/shadow sous linux, cat /etc/shadow, etc shadow sous linux, /etc/shadow, authentification utilisateur, sécurité des mots de passe, administration système Linux"
---

## Lesson Content

Le fichier `/etc/shadow` est un composant essentiel dans les systèmes Linux pour stocker les informations sensibles d'authentification des utilisateurs. Contrairement au fichier `/etc/passwd` lisible par tous, il nécessite des privilèges de superutilisateur pour y accéder, offrant ainsi un emplacement sécurisé pour les données de mot de passe.

### Le rôle du fichier etc/shadow sous Linux

L'objectif principal du **fichier etc/shadow sous Linux** est de stocker les mots de passe utilisateur chiffrés et les politiques d'expiration des mots de passe. En séparant ces données sensibles des informations utilisateur générales dans `/etc/passwd`, le système améliore la sécurité. Si un utilisateur non privilégié pouvait lire les hachages de mots de passe, il pourrait tenter de les décrypter hors ligne.

### Visualiser le fichier avec cat /etc/shadow

Pour inspecter le contenu de ce fichier, vous devez utiliser une commande avec des privilèges de superutilisateur, comme `sudo`. La commande `cat /etc/shadow` est couramment utilisée à cette fin.

```bash
$ sudo cat /etc/shadow

root:MyEPTEa$6Nonsense:15000:0:99999:7:::
```

Le format de sortie du fichier **etc shadow** est une série de champs séparés par des deux-points, chaque ligne représentant un seul utilisateur.

### Comprendre la structure du fichier

Chaque ligne dans `/etc/shadow` contient neuf champs, séparés par des deux-points :

1. **Nom d'utilisateur** : Le nom de connexion de l'utilisateur.
2. **Mot de passe chiffré** : Le mot de passe utilisateur haché. Un astérisque (`*`) ou un point d'exclamation (`!`) ici signifie que le compte est verrouillé.
3. **Date du dernier changement de mot de passe** : Le nombre de jours écoulés depuis le 1er janvier 1970 où le mot de passe a été modifié pour la dernière fois. Une valeur de `0` force un changement de mot de passe à la prochaine connexion.
4. **Âge minimum du mot de passe** : Le nombre minimum de jours devant s'écouler avant que l'utilisateur puisse changer à nouveau son mot de passe.
5. **Âge maximum du mot de passe** : Le nombre maximum de jours pendant lesquels le mot de passe est valide. Après cette période, l'utilisateur doit le changer.
6. **Période d'avertissement du mot de passe** : Le nombre de jours avant l'expiration du mot de passe pendant lesquels l'utilisateur recevra un message d'avertissement.
7. **Période d'inactivité du mot de passe** : Le nombre de jours après l'expiration du mot de passe pendant lesquels le compte est désactivé.
8. **Date d'expiration du compte** : Une date absolue, exprimée en jours depuis le 1er janvier 1970, à laquelle le compte utilisateur sera désactivé.
9. **Champ réservé** : Ce champ est réservé pour une utilisation future.

Bien que le fichier `/etc/shadow` soit fondamental, la plupart des distributions modernes le complètent avec d'autres mécanismes d'authentification, tels que les Modules d'Authentification Enfichables (PAM), qui offrent des schémas d'authentification plus flexibles et avancés.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de l'authentification utilisateur et de la gestion des mots de passe sous Linux :

1. **[Gérer les comptes utilisateurs Linux avec useradd, usermod et userdel](https://labex.io/fr/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - Entraînez-vous au cycle complet de l'administration des utilisateurs, de la création et sécurisation des nouveaux comptes avec `useradd` et `passwd` à leur modification et suppression.
2. **[Configurer les comptes utilisateurs et les privilèges Sudo sous Linux](https://labex.io/fr/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Apprenez les techniques essentielles pour gérer les comptes utilisateurs et les privilèges sudo, y compris l'application des politiques de mots de passe et la sécurisation des comptes.

Ces laboratoires vous aideront à appliquer les concepts de gestion des utilisateurs et des mots de passe dans des scénarios réels et à gagner en confiance avec l'administration système Linux.

## Quiz Question

Aucune question, passez à autre chose !
