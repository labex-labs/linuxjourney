---
lesson_id: "linux-security-updates"
course_id: "linux-hardening"
lang: "fr"
order_index: 7
title: "Mises à jour de sécurité"
description: "Apprenez à examiner les mises à jour de paquets disponibles et à vérifier un service après une maintenance approuvée."
meta_title: "Mises à jour de sécurité - Durcissement de Linux"
meta_description: "Apprenez à examiner les mises à jour de paquets disponibles et à vérifier un service après une maintenance approuvée."
meta_keywords: "mises à jour de sécurité, durcissement de Linux, cybersécurité, Linux Journey"
---

Une mise à jour de sécurité peut corriger un défaut dans un logiciel installé. Vérifiez d’abord la version en place et le correctif disponible pour votre système d’exploitation. Planifiez le changement en tenant compte du service utilisé par les personnes concernées.

## Examiner les mises à jour disponibles

Sur un hôte Ubuntu d’exercice, cette commande en lecture seule liste les paquets pour lesquels APT connaît une mise à niveau. Elle utilise les informations sur les paquets déjà présentes sur l’hôte.

```bash
$ apt list --upgradable
```

Pour chaque paquet listé, les données disponibles indiquent une version candidate plus récente. Consultez le bulletin de sécurité de votre distribution pour savoir si cette mise à jour contient le correctif nécessaire. Une liste vide peut aussi indiquer que les informations sont anciennes.

:::single-choice{#linux-security-updates-candidate-is-listed} Un paquet figure dans cette liste. Qu’est-ce que cela vous apprend ?

::option[La mise à jour a déjà été appliquée.]{#linux-security-updates-candidate-is-listed-a explanation="La liste indique qu’une version candidate est disponible."}
::option[APT connaît une version candidate plus récente pour le paquet installé.]{#linux-security-updates-candidate-is-listed-b .correct explanation="C’est ce qu’indiquent actuellement les données locales sur les paquets."}
::option[Toute version candidate plus récente est une mise à jour de sécurité.]{#linux-security-updates-candidate-is-listed-c explanation="Consultez le bulletin de la distribution pour savoir pourquoi cette mise à jour est proposée."}
:::

## Planifier la modification

Une modification approuvée doit préciser le service, la version cible et la période de maintenance. Certaines mises à jour prennent effet après le redémarrage du service ou de l’hôte. Prévoyez une requête de vérification et une solution de rétablissement avant de modifier l’hôte.

:::single-choice{#linux-security-updates-reboot-check} Une mise à jour de paquet corrige du code utilisé par un service qui tourne depuis longtemps. Que faut-il vérifier après l’installation ?

::option[Si le service doit redémarrer pour utiliser le code mis à jour.]{#linux-security-updates-reboot-check-a .correct explanation="Un processus actif peut encore avoir l’ancien code en mémoire."}
::option[Si la mise à jour figurait dans la liste des paquets avant l’installation.]{#linux-security-updates-reboot-check-b explanation="La disponibilité aide à planifier la maintenance. Elle ne renseigne pas sur la version chargée par un processus."}
::option[Si la liste des paquets n’affiche plus aucune mise à niveau.]{#linux-security-updates-reboot-check-c explanation="La liste des paquets peut être à jour alors qu’un processus utilise encore l’ancien code."}
:::

## Vérifier le résultat

Confirmez que la version installée correspond à la cible approuvée. Vérifiez le service par le chemin habituel des utilisateurs et notez le résultat. Si le correctif concerne un composant actif, vérifiez aussi que ce composant utilise effectivement la version mise à jour.

:::single-choice{#linux-security-updates-security-verification} Quelles observations permettent le mieux de confirmer qu’une mise à jour de service est terminée ?

::option[La commande de listage fonctionne deux fois.]{#linux-security-updates-security-verification-a explanation="Répéter la commande ne montre pas que le service fonctionne."}
::option[Le ticket de maintenance a un nouveau titre.]{#linux-security-updates-security-verification-b explanation="Le titre ne renseigne pas sur le service en cours d’exécution."}
::option[La version approuvée est en cours d’utilisation et une requête représentative réussit.]{#linux-security-updates-security-verification-c .correct explanation="Cela vérifie l’état du logiciel et le fonctionnement du service dont dépendent les utilisateurs."}
:::

## Examiner les deux informations de version

Un paquet installé et le programme qui traite les requêtes peuvent temporairement être à des versions différentes. Par exemple, l’inventaire des paquets peut afficher la version corrigée alors qu’un processus démarré avant la mise à jour tourne toujours. Appuyez-vous sur des éléments liés au processus actif pour terminer la vérification.

:::single-choice{#linux-security-updates-final-application} Quel point reste à vérifier lorsque la version installée est corrigée et que l’ancien processus tourne toujours ?

::option[Si tous les autres processus de la machine doivent être remplacés.]{#linux-security-updates-final-application-c explanation="La question concerne le service mis à jour et les exigences approuvées pour sa maintenance."}
::option[Si le programme mis à jour est celui qui traite les requêtes.]{#linux-security-updates-final-application-a .correct explanation="L’inventaire confirme les fichiers installés. Le contrôle du processus vérifie le service en activité."}
::option[Si une mise à jour du paquet était disponible.]{#linux-security-updates-final-application-b explanation="Le paquet installé indique déjà la version corrigée."}
:::

## Résumé

Vous savez maintenant suivre une mise à jour, de la version candidate à la vérification.

1. Distinguez les mises à jour disponibles des changements déjà installés.
2. Prévoyez les redémarrages et le rétablissement du service.
3. Vérifiez la version en cours d’utilisation et le comportement attendu.
