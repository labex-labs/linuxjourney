---
lesson_id: "ubuntu"
course_id: "getting-started"
lang: "fr"
order_index: 5
title: "Ubuntu"
description: "Découvrez comment Ubuntu associe les fondations de Debian à des options accessibles pour le bureau, les serveurs et les versions."
meta_title: "Ubuntu Linux"
meta_description: "Découvrez Ubuntu Linux, les raisons de sa popularité, son modèle de publication, sa gestion des paquets et ses usages sur bureau et serveur."
meta_keywords: "Ubuntu Linux, distribution Ubuntu, versions Ubuntu, gestion paquets Ubuntu, Ubuntu basé sur Debian, distribution Linux"
---

## Qu'est-ce qu'Ubuntu ?

Ubuntu est l'une des distributions Linux les plus utilisées. Développée par Canonical, elle repose sur Debian et est connue pour sa conception accessible, sa vaste communauté d'utilisateurs ainsi que sa large prise en charge matérielle et logicielle.

Ubuntu est devenue un point de départ courant pour les personnes qui veulent apprendre Linux sans commencer par une configuration plus manuelle ou avancée. Elle est employée sur les ordinateurs personnels, systèmes de développement, plateformes cloud et serveurs, ce qui lui donne une portée que peu d'autres distributions égalent.

:::single-choice{#identify-ubuntu-base}
Quelle distribution fournit les fondations d'Ubuntu ?

::option[La distribution Debian]{#debian-base .correct explanation="Ubuntu est construit à partir de Debian et hérite d'une grande partie de son approche des paquets. Ubuntu ajoute ensuite ses propres versions, réglages par défaut et modèle d'assistance."}
::option[La distribution Fedora]{#ubuntu-fedora-base explanation="Fedora appartient à l'écosystème Red Hat et ne sert pas de base à Ubuntu. Ubuntu fait partie de la famille Debian."}
::option[La distribution Arch]{#ubuntu-arch-base explanation="Arch Linux est une distribution distincte, avec son propre système de paquets et modèle de publication. Ubuntu est basé sur Debian."}
:::

## Pourquoi Ubuntu est populaire

Ubuntu cherche à rendre Linux pratique au quotidien. Elle propose un programme d'installation soigné, une documentation solide, des versions prévisibles et un vaste écosystème de tutoriels et d'assistance tierce. Pour beaucoup, cette combinaison en fait l'une des distributions Linux les plus faciles à vivre.

Ubuntu est également très visible parce qu'elle fonctionne dans de nombreux environnements : ordinateurs portables et de bureau, machines virtuelles, serveurs et plateformes cloud. Cette vaste adoption renforce sa réputation de distribution Linux généraliste.

:::single-choice{#recognize-beginner-support}
Quelle qualité d'Ubuntu aide le plus directement un débutant à résoudre ses problèmes ?

::option[La compilation manuelle obligatoire de chaque programme installé]{#manual-compilation explanation="Ubuntu fournit normalement des logiciels empaquetés au lieu d'exiger leur compilation manuelle. Ce travail supplémentaire ne simplifierait pas le dépannage."}
::option[Une documentation abondante et une grande communauté d'utilisateurs]{#documentation-community .correct explanation="La documentation et les discussions de la communauté offrent aux débutants de nombreuses sources d'explications et d'aide au dépannage, ce qui facilite l'apprentissage."}
::option[Des indications limitées, réservées aux administrateurs expérimentés]{#limited-guidance explanation="La visibilité d'Ubuntu tient notamment aux nombreuses ressources disponibles pour tous les niveaux. Réserver l'aide aux experts nuirait à son accessibilité."}
:::

## Ubuntu et Debian

Ubuntu est une distribution basée sur Debian : elle hérite donc d'une grande partie de son modèle de gestion et d'empaquetage des logiciels. Si vous apprenez le fonctionnement d'`apt` dans Ubuntu, ces connaissances vous aideront à comprendre les autres systèmes issus de Debian.

Ubuntu n'est toutefois pas simplement « Debian avec un bureau ». Elle possède son propre calendrier de publication, ses réglages par défaut, son modèle d'assistance et son écosystème. Pour la comparer, consultez [Choisir une distribution Linux](https://labex.io/fr/lesson/choosing-a-linux-distribution) ou découvrez [Debian](https://labex.io/fr/lesson/debian).

## Versions d'Ubuntu

Ubuntu emploie deux grands types de versions. Une nouvelle version paraît tous les six mois et, tous les deux ans, l'une d'elles devient une version Long Term Support, ou LTS. Les versions LTS sont souvent choisies pour les postes de travail, les stations professionnelles et les serveurs qui ont besoin d'une base plus stable.

Ce modèle explique une partie de l'attrait d'Ubuntu. Les utilisateurs qui recherchent une base fiable choisissent souvent une LTS, tandis que ceux qui veulent des fonctionnalités plus récentes peuvent employer les versions intermédiaires publiées plus rapidement.

:::single-choice{#choose-ubuntu-lts}
Quel type de version Ubuntu convient le mieux à un système qui exige une base prévisible et durable ?

::option[Une version intermédiaire]{#interim-release explanation="Les versions intermédiaires paraissent plus souvent et donnent plus vite accès aux nouveautés. Leur assistance plus courte ne correspond pas à la priorité indiquée."}
::option[Une version LTS]{#lts-release .correct explanation="Les versions LTS sont destinées à une assistance plus longue et couramment choisies pour les systèmes qui privilégient une base fiable."}
::option[Une mise à jour de paquet]{#package-update explanation="Une mise à jour de paquet modifie un logiciel dans une version installée. Ce n'est pas l'un des deux types de versions du système Ubuntu."}
:::

## Gestion des paquets

En tant que système issu de Debian, Ubuntu emploie le format `.deb` et le gestionnaire de paquets `apt` pour installer, mettre à jour et supprimer les logiciels. Les utilisateurs accèdent ainsi à un immense écosystème et à une méthode familière en ligne de commande.

La gestion des paquets est l'une des forces pratiques d'Ubuntu, car elle associe les outils Debian éprouvés à un environnement logiciel vaste et abondamment documenté.

:::single-choice{#identify-ubuntu-package-tool}
Quel élément est l'outil de gestion des paquets employé pour installer des logiciels dans Ubuntu ?

::option[`.deb`]{#deb-format explanation="`.deb` désigne le format de paquets des systèmes issus de Debian. Ce n'est pas l'outil en ligne de commande qui les gère."}
::option[`LTS`]{#lts-label explanation="LTS désigne une version à assistance longue. Il n'installe ni ne gère les paquets logiciels."}
::option[`apt`]{#ubuntu-apt-tool .correct explanation="Ubuntu emploie `apt` pour installer, mettre à jour et supprimer des paquets. L'outil agit sur les logiciels empaquetés au format `.deb` de Debian."}
:::

## Utilisation sur bureau et serveur

Ubuntu est employée sur les postes de travail comme sur les serveurs. Côté bureau, elle propose une expérience soignée fondée sur GNOME et des réglages par défaut relativement accessibles. Côté serveur, elle est très présente dans le développement, l'infrastructure web et les environnements cloud.

Cette polyvalence attire les utilisateurs qui souhaitent qu'une même distribution puisse accompagner leur progression, de l'apprentissage sur un ordinateur portable jusqu'aux charges de production.

## Pourquoi les débutants choisissent Ubuntu

Ubuntu est souvent recommandée aux débutants parce qu'elle est plus facile à installer et dépanner que de nombreuses autres distributions. Sa vaste base d'utilisateurs se traduit par de nombreux tutoriels, messages de forums et guides disponibles en cas de problème.

Pour ceux qui veulent une distribution accessible sans renoncer à une flexibilité à long terme, Ubuntu reste un point de départ courant.

## Pour aller plus loin

- [Ubuntu Desktop](https://ubuntu.com/desktop)
- [Ubuntu Server](https://ubuntu.com/server)
- [Cycle de publication d'Ubuntu](https://ubuntu.com/releaseendoflife)
- [Documentation des versions Ubuntu](https://documentation.ubuntu.com/project/release-team/ubuntu-releases/)

Pour poursuivre après cette introduction, nous recommandons ces cours LabEx :

1. **[Prise en main rapide de Linux](https://labex.io/fr/courses/quick-start-with-linux)** — Construisez des bases pratiques et des compétences en ligne de commande.
2. **[Linux pour les débutants](https://labex.io/fr/courses/linux-for-noobs)** — Suivez un parcours accessible pour comprendre progressivement les notions fondamentales.
3. **[Devenir administrateur système junior](https://labex.io/fr/courses/become-a-junior-system-administrator)** — Poursuivez vers les compétences pratiques d'administration une fois les bases acquises.

## Résumé

Vous savez maintenant expliquer comment Ubuntu s'appuie sur Debian tout en offrant ses propres versions et son expérience utilisateur.

1. Identifier Debian comme fondation d'Ubuntu.
2. Reconnaître les qualités d'assistance qui aident les débutants.
3. Comparer les versions LTS et intermédiaires d'Ubuntu.
4. Employer `apt` comme outil de gestion des paquets d'Ubuntu.
