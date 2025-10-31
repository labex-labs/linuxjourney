---
index: 4
lang: "fr"
title: "/etc/hosts"
meta_title: "/etc/hosts - DNS"
meta_description: "Explorez l'utilité du fichier /etc/hosts sous Linux. Apprenez comment ce fichier mappe les noms d'hôtes aux adresses IP, son rôle dans la résolution DNS locale et comment le configurer sur des systèmes comme Debian. Un guide de la configuration etc hosts linux."
meta_keywords: "/etc/hosts, etc hosts linux, debian hosts, etc host linux, etc hosts, réseau Linux, mappage nom d'hôte, résolution DNS"
---

## Lesson Content

Avant que votre système Linux n'interroge un serveur DNS pour résoudre un nom d'hôte, il recherche d'abord une correspondance sur la machine locale. Cette vérification initiale est une partie fondamentale du processus de résolution de noms.

### Le rôle de /etc/hosts

Le fichier principal pour cette recherche locale est `/etc/hosts`. Ce simple fichier texte contient des mappages statiques de noms d'hôtes à des adresses IP. La structure du fichier `etc hosts` est simple, chaque ligne contenant trois champs : l'adresse IP, le nom d'hôte canonique et des alias optionnels pour cet hôte.

Voici un exemple typique d'un fichier `etc host linux` :

```plaintext
pete@icebox:~$ cat /etc/hosts
127.0.0.1       localhost
127.0.1.1       icebox
```

Vous trouverez presque toujours l'adresse `localhost` mappée par défaut. Ce fichier est une fonctionnalité standard sur la plupart des distributions Linux, y compris sur les `Debian hosts`.

### Modification du fichier etc hosts linux

Vous pouvez modifier manuellement le fichier `/etc/hosts` pour créer vos propres mappages. Essayons un exemple amusant. Ajoutez la ligne suivante à votre fichier :

```plaintext
123.45.6.7  www.google.com
```

Après avoir enregistré le fichier, essayez de naviguer vers `www.google.com` dans votre navigateur web. Vous constaterez que cela ne fonctionne pas. C'est parce que nous avons mappé `www.google.com` à une adresse IP incorrecte. Puisque votre système vérifie d'abord le fichier local `/etc/hosts`, il utilise notre mappage défectueux et ne procède jamais à l'interrogation d'un serveur DNS pour trouver la bonne adresse. Pour corriger cela, supprimez simplement la ligne que vous avez ajoutée.

Bien que les systèmes plus anciens utilisaient `/etc/hosts.deny` et `/etc/hosts.allow` pour le contrôle d'accès, cette méthode est largement obsolète. Les pratiques de sécurité modernes reposent plutôt sur la configuration de règles de pare-feu pour une protection robuste.

### Configuration du serveur DNS local

Traditionnellement, le fichier `/etc/resolv.conf` était utilisé pour spécifier les serveurs de noms DNS pour les recherches. Cependant, avec les avancées dans la gestion des systèmes, ce fichier n'est souvent plus géré manuellement. Comme vous pouvez le voir dans l'exemple ci-dessous, le fichier est généré automatiquement par un autre service. Pour gérer les mappages de serveurs de noms DNS, vous devez consulter la documentation de votre distribution spécifique, car des outils comme `systemd-resolved` ou `resolvconf` s'en chargent désormais souvent.

```plaintext
# Fichier resolv.conf(5) dynamique pour le résolveur glibc(3) généré par resolvconf(8)
#     NE PAS MODIFIER CE FICHIER À LA MAIN -- VOS MODIFICATIONS SERONT ÉCRASÉES
nameserver 127.0.1.1
search localdomain
```

## Exercise

La pratique rend parfait ! Voici quelques laboratoires pratiques pour renforcer votre compréhension de la résolution de noms d'hôtes locale et des requêtes DNS :

1. **[Gérer la résolution de noms d'hôtes locale sous Linux](https://labex.io/fr/labs/comptia-manage-local-hostname-resolution-in-linux-592792)** - Entraînez-vous à modifier le fichier `/etc/hosts` pour gérer la résolution de noms d'hôtes locale, une étape clé avant les requêtes DNS.
2. **[Interroger les enregistrements DNS sous Linux avec dig et nslookup](https://labex.io/fr/labs/comptia-query-dns-records-in-linux-with-dig-and-nslookup-592796)** - Apprenez à interroger les enregistrements DNS à l'aide d'outils Linux essentiels comme `dig` et `nslookup` pour comprendre comment votre machine résout les noms externes.

Ces laboratoires vous aideront à appliquer les concepts dans des scénarios réels et à gagner en confiance avec la résolution de noms d'hôtes et le DNS.

## Quiz Question

Quel fichier est utilisé pour mapper les noms d'hôtes aux adresses IP sur nos machines ? (Veuillez répondre en anglais, en faisant attention à la casse)

## Quiz Answer

/etc/hosts
