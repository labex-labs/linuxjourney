---
lesson_id: "dns-tools"
course_id: "dns"
lang: "fr"
order_index: 6
title: "Outils DNS"
description: "Apprenez à comparer la résolution système et les requêtes DNS directes avec getent, resolvectl et dig."
meta_title: "Outils DNS - DNS"
meta_description: "Explorez les outils DNS essentiels pour Linux comme nslookup et la puissante commande dig. Ce tutoriel Linux pour débutants couvre les requêtes DNS et les techniques de dépannage DNS."
meta_keywords: "nslookup, commande dig, outils DNS, DNS Linux, dépannage DNS, recherche de serveur de noms, tutoriel Linux, Linux débutant"
---

Le dépannage DNS commence par l'identification de la couche testée. Les outils du résolveur système incluent les fichiers locaux et la politique, tandis que `dig` et `nslookup` envoient des requêtes DNS et peuvent cibler directement un serveur précis.

## Tester le résolveur système

Utilisez le chemin normal du service de noms avec :

```bash
$ getent ahosts www.example.com
```

Sur un hôte équipé de systemd-resolved, inspectez les serveurs par lien, les domaines de recherche et l'état des protocoles avec :

```bash
$ resolvectl status
$ resolvectl query www.example.com
```

Une application peut toujours utiliser sa propre bibliothèque ou un mandataire de résolution ; reproduisez donc le problème dans l'application lorsque les sorties diffèrent.

:::single-choice{#dns-tools-system-resolver} Quelle commande exerce le chemin configuré du service de noms système ?

::option[`dig @SERVER NAME` uniquement.]{#dns-tools-dig-direct explanation="Dig envoie une requête DNS et ne lit normalement pas les correspondances du fichier hosts."}
::option[`ip link set down`]{#dns-tools-link-down explanation="Cette commande interrompt l'interface au lieu de tester la résolution."}
::option[`getent ahosts NAME`]{#dns-tools-getent .correct explanation="Cette commande peut refléter `/etc/hosts`, le DNS et d'autres sources de Name Service Switch."}
:::

## Interroger avec dig

Précisez un nom et un type d'enregistrement :

```bash
$ dig www.example.com A
$ dig www.example.com AAAA
$ dig example.com MX
```

La sortie indique le serveur répondant, l'état, les indicateurs, la question, la réponse, l'autorité, les données supplémentaires, le temps de requête et les métadonnées de transport. `+short` est pratique dans les scripts, mais masque des éléments nécessaires au diagnostic.

:::single-choice{#dns-tools-record-type} Quelle requête demande des enregistrements d'adresses IPv6 ?

::option[`dig NAME AAAA`]{#dns-tools-aaaa .correct explanation="Les enregistrements AAAA contiennent des adresses IPv6."}
::option[`dig NAME MX`]{#dns-tools-mx explanation="MX demande les enregistrements des échangeurs de courrier."}
::option[`dig NAME PTR` sur le nom direct.]{#dns-tools-ptr-forward explanation="PTR s'interroge normalement au moyen d'un nom de recherche inverse."}
:::

## Choisir un serveur

Ciblez explicitement un résolveur ou un serveur d'autorité :

```bash
$ dig @192.0.2.53 www.example.com A
```

Comparez le résolveur récursif configuré, un second résolveur approuvé et chaque serveur d'autorité pour distinguer le cache de l'autorité. Un état `NOERROR` peut ne contenir aucune réponse du type demandé ; `NXDOMAIN` indique que le nom n'existe pas, et `SERVFAIL` que le serveur n'a pas pu terminer la requête.

:::single-choice{#dns-tools-noerror-empty} `NOERROR` peut-il être accompagné d'une section de réponse vide ?

::option[Oui, si le nom existe, mais ne possède pas le type d'enregistrement demandé.]{#dns-tools-noerror-nodata .correct explanation="L'état et le nombre de réponses doivent être interprétés ensemble."}
::option[Non, cet état garantit au moins un enregistrement d'adresse.]{#dns-tools-noerror-always-answer explanation="Le nom peut exister sans posséder de données du type demandé."}
::option[Non, une réponse vide est toujours une panne Ethernet.]{#dns-tools-empty-ethernet explanation="La sémantique DNS, et non le cadrage de la liaison, explique une réponse valide sans données."}
:::

## Vérifier récursion et autorité

`rd` dans la requête demande la récursion ; `ra` dans la réponse indique que le serveur la propose. `aa` signifie que la réponse fait autorité. Interrogez un serveur d'autorité avec `+norecurse` pour ne pas confondre son cache récursif avec les données de zone qu'il sert.

`dig +trace NAME` effectue son propre parcours itératif depuis les indications de la racine. Son résultat peut différer d'un résolveur de production, car il contourne son cache, sa transmission, sa politique, sa validation DNSSEC et son emplacement réseau.

:::single-choice{#dns-tools-aa-flag} Que signifie l'indicateur de réponse `aa` ?

::option[La requête a utilisé deux adresses IPv4 identiques.]{#dns-tools-two-addresses explanation="Cet indicateur n'a aucun rapport avec le nombre de réponses ou la famille d'adresses."}
::option[La réponse a été chiffrée avec des identifiants applicatifs.]{#dns-tools-aa-encrypted explanation="Les indicateurs DNS n'établissent pas un transport chiffré."}
::option[La réponse fait autorité.]{#dns-tools-authoritative-answer .correct explanation="Le serveur répondant revendique l'autorité sur les données de la réponse."}
:::

## Tester les requêtes inverses et TCP

Utilisez `-x` pour construire une requête PTR inverse :

```bash
$ dig -x 192.0.2.25
```

Testez le DNS sur TCP lorsque vous étudiez une troncature, un transfert de zone ou une différence de pare-feu :

```bash
$ dig +tcp @192.0.2.53 example.com SOA
```

Le DNS moderne peut utiliser UDP ou TCP sur le port 53 ; les deux doivent être autorisés selon les besoins. Une réponse UDP portant l'indicateur de troncature conduit les clients conformes à réessayer sur un transport adapté.

:::single-choice{#dns-tools-tcp-test} Que change `dig +tcp` ?

::option[La requête DNS utilise TCP au lieu de la tentative UDP par défaut.]{#dns-tools-use-tcp .correct explanation="Ce test aide à isoler le filtrage du transport et les réponses qui exigent un flux fiable plus grand."}
::option[La requête ne demande que des enregistrements de services TCP.]{#dns-tools-tcp-records explanation="Le type DNS demandé est précisé séparément."}
::option[La configuration du résolveur du serveur est modifiée définitivement.]{#dns-tools-tcp-persistent explanation="Une requête ne change pas les réglages du serveur."}
:::

## Résumé

Vous savez maintenant choisir l'outil DNS adapté à la couche du résolveur examinée.

1. Utiliser `getent` pour le chemin du résolveur système configuré.
2. Utiliser `dig` avec des types d'enregistrements et serveurs explicites.
3. Interpréter ensemble état, indicateurs, sections et serveur répondant.
4. Séparer le cache récursif des données d'autorité.
5. Tester les requêtes inverses et les deux transports DNS nécessaires.
