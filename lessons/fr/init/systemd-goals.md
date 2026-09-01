---
lesson_id: "systemd-goals"
course_id: "init"
lang: "fr"
order_index: 6
title: "Objectifs de systemd"
description: "Découvrez comment examiner, surcharger, valider, démarrer, activer et dépanner les unités de services systemd."
meta_title: "Objectifs de systemd - Init"
meta_description: "Découvrez les objectifs systemd et gérez les services Linux avec systemctl : unités, démarrage, arrêt, activation et état."
meta_keywords: "systemd, systemctl, services Linux, fichiers unités, objectifs systemd, gestion services, unités systemd"
---

`systemctl` envoie des demandes à un gestionnaire systemd. Cette leçon porte sur les unités de services système. Confirmez le nom exact de l'unité, la portée du gestionnaire, les dépendances et l'impact opérationnel avant de changer son état.

## Lire une unité de service

Une unité minimale servant d'exemple peut ressembler à ceci :

```ini
[Unit]
Description=Example worker
Wants=network-online.target
After=network-online.target

[Service]
Type=exec
ExecStart=/usr/local/bin/example-worker
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

- `[Unit]` contient la description et les relations de dépendances.
- `[Service]` définit le cycle de vie du processus et le comportement propre au service.
- `[Install]` indique aux commandes d'activation les alias ou liens de dépendances à créer ; il ne s'agit pas automatiquement d'une dépendance active à l'exécution.

`ExecStart=` n'est pas transmis par défaut à un shell. Les pipelines, redirections, variables et guillemets ne se comportent pas comme sur une ligne de commande interactive, sauf si un shell explicite est délibérément appelé.

:::single-choice{#systemd-goals-install-section} Quel est le rôle principal des directives `[Install]` comme `WantedBy=` ?

::option[Garantir que le processus du service est déjà en cours d'exécution.]{#systemd-goals-install-running explanation="L'activation à l'exécution exige un démarrage ou une autre dépendance déclenchante."}
::option[Décrire les liens ou relations créés lors de l'activation de l'unité.]{#systemd-goals-enable-links .correct explanation="Les métadonnées d'installation sont interprétées par les opérations d'activation et restent distinctes de l'état actuel du processus."}
::option[Exécuter chaque commande dans le shell interactif de l'utilisateur.]{#systemd-goals-install-shell explanation="L'analyse des commandes d'unités n'emploie pas un shell interactif par défaut."}
:::

## Examiner la configuration effective

Répertoriez les unités chargées avec :

```bash
$ systemctl list-units --type=service
```

Répertoriez les fichiers d'unités installés et leur état d'activation avec :

```bash
$ systemctl list-unit-files --type=service
```

Ces vues sont différentes : un fichier d'unité peut être activé mais inactif, actif mais désactivé, statique, généré, transitoire, masqué ou absent de l'une des listes. Examinez le contenu fusionné du fournisseur et des surcharges avec :

```bash
$ systemctl cat UNIT.service
$ systemctl show UNIT.service
```

:::single-choice{#systemd-goals-list-units-versus-files} Qu'affiche `list-unit-files` que `list-units` ne présente pas principalement ?

::option[Uniquement les processus qui consomment le plus de processeur.]{#systemd-goals-cpu-processes explanation="Le classement des ressources des processus ne relève pas de ces commandes d'inventaire des unités."}
::option[Les états d'activation des fichiers d'unités installés.]{#systemd-goals-unit-file-state .correct explanation="La commande indique si les fichiers sont activés, désactivés, statiques, masqués et d'autres états d'installation associés."}
::option[Chaque ligne jamais écrite dans le journal.]{#systemd-goals-all-journal explanation="Les requêtes du journal s'effectuent avec `journalctl`."}
:::

## Créer une surcharge locale

Employez une surcharge partielle plutôt que de modifier une unité fournie par un paquet :

```bash
$ sudo systemctl edit UNIT.service
```

Après l'enregistrement, les implémentations actuelles demandent normalement au gestionnaire de se recharger dans le cadre de cette commande. Lorsque des fichiers sont modifiés par une autre méthode, exécutez :

```bash
$ sudo systemctl daemon-reload
```

`daemon-reload` relit les définitions d'unités et reconstruit les dépendances. Il ne recharge pas la configuration des applications et ne redémarre pas les services actifs. Validez lorsque cela convient la syntaxe et les dépendances avec `systemd-analyze verify`, puis examinez l'unité fusionnée effective.

:::single-choice{#systemd-goals-daemon-reload} Que fait `systemctl daemon-reload` ?

::option[Il oblige chaque démon à relire sa configuration applicative.]{#systemd-goals-reload-all-apps explanation="Le rechargement d'une application est propre au service et distinct de la configuration du gestionnaire."}
::option[Il redémarre le noyau dans une nouvelle version.]{#systemd-goals-reload-kernel explanation="L'activation d'un noyau exige un démarrage, pas le rechargement des définitions d'unités."}
::option[Il recharge les définitions d'unités et les informations de dépendances de systemd.]{#systemd-goals-reload-manager .correct explanation="Il actualise la vue de configuration du gestionnaire sans redémarrer intrinsèquement les services."}
:::

## État d'exécution du service

Après validation de la configuration et préservation de l'accès de récupération :

```bash
$ sudo systemctl start peanut.service
$ sudo systemctl stop peanut.service
$ sudo systemctl restart peanut.service
$ sudo systemctl reload peanut.service
```

`reload` ne réussit que si l'unité définit ou prend en charge une action de rechargement. `restart` interrompt le processus et peut ne pas rétablir le service. Pour l'accès distant, le réseau, le stockage ou l'authentification, conservez une console distincte et vérifiez la configuration avant d'agir.

Contrôlez l'état et les journaux avec :

```bash
$ systemctl status peanut.service
$ systemctl is-active peanut.service
$ journalctl -u peanut.service -b
```

« Active » décrit l'état du gestionnaire, mais ne prouve pas que chaque point d'accès applicatif est sain.

:::single-choice{#systemd-goals-start-peanut} Quelle commande démarre `peanut.service` maintenant sans modifier à elle seule son activation future ?

::option[`sudo systemctl enable peanut.service`]{#systemd-goals-enable-only explanation="Enable modifie les liens d'installation, mais ne démarre pas le service sans `--now`."}
::option[`sudo systemctl start peanut.service`]{#systemd-goals-start-command .correct explanation="Start demande l'activation à l'exécution actuelle, distincte de l'activation persistante."}
::option[`sudo systemctl daemon-reload peanut.service`]{#systemd-goals-daemon-reload-unit explanation="Daemon-reload n'accepte pas d'opérande d'activation d'unité et ne démarre pas ce service."}
:::

## Activation, désactivation et masquage

Gérez les futurs liens de dépendances avec :

```bash
$ sudo systemctl enable peanut.service
$ sudo systemctl disable peanut.service
```

Enable ne démarre pas l'unité sans `--now`. Disable n'arrête pas une unité active sans `--now`. Une unité statique peut ne pas posséder de métadonnées d'installation et être tout de même activée comme dépendance d'une autre unité.

Le masquage lie l'unité à `/dev/null` et bloque son activation ordinaire, y compris par dépendance, jusqu'à ce qu'elle soit démasquée. Il est plus fort que la désactivation et peut casser les dépendants ; examinez les dépendances inverses avant de l'employer.

:::single-choice{#systemd-goals-disable-runtime} Que devient un service déjà actif après `systemctl disable UNIT` sans `--now` ?

::option[Il est immédiatement tué avec `SIGKILL`.]{#systemd-goals-disable-kills explanation="Disable seul ne demande pas l'arrêt actuel."}
::option[Son exécutable est supprimé du système de fichiers.]{#systemd-goals-disable-deletes explanation="Les opérations d'activation gèrent des liens, pas les fichiers du paquet du programme."}
::option[Il continue normalement à fonctionner tandis que les liens d'activation future sont supprimés.]{#systemd-goals-disable-keeps-running .correct explanation="L'état d'exécution et l'état d'installation sont deux dimensions distinctes."}
:::

## Vérifier le résultat du service

Après un changement, vérifiez l'état du processus, les journaux récents, les points d'écoute, les unités dépendantes, la santé de l'application et le comportement après un redémarrage contrôlé si l'activation au démarrage a changé. Employez `systemctl is-failed`, `systemctl list-dependencies` et les contrôles natifs de l'application selon les besoins.

## Résumé

Vous savez maintenant gérer un service systemd sans confondre configuration, exécution et activation.

1. Lire `[Unit]`, `[Service]` et `[Install]` selon leurs rôles distincts.
2. Comparer l'état des unités chargées à celui des fichiers d'unités installés.
3. Employer des surcharges partielles et recharger le gestionnaire après des modifications externes.
4. Démarrer, arrêter, recharger ou redémarrer seulement après examen de l'impact.
5. Considérer enable, disable et mask comme des contrôles de persistance distincts.
