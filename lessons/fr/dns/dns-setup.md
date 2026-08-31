---
lesson_id: "dns-setup"
course_id: "dns"
lang: "fr"
order_index: 5
title: "Configuration DNS"
description: "Apprenez à choisir, sécuriser, valider et exploiter des services DNS faisant autorité ou récursifs."
meta_title: "Configuration DNS - DNS"
meta_description: "Découvrez les serveurs DNS populaires pour Linux comme BIND, DNSmasq et PowerDNS. Découvrez le meilleur serveur DNS pour la configuration de votre réseau avec ce guide convivial pour les débutants."
meta_keywords: "Linux DNS, BIND, DNSmasq, PowerDNS, configuration de serveur DNS, réseau Linux, tutoriel DNS, débutant"
---

Un logiciel DNS doit être choisi selon son rôle et les exigences d'exploitation, et non comme un « meilleur serveur » universel. Un service faisant autorité publie des zones ; un service récursif résout et met en cache pour ses clients ; un résolveur transmetteur envoie les requêtes à un autre résolveur. Combiner ces rôles modifie la surface d'attaque.

## Choisir un rôle et une implémentation

- BIND peut fournir autorité et récursion avec une large prise en charge des normes.
- Unbound est couramment déployé comme résolveur récursif validant.
- dnsmasq offre transmission, cache et DHCP légers pour de petits réseaux maîtrisés.
- PowerDNS fournit des produits distincts pour l'autorité et la récursion, avec plusieurs systèmes de stockage.

Les capacités et paquets évoluent ; consultez la documentation officielle de la version installée. Ne déployez que le rôle nécessaire et désactivez toute récursion ou tout service de zone involontaire.

:::single-choice{#dns-setup-authoritative-role}
Quel rôle publie les enregistrements définitifs des zones qu'il sert ?

::option[Un serveur DNS faisant autorité.]{#dns-setup-authoritative .correct explanation="Il répond depuis l'autorité de zone configurée au lieu de résoudre récursivement des noms arbitraires."}
::option[Un commutateur Ethernet.]{#dns-setup-switch explanation="Un commutateur transfère des trames de couche liaison et ne publie pas de zones DNS."}
::option[Un résolveur récursif qui répond à des clients arbitraires.]{#dns-setup-stub explanation="Un stub envoie des requêtes à un service récursif et n'héberge pas de zones d'autorité."}
:::

## Concevoir avant d'installer

Définissez les zones, clients, volumes de requêtes, mécanismes de mise à jour, besoins DNSSEC, journaux, supervision, sauvegardes et récupération. Les zones d'autorité exigent des serveurs redondants et des délégations correctement enregistrées. La récursion exige un contrôle explicite des clients, une politique de cache, une connectivité vers l'amont ou la hiérarchie et une protection contre les abus.

N'exposez jamais une récursion sans restriction à Internet. Les résolveurs ouverts servent aux attaques par réflexion et consomment les ressources locales.

:::single-choice{#dns-setup-open-recursion}
Pourquoi limiter les requêtes récursives aux clients autorisés ?

::option[Le DNS récursif ne peut mettre aucun enregistrement en cache.]{#dns-setup-no-cache explanation="La mise en cache est une fonction essentielle du résolveur récursif."}
::option[Les délégations d'autorité exigent que chaque utilisateur soit root.]{#dns-setup-all-root explanation="La délégation DNS n'accorde aucun privilège du système d'exploitation."}
::option[Une récursion ouverte peut servir à l'amplification et épuiser les ressources.]{#dns-setup-recursion-abuse .correct explanation="Le contrôle d'accès réduit l'utilisation du résolveur comme infrastructure d'attaque publique."}
:::

## Valider la configuration et les zones

Utilisez les outils de vérification de syntaxe et de zones propres à l'implémentation avant le rechargement. Pour BIND :

```bash
$ named-checkconf
$ named-checkzone example.com /etc/bind/zones/db.example.com
```

Exécutez-les avec les permissions et chemins appropriés. La réussite de l'analyse ne prouve pas la délégation, la propagation du numéro de série, la chaîne DNSSEC, l'accessibilité au travers du pare-feu ni la justesse des réponses ; poursuivez avec des requêtes contrôlées.

:::single-choice{#dns-setup-zone-validation-limit}
Qu'est-ce qu'une vérification de syntaxe de zone réussie ne prouve pas ?

::option[Que la délégation et les réponses d'autorité de bout en bout fonctionnent.]{#dns-setup-not-end-to-end .correct explanation="Les données du parent, l'activation du service, la politique réseau et le chargement à l'exécution restent distincts."}
::option[Que l'outil peut analyser le texte de la zone.]{#dns-setup-parser-proves explanation="C'est précisément ce que prouve directement le vérificateur."}
::option[Que le fichier contient un champ propriétaire d'enregistrement.]{#dns-setup-record-owner explanation="L'analyse d'enregistrements valides vérifie déjà ces aspects structurels."}
:::

## Appliquer et tester sans risque

Conservez la configuration actuelle et un accès de récupération, validez, puis rechargez plutôt que redémarrer lorsque c'est possible. Interrogez directement chaque serveur d'autorité, récursion désactivée, puis comparez numéro de série SOA, ensemble NS, enregistrements positifs, noms inexistants et comportement UDP et TCP :

```bash
$ dig @192.0.2.53 example.com SOA +norecurse
$ dig @192.0.2.53 missing.example.com A +norecurse
$ dig @192.0.2.53 example.com SOA +norecurse +tcp
```

Pour la récursion, testez les réseaux clients autorisés et refusés, la validation DNSSEC, le cache et l'échec des dépendances en amont.

:::single-choice{#dns-setup-norecurse-test}
Pourquoi interroger un serveur d'autorité avec `+norecurse` ?

::option[Pour tester ses réponses d'autorité sans demander de récursion.]{#dns-setup-authority-only .correct explanation="Cette option sépare le service de zone de tout comportement récursif."}
::option[Pour retirer tous les enregistrements de sa zone.]{#dns-setup-remove-records explanation="Une requête ne modifie pas les données d'autorité."}
::option[Pour forcer toutes les réponses à passer par HTTP.]{#dns-setup-force-http explanation="L'option contrôle l'indicateur DNS demandant la récursion."}
:::

## Exploiter le service

Surveillez les échecs et temps de requêtes, le cache, les ressources, transferts de zones, numéros de série, expirations DNSSEC et l'état des délégations. Sauvegardez en sécurité les sources de configuration et le matériel de signature, puis vérifiez qu'une nouvelle instance peut charger les zones et servir les bonnes réponses. Maintenez des versions prises en charge et limitez les interfaces de contrôle, les mises à jour dynamiques et l'accès aux transferts.

:::single-choice{#dns-setup-redundancy-verification}
Que doit comprendre le test de redondance d'un DNS faisant autorité ?

::option[Interroger chaque serveur et tester le fonctionnement lorsqu'un autre est indisponible.]{#dns-setup-test-each-server .correct explanation="La présence de plusieurs enregistrements NS ne prouve pas que chaque service indépendant est joignable et à jour."}
::option[Vérifier uniquement que tous les serveurs portent des noms similaires.]{#dns-setup-hostname-similarity explanation="Les noms ne prouvent ni la synchronisation des données ni la disponibilité."}
::option[Utiliser le même processus et le même disque pour tous les serveurs annoncés.]{#dns-setup-shared-failure explanation="Un domaine de panne partagé affaiblit la redondance."}
:::

## Résumé

Vous savez maintenant concevoir un déploiement DNS autour de rôles explicites d'autorité ou de récursion.

1. Choisir le logiciel après avoir défini le rôle requis.
2. Limiter la récursion et les interfaces administratives.
3. Valider la configuration et les zones avant rechargement.
4. Tester directement autorité, déni, transport et politique client.
5. Surveiller redondance, DNSSEC, cohérence des données et récupération.
