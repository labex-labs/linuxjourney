---
lesson_id: "kernel-privilege-levels"
course_id: "kernel"
lang: "fr"
order_index: 2
title: "Niveaux de privilège"
description: "Découvrez comment les privilèges du processeur séparent l'exécution utilisateur de l'exécution de confiance du noyau."
meta_title: "Niveaux de privilège - Noyau"
meta_description: "Explorez les niveaux de privilège Linux, les modes noyau et utilisateur, les anneaux de protection et les transitions par appels système."
meta_keywords: "niveaux privilège Linux, mode noyau, mode utilisateur, anneaux protection, appels système, accès privilégié"
---

Les processeurs fournissent des modes de privilège qui limitent les instructions sensibles et les accès mémoire. Linux emploie cette frontière matérielle afin que les défaillances ordinaires des applications ne puissent pas écraser directement la mémoire du noyau ou reconfigurer les périphériques. Le noyau contrôle les transitions vers l'exécution privilégiée.

## Mode utilisateur

Un processus ordinaire s'exécute en mode utilisateur dans son espace d'adressage virtuel. Il peut calculer librement et accéder aux mappages mémoire accordés par le noyau, lesquels peuvent être vastes ; le mode utilisateur ne signifie donc pas « seulement une petite quantité de mémoire ». Il ne peut pas accéder directement à une adresse physique arbitraire, aux mappages privés d'un autre processus ou aux contrôles privilégiés du processeur.

Les tables de pages et les bits de protection imposent les accès mémoire. Si un thread référence une adresse invalide ou interdite, le processeur provoque une exception vers le noyau, qui peut résoudre un défaut de page valide ou livrer un signal comme `SIGSEGV`.

:::single-choice{#kernel-privilege-user-mode-memory} À quelle mémoire un processus en mode utilisateur peut-il normalement accéder directement ?

::option[À chaque adresse physique de la RAM et à toute la mémoire du noyau.]{#kernel-privilege-all-physical explanation="Les privilèges et la protection de la mémoire virtuelle empêchent ces accès."}
::option[À un seul octet fixe choisi au démarrage du processus.]{#kernel-privilege-one-byte explanation="Un processus peut posséder de nombreuses régions mappées tout en restant non privilégié."}
::option[Aux mappages autorisés dans son propre espace d'adressage virtuel.]{#kernel-privilege-own-mappings .correct explanation="Les protections matérielles des pages limitent le processus aux mappages établis avec les accès appropriés."}
:::

## Mode noyau

Le mode noyau autorise l'exécution d'instructions privilégiées et l'accès aux mappages protégés nécessaires à la gestion de la mémoire, l'ordonnancement, la gestion des interruptions et les pilotes. Sur x86, cette séparation Linux est couramment décrite comme le ring 0 pour le noyau et le ring 3 pour les processus utilisateur. Linux n'emploie normalement pas les rings 1 et 2 pour l'isolation ordinaire des processus.

Les autres architectures possèdent des noms et mécanismes différents, comme les niveaux d'exception. La virtualisation ajoute les relations entre hyperviseur et invités, qui ne rentrent pas dans un simple schéma à deux anneaux. L'idée essentielle est le privilège contrôlé, pas les numéros propres à x86.

:::single-choice{#kernel-privilege-x86-kernel-ring} Dans quel anneau de protection x86 le noyau Linux s'exécute-t-il normalement ?

::option[Ring 3.]{#kernel-privilege-ring-three explanation="Le ring 3 est le niveau de privilège conventionnel du mode utilisateur."}
::option[Ring 0.]{#kernel-privilege-ring-zero .correct explanation="Le noyau emploie l'anneau x86 traditionnel le plus privilégié."}
::option[Ring 7.]{#kernel-privilege-ring-seven explanation="Les anneaux de protection x86 traditionnels sont numérotés de 0 à 3."}
:::

## Transitions contrôlées

Plusieurs événements transfèrent le contrôle à un point d'entrée du noyau :

- une instruction d'appel système demande un service du noyau ;
- une exception signale une situation comme un défaut de page ou une instruction invalide ;
- une interruption matérielle signale un événement externe.

Le processeur enregistre le contexte d'exécution, change de privilège selon les mécanismes d'entrée configurés et commence à exécuter le code de confiance du noyau. Le noyau valide la demande et l'état, exécute ou refuse le travail, puis revient au mode utilisateur lorsque cela convient.

L'application ne devient pas temporairement du code du noyau. Le processeur exécute un gestionnaire du noyau pour le compte du thread, avec des piles et mappages contrôlés par le noyau.

:::single-choice{#kernel-privilege-system-call-transition} Que se produit-il pendant une transition d'appel système ?

::option[Le code utilisateur de l'application reçoit un accès illimité au ring 0.]{#kernel-privilege-user-ring-zero explanation="Seul le code de confiance du noyau s'exécute après l'entrée contrôlée."}
::option[Le processus change définitivement son UID en zéro.]{#kernel-privilege-uid-zero explanation="La transition du mode processeur ne réécrit pas les identifiants utilisateur."}
::option[Le contrôle entre dans un gestionnaire défini du noyau qui valide la demande.]{#kernel-privilege-kernel-handler .correct explanation="Le processeur change de mode par un chemin d'entrée configuré tout en préservant le contexte utilisateur pour le retour."}
:::

## Le privilège du processeur n'est pas l'identité de l'utilisateur

Une application exécutée comme utilisateur Linux `root` reste normalement en mode utilisateur. L'UID 0 influence les contrôles d'autorisation du noyau, mais ne permet pas à ses instructions d'accéder directement à la mémoire du noyau. Inversement, le code du noyau s'exécute en mode privilégié quel que soit l'utilisateur qui a provoqué son exécution par un appel système.

Les capacités, espaces de noms, seccomp, modules de sécurité et cgroups limitent davantage ce qu'un processus peut demander. Ces règles en couches sont distinctes de la frontière matérielle entre modes utilisateur et noyau.

:::single-choice{#kernel-privilege-root-distinction} Quelle affirmation compare correctement l'identité root et le mode noyau ?

::option[Root est un identifiant de l'espace utilisateur ; le mode noyau est un privilège d'exécution du processeur.]{#kernel-privilege-credential-versus-mode .correct explanation="Un processus root formule des demandes autorisées depuis le mode utilisateur, tandis que le code de confiance du noyau effectue l'exécution privilégiée."}
::option[Chaque instruction appartenant à root s'exécute comme code chargeable du noyau.]{#kernel-privilege-root-kernel-code explanation="L'UID propriétaire ne transforme pas un exécutable en module du noyau."}
::option[Le mode noyau est un autre nom d'utilisateur stocké dans `/etc/passwd`.]{#kernel-privilege-kernel-username explanation="Les modes du processeur sont des états matériels, pas des comptes de connexion."}
:::

## Importance de la frontière

La frontière limite les dommages causés par les bogues ordinaires et fournit un point de contrôle des accès, mais les vulnérabilités du noyau et les modules malveillants peuvent la vaincre. Maintenez noyau et micrologiciel à jour par des canaux fiables, réduisez le code privilégié et évitez les modules non fiables.

Les problèmes d'exécution spéculative et les canaux auxiliaires montrent également que l'isolation matérielle exige des mesures d'atténuation permanentes ; « un anneau différent » est un fondement, pas une preuve de sécurité complète.

:::single-choice{#kernel-privilege-boundary-limit} La séparation des modes utilisateur et noyau garantit-elle la sécurité complète du système ?

::option[Oui ; les vulnérabilités du noyau ne peuvent pas toucher les processus utilisateur.]{#kernel-privilege-no-kernel-vulns explanation="Une vulnérabilité du noyau peut compromettre tout le système."}
::option[Non ; les défauts du code privilégié et les canaux auxiliaires peuvent toujours franchir les frontières prévues.]{#kernel-privilege-not-complete .correct explanation="La séparation des modes réduit la surface d'attaque, mais doit s'accompagner d'un code du noyau correct et de mesures supplémentaires."}
::option[Oui ; les modes matériels suppriment le besoin de règles de contrôle d'accès.]{#kernel-privilege-no-policy explanation="Les identifiants et règles de sécurité restent essentiels au partage autorisé des ressources."}
:::

## Résumé

Vous savez maintenant distinguer le privilège matériel d'exécution de l'autorité des comptes Linux.

1. Relier le mode utilisateur aux espaces d'adressage virtuels protégés.
2. Relier le mode noyau aux instructions et mappages privilégiés.
3. Considérer les appels système, exceptions et interruptions comme des entrées contrôlées.
4. Distinguer l'autorisation de l'UID 0 de l'exécution en ring 0.
5. Voir les modes de privilège comme une couche d'une conception de sécurité plus large.
