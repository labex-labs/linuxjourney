---
lesson_id: "network-manager"
course_id: "network-config"
lang: "fr"
order_index: 4
title: "Gestionnaire de réseau"
description: "Découvrez comment NetworkManager distingue les périphériques, les profils de connexion persistants et l’état d’exécution actif."
meta_title: "Gestionnaire de réseau - Configuration réseau"
meta_description: "Découvrez le rôle du démon NetworkManager dans la gestion moderne des réseaux Linux et apprenez à examiner et configurer les connexions avec nmcli."
meta_keywords: "NetworkManager, nm-tool, nmcli, gestionnaire réseau Linux, NetworkManager Linux, gestion réseau Linux, configuration réseau, réseau Linux"
---

NetworkManager gère les périphériques réseau et active des profils de connexion sur de nombreux postes de travail et serveurs Linux. Il n’est pas universel : vérifiez qu’il contrôle bien l’interface visée avant d’utiliser `nmcli` pour modifier la configuration.

## Périphériques et connexions

Un périphérique est une interface du noyau telle que `enp1s0` ou `wlan0`. Une connexion est un profil enregistré qui contient des paramètres IPv4, IPv6, DNS, Wi-Fi, de routage et d’autres réglages. Un périphérique peut posséder plusieurs profils, mais un seul profil applicable est normalement actif à la fois.

```bash
$ nmcli device status
$ nmcli connection show
$ nmcli connection show --active
```

:::single-choice{#networkmanager-device-profile}
Qu’est-ce qu’un profil de connexion NetworkManager ?

::option[Un connecteur physique soudé à la carte réseau.]{#networkmanager-physical-connector explanation="Il s’agit d’un composant matériel, et non d’un profil NetworkManager."}
::option[Un ensemble de paramètres enregistré qui peut être activé sur un périphérique.]{#networkmanager-stored-settings .correct explanation="Les profils conservent la configuration indépendamment de l’objet d’interface du noyau."}
::option[Un paquet capturé dans chaque flux actif.]{#networkmanager-packet-capture explanation="Les profils décrivent la configuration et ne contiennent pas tout le trafic."}
:::

## Examiner l’état effectif

Affichez le profil actif et les détails du périphérique :

```bash
$ nmcli -f GENERAL,IP4,IP6 device show enp1s0
$ nmcli connection show 'Wired connection 1'
```

Les paramètres du profil, les résultats DHCP à l’exécution et l’état du noyau peuvent différer. Comparez-les avec `ip address`, `ip route` et le résolveur. La commande obsolète `nm-tool` ne doit pas servir de base à une procédure actuelle.

:::single-choice{#networkmanager-active-command}
Quelle commande répertorie les profils NetworkManager actifs ?

::option[`nmcli device delete --all`]{#networkmanager-delete-all explanation="Il ne s’agit pas d’une commande d’examen, et elle suggère une opération destructive."}
::option[`nmcli connection show --active`]{#networkmanager-show-active .correct explanation="Elle limite les connexions enregistrées à celles qui sont actuellement activées."}
::option[`ip route flush table all`]{#networkmanager-flush-routes explanation="Cette commande supprime l’état du routage au lieu d’afficher les profils."}
:::

## Modifier et activer un profil

Modifiez explicitement un profil nommé, puis activez-le pendant une fenêtre de maintenance :

```bash
$ sudo nmcli connection modify 'Wired connection 1' ipv4.method auto
$ sudo nmcli connection up 'Wired connection 1'
```

La modification change les données persistantes du profil ; l’activation peut remplacer les adresses, les routes et le DNS actifs. Une modification à distance nécessite un accès à la console, une copie des paramètres d’origine et un retour en arrière temporisé indépendant. Ne comptez jamais sur la connexion en cours de modification pour transporter sa propre commande de récupération.

:::single-choice{#networkmanager-modify-versus-up}
Quelle est la différence entre `connection modify` et `connection up` ?

::option[Modify redémarre l’hôte ; up modifie le code source du DNS.]{#networkmanager-reboot-source explanation="Aucune de ces descriptions ne correspond aux commandes."}
::option[Modify change les paramètres du profil ; up active un profil.]{#networkmanager-change-activate .correct explanation="La persistance et l’activation à l’exécution sont liées, mais constituent deux opérations distinctes."}
::option[Ce sont des alias en lecture seule qui ne peuvent jamais affecter la connectivité.]{#networkmanager-readonly explanation="Dans cette procédure, les deux commandes peuvent modifier l’état."}
:::

## Vérifier et protéger les secrets

Après l’activation, vérifiez l’état du profil, les adresses et les routes du noyau, le DNS, les deux familles d’adresses ainsi que l’application prévue. Les profils Wi-Fi, VPN, 802.1X et mobiles peuvent contenir des secrets. Limitez les permissions sur les profils et évitez d’imprimer les champs secrets dans des journaux partagés ou des transcriptions du shell.

:::single-choice{#networkmanager-verification}
Qu’est-ce qui apporte une preuve plus solide que l’état « connecté » indiqué par NetworkManager ?

::option[Le nom du profil contient le mot Wired.]{#networkmanager-name-proof explanation="Une étiquette ne prouve ni la santé du chemin, ni celle du service."}
::option[La fenêtre du terminal reste ouverte.]{#networkmanager-terminal-open explanation="Un terminal peut survivre à certaines pannes partielles du réseau."}
::option[Les tests du DNS et de l’application prévue réussissent.]{#networkmanager-end-to-end .correct explanation="L’état du gestionnaire doit être mis en relation avec celui du noyau et le comportement du service."}
:::

## Résumé

Vous savez maintenant gérer les profils NetworkManager sans les confondre avec les objets d’interface.

1. Vérifier que NetworkManager contrôle le périphérique visé.
2. Distinguer les profils enregistrés de l’état d’exécution actif.
3. Examiner séparément les périphériques, tous les profils et les profils actifs.
4. Traiter la modification, l’activation, la récupération et la vérification comme des étapes distinctes.
