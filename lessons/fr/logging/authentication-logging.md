---
index: 5
lang: "fr"
title: "Journalisation de l'authentification"
meta_title: "Journalisation de l'authentification - Journalisation"
meta_description: "Explorez la journalisation de l'authentification Linux en examinant le fichier /var/log/auth.log. Ce guide aide les débutants à comprendre les événements de connexion des utilisateurs, les méthodes d'authentification et comment dépanner les problèmes d'accès pour une meilleure sécurité Linux."
meta_keywords: "authentification Linux, auth.log, journalisation Linux, connexion utilisateur, sécurité Linux, autorisation système, dépannage connexion, méthodes d'authentification, débutant, tutoriel, guide, journal sécurisé"
---

## Lesson Content

Sous Linux, suivre qui accède à un système et comment il le fait est crucial pour la sécurité et le dépannage. Ce processus est géré par la journalisation de l'authentification, qui enregistre tous les événements liés à l'autorisation, tels que les connexions des utilisateurs et les méthodes utilisées.

### Le fichier auth.log

Sur les systèmes basés sur Debian comme Ubuntu, le fichier principal pour suivre cette activité est `/var/log/auth.log`. Ce fichier journal contient des informations d'autorisation système, y compris les tentatives de connexion utilisateur réussies et échouées, et tous les mécanismes d'authentification qui ont été déclenchés. L'examen de ce fichier est une étape clé pour diagnostiquer les problèmes de connexion ou enquêter sur des incidents de sécurité.

Voici un extrait typique d'un fichier `auth.log` :

```plaintext
Jan 31 10:37:50 icebox pkexec: pam_unix(polkit-1:session): session opened for user root by (uid=1000)
```

### Comprendre les entrées de journal

Chaque ligne du journal fournit des détails précieux. Dans l'exemple ci-dessus :

- **`Jan 31 10:37:50`** : L'horodatage de l'événement.
- **`icebox`** : Le nom d'hôte de la machine où l'événement s'est produit.
- **`pkexec`** : Le programme qui a initié l'événement.
- **`pam_unix(polkit-1:session)`** : Le module d'authentification et le service utilisés.
- **`session opened for user root by (uid=1000)`** : L'action effectuée — une session a été ouverte pour l'utilisateur `root` par un utilisateur avec l'UID `1000`.

### Fichiers journaux alternatifs

Il est important de noter que l'emplacement des journaux d'authentification peut varier selon les distributions Linux. Par exemple, sur les systèmes basés sur Red Hat comme CentOS et Fedora, ces événements sont généralement enregistrés dans `/var/log/secure` au lieu de `/var/log/auth.log`.

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de l'authentification utilisateur et de la gestion des comptes :

1. **[Configurer les comptes utilisateurs et les privilèges Sudo sous Linux](https://labex.io/fr/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Entraînez-vous à appliquer les politiques de mots de passe, à verrouiller/déverrouiller les comptes utilisateurs, à sécuriser le compte root, et à accorder des permissions administratives, tous éléments essentiels pour comprendre la sécurité de l'authentification.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à gagner en confiance dans la gestion des utilisateurs et de la sécurité sous Linux.

## Quiz Question

Sur les systèmes basés sur Debian, quel est le nom du fichier journal utilisé pour l'authentification des utilisateurs ? Veuillez répondre en utilisant uniquement le nom de fichier. La réponse est sensible à la casse.

## Quiz Answer

auth.log
