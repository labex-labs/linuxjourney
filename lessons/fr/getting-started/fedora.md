---
lesson_id: "fedora"
course_id: "getting-started"
lang: "fr"
order_index: 6
title: "Fedora"
description: "Découvrez comment Fedora fournit des technologies Linux actuelles grâce à un projet communautaire lié à Red Hat."
meta_title: "Distribution Linux Fedora"
meta_description: "Découvrez la distribution Fedora Linux, sa relation avec Red Hat, la gestion des paquets DNF et son attrait pour les développeurs et le bureau."
meta_keywords: "Fedora Linux, distribution Fedora, Fedora Red Hat, versions Fedora, gestion paquets DNF, distribution Linux"
---

## Qu'est-ce que Fedora ?

Fedora est une distribution Linux animée par la communauté et parrainée par Red Hat. Elle est connue pour fournir des technologies modernes, une expérience de bureau soignée et une solide prise en charge des développeurs et utilisateurs techniques.

Fedora a la réputation d'évoluer plus vite que les distributions prudentes tout en recherchant la qualité et la facilité d'utilisation. Cet équilibre attire les personnes qui souhaitent un système Linux moderne sans tout construire de zéro.

:::single-choice{#identify-fedora-project-model}
Quelle affirmation décrit correctement le projet Fedora ?

::option[Il s'agit d'une version abandonnée de Red Hat Enterprise Linux]{#discontinued-rhel explanation="Fedora est une distribution active avec ses propres versions. Elle se trouve en amont de RHEL et n'est pas une ancienne version de celle-ci."}
::option[Il s'agit d'une distribution entretenue par un seul fabricant de matériel]{#hardware-maintained explanation="Fedora collabore avec des fabricants, mais son développement est communautaire et parrainé par Red Hat."}
::option[Il s'agit d'un projet communautaire parrainé par Red Hat]{#community-sponsored .correct explanation="Fedora est construite par une communauté avec le parrainage et le soutien de Red Hat. Elle reste une distribution communautaire distincte."}
:::

## Ce qui distingue Fedora

Fedora adopte souvent les nouvelles fonctionnalités Linux avant les distributions orientées entreprise. Cela séduit les développeurs, contributeurs open source et utilisateurs de bureau qui souhaitent un système actuel étroitement lié aux projets en amont.

Elle est également connue pour son expérience claire dès l'installation. Fedora Workstation plaît particulièrement aux développeurs qui veulent un bureau moderne, des outils actuels et une bonne prise en charge des conteneurs, de la virtualisation et des autres méthodes de développement.

:::single-choice{#match-fedora-user}
Quel objectif d'utilisateur correspond le mieux à Fedora Workstation ?

::option[Conserver une même version d'entreprise inchangée pendant de nombreuses années]{#long-enterprise-lifecycle explanation="Un long cycle prudent correspond davantage au rôle de RHEL. Fedora suit un calendrier de versions et de mises à niveau plus rapide."}
::option[Employer des outils de développement actuels dans un système de bureau soigné]{#current-developer-desktop .correct explanation="Fedora Workstation associe un bureau sélectionné à des outils actuels pour le développement, les conteneurs et la virtualisation. Cela correspond directement à cet objectif."}
::option[Construire manuellement depuis les sources chaque composant du système]{#fedora-manual-source explanation="Fedora fournit un système complet sous forme de paquets et n'impose pas de tout construire soi-même. Cet objectif correspond à une méthode plus spécialisée."}
:::

## Fedora et Red Hat

Fedora joue un rôle important dans l'écosystème Red Hat. Les nouvelles technologies et modifications apparaissent souvent d'abord dans Fedora, puis une partie de ce travail influence Red Hat Enterprise Linux. Cette relation explique pourquoi Fedora paraît plus actuelle, tandis que RHEL est plus prudente et orientée entreprise.

Pour comparer Fedora aux options professionnelles, consultez [Red Hat Enterprise Linux](https://labex.io/fr/lesson/red-hat-enterprise-linux). Si vous comparez encore les familles, [Choisir une distribution Linux](https://labex.io/fr/lesson/choosing-a-linux-distribution) offre une vue d'ensemble.

:::single-choice{#explain-fedora-upstream-role}
Que signifie la relation en amont de Fedora avec RHEL ?

::option[Les versions de RHEL sont ensuite copiées sans changement dans Fedora]{#rhel-copied-to-fedora explanation="Cela inverse la relation. Fedora évolue plus vite et sert de source en amont plutôt que de copie ultérieure de RHEL."}
::option[Fedora et RHEL fournissent toujours des versions identiques des logiciels]{#identical-software-versions explanation="Les distributions ont des objectifs et calendriers différents. RHEL sélectionne et stabilise les technologies sans reproduire chaque version de Fedora."}
::option[Le travail développé dans Fedora peut ensuite influencer RHEL]{#fedora-influences-rhel .correct explanation="Fedora intègre plus tôt les technologies récentes. Une partie de ce travail contribue ensuite à la plateforme d'entreprise de Red Hat."}
:::

## Versions de Fedora

Fedora suit un cycle régulier, avec deux versions majeures la plupart des années et environ treize mois d'assistance pour chacune. Par rapport aux distributions prudentes, Fedora fournit généralement des noyaux, environnements de bureau et outils de développement plus récents à un rythme plus rapide.

Elle convient donc aux personnes qui veulent des logiciels à jour, mais préfèrent une distribution Linux organisée et généraliste à un système en publication continue plus manuel.

:::single-choice{#plan-fedora-upgrades}
Quelle maintenance un utilisateur de Fedora doit-il prévoir en raison de son modèle de publication ?

::option[Aucune mise à niveau de version pendant toute la durée de vie de l'ordinateur]{#no-version-upgrades explanation="Les versions de Fedora possèdent une période d'assistance limitée. Pour rester pris en charge, il faut passer aux versions suivantes au fil du temps."}
::option[Des mises à niveau régulières pour rester sur une version prise en charge]{#regular-release-upgrades .correct explanation="Les versions de Fedora se succèdent assez vite et reçoivent des mises à jour pendant environ treize mois. Il faut prévoir des mises à niveau régulières."}
::option[Des changements continus de paquets sans versions distinctes du système]{#no-distinct-releases explanation="Fedora publie des versions majeures distinctes et n'est pas une distribution continue classique. Ses paquets sont actuels, mais les versions comptent toujours."}
:::

## Gestion des paquets

Fedora emploie le format RPM et le gestionnaire de paquets DNF pour installer, mettre à jour et supprimer les logiciels. DNF est un élément central de l'expérience Fedora et l'un des principaux outils qui maintiennent le système à jour.

La gestion des paquets y est directe et s'inscrit naturellement dans la grande famille de systèmes Red Hat.

:::single-choice{#identify-fedora-package-tool}
Quel outil Fedora emploie-t-elle pour la gestion des paquets de haut niveau ?

::option[APT]{#fedora-apt-tool explanation="APT est associé aux distributions basées sur Debian. Fedora appartient à la famille RPM et emploie DNF."}
::option[DNF]{#fedora-dnf-tool .correct explanation="DNF installe, met à jour et supprime les paquets des dépôts Fedora. Ceux-ci reposent sur le format RPM."}
::option[Pacman]{#fedora-pacman-tool explanation="Pacman est le gestionnaire de paquets d'Arch Linux. L'outil de haut niveau de Fedora est DNF."}
:::

## Usages courants

Fedora est souvent employée sur les stations de développement, les postes techniques et les ordinateurs portables. Elle attire particulièrement les personnes qui veulent un environnement Linux moderne pour la programmation, les conteneurs, les machines virtuelles et le travail général de bureau.

Fedora peut aussi servir sur des serveurs, mais son identité la plus forte reste généralement celle d'une distribution actuelle et favorable aux développeurs.

## Fedora convient-elle aux débutants ?

Fedora peut convenir aux débutants, mais correspond généralement mieux aux utilisateurs à l'aise avec un système qui évolue assez vite. Elle est plus accessible que les distributions très manuelles, mais peut sembler moins prudente que Debian ou moins centrée sur les débutants qu'Ubuntu ou Linux Mint.

Pour ceux qui souhaitent une distribution moderne et acceptent d'apprendre en chemin, Fedora est une excellente possibilité.

## Pour aller plus loin

- [Fedora Workstation](https://fedoraproject.org/workstation/)
- [Documentation Fedora](https://docs.fedoraproject.org/)
- [Cycle de vie des versions Fedora](https://docs.fedoraproject.org/en-US/releases/lifecycle/)
- [Groupe de travail Fedora Workstation](https://docs.fedoraproject.org/en-US/workstation-working-group/)

Pour acquérir de véritables compétences après cette découverte, nous recommandons les cours LabEx suivants :

1. **[Prise en main rapide de Linux](https://labex.io/fr/courses/quick-start-with-linux)** — Étudiez les bases qui s'appliquent à de nombreuses distributions.
2. **[Pratique des commandes Linux en ligne](https://labex.io/fr/courses/linux-basic-commands-practice-online)** — Renforcez les habitudes de ligne de commande utiles au quotidien.
3. **[Gestion des paquets avec RPM et DNF](https://labex.io/fr/courses/rpm-and-dnf-package-management)** — Exercez-vous aux concepts de gestion des paquets RPM et DNF.

## Résumé

Vous savez maintenant expliquer la place de Fedora comme distribution actuelle et communautaire dans l'écosystème Red Hat.

1. Décrire le modèle communautaire et de parrainage de Fedora.
2. Reconnaître les utilisateurs et méthodes pris en charge par Fedora Workstation.
3. Expliquer la relation en amont entre Fedora et RHEL.
4. Prévoir les mises à niveau régulières des versions de Fedora.
5. Identifier DNF comme outil de gestion des paquets de Fedora.
