---
lesson_id: "etc-hosts"
course_id: "dns"
lang: "fr"
order_index: 4
title: "/etc/hosts"
description: "Découvrez comment les correspondances locales du fichier hosts participent à la résolution Linux et comment les tester sans risque."
meta_title: "/etc/hosts - DNS"
meta_description: "Explorez l'utilité du fichier /etc/hosts sous Linux. Apprenez comment ce fichier mappe les noms d'hôtes aux adresses IP, son rôle dans la résolution DNS locale et comment le configurer sur des systèmes comme Debian. Un guide de la configuration etc hosts linux."
meta_keywords: "/etc/hosts, etc hosts linux, debian hosts, etc host linux, etc hosts, réseau Linux, mappage nom d'hôte, résolution DNS"
---

`/etc/hosts` fournit des correspondances statiques entre adresses et noms à la pile locale de services de noms. Il est utile pour les noms de bouclage, les dépendances d'amorçage et les tests précisément délimités, mais ne publie aucun enregistrement aux autres hôtes et ne met pas le DNS à jour.

## Lire le fichier

Une ligne commence par une adresse IPv4 ou IPv6 suivie d'un ou plusieurs noms :

```text
127.0.0.1       localhost
192.0.2.25      app-test.example.net app-test
2001:db8::25    app-test-v6.example.net app-test-v6
```

Les commentaires commencent par `#`. Certains outils considèrent conventionnellement le premier nom comme canonique et les suivants comme des alias, mais le comportement varie selon les applications et API. Évitez les entrées en double ou contradictoires pour un même nom.

:::single-choice{#hosts-file-entry-order}
Quel élément apparaît en premier sur une ligne normale de correspondance dans `/etc/hosts` ?

::option[Une adresse IP.]{#hosts-file-address-first .correct explanation="Un ou plusieurs noms suivent l'adresse sur la même ligne."}
::option[Un TTL d'enregistrement DNS.]{#hosts-file-ttl-first explanation="Les entrées du fichier hosts n'utilisent pas les champs TTL du DNS."}
::option[Un numéro de port de transport.]{#hosts-file-port-first explanation="Le fichier associe des noms et des adresses, pas des ports applicatifs."}
:::

## Ordre du résolveur

La configuration Name Service Switch, généralement `/etc/nsswitch.conf`, détermine comment les fonctions du résolveur système combinent `files`, le DNS, les systèmes multicast et d'autres sources. Une ligne courante est :

```text
hosts: files dns
```

Ne supposez pas que les fichiers précèdent toujours le DNS sans examiner cette politique. Des applications peuvent aussi utiliser leurs propres bibliothèques DNS, caches, mandataires ou résolveurs chiffrés et ne pas suivre le chemin du système.

:::single-choice{#hosts-file-nss-order}
Qu'est-ce qui détermine si le résolveur système consulte `/etc/hosts` avant le DNS ?

::option[L'ordre alphabétique des noms de fichiers dans `/etc`.]{#hosts-file-alphabetical explanation="L'ordre de liste du système de fichiers ne définit pas la politique des services de noms."}
::option[L'ordre des sources dans la politique Name Service Switch.]{#hosts-file-nss-policy .correct explanation="La ligne de base `hosts:` contrôle l'ordre normal des sources du résolveur libc."}
::option[La taille de la fenêtre TCP de la destination.]{#hosts-file-tcp-window explanation="Le contrôle de flux du transport n'a aucun rapport avec la recherche locale de noms."}
:::

## Tester par le résolveur système

Utilisez `getent` pour exercer le chemin configuré du service de noms :

```bash
$ getent ahosts app-test.example.net
```

`dig` interroge directement le DNS et ne rapporte normalement pas les correspondances de `/etc/hosts`. Cette différence est utile : une réussite de `getent` associée à un échec de `dig` peut signaler une source locale ou une différence de politique.

:::single-choice{#hosts-file-getent-versus-dig}
Quel outil convient le mieux pour vérifier si la résolution normale du système voit une entrée du fichier hosts ?

::option[`dig`, car il lit toujours `/etc/hosts` en premier.]{#hosts-file-dig-first explanation="Dig envoie des requêtes DNS et contourne le chemin de recherche dans le fichier hosts."}
::option[`getent ahosts`, car il utilise les sources de services de noms configurées.]{#hosts-file-getent .correct explanation="Cette commande reflète le chemin du résolveur employé par de nombreuses applications natives."}
::option[`ip route flush`, car il reconstruit tous les noms.]{#hosts-file-flush-route explanation="Effacer les routes est destructeur et sans rapport avec la recherche dans le fichier hosts."}
:::

## Modifier sans risque

Conservez les entrées nécessaires de localhost et d'identité de l'hôte, validez l'adresse voulue et effectuez une modification récupérable avec un éditeur privilégié. N'écrasez pas un véritable domaine public pour un test improvisé : cela peut rediriger des identifiants ou du trafic applicatif. Utilisez un nom de test dédié et retirez l'entrée après l'expérience.

Après la modification, testez l'application exacte, car elle peut conserver un cache ou utiliser un autre résolveur. Documentez les surcharges persistantes afin qu'elles ne survivent pas silencieusement à leur objectif.

:::single-choice{#hosts-file-test-name}
Pourquoi utiliser un nom de test dédié plutôt que de surcharger le nom d'un service public ?

::option[Les noms publics ne peuvent pas contenir de points.]{#hosts-file-public-no-dots explanation="Les noms de domaine contiennent couramment plusieurs étiquettes séparées par des points."}
::option[Les noms dédiés créent automatiquement des zones DNS faisant autorité.]{#hosts-file-auto-zone explanation="Une entrée hosts reste locale et ne publie aucune zone."}
::option[Cela réduit le risque de rediriger du véritable trafic ou des identifiants.]{#hosts-file-reduce-redirection .correct explanation="Une surcharge locale peut toucher chaque client du résolveur système qui utilise ce nom public."}
:::

## Configuration des serveurs de résolution

`/etc/resolv.conf` contient traditionnellement les réglages des résolveurs DNS, mais il est souvent généré par NetworkManager, systemd-resolved, DHCP ou un autre gestionnaire. Inspectez les liens symboliques et commentaires, puis modifiez la configuration propriétaire plutôt qu'une sortie générée qui sera écrasée.

:::single-choice{#hosts-file-resolv-owner}
Que faut-il faire avant de modifier `/etc/resolv.conf` ?

::option[Supprimer `/etc/hosts` et toutes les routes réseau.]{#hosts-file-delete-state explanation="Ces changements destructeurs sont sans rapport et peuvent supprimer la connectivité."}
::option[Supposer que toutes les distributions y stockent directement les réglages permanents.]{#hosts-file-assume-direct explanation="De nombreux systèmes génèrent ce fichier dynamiquement ou le lient à un stub géré."}
::option[Déterminer si un autre service le génère et le gère.]{#hosts-file-identify-resolver-owner .correct explanation="Les changements persistants de serveurs DNS appartiennent à la configuration du gestionnaire actif."}
:::

## Résumé

Vous savez maintenant utiliser `/etc/hosts` comme source locale et contrôlée du résolveur.

1. Écrire des correspondances commençant par l'adresse, avec des noms et alias choisis.
2. Inspecter l'ordre Name Service Switch au lieu de le présumer.
3. Tester le résolveur système avec `getent` et le DNS séparément avec `dig`.
4. Employer des noms temporaires dédiés et vérifier l'application réelle.
5. Changer les serveurs de résolution par leur configuration propriétaire.
