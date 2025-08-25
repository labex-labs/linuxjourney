---
index: 1
lang: "pt"
title: "O que é DNS?"
meta_title: "O que é DNS? - DNS"
meta_description: "Aprenda o que é DNS e como ele traduz nomes de domínio para endereços IP. Entenda este conceito central da internet com nosso guia Linux para iniciantes."
meta_keywords: "DNS, Sistema de Nomes de Domínio, endereço IP, nome de host, rede Linux, iniciante, tutorial, guia"
---

## Lesson Content

Imagine se toda vez que você quisesse fazer uma pesquisa no Google, tivesse que digitar `http://192.78.12.4` em vez de `www.google.com`. Bem, sem o DNS ("Domain Name System"), é exatamente isso que aconteceria. O networking de baixo nível entende apenas o endereço IP bruto para identificar um host. O DNS permite que nós, humanos, acompanhemos sites e hosts por nome, em vez de um endereço IP. É como uma lista de contatos para a Internet. Se você sabe o nome de alguém, mas não sabe o número de telefone, pode simplesmente procurá-lo em sua lista de contatos.

O DNS é fundamentalmente um banco de dados distribuído de nomes de host para endereços IP. Nós gerenciamos nosso banco de dados para que as pessoas saibam como chegar ao nosso site/domínio, e em outro lugar, outra pessoa está gerenciando seu banco de dados para que outros possam chegar ao seu domínio. Esses domínios são então capazes de se comunicar e construir uma lista de contatos massiva da Internet.

Neste curso, abordaremos alguns conceitos básicos de DNS, mas esteja ciente de que DNS é um tópico exaustivo, e se você realmente quiser se aprofundar nele, precisará fazer pesquisas adicionais.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão de DNS e resolução de nomes de host:

1. **[Consultar Registros DNS no Linux com dig e nslookup](https://labex.io/pt/labs/linux-query-dns-records-in-linux-with-dig-and-nslookup)** - Aprenda a usar ferramentas essenciais do Linux como `dig` e `nslookup` para consultar vários tipos de registros DNS, ajudando você a entender como os nomes de host são resolvidos para endereços IP.
2. **[Gerenciar Resolução de Nome de Host Local no Linux](https://labex.io/pt/labs/linux-manage-local-hostname-resolution-in-linux)** - Pratique a edição do arquivo `/etc/hosts` para gerenciar a resolução de nome de host local, uma habilidade fundamental para controlar como seu sistema Linux resolve nomes sem depender de servidores DNS externos.
3. **[Configurar um Servidor DNS Autoritativo Local no Linux](https://labex.io/pt/labs/linux-set-up-a-local-authoritative-dns-server-on-linux)** - Ganhe experiência prática configurando seu próprio servidor DNS autoritativo local usando `bind9`, permitindo que você se aprofunde em como as zonas e registros DNS são gerenciados.

Esses laboratórios o ajudarão a aplicar os conceitos em cenários reais e a construir confiança com DNS e resolução de nomes de host em um ambiente Linux.

## Quiz Question

Verdadeiro ou falso: O DNS nos ajuda a encontrar endereços MAC para nomes de host?

## Quiz Answer

False
