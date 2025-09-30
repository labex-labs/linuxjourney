---
index: 5
lang: "pt"
title: "Configuração de DNS"
meta_title: "Configuração de DNS - DNS"
meta_description: "Aprenda sobre servidores DNS populares para Linux como BIND, DNSmasq e PowerDNS. Descubra o melhor servidor DNS para a configuração da sua rede com este guia para iniciantes."
meta_keywords: "Linux DNS, BIND, DNSmasq, PowerDNS, configuração de servidor DNS, rede Linux, tutorial DNS, iniciante"
---

## Lesson Content

Não vamos abordar a configuração de um servidor DNS, pois isso seria um tutorial bastante longo. Em vez disso, aqui está uma lista de comparação rápida de servidores DNS populares para usar com Linux.

### BIND

O servidor DNS mais popular na Internet, é o padrão usado com as distribuições Linux. Foi originalmente desenvolvido na Universidade da Califórnia em Berkeley, daí o nome BIND (Berkeley Internet Name Domain). Se você precisa de poder e flexibilidade completos, não há como errar com o BIND.

### DNSmasq

Leve e muito mais fácil de configurar do que o BIND. Se você quer simplicidade e não precisa de todos os recursos do BIND, use o DNSmasq. Ele vem com todas as ferramentas necessárias para configurar DHCP e DNS, recomendado para uma rede menor.

### PowerDNS

Completo e semelhante ao BIND, ele oferece um pouco mais de flexibilidade com as opções. Ele lê informações de vários bancos de dados, como MySQL, PostgreSQL, etc., para uma administração mais fácil. Só porque o BIND tem sido a maneira como fazemos as coisas, não significa que deva permanecer assim.

Esta não é uma lista completa, mas deve dar uma ideia de onde procurar se você estiver configurando seu próprio servidor DNS.

## Exercise

A prática leva à perfeição! Aqui estão alguns laboratórios práticos para reforçar sua compreensão de DNS no Linux:

1. **[Consultar Registros DNS no Linux com dig e nslookup](https://labex.io/pt/labs/comptia-query-dns-records-in-linux-with-dig-and-nslookup-592796)** - Aprenda a usar ferramentas essenciais de linha de comando como `dig` e `nslookup` para consultar vários tipos de registros DNS e solucionar problemas de resolução de DNS.
2. **[Configurar um Servidor DNS Autoritativo Local no Linux](https://labex.io/pt/labs/comptia-set-up-a-local-authoritative-dns-server-on-linux-592803)** - Ganhe experiência prática instalando e configurando o `bind9` para configurar seu próprio servidor DNS autoritativo local, definindo zonas e testando a resolução.

Esses laboratórios o ajudarão a aplicar os conceitos em cenários reais e a construir confiança com o gerenciamento de DNS no Linux.

## Quiz Question

Qual é o servidor DNS de fato para Linux?

## Quiz Answer

BIND
